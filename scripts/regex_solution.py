import re


def parse_json(filename):
    if not isinstance(filename, str):
        return 'Filename must be a string'
    try:
        with open(filename, 'r') as myfile:
            line = str(myfile.readlines())
            list_nums = re.findall('[+-]?\d+(?:\.\d+)?', line)

    except FileNotFoundError:
        print('File does not exist')
        return None
    except ValueError:
        print('Wrong format of file')
        return None

    list = [int(i) for i in list_nums]

    return sum(list)


# print(parse_json('jsonreading.txt'))

# 111754