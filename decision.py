class Decision:
    def __init__(self):
        #each weather has a weight on how it affects the movement of a drone
        self._weights = { "rain": 10, "sun": 2, "wind": 20}
    
    def calculate_node_cost(self,node):
        weather =node.get_weather() 
        cost =int(sum(weather[condition] * self._weights[condition] for condition in weather))
        if node.is_there_obstacle():
            cost+=100
        node.set_cost(cost)
    def fly_decision(self, drone):
        visited = set()  #use a set for efficient visited tracking
        current_location = drone.get_current_location()
        destination = drone.get_destination()

        while current_location != destination:
            next_node = self._hill_climbing(current_location, destination, visited)
            visited.add(current_location.get_name())  #mark current location as visited
            print(f"FLYING TO : {next_node.get_name()}, Metric: {next_node.get_cost()}")
            
            #update the drone's location via its sensor
            location_sensor = drone.get_sensor(0)
            location_sensor.read_data(next_node)
            location_sensor.update_agent(drone)
            
            current_location = next_node  #move to the next node

        print("Arrived at Destination!!")
        print(destination.get_name())
        print(f"Path:{visited} ")

    def _hill_climbing(self, current_location, destination, visited):
            neighbours = current_location.get_neighbours()
            if current_location == destination:
                return destination

            next_node_cost = float('inf')  #set initial cost to infinity
            next_node = None

            for neighbour in neighbours:
                if neighbour.get_name() not in visited:  #check visited using the node name
                    import time
                    print("Decision Making ...")
                    print(f"Checking Cost of {neighbour.get_name()}")
                    print(f"Cost: {neighbour.get_cost()}")
                    print(f"Weather Condition Probability:{neighbour.get_weather()}")
                    time.sleep(1)
                    if neighbour.get_cost() < next_node_cost:
                        next_node = neighbour
                        next_node_cost = neighbour.get_cost()

            if next_node is None:
                print("No valid moves available. Stuck!")
                import sys
                sys.exit(0)
            return next_node
