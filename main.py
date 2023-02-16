# #File Objects

# f = open('test.txt', 'a')
# f.write(" I like garfield")
# #read gives us everything
# #readline gives us the first line
# # print(f.readline())

# f.close()

# f = open('employees.txt', 'a')
# f.write(" These are very boring names")
# f.write(" I like pie")
# f.close()

# with open('test.txt', 'w') as f:
  # f_contents = f.read()
  # f.write("wowie fortnite")
  # print(f)

# with open('test.txt', 'w') as f:
#   for line in f:
#     print(line, end='')

with open('period7.txt','a') as f:
  f.write(" I know how to read, write, and append text files on python")