from rest_framework import serializers
from dokumen.models import DokumenModel as dokumen

class DokumenSerializer(serializers.ModelSerializer):
    class Meta:
        model = dokumen
        fields = '__all__'
