def calcArea(x_coord,y_coord,n):
    area = 0.0
    j = n-1
    for i in range(n):
        area += (x_coord[j]+x_coord[i])*(y_coord[j]-y_coord[i])
        j = i

    return abs(area/2)

x = [0.5546726167802672,-0.5162996571743341,-0.5497219390243434,0.27037915211245184]
y = [-0.7702470794526389,0.483700342825666,0.45027806097565654,-0.8880052882120844]
print(calcArea(x,y,4))
