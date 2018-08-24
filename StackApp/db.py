import psycopg2
import psycopg2.extras
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def connectDB():
    connection_string = 'dbname=mydb user=jonathan password=jonathan host=localhost'
    try:
        return psycopg2.connect(connection_string)
    except:
        print('Can\'t connect to database')

def create_db_tables():
    queries = [
        'DROP TABLE IF EXISTS "answer" CASCADE',
        'DROP TABLE IF EXISTS "question" CASCADE',
        'DROP TABLE IF EXISTS "user" CASCADE',
        """
        CREATE TABLE answer (
            answer_id SERIAL PRIMARY KEY NOT NULL, 
            answer_body VARCHAR(500) NOT NULL, 
            question_id INT NOT NULL, 
            date_posted TIMESTAMP NOT NULL, 
            posted_by VARCHAR(140) NOT NULL 
            );
        """,
        """
        CREATE TABLE question (
            question_id SERIAL PRIMARY KEY NOT NULL, 
            title VARCHAR(200) NOT NULL, 
            content VARCHAR(500) NOT NULL, 
             date_posted TIMESTAMP NOT NULL, 
            posted_by VARCHAR(140) NOT NULL
            );
        """,
        """
        CREATE TABLE users (
            user_id SERIAL PRIMARY KEY NOT NULL, 
            names VARCHAR(140) NOT NULL, 
            email VARCHAR(140) NOT NULL, 
            password VARCHAR(40) NOT NULL, 
            login_status VARCHAR(140) NOT NULL
            );
        """    
    ]
    run_query_commands(queries)

def run_query_commands(queries):
    connection = None
    try:
       connection = connectDB()
       cursor = connection.cursor()
       for query in queries:
            cursor.execute(query)
       cursor.close()
       connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()



if __name__ == '__main__':
    create_db_tables()