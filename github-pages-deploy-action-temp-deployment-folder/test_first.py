from sys import flags
from numpy import number
import pytest
import sys

def test_1():
    x = 20
    y = 20
    assert x==y

def test_2():
    x = 20
    y = 20
    # added one extra output, so that both numbers are equal or not...
    assert x==y, "Both number are not equal"

def test_api():
    print('api testing')
    
# pytest -rA
# will give the info of all the test cases...


# ! junit xml
# pytest -rA --junitxml="report.xml"
# ! html
# to generate html, make sure to install pytest-html, 
# pip install pytest-html
# will also html output
# pytest --html=MyHTMLReport.html


# ! allure report
# we can also integrate Allure report.


# flags
# pytest - h

# ! MARKERS

@pytest.mark.skip
def test_login():
    print("Login done")

@pytest.mark.skipif(sys.version_info<(3,10),reason="python version not supported")
def test_login_part2():
    print("Login done")

@pytest.mark.regression
def test_addProduct():
    print("add product")

@pytest.mark.smoke
def test_logout():
    print("Logout done")

@pytest.mark.xfail()
def test_add_to_cart():
    print("added to the cart")
# pytest -m "marker_name"
# pytest -m "marker_1 or marker_2"
# pytest -m "marker_1 and marker_2"

# its not working... 
# now every thing is working lets see what we can develop with all these 


# ! parametrize
@pytest.mark.parametrize("username,password",[
    ("selenium","webdriver"),
    ("rahul","keshav"),
    ("radha","madhav"),
    ("krishna","balram"),
])
def test_login_page(username,password):
    assert username==password

# ! Fixtures 1:09:53
# 1:09:53
"""
    Precondition
        Setup,Connection,API.
    _____________________

    Test1
    Test2
    Assertion3

    post conditions
        clean the logs, delete some files.
    ____________________

"""

@pytest.fixture 
def setup():
    print("start the browser")

    yield
    print("close the browser")

@pytest.mark.fixture_test
def test_fixture_1(setup):
    print('run test 1')

@pytest.mark.fixture_test
def test_fixture_2(setup):
    print('run test 2')

@pytest.mark.fixture_test
def test_fixture_3(setup):
    print('run test 3')


#! run tests in parallel mode
# we will use pytest distributed
# pip install pytest-xdist 

# we just have add this flag "-n 3"
# -n means number
# 3 means number of processors

