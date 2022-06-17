import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='gctools',  
     version='0.0.1',
     provides=['gctools'],
     author="Géry Casiez",
     author_email="gery.casiez@univ-lille.fr",
     description="Tools provided by GC.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://gitlab.univ-lille.fr/gery.casiez/gctools",
     packages=setuptools.find_packages(),
     install_requires=[ ],
     licence="MIT License",
     platforms=['any'],

     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
         "License :: OSI Approved :: GNU General Public License v2 (GPLv2)"
     ],

 )