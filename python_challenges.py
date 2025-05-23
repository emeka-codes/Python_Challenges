#Reversing the words in a sentence
test= 'Today is the fourth day of the week'
def reverseWords(ourSentence):
   LLIST= []
   testResult= ourSentence.split()
   for currentValue in reversed(testResult):
      LLIST.append(currentValue)
   for word in LLIST:
      print(word, end=" ")
reverseWords(test)
print()


#Checking for prime numbers
listOfNumbers= [2, 5, 7, 9, 33, 37]
newListt=[]
def checkPrimeNumbers(numbers):
   for number in listOfNumbers:
      for currentNumber in range(2, number):
         if number % currentNumber == 0:
            if number not in newListt:
               newListt.append(number)
               print (f'{number} is not a prime number') 
            else:
               pass
      
         else:
            pass
checkPrimeNumbers(listOfNumbers)


#Least Recently Used Cache
from collections import OrderedDict
class LeastRecentlyUsed:
   def __init__(self, capacity):
      self.cache= OrderedDict()
      self.capacity = capacity
   def get (self, key):
      if key not in self.cache:
         return -1
      self.cache.move_to_end(key)
      return self.cache[key]
   def put (self, key, value):
      if key in self.cache:
         self.cache[key]= value
         self.cache.move_to_end(key)
      self.cache[key]= value
      
      if len(self.cache) > self.capacity:
         self.cache.popitem(last=False)
   def display(self):
      for key, value in self.cache.items():
         print(key, value)

LRU= LeastRecentlyUsed(4)
LRU.put(1, 10)
LRU.put(2, 20)
LRU.put(3, 30)
LRU.put(4, 40)

print(LRU.get(1))
LRU.put('Date', 22)
print(LRU.display())



#Checking top n most frequent element in a list of given elements
from collections import Counter
import heapq
days= ['Monday', 'Tuesday', 'Friday', 'Monday', 'Wednesday', 'Wednesday']
k= 2
count= Counter(days)
result= heapq.nlargest(2, count.items(), key=lambda x: x[1])
print(result)


#Rotating a 2D Matrix 
rotatedMatrix= []    
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

for i in range(len(matrix)):
   newMatrix= [currentValue[i] for currentValue in reversed(matrix)]
   rotatedMatrix.append(newMatrix)
   
print(rotatedMatrix)


#Finding the missing number in an array
arr= [0, 3, 1, 5, 2]
def findingMissingNumber(ourArray):
   myList= [num for num in range(0, len(arr)+1)]
   for currentNum in myList:
      if currentNum not in ourArray:
         print(f'The missing number in {ourArray} is {currentNum}')

(findingMissingNumber(arr))


#Log File Parser, returning the log levels as key and the number of times each log level appears as value in a dict
from collections import Counter
logLevels= []
logLevelsTwo= []
def fileParser(logFile):
   with open(logFile) as f:
      for line in f:
         x= line.split()
         logLevels.append(x[2])
         
      for log in logLevels:
         y= log[0:len(log)-1]
         logLevelsTwo.append(y)
      count= Counter(logLevelsTwo)
      print(count)
 
fileParser('log.txt')


