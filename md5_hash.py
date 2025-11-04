import hashlib
import csv

input_file = 'common_passwords.csv'
output_file = 'hashed_passwords_md5.csv'

with open(input_file, 'r') as infile, \
     open(output_file, 'w') as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    for row in reader:
        password = row[0]
        hash_md5 = hashlib.md5(password.encode()).hexdigest()
        writer.writerow([hash_md5])
