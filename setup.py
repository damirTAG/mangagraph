from setuptools import setup, find_packages


LIB_NAME = 'mangagraph'

VERSION = '0.0.2.post4'

setup(
    name=LIB_NAME,
    version=VERSION,
    description='Async manga parser-converter from mangalib to telegraph pages',
    url='https://github.com/damirTAG/mangagraph',
    author='damirTAG',
    author_email='damirtagilbayev17@gmail.com',
    packages=find_packages(),
    install_requires=[
        'aiohttp',
        'sqlalchemy',
        'telegraph',
        'asyncio'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    keywords=[
        'mangalib',
        'mangalib-parser',
        'manga',
        'telegraph'
    ],
    python_requires='>=3.7',
    include_package_data=False
)