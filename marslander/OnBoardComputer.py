from Vehicle import Vehicle
from BurnDataStream import BurnDataStream
from DescentEvent import DescentEvent
from BurnInputStream import BurnInputStream

class OnBoardComputer:

    def get_next_burn(self, status):

        velocity = status.get_velocity()
        altitude = status.get_altitude()
       #print ("altitude ", altitude)
        # fuel = status.fuel()

        burn = 0
        if status.get_altitude() > 8000:
            burn = 100
        elif 8000>=status.get_altitude() > 1000:
            if status.get_velocity() >= 200:
                burn = 200
            elif 200 > status.get_velocity() >=100 :
                burn = 100
        elif 1000 >= status.get_altitude() > 200:
            if status.get_velocity() == 100:
                burn = 100
        elif 200 >= status.get_altitude() >= 50:
            if status.get_velocity() == 100:
                burn = 175
            if status.get_velocity() == 25:
                burn = 100
        elif 50 > status.get_altitude() >= 10:
            if status.get_velocity() == 25:
                burn = 115
            if status.get_velocity() == 10:
                burn = 100
        elif 10 > status.get_altitude() >= 0:
            if status.get_velocity() == 10:
                burn = 108
            if status.get_velocity() == 2:
                burn = 100


        #print(burn)  # hack!
        return burn
