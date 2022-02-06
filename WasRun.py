from TestCase import TestCase


class WasRun(TestCase):
    def __init__(self, name):
        self.log = None
        self.name = name

    def testMethod(self):
        self.log = self.log + "testMethod "

    def setUp(self):
        self.log = "setup "

    def tearDown(self):
        self.log = self.log + "tearDown "
