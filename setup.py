from setuptools import find_packages, setup

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name="lazydev",
    version='0.0.7',
    packages=find_packages(),
    install_requires=[
        "langchain>=0.0.188",
        "openai>=0.27.7"
    ],
    entry_points={
        'console_scripts': [
            'lazydev = lazydev:run',
        ],
    },
    author='Anirban Kat',
    author_email='thecodacus@gmail.com',
    description='AI developer for lazy programmer',
    long_description=readme,  # Assign the contents of README.md to long_description
    # Specify the type of long description
    long_description_content_type='text/markdown',
    url='https://github.com/thecodacus/lazy-dev',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
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
