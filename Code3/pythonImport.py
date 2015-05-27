'''Demonstration of importing a Python module

author: ThH, date: May-2015'''

import numpy as np
import pythonFunction

# Generate test-data
testData = np.arange(-5, 10)

# Use a function from the imported module
out = pythonFunction.incomeAndExpenses(testData)

# Show some results
print('You have earned {0:5.2f} EUR, and spent {1:5.2f} EUR.'.format(out[0], -out[1]))