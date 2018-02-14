from setuptools import setup

setup(
    name='lebara-api',
    version='0.3.1',
    description='lebara api',
    url='https://github.com/tlan16/lebara-api',
    author='Frank Lan',
    author_email='franklan118@gmail.com',
    license='GPL-3.0',
    packages=[
        'lebara_api',
    ],
    install_requires=[
        'requests',
        'beautifulsoup4',
        'tabulate',
    ],
    test_suite='nose.collector',
    tests_require=[
        'nose',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': ['lebara-api=lebara_api.command_line:main'],
    },
    zip_safe=False,
)
