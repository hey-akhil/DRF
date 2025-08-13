from django.core.serializers import serialize
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .serializers import StudentSerializer, EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from students.models import Students
from employees.models import Employee
from django.http import Http404
from rest_framework import mixins,generics, viewsets



class EmployeeViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request, pk=None):
        emp = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(emp)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self,request,pk=None):
        emp = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors)

    def delete(self,request, pk=None):
        emp = get_object_or_404(Employee, pk=pk)
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




"""
# Genric >> RetrieveUpdateDestroyAPIView
class Employees(generics.ListAPIView, generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeesDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = "id"

"""

""" MIX-IN
----------------------------------------------------------------------------------------------------------
class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request):
        return self.list(request)

    def post(self,request):
        return self.create(request)

class EmployeesDetailsView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin ,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = "id"

    def get(self,request,id):
        return self.retrieve(request, id)

    def delete(self,request,id):
        return self.destroy(request, id)

    def put(self,request, id):
        return self.update(request,id)
"""



""" Using class as a View:
-------------------------------------------------------------------------------------------
#Employee Model using class view functionality

class Employees(APIView):

    def get(self,request):
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self,request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeesDetailsView(APIView):
    def get_object(self,primary_key):
        try:
            return Employee.objects.get(id=primary_key)
        except Employee.DoesNotExist:
           raise Http404

    def get(self,request, primary_key):
        emp = self.get_object(primary_key)
        serializer = EmployeeSerializer(emp)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self,request,primary_key):
        try:
            emp = self.get_object(primary_key)
            emp.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self,request,primary_key):
        emp = self.get_object(primary_key)
        serializer = EmployeeSerializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
"""

#Student
@api_view(['GET','POST'])
def studentsView(request):
    if request.method == "GET":
        students = Students.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def studentDetailView(request,primary_key):
    try:
        students = Students.objects.get(id=primary_key)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(students)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = StudentSerializer(students, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Students.delete(students)
        return Response(status=status.HTTP_204_NO_CONTENT)

    else:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
