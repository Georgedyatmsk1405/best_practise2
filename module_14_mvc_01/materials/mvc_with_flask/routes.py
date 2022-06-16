from typing import List, Dict

from flask import Flask, render_template,request

from models import init_db, get_all_books, DATA, check_one_book,add_bookss,bookss_by_author,update_count
from validate import BookForm
from flask_wtf.csrf import CSRFProtect
app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'
# csrf = CSRFProtect(app)
app.config["WTF_CSRF_ENABLED"] = False
def _get_html_table_for_books(books: List[Dict]) -> str:
    table = """
<table>
    <thead>
    <tr>
        <th>ID</td>
        <th>Title</td>
        <th>Author</td>
    </tr>
    </thead>
    <tbody>
        {books_rows}
    </tbody>
</table>
"""
    rows = ''
    for book in books:
        rows += '<tr><td>{id}</tb><td>{title}</tb><td>{author}</tb></tr>'.format(
            id=book['id'], title=book['title'], author=book['author'],
        )
    return table.format(books_rows=rows)


@app.route('/books')
def all_books():
    return render_template(
        'index.html',
        books=get_all_books(),
    )


@app.route('/books/form')
def get_books_form():
    form=BookForm()
    return render_template('add_book.html',form=form)


@app.route('/books/<author>')
def get_books_by_author(author):
    books=bookss_by_author(author)
    for book in books:
        update_count(book.title,book.author)

    return render_template('author.html',books=books)


@app.route('/books/add',methods=["POST","GET"])
def add_books():
    print('first')
    form = BookForm()
    print(form.title.data)
    if form.validate_on_submit():
        print('sddssd')
        if check_one_book(form.title.data,form.author.data):
            return "already have"
        add_bookss(form.title.data, form.author.data)
        return "OK"
    return render_template('add_book.html')

if __name__ == '__main__':
    init_db(DATA)
    # app.config['WTF_CSRF_SECRET_KEY']='sdsdsdsd'

    app.run(debug=True)
    # app.config['SECRET_KEY'] = 'f3cfe9ed8fae309f02079dbf'
