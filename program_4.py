# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.

# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2) 

import math

def distance(point1, point2):
    """Return the distance between two 3D points."""
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def main():
    print("This program is going to calculate the distance between two 3D points.")

    try:
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        z1 = float(input("Enter z1: "))
        point1 = (x1, y1, z1)

        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
        z2 = float(input("Enter z2: "))
        point2 = (x2, y2, z2)
        dist = distance(point1, point2)

        print(f"\nThe distance between {point1} and {point2} is {dist:.2f}")

    except ValueError:
        print("\nError: Please enter valid numbers for coordinates.")

if __name__ == "__main__":
    main()
