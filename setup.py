from setuptools import setup

setup(
    name='lebara-api',
    version='0.1',
    description='lebara api',
    url='https://github.com/tlan16/lebara-api',
    author='Frank Lan',
    author_email='franklan118@gmail.com',
    license='GPL-3.0',
    packages=[
        'lebara-api',
    ],
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    zip_safe=False,
)
