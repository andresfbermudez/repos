

def test_find_y_value():

    from ExerciseFeb3 import find_y_value
    #Arrange
    slope = 10
    intercept = 1
    x_input = 5
    expected = slope*x_input + intercept
    #Act
    answer = find_y_value(x_input)
    #Assert
    assert answer == expected


def test_find_slope():
    from ExerciseFeb3 import find_slope
    #Arrange
    point1 = (2,2)
    point2 = (4,4)
    expected = 1
    #Act
    answer = find_slope((2,2),(4,4))
    #Assert
    assert answer == expected
