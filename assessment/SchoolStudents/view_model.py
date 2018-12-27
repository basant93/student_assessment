from .models import Student

class StudentProfileResponse(object):
    success = None
    data = None
    error_code = None
    status_code = None


class StudentProfileInfo(object):
    first_name = None
    last_name = None
    email = None
    student_gender = None
    student_contact_no = None
    student_profile_image_url = None
    student_pincode = None

    def __init__(self, user_obj):
        self.first_name = user_obj.first_name
        self.last_name = user_obj.last_name
        self.email = user_obj.email
        
        try:
            student_profile_obj = Student.objects.get(auth_user = user_obj)
        except:
            student_profile_obj = None
        if student_profile_obj is not None:
            self.student_gender = student_profile_obj.student_gender
            self.student_contact_no = student_profile_obj.student_contact_no
            self.student_profile_image_url = student_profile_obj.student_profile_image_url
            self.student_pincode = student_profile_obj.student_pincode



class StudentProfileDataResponse(object):
    id = None
    base_info = None

    def __init__(self, auth_user_obj):
        self.id = auth_user_obj.id
        self.base_info = StudentProfileInfo(auth_user_obj)
