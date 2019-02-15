from PIL import Image
from io import BytesIO

from selenium.webdriver.common.keys import Keys

from GameDriver import GameDriver

print('Starting session!\n')

imgs = []
game_driver = GameDriver()

for i in range(5):
    print('\nStarting %ith game' % (i + 1))
    game = game_driver.run_loop()

    for batch in game:
        imgs.extend(batch)
        game.send(Keys.ARROW_UP)

    print('Score:', game_driver.get_game_prop('distanceRan'))

game_driver.quit()

print('\nSaving images to files')
for i, base in enumerate(imgs):
    img = Image.open(BytesIO(base)).crop((0, 0, 350, 150))
    img.save('img-%s.png' % i)

print('\nSession ended')
