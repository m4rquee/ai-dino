def prepare_img(image, img_rect):
    return image.convert('L').crop(img_rect)


def prepare_batch(batch, img_rect):
    return map(lambda png: prepare_img(png, img_rect), batch)
