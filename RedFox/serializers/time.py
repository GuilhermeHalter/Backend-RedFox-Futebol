from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import Image
from uploader.serializers import ImageSerializer

from RedFox.models import Time

class TimeSerializer (ModelSerializer):
    class Meta:
        model = Time
        fields = "__all__"
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)

class TimeDetailSerializer(ModelSerializer):
    capa = ImageSerializer(required=False)
    