# Image Similarity

## Abstract

두 이미지간의 유사도를 판별하고자 한다

## Idea

1. OpenCV의 BFMatcher와 xfeatures2d.surf.detectAndCompute를 이용하여 특징을 탐지하여 이미지 간 유사성 판별

2. 사전 학습된 Resnet50모델을 기반으로 Feature를 탐지하여 이미지 간 유사성 판별

3. 코사인 유사도

4. 특정 행동을 정해둔다 + GPS 

   1. 바다를 배경으로 사진찍기

   2. 건물을 배경으로 사진찍기

   3. 5명과 함께 사진찍기

      



### 

## Find

- 대상 이미지간 똑같은 사이즈를 가지는 것이 좋다, 아니라면 너무 많거나 적은 특징이 검출될 수 있다

