import unittest
import json
from user import Credentials

class Test_Register_And_Login(unittest.TestCase):
    

    def test_empty_username(self):

        result = Credentials.email('') 

        expected =json.dumps("Please enter correct email"),201

        self.assertEqual(expected, result)
  
    def test_empty_password(self):

        result = Credentials.password("'', '  ', '''") 

        expected =json.dumps("Please enter correct email"),201

        self.assertEqual(expected, result)

    if __name__ ==('__main__'):
         unittest.main()