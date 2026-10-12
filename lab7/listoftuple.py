li = [(2, 3), (3, 1), (-1, -2), (0, 0)]

quadrants = {
    q: [p for p in li if (
        (q == "Quadrant I" and p[0] > 0 and p[1] > 0) or
        (q == "Quadrant II" and p[0] < 0 and p[1] > 0) or
        (q == "Quadrant III" and p[0] < 0 and p[1] < 0) or
        (q == "Quadrant IV" and p[0] > 0 and p[1] < 0) or
        (q == "Origin" and p == (0, 0))
    )]
    for q in [
        "Quadrant I", "Quadrant II",
        "Quadrant III", "Quadrant IV", "Origin"
    ]
}

print(quadrants)