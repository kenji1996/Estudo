#Maneira mais complexa porem mais otimizada, portanto mais rapida, de implementar fila com prioridade
#   usando a library heapq 
import heapq
  
# initializing list 1
li1 = [5, 7, 9, 4, 3]
  
# initializing list 2
li2 = [5, 7, 9, 4, 3]
  
# using heapify() to convert list into heap
heapq.heapify(li1)
heapq.heapify(li2)
  
# using heappushpop() to push and pop items simultaneously
# pops 2
print ("The popped item using heappushpop() is : ",end="")
print (heapq.heappushpop(li1, 2))
  
# using heapreplace() to push and pop items simultaneously
# pops 3
print ("The popped item using heapreplace() is : ",end="")
print (heapq.heapreplace(li2, 2))

print("The 3 largest numbers in list are : ",end="")
print(heapq.nlargest(3, li1))
  
# using nsmallest to print 3 smallest numbers
# prints 1, 3 and 4
print("The 3 smallest numbers in list are : ",end="")
print(heapq.nsmallest(3, li1))