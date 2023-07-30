from distutils.core import setup

REQUIRES = [
    'requests~=2.31.0',
    'structlog~=23.1.0',
    'curlify~=2.2.1',
    'allure-pytest'
]

setup(
    name='restclient',
    version='0.0.1',
    packages=['restclient'],
    url='https://github.com/vvSSpace/restclient.git',
    license='MIT',
    author='Vyacheslav Sevastyanov',
    author_email='-',
    install_requires=REQUIRES,
    description='restclient with allure and logger'
)
