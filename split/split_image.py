from PIL import Image

def split_image(img_path, row, col):
    img = Image.open(img_path)
    w, h = img.size
    sw, sh = w // col, h // row  # 每个子图的宽度和高度

    for i in range(row):
        for j in range(col):
            sub_img = img.crop((j*sw, i*sh, (j+1)*sw, (i+1)*sh))
            sub_img.save(f'sub_{i}_{j}.jpg')

split_image('test_1.jpg', 3, 5)  # 将'your_image.jpg'切分为3x5个子图
