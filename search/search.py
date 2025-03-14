# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    
    #Initializing the closed set and the fringe
    closed = set()
    fringe = util.Stack() #Stack is used to implement Depth First Search
    fringe.push((problem.getStartState(), []))
    
    #Iterating through the fringe until it is empty
    while not fringe.isEmpty():
        #Getting the state and path from the fringe
        state, path = fringe.pop()
 
        #If the state is the goal, return the path
        if problem.isGoalState(state):
            return path
        
        #If the state is already in the closed set, continue
        if state in closed:
            continue
        
        #Add the state to the closed set
        closed.add(state)
        
        #Iterate through the successors of the state and add them to the fringe
        for successor, action, _ in problem.getSuccessors(state):
            fringe.push((successor, path + [action]))
     
    #If the fringe is empty and no solution is found, return an empty list
    return []

    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #Initializing the closed set and the fringe
    closed = set()
    fringe = util.Queue() #Queue is used to implement Breadth First Search
    fringe.push((problem.getStartState(), []))
    
    #Iterating through the fringe until it is empty
    while not fringe.isEmpty():
        #Getting the state and path from the fringe
        state, path = fringe.pop()
 
        #If the state is the goal, return the path
        if problem.isGoalState(state):
            return path
        
        #If the state is already in the closed set, continue
        if state in closed:
            continue
        
        #Add the state to the closed set
        closed.add(state)
        
        #Iterate through the successors of the state and add them to the fringe
        for successor, action, _ in problem.getSuccessors(state):
            fringe.push((successor, path + [action]))
    
    #If the fringe is empty and no solution is found, return an empty list
    return []

    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #Initializing the closed set and the fringe
    closed = set()
    fringe = util.PriorityQueue() #PriorityQueue is used to implement Uniform Cost Search
    fringe.push((problem.getStartState(), []), 0)
    
    #Iterating through the fringe until it is empty
    while not fringe.isEmpty():
        #Getting the state and path from the fringe
        state, path = fringe.pop()
 
        #If the state is the goal, return the path
        if problem.isGoalState(state):
            return path
        
        #If the state is already in the closed set, continue
        if state in closed:
            continue
        
        #Add the state to the closed set
        closed.add(state)
        
        #Iterate through the successors of the state and add them to the fringe
        for successor, action, _ in problem.getSuccessors(state):
            fringe.push((successor, path + [action]), problem.getCostOfActions(path + [action]))
    
    #If the fringe is empty and no solution is found, return an empty list
    return []

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #Initializing the closed set and the fringe
    closed = set()
    fringe = util.PriorityQueue() #PriorityQueue is used to implement A* Search
    fringe.push((problem.getStartState(), []), 0)
    
    #Iterating through the fringe until it is empty
    while not fringe.isEmpty():
        #Getting the state and path from the fringe
        state, path = fringe.pop()
 
        #If the state is the goal, return the path
        if problem.isGoalState(state):
            return path
        
        #If the state is already in the closed set, continue
        if state in closed:
            continue
        
        #Add the state to the closed set
        closed.add(state)
        
        #Iterate through the successors of the state and add them to the fringe
        for successor, action, _ in problem.getSuccessors(state):
            fringe.push((successor, path + [action]), problem.getCostOfActions(path + [action]) + heuristic(successor, problem)) #Adding the heuristic to the priority of the fringe
    
    #If the fringe is empty and no solution is found, return an empty list
    return []

    util.raiseNotDefined()


# Abbreviations
dfs = depthFirstSearch
bfs = breadthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
