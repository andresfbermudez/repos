def point_finder(point1, point2, x_input):
    slope = find_slope(point1, point2)
    intercept = find_intercept(point1, point2, slope)
    y_value = find_y_value(slope, intercept, x_input)
    return y_value


def find_slope(point1, point2):
    slope = (point2[1] - point1[1])/(point2[0] - point1[0])
    return slope

def find_intercept(point1, point2, slope):
    intercept = point1[1] - slope * point1[0]
    return intercept

def find_y_value(slope, intercept, x_input):
    y_value = slope * x_input + intercept
    return y_value
