from distutils.core import setup
setup(
  name = 'pycoinpit',
  packages = ['pycoinpit'], # this must be the same as the name above
  install_requires=[ "pybitcointools", "pyelliptic", "requests" ],
  version = '0.2',
  description = 'Coinpit Python Client',
  author = 'Bharath Rao',
  author_email = 'Bharath.Rao@gmail.com',
  url = 'https://github.com/coinpit/pycoinpit', # use the URL to the github repo
  download_url = 'https://github.com/coinpit/pycoinpit/tarball/0.2',
  keywords = ['coinpit', 'trading', 'python'],
  classifiers = [],
)
