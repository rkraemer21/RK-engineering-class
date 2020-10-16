class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def singsong(self):
        for line in self.lyrics:
            print(line)

bday = Song(["happy",
            "birthday",
            "to you"])

bday.singsong() 
