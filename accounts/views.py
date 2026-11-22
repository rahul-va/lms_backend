from django.shortcuts import render

from rest_framework.views import APIView

from accounts.serializer import TrainerSerializer,TrainerProfileSerializer

from rest_framework.generics import CreateAPIView

from rest_framework.response import Response

from accounts.models import User,TrainerProfile

# Create your views here.
class TrainerSignUpView(CreateAPIView):

    serializer_class = TrainerSerializer

from rest_framework import authentication,permissions

class TrainerProfileRetriveUpdateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        auth_user = request.user

        qs = TrainerProfile.objects.get(user=auth_user)

        serializer_instance = TrainerProfileSerializer(qs)

        return Response(serializer_instance.data)

    def put(self,request):

        form_data = request.data

        instance = TrainerProfile.objects.get(user=request.user)

        serializer_instance = TrainerProfileSerializer(data=form_data,instance=instance)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

