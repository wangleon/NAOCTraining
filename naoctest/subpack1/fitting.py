import os
import re
import datetime

class Fitting(object):
    def __init__(self):
        self.name = 'test'
        self.data = 10
        self.data2 = 'apple'

    def add_data(self):
        self.data = self.data + 1
