import re


def parse(line):
    while '\x7f' in line:
        line = line.replace("\x7f", '')

    # remove []
    notes = re.finditer(r'\[[^)]*\]', line)
    if notes:
        for note in notes:
            line = line.replace(note.group(), '')

    # remove ()
    # notes = re.finditer(r'\([^)]*\)', line)
    # if notes:
    #     for note in notes:
    #         line = line.replace(note.group(), '')

    tokens = line.split('  ')
    if len(tokens) < 2:
        return
    if 'prefix' in tokens[1] or 'abbr.'  in tokens[1]:
        return

    return tokens[0], (' '.join(tokens[1:]))


def parse_dict_from(lines):
    data = {}
    for line in lines:
        values = parse(line)
        if values:
            data[values[0]] = values[1]
    
    output = []
    for key, val in data.items():
        output.append([key, val])
    return output


def get_dictionary_into_list():
    filename = 'Oxford English Dictionary.txt'
    file = open(filename, 'r').read().split('\n')
    data = parse_dict_from(file)
    return data


if __name__ == '__main__':
    get_dictionary_into_list()