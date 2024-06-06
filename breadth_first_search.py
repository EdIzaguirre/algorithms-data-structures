from collections import deque


def breadth_first_search(graph, name):
    """
    Input: Graph and initial node
    Output: True if desired node is found. False otherwise.
    """
    # 1 Keep a queue of people to check
    search_queue = deque()
    search_queue += graph['you']
    already_checked = set()
    while search_queue:
        # 2 Pop a person off of the queue
        candidate = search_queue.popleft()
        # 3 Check to see if person has already been checked
        if candidate not in already_checked:
            # 4 Check if this person is the one we are looking for
            if candidate == name:
                # 5 Yes? Finished! No? Add all neighbors to queue
                return True
            already_checked.add(candidate)
            search_queue += graph[candidate]
        # 6 Loop!

    return False


# Setting up directed graph
graph = {}
graph['Mary'] = ['Sue', 'Tom']
graph['Sue'] = ['Jim', 'Joe']
graph['Tom'] = []
graph['Jim'] = ['Tom']
graph['Joe'] = []
graph['you'] = ['Mary', 'Sue', 'Tom']

print(breadth_first_search(graph, "Jim"))
print(breadth_first_search(graph, "Sue"))
print(breadth_first_search(graph, "Holland"))
