from grade import get_grade

def test_a_grade():
    assert get_grade(85) == "A"

def test_b_grade():
    assert get_grade(72) == "B"

def test_c_grade():
    assert get_grade(65) == "C"

def test_f_grade():
    assert get_grade(30) == "F"