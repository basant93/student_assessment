from .models import UserProfile

class StudentProfileResponse(object):
    success = None
    data = None
    error_code = None
    status_code = None


class StudentProfileInfo(object):
    first_name = None
    last_name = None
    email = None
    user_gender = None
    user_contact_no = None
    user_profile_image_url = None
    user_pincode = None

    def __init__(self, user_obj):
        self.first_name = user_obj.first_name
        self.last_name = user_obj.last_name
        self.email = user_obj.email
        
        try:
            user_profile_obj = UserProfile.objects.get(auth_user = user_obj)
        except:
            user_profile_obj = None
        if user_profile_obj is not None:
            self.user_gender = user_profile_obj.user_gender
            self.user_contact_no = user_profile_obj.user_contact_no
            self.user_profile_image_url = user_profile_obj.user_profile_image_url
            self.user_pincode = user_profile_obj.user_pincode



class StudentProfileDataResponse(object):
    id = None
    base_info = None

    def __init__(self, auth_user_obj):
        self.id = auth_user_obj.id
        self.base_info = StudentProfileInfo(auth_user_obj)
