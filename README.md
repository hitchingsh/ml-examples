# ml-examples
These are Machine Learning examples I have run and and in some cases created to give you a better understanding of my machine learning understanding. - Hamilton


### CNN SVHN Classification
* For our capstone project for this Introduction to Tensorflow 2 class I created a CNN (Convolutional Neural Network) model
* We classified Street View House Numbers (SVHN) from Stanford's dataset [http://ufldl.stanford.edu/housenumbers/]
* Note: For students of the Coursera Getting Started with Tensorflow 2 class should not look at this example until after they've completed the class
[./Tensorflow_2_Class_CNN_Capstone_Project_by_Hamilton_2020_12-3.ipynb]

### Neural Translation Model using Encoder RNN and Decoder RNN
* For our capstone project for this Coursera Customzing Your Models with Tensorflow 2 class I created this model that translated from English to Germman.
* This exercise was designed to teach us the concepts of the Encoder/Decoder seq2seq architectures, in this case using LSTMs. 
* This project was for learning purposes and for a production model would require more training data and a more powerful model, such as by adding attention.
* This example uses data from the Anki dataset [http://www.manythings.org/anki/]
* Note: students of this Coursera Tensorflow Class: Customizing Your Models with Tensorflow 2 should not look at this example until after they've completed the class. 
[./Neural_Translation_Model_Capstone_Project_by_Hamilton_2021_1-12.ipynb]

### BERT GLUE E2E on TPU Notebook
* This example downloads BERT (Bidirectional Encoder Representations from Transformers) model from tfdev.hub
* It fine tunes the training on one (any one) of the GLUE (General Language Understanding Evaluation) datasets
* More info about GLUE datasets can be found at: [https://arxiv.org/pdf/1909.13719.pdf]
* This example is copied from: [https://www.tensorflow.org/tutorials/text/solve_glue_tasks_using_bert_on_tpu] 
[./BERT_Glue_E2E.ipynb]

### BERT Fine Tuning Notebook
* This example also downloads BERT  (Bidirectional Encoder Representations from Transformers) model from tfdev.hub
* It fine tunes the training and on the GLUE MRPC dataset from TFDS (tensorflow datasets)
* This example is copied from: [https://www.tensorflow.org/tutorials/text/solve_glue_tasks_using_bert_on_tpu]
[./Fine_Tuning_a_BERT_model.ipynb] 
