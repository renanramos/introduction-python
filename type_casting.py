a = '237' # if we add '237' with 3 (int) throws a typeError: can only concatenate str (not "int") to str
b = int(a)

print(b)

c = str(b)

print(c)

x = [b, c]

print(x)
