import os
import re
import datetime

def test(a, b):
    """
    This function adds a and b.

    Args:
        a (int or float): input parameter 1.
        b (int or float): input parameter 2.

    Returns:
        c: sum of a and b.

    """

    # add a +b 
    return a + b

class Fitting(object):
    """TEST class for least square fitting.

    xxxx a  a
    """
    def __init__(self):
        """
        constructor for fitting.
        """
        self.name = 'test'
        self.data = 10
        self.data2 = 'apple'

    def add_data(self):
        """ Add data.

        """
        self.data = self.data + 1
