from setuptools import setup


with open("README.md") as readme:
    README = readme.read()
setup(
    name='SDK-Laevitas',
    version='2.0.0',
    packages=['Laevitas'],
    url='https://github.com/Laevitas/Laevitas-sdk',
    download_url='https://github.com/Laevitas/Laevitas-sdk/archive/refs/tags/v2.1.0.tar.gz',
    license='apache-2.0',
    author='Elyes',
    author_email='elyes@laevitas.ch',
    description='SDK',
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    install_requires=[
                       'requests',
                   ]

)
