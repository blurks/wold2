from setuptools import setup, find_packages


setup(
    name='wold2',
    version='0.0',
    description='wold',
    long_description='',
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
    author='Robert Forkel, MPI SHH',
    author_email='forkel@shh.mpg.de',
    url='http://wold.clld.org',
    keywords='web wsgi bfg pylons pyramid',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite='wold2',
    install_requires=[
        'clld>=3.2.0',
        'clldmpg>=2.0.0',
    ],
    tests_require=[
        'WebTest >= 1.3.1',  # py3 compat
        'mock>=1.0',
    ],
    entry_points="""\
      [paste.app_factory]
      main = wold2:main
      [console_scripts]
      initialize_wold_db = wold2.scripts.initializedb:main
      """)
