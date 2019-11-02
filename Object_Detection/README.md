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

## YOLO-V3-Train

- https://github.com/ultralytics/yolov3

- 저자에 의하면 class당 2,000 iteration을 권하고 있습니다.

  ```bash
  # Default Setting
  pip install -U setuptools
  pip install -U -r requirements.txt
  
   # copy COCO2014 dataset (20GB)
  bash data/get_coco_dataset_gdrive.sh 
  
  ```

  ```bash
  # change_file_name
  python change_file_name.py --folder="coco/images/val" --format="atv_rider"
  
  # Train
  python train.py --cfg="coco/yolov3-tiny.cfg" --data="coco/atv_rider_obj_1.data" --weight="weights/darknet53.conv.74"
  
  # Detect
  python detect.py --cfg="coco/yolov3-tiny.cfg" --data="coco/atv_rider_obj_1.data" --weight="weights/last.pt"  
  python detect.py --cfg cfg/yolov3-tiny.cfg --weights weights/yolov3-tiny.weights
  ```

  

- ### yolov3 pytorch weights

  - download from Google Drive: https://drive.google.com/drive/folders/1uxgUBemJVw9wZsdpboYbzUN4bcRhsuAI

- ### .cfg file setting

  - batch=64

    - 만약 out of memory 에러가 뜨며 학습이 되지 않을 경우 batch와 subdivisions를 변경합니다.

      Batch는 4의 배수로, subdivisions는 2의 배수로 맞춰줍니다.

      (batch는 클 수록, subdivisions는 작을 수록 정확도가 높아지지만 학습이 느리고 그래픽 메모리가 많이 필요합니다)

  - subdivisions=8
    - subdivision을 8로 수정합니다. 이 뜻은 batch를 8개로 나누어 GPU 메모리 부하를 줄이겠다는 의도입니다.

  - classes =? Detection하고 싶은 물체의 개수

  - filters = (classes+5)*3 으로 입력 (line 127,171)

  - max_batches = 4000 * 클래스 갯수

