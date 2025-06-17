import networkx as nx
import json

class PathPlanner:
    def __init__(self, map_file='pathfinding/obstacle_map.json'):
        with open(map_file) as f:
            self.map_data = json.load(f)
        
        self.graph = nx.grid_2d_graph(
            self.map_data['width'], 
            self.map_data['height']
        )
        self.remove_obstacles()
    
    def remove_obstacles(self):
        for obstacle in self.map_data['obstacles']:
            self.graph.remove_node(tuple(obstacle))
    
    def find_path(self, start, end):
        return nx.astar_path(self.graph, start, end)