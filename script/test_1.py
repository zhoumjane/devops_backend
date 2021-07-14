# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, Group
import pytest

# def test_failing():
#     assert (1, 2, 3) == (3, 2, 1)


def test_success():
    assert (1, 2, 3) == (1, 2, 3)

def test_answer(cmdopt, cmdopt1):
    if cmdopt == "type1":
        print("first")
    elif cmdopt == "type2":
        print("second")
    else:
        assert 0
    print(cmdopt)
    print(cmdopt1)

if __name__ == "__main__":
    pytest.main("-s", "test_case1.py")

