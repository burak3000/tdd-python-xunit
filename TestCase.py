from TestResult import TestResult


class TestCase:
    def __init__(self, name):
        self.name = name

    def run(self):
        result = TestResult()
        result.testStarted()
        try:
            self.setUp()
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()

        self.tearDown()
        return result

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def summary(self):
        return "1 run, 0 failed"
