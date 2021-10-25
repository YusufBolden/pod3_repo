#from stations_challenge import Station
from stations_challenge import BusStation
from stations_challenge import SubwayStation
 


bus_station2 = BusStation(station_name = "Walmart Station",location = "Walmart", routes = "Nomans Land, Dire District, All Capstone")
bus_station2.show_info()
bus_station2.closed_station()
bus_station2.show_info()

subway_station2 = SubwayStation(station_name = "PA Station", location ="Perth Amboy", lines = "Manhattan to Uptown")
subway_station2.show_info()

bus_station3 = BusStation(station_name = "Co Colabs", location = "Colorado", routes = "Columbia, Yale, Amsterdam")
bus_station3.show_info()
bus_station3.closed_station()
bus_station3.show_info()
bus_station3.open_station()
bus_station3.show_info()