import pytest


@pytest.mark.dependency(
    depends=["tests/dependency/test_one.py::test_one"], scope="session")
def test_two():
    print("Two")
