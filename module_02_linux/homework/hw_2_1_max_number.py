"""
Реализуйте endpoint, с url, начинающийся с  /max_number ,
в который можно будет передать список чисел, перечисленных через / .
Endpoint должен вернуть текст "Максимальное переданное число {number}",
где number, соответственно, максимальное переданное в endpoint число,
выделенное курсивом.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/max_number/<numbers>")
def max_number(numbers):

    listnum=numbers.split(',')
    listnum=[int(x) for x in listnum]
    return f"{max(listnum)}"
    """Масштабируемое решение через ',' Через / не получается, он считает это за url"""


@app.route("/max_numbers/<int:num1>/<int:num2>")
def max_numbers(num1,num2):

    return f"{max(num1,num2)}"
    """Немасштабируемое решение """


if __name__ == "__main__":
    app.run(debug=True)
