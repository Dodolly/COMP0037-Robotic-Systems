from math import sqrt
from queue import PriorityQueue

from .planner_base import PlannerBase

class GreedyShortestDistancePlanner(PlannerBase):

    # Q4a:
    # Add queue definition
    def __init__(self, occupancyGrid):
        PlannerBase.__init__(self, occupancyGrid)
        self.priorityQueue = PriorityQueue()

    # Q4a:
    # Implement computing the search key and add to the priority queue
    def pushCellOntoQueue(self, cell):
        #Distance to the goal
        cellCoords = cell.coords()
        goalCoords = self.goal.coords()
        dX = cellCoords[0] - goalCoords[0]
        dY = cellCoords[1] - goalCoords[1]
        d = sqrt(dX*dX + dY*dY)
        self.priorityQueue.put((d, cell))
    
    # Q4a:
    # Check the queue size is zero
    def isQueueEmpty(self):
        return self.priorityQueue.empty()
        
    # Q4a:
    # Simply pull from the front of the list
    def popCellFromQueue(self):
        t = self.priorityQueue.get()
        return t[1]

    def resolveDuplicate(self, cell, parentCell):
        # Nothing to do in this case
        pass
