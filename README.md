# Senior Thesis LSTM Chatbot

An LSTM-based chatbot trained to talk like Donald Trump tweets

## Getting Started
### Prerequisites
This application requires these python libraries to run:

* Numpy
* Keras
* Tensorflow
* Gensim

To construct the plots, matplotlib is also required

To download these modules, run the command
```
pip install numpy tensorflow keras gensim matplotlib
```

### Running the LSTM
Once the required libraries are installed, if you would like to train the chatbot using our data, simply run 
```
python /Scripts/LSTM.py
```
while inside the repository

If you would like to use your own data, change the opened file in the line 
```
with open('../Dataset/trumptweetssentencesformatted.txt') as file_:
```
to your own input file

to change where the output is saved, change the line
```
logFile = '../Results/modelsize300-2.txt'
```
to direct to the file you would like to output to

### Plot Construction

To work with our plot construction, have your output files in Results, and follow the naming convention testNameTestValue-testNumber.txt. For example, testing model size with a test value of 300 on the second test our output file is named modelsize300-2.txt.

To run our plot constructor, change the line
```
testName = 'batchsize'
```
to reflect the testName you used in your output files, and change the line
```
title = 'Batch Loss'
```
to be what you would like to title your plot. Add your test values to the dictionary
```
cols = {'1024':'r',
	'512': 'b',
	'128': 'g',
	'2': 'c'}
```
with the test values as the keys and the color you would like the tests to be on your plot as the value

Finally, change the line 
```
saveLocation = '../Results/Batch-Loss-Graph.png'
```
to the location you would like to save your plot to

Then, simply run
```
python /Scripts/constructplot.py
```

## Authors
* **Michael Read** - [MichaelInAction](https://github.com/MichaelInAction) -- Main Contributor
*  **Pablo Rivas** - [pablorp80](https://github.com/pablorp80) -- Project Advisor

## Acknowledgements
* Thanks to my advisor [Pablo Rivas](https://github.com/pablorp80) for the help on this project
