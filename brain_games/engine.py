def greet_and_get_username() -> str:
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name


ROUNDS = 3


def launch(rules: str, game_logic) -> None:
    name = greet_and_get_username()
    print(rules)
    for round in range(ROUNDS):
        question, correct_answer = game_logic.generate_question_and_answer()
        question = "Question: " + question
        print(question)
        user_answer = input("Your answer: ")
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer :(.",
                f"Correct answer was '{correct_answer}'.",
                f"\nLet's try again, {name}!",
            )
            break
        if round == ROUNDS - 1:
            print(f"Congratulations, {name}!")
