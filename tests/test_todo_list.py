from lib.todo_list import TodoList
from unittest.mock import Mock
import pytest

def test_initialises_todo_list_with_empty_list():
	empty_todos = TodoList()
	assert empty_todos.tasks == []

def test_adds_todo_to_task_list():
	new_todos = TodoList()
	todo_mock = Mock()
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

	todo1 = Mock()
	todo1.task = "Walk the dog."
	todo1.is_completed = False
	todos.add(todo1)

	todo2 = Mock()
	todo2.task = "Wash the car."
	todo2.is_completed = True
	todos.add(todo2)

	todo3 = Mock()
	todo3.task = "Pay the bills."
	todo3.is_completed = False
	todos.add(todo3)

	return todos

def test_incomplete_returns_list_of_incomplete_tasks(many_todos):
	result = many_todos.incomplete()
	assert len(result) == 2
	assert all(task.is_completed == False for task in result)
	assert result[0].task == "Walk the dog."
	assert result[1].task == "Pay the bills."