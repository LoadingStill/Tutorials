# Goals  

## Lessons
### Printing  
Printing is done with the print command  
`print ("Hello world!")`  
Printing will remove the `""` when used to print string (text), not code.  
`""` Shows the beginning and the end of a string.  


`print("Hello world!\nHello World!")`
This line of codeprints 2 lines. `\n` means to start a new line   
The output is    
```
Hello World!
Hello World!
```

`print("Hello" + "Ryan")`
Will print `HelloRyan`
There is no space to the end of Hello, the beginning of Ryan or added in the middle.  So there will be no space outputted.  



Input and printing can be done on the same line or on seprate lines, these have the same end, but get to the end in different but simmilar ways.

`name=input("What is you name? ")  
print(len(name))`

`print('Hello ' + input('What is your name?') + "!")`


### Commenting  
```
print ("Hello world!")
# this is a comment
```
This output will be, `Hello world!`
Comments in Python are preceded by a #.  
Comments do not have to be on their own line you can put it after a line of code, it can look nicer to you to do it that way so either way is fine.  

```
print ("Hello world!") # this is a comment
```
This block of code will print, `Hello World!`  
Nothing will follow it. Comments are not shown anywhere expect in the source code.  The output omits coments.



### Debugging  
```
print ("Hello world!)

Error:
  File "main.py", line 2
    print ("Hello world!)
                        ^
SyntaxError: EOL while scanning string literal
```
You can solve this error by copying the line, "SyntaxError: EOL while scanning string literal" and paste that into google.  
This error is because there is a missing " between, ! and ).


### Sting Manipulation  


### Variables  
```
name = input("What is your name? ")
print(name)
```
This will print the name you input.  Name is a variable in this code.





## Project - Band Name Generator
Sudo Code:  
```
print, "Welcome to the Band Name Generator."
print, "What is the name of the city you grew up  in?"
user input {{city}}
print, "what is your pet's name?"
user input {{pet}}
print, "Your band name could be {{city}} {{Rabbit}}.
```
