# -*- coding: utf-8 -*-
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: type1 or type2",
    )
    parser.addoption(
        "--cmdopt1", action="store", default="type1", help="my option: type1 or type2",
    )

@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")

@pytest.fixture
def cmdopt1(request):
    return request.config.getoption("--cmdopt1")