from setuptools import setup, find_packages

setup(
    name="dongfeng_base",
    version="0.0.1",
    packages=find_packages(where=".", exclude=("tests",), include=("*",)),
    install_requires=("aenum", "celery[redis]", "psutil"),
    url="",
    license="",
    author="40huo",
    author_email="git@40huo.cn",
    description="",
)
