"""Code By Iustin Andrei Moisa Tudor"""
"""Importing the necessary packages"""

import math 
import random
import time

"""Defyning a function to find closest points between a series of x and y coordinates"""
def find_points(points):
    n = len(points)
    min_distance = float('inf')
    closest = None

    for i in range(n):
        for j in range(i+1, n):
            distance = math.sqrt((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)
            if distance < min_distance:
                min_distance = distance
                closest = (points[i], points[j])

    return closest, min_distance

def user_points():
    n = int(input("Enter the number of points you want: "))
    points = []
    for i in range(n):
        x, y = map(float, input(f"Enter the coordinates for each point one by one {i+1}: ").split())
        points.append((x, y))
    return points


def Answer():
    global lines, points
    option = int(input("Select option:\n1. Find closest points from random generator\n2. Find closest points from user input\n3. 1000 Coordinates\n4. 10.000 Coordinates\n5. 100 Coordinates\nEnter your choice: "))
    if option == 1:
        points = [(1.8, 8.4), (5.6, 913), (3.6, 8.2), (0.95, 9.2), (25.1, 5.6), (7.9, 5.31)]
        start = time.time()
        closest_points, min_distance = find_points(points)
        end = time.time()
        if closest_points is not None:
            print(f"The closest points are {closest_points} with a distance of {min_distance:.2f}")
            print(f"Time taken: {end - start:.6f} seconds")

    elif option == 2:
        points = user_points()
        start = time.time()
        closest_points, min_distance = find_points(points)
        end = time.time()
        if closest_points is not None:
            print(f"The closest points are {closest_points} with a distance of {min_distance:.2f}")
            print(f"Time taken: {end - start:.6f} seconds")

    elif option == 3:
        points = [(round(random.uniform(0, 10), 2), round(random.uniform(0, 10), 2)) for _ in range(1000)]
        start = time.time()
        closest_points, min_distance = find_points(points)
        end = time.time()
        if closest_points is not None:
            print(f"The closest points are {closest_points} with a distance of {min_distance:.2f}")
            print(f"Time taken: {end - start:.6f} seconds")

    elif option == 4:
        points = [(round(random.uniform(0, 10), 2), round(random.uniform(0, 10), 2)) for _ in range(10000)]
        start = time.time()
        closest_points, min_distance = find_points(points)
        end = time.time()
        if closest_points is not None:
            print(f"The closest points are {closest_points} with a distance of {min_distance:.2f}")
            print(f"Time taken: {end - start:.6f} seconds")
    
    elif option == 5:
        points = [(round(random.uniform(0, 10), 2), round(random.uniform(0, 10), 2)) for _ in range(100)]
        start = time.time()
        closest_points, min_distance = find_points(points)
        end = time.time()
        if closest_points is not None:
            print(f"The closest points are {closest_points} with a distance of {min_distance:.2f}")
            print(f"Time taken: {end - start:.6f} seconds")
Answer()
