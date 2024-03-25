from prison_management_system import PrisonManagementSystem
from models.prisoner import Prisoner
from models.guard import Guard
from models.facility import Facility
from faker import Faker

def generate_prisoners(count):
    fake = Faker('uk_UA')
    prisoners = []
    for _ in range(count):
        name = fake.name()
        prisoner_id = "P" + str(_ + 1).zfill(3)
        sentence_duration = fake.random_int(min=1, max=20)  # Generating sentence duration from 1 to 20 years
        crime = fake.random.choice(["Robbery", "Forgery", "Assault", "Drug Trafficking", "Burglary"])
        prisoner = Prisoner(name, prisoner_id, f"{sentence_duration} years", crime)
        prisoners.append(prisoner)
    return prisoners

def generate_guards(count):
    fake = Faker('uk_UA')
    guards = []
    for _ in range(count):
        name = fake.name()
        guard_id = "G" + str(_ + 1).zfill(3)
        shift = fake.random.choice(["Day", "Night"])
        guard = Guard(name, guard_id, shift)
        guards.append(guard)
    return guards

def main():
    prison_system = PrisonManagementSystem()

    # Generate 10 prisoners and add them to the system
    prisoners = generate_prisoners(10)
    for prisoner in prisoners:
        prison_system.add_prisoner(prisoner)

    # Generate 20 guards and add them to the system
    guards = generate_guards(20)
    for guard in guards:
        prison_system.add_guard(guard)

    # Creating facilities
    facility1 = Facility("F001", "Cell Block", 100)
    facility2 = Facility("F002", "Kitchen", 50)

    prison_system.add_facility(facility1)
    prison_system.add_facility(facility2)

    # Displaying information
    prison_system.display_prisoners()
    prison_system.display_guards()
    prison_system.display_facilities()

if __name__ == "__main__":
    main()
