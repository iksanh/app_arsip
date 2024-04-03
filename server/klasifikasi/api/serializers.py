from rest_framework import serializers
from klasifikasi.models import KlasifikasiModel

class KlasifikasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = KlasifikasiModel
        fields = '__all__'


