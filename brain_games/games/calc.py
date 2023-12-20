import operator
import random

RULE = "What is the result of the expression?"

OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    # "/": lambda x, y: x / y if y != 0 else division_error(),
}


def check_answer(user_answer: str, correct_answer: int) -> bool:
    try:
        user_answer_int = int(user_answer)
        return user_answer_int == correct_answer

    except ValueError:
        return False


def _calculate_answer(a: int, b: int, operator: str) -> int:
    operation = OPERATORS.get(operator)
    if operation:
        return operation(a, b)
    else:
        raise ValueError("Invalid operator")


def generate_question_and_answer() -> tuple:
    a, b = random.randrange(0, 50), random.randrange(1, 11)
    operator = random.choice(list(OPERATORS.keys()))
    question_text = f"Question: {a} {operator} {b}"
    correct_answer = _calculate_answer(a, b, operator)
    return question_text, correct_answer
