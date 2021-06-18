# so the return value testng is testing whether a functin returns ssomething or it doesn't
#
def testEqual(a, b):
    if a == b:
        print("Pass")
    else:
        print(f"Test Failed: expected {b} but got {a}")


class Student:
    def __init__(self, name, years_um=1):
        self.name = name
        self.years_UM = 1
        self.knowledge = 0

    def study(self):
        # self.knowledge+=1
        return None

    def getKnowledge(self):
        return None

    def year_at_umich(self):
        return self.years_UM


s = Student("Gary")
testEqual(s.name, "Gary")
testEqual(s.years_UM, 1)
testEqual(s.knowledge, 0)

s.study()
testEqual(s.study(), None)
testEqual(s.knowledge, 1)
testEqual(s.getKnowledge(), 1)

s2 = Student("Garrison", 3)
testEqual(s2.years_UM, 3)
testEqual(s2.year_at_umich(), 3)
