.. rescaledranges documentation master file, created by
   sphinx-quickstart on Thu Jan 28 16:50:12 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the `rescaledranges` docs!
=====================================

.. toctree::
   getstarted.rst
   examples.rst
   rescaledranges.rst


Summary
*******
``rescaledranges`` is a python package built to analyze any time series that ticks. Specifically in mind when this was built -- equities,
fixed income, commodities, and currency time series. The package only supports pulling ticker data from the Yahoo API and `.csv` files
provided by the user on their same machine where the code is executed.

The core of this code is nothing new -- just delivered through a new medium (i.e. python). H. E. Hurst developed this method of 
time series analysis and framework for understanding the world in the 1950s. Although all but eulogized by Mandelbrot, 
Hurst's contemporaries were not nearly as admiring. Hurst was an anachronism in his field of engineering. 
He was mocked by consensus for his research and assertions. 

I highly recommend further reading about the underlying framework.

- `Wiki Rescaled Range <https://en.wikipedia.org/wiki/Rescaled_range>`_
- `The Misbehavior of Markets: A Fractal View of Financial Turbulence <https://www.amazon.com/Misbehavior-Markets-Fractal-Financial-Turbulence/dp/0465043577/ref=sr_1_2?dchild=1&keywords=mandelbrot&qid=1611854283&sr=8-2>`_
- `Misbehavior of Markets by Benoit Mandelbrot <https://www.amazon.com/Misbehavior-Markets-Fractal-Financial-Turbulence/dp/0465043577/ref=sr_1_1?dchild=1&keywords=misbehavior+of+markets&qid=1623442660&sr=8-1>`_
- `The Volatility Surface by Jim Gatheral <https://www.amazon.com/Volatility-Surface-Practitioners-Guide/dp/0471792519/ref=sr_1_1?dchild=1&keywords=volatility+surface&qid=1623442740&sr=8-1>`_
- `Amity Journal of Commerce and Financial Review <https://amity.edu/UserFiles/ajcfr/4d1cHurst%20Exponent%20as%20an%20Indicator%20of%20Market%20Efficiency%20An%20empirical%20study%20of%20the%20stock%20prices%20of%20Amazon.com.pdf>`_
- `Hurst and Rescaled Range Analysis <http://sfb649.wiwi.hu-berlin.de/fedc_homepage/xplore/tutorials/xfghtmlnode99.html>`_
- `The Fractal Indicator <https://medium.com/swlh/the-fractal-indicator-detecting-tops-bottoms-in-markets-1d8aac0269e8>`_

Here's to you, Mr. Hurst |:goat:|

.. image:: https://media.giphy.com/media/I4wGMXoi2kMDe/giphy.gif
   :width: 400

Caveats and Contribution Model
******************************
- This package is still in its infancy and not fully tested in the real-world. 
- If you would like to directly contribute code, reach out to `me <https://www.taylorfturner.com>`_ and let's talk about your ideas!
- See something you would like added, please `add an issue <https://github.com/taylorfturner/rescaledranges/issues>`_ on the repo!

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
