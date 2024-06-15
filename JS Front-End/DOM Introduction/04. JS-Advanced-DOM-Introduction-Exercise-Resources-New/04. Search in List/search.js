function search() {
   const townsListElement = document.getElementById('towns');
   const searchText = document.getElementById('searchText').value;
   const resultElement = document.getElementById('result');
   let matchCount = 0;

   const townElementList = Array.from(townsListElement.children);
   for (const townElement of townElementList) {
      if (townElement.textContent.includes(searchText)) {
         townElement.style.textDecoration = 'underline';
         townElement.style.fontWeight = 'bold';
         matchCount++;
      } else {
         townElement.style.textDecoration = 'none';
         townElement.style.fontWeight = '100';
      }
   }

   resultElement.textContent = `${matchCount} matches found`
}
