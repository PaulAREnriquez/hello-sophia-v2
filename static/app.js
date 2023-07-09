class Chatbox {
    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button')
        };

        this.state = false;
        this.messages = [];
    }

    display() {
        const { openButton, chatBox, sendButton } = this.args;

        openButton.addEventListener('click', () => this.toggleState(chatBox));

        sendButton.addEventListener('click', () => this.onSendButton(chatBox));

        const node = chatBox.querySelector('input');
        node.addEventListener('keyup', ({ key }) => {
            if (key === 'Enter') {
                this.onSendButton(chatBox);
            }
        });
    }

    toggleState(chatBox) {
        this.state = !this.state;

        if (this.state) {
            chatBox.classList.add('chatbox--active');
        } else {
            chatBox.classList.remove('chatbox--active');
        }
    }

    onSendButton(chatBox) {
        const textField = chatBox.querySelector('input');
        const text = textField.value.trim();
        if (text === '') {
            return;
        }

        const msg = { name: 'User', message: text };
        this.messages.push(msg);

        fetch ($SCRIPT_ROOT + '/predict', {
            method: 'POST',
            body: JSON.stringify({ message: text }),
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json'
            },
        })
            .then(response => response.json())
            .then(response => {
                const msg = { name: 'Sophia', message: response.answer };
                this.messages.push(msg);
                this.updateChatText(chatBox);
                textField.value = '';
            })
            .catch(error => {
                console.error('Error:', error);
                this.updateChatText(chatBox);
                textField.value = '';
            });
    }

    updateChatText(chatBox) {
        const chatMessageContainer = chatBox.querySelector('.chatbox__messages');
        chatMessageContainer.innerHTML = '';
    
        this.messages.forEach(item => {
            const messageElement = document.createElement('div');
            messageElement.classList.add('messages__item');
    
            if (item.name === 'Sophia') {
                messageElement.classList.add('messages__item--visitor');
            } else {
                messageElement.classList.add('messages__item--operator');
            }
    
            const messageText = document.createElement('span');
            messageText.innerHTML = item.message;
    
            messageElement.appendChild(messageText);
    
            // Prepend the message to the beginning of the container
            chatMessageContainer.prepend(messageElement);
        });
    }
l    
}

const chatbox = new Chatbox();
chatbox.display();
