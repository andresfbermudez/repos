def point_finder((x1,y1),(x2,y2),x_input):
    point1 = (x1,y1)
    point2 = (x2,y2)
    slope = find_slope(point1,point2)
    intercept = find_intercept(point1, point2, slope)
    y_value = find_y_value(slope, intercept,x_input)
    return y_value


def find_slope(point1, point2):
    slope = (point2(2) - point1(2))/(point2(1) - point1(1))
    return slope


