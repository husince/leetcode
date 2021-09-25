from unittest import TestCase
from n1246 import Solution,Solution2

class TestSolution(TestCase):
    def setUp(self) -> None:
        self.solution = Solution()
        self.solution2 = Solution2()

    def test_minimum_moves(self):
        # self.solution = Solution()
        self.assertEqual(self.solution.minimumMoves([1,2]), 2)
        self.assertEqual(self.solution.minimumMoves([1,3,4,1,5]),3)

        self.assertEqual(self.solution2.minimumMoves([1, 2]), 2)
        self.assertEqual(self.solution2.minimumMoves([1, 3, 4, 1, 5]), 3)
