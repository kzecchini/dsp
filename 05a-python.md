# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Python lists and tuples both contain ordered values. Retrieving a value from a tuple or list is the same - using `list[index]` or `tuple[index]`. It follows that slice notation and the `in` operator work the same way for each. The main difference is that tuples are immutable and lists are mutable. A tuple cannot be changed once it is created. You cannot add or remove elements from a tuple, so there is no extend, append, remove, or pop methods for tuples.

>> The list class does not implement the method hash - a requirement for any object which is to be used as a key in a dictionary. The reason for this is because of problems that arise when using a mutable object as a key. If a key is changed, then will the value correspond to the original key, or the altered key? This would lead to bad key references and inaccessible dictionary values. Tuples, however, will work as dictionary keys because they are immutable.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> A set is an unordered collection with no duplicate elements. A list is an ordered collection which may contain duplicate elements. Thus list has methods which can alter the order, or return certain elements by their index value. An example of a list would be a list of names and we want to append new names to the end. Sets are better at comparing and doing operations on groups of elements where the order doesn't matter. Some of the math operations you can perform are intersection, union, difference, and symmetric difference. An example where a set would be appropriate would be if an unordered set of cities you have been to. This could be compared to other people's sets to find information about the intersection and difference of their travels.

>> Sets are much better at finding an element than lists are. Every element in a set is hashed. So when looking for membership, all that needs to be done is look if the object is at the position determined by the hash. This means speed of retrieval is not based on the size of the set. However, for lists, the whole list needs to be searched up until it finds the element. For lists, search speed is dependent on the size of the list.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> `lambda` is Python's way of creating anonymous functions at runtime. The functions are anonymous as they are not bound to a name and are not called. `lambda` can be used inside of functions which may need an additional function to operate. Some of these functions include include `sorted`, `map`, `filter`, and `reduce`. For example, if we are sorting a list of tuples and want to sort by the last tuple, we can write:
```
list = [(1, 2), (2, 1), (4, 4), (8, 0)]
print sorted(list, key=lambda x: x[-1])
[(8, 0), (2, 1), (1, 2), (4, 4)]
```
Another example could be mapping the first element of the tuple using the same list:
```
map(lambda x: x[0], list)
[1, 2, 4, 8]
```
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are a concise notation for creating lists. They are especially handy when needing to create a list by applying an operation to an already existing sequence or iterable. It is denoted as `[expression for item in list if conditional]`. List comprehensions can be nested and can contain complex expressions. A simple example is performing an operation on a list of numbers:
```
[x**2 for x in range(5)]
[0, 1, 4, 9, 16]
```
This can also be expressed using `map`:
```
map(lambda x: x**2, range(5))
[0, 1, 4, 9, 16]
```
Another example is returning all squares in range(5) which are divisible by 2:
```
[x**2 for x in range(5) if x**2 % 2 == 0]
[0, 4, 16]
```
Again, this can be represented through the built in `map` and `filter` functions:
```
filter(lambda x: x % 2 == 0, map(lambda x: x**2, range(5)))
[0, 4, 16]
```
It is definitely more concise and readable to write these expressions inside of list comprehensions instead of using more complex `map` and `filter` expressions using `lambda`. 

>> Similarly to list comprehensions, there exist set comprehensions and dictionary comprehensions. The same format applies for sets, except `{}` around the expressions instead of `[]`. For dictionaries, instead of one expression to return in the set, a key value pair is required. An example of set comprehension and dictionary comprehension are as follows:
```
{x**2 for x in range(8) if x**2 % 2 != 0}
set([1, 25, 49, 9])
```
```
{x: x**2 for x in range(8) if x**2 % 2 != 0}
{1: 1, 3: 9, 5: 25, 7: 49}
```
---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days


b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days


c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





