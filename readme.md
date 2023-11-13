
### Python Study

Study notes based on the course Python Essentials 2 (Aligned with PCAP-31-03) https://edube.org/study


## pip
Python install packages


pip --version
pip help install
pip show pandas
pip install --user pygame
pip install -U pandas # update package
pip install package==version
pip uninstall package

## Virtual environment

Use a virtual environment to manage the dependencies for your project, both in development and in production.

What problem does a virtual environment solve? The more Python projects you have, the more likely it is that you need to work with different versions of Python libraries, or even Python itself. Newer versions of libraries for one project can break compatibility in another project.

Virtual environments are independent groups of Python libraries, one for each project. Packages installed for one project will not affect other projects or the operating system’s packages.

Python comes bundled with the venv module to create virtual environments.


Create an environment 

`$ python3 -m venv .venv`

Activate the virtual environment

`$ . .venv/bin/activate`
