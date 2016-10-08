import unittest
import time
from utils import *
from bubble import bubbleSort

# Load related files
with open('testset/smallList.txt', 'r') as f:
    SMALL_COLLECTION = [int(line.rstrip()) for line in f]

with open('testset/smallListResult.txt', 'r') as f:
    SMALL_COLLECTION_RESULT = [int(line.rstrip()) for line in f]

class TestUtils(unittest.TestCase):
    def test_swap(self):
        a = [1,2,3]
        self.assertEqual(swap(0,1, a), [2,1,3])

class TestBubbleSort(unittest.TestCase):
    def test_bubbleSort_correctness(self):
        a = [3,5,2,4,8,7,10]

        start_time = time.time()
        result = bubbleSort(a)
        print("--- test_bubbleSort_correctness: %s seconds ---" % (time.time() - start_time))

        self.assertEqual(result, [2,3,4,5,7,8,10])

    def test_bubbleSort_small_collection(self):
        start_time = time.time()
        result = bubbleSort(SMALL_COLLECTION)
        print("--- test_bubbleSort_small_collection: %s seconds ---" % (time.time() - start_time))
        self.assertEqual(result, SMALL_COLLECTION_RESULT)
        


if __name__ == '__main__':
    unittest.main(verbosity=2)