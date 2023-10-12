import requests
from app_main import db
from models import Questions
from datetime import datetime


def save_to_db(data):
    db.session.add(data)
    db.session.commit()


def question_gen_and_save(count):
    unique_questions = []
    while len(unique_questions) < count:
        url = f'https://jservice.io/api/random?count={count}'
        r = requests.get(url)
        for i in r.json():
            ID_question = i['id']
            Answer = i['answer']
            Question = i['question']
            Created_at = datetime.strptime(i['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
            existing_question = Questions.query.filter_by(ID_question=ID_question).first()
            if not existing_question:
                data = Questions(ID_question=ID_question, Answer=Answer, Question=Question, Created_at=Created_at)
                save_to_db(data)
                unique_questions.append(data)
                count -= len(unique_questions)
            else:
                print('already in db', i)


def get_question_from_db():
    questions = Questions.query.order_by(Questions.ID).all()
    if questions:
        max_id_question = max(question.ID for question in questions)
        print(max_id_question - 1)
        question = Questions.query.filter_by(ID=max_id_question - 1).first()
        if question:
            return question.Question
        else:
            return None
    return None
