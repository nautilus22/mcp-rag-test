"""
RAG용 텍스트 전처리 모듈
원본 텍스트를 RAG 시스템에 적합한 형태로 전처리합니다.
"""

import re
from typing import List


class TextProcessor:
    """RAG용 텍스트 전처리 클래스"""
    
    def __init__(self):
        """초기화"""
        pass
    
    def process_for_rag(self, raw_content: str) -> str:
        """
        원본 텍스트를 RAG용으로 전처리
        
        Args:
            raw_content: 원본 텍스트
            
        Returns:
            RAG용 전처리된 텍스트
        """
        # 제목과 본문 분리
        lines = raw_content.split('\n')
        title = ""
        content_lines = []
        
        # 제목 추출
        for i, line in enumerate(lines):
            if line.startswith('제목:'):
                title = line.replace('제목:', '').strip()
                content_lines = lines[i+1:]
                break
            else:
                content_lines.append(line)
        
        # 본문 처리
        processed_content = self._process_content('\n'.join(content_lines))
        
        # 최종 텍스트 구성
        final_text = f"제목: {title}\n\n"
        final_text += processed_content
        
        return final_text
    
    def _process_content(self, content: str) -> str:
        """
        본문 내용을 RAG용으로 전처리
        
        Args:
            content: 원본 본문
            
        Returns:
            전처리된 텍스트
        """
        # HTML 태그 제거
        content = self._remove_html_tags(content)
        
        # 마크다운 특수문자 제거
        content = self._remove_markdown_syntax(content)
        
        # 수식 제거
        content = self._remove_math_expressions(content)
        
        # 각주 및 참조 제거
        content = self._remove_citations(content)
        
        # 불필요한 섹션 제거
        content = self._remove_unnecessary_sections(content)
        
        # 텍스트 정리
        content = self._clean_text(content)
        
        return content
    
    def _remove_html_tags(self, text: str) -> str:
        """HTML 태그 제거"""
        # HTML 태그 제거
        text = re.sub(r'<[^>]+>', '', text)
        return text
    
    def _remove_markdown_syntax(self, text: str) -> str:
        """마크다운 문법 제거"""
        # 헤더 제거
        text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
        
        # 강조 제거
        text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)  # 굵게
        text = re.sub(r'\*(.*?)\*', r'\1', text)      # 기울임
        text = re.sub(r'__(.*?)__', r'\1', text)      # 굵게
        text = re.sub(r'_(.*?)_', r'\1', text)        # 기울임
        
        # 링크 제거
        text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
        text = re.sub(r'\[([^\]]+)\]', r'\1', text)
        
        # 코드 블록 제거
        text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
        text = re.sub(r'`([^`]+)`', r'\1', text)
        
        # 인용 제거
        text = re.sub(r'^>\s*', '', text, flags=re.MULTILINE)
        
        # 수평선 제거
        text = re.sub(r'^[-*_]{3,}$', '', text, flags=re.MULTILINE)
        
        # 리스트 마커 제거
        text = re.sub(r'^[-*+]\s+', '', text, flags=re.MULTILINE)
        text = re.sub(r'^\d+\.\s+', '', text, flags=re.MULTILINE)
        
        return text
    
    def _remove_math_expressions(self, text: str) -> str:
        """수식 제거"""
        # LaTeX 수식 제거
        text = re.sub(r'\$\$.*?\$\$', '', text, flags=re.DOTALL)
        text = re.sub(r'\$.*?\$', '', text)
        
        # 수학 기호들을 일반 텍스트로 변환
        math_symbols = {
            'α': 'alpha', 'β': 'beta', 'γ': 'gamma', 'δ': 'delta',
            'ε': 'epsilon', 'ζ': 'zeta', 'η': 'eta', 'θ': 'theta',
            'ι': 'iota', 'κ': 'kappa', 'λ': 'lambda', 'μ': 'mu',
            'ν': 'nu', 'ξ': 'xi', 'π': 'pi', 'ρ': 'rho',
            'σ': 'sigma', 'τ': 'tau', 'υ': 'upsilon', 'φ': 'phi',
            'χ': 'chi', 'ψ': 'psi', 'ω': 'omega',
            '∞': '무한', '∂': '편미분', '∇': '나블라',
            '∑': '합계', '∏': '곱', '∫': '적분'
        }
        
        for symbol, replacement in math_symbols.items():
            text = text.replace(symbol, replacement)
        
        return text
    
    def _remove_citations(self, text: str) -> str:
        """각주 및 참조 제거"""
        # 각주 번호 패턴 제거
        text = re.sub(r'\[\d+\]', '', text)
        text = re.sub(r'\[\d+,\s*\d+\]', '', text)
        text = re.sub(r'\[\d+-\d+\]', '', text)
        
        # 참조 섹션 제거
        lines = text.split('\n')
        filtered_lines = []
        skip_mode = False
        
        for line in lines:
            line_lower = line.lower().strip()
            
            # 제외할 섹션 시작 감지
            if any(keyword in line_lower for keyword in [
                '참고 문헌', '참고문헌', '각주', '외부 링크', '외부링크',
                '같이 보기', '같이보기', '바깥 링크', '바깥링크',
                '더 보기', '더보기', '참고 자료', '참고자료'
            ]):
                skip_mode = True
                continue
            
            # 메인 섹션 재시작 감지
            if skip_mode and (line.strip().startswith('##') or 
                             any(keyword in line_lower for keyword in [
                                 '개요', '정의', '역사', '특징', '원리', '방법'
                             ])):
                skip_mode = False
            
            if not skip_mode:
                filtered_lines.append(line)
        
        return '\n'.join(filtered_lines)
    
    def _remove_unnecessary_sections(self, text: str) -> str:
        """불필요한 섹션 제거"""
        lines = text.split('\n')
        filtered_lines = []
        skip_mode = False
        
        for line in lines:
            line_lower = line.lower().strip()
            
            # 제외할 섹션들
            skip_keywords = [
                '편집', 'edit', '토론', 'talk', '역사', 'history',
                '모니터링', 'monitoring', '보호', 'protection',
                '분류', 'category', '카테고리'
            ]
            
            if any(keyword in line_lower for keyword in skip_keywords):
                skip_mode = True
                continue
            
            # 새로운 섹션 시작 감지
            if line.strip().startswith('##'):
                skip_mode = False
            
            if not skip_mode:
                filtered_lines.append(line)
        
        return '\n'.join(filtered_lines)
    
    def _clean_text(self, text: str) -> str:
        """텍스트 정리"""
        # 과도한 공백 제거
        text = re.sub(r'\n{3,}', '\n\n', text)
        text = re.sub(r' +', ' ', text)
        
        # 특수문자 정리
        text = re.sub(r'[^\w\s가-힣.,!?;:()\-]', '', text)
        
        # 앞뒤 공백 제거
        text = text.strip()
        
        return text
    
    def split_into_chunks(self, text: str, max_chunk_size: int = 1000) -> List[str]:
        """
        텍스트를 청크로 분할 (RAG용)
        
        Args:
            text: 분할할 텍스트
            max_chunk_size: 최대 청크 크기
            
        Returns:
            청크 리스트
        """
        # 문단 단위로 분할
        paragraphs = text.split('\n\n')
        chunks = []
        current_chunk = ""
        
        for paragraph in paragraphs:
            paragraph = paragraph.strip()
            if not paragraph:
                continue
            
            # 단일 문단이 너무 길면 더 작게 분할
            if len(paragraph) > max_chunk_size:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                    current_chunk = ""
                
                # 긴 문단을 문장 단위로 분할
                sentences = paragraph.split('. ')
                temp_chunk = ""
                for sentence in sentences:
                    if len(temp_chunk) + len(sentence) <= max_chunk_size:
                        temp_chunk += sentence + ". "
                    else:
                        if temp_chunk:
                            chunks.append(temp_chunk.strip())
                        temp_chunk = sentence + ". "
                
                if temp_chunk:
                    current_chunk = temp_chunk
                continue
            
            if len(current_chunk) + len(paragraph) <= max_chunk_size:
                current_chunk += paragraph + "\n\n"
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = paragraph + "\n\n"
        
        if current_chunk:
            chunks.append(current_chunk.strip())
        
        return chunks 