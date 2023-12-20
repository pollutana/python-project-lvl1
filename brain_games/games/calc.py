import operator
import random

RULE = "What is the result of the expression?"

OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    # "/": lambda x, y: x / y if y != 0 else division_error(),
}


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
    correct_answer = str(_calculate_answer(a, b, operator))
    return question_text, correct_answer
