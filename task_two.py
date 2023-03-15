"""
Write a program to get "HIRE DATE" of employee who's department id within range 30
to 110 AND who's salary is > 4200.
"""

import csv
from typing import Dict
from datetime import datetime
from pprint import pprint


def joining_date(less: int, greater: int, salary_: int) -> Dict[str, list]:
    with open("employees.csv") as bar:
        information = {}
        for info in csv.DictReader(bar):
            if less <= int(info['DEPARTMENT_ID']) < greater and int(info["SALARY"]) > salary_:
                ti = datetime.strptime(info["HIRE_DATE"], "%d-%b-%y")
                time = ti.strftime("%Y-%m-%d")
                if time not in information:
                    information[time] = [info["FIRST_NAME"] + " " + info["LAST_NAME"]]
                else:
                    information[time].append(info["FIRST_NAME"] + " " + info["LAST_NAME"])

        return information


if __name__ == "__main__":

    pprint(joining_date(30, 110, 4200))