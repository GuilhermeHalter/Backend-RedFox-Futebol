from rest_framework.serializers import ModelSerializer

from RedFox.models import Time

class TimeSerializer (ModelSerializer):
    class Meta:
        model = Time
        fields = "__all__"
    