import unittest
from modules.question import Qestion

class TetsQuestion(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.client = self.app.test_client()
        self.question = {
            'title': 'how to install sublime text in ubuntu',
            'body': 'I have tried many times'

        }
        self.answer ={
            'answer':'use this command...'
        }
        
    def tearDown(self):
        print('tearDown\n')
        
class TestAnswer(unittest.TestCase):
    '''tests question related actions'''
    def ask_question(self):
        ''' help post a question for a testcase that needs it'''
        res = self.client.post(
            'api/v2/questions',
            data=json.dumps(self.question),
            content_type='application/json'
        )
        return res

    def test_answer_question(self):
        '''test if asking question is possible'''
        quiz = self.ask_question()
        answer = self.client.post(
            'api/v2/questions/1/answers',
            data = json.dumps(self.answer),
            content_type='application/json'
        )
        self.assertEqual(answer.status_code, 201)

    def test_answer_question_with_empty_body(self):
        quiz = self.ask_question()
        answer = self.client.post(
            'api/v2/questions/1/answers',
            data=json.dumps({'body':''}),
            content_type='application/json'
        )

    def test_answer_question_with_empty_body(self):
        quiz = self.ask_question()
        answer = self.client.post(
            'api/v2/questions/1/answers',
            data=json.dumps({'body':''}),
            content_type='application/json'
        )

    
if __name__==('__main__'):
    unittest.main()