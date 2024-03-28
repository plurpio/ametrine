from setuptools import setup, find_packages

setup(
    name="ametrine",
    version="0a",
    author="Plurpio",
    author_email="148961679+plurpio@users.noreply.github.com",
    description="A CLI application to switch configuration files on the fly!",
    long_description="bob",
    long_description_content_type="text/markdown",
    url="https://github.com/plurpio/ametrine",
    packages=find_packages() + ['ametrine.defaultFiles'],
    package_data={'ametrine': ['defaultFiles/*']},
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        ametrine=ametrine.__main__:cli
    ''',
)
