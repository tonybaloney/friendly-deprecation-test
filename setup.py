from distutils.core import setup


setup(
    name='friendly-deprecation-test',
    version='1.3.0',
    description='Testing phasing out Python runtimes',
    author='Anthony Shaw',
    author_email='anthonyshaw@apache.org',
    url='https://github.com/tonybaloney/friendly-deprecation-test',
    packages=['friends'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, <4',
)
