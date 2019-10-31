# OpenCV



### Imread 

#### - Flag

- cv2.IRMEAD_GRAYSCALE: 우리가 방금 한 거예요. 사진을 흑백으로 읽어요. 0으로도 대체할 수 있어요.

- cv2.IMREAD_COLOR: 사진을 유색으로 읽을 수 있는데, 투명도가 다 무시되어요. cv2.imread()의 기본값은 이거예요. 1로도 대체할 수 있어요.

- cv2.IMREAD_UNCHANGED: 사진을 있는 그대로 읽어요. BGR 채널뿐만 아니라 투명도 채널까지 읽혀요. -1로도 대체할 수 있어요.



## Install 

- https://pypi.org/project/opencv-python/
- run `pip install opencv-python` if you need only main modules
- run `pip install opencv-contrib-python` if you need both main and contrib modules (check extra modules listing from [OpenCV documentation](https://docs.opencv.org/master/))