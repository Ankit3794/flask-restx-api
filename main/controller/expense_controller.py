from flask import request
from flask_restx import Resource

from main.service.expense_service import ExpenseService
from main.util.dto import ExpenseDto

api = ExpenseDto.api
_expense = ExpenseDto.expense


@api.route('/')
class Expense(Resource):
    @api.doc("Get all expenses")
    @api.response(200, 'successfully get all expenses')
    @api.marshal_list_with(_expense)
    def get(self):
        return ExpenseService.get_all_expenses()

    @api.response(201, 'Successfully added expense')
    @api.doc("Add new expense")
    @api.expect(_expense, validate=True)
    def post(self):
        data = request.json
        return ExpenseService.add_expense(data)
