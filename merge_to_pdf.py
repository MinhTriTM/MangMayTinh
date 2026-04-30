import os
from PIL import Image

def merge_images_to_pdf(output_pdf_path):
    # Lấy danh sách các file ảnh
    valid_extensions = ('.png', '.jpg', '.jpeg')
    images = [f for f in os.listdir('.') if f.lower().endswith(valid_extensions)]
    
    # Loại bỏ file output cũ nếu có (tránh gộp chính nó nếu nó là ảnh - ở đây là PDF nên ko lo, nhưng cứ cẩn thận)
    images = [img for img in images if img != output_pdf_path]
    
    # Sắp xếp theo tên
    images.sort()
    
    if not images:
        print("Không tìm thấy file ảnh nào.")
        return

    print(f"Tìm thấy {len(images)} file ảnh. Đang tiến hành gộp...")

    image_list = []
    
    # Mở file đầu tiên
    first_image = Image.open(images[0]).convert('RGB')
    
    # Mở các file còn lại
    for img_path in images[1:]:
        img = Image.open(img_path).convert('RGB')
        image_list.append(img)
        
    # Lưu thành PDF
    first_image.save(output_pdf_path, save_all=True, append_images=image_list)
    print(f"Đã tạo file PDF thành công: {output_pdf_path}")

if __name__ == "__main__":
    merge_images_to_pdf("Tai_Lieu_Gop.pdf")
