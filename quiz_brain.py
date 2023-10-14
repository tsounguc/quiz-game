class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
    #TODO: asking the question
    #TODO: checking if the answer was correct
    #TODO: checking if we're at the end of the quiz

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
