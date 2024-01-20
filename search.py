'''
searching for #includes within C and C++ files
'''


def parse_include(line: str) -> str:
    '''
    parse a line to find the header file included in a #include preprocessor
    directives. Note: function does not account for // comments and assumes
    #include calls are formatted as follows:

    #include "header.h"
    '''
    line = line.strip()
    qopen = line.find('\"')
    if qopen == -1 or qopen == len(str) - 1:
        raise ValueError('invalid formatting on preprocessor directive.')
    if line[len(line) - 1] != '\"':
        raise ValueError('invalid formatting on preprocessor directive.')
    return line[qopen:len(line)]


def strip_comment(line: str) -> str:
    ''' removes comments from a line of text '''
    return line[line.find("//"):]


def find_includes(file_name: str) -> [str]:
    with open(file_name, mode='r') as file:
        includes = []
        in_comment = False
        for line in file:
            if in_comment:
                if "*/" not in line:  # still inside of block comment
                    continue
                #  check for the close on the current line
                line = line[line.find("*/") + 2:]  # TODO check this bound
                in_comment = False

            # start of a block comment
            if "/*" in line:
                line = line[:line.find("/*")]
                includes.append(parse_include(line))
                in_comment = True
                continue

            line = strip_comment(line)  # remove any singe-line comments
            if '#includes' in line:
                includes.append(parse_include(line))
