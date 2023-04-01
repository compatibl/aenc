import setuptools

with open('./README.md', 'r') as readme_file:
    readme = readme_file.read()

with open('./requirements.txt') as requirements_file:
    requirements = [line.strip() for line in requirements_file.readlines()]

setuptools.setup(
    name="aenc",
    version="0.0.1",
    author="The Project Contributors",
    description="Specialized autoencoders for dimension reduction in quant models of financial markets (AENC)",
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    url="https://github.com/compatibl/aenc",
    packages=setuptools.find_packages(include=('aenc', 'aenc.*'), exclude=['tests', 'tests.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
