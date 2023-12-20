import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime_number(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def generate_question_and_answer() -> tuple:
    number = random.randint(2, 100)
    correct_answer = "yes" if is_prime_number(number) else "no"
    return f"Question: {number}", correct_answer
