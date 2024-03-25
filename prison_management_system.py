from models.prisoner import Prisoner
from models.guard import Guard
from models.facility import Facility

class PrisonManagementSystem:
    def __init__(self):
        self.prisoners = []
        self.guards = []
        self.facilities = []

    def add_prisoner(self, prisoner):
        self.prisoners.append(prisoner)

    def remove_prisoner(self, prisoner_id):
        self.prisoners = [p for p in self.prisoners if p.prisoner_id != prisoner_id]

    def add_guard(self, guard):
        self.guards.append(guard)

    def remove_guard(self, guard_id):
        self.guards = [g for g in self.guards if g.guard_id != guard_id]

    def add_facility(self, facility):
        self.facilities.append(facility)

    def remove_facility(self, facility_id):
        self.facilities = [f for f in self.facilities if f.facility_id != facility_id]

    def display_prisoners(self):
        print("Prisoners:")
        for prisoner in self.prisoners:
            prisoner.display_info()

    def display_guards(self):
        print("Guards:")
        for guard in self.guards:
            guard.display_info()

    def display_facilities(self):
        print("Facilities:")
        for facility in self.facilities:
            facility.display_info()
  
