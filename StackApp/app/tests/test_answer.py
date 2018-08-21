import unittest
import sys
sys.path.append('/home/jonathan/Desktop/StackApp/app/modules')
sys.path.append('/home/jonathan/Desktop/StackApp/app')
import os
import json
from question import Question
from app import answer,question


class TestAnswerPosted(unittest.TestCase):
    """Answer test case"""

    def setUp(self):
        """Test variables"""
        self.question = {"title": "Python",
                         "body": "How to install sublime-text in ubuntu"
                        }
        self.answer = {"answer_body":"this is the answer"
                      }
    def tearDown(self):
      del question.questions[:]
      del answer.answers[:]

    def test_post_answer_no_title(self):
        """
        Tests user cannnot answer a question without title 
        """
        response = self.client.post("/api/v1/questions/1/answers",
                                 data=json.dumps(dict(answer_body=" ")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Answer body is required",
                      response_msg["Message"])

    def test_post_answer_no_body(self):
        """
        Tests user cannnot answer a question without body 
        """
        response = self.client.post("/api/v1/questions/1/answers",
                                 data=json.dumps(dict(answer_body=" ")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Answer body is required",
                      response_msg["Message"])

  
    def test_user_can_fetch_all_answers(self):
        """
        Tests user can get all answers for a partiular question.
        """
        response = self.client.get("/api/v1/questions/1/answers",
                                data=json.dumps(dict()),
                                content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))
   
   