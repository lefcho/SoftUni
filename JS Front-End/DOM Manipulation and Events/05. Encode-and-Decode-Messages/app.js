function encodeAndDecodeMessages() {
    const initialMessageElement = document.querySelector('main div:first-of-type textarea');
    const encodeButtonElement = document.querySelector('main div:first-of-type button');
    const encodedMessageElement = document.querySelector('main div:last-of-type textarea');
    const decodeButtonElement = document.querySelector('main div:last-of-type button');

    function shiftASCII(message, index) {
        let shiftedMessage = '';
        for (let i = 0; i < message.length; i++) {
            let charCode = message.charCodeAt(i);
            shiftedMessage += String.fromCharCode(charCode + index);
        }
        return shiftedMessage;
    }

    encodeButtonElement.addEventListener('click', (e) => {
        let message = initialMessageElement.value;
        message = shiftASCII(message, 1)
        initialMessageElement.value = '';
        encodedMessageElement.value = message;
    })

    decodeButtonElement.addEventListener('click', (e) => {
        if (encodedMessageElement.value !== '') {
            let decodedMessage = shiftASCII(encodedMessageElement.value, -1);
            encodedMessageElement.value = decodedMessage;
        }
    })
}