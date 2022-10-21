import math
def closest_pair(points):
    if(len(points) <= 1):
        raise Exception("Точек нет или она одна.")
    else:
        minLeng = 999999999999999999
        pair = []
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                leng = math.sqrt((points[i]['x'] - points[j]['x'])**2 + (points[i]['y'] - points[j]['y'])**2)
                if (leng < minLeng):
                    minLeng = leng
                    pair = [points[i], points[j]]
        return sorted(pair, key=lambda d: d['x'])

p = [{'x': -5, 'y': 6}, {'x': 1, 'y': 2}, {'x': 4, 'y': -2}, {'x': -9, 'y': 0},
        {'x': -1, 'y': -2}, {'x': 0, 'y': 7}, {'x': 2, 'y': -1}, {'x': -3, 'y': 1}]
print(closest_pair(p))
