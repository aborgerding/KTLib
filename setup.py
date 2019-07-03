import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kissInstitute",
    version="0.0.1",
    author="KISS Institute for Practical Robotics",
    author_email="info@kipr.org",
    description="Python Method Wrapper for use with Tello EDU minidrone",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aborgerding/KTLib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
