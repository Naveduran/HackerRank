"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
Given a full name, your task is to capitalize the name appropriately.

Input Format
A single line of input containing the full name.

Constraints
The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.
"""

def capitalize(s):
    lower = s.lower()
    response = ""
    lenght = len(s)
    for i in range(lenght):
        if i==0 and lower[i].isalpha():
            response += lower[i].upper()
        elif lower[i].isalpha() and lower[i-1].isspace():
            response += lower[i].upper()
        else:
            response += lower[i]
    return response
