from flask import Flask, request, jsonify
import sys
sys.path.append('/home/jonathan/Desktop/StackApp/app/models')
sys.path.append('/home/jonathan/Desktop/StackApp/app/common')
from datetime import datetime
from config import app_config
from question import Question
from answer import Answer
from user import User
from validators import *
import psycopg2
import psycopg2.extras


user = User()
question = Question('title', 'content')
answer = Answer('answer_body', 'username')


def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

    def connectToDb():
        connectionString=(dbname=mydb, user=jonathan, password=jonathan, host=localhost, port=5432)
        print (connectionString)
        try:
            return psycopg2.connect(connectionString)
        except:
            print ("Cant connect to the database")

    @app.route("/api/v1/register", methods=["POST"])
    def register_new_user():
        request_data = request.get_json()
        user_id = str(len(user.users) + 1)

        user.create_user(user_id, request_data["names"],
                        request_data["username"], request_data["email"],
                        request_data["password"])

        return jsonify({'Message': 'User successfully created', 'User': user.users[-1]}), 201

    @app.route("/api/v1/login", methods=["POST"])
    def login_user():
        request_data = request.get_json()
        username_or_email = request_data["username_or_email"]
        password = request_data["password"]
        for person in user.users:
            if (person["username"] == username_or_email or
                    person["email"] == username_or_email) and person["password"] == password:
                if(person["login_status"] == False):
                    person["login_status"] = True
                    return jsonify({"message": "User logged in successfully", "User": person}), 200
                else:
                    return jsonify({"message": "User Already Logged in", "User": person}), 409
            return jsonify({"message": "Enter correct username or password"}), 404
        return jsonify({"message": "User does not exist"}), 404

    @app.route('/api/v1/logout', methods=['POST'])
    def logout_user():
        request_data = request.get_json()
        username_or_email = request_data['username_or_email']
        for person in user.users:
            if (person["username"] == username_or_email or
                    person["email"] == username_or_email) and person["login_status"] == True:
                person["login_status"] = False
                return jsonify({'Message': "User logged out"}), 200

        return jsonify({'Message': 'User is not logged in, please login.'}), 401

    @app.route("/api/v1/users", methods=["GET"])
    def get_all_users():
        conn = connectToDb()
        cur = conn.cursor()
        try:
            cur.execute("SELECT names, username, email from User")
        except:
            print("Error in getting users")
            results = cur.fetchall()
        return jsonify({"Users": user.users}), 200

    @app.route("/api/v1/question", methods=["POST"])
    def post_question():
        request_data = request.get_json()
        question_id = str(len(question.questions) + 1)
        title = request_data["title"]
        content = request_data["content"]
        date_posted = datetime.now()

        for quest in question.questions:
            if title == quest["title"]:
                return jsonify({"message": "Question already asked", "Question": quest}), 409
        for person in user.users:
            if person["login_status"] == True:
                username = person["username"]
                question.post_question(
                    question_id, title, content, date_posted, username)
                return jsonify({
                    'Message': 'Question posted',
                    'Question': question.questions[-1]}), 201
        return jsonify({"message": "Login to post a question"}), 400

    @app.route("/api/v1/questions", methods=["GET"])
    def get_all_questions():
        return jsonify({"Questions": question.questions}), 200

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
        answer_body = request_data["answer_body"]
        date_posted = datetime.now()

        for person in user.users:
            if person["login_status"] == True:
                for quest in question.questions:
                    if int(questionId) == int(quest["question_id"]):
                        username = person["username"]
                        answer.post_answer(answer_id, questionId,
                                           answer_body, date_posted, username)
                        return jsonify({"Message": "Answer added successfully",
                                        "Answer": answer.answers[-1]}), 200

                return jsonify({"Message": "Question with that id not found"}), 404
            return jsonify({"message": "Login to post answer"}), 400
        return jsonify({"message": "User does not exist"}), 400

    @app.route("/api/v1/questions/<questionId>/answers", methods=["GET"])
    def get_all_answers(questionId):
        conn = connectToDb()
        cur = conn.cursor()
        try:
            cur.execute("select answer_body, date_posted, question_id, posted_by from User")
        except:
            print("Error in getting answers")
            results = cur.fetchall()
        return jsonify({"Answers": answer.answers}), 200

    return app