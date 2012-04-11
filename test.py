from wrr import wrr

def test_wrr(data, times=10000):
    import collections
    testcase = []
    for x in xrange(times):
        testcase.append(wrr(data))
    counter=collections.Counter(testcase)
    print counter.most_common(4)

test_wrr({3: 50, 34: 50})
