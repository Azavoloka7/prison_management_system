class Guard:
    def __init__(self, name, guard_id, shift):
        self.name = name
        self.guard_id = guard_id
        self.shift = shift

    def update_shift(self, new_shift):
        self.shift = new_shift

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.guard_id}, Shift: {self.shift}")
  
