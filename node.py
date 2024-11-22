import random
class Node:
    def __init__(self,name):
        self._name=name
         #Each node has a neighbour
        self._neighbours =[]
        #random weather conditions with the probabilities 
        self._weather={"rain":random.random(),"sun":random.random(),"wind":random.random()}
        #The cost of passing through this node which shall be generated based on probability of weather
        self._cost=None
        #availability of obstacle is random per node
        self._obstacle = random.choice([True, False])
        #normalizing the probability so that the sum should be each to 1
        self._probability_normalization()
        
    def set_neighbors(self,neighbour):
        if neighbour not in self._neighbours:
            self._neighbours.extend(neighbour)
    def get_weather(self):
        return self._weather       
    def get_weather(self):
        return self._weather
    def get_name(self):
        return self._name
    def set_cost(self,cost):
        self._cost=cost
    def get_neighbours_names(self):
        names=[]
        for neighbour in self._neighbours:
            names.append(neighbour.get_name())
        return names
    def get_neighbours(self):
        return self._neighbours
    def is_there_obstacle(self):
            return self._obstacle
        
    def set_cost(self,cost_from_decision):
        self._cost=cost_from_decision
    
    def get_cost(self):
        if self._cost is not None:
            return self._cost
        
    def _probability_normalization(self):
        total = sum(self._weather.values())
        self._weather = {key: round((value / total),2) for key, value in self._weather.items()}
        
    
            
            
    