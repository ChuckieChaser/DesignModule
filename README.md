DOCUMENTATION: DESIGN MODULE                                   @ChuckieChaser

Its purpose is to add modular design to console. It has both advance and basic
concept of looping to reduce the redundancy of design implications.

[ PROPERTIES ] 

:consoleWidth (int):
  the width of the system that will be displayed inside a terminal or console

:boldCount (int):
  serve as a counter for bold texts. Creating a dynamic adjustment whenever
  creating a bold text since they take up 8 spaces

:Alignment (enum):
  text alignment for display function

[ FUNCTIONS ] 

:bold(string):
  creates a bold text. Take note that it will take atleast 8 spaces

:divider(none):
  creates a border line that separates content to content

:display(string..., alignment):
  display a text that will perfectly align with the system. Its alignment
  can be change but the default is center. You can set multiple series of strings
  inside

:header(string, string, alignment):
  display a title or a heading for the system. Along with it comes a subtitle that,
  by default, is null. It already has dividers inside

:selection(string...):
  processes string arguments and display it in a tidy manner. By default, it will
  present it in the middle with full content alignment to other options

:map(dictionary):
  processes dictionary items and display it in a tidy manner. By default, it will
  present it in the middle with full content alignment to other options. It also has
  this niche functionality that calls the function inside the dictionary by using
  tuple

[ HISTORY ] 

12:50 | 10 / 03 / 2024
  Coded the basic functionality and the first iteration of the design module
  Started the documentation for better and clearer understanding
15:14 | 10 / 04 / 2024
  Remove the bold text for header as it opposes the idea of modularity for this
  module

[ KNOWN BUGS ] 

1. Adding bold function to StringArgs parameter causes it to mismatch the alignment of edges
