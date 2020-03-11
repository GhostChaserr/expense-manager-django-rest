


# App Timeline
[] Server setup
  [] Models
    [x] Expense model
  [] Serializers
    [x] Expense serializer
  [] Authentication


# Expense CRUD

> Register new expense
POST http://localhost:8000/api/expenses/
{
	"note":"axali xarji",
	"amount": 200,
	"category": "shopping"
}

> Query expenses
GET http://localhost:8000/api/expenses/ => 201

> Query single expense
GET http://localhost:8000/api/expenses/1 => 200

> Update Expense
PUT http://localhost:8000/api/expenses/1/ => 200
{
	"note":"axali xarji",
	"amount": 900,
	"category": "shopping"
}

> Delete expense
DELETE http://localhost:8000/api/expenses/1/ => 204
