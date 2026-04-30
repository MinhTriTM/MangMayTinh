# Truy vấn Q3: Gộp ảnh thành PDF và chuyển đổi sang Markdown

## Câu hỏi
viết code gộp các file ảnh lại thành pdf rồi dùng @C:\tools\markitdown-0.1.5\run_markitdown.bat đểcho ra 1 file markdown

## Suy nghĩ
1.  **Mục tiêu**: Người dùng muốn gom tất cả ảnh trong thư mục hiện tại thành một file PDF, sau đó sử dụng một công cụ trích xuất text (markitdown) để chuyển PDF đó thành Markdown.
2.  **Công cụ**:
    *   Sử dụng Python với thư viện `Pillow` để gộp ảnh.
    *   Sử dụng `run_markitdown.bat` có sẵn tại `C:\tools\markitdown-0.1.5\`.
3.  **Quy trình**:
    *   Quét thư mục lấy danh sách file `.png`, `.jpg`.
    *   Sắp xếp file theo tên để đảm bảo thứ tự.
    *   Tạo script `merge_to_pdf.py` thực hiện việc gộp.
    *   Chạy script để tạo `Tai_Lieu_Gop.pdf`.
    *   Chạy lệnh shell gọi file batch để chuyển đổi sang Markdown.
4.  **Lưu ý**: Cần đảm bảo `Pillow` được cài đặt.

## Suy nghĩ
... (các bước trước)
5. **Sửa lỗi**: File `run_markitdown.bat` thực hiện lệnh `cd /d "%~dp0"`, dẫn đến việc nó tìm file PDF trong thư mục công cụ thay vì thư mục hiện tại. Tôi đã cập nhật `run_workflow.bat` để truyền đường dẫn tuyệt đối bằng biến `%cd%`.

## Câu trả lời
Tôi đã sửa lại file `run_workflow.bat` để truyền đường dẫn chính xác cho công cụ chuyển đổi. Bạn hãy chạy lại file này, nó sẽ tự động nhận diện file PDF đã tạo và chuyển đổi thành Markdown thành công.
