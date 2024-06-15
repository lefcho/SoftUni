function lockedProfile() {
    const profileElements = document.querySelectorAll('.profile');

    for (const profileElement of profileElements) {

        const buttonElement = profileElement.querySelector('button');
        const lockRadioElement = profileElement.querySelector('input[type=radio][value=lock]');
       
        buttonElement.addEventListener('click', (e) => {

            if (lockRadioElement.checked) {
                return;
            }
            
            const personalInfoElement = buttonElement.previousElementSibling;

            if (buttonElement.textContent === 'Show more') {
                buttonElement.textContent = 'Hide it';
                personalInfoElement.style.display = 'block';
                
            } else {
                buttonElement.textContent = 'Show more';
                personalInfoElement.style.display = 'none';
            }
        })
    }
}