# class Student:
#     amount_of_student = 0
#
#     def __init__(self, height):
#         self.height = height
#         Student.amount_of_student +=1
#
# vlad = Student(160)
# artem = Student(180)
#
# print(Student.amount_of_student)
# print(Student.amount_of_student)

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 0
        self.alive = True

    def to_study(self):
        print('Time to study')
        self.gladness -=3
        self.progress+= 0.12
        self.money += 7

    def to_chill(self):
        print('Rest time')
        self.gladness += 5
        self.progress -= 0.1
        self.money -=10
    def computer_games(self):
        print('Play and chill!')
        self.gladness += 10
        self.money -= 1

    def to_sleep(self):
        print('Time to sleep')
        self.gladness += 3

    def is_alive(self):
        if self.progress < -0.5:
            print('Cast out...')
            self.alive = False

        elif self.gladness <= 0:
            print('Depression...')
            self.alive = False

        elif self.progress  > 5 :
            print('Passed exams')
            self.alive = False
            self.money += 50

    def day_info(self):
        print(f"Gladness - {self.gladness}")
        print(f"Progress - {self.progress}")


    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        live_cube = random.randint(1,3)
        if live_cube == 1:
         self.to_study()
        elif live_cube == 2:
         self.to_chill()
         self.money -= 5
        else:
            self.to_sleep()
            self.day_info()
            self.is_alive()

vlad = Student("Vlad")

for day in range(1.366):
    if vlad.alive == False:
        break
    vlad.live(day)

