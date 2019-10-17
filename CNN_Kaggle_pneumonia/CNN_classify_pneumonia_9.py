import time
start = time.time()

import sys
sys.stdout = open('Classify_Pneumonia_model_log.txt', 'w')

#1.데이터 셋 불러오기
from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale=1./255)
train_set = train_datagen.flow_from_directory(
    'chest_xray/train',
    target_size=(128, 128),
    batch_size=16,
    class_mode='categorical'
    )

validation_datagen = ImageDataGenerator(rescale=1./255)
validation_set = validation_datagen.flow_from_directory(
    'chest_xray/val',
    target_size=(128, 128),
    batch_size=8,
    class_mode='categorical'
    )

test_datagen = ImageDataGenerator(rescale=1./255)
test_set = test_datagen.flow_from_directory(
    'chest_xray/test',
    target_size=(128, 128),
    batch_size=16,
    class_mode='categorical'
    )

####################################################
#2.모델구성
from keras.models import Sequential
from keras.layers import Dense, Flatten, Dropout
from keras.layers.convolutional import Conv2D, MaxPooling2D

#컨볼루션 레이어 한 층 삭제
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(128, 128, 3)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add((Flatten()))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(2, activation='softmax'))

#######################################################
#3.모델 학습과정 설정
from keras.optimizers import RMSprop
model.compile(optimizer=RMSprop(lr=0.00005), loss='binary_crossentropy', metrics=['accuracy'])
#bin -> categorical로 수정

##################################################################
#모델 정보 출력
print(model.summary())
#######################################################
#4.모델 학습
from keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor='val_loss', min_delta=0, mode='min',patience=3)
model.fit_generator(
    train_set,
    epochs=20,
    validation_data=validation_set,
    validation_steps=4,
    callbacks=[early_stopping]
)

#########################################################
#5.모델 평가하기
print("--Evaluate--")
scores = model.evaluate_generator(test_set, steps=12)
print("%s: %.2f%%"%(model.metrics_names[1], scores[1] * 100))

###################################################################
#6.모델 사용하기
import numpy as np
print("--Predict--")
output = model.predict_generator(test_set, steps=4)
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
print(test_set.class_indices)
print(output)

####################################################################
#7.모델 저장하기
model.save('Classify_Pneumonia_model.h5')

end = time.time()
end = end-start
hour = end / 3600
minute = end / 60
second = end % 60
print('소요 시간 : %d시간 %d분 %.2f초'%(hour, minute, second))



#9optimizer=RMSprop(lr=0.00005), loss='binary_crossentropy' 수정 (128, 128)
#patience : 3
#Epoch : 9
#acc = 85.94
#time = 4762Sec =  80분

