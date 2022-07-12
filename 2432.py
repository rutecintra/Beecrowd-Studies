import math

def binary_search(circles, low, high, distanceSC):
    if high < low:
        return -1
    mid = (low + high) // 2
    if (distanceSC <= circles[mid] and distanceSC > circles[mid-1]) or (distanceSC <= circles[mid] and mid == 0):
        return mid
    elif circles[mid] > distanceSC:
        return binary_search(circles, low, mid - 1, distanceSC)
    else: # circles[mid] < distanceSC
        return binary_search(circles, mid + 1, high, distanceSC)

nCircles, nShots = map(int,input().strip().split(" "))


circles = []

for i in range(nCircles):
	circles.append(float(input()))

points = 0
shotX = []
shotY = []

for i in range(nShots):
	x, y = map(int,input().strip().split(" "))
	shotX.append(x)
	shotY.append(y)

for i in range(nShots):
	distanceSC = float(math.sqrt((shotX[i]**2) + (shotY[i]**2)))
	result = binary_search(circles, 0, len(circles)-1, distanceSC)
	if(result >= 0):
		points += nCircles - result
	# for j in range(nCircles):
	#	if distanceSC <= circles[j]:
	#		points += nCircles - j
	#		break

print(points)