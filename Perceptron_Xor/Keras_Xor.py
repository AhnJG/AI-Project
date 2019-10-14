import numpy as np
from keras.models import Sequential
from keras.layers import Dense

#데이터셋 생성하기
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

#모델 구성
model = Sequential()
model.add(Dense(8, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

#모델 학습과정 설정하기
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#모델 학습시키기
hist = model.fit(X, y, batch_size=1, epochs=1000)
print(model.predict_proba(X))

#모델 평가하기
scores = model.evaluate(X, y)
print("%s: %.2f%%" %(model.metrics_names[1], scores[1]*100))
