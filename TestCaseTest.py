from TestCase import TestCase
from WasRun import WasRun
from TestResult import TestResult


class TestCaseTest(TestCase):

    def setUp(self):
        self.test = WasRun("testMethod")

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        result = test.run()
        assert "setup testMethod tearDown " == test.log
        assert "1 run, 0 failed" == result.summary()

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert "1 run, 1 failed" == result.summary()


TestCaseTest("testTemplateMethod").run()
TestCaseTest("testFailedResult").run()
