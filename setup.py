import setuptools

setuptools.setup(
    name="demo-package",
    version="0.0.1",
    author="DigiNova",
    author_email='info@diginova.com.tr',
    description="Demo Package",
    url='https://github.com/novavision-ai/demo-package',
    license='MIT',
    install_requires=['pydantic', 'opencv-python-headless'],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    packages=[
        'novavision.demo_package',
        'novavision.demo_package.executors',
        'novavision.demo_package.models',
        'novavision.demo_package.utils'
    ],
    package_dir={'novavision.demo_package': 'src'},
    python_requires=">=3.8"
)
