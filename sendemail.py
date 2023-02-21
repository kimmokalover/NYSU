import sys
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(user_info):
    # 이메일을 보낼 계정 정보 입력
    user = 'kimmokalover@naver.com'
    password = '!levelup124'

    # 이메일을 보낼 대상 정보 입력
    recipient = user_info['email']
    name = user_info['name']
    age = user_info['age']
    phone = user_info['phone']
    status = user_info['status']

    if status == 1:
        # 이메일 제목과 본문 작성
        subject = '안녕하세요, {name}님. 자녀나 반려동물이 차 안에 있습니다.'.format(name=name)
        body = '''
        안녕하세요, {name}님.
        차 안에 자녀나 반려동물이 있음을 알려드립니다.
        차량번호: {license_plate}
        연락처: {phone}
        '''.format(name=name, license_plate=user_info['license_plate'], phone=phone)

        # 이메일 구성
        message = MIMEMultipart()
        message['From'] = user
        message['To'] = recipient
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # 이메일 전송
        try:
            server = smtplib.SMTP('smtp.naver.com', 587)
            server.starttls()
            server.login(user, password)
            text = message.as_string()
            server.sendmail(user, recipient, text)
            server.quit()
            print('이메일 전송 완료')
        except Exception as e:
            print(e)


    elif status == 2:
        # 이메일 제목과 본문 작성
        temperature = user_info['temperature']
        subject = '안녕하세요, {name}님. 온도가 너무 높아 적정 온도로 가동합니다.'.format(name=name)
        body = '''
        안녕하세요, {name}님.
        온도가 너무 높아 적정 온도로 가동합니다.
        차량번호: {license_plate}
        연락처: {phone}
        차량 내부 온도: {temperature}
        '''.format(name=name, license_plate=user_info['license_plate'], phone=phone, temperature=temperature)

        # 이메일 구성
        message = MIMEMultipart()
        message['From'] = user
        message['To'] = recipient
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # 이메일 전송
        try:
            server = smtplib.SMTP('smtp.naver.com', 587)
            server.starttls()
            server.login(user, password)
            text = message.as_string()
            server.sendmail(user, recipient, text)
            server.quit()
            print('이메일 전송 완료')
        except Exception as e:
            print(e)


    elif status == 3:
        # 이메일 제목과 본문 작성
        temperature = user_info['temperature']
        subject = '안녕하세요, {name}님. 에어컨 제어에 실패하여 응급상황입니다.'.format(name=name)
        body = '''
        안녕하세요, {name}님.
        에어컨 제어에 실패하여 응급상황입니다.
        차량번호: {license_plate}
        연락처: {phone}
        차량 내부 온도: {temperature}
        '''.format(name=name, license_plate=user_info['license_plate'], phone=phone, temperature=temperature)

        # 이메일 구성
        message = MIMEMultipart()
        message['From'] = user
        message['To'] = recipient
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # 이메일 전송
        try:
            server = smtplib.SMTP('smtp.naver.com', 587)
            server.starttls()
            server.login(user, password)
            text = message.as_string()
            server.sendmail(user, recipient, text)
            server.quit()
            print('이메일 전송 완료')
        except Exception as e:
            print(e)


    elif status == 4:
        # 이메일 제목과 본문 작성
        temperature = user_info['temperature']
        subject = '안녕하세요, {name}님. 에어컨 제어에 성공하였습니다.'.format(name=name)
        body = '''
        안녕하세요, {name}님.
        에어컨 제어에 성공하였습니다.
        차량번호: {license_plate}
        연락처: {phone}
        차량 내부 온도: {temperature}
        '''.format(name=name, license_plate=user_info['license_plate'], phone=phone, temperature=temperature)

        # 이메일 구성
        message = MIMEMultipart()
        message['From'] = user
        message['To'] = recipient
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # 이메일 전송
        try:
            server = smtplib.SMTP('smtp.naver.com', 587)
            server.starttls()
            server.login(user, password)
            text = message.as_string()
            server.sendmail(user, recipient, text)
            server.quit()
            print('이메일 전송 완료')
        except Exception as e:
            print(e)

if __name__ == '__main__':
    user_info = json.loads(sys.argv[1])
    send_email(user_info)