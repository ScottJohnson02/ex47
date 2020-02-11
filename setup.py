import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="ex47"
    version="0.0.1",
    author="scott johnson",
    author_email="scottyjohnson002@gmail.com",
    url="https://github.com/scottjohnson02/ex-47",
    description="what does yourproject do?",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
