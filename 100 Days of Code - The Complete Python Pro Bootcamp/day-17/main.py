from question_model import Question
from data import question_data, api_question_data
from quiz_brain import QuizBrain

question_bank = []
question_data_list = api_question_data

for i in range(0, len(question_data_list)):
    # variables for question_data list
    # question_text = question_data_list[i]["text"]
    # question_answer = question_data_list[i]["answer"]

    # variables for api_question_data list
    question_text = question_data_list[i]["question"]
    question_answer = question_data_list[i]["correct_answer"]

    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_questions()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")
