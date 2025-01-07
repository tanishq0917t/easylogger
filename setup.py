from setuptools import setup, find_packages

setup(
    name="easylogger",
    version="0.1.0",
    description="EasyLogger is a library which makes logging flexible and easy to use without bothering about log management.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tanishq0917t/easylogger",
    author="Tanishq Rawat",
    author_email="tanishqrawat8@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    packages=find_packages(),
)
