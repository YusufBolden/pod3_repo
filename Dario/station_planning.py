from stations_challenge import *

class Atrain(Station):
    def __init__(self, station_name, location):
        super().__init__(station_name, location)

    def show_info(self):
        print(f'The A train makes stops adjacent to lines in Manhattan, such as {self.station_name} on {self.location}.')

manhattan_stops = Atrain(station_name = '14th street', location = 'Penn Station')
manhattan_stops.show_info()


class Ctrain(Atrain):
    def __init__(self, station_name, location, interconnected):
        Atrain.__init__(self, station_name, location)
        self.interconnected = interconnected

    def show_info(self):
        print(f'The C and the A trains run through many of the same stops on the {self.interconnected}, including {self.station_name} on {self.location}')

manhattan_stops2 = Ctrain(interconnected = 'same line', station_name = '42nd street', location = 'Times Square.')
manhattan_stops2.show_info()

class M60Bus():
    def __init__(self, route, avenues, boroughs):
        self.route = route
        self.avenues = avenues
        self.boroughs = boroughs

    def harlem_laguardia(self):
        print(f'The M60 bus {self.route} {self.avenues} on its path through {self.boroughs} to Laguardia airport.')


throughway = M60Bus(route = 'travels through', avenues = '125th street', boroughs = 'Harlem and Queens')
throughway.harlem_laguardia()