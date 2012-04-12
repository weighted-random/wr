import sys
import unittest
try:
    from collections import Counter
except ImportError:
    from counter import Counter

sys.path.append('../') # Yeah... well... The price you have to pay.
import wr


class WRRTestCase(unittest.TestCase):

    def test_dict(self):
        times = 10000
        data = {'cat': 60, 'dog': 30, 'bird': 10}
        testcase = []
        for _ in range(times):
            testcase.append(wr.choice(data))
        counter = Counter(testcase)
        result =  dict(counter.most_common(3))
        
        self.assertTrue(result['cat'] > result['dog'])
        self.assertTrue(result['cat'] > result['bird'])
        self.assertTrue(result['dog'] < result['cat'])
        self.assertTrue(result['dog'] > result['bird'])
        self.assertTrue(result['bird'] < result['dog'])
        self.assertTrue(result['bird'] < result['cat'])

    def test_tuple(self):
        times = 10000
        data = [(('cat'), (60)), (('dog'), (30)), (('bird'), (10))]
        testcase = []
        for _ in range(times):
            testcase.append(wr.choice(data))
        counter = Counter(testcase)
        result =  dict(counter.most_common(3))

        self.assertTrue(result['cat'] > result['dog'])
        self.assertTrue(result['cat'] > result['bird'])
        self.assertTrue(result['dog'] < result['cat'])
        self.assertTrue(result['dog'] > result['bird'])
        self.assertTrue(result['bird'] < result['dog'])
        self.assertTrue(result['bird'] < result['cat'])

if __name__ == "__main__":
    unittest.main()
