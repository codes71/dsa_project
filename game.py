import random
import pygame
import math
import heapq
import sys

def randomize_points(points):
    for key in points:
        points[key] = (random.randint(0, 100), random.randint(0, 50))

def generate_map(num_points=100, min_distance=50):
    points = {}
    labels = [str(i) for i in range(1, num_points + 1)]
    while len(points) < num_points:
        point = (random.randint(20, 780), random.randint(20, 580))
        if all(math.dist(point, p) >= min_distance for p in points.values()):
            label = labels[len(points)]
            points[label] = point
    with open('map.txt', 'w') as f:
        for label, point in points.items():
            f.write(f"{point[0]},{point[1]},{label}\n")
    return points

def generate_weights(points):
    weights = {}
    point_list = list(points.values())
    for i in range(len(point_list)):
        for j in range(i + 1, len(point_list)):
            weight = random.randint(1, 100)
            weights[(point_list[i], point_list[j])] = weight
            weights[(point_list[j], point_list[i])] = weight  # Assuming undirected graph
    return weights

def load_map(filename='map.txt'):
    points = {}
    weights = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(',')
            if len(parts) == 3:
                x, y, point_id = int(parts[0]), int(parts[1]), parts[2]
                points[point_id] = (x, y)
    return points

def dijkstra(points, weights, start, end):
    queue = [(0, start)]
    shortest_paths = {start: (None, 0)}
    while queue:
        (cost, current_point) = heapq.heappop(queue)
        if current_point == end:
            path = []
            while current_point is not None:
                path.append(current_point)
                next_point = shortest_paths[current_point][0]
                current_point = next_point
            path = path[::-1]
            return path, cost

        for (point1, point2), weight in weights.items():
            if point1 == points[current_point]:
                new_cost = cost + weight
                neighbor_label = [k for k, v in points.items() if v == point2][0]
                if neighbor_label not in shortest_paths or new_cost < shortest_paths[neighbor_label][1]:
                    shortest_paths[neighbor_label] = (current_point, new_cost)
                    heapq.heappush(queue, (new_cost, neighbor_label))

    return None, float('inf')

def display_map(points, path=None, total_weight=None, background_color=(255, 255, 255)):
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Map and Shortest Path")
    screen.fill(background_color)
    font = pygame.font.Font(None, 24)
    label_color = (0, 0, 0) if background_color == (255, 255, 255) else (255, 255, 255)

    for label, point in points.items():
        pygame.draw.circle(screen, (0, 0, 255), point, 5)
        label_render = font.render(label, True, label_color)
        screen.blit(label_render, (point[0] + 5, point[1] - 10))

    if path:
        for i in range(len(path) - 1):
            pygame.draw.line(screen, (0, 255, 0), points[path[i]], points[path[i + 1]], 2)
        weight_label = font.render(f"Total Weight: {total_weight}", True, label_color)
        screen.blit(weight_label, (10, 10))

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                

    pygame.quit()
    
def switch_background(points, background_color):
    display_map(points, background_color)

def main():
    if len(sys.argv) != 3:
        print("Usage: python game.py <start_point> <end_point>")
        return

    start = sys.argv[1]
    end = sys.argv[2]

    points = generate_map()
    weights = generate_weights(points)
    # display_map(points)

    if start not in points or end not in points:
        print("Invalid start or end point.")
        return

    path, total_weight = dijkstra(points, weights, start, end)
    display_map(points, path, total_weight)

if __name__ == "__main__":
    main()
