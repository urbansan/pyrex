import unittest


class TestGen(unittest.TestCase):
    expected_fails = (
        'HeavyTester.test_expected_fail'
    )
    @classmethod
    def generate(cls):
        class HeavyTester(unittest.TestCase):
            def test_expected_fail(self):
                self.fail('expected fail')

            def test_success(self):
                self.assertTrue(True, 'expected success')

            def test_unexpected_fail(self):
                self.fail('unexpected fail')
        suite = unittest.TestSuite()
        loader = unittest.TestLoader()
        import io
        void = io.StringIO()
        runner = unittest.TextTestRunner(void)
        tests = loader.loadTestsFromTestCase(HeavyTester)
        suite.addTests(tests)
        result = runner.run(suite)
        print()
        for id_, fail in enumerate(result.failures):
            class_ = type(fail[0]).__name__
            test_method = fail[0]._testMethodName
            id_string = f'{class_}.{test_method}'
            is_expected = id_string in cls.expected_fails
            def outer(is_expected, id_string):
                def inner(self):
                    self.assertTrue(is_expected, id_string)
                return inner

            setattr(cls, f'test_fails_{class_}_{test_method}', outer(is_expected, id_string))

TestGen.generate()

print()
if __name__ == '__main__':
    global_runner = unittest.TextTestRunner()
    global_suite = unittest.TestSuite()
    global_loader = unittest.TestLoader()
    global_suite.addTests(global_loader.loadTestsFromTestCase(TestGen))
    global_runner.run(global_suite)


