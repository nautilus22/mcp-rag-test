"""
위키피디아 데이터 다운로드 스크립트
shared/data_parser.py의 WikiDataParser를 사용하여 위키 문서를 크롤링하고 처리합니다.
"""

import sys
import os
from pathlib import Path

# 프로젝트 루트를 Python 경로에 추가
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

from util.data_parser import WikiDataParser


def main():
    """위키피디아 데이터 다운로드 메인 실행"""
    
    print("=== 위키피디아 AI/ML 문서 다운로드 ===")
    
    # OpenAI API 키 확인
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ 오류: OPENAI_API_KEY 환경변수가 설정되지 않았습니다.")
        print("다음 명령어로 API 키를 설정하세요:")
        print("export OPENAI_API_KEY='your-api-key-here'")
        return
    
    # 위키피디아 문서 URL 목록
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
    
    try:
        # WikiDataParser 초기화
        output_dir = project_root / "data" / "raw"
        parser = WikiDataParser(api_key, str(output_dir))
        
        print(f"📁 저장 위치: {output_dir}")
        print(f"📊 처리할 문서 수: {len(wiki_data)}개")
        print()
        
        # 문서 처리 실행
        results = parser.process_wiki_documents(wiki_data)
        
        # 결과 요약
        print("\n" + "="*60)
        print("📋 처리 결과 요약")
        print("="*60)
        
        if results:
            print(f"✅ 성공: {len(results)}개 문서")
            print(f"❌ 실패: {len(wiki_data) - len(results)}개 문서")
            print()
            
            print("📄 생성된 파일 목록:")
            for keyword, file_path in results.items():
                relative_path = Path(file_path).relative_to(project_root)
                print(f"  • {keyword}: {relative_path}")
        else:
            print("❌ 처리된 문서가 없습니다.")
            
        print("\n🎉 다운로드 완료!")
        
        # MCP 및 RAG 사용 안내
        print("\n" + "="*60)
        print("📖 다음 단계")
        print("="*60)
        print("1. RAG 시스템 구축:")
        print("   python rag/scripts/step1_prepare_data.py")
        print()
        print("2. MCP 서버 실행:")
        print("   python scripts/run_mcp_server.py")
        
    except KeyboardInterrupt:
        print("\n\n⏹️  사용자에 의해 중단되었습니다.")
    except Exception as e:
        print(f"\n❌ 오류 발생: {e}")
        print("문제가 지속되면 API 키와 네트워크 연결을 확인해주세요.")


if __name__ == "__main__":
    main() 