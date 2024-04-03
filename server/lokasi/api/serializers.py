from rest_framework import serializers
from lokasi.models import LokasiModel, TempatModel


class LokasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = LokasiModel
        fields = '__all__'


class TempatSerializer(serializers.ModelSerializer):
    # lokasi = LokasiSerializer()
    
    
    class Meta:
        model = TempatModel
        fields = ['id', 'nama', 'lokasi']

class TempatSerializerList(serializers.ModelSerializer):
    lokasi = LokasiSerializer()
        
    class Meta:
        model = TempatModel
        fields = ['id', 'nama', 'lokasi']
  