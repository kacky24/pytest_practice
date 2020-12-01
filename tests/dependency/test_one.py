import pytest


@pytest.mark.dependency(scope="session")
def test_one():
    print("One")


@pytest.mark.dependency(denpends=['test_one'], scope="session")
def test_one_point_five():
    print("One point five")
