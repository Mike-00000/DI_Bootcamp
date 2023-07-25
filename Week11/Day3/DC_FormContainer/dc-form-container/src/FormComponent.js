// FormComponent.js
import React from 'react';

const FormComponent = (props) => {
  return (
    <form>
      <label>
        
        <input
          type="text"
          name="firstName"
          value={props.data.firstName}
          onChange={props.handleChange}
          placeholder="First Name"
        />
      </label>
      <br />
      <label>
        
        <input
          type="text"
          name="lastName"
          value={props.data.lastName}
          onChange={props.handleChange}
          placeholder="Last Name"
        />
      </label>
      <br />
      <label>
        
        <input
          type="number"
          name="age"
          value={props.data.age}
          onChange={props.handleChange}
          placeholder="Age"
        />
      </label>
      <br /> <br></br>
      <label>
        <input
          type="radio"
          name="gender"
          value="male"
          checked={props.data.gender === 'male'}
          onChange={props.handleChange}
        /> Male<br></br>
        <input
          type="radio"
          name="gender"
          value="female"
          checked={props.data.gender === 'female'}
          onChange={props.handleChange}
        /> Female
      </label>
      <br />
      <label>
      <label className="label-bold">Select your destination:</label><br></br>
        <select
          name="destination"
          value={props.data.destination}
          onChange={props.handleChange}
        >
          <option value="">-- Please Choose a destination --</option>
          <option value="Japan">Japan</option>
          <option value="USA">USA</option>
          <option value="Germany">Germany</option>
          <option value="France">France</option>
        </select>
      </label>
      <br /><br></br>
      <label>
      <label className="label-bold">Dietary restrictions:</label><br></br>
        <input
          type="checkbox"
          name="nutsFree"
          checked={props.data.nutsFree}
          onChange={props.handleChange}
        /> Nuts free<br></br>
        <input
          type="checkbox"
          name="lactoseFree"
          checked={props.data.lactoseFree}
          onChange={props.handleChange}
        /> Lactose free<br></br>
        <input
          type="checkbox"
          name="veganMeal"
          checked={props.data.veganMeal}
          onChange={props.handleChange}
        /> Vegan
      </label>
      <br /><br></br>
      <input type="submit" value="Submit" />
    </form>
  );
};

export default FormComponent;
