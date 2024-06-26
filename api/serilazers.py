from rest_framework import serializers
from . models import Company,Empoly


class CompanySerilaers(serializers.HyperlinkedModelSerializer):
    company_id=serializers.ReadOnlyField()
    class Meta:
        model=Company
        fields="__all__"


class EmpolySerilazers(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Empoly
        fields="__all__"
        
