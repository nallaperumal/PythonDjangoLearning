def GetSquare(max_val):
    count = 1
    while count < max_val:
        yield count*count #like return but loop will contine
        count += 1

mySquares = GetSquare(10)
print(next(mySquares))
print(next(mySquares))
print(next(mySquares))
print("...")
for sqNumber in mySquares:
    print(sqNumber)