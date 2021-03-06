# coding: utf-8

"""
    Phonebook API

    RESTful API for Messente phonebook  # noqa: E501

    OpenAPI spec version: 0.0.3
    Contact: messente@messente.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "phonebook-api"
VERSION = "0.2.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Phonebook API",
    author_email="messente@messente.com",
    url="https://messente.com/documentation",
    keywords=["OpenAPI", "OpenAPI-Generator", "Phonebook API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    RESTful API for Messente phonebook  # noqa: E501
    """
)
