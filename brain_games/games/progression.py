import random

RULE = "What number is missing in the progression?"
_PROG_MIN = 5
_PROG_MAX = 10
_HIDE_SYMBOL = ".."


def _generate_progression() -> list:
    prog_len = random.randint(_PROG_MIN, _PROG_MAX + 1)
    step = random.randint(1, 11)
    start = random.randint(0, 100)
    stop = start + step * prog_len
    return list(range(start, stop, step))


def generate_question_and_answer() -> tuple:
    prog = _generate_progression()
    hidden_index = random.randint(0, len(prog) - 1)
    correct_answer = str(prog[hidden_index])
    prog[hidden_index] = _HIDE_SYMBOL
    question_text = " ".join(map(str, prog))
    return question_text, correct_answer
