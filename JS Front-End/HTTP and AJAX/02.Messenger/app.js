function attachEvents() {
    const messagesURL = 'http://localhost:3030/jsonstore/messenger'

    const textAreaElement = document.getElementById('messages');
    const authorElement = document.querySelector('input[name=author]');
    const messageElemenent = document.querySelector('input[name=content]');
    const sendButtonElement = document.getElementById('submit');
    const refreshButtonElement = document.getElementById('refresh');

    refreshButtonElement.addEventListener('click', () => {
        fetch(messagesURL)
            .then(res => res.json())
            .then(messages => {
                let textMessages = [];
                Object.values(messages)
                    .forEach(message  => {
                        textMessages.push(`${message.author}: ${message.content}`)
                    })
                textAreaElement.value = textMessages.join('\n')
            });
    });

    sendButtonElement.addEventListener('click', () => {
        let author = authorElement.value;
        let content = messageElemenent.value;
        let data = {
            author,
            content
        }

        fetch(messagesURL, {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"  
            },
            body: JSON.stringify(data),
        })
            .then(response => {
                authorElement.value = '';
                messageElemenent.value = '';
            })
    });
}

attachEvents();
