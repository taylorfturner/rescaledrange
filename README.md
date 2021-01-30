# rescaledranges
![logo](logo.jpg?raw=true "Rescaled Ranges")

## Overview 
The rescaled range of time series is calculated from dividing the range of its mean adjusted cumulative deviate series (see the Calculation section below) by the standard deviation of the time series itself. For example, consider a time series {1,3,1,0,2,5}, which has a mean m = 2 and standard deviation S = 1.79. Subtracting m from each value of the series gives mean adjusted series {-1,1,-1,-2,0,3}. To calculate cumulative deviate series we take the first value -1, then sum of the first two values -1+1=0, then sum of the first three values and so on to get {-1,0,-1,-3,-3,0}, range of which is R = 3, so the rescaled range is R/S = 1.68. [Wikipedia](https://en.wikipedia.org/wiki/Rescaled_range)

This package is built using Prefect, Dask, and Pandas. See [here]() for documentation.

## Installation
```shell
git clone https://github.com/taylorfturner/rescaledranges.git
cd rescaledranges
conda create -n rescaledranges
python setup.py install
```

## Example(s)

### Code Example
```python
python main.py
```

### Underlying Math Example
Google Sheets example using historical SPY closing prices see [here](https://docs.google.com/spreadsheets/d/1m0QqMo1E06Z1qbD-f6f8_-NZHYHQfwiHyiS9w27y0H4/edit#gid=1966444318)


## Additional Reading
- [Amity Journal of Commerce and Financial Review](https://amity.edu/UserFiles/ajcfr/4d1cHurst%20Exponent%20as%20an%20Indicator%20of%20Market%20Efficiency%20An%20empirical%20study%20of%20the%20stock%20prices%20of%20Amazon.com.pdf)
- [Hurst and Rescaled Range Analysis](http://sfb649.wiwi.hu-berlin.de/fedc_homepage/xplore/tutorials/xfghtmlnode99.html)
- [The Fractal Indicator](https://medium.com/swlh/the-fractal-indicator-detecting-tops-bottoms-in-markets-1d8aac0269e8)
- [Wiki Rescaled Range](https://en.wikipedia.org/wiki/Rescaled_range)
- [The Misbehavior of Markets: A Fractal View of Financial Turbulence](https://www.amazon.com/Misbehavior-Markets-Fractal-Financial-Turbulence/dp/0465043577/ref=sr_1_2?dchild=1&keywords=mandelbrot&qid=1611854283&sr=8-2)