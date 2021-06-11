.. rescaledranges documentation master file, created by
   sphinx-quickstart on Thu Jan 28 16:50:12 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the `rescaledranges` package docs!
======================================================

.. toctree::
   getstarted.rst
   examples.rst
   rescaledranges.rst

Summary
*******
``rescaledranges`` is a python package built to analyze any time series that ticks. Specifically in mind when this was built -- equities,
fixed income, commodities, and currency time series. The package only supports pulling ticker data from the Yahoo API.

The core of this code is nothing new -- just delivered through a new medium. H. E. Hurst developed this method of time series analysis and
framework for understanding the world in the 1950s. Although almost eulogized by Mandelbrot, Hurst's contemporaries were not nearly as admiring.
Hurst was an anachronism in his own field of engineering. He was mocked by senior partners for his findings. 

I highly recommend further reading about the underlying framework.

- `Rescaled Range Wiki <https://en.wikipedia.org/wiki/Rescaled_range>`_
- `Misbehavior of Markets by Benoit Mandelbrot <https://www.amazon.com/Misbehavior-Markets-Fractal-Financial-Turbulence/dp/0465043577/ref=sr_1_1?dchild=1&keywords=misbehavior+of+markets&qid=1623442660&sr=8-1>`_
- `The Volatility Surface by Jim Gatheral <https://www.amazon.com/Volatility-Surface-Practitioners-Guide/dp/0471792519/ref=sr_1_1?dchild=1&keywords=volatility+surface&qid=1623442740&sr=8-1>`_


Data Sources
************
- User-Provided: Users can provide a `.csv` file with their own data
- Yahoo: Using the the yahoo API python package. Interaction is abstracted through a class.

Limitations
***********
- In its infancy
- Needs to be used in "action"

Contribution Model
******************
- If you would like to directly contribute code, please reach out to [me](www.taylorfturner.com)
- See something you would like added, please add an issue on the repo! 

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
