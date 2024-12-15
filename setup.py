"""Setup configuration for timezone-adapter package."""

from setuptools import find_packages, setup

setup(
    name="timezone-adapter",
    version="0.1.0",
    description="A class for converting and manipulating datetime objects based on given timezone offset or name.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Miguel Angel Polo Castañeda",
    author_email="miguepoloc@gmail.com",
    url="https://github.com/miguepoloc/timezone-adapter",
    packages=find_packages(),
    install_requires=[
        "pytz>=2022.1",
    ],
    extras_require={
        "dev": [
            "types-pytz",
            "twine",
            "build",
            "mypy",
            "black",
            "isort",
            "flake8",
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    python_requires=">=3.6",
)
