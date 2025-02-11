from lib.todo import Todo
import pytest

@pytest.fixture
def new_todo():
	return Todo("Walk the dog.")

def test_todo_public_props_are_initialised(new_todo):
	assert isinstance(new_todo, Todo)
	assert new_todo.task == "Walk the dog."
	assert new_todo.is_completed == False

def test_mark_complete_changes_to_done(new_todo):
	new_todo.mark_complete()
	assert new_todo.is_completed == True

def test_mark_complete_does_not_change_already_completed_todo(new_todo):
	new_todo.mark_complete()
	new_todo.mark_complete()
	assert new_todo.is_completed == True

def test_raises_type_error_if_task_is_empty_string():
	with pytest.raises(ValueError) as e:
		Todo("")
	err_msg = str(e.value)
	assert err_msg == "Task cannot be an empty string."

def test_raises_type_error_if_task_not_a_string():
	with pytest.raises(TypeError) as e:
		Todo(80085)
	err_msg = str(e.value)
	assert err_msg == "Task must be a string."

	