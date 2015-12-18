import re


class Faculty(object):

    def __init__(self, data):
        self.data = data

    def find_degrees(self):
        '''
        Finds degrees held by the professors from a textfile. Returns a dictionary of
        unique degrees with a value of the frequency. For those with multiple degrees,
        they are split and counted seperately. Ex. MD PhD would count MD +1 and PhD +1.
        '''
        f = open(self.data, 'r')
        degrees = re.findall(r'[\w\s]+,([\w\.\s]+),[\w\s]+Biostatistics', f.read())
        f.close()
        res = {}
        for degree in degrees:
            temp = degree.strip().translate(None, '.').split(' ')
            for el in temp:
                if el in res:
                    res[el] += 1
                else:
                    res[el] = 1
        return res

    def find_titles(self):
        '''
        Finds titles in Biostatistics from a textfile. Returns a dictionary of
        unique titles with a value of the frequency.
        '''
        f = open(self.data, 'r')
        titles = re.findall(r',([\w\s]+)\s\w+\sBiostatistics', f.read())
        f.close()
        res = {}
        for title in titles:
            if title in res:
                res[title] += 1
            else:
                res[title] = 1
        return res

    def find_emails(self):
        '''
        Finds emails in a csv file. Returns two parts - the username and domain
        in a touple ('username', 'domain').
        '''
        f = open(self.data, 'r')
        pairs = re.findall(r'([\w\.-]+)@([\w\.-]+)', f.read())
        f.close()
        return pairs

    def emails(self):
        '''
        Returns a list of emails from the csv.
        '''
        pairs = self.find_emails()
        res = [pair[0] + '@' + pair[1] for pair in pairs]
        return res

    def unique_domains(self):
        '''
        From the csv, finds all unique email domains.
        '''
        pairs = self.find_emails()
        res = []
        for pair in pairs:
            if not pair[1] in res:
                res.append(pair[1])
        return res

# test = Faculty('faculty.csv')
# print test.find_degrees()
# print test.emails()
# print test.unique_domains()
# print test.find_titles()
