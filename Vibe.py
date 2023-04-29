from datetime import date

class Vibe:
    def __init__(self):
        self.currentdate = date.strftime(date.today(), "%d/%m/%y")
        self.questions = {
            "Mood": {
                "Question": "How's your mood 1-10? "
            },
            "Energy": {
                "Question": "How's your energy 1-10? "
            }
        }
        self.history = [{"Date" : "28/04/23", "Mood" : 0, "Energy" : 0}]

    def vibecheck(self):
        if self.checkdone() == False:
            answer = {"Date" : self.currentdate}
            print("Vibe check")
            daylist = list(self.questions.keys())
            for item in daylist:
                checked = False
                while checked == False:
                    a = input(self.questions[item]["Question"])
                    try:
                        int(a)
                    except:
                        print("that aint a number homie")
                    else:
                        checked = True
                        answer[item] = int(a)
                        print(answer)
            self.history.append(answer)
        else:
            self.showanswers()
    
    def showanswers(self):
        if self.checkdone() == True:
            print("Today's mood was " + str(self.history[-1]["Mood"]) + ", energy was " + str(self.history[-1]["Energy"]))
        else:
            print("You ain't done your check in homie")
    
    def checkdone(self):
        if self.history[-1]["Date"] == self.currentdate:
            return True
        else:
            return False

