class Hour:
    def __init__(self, subject, teacher):
        self.subject = subject
        self.teacher = teacher

    def info(self):
        print(f" {self.subject} with {self.teacher}")

    def hour(self):
        if self.subject == 'spanish':
            print('4th hour')
        elif self.subject == 'math':
            print('8th hour')
        else:
            print("dang")

spanish = Hour('spanish', 'murray')
math = Hour('math', 'bowler')

spanish.info()
spanish.hour()

math.hour()
