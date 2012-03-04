from setuptools import setup
from setuptools import find_packages

setup(
    name='mental_space',
    version='0.1',
    author='Kristoffer Snabb',
    url='https://github.com/geonition/mental_space',
    packages=find_packages(),
    include_package_data=True,
    package_data = {
        "mental_space": [
        ],
    },
    zip_safe=False,
    install_requires=['django']
)
