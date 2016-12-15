from rest_framework import serializers
from cf.models import SafeBox, Key


class SafeBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = SafeBox
        fields = ('id', 'name')


class KeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Key
        fields = ('id', 'description', 'document', 'uploaded_at', 'safe_box')
