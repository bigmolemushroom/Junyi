# quiz.py
# -------

import csv

class Quiz():
  def __init__(self, quizId, sectionId, difficulty):
    self.quizId = quizId
    self.sectionId = sectionId
    self.difficulty = {'easy': 1, 'normal': 2, 'hard': 3}[difficulty]

  def getQuizId(self):
    return self.quizId

  def getSectionId(self):
    return self.sectionId

  def getDifficulty(self):
    return self.difficulty

  def print(self):
    print('quizId:', self.quizId, '|| sectionId:', self.sectionId, '|| difficulty:', self.difficulty)


class Quizzes():
  def __init__(self, input_file):
    self.quizDict = {}
    self.readQuizDict(input_file)

  def readQuizDict(self, input_file):
    with open(input_file, newline = '') as csvfile:
      rows = csv.reader(csvfile)

      for row in rows:
        self.quizDict[row[0]] = Quiz(row[0], row[1], row[2])

  def getQuizDict(self):
    return quizDict

  def getQuiz(self, quizId):
    return quizId

  def print(self):
    for quizId, quiz in self.quizDict.items():
      quiz.print()

# testing

if __name__ == '__main__':
  quizzes = Quizzes('myData')
  quizzes.print()



