import numpy as np

np.random.seed(3)

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

#데이터셋 불러오기
data_aug_gen = ImageDataGenerator(rescale=1./255,
                                  rotation_range=0.1,
                                  width_shift_range=0.1,
                                  height_shift_range=0.1,
                                  zoom_range=0.3,
                                  fill_mode='nearest')

img = load_img('data_set/train/add/+_1.jpeg')
x = img_to_array(img)
x = x.reshape((1,) + x.shape)

i = 0
for batch in data_aug_gen.flow(x, batch_size=1, save_to_dir='data_set\preview', save_prefix='add', save_format='jpeg'):
    i += 1
    if i > 30:
        break


