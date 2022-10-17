
list=[7,9,20,3,6]
print("Original list ",list)

#insertion at a certain position
n = int(input('Enter an integer to insert:'))
p = int(input('Enter the insertion position:'))
list.insert(p,n)
print(list)

#delete first occurance
list.pop(0)
print("First element removed ",list)

#append
ap = int(input('Enter a number to append a number:'))
list.append(ap)
print("After appending", list)

#sorting
list.sort()
print("Sorted list ",list)

#pop
list.pop(len(list)-1)
print("After removing last element ",list)

#reverse
list.sort(reverse = True)
print("Reversed list ",list)
