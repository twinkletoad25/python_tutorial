# Read the data file
#filename = "data/wxobs20170821.txt"
#datafile = open(filename, 'r')
#with open(filename, 'r') as datafile:
#    data = datafile.read()

# Initialize my data variable
data = []

# Read and parse the data file
filename = "data/wxobs20170821.txt"
with open(filename, 'r') as datafile:

# Read the first three lines (header)
    for _ in range(3):
        datafile.readline()

# Read and parse the rest of the file
    for line in datafile:
        datum = line.split()
        data.append(datum)

