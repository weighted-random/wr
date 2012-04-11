import sys
try:
    from collections import Counter
except ImportError:
    from counter import Counter
from wrr import wrr

def test_wrr(data, times=10000):
    testcase = []
    for x in range(times):
        testcase.append(wrr(data))
    counter = Counter(testcase)
    print counter.most_common(4)

test_wrr({3: 50, 34: 50})
