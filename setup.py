from distutils.core import setup

setup(name = 'NAOCTest',
      version = '1.0',
      description='A test module',
      author = 'He Boliang',
      author_email = 'hebl@gmail.com',
      url = 'http://hebl.lamost.org',
      packages = [
          'naoctest',
          'naoctest/subpack1',
          'naoctest/subpack2',
          ],
    )
