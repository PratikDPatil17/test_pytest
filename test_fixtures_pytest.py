import pytest

@pytest.fixture()
def setUp():
    print()
    print("setUp Method")
    

def test_methodA(setUp):
    print("From method A")

def test_methodB(setUp):
    print("From method B")

