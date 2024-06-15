function toggle() {
    const toggleButtonElement = document.querySelector('.head span.button');
    const extraTextElement = document.querySelector('#extra');
    const currentButtonText = toggleButtonElement.textContent;

    if (currentButtonText === 'More') {
        extraTextElement.style.display = 'block';
        toggleButtonElement.textContent = 'Less';
    } else {
        extraTextElement.style.display = 'none';
        toggleButtonElement.textContent = 'More';
    }
    

}