import setuptools


with open('README.md', 'r') as file:
    long_description = file.read()

setuptools.setup(
    name='zhdate',
    version='0.1',
    author="PandaWithBeard",
    author_email="9861649@qq.com",
    description="A pachage to convert Chinese Lunar Calendar to datetime",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/CutePandaSh/zhdate',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
)

    