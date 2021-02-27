import random
import sys
import traceback

from .responses import exec_types_pairs


def matches(string, pattern):
    for string_val, pattern_val in zip(string.split(" "), pattern.split(" ")):
        if string_val != pattern_val and pattern_val != "<pie_skip>":
            return False
    return True


def random_from(responses):
    return random.choice(responses)


def print_tb_exit(tb, value):
    tb_lines = traceback.format_tb(tb)[0].split("\n")
    [print(line) for line in tb_lines[:-1]]
    print(value)


def pie_catch(exctype, value, tb):
    if exctype in exec_types_pairs.keys():
        print_tb_exit(tb, value)
        print(random_from(exec_types_pairs[exctype]))
        return
    else:
        if exctype.__base__ is not Exception:
            new_exctype = exctype.__base__
            for key, val in exec_types_pairs.items():
                if key is new_exctype:
                    print_tb_exit(tb, value)
                    print(random_from(exec_types_pairs[new_exctype]))
                    return
    print("This error looks funny O_O")
    print_tb_exit(tb, value)


sys.excepthook = pie_catch
