from setuptools import setup, find_packages

setup(
    # --- metadata ---
    name='BasicApp',
    version='0.0.1',
    description='',
    url='',
    authors=['Robby Boney',],
    author_email='robbyb@gointerject.com',

    # --- the source code folders ---
    packages=['basicapp'],

    # --- cli scripts that will be installed when cuttlefish is installed ---
    entry_points={
        'console_scripts': [
            'basicapp = basicapp.scripts.launcher:main'
        ]
    },

    # --- project dependancies ---
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    install_requires=[
        'loguru==0.3.2',
        'flask',
        'psutil',
        'requests',
        'pathlib',
        'pytest'
    ]
)
