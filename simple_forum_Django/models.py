from django.db import models

QUESTIONS = [
    {
        'id': question_id,
        'title': f'Вопрос #{question_id}',
        'text': f'Текст вопроса #{question_id}',
        'answers_number': question_id * question_id,
        'tags': ['Тег' for i in range(question_id)]
    } for question_id in range(30)
]

HOT_QUESTIONS = [
    {
        'id': question_id,
        'title': f'Вопрос #{question_id}',
        'text': f'Текст вопроса #{question_id}',
        'answers_number': question_id * question_id,
        'tags': ['Тег' for i in range(question_id)]
    } for question_id in range(5)]



