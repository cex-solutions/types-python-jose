# types-python-jose

This is a package containing type annotations
for [python-jose](https://pypi.org/project/python-jose/).

### Installing:

Simply run the following in the environment in which you want to install this package:

```shell
# install types-python-jose
$ python -m pip install types-python-jose
```

or add it to your requirements file.

### Developing

This is a partial stub package, only covering a part of the functions and objects available in `python-jose`.
Contributions (both in adding stubs for more functions, or keeping up to date with `python-jose` itself) are
welcome.

All the formatting is done using [pre-commit](https://pre-commit.com/). To use this, run the following:

```shell
# install pre-commit
$ python -m pip install pre-commit

# Set up the hooks (so pre-commit automatically runs when you do a commit)
$ cd root/directory/of/the/pulled/repository
$ pre-commit install

# This will run automatically whenever a commit is created
# To run it manually, use:
$ pre-commit run --all-files
```
