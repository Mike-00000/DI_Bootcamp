

function Anagram(ana1, ana2) {
    let len1 = ana1.length;
    let len2 = ana2.length;
    if(len1 !== len2) {
        console.log('Invalid Input')
        return;
    }
    let str1 = ana1.split('').sort().join('');
    let str2 = ana2.split('').sort().join('');
    if(str1 === str2) {
        console.log("True");
    } else {
        console.log("False");
    }
}

Anagram("acdee", "acder")
