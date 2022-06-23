import pytest

@pytest.fixture()
def Setup():
    print('Setup')
    yield
    print('Clear')


@pytest.fixture(scope='module')
def OneTimeSetup():
    print('One Time Fixture Setup')
    yield
    print('One Time Fixture Clear')
