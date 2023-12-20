import random


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def check_answer(user_answer: str, correct_answer: str) -> bool:
    return user_answer == correct_answer


def generate_question_and_answer() -> tuple:
    question = random.randrange(0, 100)
    question_text = f"Question {question}"
    correct_answer = "no" if question % 2 else "yes"
    return question_text, correct_answer
