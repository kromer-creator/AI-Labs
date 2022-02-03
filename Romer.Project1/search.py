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

def depthFirstSearch(problem):
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

    # SOURCE: https://www.tutorialspoint.com/data_structures_algorithms/depth_first_traversal.htm
    # I used this source & code I wrote for algorithms class last semester to create this fxn

    visited = []    # List to keep track of nodes that have been visited
    stack = util.Stack()    # Create stack using stack class
    # Push tuple to stack, first value is the start node and second value is a list to track the path
    stack.push((problem.getStartState(), []))

    while not stack.isEmpty():  # Loop as long as the stack isn't empty
        node, path = stack.pop()    # Pop the node and path from the top of the stack
        visited.append(node)        # Append the node the visited to track which nodes have been traversed
        if problem.isGoalState(node):   # If the goal state is reached, return the path taken
            return path
        successors = problem.getSuccessors(node)    # Find where to search next by finding the node's successors
        for s in successors:
            # If we have not visited a successor, then push it to the stack
            if s[0] not in visited:
                stack.push((s[0], path + [s[1]]))

    return path   # Return the path

    #util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    # SOURCE: https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/tutorial/
    # This pseudocode for BFS was SUPER helpful!

    visited = []    # Create list to hold visited nodes
    queue = util.Queue()    # Create queue
    queue.push((problem.getStartState(), []))   # Push start state to queue
    visited.append(problem.getStartState())     # Append start node to visited

    while not queue.isEmpty():
        node, path = queue.pop()    # Pop node off queue and add to path
        if problem.isGoalState(node):   # Return path if it have reached goal state
            return path
        successors = problem.getSuccessors(node)    # Get successors of node
        for s in successors:
            if s[0] not in visited:
                # If we have not visited a successor then push it to the queue
                # We track the path in the queue as well
                queue.push((s[0], path + [s[1]]))
                # Add the successor to the visited list
                visited.append(s[0])

    #util.raiseNotDefined()
    return path   # Return the path

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    # SOURCE: https://www.geeksforgeeks.org/uniform-cost-search-dijkstra-for-large-graphs/
    # I had not heard of uniform cost search, but this source was great.
    # I'd heard of dijkstra's algorithm and this implementation helped me understand.

    pQueue = util.PriorityQueue()   # Initialize the priority queue
    visited = []    # Initialize list of visited nodes
    # Push start node, path, and cost value to queue
    pQueue.push((problem.getStartState(), []), 0)

    while not pQueue.isEmpty():     # Loop as long as queue isn't empty
        node, path = pQueue.pop()   # Pop node off queue and assign to node and path
        if problem.isGoalState(node):   # Return the path if goal state is reached
            return path
        if node not in visited:     # Get successors of node if it hasn't been visited
            successors = problem.getSuccessors(node)
            for s in successors:
                if s[0] not in visited:
                    # Push node & path of successor to priority queue if it has not been visited
                    # Use the cost of actions fxn to add priority to the queue along with the node and path
                    pQueue.push((s[0], path + [s[1]]), problem.getCostOfActions(path + [s[1]]))
        # Append the node to the visited list
        visited.append(node)

    return path     # Return the path


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
