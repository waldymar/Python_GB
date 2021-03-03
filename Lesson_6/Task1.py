from time import sleep

my_dict = {"red": 7,
           "yellow": 2,
           "green": 7}

class TrafficLight:
    __color = "red"

    def running(self):
        print(TrafficLight.__color)
        sleep(my_dict.get(TrafficLight.__color))
        TrafficLight.__color = "yellow"
        print(TrafficLight.__color)
        sleep(my_dict.get(TrafficLight.__color))
        TrafficLight.__color = "green"
        print(TrafficLight.__color)
        sleep(my_dict.get(TrafficLight.__color))

my_tfl = TrafficLight()
my_tfl.running()