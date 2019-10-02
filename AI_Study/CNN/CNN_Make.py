import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator

import time
start = time.time()

import sys
sys.stdout = open('test.txt', 'w')
######################################################
#1.데이터셋 생성하기
train_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_directory(
        'data_set/train',
        target_size=(64, 64),
        batch_size=5,
        class_mode='categorical')

validation_datagen = ImageDataGenerator(rescale=1./255)
validation_generator = validation_datagen.flow_from_directory(
        'data_set/validation',
        target_size=(64, 64),
        batch_size = 5,
        class_mode='categorical'
)

test_datagen = ImageDataGenerator(rescale=1./255)
test_generator = test_datagen.flow_from_directory(
        'data_set/test',
        batch_size=5,
        target_size=(64, 64),
        class_mode='categorical')
#########################################################
#2.모델 구성하기
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(64, 64, 3)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(4, activation='softmax'))

# from IPython.display import SVG, display_svg
# from keras.utils.vis_utils import model_to_dot
#
# SVG(model_to_dot(model, show_shapes=True).create(prog='dot', format='svg'))

#################################################################
#3.모델 학습과정 설정하기
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


##################################################################
#모델 정보 출력
print(model.summary())
##################################################################
#4.모델 학습시키기
# train = 60, validation = 20, batch=5
from keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor='val_loss', min_delta=0, mode='min',patience=3)
model.fit_generator(
        train_generator,
        steps_per_epoch=12,
        epochs=30,
        validation_data=validation_generator,
        validation_steps=4,
        callbacks=[early_stopping]
)

######################################################################
#5.모델 평가하기
print("--Evaluate--")
scores = model.evaluate_generator(test_generator, steps=4)
print("%s: %.2f%%"%(model.metrics_names[1], scores[1] * 100))

###################################################################
#6.모델 사용하기
print("--Predict--")
output = model.predict_generator(test_generator, steps=4)
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
print(test_generator.class_indices)
print(output)

model.save('test_model.h5')

end = time.time()
end = end-start
hour = end / 3600
minute = end / 60
second = end % 60
print('소요 시간 : %d시간 %d분 %.2f초'%(hour, minute, second))



