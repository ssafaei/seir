import setuptools

setuptools.setup(
    author='Alan Garny',
    author_email='a.garny@auckland.ac.nz',
    description='OpenCOR-based Python script to model Covid-19 using the SEIR model',
    entry_points={
        'scripts': ['seir=src/main.py'],
    },
    license='Apache 2.0',
    name='seir',
    packages=setuptools.find_packages(),
    url='https://github.com/ABI-Covid-19/seir',
    version='0.1.0',
)
