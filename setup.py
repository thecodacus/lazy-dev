from setuptools import find_packages, setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="lazydev",
    version='0.0.2',
    description='AI developer for lazy programmer',
    packages=find_packages(),
    install_requires=requirements,
    author='Anirban Kat',
    author_email='thecodacus@gmail.com',
    entry_points={
        'console_scripts': [
            'lazydev = lazydev:run',
        ],
    },
    # other relevant information

    # # You can specify package data if needed
    # package_data={
    #     'lazydev': ['*.txt', '*.csv'],  # Include any additional files here
    # },

    # # You can also specify additional non-package data files
    # data_files=[
    #     ('config', ['config.ini']),
    # ],

)