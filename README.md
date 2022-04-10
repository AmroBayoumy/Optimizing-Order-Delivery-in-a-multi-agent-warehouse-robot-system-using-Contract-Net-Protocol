# MAS_Project

# Abstract:
While the use of autonomous agents in warehouses is becoming more prevalent across different industries, a few challenges remain elusive. In this assignment, we aim to examine how to optimize order delivery in an autonomous warehouse with respect to the number of agents used and the total delivery time for a sequence of orders. The system developed consists of 4 main layers, which are an environment, an agent, a solver and an input layer. This system was built using Python based on pure logic for operation as well as pre existing libraries. By defining the grid, obstacles, agents and stations in the input layer, the environment is able to integrate and render a whole warehouse. After which, the agent layer defines the logic behavior of all agents. Then, the solver layer receives a map from the environment layer which it utilizes to generate a trajectory for each agent through traversing the map as a graph using A*. To test the system, three experiment were conducted, increasing agents count in an crowded environment, increasing agents count in an obstacle free environment and increasing the size of the grid (and obstacles count) whilst maintaining agents count. The experiments were analyzed for the total distance an agent elapsed between pickup and delivery, the minimum distance set by the graph solver, the loss (i.e, the difference between both distances) as well as the order fulfillment time from pickup to delivery. The results show that increasing the grid size increases order time linearly. Additionally, they show that increasing the number of agents reduces the order fulfillment time in free grids, however, in occupied (obstacles) grids, there exists an inflection point after which the agents impede each other. 

![alt text](https://github.com/AmroBayoumy/Optimizing-Order-Delivery-in-a-multi-agent-warehouse-robot-system-using-Contract-Net-Protocol/blob/main/g1.PNG)
## Commands
Install dependency: python3 -m pip install --user tcod<br>
Execute simulation: python3 environment.py<br>
Execute visualization: python3 visualize.py<br>
Execute both: python3 environment.py && python3 visualize.py<br>
