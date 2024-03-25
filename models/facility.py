class Facility:
    def __init__(self, facility_id, facility_type, capacity):
        self.facility_id = facility_id
        self.facility_type = facility_type
        self.capacity = capacity

    def update_capacity(self, new_capacity):
        self.capacity = new_capacity

    def display_info(self):
        print(f"ID: {self.facility_id}, Type: {self.facility_type}, Capacity: {self.capacity}")
 
