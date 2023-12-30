from django.db import IntegrityError
from rest_framework import serializers
from .models import Assessment


class AssessmentSerializer(serializers.ModelSerializer):
    """
    Assessment serializer
    """

    class Meta:
        """
        Metaclass for the serializer
        """
        model = Assessment
        fields = "__all__"

    def create(self, validated_data):
        """
        Handles the unique constraint on user and video
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                "detail": "possible duplicate assessment"
            })
