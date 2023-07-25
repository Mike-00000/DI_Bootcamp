import React from "react";
import data from "./data2.json";

class Example2 extends React.Component {
  render() {
    const skills = data.Skills;

    const skillSections = Object.keys(skills).map((section, index) => (
      <div key={index}>
        <strong>{section}</strong>
        <ul>
          {skills[section].map((skill, i) => (
            <li key={i}>{skill}</li>
          ))}
        </ul>
      </div>
    ));

    return (
      <div>
        <h3>Example2 Component</h3>
        {skillSections}
      </div>
    );
  }
}

export default Example2;
