import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def calculate_and_plot_returns(file_path: str):
    """
    Reads stock price data from a CSV file, calculates daily returns,
    and plots the results.

    Args:
        file_path (str): Path to the CSV file containing 'Date' and 'Price' columns.
    """
    # 1. Load data using Pandas (best practice for tabular data)
    try:
        df = pd.read_csv(file_path, index_col='Date', parse_dates=True)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return
    except Exception as e:
        print(f"Error while loading the file: {e}")
        return

    # 2. Calculate daily returns (financial best practice)
    df['Daily_Return'] = df['Price'].pct_change()

    # 3. Visualization with Matplotlib
    plt.figure(figsize=(10, 6))

    # Plot daily returns
    plt.plot(
        df.index,
        df['Daily_Return'] * 100,
        marker='o',
        linestyle='-',
        color='skyblue',
        markersize=4
    )

    # Add a horizontal zero line for reference
    plt.axhline(0, color='red', linestyle='--', linewidth=0.8)

    # Chart configuration
    plt.title('Daily Stock Price Returns', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Daily Return (%)', fontsize=12)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.xticks(rotation=45)
    plt.tight_layout()

    output_filename = os.path.join(
        os.path.dirname(file_path),
        'daily_returns_plot.png'
    )
    plt.savefig(output_filename)
    print(f"Chart saved at: {output_filename}")

if __name__ == "__main__":
    # Define the data file path
    # Relative path ensures portability across machines
    data_file = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        'data',
        'stock_prices.csv'
    )

    calculate_and_plot_returns(data_file)
