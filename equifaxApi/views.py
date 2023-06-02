from django.shortcuts import render

# Create your views here.
import requests
from rest_framework.views import APIView
from rest_framework import generics, status

from rest_framework.response import Response
from .serializers import EquifaxResponseSerializer

class EquifaxAPIView(generics.CreateAPIView):
    def post(self, request):
        request_body = request.data.get('requestBody')

        # Make the request to the Equifax Bureau API
        
        url = "https://eportuat.equifax.co.in/cir360Report/cir360Report"
        headers = {'Content-Type': 'application/json'}
        payload = {
            "RequestHeader": {
                "CustomerId": request_body.get("CustomerId"),
                "UserId": request_body.get("UserId"),
                "Password": request_body.get("Password"),
                # Add other fields from the requestBody if needed
            },
            "RequestBody": request_body,
            "Score": [
                {
                    "Type": "MCS",
                    "Version": "3.1"
                }
            ]
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code == 200:
                # Save the response to the database
                equifax_response = EquifaxResponse.objects.create(
                    customer_id=request_body.get("CustomerId"),
                    user_id=request_body.get("UserId"),
                    response_data=response.json()
                )
                serializer = EquifaxResponseSerializer(equifax_response)
                return Response(serializer.data)
            else:
                return Response({"error": f"Request failed with status code: {response.status_code}"})
        except requests.exceptions.RequestException as e:
            return Response({"error": f"Request exception: {str(e)}"})

