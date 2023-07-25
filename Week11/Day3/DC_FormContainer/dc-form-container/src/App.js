import React, { useState } from 'react';
import FormComponent from './FormComponent';
import "./styles.css";

const App = () => {
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    age: '',
    gender: 'male',
    destination: '',
    nutsFree: false,
    lactoseFree: false,
    veganMeal: false,
  });

  const handleChange = (event) => {
    const { name, value, type, checked } = event.target;
    const newValue = type === 'checkbox' ? checked : value;
    setFormData((prevData) => ({
      ...prevData,
      [name]: newValue,
    }));
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const url = `/?firstName=${formData.firstName}&lastName=${formData.lastName}&age=${formData.age}&gender=${formData.gender}&destination=${formData.destination}&nutsFree=${formData.nutsFree}&lactoseFree=${formData.lactoseFree}&veganMeal=${formData.veganMeal}`;
    window.location.href = url;
  };

  return (
    <div>
      <div className='navbar'>
        <h2>Sample form</h2>
      </div>
      <div className='form-container'>
        <FormComponent data={formData} handleChange={handleChange} />
      </div>
      <div className='displayed-info'>
        <h2>Entered information:</h2>
        <p>Your name: {formData.firstName} {formData.lastName}</p>
        <p>Your age: {formData.age}</p>
        <p>Your gender: {formData.gender}</p>
        <p>Your destination: {formData.destination}</p>
        <p>Your dietary restrictions:</p>
        <p>Nuts free: {formData.nutsFree ? 'Yes' : 'No'}</p>
        <p>Lactose free: {formData.lactoseFree ? 'Yes' : 'No'}</p>
        <p>Vegan meal: {formData.veganMeal ? 'Yes' : 'No'}</p>
      </div>
    </div>
  );
};

export default App;
