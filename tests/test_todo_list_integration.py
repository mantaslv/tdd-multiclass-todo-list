from lib.todo import Todo
from lib.todo_list import TodoList
import pytest

def test_todo_list_integration():
	my_todos = TodoList()
	assert my_todos.incomplete() == []
	assert my_todos.complete() == []
	
	todo1 = Todo("Walk the dog.")
	my_todos.add(todo1)
	assert my_todos.incomplete() == [todo1]
	assert my_todos.complete() == []
	
	todo2 = Todo("Wash the car.")
	my_todos.add(todo2)
	assert my_todos.incomplete() == [todo1, todo2]
	assert my_todos.complete() == []

	todo3 = Todo("Pay the bills.")
	my_todos.add(todo3)
	assert my_todos.incomplete() == [todo1, todo2, todo3]
	assert my_todos.complete() == []

	todo2.mark_complete()
	assert my_todos.incomplete() == [todo1, todo3]
	assert my_todos.complete() == [todo2]

	my_todos.give_up()
	assert my_todos.complete() == [todo1, todo2, todo3]
	assert my_todos.incomplete() == []

def test_raises_type_error_if_add_param_not_todo_type():
	my_todos = TodoList()

	with pytest.raises(TypeError) as e:
		my_todos.add("Walk the dog!")

	assert my_todos.incomplete() == []
	assert my_todos.complete() == []

	err_msg = str(e.value)
	assert err_msg == "Task must be of Todo type."

