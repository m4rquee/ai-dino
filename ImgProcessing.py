from PIL import Image
from io import BytesIO


def prepare_img(png, img_rect):
    return Image.open(BytesIO(png)).convert('L').crop(img_rect)


def prepare_batch(batch, img_rect):
    return map(lambda png: prepare_img(png, img_rect), batch)
