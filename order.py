from enum import Enum
from numpy import sqrt

class Order_State(Enum):
    _Not_Assigned = 0
    _Assigned = 1
    _Picked  = 2
    _Delivered = 3

class Order:
    current_objective = ()

    def __init__(self, deliveryStation, pickupStation, requested_quantities, timestep_begin, id_code, state=0):
        self.id_code = id_code
        self.agent_assigned = None
        self.pickupStation = pickupStation
        self.deliveryStation = deliveryStation
        self.distance = sqrt((pickupStation[0] - deliveryStation[0])**2 + (pickupStation[1] - deliveryStation[1])**2)
        self.requested_quantities = requested_quantities
        self.timestep_begin = timestep_begin
        self.agent_pos = None #agent_pos_at_timestep_pick
        self.timestep_pick = None
        self.timestep_end = None
        self.state = state
        self.agentId = None
        self.timestep_of_assignment = None

    def assign_order(self, agentId, timestep, agent_pos):
        self.agentId = agentId
        self.state = 1
        self.timestep_of_assignment = timestep
        self.agent_pos = agent_pos

    def deAssign_order(self):
        '''
        Used for eCNP to remove assignment of order.
        '''
        self.agentId = None
        self.state = 0
        self.timestep_of_assignment = None

    def getTimestep_begin(self):
        return self.timestep_begin

    def getAgentId(self):
        return self.agentId

    def getOrderId(self):
        return self.id_code

    def get_order_state(self):
        return self.state

    def set_order_state(self, state):
        self.state = state

    def getPickupStation(self):
        return self.pickupStation

    def get_objective(self):
        if self.state == 1:
            return self.pickupStation
        elif self.state == 2:
            return self.deliveryStation
        else:
            print("exit() in order get_objective")
            exit()
            return None
