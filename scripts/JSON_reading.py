def parse_json(filename):

    if not isinstance(filename, str):
        return 'Filename must be a string'
    try:
        with open(filename, 'r') as myfile:
            line = str(myfile.readlines())
            result = 0
            temp = ""

            for key, value in enumerate(line):

                """
                This condition could generate error if first in row is any digit, 
                but not in format of JSON 
                """

                if value.isdigit() or value == "-":
                    if key < len(line) - 1 and line[key + 1].isdigit():
                        temp += line[key]
                    else:
                        temp += line[key]
                        result += int(temp)
                        temp = ""

    except FileNotFoundError:
        print('File does not exist')
        return None
    except ValueError:
        print('Wrong format of file')
        return None

    return result


# print(parse_json('jsonreading.txt'))

# 111754
