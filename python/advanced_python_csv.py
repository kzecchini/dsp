import csv
from advanced_python_regex import Faculty


def write_emails(data):
    '''
    Given an initial csv file, will create a list of emails and write those
    to a new csv file with the title 'emails.csv'.
    '''
    original_csv = Faculty(data)
    emails = original_csv.emails()
    f = open('emails.csv', 'w')
    fieldnames = ['email']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for email in emails:
        writer.writerow({'email': email})
    f.close()

write_emails('faculty.csv')
