import math

def dist(points):
    leng = math.sqrt((points[0]['x'] - points[1]['x'])**2 + (points[0]['y'] - points[1]['y'])**2)
    return leng

def closest_pair_between(PLeft, PRight, d):
    pair = [{'x': -999999*2, 'y': 999999*2}, {'x': 999999*2, 'y': -9999999*2}]
    Xm = (PLeft[len(PLeft)-1]['x'] + PRight[0]['x'])/2
    PStripe = []
    for i in range(len(PLeft)):
        if abs(PLeft[i]['x']-Xm) <= d:
            PStripe.append(PLeft[i])
    for i in range(len(PRight)):
        if abs(PRight[i]['x']-Xm) <= d:
            PStripe.append(PRight[i])
    if(len(PStripe) <= 1):
        return pair
    PStripe = sorted(PStripe, key=lambda d: d['y'])
    minLeng = 999999999999999999
    for i in range(len(PStripe) - 1):
        for j in range(i + 1, len(PStripe)):
            if (abs(PStripe[i]['y'] - PStripe[j]['y'])) < d:
                leng = math.sqrt((PStripe[i]['x'] - PStripe[j]['x'])**2 + (PStripe[i]['y'] - PStripe[j]['y'])**2)
                if (leng < minLeng):
                    minLeng = leng
                    pair = [PStripe[i], PStripe[j]]
            else:
                break
    return pair

def closest_pair(points):
    if(len(points) <= 1):
        raise Exception("Точек нет или она одна.")
    if (len(points) <= 3):
        minLeng = 999999999999999999
        pair = []
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                leng = math.sqrt(
                    (points[i]['x'] - points[j]['x'])**2 + (points[i]['y'] - points[j]['y'])**2)
                if (leng < minLeng):
                    minLeng = leng
                    pair = [points[i], points[j]]
        return pair

    points = sorted(points, key=lambda d: d['x'])
    PLeft = points[:(len(points)//2)]
    PRight = points[(len(points)//2):]

    pl = closest_pair(PLeft)
    pr = closest_pair(PRight)
    d = min(dist(pl), dist(pr))
    pb = closest_pair_between(PLeft, PRight, d)

    a = [pl, pr, pb]
    m = 99999999999999999
    for i in range(len(a)):
        if dist(a[i]) < m:
            m = dist(a[i])
            mpair = a[i]
    return sorted(mpair, key=lambda d: d['x'])
