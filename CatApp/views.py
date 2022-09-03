from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from CatApp.models import Cats,Employees
from CatApp.serializers import CatSerializer,EmployeeSerializer

from django.core.files.storage import default_storage

# Create your views here.

@csrf_exempt
def catApi(request,id=0):
    if request.method=='GET':
        cats = Cats.objects.all()
        cats_serializer=CatSerializer(cats,many=True)
        return JsonResponse(cats_serializer.data,safe=False)
    elif request.method=='POST':
        cat_data=JSONParser().parse(request)
        cats_serializer=CatSerializer(data=cat_data)
        if cats_serializer.is_valid():
            cats_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        cat_data=JSONParser().parse(request)
        cat=Cats.objects.get(CatId=cat_data['CatId'])
        cats_serializer=CatSerializer(cat,data=cat_data)
        if cats_serializer.is_valid():
            cats_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        cat=Cats.objects.get(CatId=id)
        cat.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_serializer=EmployeeSerializer(employees,many=True)
        return JsonResponse(employees_serializer.data,safe=False)
    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employees_serializer=EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        employee_data=JSONParser().parse(request)
        employee=Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employees_serializer=EmployeeSerializer(employee,data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        employee=Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)
