import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

data_dict = pickle.load(open('./data.pickle', 'rb'))    # Giving pickle the data.pickle file

# Defining data and labels within the data.pickle file
data = np.asarray(data_dict['data'], dtype = object)
labels = np.asarray(data_dict['labels'], dtype = object)

# Ensuring all items are of the same size
def pad_or_truncate(sample, target_length):
    if len(sample) > target_length:
        return sample[:target_length]
    else:
        return sample + [0] * (target_length - len(sample))
target_length = max(len(sample) for sample in data_dict['data'])
data = [pad_or_truncate(sample, target_length) for sample in data_dict['data']]

# Splitting the data into two sets for data and labels
# Random 20% of the data is set under 'test'
# Data will be split with the same proportion of each label
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

# Clarifying the model and fitting the 
model = RandomForestClassifier()
model.fit(x_train, y_train)

y_predict = model.predict(x_test)

# Calculating the accuracy of the model
score = accuracy_score(y_predict, y_test)
print('{}% of samples classified correctly'.format(score * 100))

# Storing the model under 'model.p'
f = open('model.p', 'wb')
pickle.dump({'model': model}, f)
f.close()
