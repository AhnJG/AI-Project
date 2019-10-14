from keras.preprocessing.image import ImageDataGenerator


######################################################
#1.데이터셋 생성하기
# train_datagen = ImageDataGenerator(rescale=1./255)
#
# train_generator = train_datagen.flow_from_directory(
#         'data_set/train',
#         target_size=(64, 64),
#         batch_size=5,
#         class_mode='categorical')

#print(train_datagen.)
# print(train_generator.image_shape)

a = 12344532452.12352345
b = a / 3600
c = a / 60
d = a % 60
print('%d %d %.2f'%(b, c, d))