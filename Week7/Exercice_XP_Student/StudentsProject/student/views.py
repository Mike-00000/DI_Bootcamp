from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt 
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from .models import Student
from .serializers import StudentSerializer

# Create your views here.


class StudentView(APIView):
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            student = Student.objects.get(id=kwargs['pk'])
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        else:
            queryset = Student.objects.all()
            serializer = StudentSerializer(queryset, many=True)
            return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk, *args, **kwargs):
        student = Student.objects.get(id=pk)
        student.delete()
        return Response()
    
    def put(self, request, pk, *args, **kwargs):
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



class StudentRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        student = self.get_object()
        serializer = self.serializer_class(student)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        student = self.get_object()
        serializer = self.serializer_class(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        student = self.get_object()
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)