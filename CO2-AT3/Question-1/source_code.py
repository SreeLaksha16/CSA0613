import math

def closest_pair(points):

    # Initialize minimum distance with infinity
    min_dist = float('inf')

    # Store total number of points
    n = len(points)

    # Compare every pair of points
    for i in range(n):

        # Store current point once
        x1, y1 = points[i]

        for j in range(i + 1, n):

            # Store second point once
            x2, y2 = points[j]

            # Calculate Euclidean distance
            dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

            # Correct comparison
            if dist < min_dist:
                min_dist = dist

    return min_dist


# Driver Code
points = [(2,3), (12,30), (40,50), (5,1), (12,10), (3,4)]

answer = closest_pair(points)

print("Minimum Distance =", answer)
