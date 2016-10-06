import unittest
import time
from bubble import *

# Load related files
with open('testset/smallList.txt', 'r') as f:
    SMALL_COLLECTION = [int(line.rstrip()) for line in f]

with open('testset/smallListResult.txt', 'r') as f:
    SMALL_COLLECTION_RESULT = [int(line.rstrip()) for line in f]


class TestBubbleSort(unittest.TestCase):

    def test_swap(self):
        a = [1,2,3]
        self.assertEqual(swap(0,1, a), [2,1,3])

    def test_sort_correctness(self):
        a = [3,5,2,4,8,7,10]

        start_time = time.time()
        result = sort(a)
        print("--- test_sort_correctness: %s seconds ---" % (time.time() - start_time))

        self.assertEqual(result, [2,3,4,5,7,8,10])

    def test_sort_small_collection(self):
        start_time = time.time()
        result = sort(SMALL_COLLECTION)
        print("--- test_sort_small_collection: %s seconds ---" % (time.time() - start_time))
        self.assertEqual(result, SMALL_COLLECTION_RESULT)
        


class TestSelectionSort(unittest.TestCase):
    def test(self):
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main(verbosity=2)