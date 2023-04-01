import setuptools

with open('./README.md', 'r') as readme_file:
    readme = readme_file.read()

with open('./requirements.txt') as requirements_file:
    requirements = [line.strip() for line in requirements_file.readlines()]

setuptools.setup(
    name='aenc',
    version='0.0.2',
    author="The Project Contributors",
    description='Autoencoders for Financial Markets (AENC)',
    long_description=readme,
    long_description_content_type='text/markdown',
    install_requires=requirements,
    url="https://github.com/compatibl/aenc",
    project_urls={
        'Source Code': 'https://github.com/compatibl/aenc',
    },
    packages=setuptools.find_packages(include=('aenc', 'aenc.*'), exclude=['tests', 'tests.*']),
    classifiers=[
        # Alpha - will attempt to avoid breaking changes but they remain possible
        'Development Status :: 3 - Alpha',

        # Audience and topic
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Financial and Insurance Industry',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',

        # License
        'License :: OSI Approved :: Apache Software License',

        # Runs on Python 3.9 and later releases
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',

        # Operating system
        'Operating System :: OS Independent',
    ],
)
