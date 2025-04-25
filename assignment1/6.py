import math
def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)
def find_nearest_neighbors(points):
    nearest_neighbors = []
    for i in range(len(points)):
        current_point = points[i]
        nearest_distance = float('inf') 
        for j in range(len(points)):
            if i != j:  # Don't compare the point with itself
                dist = distance(current_point, points[j])
                if dist < nearest_distance:
                    nearest_distance = dist
                    nearest_point = points[j]
        nearest_neighbors.append((current_point, nearest_point))
    return nearest_neighbors
def main():
    points = []
    print("Enter 10 points in 3D space (x, y, z):")
    for i in range(10):
        x, y, z = map(float, input(f"Enter point {i + 1}: ").split())
        points.append((x, y, z))
    nearest_neighbors = find_nearest_neighbors(points)
    print("\nNearest Neighbors:")
    for point, neighbor in nearest_neighbors:
        print(f"Point {point} has nearest neighbor {neighbor}")
main()
