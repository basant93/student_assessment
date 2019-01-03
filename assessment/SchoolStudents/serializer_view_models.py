from rest_framework import serializers

class StudentProfileBaseSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    user_gender = serializers.CharField()
    user_contact_no = serializers.CharField()
    user_profile_image_url = serializers.URLField()
    user_pincode = serializers.CharField()
    



class StudentProfileInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    base_info = StudentProfileBaseSerializer()


class StudentProfileMainSerializer(serializers.Serializer):
    
    success = serializers.BooleanField()
    error_code = serializers.IntegerField()
    status_code = serializers.CharField()
    data = StudentProfileInfoSerializer()