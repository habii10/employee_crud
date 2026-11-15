from django.shortcuts import render
from django.views.generic import View
from crm.models import Employee
from django.http import JsonResponse
from json import loads
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.
@method_decorator(csrf_exempt,name="dispatch")
class EmployeeCreateListView(View):
    def get(self,request):

        #for lis all employee
        qs=Employee.objects.all().values()#qs

        #converting qa to PYNT
        resonse_data=list(qs)

        #converting PYNT to json
        return JsonResponse(resonse_data,safe=False)

    def post(self,request):
        json_data=request.body
        form_data=loads(json_data)
        """"
         {"name":hari,
         "department":"hr",
         "email":"hari@gmail.com",
         "phone":"123454",
         "salary":13400,
         "location":"kakkanad"        
         """
        Employee.objects.create(
           name=form_data.get("name"),
           department=form_data.get("department"),
           email=form_data.get("email"),
           phone=form_data.get("phone"),
           salary=form_data.get("salary"),
           location=form_data.get("location")

           )
        response_data={"message":"created sucessfully"}
        return JsonResponse(response_data)
    
@method_decorator(csrf_exempt,name="dispatch")
class EmployeeRetrieveUpdateDeleteView(View):
    def get(self,request,pk=None):
        qs=Employee.objects.filter(id=pk).values()        
        response_data=list(qs)
        return JsonResponse(response_data,safe=False)

    def put(self,request,pk=None):
        json_data=request.body
        form_data=loads(json_data)

        Employee.objects.filter(id=pk).update(**form_data)

        response_data={"message":"updated successfully"}
        return JsonResponse(response_data)

    def delete(self,request,pk=None):
        Employee.objects.filter(id=pk).delete()
        response_data={"message":"deleted"}
        return JsonResponse(response_data)    
