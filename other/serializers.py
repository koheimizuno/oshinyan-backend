from rest_framework import serializers
from .models import Ambassador, Inquiry

class AmbassadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambassador
        fields = "__all__"
    def validate(self, data):
        email = data.get('email')
        ambassador_name = data.get('ambassador_name')
        if Ambassador.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'message': 'Email Address already exists'})
        if Ambassador.objects.filter(ambassador_name=ambassador_name).exists():
            raise serializers.ValidationError(
                {'message': 'Ambassador already exists'})
        return data
    
class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = "__all__"