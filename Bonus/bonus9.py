import json

with open("../files/question.json", "r") as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question['question_text'])
    for index,option in enumerate(question['options']):
        print(index +1, ") ", option )
    user_choice = int(input("Enter your option: "))
    question['user_choice'] = user_choice

score = 0
for index, question in enumerate(data):
    result = "Wrong Answer"
    if question['user_choice'] == question['correct_answer']:
        score = score + 1
        result = "Correct Answer"
    message = f"{index + 1}) {result}: your answer: {question['options'][question['user_choice'] - 1]}, and the answer is {question['options'][question['correct_answer']-1]}"
    print(message)

print(f"your score is: {score}/{len(data)}")