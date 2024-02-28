from rest_framework import serializers
from .models import Ambassador, Inquiry, Report

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

# Report Start
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"
    def validate(self, data):
        comment = data.get('comment')
        user = data.get('user')
        if Report.objects.filter(comment=comment).exists() and Report.objects.filter(user=user).exists():
            raise serializers.ValidationError('すでに通報しています。')
        return data
# Report End