import React from "react";
import data from "./data2.json";

class Example1 extends React.Component {
  render() {
    const socialMedias = data.SocialMedias.map((media, index) => (
      <li key={index}>
        <a href={media} target="_blank" rel="noopener noreferrer">
          {media}
        </a>
      </li>
    ));

    return (
      <div>
        <h3>Example1 Component</h3>
        <ul>{socialMedias}</ul>
      </div>
    );
  }
}

export default Example1;
