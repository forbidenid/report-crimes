from rest_framework import serializers
from . models import Complaint


class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ('created_by', 'seen_by', 'title', 'location', 'description', 'created_at')


