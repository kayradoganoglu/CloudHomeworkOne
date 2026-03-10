# Take array elements from user and sort in descending order

numbers = list(map(int, input("Enter the array elements separated by spaces: ").split()))

numbers.sort(reverse=True)

print("Sorted array in descending order:", numbers) 
