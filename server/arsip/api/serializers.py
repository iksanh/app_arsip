
from rest_framework import serializers
from arsip.models import ArsipModel
from unit_kerja.api.serializers import UnitKerjaSerializer
from klasifikasi.api.serializers import KlasifikasiSerializer
from media.api.serializers import MediaSerializer
from lokasi.api.serializers import LokasiSerializer
from lokasi.api.serializers import TempatSerializer
from user.api.serializers import UserSerializer
from dokumen.api.serializers import DokumenSerializer



class ArsipSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArsipModel
        fields = '__all__'


class ArsipSerializerList(serializers.ModelSerializer):
    pencipta = UnitKerjaSerializer()
    pengelola = UnitKerjaSerializer()
    kode_klasifikasi= KlasifikasiSerializer()
    media = MediaSerializer()
    jenis_dokumen =  DokumenSerializer()
    # lokasi = LokasiSerializer()
    # tempat = TempatSerializer()
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



class FilteredArsipSerializer(ArsipSerializerList):
    def to_representation(self, instance):
        # Call the parent class' to_representation method
        data = super().to_representation(instance)

        # Retrieve the received parameters from the context
        request = self.context.get('request')
        dokumen = request.data.get('dokumen')
        keterangan = request.data.get('keterangan')
        periode = request.data.get('periode')

        # Filter the data based on the received parameters
        filtered_data = []

        if dokumen and dokumen != 'Pilih Dokumen':
            filtered_data = [item for item in data if item['jenis_dokumen']['id'] == dokumen]

        if keterangan and keterangan != 'Pilih Keterangan':
            filtered_data = [item for item in filtered_data if item['keterangan'] == keterangan]

        # Add additional filters for other parameters as needed

        return filtered_data