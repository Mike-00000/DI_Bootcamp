// 1.
const sentence = "The movie is not that bad, I like it";

// 2.
const wordNot = sentence.indexOf("not");

console.log("Position of 'not':", wordNot);

// 3.
const wordBad = sentence.indexOf("bad");

console.log("Position of 'bad':", wordBad);

// 4. & 5.
const indexNot = sentence.indexOf("not");
const indexBad = sentence.indexOf("bad");

if (indexNot !== -1 && indexBad !== -1 && indexBad > indexNot) {
  const modifiedSentence = sentence.slice(0, indexNot) + "good" + sentence.slice(indexBad + 3);
  console.log("Modified sentence:", modifiedSentence);
} else {
  console.log("No substitution needed:", sentence);
}