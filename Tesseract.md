## Tesseract

[Tesseract 한국어 정리](https://blog.naver.com/PostView.nhn?blogId=tommybee&logNo=221307497468&parentCategoryNo=&categoryNo=54&viewDate=&isShowPopularPosts=true&from=search)

**설치 및 실행**

- brew install tesseract 입력후
- brew install tesseract-lang : 언어팩 설치
- tesseract [이미지] [결과] -i [언어]
- tesseract [이미지] [결과] -i kor+eng

**[Python에서 Tesseract 사용하기 for OCR](https://junyoung-jamong.github.io/computer/vision,/ocr/2019/01/30/Python%EC%97%90%EC%84%9C-Tesseract%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%B4-OCR-%EC%88%98%ED%96%89%ED%95%98%EA%B8%B0.html)**

- pip install pytesseract

```python
#이미지로부터 텍스트를 추출하는 함수 : pytesseract.image_to_string()
#자세한 사용 방법 : https://github.com/madmaze/pytesseract
pytesseract.image_to_string('img.png')

pytesseract.image_to_string('img.png', lang='eng', config='--psm 1 -c preserve_interword_spaces=1')

config = ('-l eng --oem 1 --psm 3')
pytesseract.image_to_string(im, config=config)
```

### Description

- Tesseract 3.x는 전통적인 컴퓨터 비전 알고리즘을 기반으로 합니다.
- Tesseract 4에서는 Long Short Term Memory (LSTM) 기반 인식 엔진을 구현했습니다.
- 단색 **흰색 배경에 검정색 텍스트**를 깨끗이 정리할 때 가장 좋습니다.
- 어두운 경계와 관련해서는 아주 좋은 결과물 내지는 않으며 이것들을 종종 텍스트로 간주합니다.
- **텍스트 영역을 잘라내어** Tesseract를 조금 도와 주면 완벽한 결과를 얻을 수 있습니다
- **PIL.Image로 이미지를 읽는것 보다 cv2.imread로 읽는것이 더 높은 정확도를 가진다**
  - 검증 필요, 나의 Reciept 데이터 셋을 기준으로는 더 높은 정확도를 가진다
- **이미지 크기를 원래 크기의 두 배로 조정**하면 Tesseract가 더 나은 결과를 제공하기도합니다.
- Tesseract가 실행될 이상적인 환경은 **300DPI 이상, 배경이 흰색 글꼴이 검정색, 높이 20 픽셀이상, 텍스트가 수평인 이미지**가 가장 디코딩이 좋은 조건이라고 합니다.

### Engine

- OCR Engine Mode (oem): Tesseract 4에는 2 개의 OCR 엔진이 있습니다.
  1) 레거시 Tesseract 엔진
  2) LSTM 엔진: --oem 옵션을 사용하여 선택 할 수 있는 네 가지 작동 모드는 다음과 같습니다.

  > - OCR Engine modes(–oem):
  >   0 - Legacy engine only.
  >   1 - Neural nets LSTM engine only.
  >   2 - Legacy + LSTM engines.
  >   3 - Default, based on what is available.

  > - Page segmentation modes(–psm):
  >   0 - Orientation and script detection (OSD) only.
  >   1 - Automatic page segmentation with OSD.
  >   2 - Automatic page segmentation, but no OSD, or OCR.
  >   3 - Fully automatic page segmentation, but no OSD. (Default)
  >   4 - Assume a single column of text of variable sizes.
  >   5 - Assume a single uniform block of vertically aligned text.
  >   6 - Assume a single uniform block of text.
  >   7 - Treat the image as a single text line.
  >   8 - Treat the image as a single word.
  >   9 - Treat the image as a single word in a circle.
  >   10 - Treat the image as a single character.
  >   11 - Sparse text. Find as much text as possible in no particular order.
  >   12 - Sparse text with OSD.
  >   13 - Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract-specific.

### ERROR

TesseractNotFoundError: tesseract is not installed or it's not in your path

 - tesseract가 제대로 설치되지 않은 것

 - ```
   #https://anaconda.org/conda-forge/tesseract
   conda install -c conda-forge tesseract
   ```

---

### Tesseract Training

#### jTessBoxEditor

- Note: LSTM Training for Tesseract 4.0x is not supported. (Ref. jTessBoxEditor/Readme)

#### [TrainingTesseract 4.00](https://github.com/tesseract-ocr/tesseract/wiki/TrainingTesseract-4.00)

####[tesstrain](https://github.com/tesseract-ocr/tesstrain)

- Train Tesseract LSTM with make
- 