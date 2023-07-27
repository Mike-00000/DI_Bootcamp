import React from 'react';
import './App.css';

const Todo = ({ index, todo, toggleComplete, deleteTodo }) => {
  return (
    <li
      style={{
        textDecoration: todo.completed ? 'line-through' : 'none',
        cursor: 'pointer',
      }}
      onClick={() => toggleComplete(index)}
    >
      {todo.text}
      <button style={{"left": '500px'}} onClick={() => deleteTodo(index)}>Delete</button>
    </li>
  );
};

export default Todo;
