class Sensor:
    def __init__(self,name,description):
        self._name=name
        self._description=description
        
    def get_name(self):
        return self._name
    
    def get_description(self):
        return self._description
    
    def read_data(self):
         raise NotImplementedError("The method should be overidden")
    def update_agent(self):
        raise NotImplementedError("The method should be overidden")
     
#Location has been abstracted as a node in a graph     
class LocationSensor(Sensor):
    def __init__(self,name,description):
        super().__init__(name, description)
        self._location=None
    
    def read_data(self,node):
        self._location=node
        return node.get_name()
        
    def update_agent(self,drone):
        drone.set_current_location(self._location)

#This is an abstraction of temperature sensor and other weather related sensors      
class WeatherSensor(Sensor):
    def __init__(self, name, description):
        super().__init__(name, description)
        self._weather=None
        
    def read_data(self,node):
       self._weather = node.get_weather()
       
    def update_agent(self,drone):
        drone.set_weather(self._weather)
        
        
#Abstract definition of ultrasonic sound sensor for measuring obstacles
class ObstacleSensor(Sensor):
    def __init__(self, name, description):
         super().__init__(name, description)
         self._obstacle=None
    
    def read_data(self,node):
       self._obstacle = node.is_there_obstacle()
       
    def update_agent(self,drone):
        drone.set_obstacle(self._obstacle)
         
    
    
        
        
        
        
    
        
    
    
    