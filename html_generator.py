def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title"><h3>
        ''' + concept_title
    html_text_2 = '''
    </h3></div>
    <div class="concept-description">
    ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('DESCRIPTION:')
    title = concept[start_location+6 : end_location-1]
    return title


def get_description(concept):
    start_location = concept.find('DESCRIPTION:')
    description = concept[start_location+13 :]
    return description

def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('TITLE:')
        next_concept_end   = text.find('TITLE:', next_concept_start + 1)
        concept = text[next_concept_start:next_concept_end]
        text = text[next_concept_end:]
    return concept
        

TEST_TEXT = """ TITLE: How the Web Works
DESCRIPTION: The web is a collection of user end devices, transport media, transport equipment and web servers. When an end user's device requests a web page it sends a HTTP request to a server. The server finds the appropriate HTML document and sends it back to the end user. Web browsing software installed on the device interprets the HTML code and displays it on the users screen.
TITLE: HTML Hypertext Markup Language
DESCRIPTION: HTML is used by the majority of web pages to display text documents. Hypertext is used to describe what you see. Markup describes how the page looks.
                        &#60;HTML&#62; tag indicates that anything between it and a closing HTML tag is HTML code.
                        &#60;BODY&#62; indicates anything between the opening tag and closing tag should be displayed in the browser window.
                        &#60;HEAD&#62; element contains the title of the page indicating what the page is about.
                        &#60;TITLE&#62; will be displayed in the browser above where you type the URL.
TITLE:Tags and Elements
DESCRIPTION: HTML uses elements to describe the structure of the pages. Each element has an opening tag and a closing tag.Tags act like containers, they tell you something about the information that lies between their opening and closing tags. 
TITLE: Why Computers are Stupid
DESCRIPTION:Computers are generally considered stupid because they require instructions to perform a function. They will perform those instructions literally even if those instructions are incorrect. This is why even a small programming mistake can cause big problems.
TITLE: Inline vs Block Elements
DESCRIPTION:Inline elements flow within the text and do not start on a new line i.e. &#60;img&#62;, &#60;em&#62;, and &#60;span&#62;.Block elements look like they start on a new line i.e. &#60;h1&#62; - &#60;h6&#62;, &#60;p&#62;, &#60;div&#62; tags.
                       


TITLE: Developer Tools
DESCRIPTION: HTML elements are either inline or block. Block elements form an invisible box around the content inside of them. 
TITLE: HTML's "tree-like" Structure
DESCRIPTION:HTML elements when grouped together in an HTML document form a tree like structure. Elements can contain other elements inside of them. When you look at the document in developer tools you can see this tree like structure that expands when you drill down deeper into the file structure.
TITLE: Indentations and Boxes
DESCRIPTION: Following the flow of an HTML document you can look at the structure. The more indented the element tag is the more deeply the box is nested.
TITLE: Text Editors
DESCRIPTION: Text editors are used to write code. Some text editors will even auto correct your code by adding a closing tag or automatically bring up a list of parameter suggestion.                    
             

                            
TITLE: Adding Style
DESCRIPTION: CSS allows you to create rules that specify how the content of an element should appear. You can imagine every HTML element is surrounded by an invisible box. CSS allows you to specify background color, font, padding, etc.
TITLE: Understanding CSS
DESCRIPTION: CSS works by associating rules with HTML elements. This governs how the content of the specific element should be displayed. A CSS rule contains two parts a selector and a declaration. Within the declaration you have a property and a value.
TITLE: Thinking About Cascading
DESCRIPTION: A simple web page should contain two documents an HTML file and a CSS file. HTML uses the link element to indicate where the CSS file is located i.e 
TITLE: Helpful Sites:
                        
DESCRIPTION: <a href="https://developer.mozilla.org/en-US/docs/Web/CSS" target="_blank"> Mozilla Developer Network</a>
<a href="http://css-tricks.com/" target="_blank">CSS-Tricks</a></h3>
<a href="http://stackoverflow.com/" target="_blank">StackOverflow</a></h3>
<a href="http://validator.w3.org/#validate_by_input" target="_blank">HTML Validation Checker</a>
<a href="http://jigsaw.w3.org/css-validator/" target="_blank">CSS Validation Checker</a>
                    
                            
                               
TITLE: Computers
DESCRIPTION: Computers have a limited instruction set. They are dumb devices that only function when giving a specific intruction set. Programs tell computers how to function and what actions to perform. Like the lecture pointed out, computers can do almost anything computational as long as there is a program instructing it how to perform.
TITLE: Programming Languages
DESCRIPTION: There are many different programming laugauges, but what they all have in commoning is a basic structured syntax. We have programming languages because if we wanted to tell a computer what to do in plain English it would be very verbious, and the instructions would have ambiguity. Programming languages are concise and it takes alot less wording or syntax to right an instruction.
TITLE: Iterpreters 
DESCRIPTION: Interpreters are basically translators for the programming language that you have written. It takes a high level programming language and interprets it into something that the computer can understand. Python is a high level programming language that uses an interpreter to tell a computer or device what to do. 
                                

TITLE: Variables
DESCRIPTION: Variables in Python are basically a container that is assigned a value. A vairiable can contain a numeric value or a character value such a string. A variable is assigned a value with the equal sign. We first declare a variriable such as: how_many_days, we then can assign a value to the declared variable i.e. 10 days by how_many_days=10; The difference between the equal sign in mathamatics is that in mathamatics it is the anwser it will not change and it can not be reused. The equal sign in Python assigns a variable a value to be displayed or reused and can change many times.
TITLE: Strings
DESCRIPTION: Strings in Python are declared in either single or double quotation marks. In order to be valid the starting and ending quotations need to match. The .find command is a procedure in Python that allows you to search strings. You can enter parameters to narrow your search results. The difference between 2+2 and "2"+"2" is that one is a math problem and will give you 4, while the other in adding two string together which will give you 22.
                                
                                    
TITLE: What is a functions
DESCRIPTION: A function is a block of usable code that performs an operation and returns a value. A function is defined by the keyword 'def' which is followed by operands. The basic syntax of a function is: def &#60prcedure&#62(&#60input&#62,&#60input&#62, ...) To use a function you must call the procdure using the keyword and pass the expected number of inputs.
TITLE: Difference between Making and Using a Function
DESCRIPTION: The between making and using a function is that when making a function you define the operation and the inputs required. After a funtion is defined and the required results are acceptable you can begin to use the function within a program. You use the function by calling the procedure and supplying the necessary data as iputs required for function to proceed.
TITLE: How do Functions Help to Avoid Repetition
DESCRIPTION: Functions help programmers avoid repetition by allowing code to be reused.You do not need to write the code over and over again everytime you need to perform a function. Code can be created in the form of a function and can be called within a program when needed. This way you only have to write the code once, and ofte times the function has already been written enabling you to no have to write it from scratch.
TITLE: What happens if a Function Does Not Have a Return Statement
DESCRIPTION: When a function does not have a return statement the procedure does not return a value. Even though a function is called and the necessary input may be supplied the function will process the data. But if the return statement is not issued that data from the function will not be usable. No data will be outputted from that function.
TITLE: Equality Comparisons
DESCRIPTION: Equality comparisons return a boolean value. True if comparison is correct and false if cmparison is not correct. Equality comparisons less than or greater than, equal or not equal, less than or equal to and greater than and equal to. 
TITLE: If Statements
DESCRIPTION: If statements are composed of a test expression and a block of code that is implemented if the comparison is true.<br> General syntax is:<br>
                    if condition:<br>
                        indented statement block<br>
                    If statement is true do the indented program block, if false skip program statement. There are also if else statements that can test multiple test expressions, if one statement is not true it goes to the next if else statement and test the expression if it's true the program block will be implemented.
TITLE: While Loops
DESCRIPTION: A while loop repeatedly implements the program statement as long as the condition is true. The while loop stops and proceeds to the next line of code when the while condition becomes false.
                    If the condition is untrue the first time it is tested the while loop will never run. On the other hand if the condition is always true and never false the program will run infinitely.
                    You can add a break statement if you want the program to stop. You can add a break in the while code to make the condition false and end the While Loop, moving to the next line of code.
TITLE: Structured Data
DESCRIPTION: Python allows data to be structured in different ways. It really depends on what the data is and what kind of data operations will be performed. Python allows for lists to be created. List are very versatile and allow different types data to be contained within the elements. List indices start at zero and can be sliced, concatenated, and munipulated. They have a lot of similarities with strings but the data contained is mutable.
TITLE: Mutability
DESCRIPTION: Mutable means that data can be change, immutable data cannot change it is a constant. List are mutable allowing for change this works well in the munipulation of the data. String object cannot be changed, lists can be changed.
                    Append will and the elements to the list. Adding list to an existing list will and the elments to the list in a element at the end of the list pointing to the new added elements to the list.

"""
 

def generate_all_html(text):
    current_concept_number = 1
    concept = get_concept_by_number(text, current_concept_number)
    all_html = ''
    while concept != '':
        title = get_title(concept)
        description = get_description(concept)
        concept_html = generate_concept_HTML(title, description)
        all_html = all_html + concept_html
        current_concept_number = current_concept_number + 1
        concept = get_concept_by_number(text, current_concept_number)
    return all_html

print '''<!DOCTYPE html>
        <html>
            <head>
            <link rel="stylesheet' type="text/css"
            href="readable.css"><meta http-equiv="content-type" content="text/html; charset=UTF-8">
            </head>
            <body>
            '''
print generate_all_html(TEST_TEXT)

print '''</body>
        </html>
        '''

