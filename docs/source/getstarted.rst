Get Started
===========

Github
******
.. code-block:: bash

    git clone https://github.com/taylorfturner/rescaledranges.git
    cd rescaledranges 
    conda create -n rescaledranges python==3.8
    conda activate rescaledranges
    python setup.py install

PyPi
****
Not currently supported and no plans to make publicly available at this in this format.

Conda Forge
***********
Not currently supported and no plans to make publicly available at this in this format.



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


