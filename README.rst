.. image:: http://farm5.staticflickr.com/4022/4297831216_ea3ef99461_t.jpg
    :alt: http://www.flickr.com/photos/vj-dipsy/4297831216/
    :align: right
    :target: http://pypi.python.org/pypi/wr

wr (Weighted Random)
==========================

*wr is a weighted random implementation in Python.*

``wr.choice`` can be fed with a mapping (such as dictionaries) containing a returnable (what to return) and a integer representing their respective weight.  
The key can be anything hashable but the weight must be a integer.

Optionally you may feed ``wr.choice`` with a sequence of pairs.

Example
-------
::

    >>> import wr
    
    >>> data = {'cat': 60, 'dog': 30, 'bird': 10}
    >>> animal = wr.choice(data)
    >>> print animal
    cat # well, the cat had a good 60% shot at it.

Installation
-----------------------------

Install wr with ``pip install wr`` or just `download wr.py <http://pypi.python.org/pypi/wr>`_ and place it in your project directory.

License
-------
`BSD <http://www.linfo.org/bsdlicense.html>`_
