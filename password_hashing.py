import hashlib
from passlib.hash import argon2, bcrypt, scrypt
import csv

top_passwords = 'common_passwords.csv'
output_sha256 = 'hashed_passwords_sha256.csv'
output_argon2 = 'hashed_passwords_argon2.csv'
output_bcrypt = 'hashed_passwords_bcrypt.csv'
output_scrypt = 'hashed_passwords_scrypt.csv'

with open(top_passwords, 'r') as infile, \
     open(output_sha256, 'w') as sha256_outfile, \
     open(output_argon2, 'w') as argon2_outfile, \
     open(output_bcrypt, 'w') as bcrypt_outfile, \
     open(output_scrypt, 'w') as scrypt_outfile:
    reader = csv.reader(infile)
    sha256_writer = csv.writer(sha256_outfile)
    argon2_writer = csv.writer(argon2_outfile)
    bcrypt_writer = csv.writer(bcrypt_outfile)
    scrypt_writer = csv.writer(scrypt_outfile)
    for row in reader:
        password = row[0]
        hash_sha256 = hashlib.sha256(password.encode()).hexdigest()
        hash_argon2 = argon2.hash(password)
        hash_bcrypt = bcrypt.hash(password[:72])
        hash_scrypt = scrypt.hash(password)
        sha256_writer.writerow([hash_sha256])
        argon2_writer.writerow([hash_argon2])
        bcrypt_writer.writerow([hash_bcrypt])
        scrypt_writer.writerow([hash_scrypt])