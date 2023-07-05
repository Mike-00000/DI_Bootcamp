


const apiKey = 'hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My';
const searchForm = document.getElementById('searchForm');
const searchInput = document.getElementById('searchInput');
const gifContainer = document.getElementById('gifContainer');

// Function to fetch a random GIF based on the search category
async function fetchRandomGif(category) {
  try {
    const url = `https://api.giphy.com/v1/gifs/random?api_key=${apiKey}&tag=${category}`;
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error:', error);
  }
}

// Function to create a GIF element and append it to the container
function createGifElement(gif) {
  const gifElement = document.createElement('div');
  gifElement.className = 'gif';

  const imgElement = document.createElement('img');
  imgElement.src = gif.images.original.url;
  gifElement.appendChild(imgElement);

  const deleteButton = document.createElement('button');
  deleteButton.innerText = 'Delete';
  deleteButton.addEventListener('click', () => {
    gifElement.remove();
  });
  gifElement.appendChild(deleteButton);

  gifContainer.appendChild(gifElement);
}

// Event listener for the search form submission
searchForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  const category = searchInput.value.trim();
  if (category) {
    const gifData = await fetchRandomGif(category);
    createGifElement(gifData.data);
  }
  searchInput.value = '';
});

// Function to delete all GIFs
function deleteAllGifs() {
  while (gifContainer.firstChild) {
    gifContainer.firstChild.remove();
  }
}

// Delete all button event listener
const deleteAllButton = document.createElement('button');
deleteAllButton.innerText = 'Delete All';
deleteAllButton.addEventListener('click', deleteAllGifs);
document.body.insertBefore(deleteAllButton, gifContainer);
