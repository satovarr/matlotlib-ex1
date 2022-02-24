import matplotlib.pyplot as plt
import students as std

db = std.database
db.select_user(1)


def get_percentages(marks):
    return [x * 100 / 5 for x in marks]


def students_line_plot(students):
    plt.plot(students.names, students.marks)
    plt.title("Students Marks Graph")

    plt.xlabel("Students Names")
    plt.ylabel("Students Marks")
    plt.xlim(xmin=0, xmax=len(students.names))
    plt.ylim(ymin=0, ymax=5)
    plt.grid(True)
    plt.show()


def students_bar_plot(students):
    left_edges = students.names
    height = students.percentages
    plt.bar(left_edges, height)
    plt.title("Students Percentages Graph")
    plt.xlabel("Students Names")
    plt.ylabel("Students Percentages Marks")
    plt.show()


def main(students):

    percentages = get_percentages(students.marks)
    students.percentages = percentages
    students_bar_plot(students)


if __name__ == '__main__':
    main(std)
