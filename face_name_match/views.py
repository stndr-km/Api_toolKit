from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import generics, status
from utils.restful_response import send_response
import face_recognition
from fuzzywuzzy import fuzz
from face_name_match.models import Facematching,StringMatching
from face_name_match.serializer import FaceMatchingSerializer, StringMatchingSerializer
# Create your views here.
from rest_framework.permissions import IsAuthenticated,IsAdminUser



    
class FacematchingView(generics.CreateAPIView):
    queryset=Facematching.objects.all()
    serializer_class = FaceMatchingSerializer
    
    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        user = request.user  # Get the current user
        serializer.validated_data['user'] = user

        

        face_matching=Facematching()
        image1 = face_recognition.load_image_file(request.FILES.get('image1'))
        image2 = face_recognition.load_image_file(request.FILES.get('image2'))
    
        face_matching.image1=request.data.get("image1")
        face_matching.image2=request.data.get("image2")
        
        # Detect the faces in each image
        face_locations1 = face_recognition.face_locations(image1)
        face_encodings1 = face_recognition.face_encodings(image1, face_locations1)
        face_locations2 = face_recognition.face_locations(image2)
        face_encodings2 = face_recognition.face_encodings(image2, face_locations2)

        # Compare the faces
        if len(face_encodings1) > 0 and len(face_encodings2) > 0:
            face_encoding1 = face_encodings1[0]
            face_encoding2 = face_encodings2[0]
            face_distances = face_recognition.face_distance([face_encoding1], face_encoding2)
            match_percentage = round((1 - face_distances[0]) * 100, 2)

            face_matching.match_percentage=match_percentage
            

            if match_percentage >= 50:
                
                response_data = {
                    'match_percentage': match_percentage,
                    'ui_message': 'The faces match with a certainty of {}%.'.format(match_percentage),
                    'developer_message': 'The faces match with a certainty of {}%.'.format(match_percentage)
                }
                face_matching.message='The faces match with a certainty of {}%.'.format(match_percentage)
                face_matching.user = user
                face_matching.save()
                return Response(response_data, status=status.HTTP_201_CREATED)
            else:
                match_perc=100-match_percentage
                
                
                response_data = {
                    # 'match_percentage': match_perc,   
                    'ui_message': 'The faces is not matching with a certainty of {}%. '.format(match_perc),
                    'developer_message': 'The faces do not match.'
                }
                face_matching.message='The faces is not matching with a certainty of {}%. '.format(match_perc)
                face_matching.user = user
                face_matching.save()
                return Response(response_data, status=status.HTTP_200_OK)
            
            
        else:
            response_data = {
                'match_percentage': None,
                'ui_message': 'Could not detect faces in both images.',
                'developer_message': 'Could not detect faces in both images.'
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        

class StringMatchingView(generics.CreateAPIView):

    queryset=StringMatching.objects.all()
    serializer_class=StringMatchingSerializer
    # permission_classes=[IsAuthenticated]/

    def post(self,request ,*args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = request.user  # Get the current user
            serializer.validated_data['user'] = user

            name1=request.data.get("name1")
            name2=request.data.get("name2")

        
            print("valid")
            string_matching=StringMatching()
            
            string_matching.name1=name1
            string_matching.name2=name2

            similarity_ratio = fuzz.ratio(name1, name2)

            string_matching.match_percentage=similarity_ratio
            print(string_matching.name1,similarity_ratio)
            string_matching.user = user
            string_matching.save()
            
            if similarity_ratio>70:
                return send_response(
                    status=status.HTTP_201_CREATED,
                    ui_message='The names is matching with a certainty of {}%. '.format(similarity_ratio),
                    developer_message="The names are matching"
                )
            else:
                return send_response(
                    status=status.HTTP_201_CREATED,
                    ui_message='The names is not matching with a certainty of {}%. '.format(similarity_ratio),
                    developer_message="The names are not matching correctly"
                )
            
        else:
            return send_response(
                status=status.HTTP_400_BAD_REQUEST,
                ui_message='Provided names are invalid or empty',
                developer_message="Inavlid names "
            )

