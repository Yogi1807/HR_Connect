"""
Write a program to get details of employees whose salary is > 9000. The output should
be in following format
"""


from my_utils.csv_ import HandleCSV


from flask import Flask, render_template

app = Flask(__name__)


@app.route("/info")
def get_info():

    foo = HandleCSV.read_entire_csv()
    emp = {}
    j = 1
    for i in foo:
        if int(i["SALARY"]) > 9000:
            emp[j] = {"Name": (i["FIRST_NAME"] + " " + i["LAST_NAME"]),
                      "email": i["EMAIL"], "Phone": i["PHONE_NUMBER"].replace(".", "")}
            j += 1
    return render_template("Employee_Info.html", emp=emp)


if __name__ == "__main__":

    app.run(debug= True)
