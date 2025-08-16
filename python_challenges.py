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
mydict= {}

def fileParser(logFile):
   with open(logFile) as f:
      for line in f:
         x= line.split()
         logLevels.append(x[2])

      for log in logLevels:
         y= log[0:len(log)-1]
         mydict[y]= mydict.get(y, 0)+1
   print(mydict)
 
fileParser('log.txt')


#Merging overlapping intervals
myInterval= [(1, 3), (2, 6), (8, 10), (15, 18)]
def mergeOverlap(intervals):
   intervals.sort(key= lambda x: x[0])
   merged= [intervals[0]]

   for current in intervals[1:]:
      lastTuple= merged[-1]
      if current[0]<=lastTuple[1]:
         merged[-1]= (lastTuple[0], max(lastTuple[1], current[1]))
      else:
         merged.append(current)
   return merged
print(mergeOverlap(myInterval))



#Flattening a nested list
nested = [1, [2, [3, 4], 5], 6]

def flattenList(nested):
   newNested= []
   for current in nested:
      if isinstance(current, list):
         newNested.extend(flattenList(current))
      else:
         newNested.append(current)
   return newNested

print(flattenList(nested))


#Seat booking system for movie theatres.
class theater:
   def __init__(self, rows, columns):
      self.seats= [['O' for x in range(columns)] for y in range(rows)]
   
   def displaySeats(self):
      print('-----Silverbird Cinema Seat Booking System-----')
      for currentList in self.seats:
         print(currentList)

   def bookSeat(self, row= int, column= int):
      self.seats[row-1][column-1]= 'X'
      for currentValue in self.seats:
         print(currentValue)
      print(f'Seat at row {row} and column {column} booked!')

theaterOne= theater(3,6)
theaterOne.bookSeat(2,4)
theaterOne.displaySeats()



#counting elements that appear more than n/3 times
def freqnumbers(numbers):
   from collections import Counter
   count= Counter(numbers)
   freqList= [currentValue for currentValue, freq in count.items() if freq > len(numbers)//3 ]
   print(freqList)
freqnumbers([1,1,1,4,4,5,8,8,8,8])


#Converting from roman numerals to integers
def converttoroman(romanNumeral):
   romanNumerals= {'i': 1, "ii":2, "iii": 3, "iv": 4, "v": 5, "vi":6, "vii": 7, "viii":8, "ix": 9, "x": 10, "xc": 90, "c": 100, "cm": 900 , "m":1000,}
   total= 0
   prevValue= 0
   for currentRomanNumeral in reversed(romanNumeral):
      value = romanNumerals[currentRomanNumeral]
      if value < prevValue:
         total -= value
      else:
         total += value 
      prevValue= value
   print(total)

converttoroman("mcmxciv")


#paasword generator
import random

def generatepassword():
   alphabets= ['a', 'b', 'c', 'd', 'e']
   symbols= ['#', '@', '+', '?', '%']
   numbers= list(range(0, 10))
   all_char= alphabets + symbols + numbers
   password= int(input('What length of password would you like to generate: '))
   thePassword= [str(random.choice(all_char)) for current in range(password)]

   print(''.join(thePassword))
generatepassword()


#Two Sum II – Input Array is Sorted
def twoSumTarget(numbers):
   output= []     
   target= 9
   for x in range(len(numbers)):
      for y in range(x+1, len(numbers)):
         if numbers[x] + numbers[y]== target:
            output.append((x,y))
   return output
print(twoSumTarget([2,4,7,9]))


#Product of elements of an array except self 
def productArray(nums):   
   answer= []
   for index in range(len(nums)):
      product= 1
      for y in range(len(nums)):
         if y != index:
            product *= nums[y]
         else:
            continue
      answer.append(product)
   return answer
print(productArray([2,5,7,19]))



      


