# Object Detection

## bikerider-detector-master

## YOLO-V3

### About

- (YOLO V3)http://www.programmersought.com/article/2477186478/
- (YOLO v3 algorithm notes)http://www.programmersought.com/article/7888200386/
- (Learning and understanding: YOLO v1, v2, v3) http://www.programmersought.com/article/93361001378/
- (Yolo v3 parameter understanding)http://www.programmersought.com/article/1162490678/
- (YOLO-v3 model parameter anchor setting)http://www.programmersought.com/article/709620450/

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

---

## YOLO-V3-Train

- **Awesome (Labeling, Things)https://go-programming.tistory.com/160?category=768204**

- **Awesome Train https://eehoeskrap.tistory.com/370**

- (Darknet-kr)https://zeuseyera.github.io/darknet-kr/SaYongBeob_Yolo-v3.html

- **(YOLO v3 훈련 중 출력 매개 변수 의미)http://www.programmersought.com/article/9858453147/**

- **(Awesome Example)https://eungbean.github.io/2018/11/07/yolo-for-realtime-food-recognition/**

- **(DartNet 구조)https://dhhwang89.tistory.com/103?category=733930**

- (LearnOpenCV Ex)https://github.com/spmallick/learnopencv/tree/master/YOLOv3-Training-Snowman-Detector

- (2Class Ex)https://yeonsuuu-uuu.tistory.com/2

- (Split Train and Test)https://github.com/spmallick/learnopencv/blob/master/YOLOv3-Training-Snowman-Detector/splitTrainAndTest.py

- **(Colab에서 Darknet 학습하기)http://blog.ibanyez.info/blogs/coding/20190410-run-a-google-colab-notebook-to-train-yolov3-using-darknet-in/**

- YOLO Paper : https://pjreddie.com/media/files/papers/YOLOv3.pdf

- mAP : Yolo spp > yolo > yolo-tiny (CoCo Data Set Test)

  |             |    320     |    416     |    608     |
  | :---------: | :--------: | :--------: | :--------: |
  |   YOLOv3    | 51.8(51.5) | 55.4(55.3) | 58.2(57.9) |
  | YOLOv3-SPP  |    52.6    |    57.0    | 60.7(60.6) |
  | YOLOv3-tiny |    29.0    | 32.9(33.1) |    35.5    |

  - 320, 416, 608은 입력 이미지 사이즈이다

---

- ### Train Process-DarkNet

  - **Joheph DarkNet 학습 : https://pjreddie.com/darknet/yolo/** 
  - **AlexeyAB's Darknet : https://github.com/AlexeyAB/darknet/**
  - DarkNet은 linux와 window환경에서 yolo를 쉽게 test하고 train 할 수 있는 오픈소스이다
  - DarkNet은 [Joseph Redmon](https://twitter.com/pjreddie)이 작성을 하였는데 종종 [AlexeyAB's Darknet repo](https://github.com/AlexeyAB/darknet/)도 사용된다
  - Alexey Darknet은 Redmon의 Darknet에서 Forked된 것으로 작은 변화들이 있다
    - Alexey : 학습중 출력되는 log의 수가 적다(세대가 지날때마다 log를 출력)
  - YOLOv3의 학습 속도가 YOLOv3-tiny보다 10배 정도 더 많이 걸린다
  - 학습 환경이 좋지 않다면 Colab에서 학습하는 것이 좋다(mac book pro i5 8세대 + 16gb ram 기준 100배 빠르다)
  - gif 이미지는 없는것이 좋다 (없어야 되는것 같다)
  - 검출하지 않으려는 객체들의 사진도 필요합니다. (이 사진들은 빈 txt 파일을 가져야 합니다.)
  - 클래스당 2000개 이상의 이미지가 필요합니다.
  - 이미지 속 객체들의 **크기, 밝기, 위치, 회전, 배경**이 다양할 수록 정확도가 높아집니다.
    - DarkNet에 기본적으로 Data Augmentation이 적용되어 있는것 같다

  1. 기본 세팅

     ```bash
     git clone https://github.com/pjreddie/darknet
     cd darknet
     make
     ```

  2. obj.data 파일 만들기

     ```data
     classes= 2
     train  = ./opencv/data/train.txt
     valid  = ./opencv/data/valid.txt
     names = ./opencv/data/obj.names
     backup = backup/
     ```

  3. obj.names 파일 만들기 

     - Detect 하고 싶은 물체를 차례대로 입력한다
     - person부터 차례대로 0~의 값을 가진다(person:0, bicycle:1)

     ```names
     person
     bicycle
     car
     motorcycle
     airplane
     ```

  4. 학습시킬 이미지와 라벨링된 파일은 구분지어 넣어준다

     ```txt
     /data/images/train
     atv_rider0000.jpg
     atv_rider0001.jpg
     
     /data/label/train
     atv_rider0000.txt
     atv_rider0001.txt
     ```

     - 라벨링 파일 형식(object-class, x, y, width, height)

       ```txt
       0 0.270909 0.742727 0.287273 0.416364
       ```

  5. obj.data의 train과 valid에 설정된 경로에 train.txt와 valid.txt를 만든다

     - 학습시킬 이미지들의 경로를 지정해주면 된다

     ```txt
     YOLO-V3-Train/coco/images/train/atv_rider1126.jpg
     YOLO-V3-Train/coco/images/train/atv_rider1132.jpg
     YOLO-V3-Train/coco/images/train/atv_rider0204.jpg
     YOLO-V3-Train/coco/images/train/atv_rider0576.jpg
     YOLO-V3-Train/coco/images/train/atv_rider0984.jpg
     YOLO-V3-Train/coco/images/train/atv_rider0990.jpg
     ```

  6. Pre-Trained된 Convolutional Layers를 다운받는다

     - wget https://pjreddie.com/media/files/darknet53.conv.74
     - https://drive.google.com/drive/folders/1uxgUBemJVw9wZsdpboYbzUN4bcRhsuAI
     - Darknet `*.weights` format: https://pjreddie.com/media/files/yolov3.weights
     - PyTorch `*.pt` format: https://drive.google.com/drive/folders/1uxgUBemJVw9wZsdpboYbzUN4bcRhsuAI

  7. Cfg 파일 수정

     - batch=64

       - 만약 out of memory 에러가 뜨며 학습이 되지 않을 경우 batch와 subdivisions를 변경합니다.

         Batch는 4의 배수로, subdivisions는 2의 배수로 맞춰줍니다.

         (batch는 클 수록, subdivisions는 작을 수록 정확도가 높아지지만 학습이 느리고 그래픽 메모리가 많이 필요합니다)

     - subdivisions=8
       - subdivision을 8로 수정합니다. 이 뜻은 batch를 8개로 나누어 GPU 메모리 부하를 줄이겠다는 의도입니다.

     - classes =1 Detection하고 싶은 물체의 개수

     - filters = (classes+5)*3 으로 입력 (filters의 값이 255로 되어있는 것들을 바꾸면 된다)

     - max_batches = 4000 * 클래스 갯수
     - 저자에 의하면 class당 2,000 iteration을 권하고 있습니다.

  8. 학습 시작

     ```bash
     # Darknet
     ./darknet detector train coco/atv_rider_obj_4.data coco/yolov3_2.cfg weights/darknet53.conv.74
     ./darknet detector train coco/atv_rider_obj_4.data coco/yolov3-tiny.cfg
     weights/yolov3-tiny.conv.15
     ./darknet detector train coco/atv_rider_obj_4.data coco/yolov3_2.cfg weights/darknet53.conv.74 -gpus 0,1
     ./darknet detector train coco/atv_rider_obj_4.data coco/yolov3_2.cfg weights/darknet53.conv.74 -gpus 0,1,2,3
     ```

     - YOLOv3-tiny : weight=yolov3-tiny.conv.15, cfg=yolov3-tiny-obj.cfg
     - YOLOv3 : weight=darknet53.conv.74, cfg=yolo-obj.cfg
     - YOLOv3-SPP : weight=yolov3-spp.weights, cfg=yolov3-spp.cfg

  9. 탐지하기(결과 확인)

     ```bash
     # Darknet
     ./darknet detect cfg/yolov3.cfg yolov3.weights data/dog.jpg
     ./darknet detector test cfg/coco.data cfg/yolov3.cfg yolov3.weights data/dog.jpg
     ```

     - https://github.com/ultralytics/yolov3#inference
     - 대상 폴더나 이미지를 지정하지 않으면 ./data/sample/ 에 있는 모든 이미지를 대상으로 수행하고 ./output/  에 모든 결과를 저장한다

  10. 학습 그래프 확인하기

      ```bash
      
      ```

  ---

  ### Train-Process-Ultralytics

  - https://github.com/ultralytics/yolov3 - 뭔가.. 학습이 제대로 안된다

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
  
  # file_path_write
  python file_path_write.py --folder="coco/images/val"
  
  # Delete No Labeling Image
  python delete_no_label_file.py --folder="./coco/images/train/"
  
  # Train
  python train.py --cfg="coco/yolov3-tiny.cfg" --data="coco/atv_rider_obj_2.data" --weight="weights/yolov3-tiny.conv.15"
  
  # Detect
  python detect.py --cfg="coco/yolov3-tiny.cfg" --data="coco/atv_rider_obj_1.data" --weight="weights/last.pt"  
  python detect.py --cfg="cfg/yolov3-tiny.cfg" --weights="weights/yolov3-tiny.weights"
  ```

-  ### Train Output

  - https://github.com/ultralytics/yolov3/issues/403

  ``` bash
  Epoch   gpu_mem      GIoU       obj       cls     total   targets  img_size
  0/272        0G      4.48     0.488         0      4.97         2       416
  0/272        0G      4.48     0.488         0      4.97         2       416
  ```

  - **Train Processing**
  - GIoU : box regression loss
  - obj : objectness loss
  - cls : class loss
  - total : total loss
  - targets : number of targets (objects) per batch,

  ```bash
  Class    Images   Targets         P         R       mAP        F1
    all       275         0         0         0         0         0
  ```

  - **Evaluation of the current network on the validation set**
  - mAP : 0
  - F1 : 0

---

## Darknet Train on Colab

- (Origin Site)http://blog.ibanyez.info/blogs/coding/20190410-run-a-google-colab-notebook-to-train-yolov3-using-darknet-in/
- (.ipynb)https://colab.research.google.com/drive/1lTGZsfMaGUpBG4inDIQwIJVW476ibXk_#scrollTo=LJZRcEw0LoBd

1. GPU runtime 환경 설정
   - Colab **> Menu > Runtime > Configure Runtime Type** And select **GPU** From the **Hardware accelerator** drop down meu
   - 상단바 > 런타임 > 런타임 유형 변경 > 하드웨어 가속기 > GPU
2. 