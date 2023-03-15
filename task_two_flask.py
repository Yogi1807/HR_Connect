from my_utils.csv_ import HandleCSV
from typing import Dict
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

bar = HandleCSV.read_entire_csv()


@app.route('/joining_date/<int:less>/<int:greater>/<int:salary_>')
def joining_date(less: int, greater: int, salary_: int) -> str:
    information = {}

    for info in bar:
        if less <= int(info['DEPARTMENT_ID']) < greater and int(info["SALARY"]) > salary_:
            ti = datetime.strptime(info["HIRE_DATE"], "%d-%b-%y")
            time = ti.strftime("%Y-%m-%d")
            if time not in information:
                information[time] = [info["FIRST_NAME"] + " " + info["LAST_NAME"]]
            else:
                information[time].append(info["FIRST_NAME"] + " " + info["LAST_NAME"])

    return render_template("joining_date.html", information=information)


if __name__ == '__main__':
    app.run(debug=True)