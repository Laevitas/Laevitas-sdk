from setuptools import setup


with open("README.md") as readme:
    README = readme.read()
setup(
    name='SDK-Laevitas',
    version='1.0',
    packages=['Laevitas'],
    url='https://github.com/Elyesbdakhlia',
    download_url='https://github.com/Elyesbdakhlia/API-SDK/archive/refs/tags/test-1.4.2.tar.gz',
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
