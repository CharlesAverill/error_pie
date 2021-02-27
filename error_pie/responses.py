unsure = [
    "What did you do??? D:",
    "I don't know what happened <:(",
    "What do you think went wrong? O.O",
]

math = [
    "Hmmm... numbers????? D:",
    "Da plusses and minuses... they hurt my brain OwO",
    "Maybe a calculator will help! :D",
]

buffer = ["Oh noes!! The memowy!! X_X", "Hmmm... no bites here! I mean bytes xD"]

cant_find = ["*Gasps* I can't find it T_T", "It's not there... I'm gonna cwy ;_;"]

false_assert = [
    "Hmmm... looks like you failed this test :( but you'll get it next time! :D",
    "That's not right! :-?",
]

attribute = [
    "Hehe that thing can't do that you dumbo! xD",
    "What are you doing with that?? O_O",
]

eof = ["Da file is gone!!!! :O", "Where'd that thing go??? :-?"]

floating_point = [
    "zero dot zero zero zero zero zero zero zero zero zero zero zero ... one ;D",
    "So many floating points 0o0",
]

generator = ["There goes your generator :(", "Who turned off the lights?? D:"]

import_error = [
    "Looks like there was a problem with that import OwO",
    "Try again ...fufufu... B)",
]

module_not_found = [
    "You silly goose ('^3^) there's no module with that name!",
    "Are you suuuure that that module exists? o.o?",
]

index = ["Ouchie! That slice hurt ;~;", "That object isn't as long as you think :/"]

key = ["Oh noes my key is gone!!! /0_0\\", "I can't find my keys T_T"]

keyboard = [
    "Ouch! Don't be so rough >:(",
    "Bye bye :(",
    "Wow... I thought you liked me T_T",
]

memory = [
    "010101000110100001100101001000000111011101100001011011000110110001110011001000000110000101110010011001010010000001"
    "100011011011000110111101110011011010010110111001100111001000000110100101101110001000000010000101001111011011100100"
    "111100100001",
    "I forgot... <O_O>",
    "W-where am I?",
    "Who are you OwO",
]

name = ["What da heck is that??? xD", "Never heard of her UwU"]

not_implemented = ["Go make that method right now >:(", "You forgot this :-P"]

os = ["Da computer didn't like dat O.O", "I hope your compuwuter is okay >w<"]

overflow = [
    "OMGBBQ THAT NUMBER IS SO BIG :-( )",
    "I can't even see the end of it!! OnO",
]

recursion = [
    "*echoing* uhhh... where are we??? <O_O>",
    "It's like a big tunnel! We must be at the bottom... U_U",
]

reference = [
    "Didn't you hear the garbage truck go by? They already picked up that object! ('^-^)",
    "The garbage truck just left!! Go try and catch it!!! ('O_O)",
]

general = [
    "Something broke T_T what do you think it is?",
    "What even is a runtime :-?",
    "Da pwogwam made a oopsie woopsie xD",
]

stop = ["STOP STOP STOP THERE'S NO MORE ('OnO)", "Where did everything go??? :("]

syntax = [
    "You spelled that wrong X-D",
    "You... might want to check your grammar there =^D",
]

indent = ["No no no put it back!!! <o_o>", "Should that be over there??? xD"]

tab = ["You can't mix those :/", "Just pick one -_-+"]

type_error = ["I don't think that object can do that O_O", "Good luck with that xD"]

unbound_local = [
    "I don't see a variable like that around here... -_-",
    "Try again, bub. There aren't any variables with that name! >:-(",
]

unicode = ["What language is that??? =O", "Did you type something wrong? :s"]

value = [
    "I don't think that object has the right stuff xD",
    "Apples and Oranges ('O_O)",
]

zero = ["Try a limit next time (-_-+)", "What is this, a Numberphile video??? -_-"]

exec_types_pairs = {
    BaseException: unsure,
    Exception: unsure,
    ArithmeticError: math,
    BufferError: buffer,
    LookupError: cant_find,
    AssertionError: false_assert,
    AttributeError: attribute,
    EOFError: eof,
    FloatingPointError: floating_point,
    GeneratorExit: generator,
    ImportError: import_error,
    ModuleNotFoundError: module_not_found,
    IndexError: index,
    KeyError: key,
    KeyboardInterrupt: keyboard,
    MemoryError: memory,
    NameError: name,
    NotImplementedError: not_implemented,
    OSError: os,
    OverflowError: overflow,
    RecursionError: recursion,
    ReferenceError: reference,
    RuntimeError: general,
    StopIteration: stop,
    StopAsyncIteration: stop,
    SyntaxError: syntax,
    IndentationError: indent,
    TabError: tab,
    SystemError: general,
    SystemExit: keyboard,
    TypeError: type_error,
    UnboundLocalError: unbound_local,
    UnicodeError: unicode,
    UnicodeEncodeError: unicode,
    UnicodeDecodeError: unicode,
    UnicodeTranslateError: unicode,
    ValueError: value,
    ZeroDivisionError: zero,
}

NOT_SUBSCRIPTABLE = [
    "You silly dumbo, you can't subscript that! （'^▿^）",
    "Awww, numbers aren't lists! Try again ;)",
]
