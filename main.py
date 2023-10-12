from flask import request, jsonify
from app_main.functions import question_gen_and_save, get_question_from_db
from app_main import create_app, db

app = create_app()


@app.route('/api/generate_questions/', methods=['POST', 'GET'])
def generate_question_answer():
    try:
        count = request.get_json()['questions_num']
        question_gen_and_save(count)
        question_resp = get_question_from_db()
        return jsonify({'question_resp': question_resp})
    except Exception as e:
        print(e)


with app.app_context():
    db.create_all()
    app.run('0.0.0.0', debug=True)
