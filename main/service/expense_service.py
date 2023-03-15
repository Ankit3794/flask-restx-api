from main import db
from main.model.expense import Expense


class ExpenseService:
    @classmethod
    def get_all_expenses(cls):
        return Expense.query.all()

    @classmethod
    def add_expense(cls, data):
        expense = Expense(**data)
        db.session.add(expense)
        db.session.commit()
        return {'message': 'expense added successfully'}, 201
