import unittest
from cosmopass.likelihoods.chisquares import model


class AppTests(unittest.TestCase):
    def test_app(self):
        lcdm = model('LCDM')
        lcdm.chi_list = ['h','bao']

        bao = lcdm.chi_bao(.3,147,.7,5,.8)
        h = lcdm.chi_h(.3,147,.7,5,.8)
        total =  lcdm.chi_sq(.3,147,.7,5,.8)
        self.assertEqual(total, h+bao)
#        self.assertNotEqual(squares(2), 5)

#    def test_errors(self):
#        """Check that method fails when parameter type is not numeric"""
#        with self.assertRaises(TypeError):
#            squares("foo")


def suite():
    _suite = unittest.TestSuite()
    _suite.addTest(AppTests('test_app'))
    return _suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())

