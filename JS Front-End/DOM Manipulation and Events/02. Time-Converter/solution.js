function attachEventsListeners() {
    const convertButtonElements = document.querySelectorAll('input[value=Convert]');
    const inputElements = document.querySelectorAll('input[type=text]');

    function toSeconds(value, unit) {
        switch (unit) {
            case 'days':
                return value * 24 * 60 * 60;
            case 'hours':
                return value * 60 * 60;
            case 'minutes':
                return value * 60;
            case 'seconds':
                return value;
        }
        
    }

    const converter = {
        days(seconds) {
            return seconds / 60/ 60 / 24;
        },
        hours(seconds) {
            return seconds / 60/ 60;
        },
        minutes(seconds) {
            return seconds / 60;
        },
        seconds(seconds) {
            return seconds;
        }
    }


    for (const buttonElement of convertButtonElements) {
        buttonElement.addEventListener('click', (e) => {
            const currentInputElement = e.currentTarget.previousElementSibling;

            for (const inputElement of inputElements) {
                const currentSeconds = toSeconds(Number(currentInputElement.value), currentInputElement.id);
                inputElement.value = converter[inputElement.id](currentSeconds);
            }
        });
    }
}