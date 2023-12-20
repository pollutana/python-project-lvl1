import math
import random

RULE = "Find the greatest common divisor of given numbers."


def generate_question_and_answer() -> tuple:
    a, b = random.randrange(0, 20), random.randrange(0, 20)
    question_text = f"{a} {b}"
    correct_answer = str(math.gcd(a, b))
    return question_text, correct_answer
