import matplotlib.pyplot as plt

# Function to calculate sum and difference
def calculate_operations(num1, num2):
    sum_result = num1 + num2
    difference_result = num1 - num2
    return sum_result, difference_result

# Function to plot sum and difference as coordinates on a graph
def plot_graph(sum_result, difference_result):
    # Create a scatter plot with sum as x and difference as y
    plt.scatter(sum_result, difference_result)
    plt.title(f"Sum vs Difference: ({sum_result}, {difference_result})")
    plt.xlabel("Sum")
    plt.ylabel("Difference")
    
    # Show the plot
    plt.grid(True)
    plt.show()

# Main function to execute the calculations and plotting
def main():
    # Example input, you can modify this to take user input or other sources
    num1 = 25
    num2 = 10
    
    sum_result, difference_result = calculate_operations(num1, num2)
    plot_graph(sum_result, difference_result)

if __name__ == "__main__":
    main()
