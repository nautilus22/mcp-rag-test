"""
한국 위키피디아 크롤링 및 파싱 모듈
- 위키 문서 크롤링 및 텍스트 추출
- GPT API를 이용한 요약 생성
- MCP 친화적 파일명 생성 (한글명/영어명/요약)
"""

import requests
from bs4 import BeautifulSoup
import re
import os
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import openai
from openai import OpenAI
import time
import json


class WikiDataParser:
    """위키피디아 데이터 파싱 및 처리 클래스"""
    
    def __init__(self, openai_api_key: str, output_dir: str = "data/raw/"):
        """
        초기화
        Args:
            openai_api_key: OpenAI API 키
            output_dir: 출력 디렉토리 경로
        """
        self.client = OpenAI(api_key=openai_api_key)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # 요청 헤더 설정 (위키피디아 크롤링 에티켓)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    
    def crawl_wikipedia_page(self, url: str) -> Tuple[str, str]:
        """
        위키피디아 페이지를 크롤링하여 제목과 본문을 Markdown+LaTeX 형식으로 추출
        
        Args:
            url: 위키피디아 URL
            
        Returns:
            Tuple[제목, Markdown 형식의 본문텍스트]
        """
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # 제목 추출
            title = soup.find('h1', {'class': 'firstHeading'})
            title_text = title.get_text().strip() if title else "제목없음"
            
            # 본문 추출 (mw-parser-output 클래스 내의 모든 요소들)
            content_div = soup.find('div', {'class': 'mw-parser-output'})
            if not content_div:
                return title_text, "내용을 찾을 수 없습니다."
            
            # Markdown 형식으로 변환
            markdown_content = self._convert_to_markdown(content_div, title_text)
            
            return title_text, markdown_content.strip()
            
        except Exception as e:
            print(f"크롤링 오류 ({url}): {e}")
            return "크롤링 실패", f"오류 발생: {e}"
    
    def _convert_to_markdown(self, content_div, title: str) -> str:
        """
        HTML 내용을 Markdown+LaTeX 형식으로 변환
        
        Args:
            content_div: BeautifulSoup 요소
            title: 문서 제목
            
        Returns:
            Markdown 형식의 텍스트
        """
        markdown_text = f"# {title}\n\n"
        
        # 템플릿과 네비게이션 요소 제거
        self._remove_template_elements(content_div)
        
        # 처리할 요소들을 순서대로 가져오기
        elements = content_div.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ul', 'ol', 'div'])
        
        # 제외할 섹션 감지용 플래그
        skip_content = False
        
        for element in elements:
            # 제외할 섹션인지 확인
            if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                header_text = self._clean_text(element.get_text()).lower()
                if self._should_skip_section(header_text):
                    skip_content = True
                    print(f"  📝 섹션 제외: {header_text}")
                    continue
                # 메인 섹션이면 다시 포함
                elif self._is_main_section(header_text):
                    skip_content = False
            
            # 제외할 섹션 내용이면 건너뛰기
            if skip_content:
                continue
            
            # 수식 처리
            self._process_math_elements(element)
            
            # 요소별 처리
            if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                level = int(element.name[1]) + 1  # h1은 이미 사용했으므로 +1
                if level <= 6:
                    header_text = self._clean_text(element.get_text())
                    markdown_text += f"{'#' * level} {header_text}\n\n"
            
            elif element.name == 'p':
                para_text = self._process_paragraph(element)
                if para_text and len(para_text.strip()) > 10:
                    markdown_text += f"{para_text}\n\n"
            
            elif element.name in ['ul', 'ol']:
                list_text = self._process_list(element)
                if list_text:
                    markdown_text += f"{list_text}\n\n"
            
            elif element.name == 'div' and 'mwe-math-element' in element.get('class', []):
                # 수식 블록 처리
                math_text = self._extract_math_latex(element)
                if math_text:
                    markdown_text += f"$$\n{math_text}\n$$\n\n"
        
        # 텍스트 정리
        markdown_text = re.sub(r'\n{3,}', '\n\n', markdown_text)  # 과도한 줄바꿈 제거
        markdown_text = re.sub(r'\[\d+\]', '', markdown_text)     # 각주 번호 제거
        
        return markdown_text
    
    def _remove_template_elements(self, content_div):
        """
        위키피디아 템플릿과 네비게이션 요소들을 제거
        
        Args:
            content_div: BeautifulSoup 요소
        """
        # 제거할 요소들의 클래스와 ID 목록
        removal_selectors = [
            # 네비게이션 박스
            '.navbox',
            '.navbox-inner', 
            '.navbox-group',
            '.navigation-box',
            
            # 사이드바
            '.sidebar',
            '.infobox',
            '.infobox-above',
            '.infobox-subheader',
            
            # 메시지 박스
            '.mbox',
            '.ambox',
            '.tmbox',
            '.cmbox',
            '.ombox',
            '.fmbox',
            '.dmbox',
            
            # 카테고리 박스
            '.catlinks',
            '.mw-normal-catlinks',
            
            # 기타 템플릿들
            '.hatnote',
            '.dablink',
            '.rellink',
            '.navframe',
            '.collapsible',
            
            # 편집 관련
            '.mw-editsection',
            '.mw-editsection-bracket',
            
            # 참조 관련
            '.reference',
            '.reflist',
            '.refbegin',
            '.refend',
            
            # 목차
            '.toc',
            '#toc',
            
            # 기타
            '.printfooter',
            '.mw-jump-link',
            '.visualhide',
            '.nomobile',
        ]
        
        # CSS 선택자로 요소 제거
        for selector in removal_selectors:
            elements = content_div.select(selector)
            for element in elements:
                element.decompose()
        
        # role 속성으로 제거
        navigation_elements = content_div.find_all(attrs={'role': 'navigation'})
        for element in navigation_elements:
            element.decompose()
        
        # 테이블 형태의 템플릿 제거 (특정 클래스가 있는 것들)
        tables = content_div.find_all('table')
        for table in tables:
            table_classes = table.get('class', [])
            if any(cls in ['navbox', 'infobox', 'sidebar', 'vertical-navbox', 'geography', 'biota'] 
                   for cls in table_classes):
                table.decompose()
                continue
            
            # 테이블이 너무 많은 링크를 포함하고 있으면 네비게이션 박스일 가능성이 높음
            links = table.find_all('a')
            if len(links) > 20:  # 링크가 20개 이상이면 네비게이션으로 간주
                table.decompose()
        
        # 본문 시작 전 리스트들 제거 (첫 번째 문단 이전의 리스트들)
        self._remove_pre_content_lists(content_div)
        
        print(f"  🧹 템플릿 요소 제거 완료")

    def _remove_pre_content_lists(self, content_div):
        """
        본문 시작 전의 네비게이션 리스트들을 제거
        
        Args:
            content_div: BeautifulSoup 요소
        """
        # 첫 번째 실제 문단을 찾기
        first_paragraph = None
        for p in content_div.find_all('p'):
            text = p.get_text().strip()
            if len(text) > 50:  # 충분히 긴 문단
                first_paragraph = p
                break
        
        if not first_paragraph:
            return
        
        # 첫 번째 문단 이전의 모든 리스트 제거
        current = content_div.find()
        while current and current != first_paragraph:
            next_sibling = current.find_next_sibling()
            
            if current.name in ['ul', 'ol']:
                # 리스트가 너무 많은 항목을 가지고 있으면 네비게이션으로 간주
                list_items = current.find_all('li')
                if len(list_items) > 5:
                    print(f"    🗑️ 사전 리스트 제거: {len(list_items)}개 항목")
                    current.decompose()
            
            current = next_sibling

    def _is_template_list(self, ul_element) -> bool:
        """
        리스트가 템플릿/네비게이션 요소인지 판단
        
        Args:
            ul_element: BeautifulSoup ul 요소
            
        Returns:
            템플릿 리스트이면 True
        """
        # 부모 요소들 확인
        parent = ul_element.parent
        while parent:
            if parent.get('class'):
                parent_classes = parent.get('class', [])
                if any(cls in ['navbox', 'sidebar', 'infobox', 'navigation'] 
                       for cls in parent_classes):
                    return True
            parent = parent.parent
        
        # 리스트 내용 확인
        list_items = ul_element.find_all('li')
        if len(list_items) > 10:  # 10개 이상의 항목
            # 대부분이 링크인지 확인
            link_count = len(ul_element.find_all('a'))
            if link_count / len(list_items) > 0.7:  # 70% 이상이 링크
                return True
        
        return False
    
    def _should_skip_section(self, header_text: str) -> bool:
        """
        제외할 섹션인지 확인
        
        Args:
            header_text: 소문자로 변환된 헤더 텍스트
            
        Returns:
            제외할 섹션이면 True
        """
        skip_keywords = [
            # 한글
            '같이 보기', '같이보기', '관련 항목', '관련항목',
            '각주', '주석', '참조', '출처', '참고 문헌', '참고문헌',
            '외부 링크', '외부링크', '바깥 링크', '바깥링크',
            '더 보기', '더보기', '참고 자료', '참고자료',
            '외부 고리', '바깥 고리', '읽을거리', '읽을 거리',
            
            # 영글 (혹시 영문 위키 처리할 경우)
            'see also', 'references', 'external links', 'further reading',
            'notes', 'citations', 'bibliography', 'sources',
            'related articles', 'related topics'
        ]
        
        # 정확히 일치하거나 포함하는 경우
        for keyword in skip_keywords:
            if keyword in header_text or header_text.strip() == keyword:
                return True
        
        return False
    
    def _is_main_section(self, header_text: str) -> bool:
        """
        메인 섹션인지 확인 (제외 섹션 이후에 나오는 주요 섹션)
        
        Args:
            header_text: 소문자로 변환된 헤더 텍스트
            
        Returns:
            메인 섹션이면 True
        """
        main_keywords = [
            '개요', '정의', '역사', '특징', '원리', '방법', '구조',
            '종류', '분류', '응용', '활용', '장점', '단점', '한계',
            '알고리즘', '모델', '이론', '수식', '공식'
        ]
        
        for keyword in main_keywords:
            if keyword in header_text:
                return True
        
        return False
    
    def _process_math_elements(self, element):
        """
        요소 내의 수식들을 LaTeX 형식으로 변환
        
        Args:
            element: BeautifulSoup 요소
        """
        # 인라인 수식 처리
        math_spans = element.find_all('span', class_='mwe-math-element')
        for math_span in math_spans:
            latex_text = self._extract_math_latex(math_span)
            if latex_text:
                # 인라인 수식으로 변환
                math_span.replace_with(f"${latex_text}$")
        
        # MathML 처리
        math_elements = element.find_all('math')
        for math_elem in math_elements:
            latex_text = self._mathml_to_latex(math_elem)
            if latex_text:
                math_elem.replace_with(f"${latex_text}$")
    
    def _extract_math_latex(self, math_element) -> str:
        """
        수식 요소에서 LaTeX 코드 추출
        
        Args:
            math_element: BeautifulSoup 수식 요소
            
        Returns:
            LaTeX 코드 문자열
        """
        # data-latex 속성에서 추출
        latex = math_element.get('data-latex')
        if latex:
            return latex.strip()
        
        # img 태그의 alt 속성에서 추출
        img = math_element.find('img')
        if img and img.get('alt'):
            alt_text = img.get('alt')
            # LaTeX 패턴 찾기
            latex_match = re.search(r'\\[a-zA-Z]+.*', alt_text)
            if latex_match:
                return latex_match.group().strip()
        
        # script 태그에서 LaTeX 추출
        script = math_element.find('script', type='math/tex')
        if script:
            return script.get_text().strip()
        
        # math 태그 내용을 간단한 LaTeX로 변환
        math_tag = math_element.find('math')
        if math_tag:
            return self._mathml_to_latex(math_tag)
        
        return ""
    
    def _mathml_to_latex(self, math_element) -> str:
        """
        MathML을 LaTeX로 변환 (구조적 변환 포함)
        
        Args:
            math_element: BeautifulSoup math 요소
            
        Returns:
            LaTeX 코드 문자열
        """
        try:
            return self._convert_mathml_element(math_element)
        except:
            # 변환 실패 시 기본 텍스트 변환으로 폴백
            text = math_element.get_text()
            return self._apply_symbol_replacements(text)
    
    def _convert_mathml_element(self, element) -> str:
        """
        MathML 요소를 재귀적으로 LaTeX로 변환
        
        Args:
            element: BeautifulSoup MathML 요소
            
        Returns:
            LaTeX 문자열
        """
        if element.name == 'math':
            # math 루트 요소
            return ''.join(self._convert_mathml_element(child) for child in element.children if child.name)
        
        elif element.name == 'mrow':
            # 그룹 요소
            return ''.join(self._convert_mathml_element(child) for child in element.children if child.name)
        
        elif element.name == 'mi':
            # 변수/식별자
            text = element.get_text().strip()
            return self._apply_symbol_replacements(text)
        
        elif element.name == 'mn':
            # 숫자
            return element.get_text().strip()
        
        elif element.name == 'mo':
            # 연산자
            text = element.get_text().strip()
            return self._apply_operator_replacements(text)
        
        elif element.name == 'mfrac':
            # 분수
            children = [child for child in element.children if child.name]
            if len(children) >= 2:
                numerator = self._convert_mathml_element(children[0])
                denominator = self._convert_mathml_element(children[1])
                return f"\\frac{{{numerator}}}{{{denominator}}}"
            return ''
        
        elif element.name == 'msup':
            # 위첨자 (지수)
            children = [child for child in element.children if child.name]
            if len(children) >= 2:
                base = self._convert_mathml_element(children[0])
                exponent = self._convert_mathml_element(children[1])
                return f"{base}^{{{exponent}}}"
            return ''
        
        elif element.name == 'msub':
            # 아래첨자
            children = [child for child in element.children if child.name]
            if len(children) >= 2:
                base = self._convert_mathml_element(children[0])
                subscript = self._convert_mathml_element(children[1])
                return f"{base}_{{{subscript}}}"
            return ''
        
        elif element.name == 'msubsup':
            # 위아래첨자
            children = [child for child in element.children if child.name]
            if len(children) >= 3:
                base = self._convert_mathml_element(children[0])
                subscript = self._convert_mathml_element(children[1])
                superscript = self._convert_mathml_element(children[2])
                return f"{base}_{{{subscript}}}^{{{superscript}}}"
            return ''
        
        elif element.name == 'msqrt':
            # 제곱근
            content = ''.join(self._convert_mathml_element(child) for child in element.children if child.name)
            return f"\\sqrt{{{content}}}"
        
        elif element.name == 'mroot':
            # n제곱근
            children = [child for child in element.children if child.name]
            if len(children) >= 2:
                radicand = self._convert_mathml_element(children[0])
                index = self._convert_mathml_element(children[1])
                return f"\\sqrt[{index}]{{{radicand}}}"
            return ''
        
        elif element.name == 'munder':
            # 아래 첨부
            children = [child for child in element.children if child.name]
            if len(children) >= 2:
                base = self._convert_mathml_element(children[0])
                under = self._convert_mathml_element(children[1])
                if base in [r'\sum', r'\int', r'\prod']:
                    return f"{base}_{{{under}}}"
                return f"\\underset{{{under}}}{{{base}}}"
            return ''
        
        elif element.name == 'mover':
            # 위 첨부
            children = [child for child in element.children if child.name]
            if len(children) >= 2:
                base = self._convert_mathml_element(children[0])
                over = self._convert_mathml_element(children[1])
                return f"\\overset{{{over}}}{{{base}}}"
            return ''
        
        else:
            # 기타 요소는 텍스트 변환
            text = element.get_text().strip()
            return self._apply_symbol_replacements(text)
    
    def _apply_symbol_replacements(self, text: str) -> str:
        """
        그리스 문자 및 특수 기호를 LaTeX로 변환
        
        Args:
            text: 원본 텍스트
            
        Returns:
            LaTeX 변환된 텍스트
        """
        replacements = {
            # 그리스 문자 (소문자)
            'α': r'\alpha', 'β': r'\beta', 'γ': r'\gamma', 'δ': r'\delta',
            'ε': r'\epsilon', 'ζ': r'\zeta', 'η': r'\eta', 'θ': r'\theta',
            'ι': r'\iota', 'κ': r'\kappa', 'λ': r'\lambda', 'μ': r'\mu',
            'ν': r'\nu', 'ξ': r'\xi', 'π': r'\pi', 'ρ': r'\rho',
            'σ': r'\sigma', 'τ': r'\tau', 'υ': r'\upsilon', 'φ': r'\phi',
            'χ': r'\chi', 'ψ': r'\psi', 'ω': r'\omega',
            
            # 그리스 문자 (대문자)
            'Α': r'A', 'Β': r'B', 'Γ': r'\Gamma', 'Δ': r'\Delta',
            'Ε': r'E', 'Ζ': r'Z', 'Η': r'H', 'Θ': r'\Theta',
            'Ι': r'I', 'Κ': r'K', 'Λ': r'\Lambda', 'Μ': r'M',
            'Ν': r'N', 'Ξ': r'\Xi', 'Π': r'\Pi', 'Ρ': r'P',
            'Σ': r'\Sigma', 'Τ': r'T', 'Υ': r'\Upsilon', 'Φ': r'\Phi',
            'Χ': r'X', 'Ψ': r'\Psi', 'Ω': r'\Omega',
            
            # 특수 기호
            '∞': r'\infty', '∂': r'\partial', '∇': r'\nabla',
            '∅': r'\emptyset', '∈': r'\in', '∉': r'\notin',
            '∪': r'\cup', '∩': r'\cap', '⊂': r'\subset', '⊃': r'\supset',
            '⊆': r'\subseteq', '⊇': r'\supseteq', '≡': r'\equiv',
            '≈': r'\approx', '≠': r'\neq', '≤': r'\leq', '≥': r'\geq',
            '±': r'\pm', '∓': r'\mp', '×': r'\times', '÷': r'\div',
            '·': r'\cdot', '→': r'\rightarrow', '←': r'\leftarrow',
            '↔': r'\leftrightarrow', '⇒': r'\Rightarrow', '⇐': r'\Leftarrow',
            '⇔': r'\Leftrightarrow', '∀': r'\forall', '∃': r'\exists',
            '√': r'\sqrt', '∑': r'\sum', '∏': r'\prod', '∫': r'\int'
        }
        
        for symbol, latex in replacements.items():
            text = text.replace(symbol, latex)
        
        return text
    
    def _apply_operator_replacements(self, text: str) -> str:
        """
        연산자를 LaTeX로 변환
        
        Args:
            text: 연산자 텍스트
            
        Returns:
            LaTeX 연산자
        """
        operator_map = {
            '=': '=',
            '+': '+', 
            '-': '-',
            '±': r'\pm',
            '∓': r'\mp',
            '×': r'\times',
            '·': r'\cdot',
            '÷': r'\div',
            '/': '/',
            '≤': r'\leq',
            '≥': r'\geq',
            '<': '<',
            '>': '>',
            '≠': r'\neq',
            '≈': r'\approx',
            '≡': r'\equiv',
            '∝': r'\propto',
            '∼': r'\sim',
            '→': r'\rightarrow',
            '←': r'\leftarrow',
            '↔': r'\leftrightarrow',
            '∈': r'\in',
            '∉': r'\notin',
            '⊂': r'\subset',
            '⊃': r'\supset',
            '∪': r'\cup',
            '∩': r'\cap',
            '∧': r'\land',
            '∨': r'\lor',
            '¬': r'\neg',
            '∀': r'\forall',
            '∃': r'\exists'
        }
        
        return operator_map.get(text.strip(), text)
    
    def _process_paragraph(self, paragraph) -> str:
        """
        문단을 Markdown 형식으로 처리
        
        Args:
            paragraph: BeautifulSoup p 요소
            
        Returns:
            Markdown 형식의 문단 텍스트
        """
        # 각주 및 참조 관련 요소 제거
        for sup in paragraph.find_all('sup'):
            sup.decompose()
        
        # 참조 관련 span 제거 (class가 reference인 것들)
        for ref_span in paragraph.find_all('span', class_=['reference', 'mw-ref']):
            ref_span.decompose()
        
        # 편집 링크 제거 ([편집] 등)
        for edit_span in paragraph.find_all('span', class_='mw-editsection'):
            edit_span.decompose()
        
        # 링크 처리 - 모든 링크를 텍스트만 남기고 URL 제거
        for link in paragraph.find_all('a'):
            link_text = link.get_text().strip()
            
            # 특수 링크들은 완전히 제거
            if (link.get('href', '').startswith('#cite') or 
                link.get('href', '').startswith('#ref') or 
                link.get('href', '').startswith('#note') or
                'cite_note' in link.get('href', '') or
                'cite_ref' in link.get('href', '') or
                '[편집]' in link_text or 
                'edit' in link_text.lower() or
                link.get('class') and any('reference' in str(cls) for cls in link.get('class', []))):
                link.decompose()
                continue
            
            # 모든 일반 링크는 텍스트만 남기기
            if link_text:
                link.replace_with(link_text)
            else:
                link.decompose()
        
        # 강조 처리
        for strong in paragraph.find_all(['strong', 'b']):
            text = strong.get_text()
            strong.replace_with(f"**{text}**")
        
        for em in paragraph.find_all(['em', 'i']):
            text = em.get_text()
            em.replace_with(f"*{text}*")
        
        # 텍스트 정리 및 각주 번호 패턴 제거
        text = self._clean_text(paragraph.get_text())
        
        # 각주 번호 패턴 제거 (더 정교하게)
        text = re.sub(r'\[\d+\]', '', text)  # [1], [2] 등
        text = re.sub(r'\[\d+,\s*\d+\]', '', text)  # [1, 2] 등
        text = re.sub(r'\[\d+-\d+\]', '', text)  # [1-3] 등
        text = re.sub(r'^\s*\^', '', text)  # 줄 시작의 ^ 제거
        
        return text
    
    def _process_list(self, list_element) -> str:
        """
        리스트를 Markdown 형식으로 처리
        
        Args:
            list_element: BeautifulSoup ul/ol 요소
            
        Returns:
            Markdown 형식의 리스트 텍스트
        """
        list_text = ""
        is_ordered = list_element.name == 'ol'
        
        for i, li in enumerate(list_element.find_all('li', recursive=False), 1):
            item_text = self._clean_text(li.get_text())
            if item_text:
                if is_ordered:
                    list_text += f"{i}. {item_text}\n"
                else:
                    list_text += f"- {item_text}\n"
        
        return list_text
    
    def _clean_text(self, text: str) -> str:
        """
        텍스트 정리
        
        Args:
            text: 원본 텍스트
            
        Returns:
            정리된 텍스트
        """
        # 여러 공백을 하나로
        text = re.sub(r'\s+', ' ', text)
        # 앞뒤 공백 제거
        text = text.strip()
        return text
    
    def summarize_with_gpt(self, text: str, max_length: int = 100) -> str:
        """
        GPT API를 사용하여 텍스트 요약
        
        Args:
            text: 요약할 텍스트
            max_length: 최대 요약 길이
            
        Returns:
            요약된 텍스트
        """
        try:
            # 텍스트가 너무 길면 자르기 (GPT 토큰 제한 고려)
            if len(text) > 8000:
                text = text[:8000] + "..."
            
            prompt = f"""
다음 위키피디아 문서를 {max_length}자 이내로 핵심 내용만 간단히 요약해주세요.
전문용어는 그대로 유지하고, MCP 시스템에서 파일명으로 사용할 수 있도록 명확하고 간결하게 작성해주세요.

문서 내용:
{text}

요약:
"""
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "당신은 기술 문서 요약 전문가입니다. 핵심 내용을 간결하고 정확하게 요약합니다."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=200,
                temperature=0.3
            )
            
            summary = response.choices[0].message.content.strip()
            
            # 요약 길이 체크 및 조정
            if len(summary) > max_length:
                summary = summary[:max_length-3] + "..."
            
            return summary
            
        except Exception as e:
            print(f"GPT 요약 오류: {e}")
            return "AI/ML 관련 기술 문서"
    
    def get_english_name(self, korean_name: str) -> str:
        """
        한글 키워드에 대응하는 영어명 반환
        
        Args:
            korean_name: 한글 키워드
            
        Returns:
            영어명
        """
        # 한글-영어 매핑 사전
        name_mapping = {
            "인공지능": "Artificial Intelligence",
            "기계 학습": "Machine Learning", 
            "딥 러닝": "Deep Learning",
            "합성곱 신경망": "CNN",
            "순환 신경망": "RNN", 
            "장단기 메모리": "LSTM",
            "게이트 순환 유닛": "GRU",
            "트랜스포머 (기계 학습)": "Transformer",
            "GPT (언어 모델)": "GPT",
            "알파고": "AlphaGo",
            "강화 학습": "Reinforcement Learning"
        }
        
        return name_mapping.get(korean_name, korean_name)
    
    def create_filename(self, korean_name: str, english_name: str, summary: str) -> str:
        """
        MCP 친화적 파일명 생성
        
        Args:
            korean_name: 한글명
            english_name: 영어명  
            summary: 요약
            
        Returns:
            파일명 (확장자 제외)
        """
        # 파일명에 사용할 수 없는 문자 제거
        def clean_name(name):
            return re.sub(r'[<>:"/\\|?*]', '', name).strip()
        
        korean_clean = clean_name(korean_name)
        english_clean = clean_name(english_name)
        summary_clean = clean_name(summary)
        
        # 파일명 조합: "한글명/영어명/요약"
        filename = f"{korean_clean}/{english_clean}/{summary_clean}"
        
        # 파일명 길이 제한 (255자)
        if len(filename) > 200:
            filename = filename[:200] + "..."
            
        return filename
    
    def save_document(self, title: str, content: str) -> str:
        """
        Markdown 형식의 문서를 파일로 저장
        
        Args:
            title: 문서 제목 (파일명으로 사용됨)
            content: Markdown 형식의 문서 내용
            
        Returns:
            저장된 파일 경로
        """
        # 파일명에 사용할 수 없는 문자 제거
        clean_title = re.sub(r'[<>:"/\\|?*]', '', title).strip()
        
        # 파일 경로 생성 (.md 확장자 사용)
        file_path = self.output_dir / f"{clean_title}.md"
        
        # Markdown 메타데이터 추가
        full_content = f"""---
title: {title}
type: 위키피디아 문서
format: markdown
---

{content}"""
        
        # 파일 저장
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        return str(file_path)
    
    def copy_to_mcp_docs(self, results: Dict[str, str], mcp_dir: str = "data/mcp_docs") -> Dict[str, str]:
        """
        처리된 Markdown 문서들을 MCP용으로 복사 (간단한 파일명으로)
        
        Args:
            results: process_wiki_documents의 결과 (.md 파일들)
            mcp_dir: MCP 문서 저장 디렉토리
            
        Returns:
            {키워드: MCP_파일_경로} 형태의 딕셔너리
        """
        mcp_path = Path(mcp_dir)
        mcp_path.mkdir(parents=True, exist_ok=True)
        
        mcp_results = {}
        
        print(f"\n📋 MCP용 Markdown 파일 복사 중...")
        
        for keyword, original_path in results.items():
            try:
                # 원본 Markdown 파일 읽기
                with open(original_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # MCP용 간단한 파일명 생성 (.md 확장자 유지)
                simple_filename = f"{keyword}.md"
                mcp_file_path = mcp_path / simple_filename
                
                # MCP용 Markdown 파일 저장
                with open(mcp_file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                mcp_results[keyword] = str(mcp_file_path)
                print(f"  ✅ {keyword} → {simple_filename}")
                
            except Exception as e:
                print(f"  ❌ {keyword} 복사 실패: {e}")
                continue
        
        print(f"📁 MCP Markdown 파일 저장 완료: {mcp_path}")
        return mcp_results

    def process_wiki_documents(self, wiki_data: Dict[str, str]) -> Dict[str, str]:
        """
        위키피디아 문서들을 일괄 처리
        
        Args:
            wiki_data: {키워드: URL} 형태의 딕셔너리
            
        Returns:
            {키워드: 저장된_파일_경로} 형태의 딕셔너리
        """
        results = {}
        
        print(f"총 {len(wiki_data)}개 문서 처리 시작...")
        
        for i, (keyword, url) in enumerate(wiki_data.items(), 1):
            print(f"\n[{i}/{len(wiki_data)}] 처리 중: {keyword}")
            
            try:
                # 1. 위키피디아 크롤링
                print("  - 크롤링 중...")
                title, content = self.crawl_wikipedia_page(url)
                
                if content == "내용을 찾을 수 없습니다.":
                    print(f"  - 건너뜀: 내용 없음")
                    continue
                
                # 2. 파일 저장
                print("  - 파일 저장 중...")
                file_path = self.save_document(title, content)
                
                results[keyword] = file_path
                print(f"  - 완료: {file_path}")
                
                # API 요청 제한 고려 (1초 대기)
                time.sleep(1)
                
            except Exception as e:
                print(f"  - 오류 발생: {e}")
                continue
        
        print(f"\n처리 완료! 총 {len(results)}개 파일 생성됨")
        
        # MCP용 파일 복사
        if results:
            mcp_results = self.copy_to_mcp_docs(results)
            return results
        
        return results


def main():
    """메인 실행 함수"""
    
    # 위키피디아 데이터
    wiki_data = {
        "인공지능": "https://ko.wikipedia.org/wiki/인공지능",
        "머신러닝": "https://ko.wikipedia.org/wiki/기계_학습", 
        "딥러닝": "https://ko.wikipedia.org/wiki/딥_러닝",
        "cnn": "https://ko.wikipedia.org/wiki/합성곱_신경망",
        "rnn": "https://ko.wikipedia.org/wiki/순환_신경망",
        "lstm": "https://ko.wikipedia.org/wiki/장단기_메모리",
        "gru": "https://ko.wikipedia.org/wiki/게이트_순환_유닛", 
        "transformer": "https://ko.wikipedia.org/wiki/트랜스포머_(기계_학습)",
        "gpt": "https://ko.wikipedia.org/wiki/GPT_(언어_모델)",
        "alphago": "https://ko.wikipedia.org/wiki/알파고",
        "강화학습": "https://ko.wikipedia.org/wiki/강화_학습"
    }
    
    # OpenAI API 키 (환경변수에서 가져오기)
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("오류: OPENAI_API_KEY 환경변수가 설정되지 않았습니다.")
        return
    
    # 파서 초기화 및 실행
    parser = WikiDataParser(api_key)
    results = parser.process_wiki_documents(wiki_data)
    
    # 결과 출력
    print("\n=== 처리 결과 ===")
    for keyword, file_path in results.items():
        print(f"{keyword}: {file_path}")


if __name__ == "__main__":
    main() 