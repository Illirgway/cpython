from test.test_support import verbose
import random
from UserList import UserList

nerrors = 0

def check(tag, expected, raw, compare=None):
    global nerrors

    if verbose:
        print "    checking", tag

    orig = raw[:]   # save input in case of error
    if compare:
        raw.sort(compare)
    else:
        raw.sort()

    if len(expected) != len(raw):
        print "error in", tag
        print "length mismatch;", len(expected), len(raw)
        print expected
        print orig
        print raw
        nerrors += 1
        return

    for i, good in enumerate(expected):
        maybe = raw[i]
        if good is not maybe:
            print "error in", tag
            print "out of order at index", i, good, maybe
            print expected
            print orig
            print raw
            nerrors += 1
            return

# Try a variety of sizes at and around powers of 2, and at powers of 10.
sizes = [0]
for power in range(1, 10):
    n = 2 ** power
    sizes.extend(range(n-1, n+2))
sizes.extend([10, 100, 1000])

class Complains(object):
    maybe_complain = True

    def __init__(self, i):
        self.i = i

    def __lt__(self, other):
        if Complains.maybe_complain and random.random() < 0.001:
            if verbose:
                print "        complaining at", self, other
            raise RuntimeError
        return self.i < other.i

    def __repr__(self):
        return "Complains(%d)" % self.i

class Stable(object):
    def __init__(self, key, i):
        self.key = key
        self.index = i

    def __cmp__(self, other):
        return cmp(self.key, other.key)

    def __repr__(self):
        return "Stable(%d, %d)" % (self.key, self.index)

for n in sizes:
    x = range(n)
    if verbose:
        print "Testing size", n

    s = x[:]
    check("identity", x, s)

    s = x[:]
    s.reverse()
    check("reversed", x, s)

    s = x[:]
    random.shuffle(s)
    check("random permutation", x, s)

    y = x[:]
    y.reverse()
    s = x[:]
    check("reversed via function", y, s, lambda a, b: cmp(b, a))

    if verbose:
        print "    Checking against an insane comparison function."
        print "        If the implementation isn't careful, this may segfault."
    s = x[:]
    s.sort(lambda a, b:  int(random.random() * 3) - 1)
    check("an insane function left some permutation", x, s)

    x = [Complains(i) for i in x]
    s = x[:]
    random.shuffle(s)
    Complains.maybe_complain = True
    it_complained = False
    try:
        s.sort()
    except RuntimeError:
        it_complained = True
    if it_complained:
        Complains.maybe_complain = False
        check("exception during sort left some permutation", x, s)

    s = [Stable(random.randrange(10), i) for i in xrange(n)]
    augmented = [(e, e.index) for e in s]
    augmented.sort()    # forced stable because ties broken by index
    x = [e for e, i in augmented] # a stable sort of s
    check("stability", x, s)


import unittest
from test import test_support
import sys

#==============================================================================

class TestBugs(unittest.TestCase):

    def test_bug453523(self):
        # bug 453523 -- list.sort() crasher.
        # If this fails, the most likely outcome is a core dump.
        # Mutations during a list sort should raise a ValueError.

        class C:
            def __lt__(self, other):
                if L and random.random() < 0.75:
                    L.pop()
                else:
                    L.append(3)
                return random.random() < 0.5

        L = [C() for i in range(50)]
        self.assertRaises(ValueError, L.sort)

    def test_cmpNone(self):
        # Testing None as a comparison function.

        L = range(50)
        random.shuffle(L)
        L.sort(None)
        self.assertEqual(L, range(50))

#==============================================================================

class TestDecorateSortUndecorate(unittest.TestCase):

    def test_decorated(self):
        data = 'The quick Brown fox Jumped over The lazy Dog'.split()
        copy = data[:]
        random.shuffle(data)
        data.sort(key=str.lower)
        copy.sort(cmp=lambda x,y: cmp(x.lower(), y.lower()))

    def test_baddecorator(self):
        data = 'The quick Brown fox Jumped over The lazy Dog'.split()
        self.assertRaises(TypeError, data.sort, None, lambda x,y: 0)

    def test_stability(self):
        data = [(random.randrange(100), i) for i in xrange(200)]
        copy = data[:]
        data.sort(key=lambda (x,y): x)  # sort on the random first field
        copy.sort()                     # sort using both fields
        self.assertEqual(data, copy)    # should get the same result

    def test_cmp_and_key_combination(self):
        # Verify that the wrapper has been removed
        def compare(x, y):
            self.assertEqual(type(x), str)
            self.assertEqual(type(x), str)
            return cmp(x, y)
        data = 'The quick Brown fox Jumped over The lazy Dog'.split()
        data.sort(cmp=compare, key=str.lower)

    def test_badcmp_with_key(self):
        # Verify that the wrapper has been removed
        data = 'The quick Brown fox Jumped over The lazy Dog'.split()
        self.assertRaises(TypeError, data.sort, "bad", str.lower)

    def test_key_with_exception(self):
        # Verify that the wrapper has been removed
        data = range(-2,2)
        dup = data[:]
        self.assertRaises(ZeroDivisionError, data.sort, None, lambda x: 1/x)
        self.assertEqual(data, dup)

    def test_reverse(self):
        data = range(100)
        random.shuffle(data)
        data.sort(reverse=True)
        self.assertEqual(data, range(99,-1,-1))
        self.assertRaises(TypeError, data.sort, "wrong type")

    def test_reverse_stability(self):
        data = [(random.randrange(100), i) for i in xrange(200)]
        copy1 = data[:]
        copy2 = data[:]
        data.sort(cmp=lambda x,y: cmp(x[0],y[0]), reverse=True)
        copy1.sort(cmp=lambda x,y: cmp(y[0],x[0]))
        self.assertEqual(data, copy1)
        copy2.sort(key=lambda x: x[0], reverse=True)
        self.assertEqual(data, copy2)

class TestSorted(unittest.TestCase):

    def test_basic(self):
        data = range(100)
        copy = data[:]
        random.shuffle(copy)
        self.assertEqual(data, list.sorted(copy))
        self.assertNotEqual(data, copy)

        data.reverse()
        random.shuffle(copy)
        self.assertEqual(data, list.sorted(copy, cmp=lambda x, y: cmp(y,x)))
        self.assertNotEqual(data, copy)
        random.shuffle(copy)
        self.assertEqual(data, list.sorted(copy, key=lambda x: -x))
        self.assertNotEqual(data, copy)
        random.shuffle(copy)
        self.assertEqual(data, list.sorted(copy, reverse=1))
        self.assertNotEqual(data, copy)

    def test_inputtypes(self):
        s = 'abracadabra'
        for T in [unicode, list, tuple]:
            self.assertEqual(list.sorted(s), list.sorted(T(s)))

        s = ''.join(dict.fromkeys(s).keys())  # unique letters only
        for T in [unicode, set, frozenset, list, tuple, dict.fromkeys]:
            self.assertEqual(list.sorted(s), list.sorted(T(s)))

    def test_baddecorator(self):
        data = 'The quick Brown fox Jumped over The lazy Dog'.split()
        self.assertRaises(TypeError, list.sorted, data, None, lambda x,y: 0)

    def classmethods(self):
        s = "hello world"
        a = list.sorted(s)
        b = UserList.sorted(s)
        c = [].sorted(s)
        d = UserList().sorted(s)
        class Mylist(list):
            def __new__(cls):
                return UserList()
        e = MyList.sorted(s)
        f = MyList().sorted(s)
        class Myuserlist(UserList):
            def __new__(cls):
                return []
        g = MyList.sorted(s)
        h = MyList().sorted(s)
        self.assert_(a == b == c == d == e == f == g == h)
        self.assert_(b.__class__ == d.__class__ == UserList)
        self.assert_(e.__class__ == f.__class__ == MyList)
        self.assert_(g.__class__ == h.__class__ == Myuserlist)

#==============================================================================

def test_main(verbose=None):
    test_classes = (
        TestDecorateSortUndecorate,
        TestSorted,
        TestBugs,
    )

    test_support.run_unittest(*test_classes)

    # verify reference counting
    if verbose and hasattr(sys, "gettotalrefcount"):
        import gc
        counts = [None] * 5
        for i in xrange(len(counts)):
            test_support.run_unittest(*test_classes)
            gc.collect()
            counts[i] = sys.gettotalrefcount()
        print counts

if __name__ == "__main__":
    test_main(verbose=True)


