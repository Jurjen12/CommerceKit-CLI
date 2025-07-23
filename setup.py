from setuptools import setup

setup(
    name="commercekit",
    version="0.1.0",
    packages=["commercekit"],
    install_requires=[
        "typer",
    ],
    entry_points={
        "console_scripts": [
            "instijl=commercekit.main:app",  # This creates the 'instijl' CLI command that runs app() in main.py
        ],
    },
)
