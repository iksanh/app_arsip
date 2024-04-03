from rest_framework import serializers
from media.models import MediaModel as media

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = media
        fields = '__all__'
