import os
from PIL import Image, ImageChops
import allure


def compare_screenshots(actual_path, expected_path, diff_dir):
    actual_image = Image.open(actual_path).convert("RGB")
    expected_image = Image.open(expected_path).convert("RGB")
    diff_image = ImageChops.difference(actual_image, expected_image)
    if diff_image.getbbox():
        contrast_diff = Image.new("RGB", actual_image.size, (255, 255, 255))
        for x in range(diff_image.width):
            for y in range(diff_image.height):
                if diff_image.getpixel((x, y)) != (0, 0, 0):
                    contrast_diff.putpixel((x, y), (255, 0, 0))
        os.makedirs(diff_dir, exist_ok=True)
        actual_image_path = os.path.join(diff_dir, 'Actual.png')
        expected_image_path = os.path.join(diff_dir, 'Expected.png')
        diff_image_path = os.path.join(diff_dir, 'Diff.png')

        actual_image.save(actual_image_path)
        expected_image.save(expected_image_path)
        contrast_diff.save(diff_image_path)

        allure.attach.file(actual_image_path, name="Actual Screenshot", attachment_type=allure.attachment_type.PNG)
        allure.attach.file(expected_image_path, name="Expected Screenshot", attachment_type=allure.attachment_type.PNG)
        allure.attach.file(diff_image_path, name="Diff Screenshot", attachment_type=allure.attachment_type.PNG)
        assert False, f"Differences found between Actual and Expected. Differences are stored in {diff_dir}"
    else:
        actual_image.close()
        expected_image.close()
