# Wine-Quality-Predictions-with-Machine-Learning
This is basic Machine Learning project of Quality of Wine.
Predicting the Quality of Red Wine using Machine Learning Algorithms for Regression Analysis, Data Visualizations and Data Analysis.


[![](https://camo.githubusercontent.com/2fb0723ef80f8d87a51218680e209c66f213edf8/68747470733a2f2f666f7274686562616467652e636f6d2f696d616765732f6261646765732f6d6164652d776974682d707974686f6e2e737667)](https://python.org)

# Documantation
On this repository it is  simple machine learning project.

In machine learning project predict the Quality of wine ['Fixed-acidity','Volatile-acidity','Residual-Sugar','Chlorides','RFree-Sulphur-Dioxide',etc..] 1600 records in **csv** file on this project.


on this project are testing a multiple regrassion model there example are below
 - DecisionTreeClassifier Model
 - KNeighborsClassifier Model
 - KMeans Model

# Context
The two datasets are related to red and white variants of the Portuguese "Vinho Verde" wine. For more details, consult the reference [Cortez et al., 2009]. Due to privacy and logistic issues, only physicochemical (inputs) and sensory (the output) variables are available (e.g. there is no data about grape types, wine brand, wine selling price, etc.).

These datasets can be viewed as classification or regression tasks. The classes are ordered and not balanced (e.g. there are much more normal wines than excellent or poor ones).

This dataset is also available from the UCI machine learning repository 

# Content
For more information, read [Cortez et al., 2009].
Input variables (based on physicochemical tests):
1 - fixed acidity 
2 - volatile acidity 
3 - citric acid 
4 - residual sugar 
5 - chlorides 
6 - free sulfur dioxide 
7 - total sulfur dioxide 
8 - density 
9 - pH 
10 - sulphates 
11 - alcohol 
Output variable (based on sensory data): 
12 - quality (score between 0 and 10) 

# Tips
What might be an interesting thing to do, is aside from using regression modelling, is to set an arbitrary cutoff for your dependent variable (wine quality) at e.g. 7 or higher getting classified as 'good/1' and the remainder as 'not good/0'. This allows you to practice with hyper parameter tuning on e.g. decision tree algorithms looking at the ROC curve and the AUC value. Without doing any kind of feature engineering or overfitting you should be able to get an AUC of .88 (without even using random forest algorithm)

KNIME is a great tool (GUI) that can be used for this.
1 - File Reader (for csv) to linear correlation node and to interactive histogram for basic EDA.
2- File Reader to 'Rule Engine Node' to turn the 10 point scale to dichtome variable (good wine and rest), the code to put in the rule engine is something like this:
- $quality$ > 6.5 => "good"
- TRUE => "bad" 
3- Rule Engine Node output to input of Column Filter node to filter out your original 10point feature (this prevent leaking)
4- Column Filter Node output to input of Partitioning Node (your standard train/tes split, e.g. 75%/25%, choose 'random' or 'stratified')
5- Partitioning Node train data split output to input of Train data split to input Decision Tree Learner node and 
6- Partitioning Node test data split output to input Decision Tree predictor Node
7- Decision Tree learner Node output to input Decision Tree Node input
8- Decision Tree output to input ROC Node.. (here you can evaluate your model base on AUC value)

## Technology used in Project :
<img target="_blank" src="https://github.com/yogeshnile/technology/blob/master/pandas.png" width="300">   <img target="_blank" src="https://github.com/yogeshnile/technology/blob/master/Jupyter.png" width="200">    <img target="_blank" src="https://github.com/yogeshnile/technology/blob/master/numpy.png" width="200">     

# Inspiration
Use machine learning to determine which physiochemical properties make a wine 'good'!

# Acknowledgements
This dataset is also available from the UCI machine learning repository, https://archive.ics.uci.edu/ml/datasets/wine+quality , 
I just shared it to kaggle for convenience. (I am mistaken and the public license type disallowed me from doing so, I will take this down at first request. I am not the owner of this dataset.)

 Modeling wine preferences by data mining from physicochemical properties.

## Bug / Feature Request :
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/yogeshnile/Iris-Flower-Classification-using-Machine-Learning/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/yogeshnile/Iris-Flower-Classification-using-Machine-Learning/issues/new). Please include sample queries and their corresponding results.


## Contribution

Contributions are welcome! If you have any suggestions, bug fixes, or feature additions, please open an issue or submit a pull request.

**BTC Wallet : OxfCaaF45156380eF33f078256d0Aa98f0b10F175b** my efforts and help it grow by buying me coffee - but only if you're definitely able to!


## Connect with me! 🌐
Known on internet as **BadBoy17**

[<img target="_blank" src="https://img.icons8.com/bubbles/100/000000/linkedin.png" title="LinkedIn">](www.linkedin.com/in/kunal-ranjan-166b30249)      [<img target="_blank" src="https://img.icons8.com/bubbles/100/000000/github.png" title="Github">](https://github.com/BadBoy0170)     [<img target="_blank" src="https://img.icons8.com/bubbles/100/000000/instagram-new.png" title="Instagram">](https://instagram.com/badboy__17_/) 

## Email Me :e-mail:
[<img target="_blank" src="https://img.icons8.com/bubbles/100/000000/secured-letter.png" title="Mail me">](mailto:Rajveershikhawat07@gmail.com)
