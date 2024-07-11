import sys

class Question:
  def __init__(self,text,options,index_answer):
    self.text = text
    self.options = options
    self.index_answer = index_answer

class Quiz:
  def __init__(self,questions):
    self.questions = questions
    self.current_question = 0
    self.score = 0

  def ask_question(self):
    while self.current_question < len(self.questions):
      question = self.questions[self.current_question]
      print(question.text)
      for i, option in enumerate(question.options):
        print(f"{i+1}. {option}")
      user_input = input("Enter your answer:, 'n' for next question, 'q' for quit: ")
      if user_input.lower() == 'q':
        self.quit_quiz()
        break
      elif user_input.lower() == 'n':
        self.current_question += 1
        continue
      elif user_input.isdigit() and 1 <= int(user_input) <= 4:
        answer = int(user_input) - 1

        if answer == question.index_answer:
          print("Correct!")
          self.score += 1
        else:
          print("Incorrect!")

        self.current_question += 1

      else:
        print("Invalid input. Please enter a valid option.")
    self.show_result()
  def quit_quiz(self):
    print("Quit Quiz")
    self.show_result()
    sys.exit()

  def show_result(self):
    print(f"Quiz completed! Your score is {self.score}/{len(self.questions)}")
  


def main():
  questions = [
    Question("What doe the print() function do in python?",["Display Output","Take input","Perform Calculations","Define Variables"],0),
    Question("Which of the following is correct extension of python file?",[".py",".python",".p",".pyt"],0),
    Question("Is Python Compiled or Interpreted Language?",["Compiled","Interpreted","Both","Neither"],1)
  ]
  quiz = Quiz(questions)
  quiz.ask_question()

if __name__ == "__main__":
  main()