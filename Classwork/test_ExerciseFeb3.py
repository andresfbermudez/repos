

def test_point_finder():
    from ExerciseFeb3 import point_finder
    #Arrange
    point1 = (1,1)
    point2 = (2,2)
    x_input = 3
    expected = 3
    #Act
    answer = point_finder(point1, point2, x_input)
    #Assert
    assert answer == expected



def test_find_y_value():
    from ExerciseFeb3 import find_y_value
    #Arrange
    slope = 10
    intercept = 1
    x_input = 5
    expected = slope*x_input + intercept
    #Act
    answer = find_y_value(slope, intercept, x_input)
    #Assert
    assert answer == expected


def test_find_slope():
    from ExerciseFeb3 import find_slope
    #Arrange
    point1 = (2, 2)
    point2 = (4, 4)
    expected = 1
    #Act
    answer = find_slope((2, 2), (4, 4))
    #Assert
    assert answer == expected

def test_find_intercept():
    from ExerciseFeb3 import find_intercept
    #Arrange
    point1 = (5, 5)
    point2 = (10, 15)
    expected = -5
    #Act
    answer = find_intercept((5, 5), (10, 15), 2)
    #Assert
    assert answer == expected
