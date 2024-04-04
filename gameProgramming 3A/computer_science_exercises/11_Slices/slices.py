# Slices, Gavin, Kloeckner, v0.1


alphabet = "abcdefghijklmnopqrstuvwxyz"
string0 = "Type a random string."
string1 = "You're getting drafted into the US Army!"
string2 = "Go drive a tank! It only costs a couple million $$."


# Python treats strings like lists
# There is an index value for each character in the string

print(alphabet[0])
print(alphabet[-1])

# Slice Operator:
# Syntax stringname[start:stop]
# start = inclusive
# stop = exclusive

print(alphabet[4:12]) # e to l


print(string1[3:13])
print(string1[0:6])
print(string1[7:40])
# Slice to the end
print(string0[3:])

# Slice from the start
print(string2[:13])

# Slice the whole thing
print(string2[:])