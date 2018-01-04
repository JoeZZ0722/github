import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import MinMaxScaler

# fix random seed for reproducibility
numpy.random.seed(7)

# load the dataset
dataframe = pandas.read_excel('data01.xlsx', usecols=[1], sep = ',')
dataset1 = dataframe.values[:-45,]
dataset2 = dataframe.values[-45:-14,]
dataset1 = dataset1.astype('float32')
dataset2 = dataset2.astype('float32')

# normalize the dataset
scaler = MinMaxScaler(feature_range=(0, 1))
dataset1 = scaler.fit_transform(dataset1)
dataset2 = scaler.fit_transform(dataset2)

# split into train and test sets
train = dataset1
feed = dataset2
#print "train_data_size: "+str(len(train)), " test_data_size: "+str(len(test))

# convert an array of values into a dataset matrix
def create_dataset(dataset, look_back=1,look_ahead=1):
    dataX, dataY = [], []
    for i in range(1,(len(dataset)-look_back-look_ahead),look_back):
        a = dataset[i:(i+look_back), 0]
        dataX.append(a)
        dataY.append(dataset[(i + look_back):(i+look_back+look_ahead), 0])
    return numpy.array(dataX), numpy.array(dataY)

def create_dataset1(dataset, look_back=1):
    dataX = []
    for i in range(0,len(dataset),look_back):
        a = dataset[i:(i+look_back), 0]
        dataX.append(a)
    return numpy.array(dataX)

# reshape into X=t and Y=t+31
look_ahead = 31
look_back = 31
trainX, trainY = create_dataset(train, look_back,look_ahead)
feedX = create_dataset1(feed,look_back)

# reshape input to be [samples, time steps, features]
trainX = numpy.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
feedXX = numpy.reshape(feedX, (feedX.shape[0], 1, feedX.shape[1]))
#print feedXX

# create and fit the LSTM network
model = Sequential()
model.add(LSTM(5,input_shape=(1,31),return_sequences=True))
model.add(LSTM(16))
model.add(Dense(31))
model.compile(loss='mape', optimizer='adam')
model.fit(trainX, trainY, nb_epoch=150, batch_size=1, verbose=2)

# make predictions
testPredict = model.predict(feedXX)

# invert predictions
Predict = scaler.inverse_transform(testPredict)
feedXX = scaler.inverse_transform([feedXX])

print "train_data_size: "+str(len(train)), " test_data_size: "+str(len(feed))
print feedXX
# print Predict
print Predict[0][-31:-17]
print dataframe.values[-14:,0]

dataset3 = Predict[0][-17:]
rng = pandas.date_range('12/15/2017', periods=len(dataset3), freq='D')
df1 = pandas.DataFrame(dataset3,index=rng,columns=['DataflowByDay_4G_GB'])
df2 = pandas.read_excel('data01.xlsx',sep=',',index_col='Date')
df3 = pandas.concat([df2,df1],ignore_index= False)
df3.to_excel('data0112.xlsx')

Relative_error_rate = numpy.abs(Predict[0][-31:-17]-dataframe.values[-14:,0])/dataframe.values[-14:,0]*100
print ("Relative_error_rate:",Relative_error_rate)



