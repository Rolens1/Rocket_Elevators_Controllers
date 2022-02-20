class Column:

    def get_Details(self):
        _floors = int(input('How many floors : '))
        self._floors = _floors

        _basements = input('How many basements : ')
        self._basements = _basements

        _elevators = int(input('How many elevators per column : '))
        self._elevators = _elevators

        print(f'You have {self._floors} floors, {self._basements} basements, {self._elevators} elevators per column')

        self.elevators = create_elevators(_elevators)

def create_elevators(total):
    total = total
    x = 0
    li = []
    while(x < total):
        elevator = Elevator()
        elevator.el()
        elevator.id = x
        li.append(elevator)
        x += 1

    for obj in li:
        print(f'This is elevator no.{obj.id}, at position {obj.position}, going to {obj.dir}')
    
    return li

class Elevator:
    def el(self):
        self.position = 0
        self.dir = 0
        self.id = 0
        
class User:
    def user(self):
        self.position = int(input("Starting position of user : "))
        self.dir = int(input('Destination of user : '))
        self.inside = False

def closest_elevator(arr, user):
    arr = arr
    user_pos = user.position
    difference = 999
    best = arr[0]
    
    for obj in arr:
        pos = obj.position
        if user_pos > pos:
            x = user_pos - pos
        elif user_pos <= pos:
            x = pos - user_pos
        
        if x < difference:
            difference = x
            best = obj

    return best

def move_elevator(elevator, user):
    if(elevator.position < user.position):
        elevator.dir = user.dir
        movingUp = True
        movingDown = False
        idle = False
    if(elevator.position > user.position):
        elevator.dir = user.dir
        movingUp = False
        movingDown = True
        idle = False
    if(elevator.position == user.position):
        elevator.dir = user.dir
        movingUp = False
        movingDown = False
        idle = True

    while movingUp:
        elevator.position += 1
        print(f"Elevator going up a floor {elevator.position}")
        if elevator.position == user.position:
            movingUp = False
            idle = True
            print('elevator at right destination')

    while movingDown:
        elevator.position -= 1
        print(f"Elevator going down a floor {elevator.position}")
        if elevator.position == user.position:
            movingDown = False
            idle = True
            print('elvator at right destination')

    user.inside = True

    while user.inside:
        elevator.dir = user.dir
        while user.position < user.dir:
            elevator.position += 1
            user.position = elevator.position
            print(f"going up at Floor {elevator.position}")
        while user.position > user.dir:
            elevator.position -= 1
            user.position = elevator.position
            print(f"going down at Floor {elevator.position}")
        if user.dir == user.position:
            print(f'user going out the elevator on floor {user.position}')
            user.inside = False
    
    



while True:
    answer = input('Do you want to try our elevator? y/n : ').lower()

    if 'y' in answer:
        print('Yes')
        print("BASIC INFOS")
        column = Column()
        column.get_Details()
        move = input('Do you want to  move some elevators? :').lower()
        if 'y' in move:
            while True:
                x = int(input('Wich one (enter elevator number) : '))
                y = int(input("Where ? (enter floor) : "))
                column.elevators[x].position = column.elevators[x].dir = y 
                print(f'Elevator no.{x}, at position {y}')
                ask = input('another one ? y/n ')
                if 'n' in ask:
                    break
        
        print('Everything is set up!')
        for obj in column.elevators:
            print(f'This is elevator no.{obj.id}, at position {obj.position}, going to {obj.dir}')

        print("now let's set up the user")
        user = User()
        user.user()
        print(f'user is at floor {user.position} and going to floor {user.dir}')

        best = closest_elevator(column.elevators, user)
        print(f'best elevator is {best.id} on floor {best.position}!')

        move_elevator(best, user)



        break


    else:
        print('no')
        break
        

