from src.math_operation import add,sub

def test_add(a,b):
    assert(2,3)==5
    assert(7,2)==9
    assert(0,0)==0
    assert(-2,3)==1
    assert(2,-3)==-1


def test_sub(a,b):
    assert(7,4)==3
    assert(0,0)==0
    assert(-7,4)==-11
    assert(7,-4)==11
    assert(3,4)==-1
