NumPy Practical Assignment – 21 Tasks
1. Project Description
This repository contains a Python practical assignment with 21 NumPy tasks. The program demonstrates how to create NumPy arrays, inspect array properties, generate numerical sequences, convert data types, access and modify array elements, filter values, iterate through multidimensional arrays, and perform simple analysis on student marks, sales, and employee salaries.

The assignment is implemented in one Python script and uses NumPy for numerical operations.
2. Objectives
- Create and work with 0-D, 1-D, 2-D, and 3-D arrays.
- Generate evenly spaced and logarithmically spaced values.
- Initialize arrays with zeros, ones, and a specified value.
- Calculate basic statistics such as minimum, maximum, sum, and mean.
- Inspect array dimensions, shape, size, data type, and memory usage.
- Convert arrays between integer and floating-point data types.
- Apply positive/negative indexing, slicing, and fancy indexing.
- Filter values using Boolean conditions.
- Iterate through arrays using np.nditer() and np.ndenumerate().
- Apply NumPy operations to simple student, sales, and salary examples.
3. Tools and Technologies
- Language: Python 3
- Library: NumPy
- Editor: VS Code, PyCharm, or any Python-compatible editor
- Execution: Command line / terminal
4. Installation and Requirements
Python 3 must be installed.

Install NumPy with:
python -m pip install numpy
Check that NumPy is installed:
python -c "import numpy; print(numpy.__version__)"
5. Files in This Repository
NumPy-Practical-Assignment/
├── 11-12-26 python task(1).py
└── README.md
The Python script contains all 21 tasks. The README explains the purpose and execution of the assignment.
6. Tasks Implemented
Task	Topic	Work performed
1	Array dimensions and attributes	Creates 0-D, 1-D, 2-D, and 3-D arrays; displays ndim, shape, and size.
2	np.arange()	Generates values from 1 with a step of 5, stopping before 101.
3	np.linspace()	Generates 10 equally spaced values between 1 and 50.
4	Array initialization	Creates zero, one, and constant-filled arrays using zeros(), ones(), and full().
5	Random integer statistics	Generates 20 random integers and calculates maximum, minimum, mean, and sum.
6	np.logspace()	Generates five logarithmically spaced values between 10¹ and 10⁵.
7	Data type conversion	Converts a floating-point array to int, float32, and float64.
8	5×5 array properties	Creates a 5×5 array and displays its shape, size, dimensions, data type, and item size.
9	Memory consumption	Calculates array memory usage using the number of elements and bytes per element.
10	Positive and negative indexing	Accesses first, last, third, and second-last elements of an array.
11	2-D array indexing	Accesses selected elements from a 3×3 matrix.
12	Array slicing	Extracts the first five, last five, and alternate elements, and reverses an array.
13	2-D array slicing	Extracts a 3×3 sub-matrix from a 5×5 matrix.
14	3-D indexing and slicing	Displays the two 2-D matrices and extracts their last two columns.
15	Fancy indexing	Selects elements at specified index positions.
16	Boolean masking	Filters random values greater than 50, less than 25, and between 30 and 70 inclusive.
17	Student marks analysis	Filters marks, counts marks greater than or equal to 60, replaces marks below 35 with zero, and calculates the modified average.
18	np.nditer()	Iterates through a matrix and calculates its sum, counts even values, and collects values greater than 50.
19	np.ndenumerate()	Displays the diagonal elements of the matrix with their index positions.
20	Sales data analysis	Calculates sales statistics, filters sales above 2000, replaces values below 1000, and calculates the modified average.
21	Employee salary analysis	Finds highest and lowest salaries, filters salaries above 40000, applies a 10% increase, counts salaries above 50000 after the increase, and calculates the new average.


7. How to Run the Program
1. Download or clone this repository.
2. Open the project folder in a terminal or Python IDE.
3. Confirm that Python 3 and NumPy are installed.
4. Run the script:
python "11-12-26 python task(1).py"
5. The terminal displays the output for each task, labelled from Task 1 to Task 21.
If the file is renamed, use the new filename in the command.
8. Concepts and NumPy Functions Used
Concept	Functions / Attributes
Array creation	np.array()
Numerical sequences	np.arange(), np.linspace(), np.logspace()
Array initialization	np.zeros(), np.ones(), np.full()
Random numbers	np.random.randint()
Array information	ndim, shape, size, dtype, itemsize
Data type conversion	astype()
Statistical operations	np.max(), np.min(), np.mean(), np.sum()
Counting	np.count_nonzero()
Reshaping	reshape()
Indexing and slicing	Positive, negative, and multi-dimensional indexing; slice notation
Filtering	Boolean masks and fancy indexing
Array iteration	np.nditer(), np.ndenumerate()


9. Notes About the Output
- Tasks 5 and 16 generate random numbers. Their values can change each time the script runs.
- The memory calculation in Task 9 depends on the array data type. The script uses int64, so each element occupies 8 bytes.
- In Task 7, converting floating-point values to integers removes the fractional part; it does not round to the nearest integer.
- In Task 20, total, maximum, minimum, and filtered high sales are calculated from the original array. Values below 1000 are then replaced, and the average is calculated from the modified array.
- In Task 21, the salary increase is applied before counting salaries above 50000 and calculating the new average.
10. Expected Learning Outcomes
After completing these tasks, the learner should be able to:
- Create and inspect NumPy arrays of different dimensions.
- Generate and initialize arrays for numerical work.
- Perform common calculations on array data.
- Select, slice, and filter array elements.
- Traverse multidimensional arrays and access their indices.
- Modify array values using conditions.
- Apply NumPy techniques to basic student marks, sales, and employee salary examples.
11. Conclusion
This practical assignment provides hands-on experience with 21 fundamental NumPy tasks. It demonstrates array creation, attributes, numerical operations, indexing, slicing, filtering, iteration, and basic data analysis. The examples build a foundation for using NumPy in Python programming and further data analysis.
Assignment: Python – NumPy Practical Tasks
Total tasks: 21
Main dependency: NumPy
