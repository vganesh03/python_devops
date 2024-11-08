import matplotlib
matplotlib.use('Agg')  # Use non-interactive Agg backend for matplotlib
import sys
from io import StringIO

# Import the functions from app.py
from app import calculate_operations, plot_graph

def test_sum():
    num1 = 5
    num2 = 3
    sum_result, _ = calculate_operations(num1, num2)
    assert sum_result == 8, "Sum operation failed"

def test_difference():
    num1 = 5
    num2 = 3
    _, difference_result = calculate_operations(num1, num2)
    assert difference_result == 2, "Difference operation failed"

def test_plot_graph():
    # We want to test if plot_graph is called and doesn't throw errors
    # Redirect stdout to capture any output
    captured_output = StringIO()
    sys.stdout = captured_output

    try:
        # Let's mock a simple case: sum = 8, difference = 2
        plot_graph(8, 2)

        # Since `plot_graph` doesn't return anything but just shows a plot,
        # we check if the function ran without errors.
        assert "Sum vs Difference" in captured_output.getvalue()

    finally:
        # Reset stdout
        sys.stdout = sys.__stdout__
