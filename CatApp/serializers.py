from rest_framework import serializers
from CatApp.models import Cats, Employees

class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cats
        fields=('CatId','CatName','Age','DateOfArrival','Needs','PhotoFileName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=('EmployeeId','EmployeeName','Position','StartDate','Pay')