Get Started
===========

Install
*******
.. code-block:: bash

    git clone https://github.com/taylorfturner/rescaledranges.git
    cd rescaledranges 
    conda create -n rescaledranges python==3.8
    conda activate rescaledranges
    python setup.py install

*Note*: PyPi and conda forge are not currently supported.

Unit Tests
***********
Unit testing results are written in HTML files to `htmlcov/`. 
Open in preferred browser for futher analysis of "line-level"
coverage and missing lines.

.. code-block:: bash

    pytest --cov=rescaledranges/ --cov-report html


Build Docs
***********

.. code-block:: bash

    cd docs 
    make html
