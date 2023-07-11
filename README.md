Hello Sophia v.2

Sample welcome conversation: 
![hello-sophia-v2-convo1](https://github.com/PaulAREnriquez/hello-sophia-v2/assets/105270881/e2557817-3da4-4e44-a1a5-8c11be30f820)

Sample of conversation in which Sophia cannot understand:
![hello-sophia-convo2](https://github.com/PaulAREnriquez/hello-sophia-v2/assets/105270881/0e3f93e8-ad24-4dd3-8592-2db07c3dc011)

Sample goodbye conversation:
![hello-sophia-convo3](https://github.com/PaulAREnriquez/hello-sophia-v2/assets/105270881/bae73d3a-341d-404b-8e61-068e4633a197)

Hello Sophia is a simple customer service assistant designed for a store similar to Goldilocks bakeshop. A simple neural network designed for multi-class classification is developed in Pytorch. It will predict the category of the query of the customer, and based on the category it will try to answer from a list of pre-determined statements. The application is made with Flask and JavaScript.

The data can be found on the [**intents.json**](./data/intents.json), and can be modified if you wish. However, you will also need to retrain the model with the new data. To proceed with the training:

`python -m train`

To run the application:

`flask run`

The libraries are contained inside [requirements.txt](./requirements.txt). 

`pip install requirements.txt`

Hope you learned something here. Thanks for visiting!
