from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Company,Empoly
from .serilazers import CompanySerilaers,EmpolySerilazers
from rest_framework.decorators import action


# Create your views here.

class Companyviewset(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerilaers
    @action(detail=True,methods=['get'])
    def employ(self,request,pk=None):
        company=Company.objects.get(pk=pk)
        emps=Empoly.objects.filter(company=company)
        emps_serilazers=EmpolySerilazers(emps,many=True,context={
            'request':request})
        return Response(emps_serilazers)
        



class Empolyviewset(viewsets.ModelViewSet):
    queryset=Empoly.objects.all()
    serializer_class=EmpolySerilazers

