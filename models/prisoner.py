class Prisoner:
    def __init__(self, name, prisoner_id, sentence_duration, crime):
        self.name = name
        self.prisoner_id = prisoner_id
        self.sentence_duration = sentence_duration
        self.crime = crime

    def update_sentence_duration(self, new_duration):
        self.sentence_duration = new_duration

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.prisoner_id}, Sentence Duration: {self.sentence_duration}, Crime: {self.crime}")
  
