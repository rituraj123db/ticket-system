from rest_framework import serializers

from .models import TicketRaise, UserRegistration


class TickerListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    status = serializers.CharField(max_length=255)
    priority = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField()

    class Meta:
        model = TicketRaise
        field = ["id", "title", "description", "priority", "status", "created_at"]


class TickerCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=True)
    description = serializers.CharField(max_length=255, required=True)

    class Meta:
        model = TicketRaise
        fields = ["title", "description"]


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, required=True)
    role = serializers.CharField(max_length=255, required=True)

    class Meta:
        model = UserRegistration
        fields = ["username", "role"]
