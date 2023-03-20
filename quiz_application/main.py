from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for question in question_data:
    question_text=question["question"]
    question_answer=question["correct_answer"]
    #print(question_text)
    #print(question_answer)
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
else:
    print("You completed the quiz successfully")
    print(f"Your final score is: {quiz.score}/{quiz.question_number}")



#you completed the quiz
#your final score was:10/12
