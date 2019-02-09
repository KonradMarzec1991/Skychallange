def phrases(filename):

    if not isinstance(filename, str):
        return 'Filename must be a string'
    try:
        with open(filename, 'r') as myfile:
            counter = 0
            for line in myfile:
                line = line.rstrip()
                words = line.split(" ")
                if len(words) == len(set(words)):
                    counter += 1
    except FileNotFoundError:
        print('File does not exist')
        return None
    except ValueError:
        print('Wrong format of file')
        return None

    return counter


# print(phrases('phrases.txt'))

# 383
