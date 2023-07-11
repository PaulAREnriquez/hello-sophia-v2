Hello Sophia v.2

Sample **welcome** conversation: 
![hello-sophia-v2-convo1](https://github.com/PaulAREnriquez/hello-sophia-v2/assets/105270881/3a8afdb0-39ab-4dff-b1a0-0f7f8fec4647)

Sample of conversation in which Sophia ***cannot understand***:
![hello-sophia-convo2](https://github.com/PaulAREnriquez/hello-sophia-v2/assets/105270881/7e7f8ad8-8e69-467f-94e8-6bfb5fa3b49b)

Sample **goodbye** conversation:
![hello-sophia-convo3](https://github.com/PaulAREnriquez/hello-sophia-v2/assets/105270881/7fadccf7-b540-4c2a-b132-09237c618310)

Hello Sophia is a simple customer service assistant designed for a store similar to Goldilocks bakeshop. A simple neural network designed for multi-class classification is developed in Pytorch. It will predict the category of the query of the customer, and based on the category it will try to answer from a list of pre-determined statements. The application is made with Flask and JavaScript.

The data can be found on the [**intents.json**](./data/intents.json), and can be modified if you wish. However, you will also need to retrain the model with the new data. To proceed with the training:

`python -m train`

To run the application:

`flask run`

The libraries are contained inside [requirements.txt](./requirements.txt). 

`pip install requirements.txt`

Hope you learned something here. Thanks for visiting!
