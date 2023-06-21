
// Exercise 7 : My Book List

// 7.2 
const allBooks = [
    {
      title: "Harry Potter",
      author: "JK Rowling",
      image: "harry_potter.jpg",
      alreadyRead: false
    },
    {
      title: "Lord of the Rings",
      author: "J. R. R. Tolkien",
      image: "LotR.jpg",
      alreadyRead: true
    }
  ];
  
  // 7.4 
  const sectionElement = document.querySelector('.listBooks');
  
  allBooks.forEach(function(book) {
    const divElement = document.createElement('div');
    const titleElement = document.createElement('h2');
    const authorElement = document.createElement('p');
    const imageElement = document.createElement('img');
  
    titleElement.textContent = book.title;
    authorElement.textContent = "Written by " + book.author;
    imageElement.src = book.image;
    imageElement.style.width = '100px';
  
    divElement.appendChild(titleElement);
    divElement.appendChild(authorElement);
    divElement.appendChild(imageElement);
  
    if (book.alreadyRead) {
      divElement.style.color = 'red';
    }
  
    sectionElement.appendChild(divElement);
  });
  