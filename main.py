import time

from GameDriver import GameDriver

game_driver = GameDriver()

print('Starting session!\n')

for i in range(1, 11):
    print('\nStarting %ith game' % i)
    game_driver.send_key()

    game_driver.run_loop()
    print('Score:', game_driver.get_game_prop('distanceRan'))
    time.sleep(1)

game_driver.quit()

print('Game session')
