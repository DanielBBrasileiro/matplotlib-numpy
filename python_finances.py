# How to calculate return?
# return = (price[i] - price[i-1]) / price[i-1]
# How to calculate it using Python and data from an Excel file?

import openpyxl
import numpy as np
import matplotlib.pyplot as plt

# Load Excel file
workbook = openpyxl.load_workbook(
    '/Users/daniel/Downloads/Exemplo_de_Acoes_1.1.xlsx'
)

sheet = workbook['Sheet1']

prices = [
    cell
    for cell in next(
        sheet.iter_cols(
            min_col=1,
            max_col=1,
            min_row=2,
            values_only=True
        )
    )
]

# Convert list to NumPy array
price_array = np.array(prices)
print(price_array)

# Calculate returns
returns = (price_array[1:20] - price_array[0:19]) / price_array[0:19]
print(returns)

# Plot returns
time_index = np.arange(0, 19)
plt.plot(time_index, returns)

plt.title('Returns')
plt.xlabel('Time')
plt.ylabel('Return')

plt.show()
