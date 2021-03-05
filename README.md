# ml-examples
These are Machine Learning examples I have created or adapted to give you a better understanding of my machine learning understanding. - Hamilton


### CNN SVHN Classification
* I created a CNN (Convolutional Neural Network) model to classify Street View House Numbers (SVHN)
* This was the capstone project for the Coursera class Getting Started with Tensorflow 2 class 
* Current students of the Coursera Getting tarted with Tensorflow 2 class should not look at this example 
* [CNN_SVHN_TF2_Capstone_Project_by_Hamilton_2020_12_3.ipynb](CNN_SVHN_TF2_Capstone_Project_by_Hamilton_2020_12_3.ipynb)

### Language Translation Model using Encoder RNN and Decoder RNN
* I created this model that translated from English to Germman
* This was the capstone project for the Coursera Customzing Your Models with Tensorflow 2 class 
* This project taught us Encoder/Decoder seq2seq architectures, using LSTMs (Long Short Term Memory)
* This project was for learning purposes only and not production
* Current students of this Customizing Your Models with Tensorflow 2 class should not look at this
* [Neural_Translation_Model_Capstone_Project_by_Hamilton_2021_1_12.ipynb](Neural_Translation_Model_Capstone_Project_by_Hamilton_2021_1_12.ipynb)

### Language Translation Using the T5 Model and HuggingFace Framework
* Translates the same 5 English strings (all accurately) as my Capstone project above from English to German
* Translates using the HuggingFace pipeline, and with slightly lower level calls to the T5 and MarianMT models
* [Language_Translation_Using_the_T5_Model_And_HuggingFace_Framework.ipynb](Language_Translation_Using_the_T5_Model_And_HuggingFace_Framework.ipynb) 

### Sentiment Analysis - Fine Tuning BERT model on IMDB
* This example downloads BERT (Bidirectional Encoder Representations from Transformers) model from tfdev.hub
* It also serves the model for inference via TensorFlow Serving
* Trained the BERT model on the IMDB Movie Review dataset to make positive and negative sentiment classification predictions
* [Sentiment_Analysis_Fine_Tuning_a_BERT_model_on_IMDB.ipynb](Sentiment_Analysis_Fine_Tuning_a_BERT_model_on_IMDB.ipynb)

### Question Answering using BERT, Roberta & Electra Models Pretrained on Squad & Squad 2
* I adapted these short examples using the HuggingFace API
* [Question_Answering_Models_BERT_Roberta_Electra_Pretrained_on_Squad2.ipynb](Question_Answering_Models_BERT_Roberta_Electra_Pretrained_on_Squad2.ipynb)

### BERT GLUE E2E on TPU Notebook
* This example downloads BERT (Bidirectional Encoder Representations from Transformers) model from tfdev.hub
* It fine tunes the training on one (any one) of the GLUE (General Language Understanding Evaluation) datasets
* More info about GLUE datasets can be found at: https://arxiv.org/pdf/1909.13719.pdf
* This example is copied from: https://www.tensorflow.org/tutorials/text/solve_glue_tasks_using_bert_on_tpu
* [BERT_Glue_E2E.ipynb](BERT_Glue_E2E.ipynb)

### Live Demo of Blender Chatbot using the RoBERTa Transformer
* I setup this demo with a modestly improved UI on Google Cloud using Docker
* See a Blenderbot [example conversation](sample-blender-conversation.png)
* Try it out at: https://blenderbot-wg5fqcbcta-uw.a.run.app (Can take 15+ seconds for Google Cloud to load docker image in) 
* Note, this demo uses the 90 million parameter model. The much larger 2.7 billion and 9.4 billion parameters models will produce better conversations and can be run on more expensive hardware.
* Here's the paper on BlenderBot developed by the Facebook AI team: https://arxiv.org/pdf/2004.13637.pdf 
