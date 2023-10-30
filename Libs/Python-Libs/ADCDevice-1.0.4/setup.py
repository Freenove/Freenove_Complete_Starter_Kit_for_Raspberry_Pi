
#from setuptools import setup,find_packages
from distutils.core import setup
from setuptools import setup, find_packages


setup(
    name = "ADCDevice",
    version = "V1.0.4",
    description = "Freenove ADC Module python library.",
    author = "Freenove",
    url = "http://www.freenove.com",
    license = " ",
    packages = find_packages('src'),
    package_dir = {'':'src'},
    include_package_data = True,
    
    )
