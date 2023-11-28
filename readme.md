<h1>Python Labs</h1>
<b>08-exceptions-fileio</b>
<table>
<tr>
<td><b>#</b></td>
<td><b>Problems</b></td>
</tr>
<td>
1</td>
<td>
Modify arithmagic() so that it verifies the user’s input at each step. Raise a ValueError with an informative error message if any of the following occur:
• The first number (step_1) is not a 3-digit number.
• The first number’s first and last digits differ by less than 2.
• The second number (step_2) is not the reverse of the first number.
• The third number (step_3) is not the positive difference of the first two numbers. • The fourth number (step_4) is not the reverse of the third number.
</td>
<tr>
<td>2</td>
<td>
Modify random_walk() so that if the user raises a KeyboardInterrupt by pressing ctrl+c while the program is running, the function catches the exception and prints “Process interrupted at iteration i”. If no KeyboardInterrupt is raised, print “Process completed”. In both cases, return walk as before.
</td>
</tr>
<tr>
<td>3</td>
<td>Define a class called ContentFilter. Implement the constructor so that it accepts the name of a file to be read. <br> 1. If the file name is invalid in any way, prompt the user for another filename using input(). Continue prompting the user until they provide a valid filename. <br> 2. Read the file and store its name and contents as attributes (store the contents as a single string). Make sure the file is securely closed.</td>
</tr>
<tr>
<td>4</td>
<td>Add the following methods to the ContentFilter class for writing the contents of the original file to new files. Each method should accept the name of a file to write to and a keyword argument mode that specifies the file access mode, defaulting to 'w'. If mode is not 'w', 'x', or 'a', raise a ValueError with an informative message.</td>
</tr>
</table>
<br>
<b>08-objectoriented</b>
<table>
<tr>
<td><b>#</b></td>
<td><b>Problems</b></td>
</tr>
<td>
1</td>
<td>
Expand the Backpack class to match the following specifications:
<br>1. Modify the constructor so that it accepts three total arguments:name,color, and max_size(in that order). Make max_size a keyword argument that defaults to5. Store each input as an attribute.
<br>2. Modify the put()method to check that the backpack does not go over capacity. If there are already max_size items or more, print “No Room!” and do not add the item to the contents list.
<br>3. Write a new method called dump()that resets the contents of the backpack to an empty list. This method should not receive any arguments (except self).
<br>4. Documentation is especially important in classes so that the user knows what an ob-ject’s attributes represent and how to use methods appropriately. Update (or write) the docstrings for the__init__(),put(), and dump()methods, as well as the actual class docstring (under class but before__init__()) to reflect the changes from parts 1-3 of this problem.
</td>
<tr>
<td>2</td>
<td>
Write a Jetpack class that inherits from the Backpack class.
<br>1. Override the constructor so that in addition to a name, color, and maximum size, it also accepts an amount of fuel. Change the default value of max_size to 2, and set the default value of fuel to 10. Store the fuel as an attribute.
<br>2. Add a fly()method that accepts an amount of fuel to be burned and decrements the fuel attribute by that amount. If the user tries to burn more fuel than remains, print “Not enough fuel!” and do not decrement the fuel.
<br>3. Override the dump()method so that both the contents and the fuel tank are emptied.
<br>4. Write clear, detailed docstrings for the class and each of its methods.
</td>
</tr>
<tr>
<td>3</td>
<td>
Endow the Backpack class with two additional magic methods:
<br>1. The__eq__()magic method is used to determine if two objects are equal, and is invoked by the==operator. Implement the__eq__()magic method for the Backpack class so that two Backpack objects are equal if and only if they have the same name, color, and number of contents.
<br>2. The__str__()magic method returns the string representation of an object. This method is invoked by str()and used by print().  Implement the__str__()method in the Backpack class so that printing a Backpack object yields the following output (that is,construct and return the following string).
</td>
</tr>
<tr>
<td>4</td>
<td>
Write a ComplexNumber class from scratch.
<br>1. Complex numbers are denote da+bi where a, b∈Randi=√−1. Write the constructor so it accepts two numbers. Store the first as self.real and the second as self.imag.
<br>2. The complex conjugate of a+bi is defined as a+bi=a−bi. Write a conjugate() method that returns the object’s complex conjugate as a new ComplexNumber object.
<br>3. Add the following magic methods:
<br>(a) Implement__str__()so that a+bi is printed out as(a+bj) for b≥0and(a-bj) for b <0.
<br>(b) The magnitude of a+bi is |a+bi|=√a2+b2. The__abs__() magic method determines the output of the built-in abs()function (absolute value). Implement__abs__()so that it returns the magnitude of the complex number.
<br>(c) Implement__eq__()so that two ComplexNumber objects are equal if and only if they have the same real and imaginary parts.
<br>(d) Implement__add__(),__sub__(),__mul__(), and__truediv__()appropriately. Each of these should return a new ComplexNumber object.
</td>
</tr>
</table>
<br><br>
<hr>
<i>source: ACME</i><br>
<i>credits: Maksym Petukhov, PMA-23, 2023</i>
