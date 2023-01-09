from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegistrationSerializer, LoginSerializer


class RegistrationView(APIView):

    def post(self, request):

        serializer = RegistrationSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response('ТЫ ЗАРЕГАЛСЯ УСПЕШНА gl hf')




class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer