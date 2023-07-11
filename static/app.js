class Chatbox {
    // Executed when a new instance of Chatbox is created
    // class properties are args, state and messages
    constructor() {
        // contains HTML elements of the chatbox
        // open button, chatbox container, send button
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button')
        };
        // keeps track of the open and closed state of the chatbox
        this.state = false;
        // array to store the messages
        this.messages = [];
    }

    // method to set up event listeners and handle user interactions with the chatbox.
    display() {
        const { openButton, chatBox, sendButton } = this.args;

        // attaches a click event listener to the open button, which calls the toggleState() method when clicked.
        openButton.addEventListener('click', () => this.toggleState(chatBox));

        // attaches a click event listener to the send button, which calls the onSendButton() method when clicked.
        sendButton.addEventListener('click', () => this.onSendButton(chatBox));

        // attaches a keyup event listener to the input field in the chatbox, which calls the onSendButton() method when the Enter key is pressed.
        const node = chatBox.querySelector('input');
        node.addEventListener('keyup', ({ key }) => {
            if (key === 'Enter') {
                this.onSendButton(chatBox);
            }
        });
    }

    // method responsible for toggling the open or closed state of the chatbox.
    toggleState(chatBox) {
        // flips the value of the state property
        this.state = !this.state;

        // If the state is true, it adds the CSS class chatbox--active to the chatbox container, which displays it.
        if (this.state) {
            chatBox.classList.add('chatbox--active');
            // If the state is false, it removes the chatbox--active class, hiding the chatbox.
        } else {
            chatBox.classList.remove('chatbox--active');
        }
    }

    // method is called when the user clicks the send button or presses Enter in the chatbox.
    onSendButton(chatBox) {
        // It retrieves the input field element from the chatbox container and gets the value of the input text.
        const textField = chatBox.querySelector('input');
        // input text is trimmed to remove any leading or trailing whitespace.
        const text = textField.value.trim();
        // If the trimmed text is empty, i.e., the user didn't enter any message, the method returns early.
        if (text === '') {
            return;
        }
        // Otherwise, it creates a new message object with the user's name and message text and adds it to the messages array.
        const msg = { name: 'User', message: text };
        this.messages.push(msg);

        // initiates an HTTP request to the URL, 
        // which is the endpoint of the Flask server where the prediction is expected to be handled. 
        // The second argument is an object containing the options for the request.
        fetch($SCRIPT_ROOT + '/predict', {
            method: 'POST', // request to send data to the server
            body: JSON.stringify({ message: text }), // sets the javascript object {message:text} to a JSON string, this allows as to send user input as JSON to the server
            mode: 'cors', // specifies request is a cross-origin-request, allows browser to make requests to a different domain
            headers: { // sets the request header to specify that data is being sent as a JSON format
                'Content-Type': 'application/json'
            },
        })
            // chained to the fetch method to handle response from server, converts it to json
            .then(response => response.json())
            // another chained method to handle the JSON response
            // the response is assigned to the response variable
            .then(response => {
                // msg object is created with name property set to 'Sophia' and message property set to 'response.answer'
                const msg = { name: 'Sophia', message: response.answer };
                // adds the 'msg' object, representing the chatbot response to the 'messages' array to store conversation history
                this.messages.push(msg);
                // calls the updateChatText() method to update the chatbox UI with the new message
                this.updateChatText(chatBox);
                // clears the input field by setting its value to an empty string
                textField.value = '';
            })
            // handles errors that may occur during HTTP requests
            // error is logged to the console using console.error()
            .catch(error => {
                console.error('Error:', error);
                // updates the chatbox UI in case of error
                this.updateChatText(chatBox);
                // clears the input to ensure consistecy of UI
                textField.value = '';
            });
    }

    // method responsible for updating the chat messages in the chatbox UI.
    updateChatText(chatBox) {
        // Retrieves the chat message container element from the chatbox container using the class chatbox__messages.
        const chatMessageContainer = chatBox.querySelector('.chatbox__messages');
        // clears the existing chat messages by setting the innerHTML property of the container to an empty string.
        chatMessageContainer.innerHTML = '';

        // iterates over the 'messages' array and creates a 'div' element for each message
        this.messages.forEach(item => {
            const messageElement = document.createElement('div');
            messageElement.classList.add('messages__item');

            // Depending on the sender of the message (user or operator), it adds the appropriate CSS class to the message element.
            if (item.name === 'Sophia') {
                messageElement.classList.add('messages__item--visitor');
            } else {
                messageElement.classList.add('messages__item--operator');
            }

            // creates a 'span' element for the message text 
            const messageText = document.createElement('span');
            // sets its 'innerHTML' to the message content
            messageText.innerHTML = item.message;

            // message text element is appended to the message element
            messageElement.appendChild(messageText);

            // Prepend the message to the beginning of the chat message container
            chatMessageContainer.prepend(messageElement);
        });
    }
    l
}

// instantiates the Chatbox class
const chatbox = new Chatbox();
// calls the 'display' method of the chatbox object to set up the chatbox and its event listeners
chatbox.display();



