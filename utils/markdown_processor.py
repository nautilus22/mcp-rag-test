"""
MCP용 마크다운 처리 모듈
원본 텍스트를 MCP 시스템에 적합한 마크다운 형식으로 변환합니다.
"""

import re
from typing import Optional


class MarkdownProcessor:
    """MCP용 마크다운 처리 클래스"""
    
    def __init__(self):
        """초기화"""
        pass
    
    def process_for_mcp(self, raw_content: str) -> str:
        """
        원본 텍스트를 MCP용 마크다운으로 처리
        
        Args:
            raw_content: 원본 텍스트
            
        Returns:
            MCP용 마크다운 텍스트
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
        
        # 최종 마크다운 구성
        markdown = f"# {title}\n\n"
        markdown += processed_content
        
        return markdown
    
    def _process_content(self, content: str) -> str:
        """
        본문 내용을 마크다운 형식으로 처리
        
        Args:
            content: 원본 본문
            
        Returns:
            처리된 마크다운 텍스트
        """
        # HTML 태그 제거
        content = self._remove_html_tags(content)
        
        # 마크다운 특수문자 처리
        content = self._process_markdown_syntax(content)
        
        # 각주 및 참조 제거
        content = self._remove_citations(content)
        
        # 텍스트 정리
        content = self._clean_text(content)
        
        return content
    
    def _remove_html_tags(self, text: str) -> str:
        """HTML 태그 제거"""
        # 간단한 HTML 태그 제거
        text = re.sub(r'<[^>]+>', '', text)
        return text
    
    def _process_markdown_syntax(self, text: str) -> str:
        """마크다운 문법 처리"""
        # 강조 처리
        text = re.sub(r'\*\*(.*?)\*\*', r'**\1**', text)  # 굵게
        text = re.sub(r'\*(.*?)\*', r'*\1*', text)        # 기울임
        
        # 링크 처리 (간단한 형태)
        text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
        
        # 코드 블록 처리
        text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
        text = re.sub(r'`([^`]+)`', r'\1', text)
        
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
                '같이 보기', '같이보기', '바깥 링크', '바깥링크'
            ]):
                skip_mode = True
                continue
            
            # 메인 섹션 재시작 감지
            if skip_mode and line.startswith('#'):
                skip_mode = False
            
            if not skip_mode:
                filtered_lines.append(line)
        
        return '\n'.join(filtered_lines)
    
    def _clean_text(self, text: str) -> str:
        """텍스트 정리"""
        # 과도한 공백 제거
        text = re.sub(r'\n{3,}', '\n\n', text)
        text = re.sub(r' +', ' ', text)
        
        # 앞뒤 공백 제거
        text = text.strip()
        
        return text 