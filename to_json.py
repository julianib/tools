to_convert = """
sample: text
"""

lines = to_convert.strip("\n").split("\n")

output = {}
for line in lines:
    index = line.index(":")
    key = line[:index]
    value = line[index + 2:]
    output[key] = value

print(output)
