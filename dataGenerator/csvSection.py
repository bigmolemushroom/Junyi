# csvSection.py
# -------------

# -*- coding: utf8 -*-

import sys
import io
import csv

from pymongo import MongoClient
from bson.objectid import ObjectId

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding = 'utf-8')

conn = MongoClient()
db = conn.Junyi
collection = db.ProblemLog
cursor = collection.find({})
allData = [d for d in cursor]

sectionList = [[] for _ in range(7)]
sectionSet = set()

quizList = [{} for _ in range(7)]
quizSet = set()

for data in allData:
  sec = data['section_key']
  quizId = data['quiz_id']
  gra = 0
  if(data['curriculum_guideline_99']):
    gra = int(data['curriculum_guideline_99'][0])
  if(gra <= 5):
    continue
  if(not sec in sectionSet):
    sectionList[gra].append(sec)
    sectionSet.add(sec)
    quizList[gra][sec] = []
  if(not quizId in quizSet):
    quizList[gra][sec].append(quizId)
    quizSet.add(quizId)
  quizList[gra][sec].append([data['quiz_id'], sec])

with open('sectionInfo_56.csv', 'w', newline = '', encoding = 'utf-8') as csvfile:
  writer = csv.writer(csvfile)

  for gra in [5, 6]:
    for sec in sectionList[gra]:
      writer.writerow([sec])

with open('quizInfo_56.csv', 'w', newline = '', encoding = 'utf-8') as csvfile:
  writer = csv.writer(csvfile)

  for gra in [5, 6]:
    for sec, quizL in quizList[gra].items():
      for quizId in quizL:
        writer.writerow([quizId, sec])

