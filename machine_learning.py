import pickle
import numpy as np

model = pickle.load(open('MachineLearningModel.pkl', 'rb'))

#perform tests on the loaded model

inputInstance = []   #The input given by the user will be stored here

inputInstance = np.array(input).reshape(1,-1)    #Reshaping the instance to be accepted by the model

predictedOutputRating = int(round(float(model.predict(inputInstance)))) #Return the Output rating to the user in the app