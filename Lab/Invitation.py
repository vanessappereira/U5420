""" Create a program that produces a formatted letter on standard output similar to the example given below. It should request the input of the information underlined, and any other necessary data. 
The first line and the last two lines ("Dear Alberto/Armanda", "Yours," and "Arnaldo Antunes") should be indented by 10 characters. The first line of each paragraph should be indented by 4 characters from the left margin. 
The dashed line should contain 20 dashes and be indented by 7 characters. It should include the line spacing indicated in the example: """

INDENT_GREETING = 10
INDENT_PARAGRAPH = 4
INDENT_NAME = INDENT_GREETING
INDENT_SEPARATOR = 7
SEPARATOR_CHAR = "-"
SEPARATOR_LENGTH = 20
INDENT_CLOSING = INDENT_GREETING

name = input("Enter your name: ").capitalize()
invitation = f"""
{INDENT_GREETING * ' '}Dear {name}

{INDENT_PARAGRAPH*' '}I hereby invite you to the ceremony to be held at 4:00 PM on May 31, 2036. 
Dear {name}, the dress code is formal, which means you should wear a suit and tie/dress and high heels. 

{INDENT_PARAGRAPH * ' '}May 31, 2036, is a very special date for me and we look forward to your presence. 
The invitation is extendable to your partner. 

{INDENT_PARAGRAPH * ' '}We await your confirmation 
{INDENT_CLOSING * ' '}Yours,
{INDENT_SEPARATOR * ' '}{SEPARATOR_CHAR * SEPARATOR_LENGTH}
{INDENT_NAME * ' '}Arnaldo Antunes """

print(invitation)