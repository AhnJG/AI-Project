# Object Detection

## bikerider-detector-master

## YOLO-V3

- Deep Learning based Object Detection using YOLOv3 with OpenCV ( Python / C++ )

- https://www.learnopencv.com/deep-learning-based-object-detection-using-yolov3-with-opencv-python-c/

- Git : https://github.com/AhnJG/learnopencv/tree/master/ObjectDetection-YOLO

- GPU의 메모리 사이즈가 4GB이상이라면 yolov3모델을, 4GB 이하라면 tiny모델을 사용할 것을 추천합니다.

- ```bash
  sudo chmod a+x getModels.sh
  ./getModels.sh
  ```

- ```python
  python3 object_detection_yolo.py --image=bird.jpg
  ```

- ### Class

  - Person
  - motorbike(atv)

## YOLO-V3-Train

- https://github.com/ultralytics/yolov3

- 만약 out of memory 에러가 뜨며 학습이 되지 않을 경우 batch와 subdivisions를 변경합니다.

  Batch는 4의 배수로, subdivisions는 2의 배수로 맞춰줍니다.

  (batch는 클 수록, subdivisions는 작을 수록 정확도가 높아지지만 학습이 느리고 그래픽 메모리가 많이 필요합니다)

  ```bash
  # Default Setting
  pip install -U setuptools
  pip install -U -r requirements.txt
  
   # copy COCO2014 dataset (20GB)
  bash data/get_coco_dataset_gdrive.sh 
  
  # CUSTOM TRAINING EXAMPLE
  python3 train.py --data data/coco_16img.data --batch-size 16 --accumulate 1 --nosave --name coco_16img  
  python3 train.py --data data/coco_64img.data --batch-size 16 --accumulate 1 --nosave --name coco_64img
  
  # plot as 'results.png'
  python3 -c "from utils import utils; utils.plot_results()"  
  
  # Evaluate Trained Model, 이미지를 data/samples폴더에 복사하고 다음을 실행
  python3 detect.py --weights weights/best.pt
  ```

- ### yolov3 pytorch weights

  - download from Google Drive: https://drive.google.com/drive/folders/1uxgUBemJVw9wZsdpboYbzUN4bcRhsuAI

