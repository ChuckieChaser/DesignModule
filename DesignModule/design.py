'''
    DOCUMENTATION: DESIGN MODULE                                   @ChuckieChaser

    Its purpose is to add modular design to console. It has both advance and basic
    concept of looping to reduce the redundancy of design implications.

    :============================== [ PROPERTIES ] ==============================:
    :console_width (int):
        the width of the system that will be displayed inside a terminal or console

    :format_text (int):
        serve as a counter for ANSI texts. Creating a dynamic adjustment whenever
        the user wants to create ANSI related text since they take up atleats 8
        spaces for some reason. +1 if is colored

    :Alignment (enum):
        text alignment for display function

    :ErrorType (enum):
        types of error that could be encounter during runtime

    :============================== [ FUNCTIONS ] ===============================:
    :divider (none):
        creates a border line that separates content to content

    :display (string..., alignment):
        display a text that will perfectly align with the system. Its alignment
        can be change but the default is center. You can set multiple series of strings
        inside

    :header (string, string, alignment):
        display a title or a heading for the system. Along with it comes a subtitle that,
        by default, is null. It already has dividers inside

    :selection (string...):
        processes string arguments and display it in a tidy manner. By default, it will
        present it in the middle with full content alignment to other options

    :map (dictionary):
        processes dictionary items and display it in a tidy manner. By default, it will
        present it in the middle with full content alignment to other options. It also has
        this niche functionality that calls the function inside the dictionary by using
        tuple

    :============================== [ UTILITIES ] ===============================:
    :error (ErrorType):
        display a header with a message of error, similar to what header does but for error
        handling with additional input like pause function

    :isEmpty (Data Structure):
        returns True if the content of the target data structure is empty. False if otherwise

    :pause (none):
        uses command line to pause the terminal

    :clear (none):
        uses command line to clear the terminal

    :=============================== [ HISTORY ] ================================:
    00:50 | 10 / 03 / 2024
        Coded the basic functionality and the first iteration of the design module
        Started the documentation for better and clearer understanding
    15:14 | 10 / 04 / 2024
        Remove the bold text for header as it opposes the idea of modularity for this
        module
    15:21 | 10 / 06 / 2024
        Fixed the issue of calling the bold function inside functions with StringArgs
        as parameter, except for the selection and map. Since it takes the max length
        of whichever is the longest. Bold adds like 8 white spaces for some reason so
        adding bold to those 2 would mismatch the alignment of the options but not the
        edges
    18:30 | 10 / 06 / 2024
        Added utilities inside the design module. These are helpers for added functionality
        and reduce redundancy when invoking things like cls and pause
    00:32 | 10 / 08 / 2024
        Followed the naming convention of python! Along with the Color Update. Right now,
        colors are Red Green and Blue. I also removed the bold function as the new 'escape'
        character is now implemented

        B/ {text} /> = bold
        x/ {text} /> = Red Blue Green ? (r) (g) (b)

        E.G
            B/HELLO/>       :   will produce BOLDED HELLO
            r/I AM RED/>    :   will produce Color Red I AM RED
            g/I AM GREEN/>  :   will produce Color Green I AM GREEN

    :============================= [ KNOWN BUGS ] ===============================:
    1. Bold() -> StringArgs (FIXED... Kinda)
        Adding bold function to StringArgs parameter causes it to mismatch the alignment
        of edges
'''

# ========== [ IMPORTS ] ========== #
from enum import Enum
from typing import List, Union
import os

# ========== [ VARIABLES ] ========== #
console_width: int = 50
format_text: int = 0

class Alignment(Enum):
    LEFT = 'ljust'
    CENTER = 'center'
    RIGHT = 'rjust'

class ErrorType(Enum):
    VALUE = 'Invalid Input!'
    BOUND = 'Out of Bound!'
    SIZE = 'Input length is not within Range!'

# ========== [ FUNCTIONS ] ========== #
def divider() -> None:
    print(f'+{'-' * console_width}+')

def display(*texts: str, alignment: Alignment = Alignment.CENTER) -> None:
    global format_text

    for text in texts:
        format_offset: int = 8

        if 'B/' in text and text.endswith('/>'):
            text = text.replace('B/', '\033[1m', 1).replace('/>', '\033[0m', 1)
            format_text += 1
        if 'r/' in text and text.endswith('/>'):
            text = text.replace('r/', '\033[91m', 1).replace('/>', '\033[0m', 1)
            format_text += 1
            format_offset += 1
        if 'g/' in text and text.endswith('/>'):
            text = text.replace('g/', '\033[92m', 1).replace('/>', '\033[0m', 1)
            format_text += 1
            format_offset += 1
        if 'b/' in text and text.endswith('/>'):
            text = text.replace('b/', '\033[94m', 1).replace('/>', '\033[0m', 1)
            format_text += 1
            format_offset += 1

        print(f'|  {getattr(text, alignment.value)(console_width - 4 + (format_text * format_offset))}  |')
        format_text = 0

def header(title: str, subtitle: str = '', alignment: Alignment = Alignment.CENTER) -> None:
    clear()
    divider()
    display(title, alignment = alignment)

    if subtitle.strip() != '': display(subtitle, alignment = alignment)

    divider()

def selection(*texts: str) -> None:
    option_number: int = 1

    for text in texts:
        padding: int = max(len(text) + 5 for text in texts) - len(text)

        if text == texts[-1]: option_number = 0

        display(f'[ {option_number} ] {text}{' ' * padding}')
        option_number += 1

    divider()

def map(dictionary: dict) -> None:
    options: List[str] = [f'[ {value } ] {option}' for value, (option, _) in dictionary.items()]
    padding: int = max(len(option) for option in options)

    for option in options:
        alignedOption = option.ljust(padding)
        display(alignedOption)

    divider()

# ========== [ UTILITIES ] ========== #
def error(type: ErrorType = ErrorType.VALUE) -> str:
    clear()
    header(f'ERROR: {type.value}')
    pause()
    clear()

def isEmpty(object: Union[list, tuple, set, dict]) -> bool:
    if len(object) == 0: return True
    return False

def pause() -> None:
    os.system('pause')

def clear() -> None:
    os.system('cls')
