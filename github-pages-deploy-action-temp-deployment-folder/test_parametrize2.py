import pytest

def test_calc_square_1():
    result=pow(5, 2)
    assert result == 25
def test_calc_square_2():
    result=pow(9, 2)
    assert result == 81
def test_calc_square_3():
    result=pow(10, 2)
    assert result == 100

@pytest.mark.parametrize("test_input, expected",[
        (5, 25),
        (9, 81),
        (10, 100)
                                                  ])
def test_calc_square(test_input, expected):
    result=pow(test_input, 2)
    assert result == expected

list_tuples = [
    (5, 25,'test_1'),
    (9,80,'test_2'),
    (10,100,'test_3'),
]

# ! parametrize
@pytest.mark.parametrize("test_input,expected,test_report",list_tuples)
def test_login_page2(test_input,expected,test_report):
    result=pow(test_input, 2)
    assert result == expected , "results are not matching"