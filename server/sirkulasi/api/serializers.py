from rest_framework import serializers
from server.sirkulasi.models import SirkulasiModel
from pegawai.api.serializers import PegawaiSerializer
from arsip.api.serializers import ArsipSerializer
from user.api.serializers import UserSerializer

class SirkulasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = SirkulasiModel
        fields = '__all__'

class SirklusiSerializerList(serializers.ModelSerializer):
    nomor_arsip = ArsipSerializer()
    peminjam = PegawaiSerializer()
    created_by = serializers.SerializerMethodField()
    updated_by = serializers.SerializerMethodField()

    def get_created_by(self, obj):
        return {
            'username': obj.created_by.username if obj.created_by else None,
            'email': obj.created_by.email if obj.created_by else None
        }
    def get_updated_by(self, obj):
        return {
            'username': obj.updated_by.username if obj.updated_by else None,
            'email': obj.updated_by.email if obj.updated_by else None
        }

    class Meta:
        model = SirkulasiModel
        fields = '__all__'


