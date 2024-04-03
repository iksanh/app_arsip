from rest_framework import serializers
from unit_kerja.models import UnitKerjaModel, SubUnitKerjaModel


class UnitKerjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitKerjaModel
        fields = '__all__'

class SubUnitKerjaSerializerList(serializers.ModelSerializer):
    unit_kerja = UnitKerjaSerializer()
    class Meta:
        model = SubUnitKerjaModel
        fields = ['name', 'unit_kerja']

class SubUnitKerjaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SubUnitKerjaModel
        fields = ['name', 'unit_kerja']


