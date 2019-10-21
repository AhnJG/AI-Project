# Reciept OCR

---

## Abstract
영수증에 있는 가게명, 거래일, 구입 물품, 금액등의 정보를 가져올수 있는 OCR을 수행하고자 한다.

### conda

activate py35

---

## Idea

1. **이미지 전처리**
   1. GRAY_SCALE로 변경
   2. 이미지 잡음 제거, Threshold -> 어느 정도로 처리를 해야 정확도가 좋아질지 잘 모르겠다
   3. 영수증을 인식하여 정방향으로 회전
   4. 영수증 안에서 텍스트 영역 Detection
2. 영수증에 사용되는 폰트를 이용하여 글자를 생성해서 해당 폰트 학습
   1. 영수증에 주로 나타나는 글자를 학습시킨다. 가맹점, 합계 ...
3. 맞춤법 검사기를 통해 **오타 수정**
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
6. **좋은 이미지를 만들도록 사용자 행동을 유도한다**
   1. 입력 이미지가 OCR의 결과에 많은 영향을 준다, 따라서 좋은 입력을 만들수 있다면 가장 편하게 좋은 결과를 얻을수 있다
7. 예측 실패 데이터를 넣어 추가적인 학습을 시킬수는 없을까?
8. Receipt OCR을 수행하기 전에 해당 이미지가 Receipt가 맞는지 확인을 해야한다. 아니라면 사용자가 손으로 쓴 글씨도 똑같이 영수증 OCR을 수행하게 된다

---

## Text Detection

[OpenCV (C++/Python)를 활용한 딥러닝 기반의 텍스트 탐지](https://blog.naver.com/PostView.nhn?blogId=tommybee&logNo=221650194118&parentCategoryNo=&categoryNo=157&viewDate=&isShowPopularPosts=true&from=search#)

-  [EAST: An Efficient and Accurate Scene Text Detector](https://arxiv.org/abs/1704.03155v2) 기반 텍스트 탐지

  

---

## Image Preprocessing

[Improve Accuracy of OCR using Image Preprocessing](https://medium.com/cashify-engineering/improve-accuracy-of-ocr-using-image-preprocessing-8df29ec3a033)

---

## Spell Check (문법 검사)

[파이썬 한글 맞춤법 검사 라이브러리. (네이버 맞춤법 검사기 사용)](https://github.com/ssut/py-hanspell)

---

### OpenCV

#### cv2.Imread 

Flag

- cv2.IRMEAD_GRAYSCALE: 우리가 방금 한 거예요. 사진을 흑백으로 읽어요. 0으로도 대체할 수 있어요.

- cv2.IMREAD_COLOR: 사진을 유색으로 읽을 수 있는데, 투명도가 다 무시되어요. cv2.imread()의 기본값은 이거예요. 1로도 대체할 수 있어요.

- cv2.IMREAD_UNCHANGED: 사진을 있는 그대로 읽어요. BGR 채널뿐만 아니라 투명도 채널까지 읽혀요. -1로도 대체할 수 있어요.

---

### PIL

#### Image

```python
# use nearest neighbour
im2 = im1.resize((width, height), Image.NEAREST)      
# linear interpolation in a 2x2 environment
im3 = im1.resize((width, height), Image.BILINEAR)
# cubic spline interpolation in a 4x4 environment
im4 = im1.resize((width, height), Image.BICUBIC)      
## best down-sizing filter
im5 = im1.resize((width, height), Image.ANTIALIAS)    
```



---

## Result

- 배경이 어두운색(검은색) 일수록 이미지 전처리(edge, findContours, Perspective Transform)에서 높은 정확도를 가진다
- 