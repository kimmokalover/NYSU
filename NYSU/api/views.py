from django.shortcuts import render
from .models import User
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
import subprocess
import json


# e-mail 보내는 프로그램의 위치
program_path = "/home/kimmokalover/바탕화면/hackerton/sendemail.py"

@api_view(['POST'])
def child_or_pet_in_car(request):
    if request.method == 'POST':
        child_or_pet = request.data.get('child_or_pet', True)
        license_plate = request.data.get('license_plate')
        if child_or_pet:
            # 해당 정보를 처리하고, HTTP 201 Created 상태코드와 함께 응답
            try:
                user = User.objects.get(license_plate=license_plate)
            except User.DoesNotExist:
                return Response({'message': '해당하는 사용자 정보가 없습니다.'}, status=404)

            # e-mail 프로그램 실행
            user_info = {'name': user.name, 'age': user.age, 'phone': user.contact_number, 'email': user.email, 'status': 1, 'license_plate': user.license_plate}
            subprocess.run(["python", program_path, json.dumps(user_info)])

            return Response({'message': '아이나 반려동물이 차 안에 있습니다.', 'license_plate' : license_plate, 'status' : 1}, status=201)
        else:
            # HTTP 400 Bad Request 상태코드와 함께 응답
            return Response({'message': '아이나 반려동물이 차 안에 없습니다.'}, status=400)


@api_view(['POST'])
def turn_on_airconditioner(request):
    if request.method == 'POST':
        temperature = request.data.get('temperature', 40)
        license_plate = request.data.get('license_plate')
        if temperature >= 40:
            child_or_pet = request.data.get('child_or_pet', True)
            if child_or_pet :
                try:
                    user = User.objects.get(license_plate=license_plate)
                except User.DoesNotExist:
                    return Response({'message': '해당하는 사용자 정보가 없습니다.'}, status=404)

                # e-mail 프로그램 실행
                user_info = {'name': user.name, 'age': user.age, 'phone': user.contact_number, 'email': user.email, 'status': 2, 'license_plate': user.license_plate, 'temperature':temperature}
                subprocess.run(["python", program_path, json.dumps(user_info)])
            else:
                # HTTP 400 Bad Request 상태코드와 함께 응답
                return Response({'message': '에어컨 가동할 필요가 없습니다.'}, status=400)


            # 해당 정보를 처리하고, HTTP 201 Created 상태코드와 함께 응답
            return Response({'message': '온도가 너무 높아 적정 온도로 가동합니다.'}, status=201)
        else:
            # HTTP 400 Bad Request 상태코드와 함께 응답
            return Response({'message': '에어컨 가동할 필요가 없습니다.'}, status=400)


@api_view(['POST'])
def emergency(request):
    if request.method == 'POST':
        # 에어컨 제어 실패 여부를 판단하여 처리
        airconditioner_status = request.data.get('airconditioner_status', False)
        license_plate = request.data.get('license_plate')
        temperature = request.data.get('temperature')
        
        try:
            user = User.objects.get(license_plate=license_plate)
        except User.DoesNotExist:
            return Response({'message': '해당하는 사용자 정보가 없습니다.'}, status=404)

        if not airconditioner_status:
            # 에어컨 제어 실패시, 응급상황으로 처리하고, HTTP 201 Created 상태코드와 함께 응답
            user_info = {'name': user.name, 'age': user.age, 'phone': user.contact_number, 'email': user.email, 'status': 3, 'license_plate': user.license_plate, 'temperature': temperature}
            subprocess.run(["python", program_path, json.dumps(user_info)])
            return Response({'message': '에어컨 제어에 실패하여 응급상황입니다.'}, status=201)
        else:
            # HTTP 400 Bad Request 상태코드와 함께 응답
            user_info = {'name': user.name, 'age': user.age, 'phone': user.contact_number, 'email': user.email, 'status': 4, 'license_plate': user.license_plate, 'temperature': temperature}
            subprocess.run(["python", program_path, json.dumps(user_info)])
            return Response({'message': '에어컨 제어가 정상적으로 이루어졌습니다.'}, status=400)