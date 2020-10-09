import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="geneticml-vphadnis", # Replace with your own username
    version="0.0.1",
    author="Vinay Phadnis",
    author_email="phadnisvinay30@gmail.com",
    description="A genetic optimisation package to perform hyper parameter tuning for Machine Learning workloads",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vinayphadnis/geneticml",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)