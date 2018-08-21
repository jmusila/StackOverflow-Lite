from datetime import datetime

class Question(object):

    def __init__(self, title, body): 
        self.title = title
        self.body = body
        self.date_posted = datetime.now()
        self.questions = []
        
    def post_question(self, question_id, title, body, date_posted):
        new_question = {
            'question_id': question_id,
            'title': title,
            'body': body,
            'date_posted':date_posted}

        self.questions.append(new_question)
        return (self.questions)