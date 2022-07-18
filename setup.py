import setuptools

setuptools.setup(
    name="pysnoutboops",
    version="0.0.1",
    author="Leo Liu",
    author_email="liuleo@stanford.edu",
    description="Play neuron spikes out loud (WIP)",
    packages=setuptools.find_packages(),
    install_requires=[
          'numpy',
          'pysinewave',
    ],
    python_requires='>=3.6',
)
