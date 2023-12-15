from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

version = "2.3.19"

install_requires = [
    "pymem",
    "psutil"
]

setup(
    name="pywxdump_mini",
    author="xaoyaoo",
    version=version,
    author_email="xaoyaoo@gmail.com",
    description="微信信息获取工具",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xaoyaoo/PyWxDumpMini",
    license='MIT',

    packages=['pywxdump_mini'],
    package_dir={'pywxdump_mini': 'pywxdump_mini'
                 },

    package_data={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6, <4',
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'wxinfo = pywxdump.cli:console_run',
        ],
    },
    setup_requires=['wheel']
)
