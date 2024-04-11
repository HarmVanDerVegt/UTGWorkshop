def classify_triangle(side1, side2, side3):
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return "Invalid"  # Negative or zero length side
        
    if side1 == side2 == side3:
        return "Equilateral"  # All sides are equal

    if (side1 == side2) or (side2 == side3) or (side1 == side3):
        return "Isosceles"  # Two sides are equal

    if (side1 + side2 <= side3) or (side2 + side3 <= side1) or (side1 + side3 <= side2):
        return "Invalid"  # Triangle inequality theorem violated

    return "Scalene"  # No sides are equal
