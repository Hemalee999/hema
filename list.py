List = []
Number = int(input("Enter the Total Number of List Elements= "))
for i in range(1, Number+1):
    value = int(input("Enter the Value of %d Element = " %i))
    List.append(value)
List.sort(reverse=True)
print("Sorting List in descending Order is = ", List)

###
OUTPUT:
Enter the Total Number of List Elements= 3
Enter the Value of 1 Element = 10
Enter the Value of 2 Element = 50
Enter the Value of 3 Element = 5
Sorting List in descending Order is =  [50, 10, 5]
###
