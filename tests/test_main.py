import unittest
from unittest.mock import patch
from app import calculate_operations, plot_graph

class TestMathOperations(unittest.TestCase):
    
    def test_sum(self):
        num1 = 5
        num2 = 3
        sum_result, _ = calculate_operations(num1, num2)
        self.assertEqual(sum_result, 8, "Sum operation failed")
        
    def test_difference(self):
        num1 = 5
        num2 = 3
        _, difference_result = calculate_operations(num1, num2)
        self.assertEqual(difference_result, 2, "Difference operation failed")
        
class TestPlotting(unittest.TestCase):

    @patch('matplotlib.pyplot.show')  # Mock plt.show() to prevent it from displaying a plot
    @patch('matplotlib.pyplot.scatter')  # Mock plt.scatter to check if it was called
    def test_plot_graph(self, mock_scatter, mock_show):
        # Let's mock a simple case: sum = 8, difference = 2
        plot_graph(8, 2)

        # Check if plt.scatter was called with the correct arguments (8, 2)
        mock_scatter.assert_called_once_with(8, 2)

        # Check if plt.show was called once
        mock_show.assert_called_once()

if __name__ == '__main__':
    unittest.main()
