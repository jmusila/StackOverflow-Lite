from datetime import datetime

class Answer():
    """class to implement answer fuctionality"""

    def __init__(self ,answer_title,answer_body):
        self.answer_title = answer_title
        self.answer_body = answer_body
        self.answer_date = datetime.now()
        self.answers = []

    def post_answer(self, answer_id, question_id, answer_title, answer_body, date_posted):
        new_answers = {
                  "answer_id":answer_id,
                  "question_id":question_id,
                  "answer_title":answer_title,
                  "answer_body":answer_body,
                  "date_posted":date_posted
                  
                  # "posted_by":username
                  }

        self.answers.append(new_answers)
        return (self.answers)
				
		