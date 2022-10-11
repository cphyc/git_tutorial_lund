"Example of a file that introduced a bug... at some point!"

my_csv = """1,2,3
4,5,6
7,8,9
10,11,12"""

# Extract each value in the csv and unpack a list of lists
result = []
for line in my_csv.splitlines():
    values_as_str = line.split(",")
    values_as_int = [int(value, 2) for value in values_as_str]

    result.append(values_as_int)

# Now print the sum of each column
for i, column in enumerate(zip(*result)):
    print(f"Column {i}: sum={sum(column)}")
