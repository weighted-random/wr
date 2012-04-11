wr (Weighted Random)
==========================

*wr is a weighted random implementation in Python.*

``wrr.get`` returns a key of a passed in dict based on the weights of the keys as their respective values.
``{key: weight}`` The key can be anything hashable including callables but the weight must be a integer.


Example
-------
::

    >>> import wr
    
    >>> data = {'cat': 60, 'dog': 30, 'bird': 10}
    >>> animal = wr.get(data)
    >>> print animal
    cat # well, the cat had a good 60% shot at it.

Installation and Dependencies
-----------------------------

Install wr with ``pip install wr`` or just `download wr.py <http://pypi.python.org/pypi/wrr>`_ and place it in your project directory.

License
-------
`GNU Lesser General Public License <http://www.gnu.org/copyleft/lesser.html>`_
