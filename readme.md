<h1>Python Labs</h1>
<hr>
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
<br><br>
<hr>
<i>source: ACME</i><br>
<i>credits: Maksym Petukhov, PMA-23, 2023</i>
