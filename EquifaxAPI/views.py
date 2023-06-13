from rest_framework import generics
import requests
from django.http import JsonResponse
from django.views import View
import dotenv
dotenv.load_dotenv('.env')
import os
from EquifaxAPI.models import EquifaxAPI
from EquifaxAPI.serializer import EquifaxResponseSerializer

class EquifaxAPI(generics.CreateAPIView):
    queryset=EquifaxAPI.objects.all()
    serializer_class=EquifaxResponseSerializer

    def post(self, request):
        dotenv.load_dotenv()  # Load environment variables from .env file
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Validate the serializer's data

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
                "CustomerId": "21",
                "UserId": "UAT_ARTHIM",
                "Password": "V2*Pdhbr",
                "MemberNumber": "028FZ00016",
                "SecurityCode": "FR7",
                "ProductVersion": "4.5",
                "CustRefField": "123456",
                "ProductCode": ["CCR"]

            #     "CustomerId": os.environ.get("CustomerId"),
            #     "UserId": os.environ.get("UserId"),
            #     "Password": os.environ.get("Pass"),
            #     "MemberNumber": os.environ.get("MemberNumber"),
            #     "SecurityCode": os.environ.get("SecurityCode"),
            #     "ProductVersion": os.environ.get("ProductVersion"),
            #     "CustRefField": os.environ.get("CustRefField"),
            #     "ProductCode": [os.environ.get("ProductCode")]

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

        print(response.json())
        equifax_response = serializer.save(
                    name=name,
                    dob=dob,
                    address = address,
                    pan_number=pan_number,
                    state = state,
                    pincode = pincode,
                    response_data=response.json()
                )
        # Return the response as JSON
        return JsonResponse(response.json(), status=response.status_code)
