from random_names import random_names

import unittest


class DummyRandomizer:
    pass


class StubRandomizer:
    def randomize(self, names):
        return "Budi"


class SpyRandomizer:
    def __init__(self):
        self.randomize_method_called = False

    def randomize(self, names):
        self.randomize_method_called = True
        return "Budi"


class MockRandomizer:
    def __init__(self):
        self.count_called = 0
        self.expected_methods_called = {}

    def expect(self, expectations):
        for ex in expectations:
            self.expected_methods_called[ex] = False

    def verify(self):
        for val in self.expected_methods_called.values():
            if val != True:
                return False
        return True

    def randomize(self, names):
        self.count_called += 1
        self.expected_methods_called["randomize"] = True
        return "Budi"


class FakeRandomizer:
    def __init__(self):
        self.count_called = 0
        self.expected_methods_called = {}

    def expect(self, expectations):
        for ex in expectations:
            self.expected_methods_called[ex] = False

    def verify(self):
        for val in self.expected_methods_called.values():
            if val != True:
                return False
        return True

    def randomize(self, names):
        self.count_called += 1
        self.expected_methods_called["randomize"] = True

        if len(names) == 0:
            return ""
        else:
            return names[0]


class TestFaktorial(unittest.TestCase):
    def test_empty_name(self):
        result = random_names(DummyRandomizer(), [])
        self.assertEqual(result, "No name provided")

    def test_single_name(self):
        randomizer = MockRandomizer()
        randomizer.expect(["randomize"])
        result = random_names(randomizer, ["Budi"])
        self.assertEqual(result, "Budi")
        self.assertEqual(randomizer.verify(), True)

    def test_multiple_names(self):
        randomizer = FakeRandomizer()
        randomizer.expect(["randomize"])
        result = random_names(randomizer, ["Cheryl", "Ibnu", "Matthew"])
        self.assertEqual(result, "Cheryl")
        self.assertEqual(randomizer.verify(), True)


if __name__ == "__main__":
    unittest.main()