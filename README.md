# iex-wrapper
In Development


##### Example 1
Collect book of amazon stock
```python
import iexwrapper as iex
amzn_book = iex.stock('amzn', 'book').output
print (amzn_book)
```

##### Example 2
Collet market data
```python
import iexwrapper as iex
mkt = iex.market('').output
print (mkt)
```