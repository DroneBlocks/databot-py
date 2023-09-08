# update version num in setup.py

python -m build

# you may need to pip install twine

twine upload --repository testpypi dist/\*
twine upload --skip-existing dist/\*

un: **token**
