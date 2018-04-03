from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='ds4biz',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='',
      author_email='',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'cycler==0.10.0'
	,'dill==0.2.7.1'
	,'et-xmlfile==1.0.1'
	,'html2text==2018.1.9'
	,'jdcal==1.3'
	,'matplotlib==2.0.2'
	,'nameparser==0.5.6'
	,'nltk==3.2.4'
	,'numpy==1.14.0'
	,'openpyxl==2.5.0'
	,'pandas==0.22.0'
	,'pymongo==3.5.1'
	,'pyparsing==2.2.0'
	,'python-dateutil==2.6.1'
	,'pytz==2017.3'
	,'scikit-learn==0.19.0'
	,'scipy==0.18.1'
	,'singleton-decorator==1.0.0'
	,'six==1.11.0'
	,'sklearn==0.0'
	,'tqdm==4.19.6'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
