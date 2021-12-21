from django.db.models import fields
from rest_framework import serializers
from.models import Employee
class EmpSerializer(serializers.Serializer):
    eno=serializers.IntegerField()
    ename=serializers.CharField()
    esal=serializers.FloatField()
    eaddr=serializers.CharField()

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)
        # return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.eno=validated_data.get('eno',instance.eno)
        instance.ename=validated_data.get('eno',instance.ename)
        instance.esal=validated_data.get('eno',instance.esal)
        instance.eaddr=validated_data.get('eno',instance.eaddr)
        instance.save()
        return instance
        # return super().update(instance, validated_data)

class EmpModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"
    
    



