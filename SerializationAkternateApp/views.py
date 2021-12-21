from functools import partial
from django.shortcuts import render
from rest_framework.response import Response
from .models import Employee
from .serializers import EmpSerializer,EmpModelSerializer
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
# Create your views here.

class EmpViews(APIView):
    def get(self,request,pk=None,*args,**kwargs):
        if pk is not None:
            emp=Employee.objects.get(id=pk)
            eserializer=EmpSerializer(emp)
            return Response(eserializer.data)
        qs=Employee.objects.all()
        eserializer=EmpSerializer(qs,many=True)
        return Response(eserializer.data)
    
    def post(self,request,*args,**kwargs):
        data=request.data
        eserializer=EmpSerializer(data=data)
        if eserializer.is_valid():
            print(eserializer.validated_data)
            eserializer.save()
            return Response({'msg':'Data Added Successfully'})
        return Response(eserializer.errors,status=401)

    def put(self,request,pk,*args,**kwargs):
        data=request.data
        emp=Employee.objects.get(id=pk)
        eserializer=EmpSerializer(emp,data=data,partial=True)
        if eserializer.is_valid():
            print(eserializer.validated_data)
            eserializer.save()
            return Response({'msg':'Data Updated Successfully'})
        return Response(eserializer.errors,status=401)

    def delete(self,request,pk,*args,**kwargs):
        if pk is not None:
            emp=Employee.objects.get(id=pk)
            emp.delete()
            return Response({'msg':'Data Deleted Successfully'})
        return Response({'msg':'Please Provide a valid Primary Key Reference '})

# class EmployeMixinView(GenericAPIView,ListModelMixin):
#     queryset=Employee.objects.all()
#     serializer_class=EmpModelSerializer
#     def get(self,request,pk=None,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
class EmployeMixinListCreateView(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Employee.objects.all()
    serializer_class=EmpModelSerializer
    def get(self,request,pk=None,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,pk=None,*args,**kwargs):
        return self.create(request,*args,**kwargs)
class EmployeMixinRetrieveUpdateDestroyView(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Employee.objects.all()
    serializer_class=EmpModelSerializer
    def get(self,request,pk,*args,**kwargs):
        return self.retrieve(request,pk,*args,**kwargs)
    def put(self,request,pk,*args,**kwargs):
        return self.update(request,pk,*args,**kwargs)
    def patch(self,request,pk,*args,**kwargs):
        return self.partial_update(request,pk,*args,**kwargs)
    def delete(self,request,pk,*args,**kwargs):
        return self.destroy(request,pk,*args,**kwargs)

    






        



