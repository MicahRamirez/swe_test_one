
from unittest import main, TestCase

from RangeIterator import   \
    range_iterator_class,   \
    range_iterator_function

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            range_iterator_class,
            range_iterator_function]

    def test_1 (self) :
        for f in self.a :
            with self.subTest() :
                p = f(2, 2)
                self.assertIs(iter(p), p)
                self.assertRaises(StopIteration, next, p)

    def test_2 (self) :
        for f in self.a :
            with self.subTest() :
                p = f(2, 3)
                self.assertIs(iter(p), p)
                self.assertEqual(next(p), 2)
                self.assertRaises(StopIteration, next, p)

    def test_3 (self) :
        for f in self.a :
            with self.subTest() :
                p = f(2, 4)
                self.assertIs(iter(p), p)
                self.assertEqual(next(p), 2)
                self.assertEqual(next(p), 3)
                self.assertRaises(StopIteration, next, p)

    def test_4 (self) :
        for f in self.a :
            with self.subTest() :
                p = f(2, 5)
                self.assertEqual(list(p), [2, 3, 4])
                self.assertEqual(list(p), [])

if __name__ == "__main__" :
    main()
