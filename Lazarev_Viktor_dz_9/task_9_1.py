import itertools
import time


class TrafficLight:
    __color = {'красный': 7, 'жёлтый': 2, 'зелёный': 7}

    def running(self):
        for key, value in itertools.cycle(self.__color.items()):
            print(key)
            time.sleep(value)


traffic_light = TrafficLight()
traffic_light.running()
