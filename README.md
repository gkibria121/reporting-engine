
befor start install the packages by clicking install.cmd



Variable Declaration:

1. Variables must start with the symbol '$', and their values can be expressions that will be evaluated.
2. Expressions can use previously assigned variables, allowing for recursive operations.
3. Variables can be declared with values of any type, including objects and lists. To include expression values within an object, the 'eval()' function should be used. For example: `$list = [eval(1+2),'1+2']`.
4. Previously assigned variables can be used within lists or objects.
5. Table data can be inserted into a variable using JSON format.
6. Comments can be added using '#' for single-line comments and '/* ... */' for multiple lines.

Report Engine:

1. Use '{{$variable}}' to print the value of an integer or float variable.
2. Use '{{$variable : format_rule }}' to print a formatted value of a variable.
3. Use '{{$variable.value()}}' to print the value of an object or string variable.
4. Use '{%python%} ... {%endpython%}' to include Python code. Declare variables within the code using '{{$variable}}' or '{{$variable.value()}}'.
5. Use '{{% ... %}}' to include Python code directly.
6. Operations such as 'avg()', 'min()', 'max()', 'sum()', 'count()' ,'len()', 'reverse()' ,'index()', 'map()', 'set()', 'distinct()' can be performed. Filter operations can be done using arrow functions. For example: 'sum((x)=>x>1)'.

Report Engine Examples:

