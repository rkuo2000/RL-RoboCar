"""
The design of this comes from here:
http://outlace.com/Reinforcement-Learning-Part-3/
"""
from tensorflow.keras import models, layers, optimizers

class LossHistory():
    def on_train_begin(self, logs={}):
        self.losses = []

    def on_batch_end(self, batch, logs={}):
        self.losses.append(logs.get('loss'))


def neural_net(num_sensors, params, load=''):
    # Build Model    
    model = models.Sequential()
    # First layer.
    model.add(layers.Dense(params[0], activation='relu', input_shape=(num_sensors,)))
    model.add(layers.Dropout(0.2))
    # Second layer.
    model.add(layers.Dense(params[1], activation='relu'))
    model.add(layers.Dropout(0.2))
    # Output layer.
    model.add(layers.Dense(3, activation='linear'))

    model.summary()
    
    # Compile Model
    model.compile(loss='mse', optimizer='RMSprop')

    if load:
        model.load_weights(load)

    return model
