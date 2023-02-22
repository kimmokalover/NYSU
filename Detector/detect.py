import cv2
import cvlib
from cvlib.object_detection import draw_bbox
import time

def detect_person_or_dog():
    cap = cv2.VideoCapture(0)
    start_time = time.time()
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        bbox, label, conf = cvlib.detect_common_objects(frame, model='yolov4', confidence=0.5, nms_thresh=0.3)
        for i in range(len(label)):
            if label[i] in ['person', 'dog']:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    cap.release()
                    return True
        out = draw_bbox(frame, bbox, label, conf, write_conf=False)
        cv2.imshow("Detection", out)
        if cv2.waitKey(1) == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            return False
    cap.release()
    cv2.destroyAllWindows()
    return False
