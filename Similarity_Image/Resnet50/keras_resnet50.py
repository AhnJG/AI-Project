from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
from keras.models import Model
import numpy as np
from os import listdir, walk
from os.path import isfile, join
import itertools

def getAllFilesInDirectory(directoryPath= str):
    return [(directoryPath + "/" + f) for f in listdir(directoryPath) if isfile(join(directoryPath, f))]

def predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return model.predict(x)

def findDifference(f1, f2):
    return np.linalg.norm(f1-f2)

def findDifferences(feature_vectors):
    similar: dict = {}
    keys = [k for k,v in feature_vectors.items()]
    min : dict = {}
    for k in keys:
        min[k] = 10000000
    possible_combinations=list(itertools.combinations(keys, 2))
    for k,v in possible_combinations:
       diff=findDifference(feature_vectors[k],feature_vectors[v])
       if(diff < min[k]):
           min[k] = diff
           similar[k] = v
           min[v] = diff
           similar[v] = k
    return similar 

def driver():
    feature_vectors: dict = {}
    model = ResNet50(weights='imagenet')
    for img_path in getAllFilesInDirectory("images"):
        feature_vectors[img_path] = predict(img_path,model)[0]
    results=findDifferences(feature_vectors)
    for k,v in results.items():
        print(k +" is most similar to: "+ v)    
    #print('Predicted:', decode_predictions(preds, top=3)[0])

driver()

# Output Result

# images/shoe.jpg is most similar to: images/shoe1.jpg
# images/shoe1.jpg is most similar to: images/shoe.jpg
# images/bikini.jpg is most similar to: images/dress.jpeg
# images/dress.jpeg is most similar to: images/bikini.jpg
# images/bear.jpg is most similar to: images/printer1.jpg
# images/printer1.jpg is most similar to: images/printer2.jpg
# images/coil1.jpeg is most similar to: images/printer1.jpg
# images/printer2.jpg is most similar to: images/printer1.jpg
