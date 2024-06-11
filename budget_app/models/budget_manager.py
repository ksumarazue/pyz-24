<<<<<<< HEAD
from .expense import Expense
=======
from models.expense import Expense
from database import db
from datetime import date


class InvalidExpenseError(Exception):
    pass


class NotFoundExpenseError(Exception):
    pass


>>>>>>> 7de5fa2ccfcc2497493f9d4fced3a04af99866da
class BudgetManger:
    def get_expenses(self):
        return Expense.query.all()

    def add_expense(self, description: str, amount: float, ex_date: str):
        if not description or amount <= 0:
            raise InvalidExpenseError("Invalid expense data")
        ex_date = date.fromisoformat(ex_date)
        new_expense = Expense(description=description, amount=amount, date=ex_date)
        db.session.add(new_expense)
        db.session.commit()

    def update_expense(self, id, description, amount, ex_date):
        expense = self.get_expense(id)
        if not description or amount <= 0:
            raise InvalidExpenseError("Invalid expense data")
        if expense:
            expense.description = description
            expense.amount = amount
            expense.date = date.fromisoformat(ex_date)
            db.session.commit()

    def delete_expense(self, id):
        expense = self.get_expense(id)
        if expense:
            db.session.delete(expense)
            db.session.commit()

    @staticmethod
    def get_expense(id):
        expense = Expense.query.filter_by(id=id).first()

<<<<<<< HEAD

    def delete_expense(self, id):
        expense = self.get_expense(id)
        self.expenses.remove(expense)
=======
        if not expense:
            raise NotFoundExpenseError(f"Expense ID = {id} not found")
        else:
            return expense
>>>>>>> 7de5fa2ccfcc2497493f9d4fced3a04af99866da
