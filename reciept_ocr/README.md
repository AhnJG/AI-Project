## Reciept OCR

---

### Tesseract

[Tesseract 한국어 정리](https://blog.naver.com/PostView.nhn?blogId=tommybee&logNo=221307497468&parentCategoryNo=&categoryNo=54&viewDate=&isShowPopularPosts=true&from=search)

**설치 및 실행**

- brew install tesseract 입력후
- brew install tesseract-lang : 언어팩 설치
- tesseract [이미지] [결과] -i [언어]
- tesseract [이미지] [결과] -i kor+eng

**[Python에서 Tesseract 사용하기 for OCR]([https://junyoung-jamong.github.io/computer/vision,/ocr/2019/01/30/Python%EC%97%90%EC%84%9C-Tesseract%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%B4-OCR-%EC%88%98%ED%96%89%ED%95%98%EA%B8%B0.html](https://junyoung-jamong.github.io/computer/vision,/ocr/2019/01/30/Python에서-Tesseract를-이용해-OCR-수행하기.html))**

- pip install pytesseract

```python
#이미지로부터 텍스트를 추출하는 함수 : pytesseract.image_to_string()
#자세한 사용 방법 : https://github.com/madmaze/pytesseract
print(pytesseract.image_to_string('img.png'))
pytesseract.image_to_string('img.png', lang='eng', config='--psm 1 -c preserve_interword_spaces=1')
```

**ERROR**

TesseractNotFoundError: tesseract is not installed or it's not in your path

 - tesseract가 제대로 설치되지 않은 것

 - ```
   #https://anaconda.org/conda-forge/tesseract
   conda install -c conda-forge tesseract
   ```

---

### conda

activate py35



