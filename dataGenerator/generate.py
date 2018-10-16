# generate.py
# -----------

import sys
import csv
import random
import time
from math import *

from student import Student
from quiz import Quiz

random.seed(time.time())

def initSectionInfo(input_file):
  sectionList = []
  sectionDict = {}
  with open(input_file, newline = '', encoding = 'utf-8') as csvfile:
    rows = csv.reader(csvfile)
    cnt = 0
    for row in rows:
      sectionList.append(row[0])
      sectionDict[row[0]] = cnt
      cnt += 1

  return sectionList, sectionDict

def initQuizInfo(input_file, sectionDict):
  quizList = [{} for _ in range(len(sectionDict))]
  with open(input_file, newline = '', encoding = 'utf-8') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
      idx = sectionDict[row[1]]
      quizList[idx][row[0]] = Quiz(quizId = row[0], sectionId = idx, difficulty = row[2])

  return quizList

def initStudentList(sectionNum, studentNum = 1):
  studentList = []
  for i in range(studentNum):
    studentList.append(Student(sectionNum = sectionNum))

  return studentList

def doOneQuiz(student, quiz, c = 0):
  sectionId = quiz.getSectionId()
  d = quiz.getDifficulty()
  s = student.getSkillValue(sectionId)
  p = c + (1-c) / (1+exp(-s+d))

  result = (random.random() <= p)

  student.updateSkillValue(sectionId = sectionId, rightAns = result)

  return result
    


################
##   main()   ##
################
if __name__ == '__main__':
  sectionList, sectionDict = initSectionInfo(input_file = sys.argv[1])
  quizList = initQuizInfo(input_file = sys.argv[2], sectionDict = sectionDict)
  studentList = initStudentList(sectionNum = len(sectionList))

  for i in range(len(studentList)):
    with open('./generatedData/quizHist'+str(i)+'.csv', 'w', encoding = 'utf-8') as csvfile:
      writer = csv.writer(csvfile)

      quiz = quizList[0][random.choice(list(quizList[0].keys()))]

      for _ in range(100):
        result = doOneQuiz(student = studentList[i], quiz = quiz)
        writer.writerow([quiz.getQuizId(), quiz.getSectionId(), quiz.getDifficulty(), result])

      


