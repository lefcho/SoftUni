function solve() {
  const textElement = document.getElementById('text');
  const parameterElement = document.getElementById('naming-convention');
  const resultElement = document.getElementById('result');

  const text = textElement.value;
  const parameter = parameterElement.value;

  const toPascal = (text) => 
    text
    .split(' ')
    .map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
    .join('');

  const convertor = {
    'Pascal Case': toPascal,
    'Camel Case': (text) => toPascal(text).charAt(0).toLowerCase() + toPascal(text).slice(1)
  };

  if (!Object.keys(convertor).includes(parameter)) {
    resultElement.textContent = 'Error!';
  } else {
    resultElement.textContent = convertor[parameter](text); 
  }

}