from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile

from .serializers import ProfileSerializer


# Create your views here.

class MyProfile(APIView):
    def get(self, request):
        my_profile = Profile()
        my_profile.slackUsername = 'SamDodo'
        my_profile.backend = True
        my_profile.age = 25
        my_profile.bio = 'A willful and determined person that loves challenges and does not give up'
        serializer = ProfileSerializer(my_profile)
        return Response(serializer.data)

