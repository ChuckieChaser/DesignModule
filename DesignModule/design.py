"""
    DOCUMENTATION: DESIGN MODULE                                   @ChuckieChaser

    Its purpose is to add modular design to console. It has both advance and basic
    concept of looping to reduce the redundancy of design implications.

    :============================== [ PROPERTIES ] ==============================:
    :consoleWidth (int):
        the width of the system that will be displayed inside a terminal or console

    :boldCount (int):
        serve as a counter for bold texts. Creating a dynamic adjustment whenever
        creating a bold text since they take up 8 spaces

    :Alignment (enum):
        text alignment for display function

    :============================== [ FUNCTIONS ] ===============================:
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

    :=============================== [ HISTORY ] ================================:
    12:50 | 10 / 03 / 2024
        Coded the basic functionality and the first iteration of the design module
        Started the documentation for better and clearer understanding
    15:14 | 10 / 04 / 2024
        Remove the bold text for header as it opposes the idea of modularity for this
        module

    :============================= [ KNOWN BUGS ] ===============================:
    1. Adding bold function to StringArgs parameter causes it to mismatch the alignment
       of edges
"""

# ========== [ IMPORTS ] ========== #
from enum import Enum
from typing import Dict, List

# ========== [ VARIABLES ] ========== #
consoleWidth: int = 50
boldCount: int = 0
class Alignment(Enum):
    LEFT = "ljust"
    CENTER = "center"
    RIGHT = "rjust"

# ========== [ FUNCTIONS ] ========== #
def bold(text: str) -> str:
    global boldCount
    boldCount += 1
    return f"\033[1m{text}\033[0m"

def divider() -> None:
    print(f"+{'-' * consoleWidth}+")

def display(*texts: str, alignment: Alignment = Alignment.CENTER) -> None:
    global boldCount
    for text in texts:
        print(f"|  {getattr(text, alignment.value)(consoleWidth - 4 + (boldCount * 8))}  |")
    boldCount = 0

def header(title: str, subtitle: str = "", alignment: Alignment = Alignment.CENTER) -> None:
    divider()
    display(title, alignment = alignment)
    if subtitle.strip() != "": display(subtitle, alignment = alignment)
    divider()

def selection(*texts: str) -> None:
    optionNumber: int = 1
    for text in texts:
        padding: int = max(len(text) + 5 for text in texts) - len(text)
        if text == texts[-1]: optionNumber = 0
        display(f"[ {optionNumber} ] {text}{' ' * padding}")
        optionNumber += 1
    divider()

def map(dictionary: Dict) -> None:
    options: List[str] = [f"[ {value } ] {option}" for value, (option, function) in dictionary.items()]
    padding: int = max(len(option) for option in options)
    for option in options:
        alignedOption = option.ljust(padding)
        display(alignedOption)
    divider()

# ========== [ SAMPLE ] ========== #
# def option1():
#   display("This is option 1")
#
# def option2():
#   display("This is option 2")
#
# dictionary = {
#   1: ("Option 1", option1),
#   2: ("Option 2", option2)
# }
#
# header("TITLE", "This is a subtitle")
# selection("Option 1", "Option 2", "Option 3", "Option 4", "Option 5",)
# display("This is a display")
# display("You", "can", "put", "series", "of", "strings", "here")
# header(bold("MAP"))
# map(dictionary)
# display("It will display just like the selection")
# divider()
