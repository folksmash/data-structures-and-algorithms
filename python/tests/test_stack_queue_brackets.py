from code_challenges.stack_queue_brackets import validate_brackets







def test_validate_bracket1():
    actual= validate_brackets('{}(){}')
    expected= True
    assert actual== expected

def test_validate_bracket2():
    actual= validate_brackets('()[[Extra Str]]')
    expected= True
    assert actual== expected

def test_validate_bracket3():
    actual= validate_brackets('[({}]')
    expected= False
    assert actual== expected

def test_validate_bracket4():
    actual= validate_brackets('{(})')
    expected= False
    assert actual== expected
