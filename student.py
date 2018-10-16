# student.py
# ----------

import sections

class Student():
  def __init__(self, sectionNum, initSkillValues = None, initLearningRates = None):
    self.skillValues = initSkillValues if(initSkillValues != None) else [-10 for _ in range(sectionNum)]
    self.learningRates = initLearningRates if(initLearningRates != None) else [1 for _ in range(sectionNum)]

  def updateSkillValue(self, sectionId, rightAns = True):
    if(rightAns):
      self.skillValues[sectionId] += self.learningRates[sectionId]
    else:
      self.skillValues[sectionId] += 0.5 * self.learningRates[sectionId]

  def getSkillValue(self, sectionId):
    return self.skillValues[sectionId]

# testing
if __name__ == '__main__':
  alice = Student(sectionNum = 10)
  bob = Student(sectionNum = 10, initSkillValues = [100 for _ in range(10)])