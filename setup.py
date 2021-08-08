import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyclesperanto_assistant",
    version="0.1.0",
    author="haesleinhuepf",
    author_email="robert.haase@tu-dresden.de",
    description="Assistant for pyclesperanto scripting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/clEsperanto/pyclesperanto_assistant",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["pyclesperanto_assistant"],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Development Status :: 3 - Alpha",
    ],
)
