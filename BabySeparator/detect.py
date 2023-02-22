import cv2
import cvlib
from cvlib.object_detection import draw_bbox

import requests

# API 정보
api = "https://nysu-eufbm.run.goorm.site/api/exist_in_car/"
response = requests.post(api, {
    "license_plate": "1234",
    "exist_state": "Camera send Connect"
})

# API 통신
if response.status_code == 200:
    print(f"API CONNECT! {response.status_code}")
else:
    print(f"Request failed with status code {response.status_code}") 
    exit()

cap = cv2.VideoCapture(0)

# 정보
car_num = 1234

# 감지 상태
baby_count = 0
dog_count = 0

baby_detect = False
dog_detect = False

while(True):
    # frame 캡쳐
    ret, frame = cap.read()

    # 1 -> 좌우반전, 0 -> 상하반전
    # frame = cv2.flip(frame, 1)

    if not ret: break #프레임 오류
    
    # 흑백
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 감지
    b, l, c = cvlib.detect_common_objects(frame, 0.5, 0.3, model="yolov8")

    bbox = []
    label = []
    conf = []

    current_baby_count = 0 # 현재 아기 수
    current_dog_count = 0 # 현재 강아지 수
    for i in range(len(l)):
        if(l[i] == "person" or l[i] == "dog"):
            bbox.append(b[i])
            label.append(l[i])
            conf.append(c[i])

        if(l[i] == "person"): current_baby_count += 1
        if(l[i] == "dog"): current_dog_count += 1

    if baby_count != current_baby_count:
        state = ""

        if baby_count > current_baby_count:
            state = f"Remove Baby {baby_count - current_baby_count}"
            baby_count = current_baby_count
        else:
            state = f"Add Baby {current_baby_count - baby_count}"
            baby_count = current_baby_count

        data = {
            "license_plate": car_num,
            "exist_state": state
        }

        response = requests.post(api, data=data)
    
    if dog_count != current_dog_count:
        state = ""

        if dog_count > current_dog_count:
            state = f"Remove Dog {dog_count - current_dog_count}"
            dog_count = current_dog_count
        else:
            state = f"Add Dog {current_dog_count - dog_count}"
            dog_count = current_dog_count

        data = {
            "license_plate": car_num,
            "exist_state": state
        }

        response = requests.post(api, data=data)


    out = draw_bbox(frame, bbox, label, conf, write_conf=False)

    # 실시간 보여주기
    cv2.imshow("Baby Camera in Hyundai Car", out)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
