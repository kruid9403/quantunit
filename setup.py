from setuptools import setup, find_packages

setup(
    name="quantunit",
    version="0.1.0",
    description="Unit testing framework for quantum programs",
    packages=find_packages(),
    install_requires=[
        "qiskit>=0.46"
    ],
    python_requires=">=3.8",
)