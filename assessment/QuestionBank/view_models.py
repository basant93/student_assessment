

class QuestionBankResponse(object):
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

        
    




    
    


