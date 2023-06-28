

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('libform');
    const storyElement = document.getElementById('story');
    const shuffleButton = document.getElementById('shuffle-button');
  
    form.addEventListener('submit', function(event) {
      event.preventDefault();
  
      const noun = document.getElementById('noun').value;
      const adjective = document.getElementById('adjective').value;
      const person = document.getElementById('person').value;
      const verb = document.getElementById('verb').value;
      const place = document.getElementById('place').value;
  
      if (noun !== '' && adjective !== '' && person !== '' && verb !== '' && place !== '') {
        const story = `Once upon a time, ${person} went to ${place} and found a ${adjective} ${noun}. They quickly ${verb} away. The end.`;
        storyElement.textContent = story;
      } else {
        console.log('Please fill in all the inputs.');
      }
    });
  
    shuffleButton.addEventListener('click', function() {
      const stories = [
        'Once upon a time, there was a brave adventurer who found a mysterious treasure in a hidden cave.',
        'In a faraway kingdom, a young prince discovered a magic sword and used it to defeat an evil dragon.',
        'A group of friends embarked on an unforgettable journey to a magical land filled with talking animals and enchanted forests.'
      ];
  
      const randomIndex = Math.floor(Math.random() * stories.length);
      storyElement.textContent = stories[randomIndex];
    });
  });
  