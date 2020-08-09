import io
import re
from setuptools import setup, find_packages

_version_re = re.compile(r"__version__\s+=\s+(.*)")

with io.open("mytools/__init__.py", "rt", encoding="utf8") as f :
    version = re.search(r"__version__ = \"(.*?)\"", f.read()).group(1)

requires = [
    "colorful"
]

setuptools.setup(
    name="mytools",
    description="My python tools",
    version=version,
    author="Ryuki Fujita",
    packages=find_packages(),
    install_requires=requires,
    py_modules=["mytools"],
)
