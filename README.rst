wrr (Weighted Round Robin)
==========================

wrr is a weighted round robin implementation in Python.

Wikipedia: http://en.wikipedia.org/wiki/Weighted_round_robin

Installation and Dependencies
-----------------------------

Install wrr with ``pip install wrr`` or just `download wrr.py <http://pypi.python.org/pypi/wrr>`_ and place it in your project directory. There are no (hard) dependencies other than the Python Standard Library.

Example
-------
::

    import wrr
    
    data = {'cat': 60, 'dog': 30, 'bird': 10}
    animal = wrr.get(data)
