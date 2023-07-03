// Daily Challenge: Play With Words

// ________________________________________________
// 1rst Daily Challenge

function makeAllCaps(words) {
  return new Promise((resolve, reject) => {
    const wordsEvery = words.every((word) => typeof word === "string");
    if (wordsEvery) {
      const uppercasedWords = words.map((word) => word.toUpperCase());
      resolve(uppercasedWords);
    } else {
      reject("Contains non-string values");
    }
  });
}

function sortWords(words) {
  return new Promise((resolve, reject) => {
    if (words.length > 4) {
      resolve(words.sort());
    } else {
      reject("Array length is bigger than 4");
    }
  });
}

makeAllCaps([1, "pear", "banana"])
  .then((arr) => sortWords(arr))
  .then((result) => console.log(result))
  .catch((error) => console.log(error));

makeAllCaps(["apple", "pear", "banana"])
  .then((arr) => sortWords(arr))
  .then((result) => console.log(result))
  .catch((error) => console.log(error));

makeAllCaps(["pear", "kiwi", "apple", "goyave", "orange"])
  .then((arr) => sortWords(arr))
  .then((result) => console.log(result))
  .catch((error) => console.log(error));

// ________________________________________________
// 2nd Daily Challenge

const morse = `{
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
  }`;

function toJs() {
    return new Promise((resolve, reject) => {
        const morseJS = JSON.parse(morse)
        console.log(morseJS);
        if (Object.keys(morseJS).length === 0) {
            reject ("object is empty")
        } else {
            resolve (console.log(morseJS))
        }
    })
}

function toMorse(morseJS) {
    return new Promise((resolve, reject) => {
        const sentence = prompt("type a word or a sentence");
        const charSentence = [...sentence.toLocaleLowerCase()];
        const morseTranslation = [];

        for (let letter of charSentence) {
            if (morseJS.hasOwnProperty(letter)) {
                morseTranslation.push(morseJS[letter]);
            } else {
                reject(`Invalid character: ${letter}`);
                return;
            }
        }
    
        resolve(morseTranslation);
      });
    }



toJs()
.then(() => toMorse(JSON.parse(morse)))
.then((result) => console.log(result))
.catch((error) => console.log(error));
  
// 4.
function joinWords(morseTranslation) {
    const morseText = morseTranslation.join('\n');
    document.getElementById('output').innerText = morseText;
  }

toJs()
.then(() => toMorse(JSON.parse(morse)))
.then((result) => joinWords(result))
.catch((error) => console.log(error));


// 5.
toJs()
  .then((morseJS) => toMorse(morseJS))
  .then((morseTranslation) => joinWords(morseTranslation))
  .catch((error) => console.log(error));
