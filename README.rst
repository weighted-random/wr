wr (Weighted Random)
==========================

*wr is a weighted random implementation in Python.*

``wr.get`` can be fed both mappings (such as dictionaries) and sequences of pairs containing what to return and a integer representing their respective weight. It returns a the key of in case of mappings based on the weights defined in the key's corresponding value.

The key can be anything hashable but the weight must be a integer.

Optionally you may feed ``wr.get`` with a sequence of pairs.

Structures
----------
::

    {something_to_return: weight, something_else_to_return: weight}
    # Or as a sequence:
    [[(something_to_return), (weight)], [(something_else_to_return), (weight)]]

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

Install wr with ``pip install wr`` or just `download wr.py <http://pypi.python.org/pypi/wr>`_ and place it in your project directory.

License
-------
`GNU Lesser General Public License <http://www.gnu.org/copyleft/lesser.html>`_
