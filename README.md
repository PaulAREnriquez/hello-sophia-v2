Hello Sophia v.2

Hello Sophia is a simple customer service assistant designed for a store similar to Goldilocks bakeshop. A simple neural network designed for multi-class classification is developed in Pytorch. It will predict the category of the query of the customer, and based on the category it will try to answer from a list of pre-determined statements. The application is made with Flask and JavaScript.

The data can be found on the [**intents.json**](./data/intents.json), and can be modified if you wish. However, you will also need to retrain the model with the new data. To proceed with the training:

`python -m train`

To run the application:

`flask run`

The libraries are contained inside [requirements.txt](./requirements.txt). 

`pip install requirements.txt`