import re
import markdown
from pathlib import Path
from typing import List, Dict, Any
from bs4 import BeautifulSoup


class MarkdownProcessor:
    """마크다운 파일을 전처리하여 특수기호를 제거하고 텍스트를 정리하는 클래스"""
    
    def __init__(self, preprocessed_dir: str = "data/preprocessed"):
        self.md = markdown.Markdown()
        self.preprocessed_dir = Path(preprocessed_dir)
        self.preprocessed_dir.mkdir(parents=True, exist_ok=True)
    
    def clean_text(self, text: str) -> str:
        """텍스트에서 특수기호와 불필요한 문자들을 제거합니다."""
        # HTML 태그 제거
        soup = BeautifulSoup(text, 'html.parser')
        text = soup.get_text()
        
        # 마크다운 특수문자 제거
        text = re.sub(r'[#*_`~\[\](){}|\\>]', '', text)
        
        # 수식 제거 (LaTeX 수식)
        text = re.sub(r'\$\$.*?\$\$', '', text, flags=re.DOTALL)
        text = re.sub(r'\$.*?\$', '', text)
        
        # 링크 제거
        text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
        
        # 이미지 제거
        text = re.sub(r'!\[([^\]]*)\]\([^)]+\)', '', text)
        
        # 코드 블록 제거
        text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
        text = re.sub(r'`.*?`', '', text)
        
        # 인용 제거
        text = re.sub(r'^>\s*', '', text, flags=re.MULTILINE)
        
        # 수평선 제거
        text = re.sub(r'^[-*_]{3,}$', '', text, flags=re.MULTILINE)
        
        # YAML front matter 제거
        text = re.sub(r'^---\s*\n.*?\n---\s*\n', '', text, flags=re.DOTALL)
        text = re.sub(r'^---\s*\n.*?\n---', '', text, flags=re.DOTALL)
        # YAML front matter 완전 제거 (더 강력한 패턴)
        text = re.sub(r'^---\s*\n(?:.*\n)*?---\s*\n?', '', text, flags=re.MULTILINE)
        
        # 여러 개의 공백을 하나로
        text = re.sub(r'\s+', ' ', text)
        
        # 줄바꿈 정리
        text = re.sub(r'\n\s*\n', '\n\n', text)
        
        # 앞뒤 공백 제거
        text = text.strip()
        
        return text
    
    def save_preprocessed_text(self, file_name: str, cleaned_text: str, chunks: List[str]) -> str:
        """전처리된 텍스트를 txt 파일로 저장합니다."""
        # 전체 정리된 텍스트만 저장
        full_text_path = self.preprocessed_dir / f"{file_name}.txt"
        with open(full_text_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_text)
        
        return str(full_text_path)
    
    def process_markdown_file(self, file_path: Path) -> Dict[str, Any]:
        """마크다운 파일을 처리하여 정리된 텍스트와 메타데이터를 반환합니다."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # YAML front matter 제거 (HTML 변환 전에)
            content = re.sub(r'^---\s*\n(?:.*\n)*?---\s*\n?', '', content, flags=re.MULTILINE)
            
            # 마크다운을 HTML로 변환
            html = self.md.convert(content)
            
            # 텍스트 정리
            cleaned_text = self.clean_text(html)
            
            # 청크로 분할 (문단 단위)
            chunks = self.split_into_chunks(cleaned_text)
            
            # 전처리된 텍스트 저장
            saved_path = self.save_preprocessed_text(file_path.stem, cleaned_text, chunks)
            
            return {
                'file_path': str(file_path),
                'file_name': file_path.stem,
                'original_content': content,
                'cleaned_text': cleaned_text,
                'chunks': chunks,
                'preprocessed_path': saved_path,
                'metadata': {
                    'title': file_path.stem,
                    'source': 'markdown',
                    'file_size': len(content),
                    'preprocessed_size': len(cleaned_text),
                    'chunk_count': len(chunks)
                }
            }
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return None
    
    def split_into_chunks(self, text: str, max_chunk_size: int = 500) -> List[str]:
        """텍스트를 청크로 분할합니다."""
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
    
    def process_directory(self, directory_path: Path) -> List[Dict[str, Any]]:
        """디렉토리 내의 모든 마크다운 파일을 처리합니다."""
        processed_files = []
        
        for file_path in directory_path.glob("*.md"):
            result = self.process_markdown_file(file_path)
            if result:
                processed_files.append(result)
        
        return processed_files 