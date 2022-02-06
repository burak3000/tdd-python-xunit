from TestCase import TestCase
from WasRun import WasRun


class TestCaseTest(TestCase):

    def setUp(self):
        self.test = WasRun("testMethod")

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert "setup testMethod tearDown " == test.log
        print(test.log)

    # def testRunning(self):
    #     self.test.run()
    #     assert("setup testMethod " == self.test.log)
    #
    # def testSetUp(self):
    #     self.test.run()
    #     assert("setup " == self.test.log)


TestCaseTest("testTemplateMethod").run()
