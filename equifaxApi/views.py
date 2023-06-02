from django.shortcuts import render

# Create your views here.
import requests
from rest_framework.views import APIView
from rest_framework import generics, status

from rest_framework.response import Response
from equifaxApi.serializer import EquifaxResponseSerializer
from equifaxApi.models import EquifaxAPI

class EquifaxAPIView(generics.CreateAPIView):
    queryset=EquifaxAPI.objects.all()
    serializer_class = EquifaxResponseSerializer

    def post(self, request):
        
        FirstName=request.GET.get('FirstName')
        DOB=request.GET.get('DOB')
        AddressLine1=request.GET.get('AddressLine1')
        State=request.GET.get('State')
        Postal=request.GET.get('Postal')
        PanNumber=request.GET.get('PanNumber')
        print(FirstName)
        
        # Make the request to the Equifax Bureau API

        url = "https://eportuat.equifax.co.in/cir360Report/cir360Report"
        headers = {'Content-Type': 'application/json'}
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
            },
            "RequestBody": {
                    "InquiryPurpose": "00",
                    "FirstName": FirstName,
                    "DOB": "1960-05-30",
                    "InquiryAddresses": [
                        {
                            "seq": "1",
                            "AddressType": ["H"],
                            "AddressLine1": "169 RAJEEV NAGAR  TARLI KANDOLI DEHRADUN UTTARAKHAND DEHRADUN",
                            "State": "UK",
                            "Postal": "249145"
                        }
                    ],
                    "IDDetails": [
                        {
                            "seq": "1",
                            "IDType": "T",
                            "IDValue": "ARSPB2789E",
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

        try:
            response = requests.post(url, headers=headers, json=payload)
            print(response)
            if response.status_code == 200:
                # Save the response to the database
                equifax_response = EquifaxAPI.objects.create(
                    
                    FirstName=FirstName,
                    PanNumber=PanNumber,
                    DOB=DOB,
                    AddressLine1=AddressLine1,
                    State=State,
                    Postal=Postal,
                    response_data=response.json()
                )
                serializer = EquifaxResponseSerializer(equifax_response)
                return Response(serializer.data)
            else:
                return Response({"error": f"Request failed with status code: {response.status_code}"})
        except requests.exceptions.RequestException as e:
            return Response({"error": f"Request exception: {str(e)}"})

