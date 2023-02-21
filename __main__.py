import sounddevice as sd
import soundfile as sf
import serial
import threading
from sound_classifier_model.test import predict

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

    flag = False  # 아이 혹은 반려동물이 차량에 있는 경우

    while True:
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
            flag = True
            pass

        # 시리얼 통신으로부터 데이터 읽기
        # 시리얼 버퍼에 데이터가 있는 경우
        if ser.in_waiting > 0:
            # 데이터 읽기
            data = ser.readline().decode().rstrip()
            ser.flushInput()
            if flag == True and data >= 40:
                # 위험 문자를 부모 혹은 반려인간에게 보낸 후 에어컨 제어시스템 가동.
                pass

            # 파일에 데이터 쓰기
            with open("temperature.txt", "a") as f:
                f.write(data + "\n")



if __name__ == '__main__':
    main()