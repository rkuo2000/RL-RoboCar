"""
Once a model is learned, use this to play it.
"""

from flat_game import carmunk
import numpy as np
from nn import neural_net

NUM_SENSORS = 3

# for display screen
show_sensors = True
draw_screen = True

def play(model):

    car_distance = 0
    game_state = carmunk.GameState()


    # Do nothing to get initial.
    _, state = game_state.frame_step((2))

    # Move.
    while True:
        car_distance += 1

        # Choose action.
        action = (np.argmax(model.predict(state, batch_size=1)))

        # Take action.
        _, state = game_state.frame_step(action)

        # Tell us something.
        #if car_distance % 1000 == 0:
        #    print("Current distance: %d frames." % car_distance)
        print("frame no.: %d" % car_distance)
		
        if car_distance==1000: # just play for 1000 frames
            break


if __name__ == "__main__":
    saved_model = 'saved-models/128-128-64-50000-50000.h5'
    model = neural_net(NUM_SENSORS, [128, 128], saved_model)
    play(model)
