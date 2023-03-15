import csv


class HandleCSV:
    filename = "C:\\Users\\Shree\\VelocityProjects\\HRConnect\\employees.csv"

    @classmethod
    def read_entire_csv(cls):
        li = []
        with open(cls.filename, "r") as foo:
            result = csv.DictReader(foo)
            for i in result:
                li.append(i)
        return li

    @classmethod
    def read_csv_line_by_line(cls):
        with open(cls.filename) as bar:
            yield bar.readline()


