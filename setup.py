import setuptools

setuptools.setup(
        name='check_lines',
        author='iRyukizo',
        author_email='hugo.moreau@epita.fr',
        description='A little script to check lines using ctags',
        license='MIT',
        version='0.3.2',
        scripts=['check_lines'],
        url='https://github.com/iRyukizo/check_lines',
        packages=['checklines'],
        python_requires='>=3.5',
        install_requires=['colorama']
)
