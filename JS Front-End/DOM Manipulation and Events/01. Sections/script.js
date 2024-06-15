function create(words) {
   const contentElement = document.getElementById('content');

   const divElements = words
      .map(word => {
         const divElement = document.createElement('div');
         const pElement = document.createElement('p');

         pElement.style.display = 'none';
         pElement.textContent = word;
         divElement.appendChild(pElement);

         divElement.addEventListener('click', () => {
            pElement.style.display = 'block';
         })

         return divElement;
   });

   divElements.forEach(divElements => contentElement.appendChild(divElements));
}