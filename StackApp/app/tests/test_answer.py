import unittest
import sys
sys.path.append('/home/jonathan/Desktop/StackApp/app/tests')
sys.path.append('/home/jonathan/Desktop/StackApp/app')
import os
import json
from app import create_app
from question import Question
from app import answer,question,user


class TestAnswerFunctinality(unittest.TestCase):
    """This class represents the Answer test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.question = {"title": "No module found error",
                         "content": "What is the correct way to fix this ImportError error?"
                     }
        self.answer = {"answer_body":"wertghdfggdggdg"
                     }
    def tearDown(self):
      del user.users[:]
      del question.questions[:]
      del answer.answers[:]


    def test_user_can_post_answer(self):
        """
        Tests a user can post a question.
        """
        response = self.client.post("/api/v1/register",data=json.dumps(dict(first_name="john",
                                                        last_name="kiptoo",
                                                         username="jkiptoo",
                                                         email="jkip@gmal.com",
                                                         password="jkip")),
                                    content_type="application/json")

        response = self.client.post("/api/v1/login",data=json.dumps(dict(
                                        username_or_email="jkip",
                                        password="jkip")),
                                    content_type="application/json")

        response = self.client.post("/api/v1/question",data=json.dumps(self.question),
                                    content_type="application/json")
        response = self.client.post("/api/v1/questions/1/answers",
                                    data=json.dumps(self.answer),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Answer added successfully", response_msg["Message"])

    def test_post_answer_empty_body(self):
        """
        Tests user cannnot answer a question without body 
        """
        response = self.client.post("/api/v1/questions/1/answers",data=json.dumps(dict(answer_body=" ")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Answer body is required",
                      response_msg["Message"])

  
    def test_user_can_fetch_all_answers(self):
        """
        Tests user can get all answers for a partiular question.
        """
        response = self.client.get("/api/v1/questions/1/answers", data=json.dumps(dict()),
                                content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))

    

    def test_user_must_login_to_answer_question(self):
        response = self.client.post("/api/v1/register",data=json.dumps(dict(first_name="john",
                                                         last_name="kiptoo",
                                                         username="jkip",
                                                         email="jkip@gmal.com",
                                                         password="jkip")),
                                    content_type="application/json")

        response = self.client.post("/api/v1/question",data=json.dumps(dict(title="gfgf ghfdvhf",
                                    content = "gdfdg dgvgr")),
                                    content_type="application/json")
        response = self.client.post("/api/v1/questions/1/answers",data=json.dumps(self.answer),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 400)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertEqual("Login to post answer", response_msg["message"])

    def test_user_must_be_registered_to_answer_question(self):
        
        response = self.client.post("/api/v1/questions/1/answers",data=json.dumps(self.answer),
                                    content_type="application/json")
        self.assertEqual(response.status_code, 400)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("User does not exist", response_msg["message"])

