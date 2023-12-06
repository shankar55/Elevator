from elevator import Elevator


class Controller:
    def __init__(self):
        self.elevators = [Elevator(i, 5) for i in range(5)]

    def handle_request(self, request):
        available_elevators = [e for e in self.elevators if not e.busy]
        closest_elevator = min(available_elevators, key=lambda e: abs(e.current_floor - request.source_floor))

        if closest_elevator:
            closest_elevator.set_busy(True)
            self.process_request(closest_elevator, request)
            closest_elevator.set_busy(False)
        else:
            print("All elevators are busy. Please try again later.")

    @staticmethod
    def process_request(elevator, request):
        # Move the elevator to the source floor and then to the destination floor
        while elevator.current_floor != request.source_floor:
            if elevator.current_floor < request.source_floor:
                elevator.move_up()
            else:
                elevator.move_down()
        elevator.open_doors()
        elevator.close_doors()

        # Move the elevator to the destination floor
        while elevator.current_floor != request.destination_floor:
            if elevator.current_floor < request.destination_floor:
                elevator.move_up()
            else:
                elevator.move_down()
        elevator.open_doors()
        elevator.close_doors()
