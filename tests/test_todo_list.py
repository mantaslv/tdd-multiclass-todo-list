# File: tests/todo_list.py


from lib.todo_list import TodoList
from lib.todo import Todo
from unittest.mock import Mock
import pytest

def test_initialises_todo_list_with_empty_list():
	empty_todos = TodoList()
	assert empty_todos.tasks == []

def test_adds_todo_to_task_list():
	new_todos = TodoList()
	todo_mock = Mock(spec=Todo)
	todo_mock.task = "Walk the dog."
	todo_mock.is_completed = False

	new_todos.add(todo_mock)

	assert todo_mock in new_todos.tasks
	assert len(new_todos.tasks) == 1
	assert new_todos.tasks[0].task == "Walk the dog."
	assert new_todos.tasks[0].is_completed == False

@pytest.fixture
def many_todos():
	todos = TodoList()

	def mark_complete_side_effect(todo):
		todo.is_completed = True
		todo.get_is_completed = Mock(return_value=True) 


	todo1 = Mock(spec=Todo)
	todo1.task = "Walk the dog."
	todo1.is_completed = False
	todo1.get_is_completed = Mock(return_value=todo1.is_completed)
	todo1.mark_complete.side_effect = lambda: mark_complete_side_effect(todo1)
	todos.add(todo1)

	todo2 = Mock(spec=Todo)
	todo2.task = "Wash the car."
	todo2.is_completed = True
	todo2.get_is_completed = Mock(return_value=todo2.is_completed)
	todo2.mark_complete.side_effect = lambda: mark_complete_side_effect(todo2)
	todos.add(todo2)

	todo3 = Mock(spec=Todo)
	todo3.task = "Pay the bills."
	todo3.is_completed = False
	todo3.get_is_completed = Mock(return_value=todo3.is_completed)
	todo3.mark_complete.side_effect = lambda: mark_complete_side_effect(todo3)
	todos.add(todo3)

	return todos

def test_incomplete_returns_list_of_incomplete_tasks(many_todos):
	result = many_todos.incomplete()
	assert len(result) == 2
	assert all(task.get_is_completed() is False for task in result)
	assert result[0].task == "Walk the dog."
	assert result[1].task == "Pay the bills."

def test_complete_returns_list_of_complete_tasks(many_todos):
	result = many_todos.complete()
	assert len(result) == 1
	assert all(task.get_is_completed() is True for task in result)
	assert result[0].task == "Wash the car."

def test_give_up_marks_all_tasks_as_complete(many_todos):
	many_todos.give_up()
	assert len(many_todos.incomplete()) == 0
	result = many_todos.complete()
	assert len(result) == 3

	for task in result:
		print(f"Task: {task.task}, Is Completed: {task.get_is_completed()}")

	assert all(task.get_is_completed() == True for task in result)
	assert result[0].task == "Walk the dog."
	assert result[1].task == "Wash the car."
	assert result[2].task == "Pay the bills."

	
