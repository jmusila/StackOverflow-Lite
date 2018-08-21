import sys
from flask import Flask, jsonify, make_response, request
sys.path.append('/home/jonathan/Desktop/StackApp/app/modules')
from datetime import datetime
from question import Question
from answer import Answer

question = Question('title', 'body')
answer = Answer('answer_title', 'answer_body')

   

app = Flask(__name__)
   

@app.route("/api/v1/questions", methods=["GET"])
def get_all_questions():
    return jsonify({"Questions": question.questions}), 200

@app.route("/api/v1/question", methods=["POST"])
def post_question():
    request_data = request.get_json()
    question_id = str(len(question.questions) + 1)
    title = request_data["POST"]
    body = request_data["body"]
    date_posted = datetime.now()
    if title == query["title"]:
        return jsonify({"message": "Question already existing", "Question": query}), 409
    for query in question.questions:
        if title == query["title"]:
            return jsonify({"message": "Question already asked", "Question": query}), 409
            question.post_question( question_id, title, body, date_posted)
            return jsonify({'Message': 'Question posted','Question': question.questions[-1]}), 201

@app.route('/app/v1/questions/<int:question_id>', methods=['GET'])
def get_question(question_id):
    question = [question for question in questions if question['id'] == question_id]
    if len(question) == 0:
        abort(404)
    return jsonify({'question': question[0]})

@app.route("/api/v1/question/<id>", methods=["GET"])
def get_a_question_by_id(id):
    for quest in question.questions:
        if id == quest["question_id"]:
            return jsonify({"message": "Question found", "Question": quest}), 200
        return jsonify({"message": "Question not found"}), 404

@app.route("/api/v1/questions/<questionId>/answers", methods=["POST"])
def add_answer(questionId):
    request_data = request.get_json()
    answer_id = str(len(answer.answers) + 1)
    answer_title = request_data["answer_title"]
    answer_body = request_data["answer_body"]
    date_posted = datetime.now()
    for query in question.questions:
        if int(questionId) == int(query["question_id"]):
            answer.post_answer(answer_id, questionId,answer_title, answer_body, date_posted)
            return jsonify({"Message": "Answer added successfully","Answer": answer.answers[-1]}), 200
            return jsonify({"Message": "Question with that id not found"}), 404

@app.route("/api/v1/questions/<questionId>/answers", methods=["GET"])
def get_all_answers(questionId):
    return jsonify({"Answers": answer.answers}), 200

if __name__ == '__main__':
    app.run(debug=True)