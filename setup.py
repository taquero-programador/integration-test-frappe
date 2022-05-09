from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tienda_prueba/__init__.py
from tienda_prueba import __version__ as version

setup(
	name="tienda_prueba",
	version=version,
	description="tienda prueba",
	author="Javier Rangel",
	author_email="jrangel93@proton.me",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
