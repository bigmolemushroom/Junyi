# sections.py
# -----------

import csv

class Sections():
  def __init__(self, input_file):
    self.sectionList = []
    self.readSectionList(input_file)

  def readSectionList(self, input_file):
    with open(input_file, newline = '') as csvfile:
      rows = csv.reader(csvfile)

      for row in rows:
        self.sectionList.append(row[0])

  def getSectionList(self):
    return self.sectionList

  def getSectionListSize(self):
    return len(self.sectionList)