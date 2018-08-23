[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/hyperium/hyper/master/LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)


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


## Authors
Jonathan Musila