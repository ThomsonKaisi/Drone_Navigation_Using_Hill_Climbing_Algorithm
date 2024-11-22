from decision import Decision
from node import Node
from drone import Drone
from sensor import LocationSensor, WeatherSensor, ObstacleSensor

#creating an environment of drone
#the drone will be flying in Gasabo district of Kigali, Rwanda
#Gasabo District Sectors
kimironko = Node("Kimironko")
kacyiru = Node("Kacyiru")
remera = Node("Remera")
gisozi = Node("Gisozi")
bumbogo = Node("Bumbogo")
gatsata = Node("Gatsata")
jabana = Node("Jabana")
rutunga = Node("Rutunga")
ndera = Node("Ndera")
kibagabaga = Node("Kibagabaga")
kinyinya = Node("Kinyinya")
nyarutarama = Node("Nyarutarama")
gikomero = Node("Gikomero")
rusororo = Node("Rusororo")
nduba = Node("Nduba")

#creating a graph representing gabosa district
kimironko.set_neighbors([remera, kacyiru, gisozi])
kacyiru.set_neighbors([kimironko, nyarutarama, gisozi])
remera.set_neighbors([kimironko, kacyiru, nyarutarama])
gisozi.set_neighbors([kimironko, kacyiru, bumbogo, kinyinya])
bumbogo.set_neighbors([gisozi, rutunga, jabana])
gatsata.set_neighbors([jabana, ndera, gisozi])
jabana.set_neighbors([bumbogo, gatsata, nduba])
rutunga.set_neighbors([bumbogo, gikomero])
ndera.set_neighbors([gatsata, rusororo])
kibagabaga.set_neighbors([nyarutarama, rusororo])
kinyinya.set_neighbors([gisozi, rusororo])
nyarutarama.set_neighbors([kacyiru, remera, kibagabaga])
gikomero.set_neighbors([rutunga, rusororo])
rusororo.set_neighbors([gikomero, kibagabaga, kinyinya, ndera])
nduba.set_neighbors([jabana])
sectors = [kimironko, kacyiru, remera, gisozi, bumbogo, gatsata, jabana, rutunga, ndera, kibagabaga, kinyinya, nyarutarama, gikomero, rusororo, nduba]
#creating sensors

location_sensor=LocationSensor(name="GPS-Sensor",description="Measures the current location of the drone")
weather_sensor=WeatherSensor(name="Weather",description="Measures weather condition at a certain location")
obstacle_sensor=ObstacleSensor(name="Utra-sonic sensor",description="measures if there is an obstacle at a specific location")

sensors= [location_sensor,weather_sensor,obstacle_sensor]

#adding sensors to drone
#setting maxmum payload a drone can carry to 4kgs
drone=Drone(sensors=sensors,maxpayload=4)
drone.set_map(map=sectors)


#drone drive

def drone_fly():
    #getting location sensor, it has index 0
    location =drone.get_sensor(0)
    #setting initial location to kimironko
    print(f"Starting Flight in {location.read_data(kimironko)}")
    location.update_agent(drone)
    #setting destination to gatsata
    drone.set_destination(nyarutarama)
    drone.fly(drone)
          
    
drone_fly()
    
    
    





