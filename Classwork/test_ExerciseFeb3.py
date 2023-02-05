def test_find_y_value(slope,intercept,x_input):
    from ExerciseFeb3 import find_y_value
    #Arrange
    expected = slope*x_input + intercept
    #Act
    answer = find_y_value(x_input)
    #Assert
    assert answer == expected


