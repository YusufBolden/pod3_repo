from stations_challenge import *

bustation2 = BusStation(station_name = 'Brooklyn Megabus Stop',location = '53th street and 17h avenue',routes = ['Pittsburgh', 'DC', 'Albany']) 

subway_station2 = SubwayStation(station_name= '11th street', location= '14th street and 7th avenue', lines= ['a', '2', 'b', 'L'])

bustation3 = BusStation(station_name = 'Manhattan Station',location = '9th street and 8th avenue',routes = ['Baltimore', 'Harrisburg', 'Penn State']) 

bustation2.show_info()
subway_station2.show_info()
bustation3.show_info()