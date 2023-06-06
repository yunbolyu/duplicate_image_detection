from PIL import Image

def split_image(image_path, rows, columns):
    # 加载PNG图片
    image = Image.open(image_path)
    image = image.convert("RGB")  # 将图像转换为RGB模式

    # 获取图像尺寸和子图尺寸
    width, height = image.size
    sub_width = width // columns
    sub_height = height // rows

    # 切分图像并保存子图
    for i in range(rows):
        for j in range(columns):
            left = j * sub_width
            upper = i * sub_height
            right = left + sub_width
            lower = upper + sub_height

            sub_img = image.crop((left, upper, right, lower))
            sub_img.save(f'test_lisa/sub_{i}_{j}.jpg')

split_image('mona_lisa.png', 2, 4)  # 将'mona_lisa.png'切分为3x5个子图
