# Learning python in 2024

## Number in Python

* Number data types store numeric values. They are immutable data types, which means that changing the value of a number data type results in a newly allocated object.

* ### int datatype
  * Python int is the whole number, including negative numbers but not fractions. **In Python, there is no limit to how long an integer value can be**.

    ```python
    num1 = 8
    num2 = -8
    print(type(num1)) #<class 'int'>
    print(type(num2)) #<class 'int'>
    ```
* ### float datatype
    * This is a real number with a floating-point representation. It is specified by a decimal point. Optionally, the character e or E followed by a positive or negative integer may be appended to specify scientific notation. . Some examples of numbers that are represented as floats are 0.5 and -7.823457.

    * They can be created directly by entering a number with a decimal point, or by using operations such as division on integers. **Extra zeros present at the number’s end are ignored automatically**.

        ```python
        PI = 3.14
        print(type(PI)) #<class 'float>
        ```

* ### complex datatype
    * A complex number is a number that consists of real and imaginary parts. For example, 2 + 3j is a complex number where 2 is the real component, and 3 multiplied by j is an imaginary part.

        ```python
        num = 2 + 3j 
        print(type(num)) #<class 'complex>
        ```

## String in Python
 * In Python, a string is a sequence of characters enclosed within single, double, or triple quotes. Strings are immutable, meaning they cannot be modified after creation. 

 * They support various operations like concatenation, slicing, and formatting. Strings can contain alphanumeric characters, symbols, and whitespace.

 * Python provides extensive string manipulation methods, including searching, replacing, and splitting. String literals can include escape sequences to represent special characters.

 * Python offers powerful string formatting options using placeholders or f-strings. Strings play a fundamental role in Python programming, serving as data containers for text-based information in tasks ranging from simple data handling to complex text processing algorithms.

    ```python
    name = 'python'
    print(type(name)) #<class 'str'>
    ```

## List in Python

* In Python, a list is a mutable, ordered collection of items enclosed in square brackets []. Lists can contain elements of different types, such as integers, strings, or even other lists. 

* They support indexing and slicing for accessing elements, and offer versatile methods for manipulation, including appending, removing, and sorting items.

* Lists are commonly used to store and manage data that needs to be dynamically modified during program execution. Example: my_list = [1, "apple", 3.14, [4, 5]] combines integers, strings, a float, and another list. Access individual elements with my_list[0], my_list[1], etc.

    ```python
    my_list = [1, "apple", 3.14, [4, 5]] 
    my_list[0] # 1
    my_list[1] # apple
    type(my_list) # <class 'list'>
    ```