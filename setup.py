from setuptools import setup, find_packages

setup(
    name='plothic',
    version='0.4.8',
    author='Zijie Jiang',
    author_email='jzjlab@163.com',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.21.2',
        'pandas>=2.2.3',
        'matplotlib>=3.9.2',
        'hic-straw>=1.3.1',
        'scikit-learn>=1.5.2',
        'scipy>=1.14.1',
        'six>=1.16.0',
    ],
    description='Plot whole genome contact heatmap',
    url='https://github.com/Jwindler/PlotHiC',
    license='G',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GPL-3.0 License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    entry_points={
        'console_scripts': [
            'plothic=plothic.cli:main',
        ],
    },
)
