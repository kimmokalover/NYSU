import sounddevice as sd
import soundfile as sf
import serial
from sound_classifier_model.test import predict
import requests
import time
from Detector.detect import detect_person_or_dog

child_or_pet = False
license_plate = '1234'


def send_child_or_pet_in_car(url, data):
    response = requests.post(url, data=data)
    return response

def turn_on_airconditioner(url, data):
    response = requests.post(url, data=data)
    return response

def emergency(url, data):
    response = requests.post(url, data=data)
    return response

def main():
    # 시리얼 포트와 통신 속도 설정
    port = "/dev/ttyACM0" # 포트명은 사용자의 환경에 따라 다름
    baudrate = 9600

    # 시리얼 통신 시작
    ser = serial.Serial(port, baudrate)

    # 녹음할 설정
    duration = 4  # 녹음할 시간 (초)
    fs = 44100  # 샘플링 주파수
    channels = 2  # 채널 수

    child_or_pet = False  # 아이 혹은 반려동물이 차량에 있는 경우

    while True:
        if not child_or_pet:
            #카메라로 감지하기
            child_or_pet = detect_person_or_dog()
            if child_or_pet:
                url = 'https://nysu-awolm.run.goorm.site/api/child_or_pet_in_car/'
                data = {'child_or_pet':child_or_pet, 'license_plate':license_plate}
                send_child_or_pet_in_car(url, data)
                continue
            # 녹음 시작
            print("녹음을 시작합니다.")
            recording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
            sd.wait()  # 녹음이 끝날 때까지 대기

            # 녹음된 음성 파일로 저장
            filename = "recorded.wav"
            sf.write(filename, recording, fs)
            print(f"{filename} 파일이 저장되었습니다.")
            predict_class = predict()

            # 만약 예측값이 강아지가 짖는 것이라면
            if predict_class == "dog_bark":
                # 부모나 보호자에게 차량에 반려견이 존재한다고 알림 메세지 전송
                child_or_pet = True
                url = 'https://nysu-awolm.run.goorm.site/api/child_or_pet_in_car/'
                data = {'child_or_pet':child_or_pet, 'license_plate':license_plate}
                print(send_child_or_pet_in_car(url, data))

        # 시리얼 통신으로부터 데이터 읽기
        # 시리얼 버퍼에 데이터가 있는 경우
        if ser.in_waiting > 0:
            # 데이터 읽기
            Data = ser.readline().decode().rstrip()
            Data = float(Data)
            print(Data)
            ser.flushInput()
            if child_or_pet == True and Data >= 40:
                url = 'https://nysu-awolm.run.goorm.site/api/turn_on_airconditioner/'
                data = {'temperature':Data,'child_or_pet':child_or_pet, 'license_plate':license_plate}
                ret = turn_on_airconditioner(url, data)
                print(ret)
                
                
                time.sleep(10)
                ser.flushInput()
                Data = ser.readline().decode().rstrip()
                Data = float(Data)
                if Data >= 40:
                    url = 'https://nysu-awolm.run.goorm.site/api/emergency/'
                    data = {'child_or_pet':child_or_pet, 'license_plate':license_plate, 'temperature':Data, 'airconditioner_status':'0'}
                    print(emergency(url,data))
                #에어컨 시스템 제동 실패
                else :
                    url = 'https://nysu-awolm.run.goorm.site/api/emergency/'
                    data = {'child_or_pet':child_or_pet, 'license_plate':license_plate, 'temperature':Data, 'airconditioner_status':'1'}
                    print(emergency(url,data))


            # 파일에 데이터 쓰기
            with open("temperature.txt", "a") as f:
                f.write(str(Data) + "\n")



if __name__ == '__main__':
    main()