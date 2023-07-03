from django.http import JsonResponse
import dotenv, requests, json, os
from surepass.models import AadhaarAPI, OtpVerificationAPI, PanAPI
from surepass.serializers import AadhaarResponseSerializer, OtpResponseSerializer, PanResponseSerializer
from rest_framework import generics , status
from utils.restful_response import send_response

class PanVerificationView(generics.CreateAPIView):
    queryset=PanAPI.objects.all()
    serializer_class=PanResponseSerializer
    def post(self, request):
        dotenv.load_dotenv(".env")  # Load environment variables from .env file
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Pan_api=PanAPI()

        user = request.user  # Get the current user
        serializer.validated_data['user'] = user

        if not serializer.is_valid():
            return send_response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.error_messages,
                ui_message='Validation error occurred',
                developer_message='Validation error occurred'
        )
        pan_number = request.data.get("pan_number")
        Pan_api.pan_number=pan_number

        url =  os.getenv("pan_url")

        payload = json.dumps({
            "id_number": pan_number
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': os.getenv("Authorization"),
        }

        response = requests.post(url, headers=headers, data=payload)
        data = response.json()
        Pan_api.response_data=data
        Pan_api.save()
        #return JsonResponse(data)
        return send_response(
            status=status.HTTP_200_OK,
            data=data,
            ui_message='Your response recorded succesfully',
            developer_message="Your response recorded succesfully "
           
        ) 
    

class AadhaarVerificationView(generics.CreateAPIView):
    queryset=AadhaarAPI.objects.all()
    serializer_class=AadhaarResponseSerializer
    def post(self, request):
        dotenv.load_dotenv(".env")  # Load environment variables from .env file
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user  # Get the current user
        serializer.validated_data['user'] = user

        if not serializer.is_valid():
            return send_response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.error_messages,
                ui_message='Validation error occurred',
                developer_message='Validation error occurred'
        )
        aadhaar_number = request.data.get("aadhaar_number")

        url = os.getenv("aadhaar_url") 

        payload = json.dumps({
            "id_number": aadhaar_number
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': os.getenv("Authorization"),
        }

        response = requests.post(url, headers=headers, data=payload)
        data = response.json()

        #return JsonResponse(data)
        return send_response(
            status=status.HTTP_200_OK,
            data=data,
            ui_message='Your response recorded succesfully',
            developer_message="Your response recorded succesfully "
           
        ) 


class OtpVerificationView(generics.CreateAPIView):
    queryset=OtpVerificationAPI.objects.all()
    serializer_class=OtpResponseSerializer
    def post(self, request):
        dotenv.load_dotenv(".env")  # Load environment variables from .env file
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user  # Get the current user
        serializer.validated_data['user'] = user

        if not serializer.is_valid():
            return send_response(
                status=status.HTTP_400_BAD_REQUEST,
                data=serializer.error_messages,
                ui_message='Validation error occurred',
                developer_message='Validation error occurred'
        )
        client_id = request.data.get("client_id")
        otp = request.data.get("otp")

        url = os.getenv("aadhaar_otp_submit") 

        payload = json.dumps({
            "client_id":client_id,
            "otp": otp
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': os.getenv("Authorization"),
        }

        response = requests.post(url, headers=headers, data=payload)
        data = response.json()

        #return JsonResponse(data)
        return send_response(
            status=status.HTTP_200_OK,
            data=data,
            ui_message='Your response recorded succesfully',
            developer_message="Your response recorded succesfully "
           
        ) 
