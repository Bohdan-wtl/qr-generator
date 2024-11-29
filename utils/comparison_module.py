import shutil

from PIL import Image, ImageChops
import os
import allure
import json
import base64

# def compare_images(actual_path, expected_path, diff_dir, threshold=11, max_diff_percentage=11):
#     img1 = Image.open(actual_path).convert("RGB")
#     img2 = Image.open(expected_path).convert("RGB")
#     if img1.size != img2.size:
#         print(f"Images have different sizes: {img1.size} and {img2.size}")
#         img2 = img2.resize(img1.size)
#         img2.save(expected_path)
#     img1_np = np.array(img1)
#     img2_np = np.array(img2)
#     diff = np.abs(img1_np - img2_np)
#     if threshold > 0:
#         diff = np.where(diff > threshold, 255, 0)
#     diff_mask = np.zeros_like(img1_np)
#     diff_mask[:, :, 0] = diff.max(axis=2)
#     diff_mask_image = Image.fromarray(diff_mask)
#     diff_highlighted = Image.blend(img1, diff_mask_image, alpha=0.5)
#     if not os.path.exists(diff_dir):
#         os.makedirs(diff_dir)
#     diff_path = os.path.join(diff_dir, "difference.png")
#     diff_highlighted.save(diff_path)
#     diff_percentage = np.mean(diff) / 255 * 100
#
#     with allure.step("Images difference check"):
#         allure.attach.file(actual_path, name="Actual Image", attachment_type=allure.attachment_type.PNG)
#         allure.attach.file(expected_path, name="Expected Image", attachment_type=allure.attachment_type.PNG)
#         allure.attach.file(diff_path, name="Difference Image", attachment_type=allure.attachment_type.PNG)
#
#         assert diff_percentage <= max_diff_percentage, f"Difference percentage is {diff_percentage:.2f}%"
#
#     return diff_path, diff_percentage

def allure_attach_image_diff(actual_path, expected_path, diff_dir, max_diff_percentage=11.0, diff_name="difference.png"):
    os.makedirs(diff_dir, exist_ok=True)
    diff_path = os.path.join(diff_dir, diff_name)
    img1 = Image.open(actual_path).convert("RGB")
    img2 = Image.open(expected_path).convert("RGB")
    if img1.size != img2.size:
        print(f"Images have different sizes: {img1.size} and {img2.size}")
        img2 = img2.resize(img1.size)
        img2.save(expected_path)

    diff_img = ImageChops.difference(img1, img2)
    diff_img.save(diff_path)

    diff_pixels = sum(1 for x in range(diff_img.width) for y in range(diff_img.height) if diff_img.getpixel((x, y)) != (0, 0, 0))
    total_pixels = diff_img.width * diff_img.height
    diff_percentage = (diff_pixels / total_pixels) * 100

    with open(expected_path, "rb") as expected_file:
        expected = base64.b64encode(expected_file.read()).decode()
    with open(actual_path, "rb") as actual_file:
        actual = base64.b64encode(actual_file.read()).decode()
    with open(diff_path, "rb") as diff_file:
        diff = base64.b64encode(diff_file.read()).decode()

    content = json.dumps({
        'expected': f'data:image/png;base64,{expected}',
        'actual': f'data:image/png;base64,{actual}',
        'diff': f'data:image/png;base64,{diff}',
    }).encode()
    allure.attach(content, name='Screenshot diff', attachment_type='application/vnd.allure.image.diff')
    assert diff_percentage <= max_diff_percentage, f"Difference percentage is {diff_percentage:.2f}%"
    shutil.rmtree.shutil("artifacts/snapshots")
