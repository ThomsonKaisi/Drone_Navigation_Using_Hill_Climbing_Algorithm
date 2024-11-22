# Drone_Navigation_Using_Hill_Climbing_Algorithm
This repository contains a simulation that demonstrates how a drone can use the Hill Climbing algorithm to find the best path for navigation from a source to a destination. The algorithm focuses on incrementally improving the path by evaluating neighboring positions to identify the optimal route while avoiding obstacles and constraints.

## Features

### 1. Environment Simulation
- **Gasabo District Representation**: 
  - The district is modeled as a graph, where nodes represent sectors.
  - Connections between sectors are defined as neighbors.
- **Example Sectors**: Kimironko, Kacyiru, Nyarutarama, Gisozi, etc.

### 2. Sensors
The drone is equipped with the following sensors:
- **Location Sensor**: Tracks and updates the drone's current location.
- **Weather Sensor**: Measures weather conditions at the current location.
- **Obstacle Sensor**: Detects obstacles in the drone's path.

### 3. Drone Operations
- **Payload Support**: The drone can carry a maximum payload of 4 kg.
- **Map Integration**: The drone uses the graph-based map for navigation.
- **Flight Simulation**: From a defined start point (e.g., Kimironko) to a destination (e.g., Nyarutarama).

---

## Structure

### Nodes (Sectors)
Each sector in Gasabo District is represented as a `Node` with connections (neighbors) to adjacent sectors.

### Sensors
- **GPS-Sensor**: Provides the drone's current location.
- **Weather Sensor**: Supplies environmental data.
- **Ultrasonic Sensor**: Detects obstacles on the path.

### Drone
- Configured with a set of sensors for data-driven decision-making.
- Operates on a graph-based map for navigation.

---

## How It Works

### Environment Setup
1. The district is defined as a graph of connected nodes.
2. Sensors are created and added to the drone.

### Flight Simulation
1. The drone's initial location is set to **Kimironko**.
2. The destination is set to **Nyarutarama**.
3. The drone navigates the environment using its sensors and predefined map.

### Navigation Process
- Reads the initial location using the **GPS sensor**.
- Iteratively updates the drone's position while:
  - Avoiding obstacles.
  - Adapting to weather conditions.

---

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Drone_Navigation_Using_Hill_Climbing_Algorithm.git
   cd drone-gasabo-navigation

