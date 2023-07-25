import React from "react";
import data from "./data2.json";


class Example3 extends React.Component {
  render() {
    const experiences = data.Experiences;

    const experienceList = experiences.map((experience) => (
      <div key={experience.id}>
        <div style={{ width: "50px", height: "50px", backgroundColor: "gray", borderRadius: "50%", margin: "auto" }}>
          {experience.image ? "Image Here" : "NO IMAGE AVAILABLE"}
        </div>
        <a href="#" style={{ color: "blue", textDecoration: "underline" }}>
          {experience.company}
        </a>
        <strong>{experience.role}</strong>
        <p>{experience.date} {experience.location}</p>
        <p>{experience.description}</p>
      </div>
    ));

    return (
      <div>
        <h3>Example3 Component</h3>
        {experienceList}
      </div>
    );
  }
}

export default Example3;
