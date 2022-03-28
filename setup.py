from setuptools import setup

setup(
    name='NEA-mfahey-7407',
    version='1.0',
    packages=['src', 'src.module0', 'src.module1', 'src.module2'],
    url='https://github.com/MJF2003/NEA',
    license='MIT',
    author='Michael Fahey',
    author_email='michaelfahey42@gmail.com',
    description='Road Sign ID NEA',
    install_requires=[
        "matplotlib >= 3.5.1",
        "numpy >= 1.22.3",
        "tensorflow >= 2.8.0",
        "Pillow >= 9.0.1"
    ]
)
