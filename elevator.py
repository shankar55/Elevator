class Elevator:
    def __init__(self, id, total_floors):
        self.id = id
        self.current_floor = 0
        self.total_floors = total_floors
        self.direction = None
        self.busy = False

    def move_up(self):
        if self.current_floor < self.total_floors:
            self.current_floor += 1

    def move_down(self):
        if self.current_floor > 0:
            self.current_floor -= 1

    def open_doors(self):
        print(f"Elevator {self.id} opening doors of {self.current_floor} floor")

    def close_doors(self):
        print(f"Elevator {self.id} closing doors of {self.current_floor} floor")

    def set_busy(self, value):
        self.busy = value
