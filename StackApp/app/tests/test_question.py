import unittest
import sys
sys.path.append('/home/jonathan/Desktop/StackApp/app/modules')
sys.path.append('/home/jonathan/Desktop/StackApp/app')
import os
import json
from question import Question
from app.app import answer,question


class TestQuestionFunctinality(unittest.TestCase):
    """This class represents the question test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.question = {"title": "No module found error",
                         "content": "What is the correct way to fix this ImportError error?"
                     }
    def tearDown(self):
      del user.users[:]
      del question.questions[:]
      del answer.answers[:]
    
    def test_post_question_empty_content(self):
        """
        Tests user cannnot ask a question without body content
        """
        response = self.client.post("/api/v1/question",
                                 data=json.dumps(dict(title="how to delete git branch",
                                                      content="")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Content is required",
                      response_msg["Message"])

    def test_post_question_empty_title(self):
        """
        Tests user cannnot add a question without title
        """
        response = self.client.post("/api/v1/question",
                                 data=json.dumps(dict(title="",
                                                      content="I want to delete a branch both locally..")),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 401)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Title is required",
                      response_msg["Message"])

    def test_user_can_fetch_all_questions(self):
        """
        Tests user can get all questions he/she has asked.
        """
        response = self.client.get("/api/v1/questions",
                                data=json.dumps(dict()),
                                content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))

    def test_user_can_get_one_question_by_id(self):
        """
        Tests a user can get a question by id.
        """
        response = self.client.post("/api/v1/register",
                                    data=json.dumps(dict(first_name="joyce",
                                                         last_name="korir",
                                                         username="joykorry",
                                                         email="joy@gmail.com",
                                                         password="joy")),
                                    content_type="application/json")
        response = self.client.post("/api/v1/login",
                                    data=json.dumps(dict(
                                        username_or_email="joykorry",
                                        password="joy")),
                                    content_type="application/json")

        response = self.client.post("/api/v1/question",
                                 data=json.dumps(dict(
                                 title="test-title",
                                 content="test-content")),
                                 content_type="application/json")

        response = self.client.get("/api/v1/question/1",
                                 data=json.dumps(dict(question_id=1)),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 200)
        response_msg = json.loads(response.data.decode("UTF-8"))
        self.assertIn("Question found", response_msg["message"])

