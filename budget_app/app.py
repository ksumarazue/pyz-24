from flask import Flask
from database import db
from controllers.budget.views import budget_bp

app = Flask(__name__)
app.secret_key = 'secret-key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()

app.register_blueprint(budget_bp)


@app.route('/')
@app.route('/index')
def home():
<<<<<<< HEAD
    return render_template('index.html', expenses=budget_manager.expenses)


@app.route('/add', methods=['GET', 'POST'])
def create_expense():
    if request.method == 'POST':
        description = request.form['description']
        amount = request.form['amount']
        date = request.form['date']
        budget_manager.add_expense(description, amount,date)

        return redirect(url_for('home'))

    return render_template('add.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def update_expense(id):
    if request.method == 'GET':
        expense = budget_manager.get_expense(id)
        return render_template('edit.html', expense=expense)

    if request.method == 'POST':
        description = request.form['description']
        amount = request.form['amount']
        date = request.form['date']
        budget_manager.update_expense(id, description, amount, date)
        return redirect(url_for('home'))


@app.route('/delete/<int:id>', methods=['POST'])
def delete_expense(id):
    budget_manager.delete_expense(id)
    return redirect(url_for('home'))
=======
    # TODO: add index.html template
    return 'Hello hello!'
>>>>>>> 7de5fa2ccfcc2497493f9d4fced3a04af99866da


if __name__ == '__main__':
    app.run(debug=True)