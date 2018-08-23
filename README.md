[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/jonathanmusila/StackOverflow-Lite/blob/gh-pages/LICENSE)

# StackOverflow-Lite
StackOverflow-Lite is a platform where people can ask questions and answer questions



## Endpoints

| Endpoint       | Description          |   HTTP-verb  |
| ------------- |:-------------:| -----:| 
| /api/v1/register | Register new user | POST |
| /api/v1/login  | Login the user using this endpoint      | POST   |
| /api/v1/logout | Logout the user from the system      | POST   |
| /api/v1/users | Get all users |  GET |
| /api/v1/question | Post a question | POST|
| /api/v1/question/id | Get question by id | GET |
| /api/v1/questions | Get all questions | GET |
| /api/v1/answer/questionId | Post an answer | POST|
| /api/v1//answers/questionId | Get all answers for a question | GET |

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
A few requirements to install, run and test this project.

cd path/to/directory-your-directory
- git clone https://github.com/jonathanmusila/StackOverflow-Lite.git
 -Install virtual environment 
- commands:
    
    - $ virtualenv venv 
    - $ source venv/bin/activate
    - $ pip install -r requirements.txt
    - $ pip install pytest
    
- To run tests, do:

    - $ pytests

- Then run the app by executing:
    - $ python run.py
    
- Install postman to test the various endpoints

## Testing
Manually open the index.html file in your preferred browser. Navigate through the pages with the links provided.




## Built With
* HTML
* CSS
* JavaScript
* python

## Authors
Jonathan Musila
