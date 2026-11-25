from django.shortcuts import render,get_object_or_404

# Create your views here.
from rest_framework.views import APIView

from course_management.models import Course

from rest_framework import authentication,permissions

from rest_framework.response import Response

from course_management.serailizer import CourseSerializer

#from rest_framework.generics import ListAPIView


class CourseListCreateView(APIView):

    serializer_class = CourseSerializer

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        qs = Course.objects.filter(trainer = request.user)
        serializer_instance = CourseSerializer(qs,many=True)
        return Response(serializer_instance.data)

    def post(self,request):

        from_data = request.data

        serializer_instance = CourseSerializer(data = from_data)

        if serializer_instance.is_valid():

            serializer_instance.save(trainer = request.user)
            return Response(serializer_instance.data)
        else:

            return Response(serializer_instance.errors)

class CourseRetriveUpdateDeleteView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,pk=None):

        qs = get_object_or_404(Course,id = pk)

        serializer_instance = CourseSerializer(qs)

        return Response(serializer_instance.data)

    def put(self,request,pk=None):

        form_data = request.data

        instance = get_object_or_404(Course,id = pk)

        serializer_instance = CourseSerializer(data = form_data,instance = instance)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)

    def delete(self,request,pk=None):

        instance = get_object_or_404(Course,id = pk)

        instance.delete()

        return Response({"message":"deleted"})