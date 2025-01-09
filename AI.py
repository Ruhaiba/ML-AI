import json
from difflib import get_close_matches
import datetime

def load_know_base(file_path: str): 
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

def save_know_base(file_path: str, data: dict):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list):
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.75)
    return matches[0] if matches else None

def get_answers_for_question(question: str, know_base: dict):
    for q in know_base["questions"]:
        if q["question"] == question:
            return q["answer"]
    return None

def chat_bot():
    know_base = load_know_base("know_base.json")

    while True:
        user_inp = input("You: ")
        if user_inp.lower() == "quit":
            break
        elif user_inp.lower() == "what's today's date?":
            print("Bot:", datetime.datetime.now().strftime("%Y-%m-%d"))
            continue

        best_match = find_best_match(user_inp, [q["question"] for q in know_base["questions"]])
        
        if best_match:
            answer = get_answers_for_question(best_match, know_base)
            print(f'Bot: {answer}')
        else:
            print("Bot: I haven't heard of this query before. Can you teach me?")
            new_ans = input("Type answer or write *skip* to skip: ")
            if new_ans.lower() == "skip":
                continue
            else:
                know_base["questions"].append({"question": user_inp, "answer": new_ans})
                save_know_base("know_base.json", know_base)
                print("Bot: Thank you for all your help!")

if __name__ == "__main__":
    chat_bot()

