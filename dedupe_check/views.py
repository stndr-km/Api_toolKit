from django.shortcuts import render
# from dedupe_check.models import DedueCheck
# from dedupe_check.serializer import DedueCheckSerializer
from rest_framework import generics,status
from utils.restful_response import send_response

# Create your views here.

# class DedueCheckView(generics.CreateAPIView):

#     queryset=DedueCheck.objects.all()
#     serializer_class=DedueCheckSerializer

#     def post(self,request ,*args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         deduecheck=DedueCheck()
#         user=request.data.get("user")
#         pan=request.data.get("pan")
#         deduecheck.user=user
#         deduecheck.pan=pan
#         deduecheck.save()

#         return send_response(
#                     status=status.HTTP_201_CREATED,
#                     ui_message='Created',
#                     developer_message="done"
#                 )
        

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connections


@api_view(['GET'])
def check_customer_exists(request):
    mobile_number = request.GET.get('mobile_number', '')
    exists = customer_exists(mobile_number)
    
    return Response({'exists': exists})

def customer_exists(mobile_number):
    with connections['default'].cursor() as cursor:
        # Execute the raw SQL query to check if the customer exists
        query = f"SELECT COUNT(*) FROM ifs_closed_customers WHERE mobile_no = '{mobile_number}'"
        cursor.execute(query)
        count = cursor.fetchone()[0]

    return count > 0  # Return True if count > 0, indicating that the customer exists
