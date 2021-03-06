import unittest
import random
import time
from utils import *
from bubble import bubbleSort
from selection import selectionSort
from insertion import insertionSort
from merge import mergeSort
from quick import quickSort

# Load related files
with open('testset/smallList.txt', 'r') as f:
    SMALL_COLLECTION = [int(line.rstrip()) for line in f]

with open('testset/smallListResult.txt', 'r') as f:
    SMALL_COLLECTION_RESULT = [int(line.rstrip()) for line in f]

class TestSortWithBigRandomAmount(unittest.TestCase):

    def test_10000_quick(self):
        LIST_10K = random.sample(range(10000), 10000)
        LIST_10K_ANSWER = sorted(LIST_10K)
        start_time = time.time()
        result = quickSort(LIST_10K)
        print("##Quick Sort <10k> ## ==> TIME: %s seconds\n" % (time.time() - start_time))
        self.assertEqual(result, LIST_10K_ANSWER)

    def test_10000_merge(self):
        LIST_10K = random.sample(range(10000), 10000)
        LIST_10K_ANSWER = sorted(LIST_10K)
        start_time = time.time()
        result = mergeSort(LIST_10K)
        print("##Merge Sort <10k> ## ==> TIME: %s seconds\n" % (time.time() - start_time))
        self.assertEqual(result, LIST_10K_ANSWER)

    def test_10000_bubble(self):
        LIST_10K = random.sample(range(10000), 10000)
        LIST_10K_ANSWER = sorted(LIST_10K)
        start_time = time.time()
        result = bubbleSort(LIST_10K)
        print("##Bubble Sort <10k> ## ==> TIME: %s seconds\n" % (time.time() - start_time))
        self.assertEqual(result, LIST_10K_ANSWER)

    def test_10000_insertion(self):
        LIST_10K = random.sample(range(10000), 10000)
        LIST_10K_ANSWER = sorted(LIST_10K)
        start_time = time.time()
        result = insertionSort(LIST_10K)
        print("##Insertion Sort <10k> ## ==> TIME: %s seconds\n" % (time.time() - start_time))
        self.assertEqual(result, LIST_10K_ANSWER)

    def test_10000_selection(self):
        LIST_10K = random.sample(range(10000), 10000)
        LIST_10K_ANSWER = sorted(LIST_10K)
        start_time = time.time()
        result = selectionSort(LIST_10K)
        print("##Insertion Sort <10k> ## ==> TIME: %s seconds\n" % (time.time() - start_time))
        self.assertEqual(result, LIST_10K_ANSWER)


class TestUtils(unittest.TestCase):
    def test_swap(self):
        a = [1,2,3]
        self.assertEqual(swap(0,1, a), [2,1,3])

# compare with the built in python sort function
class TestPythonBuiltInSort(unittest.TestCase):
    def test_python_build_in_sort_func_correctness(self):
        a = [3,5,2,4,8,7,10,43,1,9]
        start_time = time.time()
        result = sorted(a)
        print("##Python Sort <10> ## ==> TIME: %s seconds\n" % (time.time() - start_time))
        self.assertEqual(result, [1,2,3,4,5,7,8,9,10,43])

    def test_python_build_in_sort_func_small_collection(self):
        start_time = time.time()
        result = sorted(SMALL_COLLECTION)
        print("##Python Sort <1000>## ==> TIME: %s seconds\n" % (time.time() - start_time))
        self.assertEqual(result, SMALL_COLLECTION_RESULT)

class TestBubbleSort(unittest.TestCase):
    def test_bubbleSort_correctness(self):
        a = [3,5,2,4,8,7,10,43,1,9]

        start_time = time.time()
        result = bubbleSort(a)
        print("##Bubble Sort <10> ## ==> TIME: %s seconds\n" % (time.time() - start_time))

        self.assertEqual(result, [1,2,3,4,5,7,8,9,10,43])

    def test_bubbleSort_small_collection(self):
        start_time = time.time()
        result = bubbleSort(SMALL_COLLECTION)
        print("##Bubble Sort <1000> ## ==> TIME: %s seconds\n" % (time.time() - start_time))
        self.assertEqual(result, SMALL_COLLECTION_RESULT)
        


class TestSelectionSort(unittest.TestCase):
    def test_selectionSort_correctness(self):
        a = [3,5,2,4,8,7,10,43,1,9]

        start_time = time.time()
        result = selectionSort(a)
        print("##Selection Sort <10> ## ==> TIME: %s seconds\n" % (time.time() - start_time))

        self.assertEqual(result, [1,2,3,4,5,7,8,9,10,43])

    def test_selectionSort_small_collection(self):
        start_time = time.time()
        result = selectionSort(SMALL_COLLECTION)
        print("##Selection Sort <1000> ## ==> TIME: %s seconds\n" % (time.time() - start_time))
        self.assertEqual(result, SMALL_COLLECTION_RESULT)


class TestInsertionSort(unittest.TestCase):
    def test_insertionSort_correctness(self):
        a = [3,5,2,4,8,7,10,43,1,9]

        start_time = time.time()
        result = insertionSort(a)
        print("##Insertion Sort <10> ## ==> TIME: %s seconds\n" % (time.time() - start_time))

        self.assertEqual(result, [1,2,3,4,5,7,8,9,10,43])

    def test_insertionSort_small_collection(self):
        start_time = time.time()
        result = insertionSort(SMALL_COLLECTION)
        print("##Insertion Sort <1000> ## ==> TIME: %s seconds\n" % (time.time() - start_time))
        self.assertEqual(result, SMALL_COLLECTION_RESULT)

class TestMergeSort(unittest.TestCase):
    def test_mergeSort_correctness(self):
        a = [3,5,2,4,8,7,10,43,1,9]

        start_time = time.time()
        result = mergeSort(a)
        print("##Merge Sort <10> ## ==> TIME: %s seconds\n" % (time.time() - start_time))

        self.assertEqual(result, [1,2,3,4,5,7,8,9,10,43])

    def test_mergeSort_small_collection(self):
        start_time = time.time()
        result = mergeSort(SMALL_COLLECTION)
        print("##Merge Sort <1000> ## ==> TIME: %s seconds\n" % (time.time() - start_time))
        self.assertEqual(result, SMALL_COLLECTION_RESULT)

class TestQuickSort(unittest.TestCase):
    def test_quickSort_correctness(self):
        a = [3,5,2,4,8,7,10,43,1,9]

        start_time = time.time()
        result = quickSort(a)
        print("##Quick Sort <10> ## ==> TIME: %s seconds\n" % (time.time() - start_time))

        self.assertEqual(result, [1,2,3,4,5,7,8,9,10,43])

    def test_quickSort_small_collection(self):
        start_time = time.time()
        result = quickSort(SMALL_COLLECTION)
        print("##Quick Sort <1000> ## ==> TIME: %s seconds\n" % (time.time() - start_time))
        self.assertEqual(result, SMALL_COLLECTION_RESULT)

if __name__ == '__main__':
    unittest.main(verbosity=1)