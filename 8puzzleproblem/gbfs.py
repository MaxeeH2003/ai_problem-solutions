from state import State
from queue import PriorityQueue
def Greedy(given_state,n):
    frontier = PriorityQueue()
    explored = []
    counter = 0
    root = State(given_state,None,None,0,0)

    evaluation = root.Misplaced_Tiles(n)
    frontier.put((evaluation,counter,root))

    while not frontier.empty():
        current_node = frontier.get()
        current_node = current_node[2]
        explored.append(current_node.state)

        if current_node.test():
            return current_node.solution(), len(explored)

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                counter += 1
                evaluation = child.Misplaced_Tiles(n)
                frontier.put((evaluation,counter,child))
    return
