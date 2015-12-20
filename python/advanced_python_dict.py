# I used two methods to solve this problem - the first using regular expressions and the second using the csv module.
# I think that using csv is a simpler approach, however I had all of the regular expressions already worked out from
# advanced_python_regex.py. It was a good exercise to piece them together to parse through the lines effectively.
# I left the csv approach as my final submission with the regex approach commented out.


# import re

# def regex_make_dict(data):
#     f = open(data, 'r')
#     tuples = re.findall(r'([\w]+)\s*,\s*([\w\.\s]+),([\w\s]+)\s\w+\s*Biostatistics\s*,\s*([\w\.-]+@[\w\.-]+)', f.read())
#     f.close()
#     faculty_dict = {}
#     for row in tuples:
#         if row[0] in faculty_dict:
#             faculty_dict[row[0]].append(list(row[1:]))
#         else:
#             faculty_dict[row[0]] = [list(row[1:])]
#     return faculty_dict


# def regex_make_dict2(data):
#     f = open(data, 'r')
#     tuples = re.findall(r'\n([\w\.\-\(\)\s]+)\s([\w]+)\s*,\s*([\w\.\s]+),([\w\s]+)\s\w+\s*Biostatistics\s*,\s*([\w\.-]+@[\w\.-]+)', f.read())
#     f.close()
#     faculty_dict = {row[:2]: list(row[2:]) for row in tuples}
#     return faculty_dict

import csv


def csv_make_dict(data):
    '''
    Answer to Q6. Creates dictionary from csv input with keys and values as
    Last_Name: [[Degree, Title, Email]]. For people with the same last name,
    appends the list of information to correspond to the key.
    Ex. Ellenberg: [[' Ph.D.', 'Professor', 'sellenbe@upenn.edu'], [' Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']]

    '''
    f = open(data, 'rU')
    parsed_list = [row for row in csv.reader(f)]
    f.close()
    del parsed_list[0]
    for line in parsed_list:
        line[0] = line[0].split()[-1]
        line[2] = ' '.join(line[2].split()[:-2])
    faculty_dict = {}
    for line in parsed_list:
        if line[0] in faculty_dict:
            faculty_dict[line[0]].append(line[1:])
        else:
            faculty_dict[line[0]] = [line[1:]]
    return faculty_dict


def csv_make_dict2(data):
    '''
    Answer to Q7 and Q8. Creates dictionary from csv input with keys and values as
    (First, Last): [Degree, Title, Email].
    '''
    f = open(data, 'rU')
    parsed_list = [row for row in csv.reader(f)]
    f.close()
    del parsed_list[0]
    for line in parsed_list:
        names = line[0].split()
        line[0] = (' '.join(names[:-1]), names[-1])
        line[2] = ' '.join(line[2].split()[:-2])
    faculty_dict = {line[0]: line[1:] for line in parsed_list}
    return faculty_dict


def print_dict(dic, last_Name=None):
    '''
    Sorts dictionaries by key. If last_Name, will sort by last tuple then
    first tuple in the key.
    '''
    if last_Name:
        for key in sorted(dic.keys(), key=lambda x: (x[-1], x[0])):
            print '%s: %s' % (key, dic[key])
    else:
        for key in sorted(dic.keys()):
            print '%s: %s' % (key, dic[key])

# Testing:

test1 = csv_make_dict('faculty.csv')
test2 = csv_make_dict2('faculty.csv')
# test1 = regex_make_dict('faculty.csv')
# test2 = regex_make_dict2('faculty.csv')
print_dict(test1)
print_dict(test2)
print_dict(test2, last_Name=True)
