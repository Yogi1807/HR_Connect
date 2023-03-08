"""
Write a program to get details of employees who's salary is > 9000. The output should
be in following format
"""


import csv
from pprint import pprint # for pretty print
from typing import Dict


def get_info(filename: str, value: int) -> Dict:

    with open(filename) as foo:
        emp = {}
        j = 1
        for i in csv.DictReader(foo):
            if int(i["SALARY"]) > value:
                emp[j] = {"Name": (i["FIRST_NAME"] + " " + i["LAST_NAME"]),
                          "email": i["EMAIL"], "Phone": i["PHONE_NUMBER"].replace(".", "")}
                j += 1

        return emp


if __name__ == "__main__":

    pprint(get_info("employees.csv", 9000))
