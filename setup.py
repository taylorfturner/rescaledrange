from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="rescaledranges",
    version="0.0.0",
    description="Rescaled Range Analysis",
    author="Taylor F. Turner, IV",
    author_email="taylorfturner@gmail.com",
    license="All Rights Reserved",
    packages=find_packages(),
    include_package_data=True,
    install_requires=required,
    zip_safe=False,
)
