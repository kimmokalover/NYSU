import cv2
import cvlib
from cvlib.object_detection import draw_bbox

cap = cv2.VideoCapture(0)

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

    for i in range(len(l)):
        if(l[i] == "person" or l[i] == "dog"):
            bbox.append(b[i])
            label.append(l[i])
            conf.append(c[i])


    out = draw_bbox(frame, bbox, label, conf, write_conf=False)

    # 실시간 보여주기
    cv2.imshow("Baby Camer in Hyundai Car", out)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()