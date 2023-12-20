import math
import random

RULE = "Find the greatest common divisor of given numbers."


def check_answer(user_answer: str, correct_answer: int) -> bool:
    try:
        user_answer_int = int(user_answer)
        return user_answer_int == correct_answer

    except ValueError:
        return False


def _calculate_answer(a: int, b: int) -> int:
    return math.gcd(a, b)


def generate_question_and_answer() -> tuple:
    a, b = random.randrange(0, 20), random.randrange(0, 20)
    question_text = f"Question: {a} {b}"
    correct_answer = _calculate_answer(a, b)
    return question_text, correct_answer
