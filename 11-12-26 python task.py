
import numpy as np

# =====================================================
# TASK 1: Create 0-D, 1-D, 2-D and 3-D Arrays
# =====================================================

print("\n========== TASK 1 ==========")

arr_0d = np.array(10)
arr_1d = np.array([10, 20, 30, 40])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
arr_3d = np.array([[[1, 2], [3, 4]],
                   [[5, 6], [7, 8]]])

# Store array attributes separately
array_info = {
    "0-D": {
        "ndim": arr_0d.ndim,
        "shape": arr_0d.shape,
        "size": arr_0d.size
    },
    "1-D": {
        "ndim": arr_1d.ndim,
        "shape": arr_1d.shape,
        "size": arr_1d.size
    },
    "2-D": {
        "ndim": arr_2d.ndim,
        "shape": arr_2d.shape,
        "size": arr_2d.size
    },
    "3-D": {
        "ndim": arr_3d.ndim,
        "shape": arr_3d.shape,
        "size": arr_3d.size
    }
}

print("0-D Array:", arr_0d)
print("1-D Array:", arr_1d)
print("2-D Array:\n", arr_2d)
print("3-D Array:\n", arr_3d)

for name, details in array_info.items():
    print(name, "Array Attributes:", details)


# =====================================================
# TASK 2: Generate Numbers Using np.arange()
# =====================================================

print("\n========== TASK 2 ==========")

arr2 = np.arange(1, 101, 5)

print("Numbers from 1 to 100 with step 5:")
print(arr2)


# =====================================================
# TASK 3: Generate Numbers Using np.linspace()
# =====================================================

print("\n========== TASK 3 ==========")

arr3 = np.linspace(1, 50, 10)

print("10 Equally Spaced Numbers:")
print(arr3)


# =====================================================
# TASK 4: Array Initialization
# =====================================================

print("\n========== TASK 4 ==========")

zero_matrix = np.zeros((3, 3))
ones_matrix = np.ones((4, 4))
full_matrix = np.full((2, 3), 100)

print("3x3 Zero Matrix:")
print(zero_matrix)

print("4x4 Ones Matrix:")
print(ones_matrix)

print("2x3 Matrix Filled with 100:")
print(full_matrix)


# =====================================================
# TASK 5: Random Integer Statistics
# =====================================================

print("\n========== TASK 5 ==========")

random_numbers = np.random.randint(1, 101, size=20)

maximum = np.max(random_numbers)
minimum = np.min(random_numbers)
average = np.mean(random_numbers)
total = np.sum(random_numbers)

print("Random Numbers:")
print(random_numbers)

print("Maximum:", maximum)
print("Minimum:", minimum)
print("Average:", average)
print("Sum:", total)


# =====================================================
# TASK 6: Logarithmically Spaced Values
# =====================================================

print("\n========== TASK 6 ==========")

log_values = np.logspace(1, 5, num=5)

print("Logarithmic Values:")
print(log_values)


# =====================================================
# TASK 7: Data Type Conversion
# =====================================================

print("\n========== TASK 7 ==========")

original = np.array([10.5, 20.8, 30.9, 40.2])

int_array = original.astype(int)
float32_array = original.astype(np.float32)
float64_array = original.astype(np.float64)

print("Original Array:", original)

print("Integer Array:", int_array)
print("Integer Data Type:", int_array.dtype)

print("Float32 Array:", float32_array)
print("Float32 Data Type:", float32_array.dtype)

print("Float64 Array:", float64_array)
print("Float64 Data Type:", float64_array.dtype)


# =====================================================
# TASK 8: 5x5 Array Properties
# =====================================================

print("\n========== TASK 8 ==========")

arr8 = np.arange(1, 26).reshape(5, 5)

shape = arr8.shape
size = arr8.size
dimensions = arr8.ndim
data_type = arr8.dtype
item_size = arr8.itemsize

print("5x5 Array:")
print(arr8)

print("Shape:", shape)
print("Size:", size)
print("Dimensions:", dimensions)
print("Data Type:", data_type)
print("Item Size:", item_size, "bytes")


# =====================================================
# TASK 9: Calculate Memory Consumption
# =====================================================

print("\n========== TASK 9 ==========")

arr9 = np.arange(1, 101, dtype=np.int64)

total_memory = arr9.size * arr9.itemsize

print("Array:")
print(arr9)

print("Number of Elements:", arr9.size)
print("Data Type:", arr9.dtype)
print("Item Size:", arr9.itemsize, "bytes")
print("Total Memory Consumption:", total_memory, "bytes")


# =====================================================
# TASK 10: Positive and Negative Indexing
# =====================================================

print("\n========== TASK 10 ==========")

arr10 = np.arange(10, 101)

print("Original Array:")
print(arr10)

print("First Element:", arr10[0])
print("Last Element:", arr10[-1])
print("Third Element:", arr10[2])
print("Second Last Element:", arr10[-2])


# =====================================================
# TASK 11: 2-D Array Indexing
# =====================================================

print("\n========== TASK 11 ==========")

a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Original Matrix:")
print(a)

print("Element 10:", a[0, 0])
print("Element 50:", a[1, 1])
print("Element 90:", a[2, 2])
print("Element 30:", a[0, 2])
print("Element 70:", a[2, 0])


# =====================================================
# TASK 12: Array Slicing
# =====================================================

print("\n========== TASK 12 ==========")

arr12 = np.arange(1, 21)

print("Original Array:", arr12)

print("First Five Elements:", arr12[:5])
print("Last Five Elements:", arr12[-5:])
print("Every Second Element:", arr12[::2])
print("Reversed Array:", arr12[::-1])


# =====================================================
# TASK 13: 2-D Array Slicing
# =====================================================

print("\n========== TASK 13 ==========")

arr13 = np.arange(1, 26).reshape(5, 5)

print("Original Matrix:")
print(arr13)

sub_matrix = arr13[1:4, 1:4]

print("Required Sub-Matrix:")
print(sub_matrix)


# =====================================================
# TASK 14: 3-D Array Indexing and Slicing
# =====================================================

print("\n========== TASK 14 ==========")

arr14 = np.arange(1, 25).reshape(2, 3, 4)

print("Original 3-D Array:")
print(arr14)

first_matrix = arr14[0]
second_matrix = arr14[1]

print("First 2-D Matrix:")
print(first_matrix)

print("Second 2-D Matrix:")
print(second_matrix)

last_two_columns = arr14[:, :, 2:]

print("Last Two Columns from Both Matrices:")
print(last_two_columns)


# =====================================================
# TASK 15: Fancy Indexing
# =====================================================

print("\n========== TASK 15 ==========")

a15 = np.array([10, 20, 30, 40, 50, 60, 70, 80])

selected = a15[[1, 3, 5, 7]]

print("Original Array:", a15)
print("Elements at Indices 1, 3, 5, 7:")
print(selected)


# =====================================================
# TASK 16: Boolean Masking
# =====================================================

print("\n========== TASK 16 ==========")

arr16 = np.random.randint(1, 101, size=20)

greater_50 = arr16[arr16 > 50]
less_25 = arr16[arr16 < 25]
between_30_70 = arr16[(arr16 >= 30) & (arr16 <= 70)]

print("Random Numbers:")
print(arr16)

print("Values Greater Than 50:")
print(greater_50)

print("Values Less Than 25:")
print(less_25)

print("Values Between 30 and 70:")
print(between_30_70)


# =====================================================
# TASK 17: Student Marks Analysis
# =====================================================

print("\n========== TASK 17 ==========")

marks = np.array([45, 78, 90, 32, 88,
                  56, 95, 25, 67, 85])

print("Original Marks:")
print(marks)

above_60 = marks[marks > 60]
below_35 = marks[marks < 35]

count_60 = np.count_nonzero(marks >= 60)

print("Marks Greater Than 60:")
print(above_60)

print("Marks Less Than 35:")
print(below_35)

print("Count of Marks Greater Than or Equal to 60:")
print(count_60)

# Replace marks below 35 with zero
marks[marks < 35] = 0

print("Modified Marks:")
print(marks)

modified_average = np.mean(marks)

print("Average of Modified Marks:", modified_average)


# =====================================================
# TASK 18: Iteration Using np.nditer()
# =====================================================

print("\n========== TASK 18 ==========")

matrix = np.array([
    [10, 20, 60],
    [40, 55, 70],
    [80, 90, 30]
])

print("Original Matrix:")
print(matrix)

total_sum = 0
even_count = 0
greater_than_50 = []

print("Individual Elements:")

for element in np.nditer(matrix):

    value = element.item()

    print(value)

    total_sum += value

    if value % 2 == 0:
        even_count += 1

    if value > 50:
        greater_than_50.append(value)

print("Total Sum:", total_sum)
print("Even Elements Count:", even_count)
print("Elements Greater Than 50:", greater_than_50)


# =====================================================
# TASK 19: Iteration Using np.ndenumerate()
# =====================================================

print("\n========== TASK 19 ==========")

print("Diagonal Elements with Their Indices:")

for index, value in np.ndenumerate(matrix):

    if index[0] == index[1]:

        print("Index:", index, "Value:", value)


# =====================================================
# TASK 20: Sales Data Analysis
# =====================================================

print("\n========== TASK 20 ==========")

sales = np.array([1000, 2500, 500, 4000,
                  1500, 5000, 3000, 800])

print("Original Sales:")
print(sales)

# Calculate statistics on original sales
total_sales = np.sum(sales)
maximum_sales = np.max(sales)
minimum_sales = np.min(sales)

high_sales = sales[sales > 2000]

print("Total Sales:", total_sales)
print("Maximum Sales:", maximum_sales)
print("Minimum Sales:", minimum_sales)
print("Sales Greater Than 2000:", high_sales)

# Replace values below 1000
sales[sales < 1000] = 1000

print("Modified Sales:")
print(sales)

average_sales = np.mean(sales)

print("Average Sales After Replacement:", average_sales)


# =====================================================
# TASK 21: Employee Salary Analysis
# =====================================================

print("\n========== TASK 21 ==========")

salary = np.array([
    25000, 35000, 45000, 20000,
    60000, 55000, 30000, 75000
])

print("Original Salaries:")
print(salary)

# Find highest and lowest salaries
highest_salary = np.max(salary)
lowest_salary = np.min(salary)

# Extract salaries greater than 40000
salary_above_40000 = salary[salary > 40000]

print("Highest Salary:", highest_salary)
print("Lowest Salary:", lowest_salary)
print("Salaries Greater Than 40000:")
print(salary_above_40000)

# Increase all salaries by 10%
salary = salary.astype(np.float64)
salary = salary * 1.10

print("Salaries After 10% Increase:")
print(salary)

# Count salaries above 50000 after increment
count_above_50000 = np.count_nonzero(salary > 50000)

print("Count of Salaries Above 50000 After Increase:")
print(count_above_50000)

# Calculate average after increment
average_salary = np.mean(salary)

print("Average Salary After Increase:", average_salary)


# =====================================================
# ASSIGNMENT COMPLETED
# =====================================================

print("\n====================================")
print("ALL 21 TASKS COMPLETED SUCCESSFULLY")
print("====================================")

