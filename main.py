from io import BytesIO

from PIL import Image

from GameDriver import GameDriver

print('Starting session!\n')

imgs = []
game_driver = GameDriver()

for i in range(10):
    print('\nStarting %ith game' % (i + 1))

    imgs.extend(game_driver.run_loop())
    print('Score:', game_driver.get_game_prop('distanceRan'))

game_driver.quit()

for i, base in enumerate(imgs):
    img = Image.open(BytesIO(base))
    img.save('img-%s.png' % i)

print('Session ended')
