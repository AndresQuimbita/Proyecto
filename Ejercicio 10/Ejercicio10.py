
'''
10. You have a graph of  𝑛  nodes. You are given an integer  𝑛  and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
Return the number of connected components in the graph.

Example 1:

Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Example 2:

Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
'''


def visited_1(self, n, visited):
    '''
    Set visited edges in a pyhton list (adjencency list form of a graph)
    '''
    visited[n] = True
    for i in self[n]:
        if (not visited[i]):
            visited_1(self, i, visited)


def n_edges(edges, n):
    '''
    Calculate the number of total compoments connected in a graph, usign a python list to represent a adjencency list form of a graph
    '''
    count = 0
    edge = [[] for i in range(n)]
    visit = [False for i in range(n)]
    for i in edges:
        edge[i[0]].append(i[1])
        edge[i[1]].append(i[0])
    for i in range(n):
        if (visit[i] == False):
            visited_1(edge, i, visit)
            count += 1
    return count
