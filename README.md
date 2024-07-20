# Data Structures and Algorithms using python

## Algorithms
> An algorithm is a step-by-step procedure for solving a problem or performing a task. It takes inputs, processes them through a sequence of well-defined steps, and produces outputs. Key characteristics include clarity, finiteness, and effectiveness. Algorithms are fundamental in computer science for tasks like sorting, searching, and optimizing data operations.

## Calculating complexities
### Time complexity
> Time complexity is a measure of the amount of time an algorithm takes to complete as a function of the size of its input. It helps in evaluating the efficiency and performance of the algorithm.

```py
# Example 1
for i in range(n):
    # Statements
```

- Time complexity for the above loop is O(n)

```py
for i in range(n):
    for j in range(n):
        # Statements
```

- Time complexity for the above nested loop is O(n*n)

### Space complexity
> Space complexity measures the amount of memory an algorithm uses relative to the input size. It includes all memory used by variables, data structures, and the call stack during execution.

```py
def example_function(arr):
    for i in range(len(arr)):
        # statements
        print(arr[i])
```
- Space complexity of the above function is O(1)