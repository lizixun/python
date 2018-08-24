for value in range(1,5):
    print(value)
numbers=list(range(1,6))
print(numbers)
print(list(range(2,11,2)))
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)
print(squares)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
array=[num**2 for num in range(1,11)]
print(array)