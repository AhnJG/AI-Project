## Reciept OCR

---

### Tesseract

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
- 단색 흰색 배경에 검정색 텍스트를 깨끗이 정리할 때 가장 좋습니다.
- 어두운 경계와 관련해서는 아주 좋은 결과물 내지는 않으며 이것들을 종종 텍스트로 간주합니다.
- 텍스트 영역을 잘라내어 Tesseract를 조금 도와 주면 완벽한 결과를 얻을 수 있습니다
- **PIL.Image로 이미지를 읽는것 보다 cv2.imread로 읽는것이 더 높은 정확도를 가진다**
  - 검증 필요, 나의 Reciept 데이터 셋을 기준으로는 더 높은 정확도를 가진다

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

### conda

activate py35

---

### Idea

1. 이미지 전처리
   1. GRAY_SCALE로 변경
   2. 이미지 잡음 제거, Threshold -> 어느 정도로 처리를 해야 정확도가 좋아질지 잘 모르겠다
   3. 영수증을 인식하여 정방향으로 회전
   4. 영수증 안에서 텍스트 영역 Detection
2. 영수증에 사용되는 폰트를 이용하여 글자를 생성해서 해당 폰트 학습

3. 맞춤법 검사기를 통해 오타 수정
   1. 현금영수증을 뺀금 영수중, 핸금 영수중과 같은 단어로 인식하면 오타를 잡을수 없다

4. 3-1을 해결하기 위해 뺀금 -> 현금, 영수중 -> 영수증과 같이 오타를 교정하는 데이터 셋을 직접 만든다

5. 영수증을 영상으로 찍는다, 
   1. 프레임 단위로 이미지 변환
   2. 모든 이미지에 ocr 수행
   3. 결과를 line 단위로 배열에 저장, 가장 많은 똑같은 결과를 가지는 항목을 출력한다
      1. 잘못된 결과가 가장 많이 검출될 수 있다
      2. **영상을 프레임단위로 이미지로 변환해도 이미지 간의 차이가 미미하여 이미지 하나의 정확도가 낮게 나올경우 전체적으로 매우 안좋은 결과를 가진다 (images/video_receipt)**
   4. 모든 이미지에 맞춤법 검사를 수행하여 가장 오류가 적은 항목을 선정
   5. 라인별로 맞춤법 검사를 수행하여 가장 오류가 적은 라인을 선정

---

### Text Detection

[OpenCV (C++/Python)를 활용한 딥러닝 기반의 텍스트 탐지](https://blog.naver.com/PostView.nhn?blogId=tommybee&logNo=221650194118&parentCategoryNo=&categoryNo=157&viewDate=&isShowPopularPosts=true&from=search#)



