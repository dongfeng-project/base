from setuptools import setup, find_packages
from pip.req import parse_requirements

setup(
    name="dongfeng_base",
    version="0.0.1",
    packages=find_packages(where=".", exclude=("tests",), include=("*",)),
    install_requires=parse_requirements("requirements.txt"),
    url="",
    license="",
    author="40huo",
    author_email="git@40huo.cn",
    description="",
)
