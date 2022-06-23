import pytest

@pytest.mark.usefixtures('Setup', 'OneTimeSetup')
class Test_Demo():
    def test_methodA(self):
        print('Method A')

    def test_methodB(self):
        print('Method B')
