import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dynamic_dcs",
    python_requires=">=3.9",
    version="0.0.1dev",
    author="Rhys Deimel",
    author_email="deimelr@hotmail.com",
    description="Dynamic mission generator for DCS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages("src", exclude=["tests"]),
    package_dir={"": "src"},
    test_suite="tests",
    install_requires=[],
)
