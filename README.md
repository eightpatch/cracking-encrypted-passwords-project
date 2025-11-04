# Benchmarking Password Cracking Speed
A CSC 450 Senior Research Project

---

## Project Objective
The objective of this project is to quantitatively measure and compare the cracking resistance of four common hashing algorithms: **SHA-256**, **bcrypt**, **scrypt**, and **Argon2**.

This benchmark evaluates each algorithm's vulnurability against brute-force and dictionary attacks.
* The **time** elapsed after the attack.
* The **percentage** of passwords successfully cracked within a time limit.

## Background
When a company database is breached, the security of its users' passwords depends entirely on how they are stored. Older, fast algorithms like **SHA-256** are now considered insecure for password storage. They are vulnerable to modern cracking hardware (GPUs) and can be broken quickly with brute-force or dictionary attacks.

Modern algorithms like **bcrypt**, **scrypt**, and **Argon2** were designed specifically to resist these attacks. They are intentionally slow and "memory-hard," which makes it significantly more expensive and time-consuming for an attacker to test guesses.

This project provides a clear, practical dataset to demonstrate exactly *how much* more secure these modern algorithms are compared to their legacy counterparts.

## Methodology
1.  **Hashing:** A "victim" list of 10,000 common passwords is hashed using Python scripts. This creates four separate hash files, one for each target algorithm.
2.  **Cracking Tool:** Hashcat is used to perform all cracking attempts.
3.  **Attacks Performed:**
    * **Brute-Force Attack**: A character mask (`'?a?a?a?a?a?a?a?a'`) is run against each hash set
    * **Dictionary Attack** : A separate "dictionary" list of 10,000 common passwords is run against each hash set
4.  **Measure:** Time elapsed and percentage of passwords cracked  

## Tools & Libraries Used
* **Python 3.11**
    * `hashlib`
    * `passlib`
    * `argon2_cffi` 
    * `bcrypt` 
* **Hashcat**
* **Datasets:** Two 10,000-password lists (one "victim" list, one "dictionary" list).
