function solve() {
  const textAreaElement = document.getElementById('input');
  const text = textAreaElement.value;
  const outputElement = document.getElementById('output');

  const sentanceArray = text.split('.').filter(sentance => sentance.length >= 1);
  const formatedArray = [];

  const arrayLength = Math.floor(sentanceArray.length / 3);
  for (let i = 0; i < arrayLength; i++) {
    let firstElement = sentanceArray.shift();
    let secondElement = sentanceArray.shift();
    let thirdElement = sentanceArray.shift();

    formatedArray.push(`<p>${firstElement.trim()}.${secondElement}.${thirdElement}.</p>`);
    
  }

  if (sentanceArray.length !== 0) {
    formatedArray.push(`<p>${sentanceArray.join('.').trim()}.</p>`)
  }

  const result = formatedArray.join('\n');
  outputElement.innerHTML = result;
}