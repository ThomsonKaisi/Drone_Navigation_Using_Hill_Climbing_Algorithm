from decision import Decision
class Drone:
    def __init__(self,sensors,maxpayload):
        self._payload_weight=None
        self._max_payload=maxpayload
        self._current_location=None
        self._obstacle=None
        self._destination=None
        self._map=[]
        self._sensors=sensors
        self._decision=None
        self._decision=Decision()
    def get_sensor(self,index):
        return self._sensors[index]
    def set_payload(self,payload):
        if payload >self._max_payload:
            print(f"Payload too heavy, reduce it to: {self._max_payload}")
        else:
            self._payload_weight=payload
            print("Payload loaded successfully")
            
    def set_weather(self,sensor_weather_input):
        self._weather_conditions.append(sensor_weather_input)
    
    def set_current_location(self,location_sensor_input):
        self._current_location = location_sensor_input
        
    def set_obstacle(self,obstacle):
        self._obstacle=obstacle
    def set_destination(self,node):
        self._destination=node
    def set_map(self,map):
        self._map.extend(map)
        self._calculate_node_cost()
    #Calculating the cost to every city or area that the drone can pass
    def _calculate_node_cost(self):
        if self._map is not None:
            for node in self._map:
                self._decision.calculate_node_cost(node=node)
            print("Node cost calculation completed")
        else:
            print("No Map is Given !!!")
            
    def get_current_location(self):
        return self._current_location
    def get_destination(self):
        return self._destination
    def fly(self,drone):
        self._decision.fly_decision(drone)
        
    
        
            
        