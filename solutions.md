# Here is my HackerRank Solutions

>The repository contains the solutions to various HackerRank problems.Organize the solutions so they are easy to navigate and understand. Each solution includes a reference to the problem statement and is well-documented to explain the logic and approach.




## Solution Approach

>In the "Solution Approach" section, provide a detailed explanation of your approach to solving the problem. Describe the algorithm, data structures, and any key insights that led to your solution. This helps others understand your thought process and learn from your solutions.

### Problem 1


  - [Problem](https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](./solution.py) (navigate to the Solution file)
  - Explanation: (Explain your problem-solving approach in detail)
  
### Problem 2

  - [Problem](https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](./solution.py)(navigate to the Solution file)
  - Explanation: (Explain your problem-solving approach in detail)

### Example  
---
## 3.Grading Students
  - [Problem](https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](Grading_Students/gradingstudents.py) (navigate to the Solution file)
  - Explanation:
  > In this problem, I created a program that takes input for the number of grades to be entered, and then prompts the user to enter each grade. The program then rounds each grade according to a specific rule and prints the rounded grades.
```python
n = int(input().strip())

for _ in range(n):
    grade = int(input().strip())
    
    if grade >= 38 and grade % 5 >= 3:
        grade += 5 - (grade % 5)

    print(grade)

```

It takes input for the number of grades to be entered as n.

 It uses a for loop to iterate over the range of the number of grades.

 Inside the loop, it takes input for each grade.

 It checks if the grade is greater than or equal to 38 and if the remainder of the grade divided by 5 is greater than or equal to 3.

 If the condition is true, it rounds the grade by adding the difference between 5 and the remainder of the grade divided by 5.
 
 Finally, it prints the rounded grade.

```
n = int(input().strip())  # Enter the number of grades: 3

for _ in range(n):
    grade = int(input().strip())  # Enter the grades: 73, 67, 41
    
    if grade >= 38 and grade % 5 >= 3:
        grade += 5 - (grade % 5)
    
    print(grade)
Output:

75
67
41
```
In this example, we entered 3 grades: 73, 67, and 41. The first grade, 73, is rounded up to 75 because the remainder of 73 divided by 5 is 3, which is greater than or equal to 3. The second grade, 67, remains the same because the remainder of 67 divided by 5 is 2, which is less than 3. The third grade, 41, also remains the same because it is less than 38.
****
## 4.Mini-Max Sum

  - [Problem](https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true)(navigate to the Problem)
  - [Solution](Mini-Max_Sum/minimaxsum.py) (navigate to the Solution file)
  - Explanation:
  >This problem  takes an array of integers as input and calculates the minimum and maximum sums of four out of the five elements in the array.

#### The miniMaxSum function takes an array (arr) as input and performs the following steps:

 1.Sorts the array in ascending order using the sort() method.

 2.Calculates the sum of all elements except the last one using the sum() function and slicing (arr[:-1]).

 3.Calculates the sum of all elements except the first one using the sum() function and slicing (arr[1:]).

 4.Prints the minimum sum and maximum sum.

 code with an example. Consider the following input:

```python
def miniMaxSum(arr):
    arr.sort()
    print(sum(arr[:-1]), sum(arr[1:]))

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    miniMaxSum(arr)

```
 The miniMaxSum function will perform the following steps:

 Example input: arr = 5 2 3 4 1

 ```arr.sort()```: Sorts arr in ascending order = [1,2,3,4,5]

 ```sum(arr[:-1])```: Calculate the minimum sum by removing last element of array: 1+2+3+4 = 10

 ```sum(arr[1:])```: Calculate the maximum sum by removing first element of array: 2+3+4+5= 14

 Print the minimum sum: 10
 
 Print the maximum sum: 14

#### Sample input & output
input
```
1 3 5 7 2 6
```
output
```
17 23
```
****


