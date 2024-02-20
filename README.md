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