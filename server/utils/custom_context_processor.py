from pegawai.models import PegawaiModel


def get_unit_kerja(request):
    unit_kerja =  None

    if request.user.is_authenticated:
        pegawai = PegawaiModel.objects.filter(user_profile = request.user).first()

        if pegawai:
            unit_kerja = pegawai.unit_kerja
    
    return {'unit_kerja': unit_kerja}