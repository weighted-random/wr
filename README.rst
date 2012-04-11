wrr (Weighted Round Robin)
==========================

*wrr is a weighted round robin implementation in Python.*

``wrr.get`` returns a key of a passed in dict based on the weights of the keys as their respective values.
``{key: weight}`` The key can be anything hashable including callables but the weight must be a integer.

Wikipedia: http://en.wikipedia.org/wiki/Weighted_round_robin

Example
-------
::

    >>> import wrr
    
    >>> data = {'cat': 60, 'dog': 30, 'bird': 10}
    >>> animal = wrr.get(data)
    >>> print animal
    cat # well, the cat had a good 60% shot at it.

Installation and Dependencies
-----------------------------

Install wrr with ``pip install wrr`` or just `download wrr.py <http://pypi.python.org/pypi/wrr>`_ and place it in your project directory.

License
-------
`GNU Lesser General Public License <http://www.gnu.org/copyleft/lesser.html>`_