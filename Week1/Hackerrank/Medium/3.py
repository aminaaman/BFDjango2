import math

AB = int(input())
BC = int(input())

h = math.sqrt((AB * AB) + (BC * BC))
angle = math.degrees(math.acos(BC / h))

print(str(round(angle)) + "°")