from .models import Question_Answer, Answer

class AssignmentMainResponse(object):
    success = None
    error = None
    data = None
    status = None



class QuestionBankDataResponse(object):
    
    ques_grades = None
    ques_sections = None
    total_marks = None
    total_time = None
    general_instructions = None
    ques_bank_title = None
    subject = None

    def __init__(self, quesBankObj):
        self.ques_grades = quesBankObj.ques_grades
        self.ques_sections = quesBankObj.ques_sections
        self.total_marks = quesBankObj.total_marks
        self.total_time = quesBankObj.total_time
        self.general_instructions = quesBankObj.general_instructions
        self.ques_bank_title = quesBankObj.ques_bank_title
        self.subject = quesBankObj.subject


class SectionDataResponse(object):

    section_name = None
    comprehension_description = None
    question_answer_list = None

    # def __init__(self, question_answer_sections):
    #     self.section_name = 

class QuestionInfoDataResponse(object):
    question_id = None
    question_type = None
    question_title = None
    question_marks = None
    question_answer_options = None
    
class AnswerMainDataResponse(object):
    
    answer_id = None
    option_one = None
    option_two = None
    answers_marks = None
    is_correct = None


class SectionQuesAnsDataResponse(object):
    section_questions_info = None

    def __init__(self,section_questions):

        self.section_questions_info = SectionQuesAnsDataResponse.process_section_info(section_questions)

    @staticmethod
    def process_section_info(section_questions):
        sec_ret_val = []
        for ques in section_questions:
            
            ques_ans_objs = list(Question_Answer.objects.filter(question = ques.id))

            related_answer_objs = list(map(lambda ans : ans.answer  , ques_ans_objs))
            answer_obj_list = []

            for ans in related_answer_objs:
                answer_obj = AnswerMainDataResponse()
                answer_obj.answer_id = ans.id
                answer_obj.option_one = ans.option_one
                answer_obj.option_two = ans.option_two
                answer_obj.answers_marks = ans.answers_marks
                answer_obj.is_correct = ans.is_correct

                answer_obj_list.append(answer_obj)

            question_details = QuestionInfoDataResponse()
            question_details.question_id = ques.id
            question_details.question_type = ques.question_type
            question_details.question_title = ques.question_title
            question_details.question_marks = ques.question_marks
            question_details.question_answer_options = answer_obj_list

            sec_ret_val.append(question_details)
        return sec_ret_val




class QuestionAnswerDataResponse(object):

    ques_bank_id = None
    ques_bank_title = None
    exam_start_time = None
    exam_end_time = None
    subject = None
    general_instruction = None
    section_info = None

    def __init__(self, ques_bank_obj):
        self.ques_bank_id = ques_bank_obj.id
        self.ques_bank_title = ques_bank_obj.ques_bank_title
        self.exam_start_time = ques_bank_obj.exam_start_time
        self.exam_end_time = ques_bank_obj.exam_end_time
        self.subject = ques_bank_obj.subject
        self.general_instruction = ques_bank_obj.general_instructions
        self.section_info = QuestionAnswerDataResponse.process_section_info(list(ques_bank_obj.questionssections_set.all()))
        #self.section_info =  SectionDataResponse(list(ques_bank_obj.questionssections_set.all()) )

    
    @staticmethod
    def process_section_info(section_infos):

        ret_val = []
        for section in section_infos:
            ques_section_info = SectionDataResponse()
            ques_section_info.section_name = section.section_name
            ques_section_info.comprehension_description = section.comprehension_desc
            ques_section_info.question_answer_list = SectionQuesAnsDataResponse(list(section.question_set.all()))

            ret_val.append(ques_section_info)
        
        return ret_val


    
class StudentResponseSaved(object):

    message = None

    def __init__(self, message):
        self.message = message


class StudentMarksResponse(object):
    question_bank_title = None
    user_name = None
    user_email = None
    marks_scored = None

    def __init__(self, student_response):
        self.question_bank_title = student_response.question_bank.ques_bank_title
        self.user_name = student_response.student.auth_user.username
        self.user_email = student_response.student.auth_user.email
        self.marks_scored = student_response.marks_scored


class AllStudentMarksResponse(object):
    question_bank_title = None
    user_name = None
    user_email = None
    marks_scored = None



class AllStudentMarksMainResponse(object):
    student_list  = None

    def __init__(self, student_response_list):

        self.student_list = AllStudentMarksMainResponse.process_student_result(student_response_list)

    @staticmethod
    def process_student_result(student_response_list):

        ret_val = []

        for student_response in student_response_list:
            student_result = AllStudentMarksResponse()
            student_result.question_bank_title = student_response.question_bank.ques_bank_title
            student_result.user_name = student_response.student.auth_user.username
            student_result.user_email = student_response.student.auth_user.email
            student_result.marks_scored = student_response.marks_scored

            ret_val.append(student_result)
        
        return ret_val
