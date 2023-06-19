from rest_framework import generics
import requests
from django.http import JsonResponse

import dotenv
import json
import os
from EquifaxAPI.models import EquifaxAPI
from EquifaxAPI.serializer import EquifaxResponseSerializer
from utils.restful_response import send_response
from rest_framework import status

class EquifaxAPI(generics.CreateAPIView):
    queryset=EquifaxAPI.objects.all()
    serializer_class=EquifaxResponseSerializer

    def post(self, request):
        dotenv.load_dotenv("/home/abhishek/Desktop/drfx-new/.env")  # Load environment variables from .env file
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
        # Get parameters from request data 
        name = request.data.get("name")
        dob = request.data.get("dob")
        address = request.data.get("address")
        pan_number = request.data.get("pan_number")
        state = request.data.get("state")
        pincode = request.data.get("pincode")
        

        # Prepare JSON payload
        payload = {
            "RequestHeader": {
                "CustomerId": os.getenv("CustomerId"),
                "UserId": os.getenv("UserId"),
                "Password": os.getenv("Password"),
                "MemberNumber": os.getenv("MemberNumber"),
                "SecurityCode": os.getenv("SecurityCode"),
                "ProductVersion": os.getenv("ProductVersion"),
                "CustRefField": os.getenv("CustRefField"),
                "ProductCode": [os.getenv("ProductCode")],

            },
            "RequestBody": {
                "InquiryPurpose": "00",
                "FirstName": name,
                "DOB": dob,
                "InquiryAddresses": [
                    {
                        "seq": "1",
                        "AddressType": ["H"],
                        "AddressLine1": address,
                        "State": state,
                        "Postal": pincode
                    }
                ],
                "IDDetails": [
                    {
                        "seq": "1",
                        "IDType": "T",
                        "IDValue": pan_number,
                        "Source": "Inquiry"
                    }
                ]
            },
            "Score": [
                {
                    "Type": "MCS",
                    "Version": "3.1"
                }
            ]
        }

        # Make the POST request

        url = "https://eportuat.equifax.co.in/cir360Report/cir360Report"
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=payload, headers=headers)
        
        equifax_response = serializer.save(
                    name=name,
                    dob=dob,
                    address = address,
                    pan_number=pan_number,
                    state = state,
                    pincode = pincode,
                    response_data=response.json()
                )
       
        return send_response(
            status=status.HTTP_200_OK,
            data=json.dumps(response.json()),
            ui_message='Your response recorded succesfully',
            developer_message="Your response recorded succesfully "
           
        ) 

