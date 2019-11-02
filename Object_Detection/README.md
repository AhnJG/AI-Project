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

---

## YOLO-V3-Train

- https://github.com/ultralytics/yolov3

- https://pjreddie.com/darknet/yolo/

- https://zeuseyera.github.io/darknet-kr/SaYongBeob_Yolo-v3.html

- https://eungbean.github.io/2018/11/07/yolo-for-realtime-food-recognition/

- https://yeonsuuu-uuu.tistory.com/2

- Paper : https://pjreddie.com/media/files/papers/YOLOv3.pdf

- mAP : Yolo spp > yolo > yolo-tiny (CoCo Data Set Test)

  |             |    320     |    416     |    608     |
  | :---------: | :--------: | :--------: | :--------: |
  |   YOLOv3    | 51.8(51.5) | 55.4(55.3) | 58.2(57.9) |
  | YOLOv3-SPP  |    52.6    |    57.0    | 60.7(60.6) |
  | YOLOv3-tiny |    29.0    | 32.9(33.1) |    35.5    |

  - 320, 416, 608은 입력 이미지 사이즈이다

- ### Train Process

  1. obj.data 파일 만들기

     ```data
     classes= 2
     train  = ./opencv/data/train.txt
     valid  = ./opencv/data/valid.txt
     names = ./opencv/data/obj.names
     backup = backup/
     ```

  2. obj.names 파일 만들기 

     - Detect 하고 싶은 물체를 차례대로 입력한다
     - person부터 차례대로 0~의 값을 가진다(person:0, bicycle:1)

     ```names
     person
     bicycle
     car
     motorcycle
     airplane
     ```

  3. 학습시킬 이미지와 라벨링된 파일을 같은 폴더안에 넣어준다

     ```txt
     atv_rider0000.jpg
     atv_rider0000.txt
     atv_rider0001.jpg
     atv_rider0001.txt
     ```

     - 라벨링 파일 형식(object-class, x, y, width, height)

       ```txt
       0 0.270909 0.742727 0.287273 0.416364
       ```

  4. obj.data의 train과 valid에 설정된 경로에 train.txt와 valid.txt를 만든다

     - 학습시킬 이미지들의 경로를 지정해주면 된다

     ```txt
     YOLO-V3-Train/coco/images/train/atv_rider1126.jpg
     YOLO-V3-Train/coco/images/train/atv_rider1132.jpg
     YOLO-V3-Train/coco/images/train/atv_rider0204.jpg
     YOLO-V3-Train/coco/images/train/atv_rider0576.jpg
     YOLO-V3-Train/coco/images/train/atv_rider0984.jpg
     YOLO-V3-Train/coco/images/train/atv_rider0990.jpg
     ```

  5. Pre-Trained된 Convolutional Layers를 다운받는다

     - wget https://pjreddie.com/media/files/darknet53.conv.74
     - https://drive.google.com/drive/folders/1uxgUBemJVw9wZsdpboYbzUN4bcRhsuAI
     - Darknet `*.weights` format: https://pjreddie.com/media/files/yolov3.weights
     - PyTorch `*.pt` format: https://drive.google.com/drive/folders/1uxgUBemJVw9wZsdpboYbzUN4bcRhsuAI

  6. Cfg 파일 수정

     - batch=64

       - 만약 out of memory 에러가 뜨며 학습이 되지 않을 경우 batch와 subdivisions를 변경합니다.

         Batch는 4의 배수로, subdivisions는 2의 배수로 맞춰줍니다.

         (batch는 클 수록, subdivisions는 작을 수록 정확도가 높아지지만 학습이 느리고 그래픽 메모리가 많이 필요합니다)

     - subdivisions=8
       - subdivision을 8로 수정합니다. 이 뜻은 batch를 8개로 나누어 GPU 메모리 부하를 줄이겠다는 의도입니다.

     - classes =1 Detection하고 싶은 물체의 개수

     - filters = (classes+5)*3 으로 입력 (line 127,171)

     - max_batches = 4000 * 클래스 갯수
     - 저자에 의하면 class당 2,000 iteration을 권하고 있습니다.

  7. 학습 시작

     ```bash
     python train.py --cfg="coco/yolov3-tiny.cfg" --data="coco/atv_rider_obj_2.data" --weight="weights/yolov3-tiny.conv.15"
     ```

     - YOLOv3-tiny : weight=yolov3-tiny.conv.15, cfg=yolov3-tiny-obj.cfg
     - YOLOv3 : weight=darknet53.conv.74, cfg=yolo-obj.cfg
     - YOLOv3-SPP : weight=yolov3-spp.weights, cfg=yolov3-spp.cfg

  8. 탐지하기(결과 확인)

     ```bash
     python detect.py --cfg="cfg/yolov3-tiny.cfg" --weights="weights/yolov3-tiny.weights"
     ```

     - https://github.com/ultralytics/yolov3#inference
     - 대상 폴더나 이미지를 지정하지 않으면 ./data/sample/ 에 있는 모든 이미지를 대상으로 수행하고 ./output/  에 모든 결과를 저장한다

  9. 학습 그래프 확인하기

     ```bash
     
     ```

     

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
  
  # Train
  python train.py --cfg="coco/yolov3-tiny.cfg" --data="coco/atv_rider_obj_1.data" --weight="weights/darknet53.conv.74"
  python train.py --cfg="coco/yolov3-tiny.cfg" --data="coco/atv_rider_obj_2.data" --weight="weights/yolov3-tiny.weights"
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