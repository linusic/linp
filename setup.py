from setuptools import setup


setup(
    name='linp',
    version="0.0.1",
    author="linusic",
    author_email='cython_lin@cklin.top',
    description="python operator for argv",
    url="https://github.com/linusic/linp",   # Github Repositoriy (auto sync stars ...)
    classifiers=[
        'Intended Audience :: Developers',        
        "Environment :: Console",                 
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        "Topic :: Software Development",
        "Topic :: Utilities",
    ],  
    py_modules=["linp"], 
    python_requires='>=3.6',
)
