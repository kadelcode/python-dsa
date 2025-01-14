- It doesn't work properly because:
1. Modifying ```val``` does not modify ```data```:
- In Python, when you iterate over a list using ```for val in data```, ```val``` is just a temporary variable that takes the value of each element in the list during the iteration.
- Assigning to ```val``` or modifying it (e.g., ```val *= factor```) does not change the original list elements. Instead, it only updates the temporary variable ```val```.