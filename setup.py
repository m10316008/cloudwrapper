from setuptools import setup, find_packages
import sys

import cloudwrapper


open_kwds = {}
if sys.version_info > (3,):
    open_kwds['encoding'] = 'utf-8'

with open('README.md', **open_kwds) as f:
    readme = f.read()

install_requires = [
]

extras_requires = {
    'amazon': [
        'boto==2.48.0',
    ],
    'google': [
        'gcloud==0.13.0',
        'gcloud_taskqueue==0.1.2',
        'google-api-python-client==1.5.1',
        'oauth2client==2.0.2',
        'pyyaml==3.11',
        'requests==2.9.1',
    ],
    'gcm3': [
        'google-cloud-monitoring==0.27.0',
        'google-cloud-core==0.27.1',
        'oauth2client==2.0.2',
        'requests==2.18.4'
    ],
    'beanstalkd': [
        'pyyaml==3.11',
        'beanstalkc3==0.4.0',
    ],
    'influxdb': [
        'influxdb==3.0.0',
    ]
}

setup(
    name='cloudwrapper',
    version=cloudwrapper.__version__,
    description="Wrappers around cloud services for Amazon, Google and private cloud",
    long_description=readme,
    classifiers=[],
    keywords='',
    author='Klokan Technologies GmbH',
    author_email='info@klokantech.com',
    maintainer='Martin Mikita',
    maintainer_email='martin.mikita@klokantech.com',
    url='https://github.com/klokantech/cloudwrapper',
    license='LGPL 2.1',
    packages=find_packages(exclude=[]),
    include_package_data=True,
    install_requires=install_requires,
    extras_requires=extras_requires,
)
