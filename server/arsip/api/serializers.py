
from rest_framework import serializers
from arsip.models import ArsipModel
from unit_kerja.api.serializers import UnitKerjaSerializer
from klasifikasi.api.serializers import KlasifikasiSerializer
from media.api.serializers import MediaSerializer
from lokasi.api.serializers import LokasiSerializer
from lokasi.api.serializers import TempatSerializer
from user.api.serializers import UserSerializer



class ArsipSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArsipModel
        fields = '__all__'


class ArsipSerializerList(serializers.ModelSerializer):
    pencipta = UnitKerjaSerializer()
    pengelola = UnitKerjaSerializer()
    kode_klasifikasi= KlasifikasiSerializer()
    media = MediaSerializer()
    lokasi = LokasiSerializer()
    tempat = TempatSerializer()
    #created_by = serializers.CharField(source='created_by.username', read_only=True)
    created_by = serializers.SerializerMethodField()
    updated_by = serializers.SerializerMethodField()



    class Meta:
        model = ArsipModel
        fields = '__all__'

    def get_created_by(self, obj):
        return {
            'username': obj.created_by.username if obj.updated_by else None,
            'email': obj.created_by.email if obj.created_by else None
        }

    def get_updated_by(self, obj):
        return {
            'username': obj.updated_by.username if obj.updated_by else None,
            'email': obj.updated_by.email if obj.updated_by else None
        }

