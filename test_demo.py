from unittest import TestCase
from unittest import skip
from unittest import SkipTest

@skip("Word in progress")
class TestDemo(TestCase):
  def test_case_1(self):
    self.assertEqual(1 + 1, 2)

  @skip("Word in progress")
  def test_case_2(self):
    self.assertEqual(1 + 1, 2)

  def test_case_3(self):
    self.skipTest("Word in progress")

  def test_case_4(self):
    raise SkipTest("Word in progress")
