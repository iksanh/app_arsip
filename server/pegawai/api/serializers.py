from rest_framework import serializers
from pegawai.models import PegawaiStatusModel, PegawaiModel
from unit_kerja.api.serializers import UnitKerjaSerializer, SubUnitKerjaSerializer


class PegawaiStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PegawaiStatusModel
        fields = '__all__'

class PegawaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = PegawaiModel
        fields = '__all__'

class PegawaiSerializerList(serializers.ModelSerializer):
    status = PegawaiStatusSerializer()
    unit_kerja = UnitKerjaSerializer()
    sub_unit_kerja = SubUnitKerjaSerializer()

    class Meta:
        model = PegawaiModel
        fields = ['id', 'nama', 'identitas', 'status', 'created_at', 'unit_kerja','sub_unit_kerja']