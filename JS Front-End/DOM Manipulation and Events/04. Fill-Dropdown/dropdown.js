function addItem() {
    const textElement = document.getElementById('newItemText');
    const valueElement = document.getElementById('newItemValue');
    const menuElement = document.getElementById('menu');

    const newOptionElement = document.createElement('option');
    newOptionElement.textContent = textElement.value;
    newOptionElement.value = valueElement.value;

    menuElement.appendChild(newOptionElement);

    textElement.value = '';
    valueElement.value = '';
}