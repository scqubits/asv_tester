from asv_tester import bar
import sys

sys.path.append('../../')

def test_slow_function():
    bar.slow_function()


def test_hello():
    bar.hello()
