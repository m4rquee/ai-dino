import numpy as np

from DinoNN import DinoNN
from GameDriver import GameDriver

print('Starting session!\n')

brain = DinoNN((35, 0, 225, 130))
game_driver = GameDriver()
game_driver.init()

for i in range(1, 6):
    print('\nStarting %ith game' % i)
    game = game_driver.run_loop()

    for batch in game:
        q_values = brain.map(batch)
        game.send(game_driver.keys[np.argmax(q_values)])

    print('Score:', game_driver.get_score())

game_driver.quit()

print('\nSession ended')
