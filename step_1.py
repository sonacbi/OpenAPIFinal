from pathlib import Path

# 작업하고자 하는 디렉터리 만들기
WORK_DIR = Path(__file__).parent
IN_DIR, OUT_DIR = WORK_DIR / "input", WORK_DIR / "output"

# if __name__ == "__main__":
#     IN_DIR.mkdir(exist_ok=True)
#     OUT_DIR.mkdir(exist_ok=True)


# 디렉터리 생성 (import 시에도 생성됨)
IN_DIR.mkdir(exist_ok=True)
OUT_DIR.mkdir(exist_ok=True)