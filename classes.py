#name, age, and class with default value "student".

class Students:
    #student = "yes"
    def __init__(self, gender="male", name="hkojo", age="kkk;m", _class="ljkkk"):
        self.gender = gender
        self.name = name  
        self.age = age
        self._class = _class
        

    def scores(self, one, two, three):

        avg = (one + two + three) / 3

        return f"{avg}"

newStd = Students("male", "james", 34, "history")



print(newStd.__dict__)
print(newStd.scores(10, 20, 30))

