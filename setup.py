# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages  # type: ignore
import sys
import requests

sys.path.append("Browser")

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

packages = find_packages(exclude=["utest", "atest"])

package_data = {
    "": ["*"],
    "Browser": [
        "wrapper/index.js",
        "wrapper/package.json",
        "wrapper/package-lock.json",
        "wrapper/static/selector-finder.js",
    ],
}

install_requires = open(os.path.join("Browser", "requirements.txt")).readlines()

# Get last version of robotframework-browser from pypi
package_name = "robotframework-browser"
url = f"https://pypi.org/pypi/{package_name}/json"
response = requests.get(url)

if response.status_code == 200:
    package_info = response.json()
    latest_version = package_info["info"]["version"]
    print(f"Latest version of {package_name} is {latest_version}")
else:
    print(f"Error getting {package_name} version from pypi")
    latest_version = "18"

setup_kwargs = {
    "name": "robotframework-browser-stealth",
    "version": latest_version,
    "description": "Robot Framework Browser library powered by Playwright. Aiming for speed, reliability and visibility.",
    "long_description": long_description,
    "long_description_content_type": "text/markdown",
    "author": "MarketSquare - Robot Framework community",
    "author_email": "mikko.korpela@gmail.com",
    "maintainer": None,
    "maintainer_email": None,
    "url": "https://github.com/ButlerHat/robotframework-browser-stealth/archive/",
    "packages": packages,
    "package_data": package_data,
    "install_requires": install_requires,
    "entry_points": {"console_scripts": ["rfbrowser=Browser.entry:cli"]},
    "python_requires": ">=3.8,<4.0",
    "classifiers": [
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Testing",
        "Framework :: Robot Framework",
        "Framework :: Robot Framework :: Library",
    ],
    "include_package_data": True,
}


setup(**setup_kwargs)
