import easyocr

from step_1 import IN_DIR # 이전에 작성한 모듈 불러오기

path = IN_DIR / "ocr.jpg"
reader = easyocr.Reader(["ko", "en"], verbose=False)
parsed = reader.readtext(path.read_bytes())
print(parsed)


""" 시험문제 라이브러리 대체 """
# deepl : 문자번역
# easyocr : 문자인식
# numpy : 대규모 연산
# pillow : 이미지 처리
# request : 인터넷 통신(http 처리)
# streamlit : 웹 앱 제작
# torch, torchvision : 머신러닝

## pip install -U "numpy<=1.26.4" "torch<=2.5.1" "torchvision<=0.20.1" "easyocr<=1.7.2" "pillow<=10.4.0" deepl streamlit