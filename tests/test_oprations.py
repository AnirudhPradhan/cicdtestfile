from src.math_operation import add,sub

def test_add():
    assert add(2,3)==5
    assert add(7,2)==9
    assert add(0,0)==0
    assert add(-2,3)==1
    assert add(2,-3)==-1


def test_sub():
    assert sub(7,4)==3
    assert sub(0,0)==0
    assert sub(-7,4)==-11
    assert sub(7,-4)==11
    assert sub(3,4)==-1
