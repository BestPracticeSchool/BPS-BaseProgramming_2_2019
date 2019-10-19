def geometry_features(a = 1, b = 1):
    perimeter = 2 * (a + b)
    square = a * b
    return perimeter, square, square / perimeter
    
for i in range(1, 1000):
    p, _, metrics = geometry_features(i, i)
    print(p, metrics)





