from src.math_operation import add,sub,multiply,divide

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    
def test_sub():
    assert sub(5,3)==2
    assert sub(4,3)==1
    assert sub(3,3)==0
    assert sub(2,3)==-1

def test_multiply():
    assert multiply(2,3)==6
    assert multiply(-1,1)==-1
    assert multiply(0,5)==0

def test_divide():
    assert divide(6,3)==2
    assert divide(5,2)==2.5
    try:
        divide(5,0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"