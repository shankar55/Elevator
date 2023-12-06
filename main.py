from controller import Controller
from request import Request


def main():
    controller = Controller()
    while True:
        source_floor = int(input("Enter your source floor number(0-5): "))
        destination_floor = int(input("Enter destination floor number(0-5): "))
        request = Request(source_floor, destination_floor)
        if source_floor < 0 or source_floor > 5 or destination_floor < 0 or destination_floor > 5:
            print("Invalid floor, please try again")
        else:
            controller.handle_request(request)


if __name__ == '__main__':
    main()
