from setuptools import setup, find_packages

    

setup(
    name="atp_tennis_scraper",  # Your package name (must be unique on PyPI)
    version="0.1.2",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
    ],
    author="Semyon Tsyrenov",
    author_email="tsyrenovsemyon@gmail.com",
    description="A Python package for scraping ATP tennis rankings.",
    long_description=open("README.md", encoding="utf-8").read(),

    long_description_content_type="text/markdown",
    url="https://github.com/Semne77/atp_tennis_scraper",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    include_package_data=True,

)