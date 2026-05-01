# CHƯƠNG 7: TRẮC NGHIỆM AN NINH MẠNG MÁY TÍNH

**Câu 1:** Một tin tặc chặn đường truyền, sửa đổi số tiền trong gói tin chuyển khoản ngân hàng từ 100 USD thành 1.000.000 USD trước khi nó đến được máy chủ ngân hàng. Hành vi này đã phá vỡ thuộc tính cốt lõi nào của an toàn mạng?
A. Tính Bảo mật (Confidentiality).
B. Xác thực thiết bị cuối (End-point Authentication).
C. Tính Toàn vẹn thông điệp (Message Integrity).
D. Tính Sẵn sàng (Availability).
*Đáp án: C*
*Giải thích: Tính Toàn vẹn (Integrity) đảm bảo dữ liệu không bị ai đó chèn, xóa hay chỉnh sửa lén lút trên đường truyền. Hàm băm MAC hoặc Chữ ký số giải quyết vấn đề này.*

**Câu 2:** Việc sử dụng một "Đội quân" hàng ngàn máy tính bị nhiễm mã độc (Botnet) cùng đồng loạt gửi các truy vấn rác về làm sập trang web của đối thủ được gọi là loại hình tấn công gì?
A. Phishing (Câu cá).
B. Man-in-the-Middle (Người đứng giữa).
C. Ransomware.
D. DDoS (Distributed Denial of Service - Từ chối dịch vụ phân tán).
*Đáp án: D*
*Giải thích: DDoS vắt kiệt băng thông hoặc tài nguyên CPU/RAM của mục tiêu khiến nó không thể phục vụ khách hàng hợp pháp.*

**Câu 3:** Thuật toán RSA dựa trên bài toán toán học khó giải nào để tạo ra sức mạnh mã hóa?
A. Đảo ngược các bit 0 và 1.
B. Chia lấy dư một đa thức lớn.
C. Bài toán phân tích thừa số nguyên tố của một số nguyên siêu lớn.
D. Sắp xếp ma trận Rubik.
*Đáp án: C*
*Giải thích: Sức mạnh của khóa Công khai/Bí mật RSA phụ thuộc vào việc tìm ra 2 số nguyên tố cấu thành một số cực lớn (tốn hàng vạn năm máy tính tính toán).*

**Câu 4:** Hệ thống Mật mã Khóa Đối xứng (Symmetric Key) và Bất đối xứng (Public Key) có đặc điểm tốc độ chênh lệch thế nào?
A. Public Key mã hóa nhanh hơn Symmetric Key.
B. Cả hai chạy nhanh bằng nhau do đều dùng chung chip phần cứng.
C. Symmetric Key (như AES) có tốc độ siêu nhanh (nhanh hơn hàng ngàn lần) so với Public Key (như RSA). Do đó Public Key hầu như không dùng để mã hóa nội dung dữ liệu lớn.
D. Public Key không mã hóa được tệp tin video.
*Đáp án: C*
*Giải thích: RSA yêu cầu các phép nâng lên lũy thừa số khổng lồ, làm CPU quá tải. Vì vậy mạng máy tính kết hợp cả hai: Dùng RSA trong 1 giây đầu để tuồn lén Khóa Đối xứng qua mạng, sau đó dùng Khóa Đối xứng để mã hóa dữ liệu thực.*

**Câu 5:** Giá trị Hash (Mã Băm) do các thuật toán như SHA-256 tạo ra có tính chất quan trọng nào để trở thành "vân tay" của một tệp tin?
A. Kích thước mã băm thay đổi tỷ lệ thuận với dung lượng file gốc.
B. Hoàn toàn có thể dùng mã băm để giải nén lại thành file gốc (Có thể đảo ngược).
C. Bất khả nghịch (không thể dịch ngược thành file gốc) và cực kỳ khó để tạo ra hai tệp tin khác nhau nhưng lại xuất ra cùng một mã băm (Tính chống đụng độ).
D. Mỗi máy tính khi băm cùng một file sẽ ra mã khác nhau.
*Đáp án: C*
*Giải thích: Chỉ cần thay đổi 1 dấu phẩy trong file Word 10GB, mã băm SHA-256 cũng sẽ biến đổi thành một chuỗi Hexadecimal sai khác hoàn toàn.*

**Câu 6:** Một bức thư được ký bằng Chữ ký Số (Digital Signature) thực hiện bởi Alice được gửi cho Bob. Để xác thực đây ĐÚNG LÀ chữ ký của Alice chứ không phải bị giả mạo, Bob phải dùng chìa khóa nào để MỞ khóa chữ ký?
A. Khóa Bí mật của Alice.
B. Khóa Công khai của Bob.
C. Khóa Bí mật của Bob.
D. Khóa Công khai (Public Key) của Alice.
*Đáp án: D*
*Giải thích: Quy tắc vàng của Bất đối xứng: Alice niêm phong chữ ký bằng KHÓA BÍ MẬT của riêng cô ấy. Do đó, DUY NHẤT Khóa CÔNG KHAI của cô ấy mới có thể giải được niêm phong đó. Bất kỳ ai mở được đều phải công nhận người tạo là Alice.*

**Câu 7:** Để chứng minh cho Bob biết cái Khóa Công Khai (Public Key) mà anh ta nhận được TỪ INTERNET là đồ "chính chủ" của Alice chứ không phải do hacker Tráo đổi (Man-in-the-middle), Bob cần kiểm tra cái gì?
A. Nhìn xem chữ cái có viết hoa không.
B. Kiểm tra IP của Alice.
C. Đọc tờ Chứng chỉ Số (Digital Certificate) của Alice, xem nó có mang Chữ Ký bảo lãnh của một Tổ chức Cấp Chứng thực (CA) đáng tin cậy không.
D. Yêu cầu Alice đọc lại Khóa Công Khai qua điện thoại di động.
*Đáp án: C*
*Giải thích: Chứng chỉ số là thẻ Căn cước Công dân của thế giới số. CA (như VeriSign) đóng vai trò Công an đóng dấu đỏ khẳng định Khóa này thuộc về thực thể nào.*

**Câu 8:** Các cuộc tấn công "SQL Injection" vào dữ liệu website hay bẻ khóa mật khẩu người dùng sẽ đi qua lớp bảo vệ nào nếu Tường lửa (Firewall) cấu hình sai?
A. Đi qua lớp Packet Filter (Lọc IP và Port).
B. Đi qua lớp Physical.
C. Đi qua Tường lửa phần cứng nhưng bị chặn ở Tầng Liên Kết.
D. Tường lửa luôn luôn chặn được SQL Injection.
*Đáp án: A*
*Giải thích: Tường lửa lọc gói tin (Packet Filter) chỉ nhìn vỏ ngoài (Port 80/443). Do SQL Injection ngụy trang trong gói tin HTTP hợp lệ, Tường lửa truyền thống sẽ mù lòa mở cửa cho nó đi qua. Cần có IDS/IPS kiểm tra sâu (DPI) để chặn.*

**Câu 9:** HTTPS là giao thức kết hợp giữa HTTP truyền thống và cái gì?
A. IPsec (Bảo mật Tầng Mạng).
B. SSL / TLS (Bảo mật Tầng Giao vận).
C. WPA2 (Bảo mật Wi-Fi).
D. PGP (Bảo mật Email).
*Đáp án: B*
*Giải thích: SSL/TLS chèn một tầng mã hóa ngay bên trên TCP. Khi HTTP đẩy văn bản rõ xuống, TLS sẽ băm và khóa nó thành mớ hỗn độn rồi mới giao cho TCP truyền đi.*

**Câu 10:** Khi thiết lập IPsec (Mạng riêng ảo VPN) để nối thông hai văn phòng, các gói tin dữ liệu bên trong mạng LAN của chi nhánh sẽ được bảo vệ ra sao?
A. Chỉ mã hóa được nội dung web.
B. Được tự động mã hóa TẤT CẢ, bất kể đó là gói tin ứng dụng gì (Web, FTP, Game, Ping), vì IPsec hoạt động mã hóa trong suốt ở mức Tầng Mạng (Network Layer).
C. Được tải lên đám mây.
D. Phải dùng cáp riêng không qua Internet.
*Đáp án: B*
*Giải thích: IPsec nén toàn bộ IP Datagram gốc (kể cả Header IP gốc) vào trong Payload của một IP Datagram IPsec mới, mã hóa sạch sành sanh.*

**Câu 11:** Trong các Firewall (Tường lửa), loại "Stateful Packet Inspection" (Kiểm tra gói tin có trạng thái) cải tiến được nhược điểm nào của bộ lọc cũ?
A. Nó không cần CPU để chạy.
B. Thay vì chỉ kiểm tra từng gói tin rời rạc tĩnh, nó có "Trí nhớ" duy trì một Bảng theo dõi trạng thái các kết nối TCP hiện tại. Nhờ vậy nó biết gói tin đến có thuộc một luồng giao tiếp hợp pháp đang diễn ra hay là một gói rác đột ngột xâm nhập.
C. Nó mã hóa toàn bộ dữ liệu.
D. Nó tìm được địa chỉ nhà của hacker.
*Đáp án: B*
*Giải thích: Nếu một gói tin mang cờ ACK lao từ Internet vào LAN mà trong Bảng trạng thái không hề có kết nối SYN nào được mở ra trước đó, Stateful Firewall sẽ Drop ngay lập tức.*

**Câu 12:** Tính năng DPI (Deep Packet Inspection - Kiểm tra sâu) của thiết bị IDS làm gì?
A. Nó đo cáp mạng chìm dưới đáy biển.
B. Nó lột lớp vỏ TCP/IP để soi thẳng vào ruột Payload Tầng Ứng dụng xem có chứa chuỗi mã độc (Signatures) hoặc hành vi đáng ngờ không.
C. Nó tìm IP của người dùng.
D. Nó chia nhỏ Datagram ra sâu hơn MTU.
*Đáp án: B*
*Giải thích: Giống như Hải quan mở toang vali hàng hóa ra kiểm tra, DPI tốn cực kỳ nhiều CPU và tài nguyên mạng, bù lại có khả năng chống chọi hầu hết sự xâm nhập.*

**Câu 13:** Mã hóa DES (Data Encryption Standard) với khóa 56 bit bị coi là "Cổ vật" không an toàn ở hiện tại do đâu?
A. Giao diện quá xấu.
B. Chiều dài chìa khóa (Key) 56 bit là quá ngắn. Máy tính hiện đại, card màn hình có thể sử dụng phương pháp "Vét cạn" (Brute-force) thử hết 2^56 chìa khóa để bẻ khóa trong vòng 1-2 ngày.
C. Do không cài được trên Windows.
D. Do Microsoft chặn thuật toán.
*Đáp án: B*
*Giải thích: Thuật toán mật mã học bị đánh bại bởi tốc độ vi xử lý tăng theo định luật Moore. Ngày nay khóa tối thiểu của AES là 128 bits, mạnh hơn tỷ tỷ tỷ lần.*

**Câu 14:** Giao thức nào cung cấp bảo mật (Mã hóa và Xác thực) trên kênh truyền Không dây (Wi-Fi)?
A. OSPF
B. WEP, WPA2, WPA3
C. IPsec
D. TLS
*Đáp án: B*
*Giải thích: Chuẩn bảo mật WPA (đặc biệt bản mới nhất WPA3) sử dụng AES để mã hóa các khung vô tuyến (Frame) trực tiếp trước khi phát ra ăng ten.*

**Câu 15:** Vì sao hiện tượng "Packet Sniffing" lại đặc biệt nguy hiểm trên môi trường kết nối Wi-Fi công cộng ở quán cà phê?
A. Vì Wi-Fi công cộng miễn phí cước.
B. Vì sóng Wi-Fi phát tán tứ phía vào không trung. Ai trong quán cũng có thể cài phần mềm bắt được toàn bộ các gói tin bay qua lại của máy tính khác. Nếu không dùng HTTPS, mật khẩu sẽ lộ rõ như ban ngày.
C. Vì Wi-Fi ở quán cafe dùng cáp đồng hỏng.
D. Vì quán cafe thường lắp camera quan sát.
*Đáp án: B*
*Giải thích: Khác với mạng dây (cắm switch) được cô lập, mạng vô tuyến là mạng phát thanh. Hacker chỉ việc dùng card mạng chế độ Promiscuous (Nghe trộm) là thu thập được mọi thứ.*

**Câu 16:** Bạn nhận được email từ ngân hàng yêu cầu nhấp vào link "http://192.168.12.1/login" thay vì "https://bank.com" để cấp lại mật khẩu. Kẻ tấn công đang dùng thủ đoạn nào?
A. DoS Flooding.
B. Man in the Middle.
C. Phishing (Tấn công lừa đảo / Câu cá) kết hợp tạo trang giả.
D. Mã hóa tống tiền.
*Đáp án: C*
*Giải thích: Lợi dụng sự nhẹ dạ và thiếu kỹ năng, hacker gửi một giao diện giống hệt trang thật (nhưng IP/Domain fake) dụ người dùng tự điền pass.*

**Câu 17:** Thuật ngữ "Zero-day exploit" trong an ninh mạng mô tả sự kiện nào?
A. Sự cố mạng mất kết nối vào ngày đầu năm mới.
B. Lỗ hổng bảo mật chưa từng được ai (kể cả nhà sản xuất) biết tới, bị hacker phát hiện và khai thác tận dụng (exploit) trước khi bản vá lỗi kịp tung ra.
C. Mã hóa ổ cứng trong vòng 0 ngày.
D. Việc khởi động lại máy chủ mỗi ngày để xóa bộ nhớ.
*Đáp án: B*
*Giải thích: Zero-day là vũ khí đáng sợ nhất vì không có Antivirus hay Tường lửa nào chặn được nó (vì chưa hề có cơ sở dữ liệu mẫu nhận diện).*

**Câu 18:** Khái niệm "Operational Security" bao gồm các công tác gì để giữ an toàn tổ chức?
A. Cập nhật phần mềm định kỳ, sử dụng Mật khẩu phức tạp đổi định kỳ, sao lưu dữ liệu (Backup), phân quyền hạn chế (Zero Trust), giáo dục nhận thức nhân viên.
B. Chỉ việc mua thiết bị của Cisco.
C. Kéo dây cáp đi qua đường hầm dưới lòng đất.
D. Chỉ sử dụng IPv6.
*Đáp án: A*
*Giải thích: Bạn có thể lắp Tường lửa 1 triệu đô, nhưng nhân viên viết Pass ra giấy nhớ dán lên màn hình thì mạng vẫn sập. Operational Security là việc duy trì quy trình vận hành an toàn.*

**Câu 19:** Mã độc Ransomware hoạt động theo cơ chế nào để tống tiền nạn nhân?
A. Khóa màn hình máy tính lại không cho hiện hình ảnh.
B. Bí mật xâm nhập, lén lút quét tất cả các file tài liệu quan trọng trên đĩa cứng và mã hóa chúng bằng Mã hóa Bất đối xứng (hoặc kết hợp) theo khóa nằm ở máy chủ hacker. Xong xuôi nó xóa file gốc, ép người dùng trả tiền điện tử (Bitcoin) để mua chìa khóa giải mã.
C. Mở loa ngoài to hết cỡ.
D. Truyền vi-rút vào thẻ tín dụng.
*Đáp án: B*
*Giải thích: Mã hóa là công cụ bảo vệ dữ liệu, nhưng Ransomware dùng chính thanh gươm này để phong ấn file nạn nhân thành rác nếu không trả tiền chuộc.*

**Câu 20:** Làm sao để hạn chế cuộc tấn công giả mạo IP (IP Spoofing)?
A. Đóng tất cả các cổng trên Router.
B. Xóa IP cũ nhập IP mới.
C. Các ISP cấu hình Tường lửa/Router kiểm tra tính xác thực của luồng IP: Nếu Router ở mạng nội bộ 10.0.0.x lại nhận được một gói tin có IP Nguồn ghi từ Mỹ đi ra từ mạng nội bộ, router sẽ chặn Drop ngay. Đây gọi là Lọc ở đường ra (Egress Filtering).
D. Không dùng cáp Ethernet.
*Đáp án: C*
*Giải thích: Nhà ai nấy giữ. Router ở mạng X không được phép xuất hành bất kỳ gói tin nào mang IP nguồn mạo danh Y ra ngoài thế giới Internet.*

**Câu 21:** Quá trình "Thỏa thuận khóa phiên" (Session Key Negotiation) trong bước bắt tay giao thức TLS/SSL dùng kỹ thuật gì?
A. Hash mật khẩu của người dùng.
B. Client sinh ngẫu nhiên một Khóa Đối xứng (Session Key), dùng Public Key lấy từ Chứng chỉ số của Server để khóa nó lại, và gửi cục đã khóa lên cho Server.
C. Server sinh ra mã băm MD5 và dùng Private Key mã hóa.
D. IPsec tự động phân phát khóa bằng UDP.
*Đáp án: B*
*Giải thích: Đưa khóa đối xứng qua mạng là điều tối kỵ. Nhưng nhờ Public Key của Server (an toàn tuyệt đối), Client bỏ Session Key vào đó, đóng kín lại. Ai bắt được cục hàng đó trên mạng cũng bó tay, chỉ có Server mới có Private Key để tự mở ra lấy Session Key.*

**Câu 22:** Một Tường lửa (Firewall) cấu hình "Default Deny" (Cấm mặc định) hoạt động theo triết lý gì?
A. Mở cửa tất cả, chỉ cấm các IP nằm trong danh sách đen (Blacklist).
B. Đóng cửa hoàn toàn, không có gói tin nào lọt vào. Bắt buộc phải thêm các ngoại lệ (Whitelist) một cách cực kỳ chi tiết cho những dịch vụ nào được phép lưu thông.
C. Mặc định chỉ cấm ban ngày.
D. Cấm tất cả các lệnh Ping.
*Đáp án: B*
*Giải thích: Tương tự như an ninh sân bay, mặc định là không ai được vào. Chứ không phải thả cửa cho tất cả vào trừ tội phạm truy nã (Default Allow).*

**Câu 23:** Khác biệt giữa Hệ thống phát hiện xâm nhập (IDS) và Hệ thống ngăn chặn xâm nhập (IPS) là gì?
A. Cả hai là một.
B. IDS chỉ cảnh báo (Báo động cho quản trị viên, gửi email), còn IPS thì cảnh báo VÀ tự động đưa ra các hình phạt thực tế (như cắt đứt đường cáp kết nối (Drop) của hacker đang tấn công, cập nhật tường lửa).
C. IPS hoạt động trên Tầng Giao vận, IDS trên Tầng Vật lý.
D. IDS đắt hơn IPS.
*Đáp án: B*
*Giải thích: Detection (Phát hiện) chỉ có chức năng nhìn thấy và la lên. Prevention (Ngăn chặn) có thẩm quyền hành động ngay tại chỗ.*

**Câu 24:** Thuật toán mã hóa khóa Công khai RSA được đặt tên theo điều gì?
A. Thuật toán do Nga thiết kế (Russian Security Algorithm).
B. Tên của trường Đại học nghiên cứu ra nó.
C. Chữ cái đầu tên của 3 nhà phát minh: Ron Rivest, Adi Shamir, và Leonard Adleman.
D. Rất Siêu An toàn.
*Đáp án: C*
*Giải thích: Bộ ba này tại Viện MIT đã tạo ra RSA vào năm 1977, trở thành công nghệ mật mã vĩ đại nhất lịch sử Internet.*

**Câu 25:** Kỹ thuật "Salting" (Rắc muối) khi băm (Hashing) lưu trữ mật khẩu trong cơ sở dữ liệu giải quyết vấn đề gì?
A. Tạo ra mã băm nhỏ hơn.
B. Nếu có hai người dùng đặt cùng một mật khẩu yếu (vd: "123456"), bằng cách ghép thêm một chuỗi "muối" ngẫu nhiên khác nhau vào mật khẩu mỗi người trước khi Hash, mã băm đầu ra sẽ hoàn toàn khác biệt. Giúp chống lại các cuộc tấn công tra bảng băm làm sẵn (Rainbow Tables).
C. Để mật khẩu nhanh được gửi lên hệ thống.
D. Để phá vỡ tường lửa.
*Đáp án: B*
*Giải thích: Muối là chuỗi sinh ngẫu nhiên. Password "123456" + Muối "A" -> Hash X. Password "123456" + Muối "B" -> Hash Y. Hacker trộm data thấy X và Y khác nhau không biết là trùng pass.*

**Câu 26:** Chứng chỉ khóa công khai (X.509) do CA cấp thường bị mất hiệu lực vì nguyên nhân nào phổ biến nhất?
A. CA xóa sổ công ty.
B. Hết thời hạn chứng chỉ (Expiration Date) hoặc bị rò rỉ khóa bí mật của máy chủ khiến CA phải thêm nó vào danh sách Thu hồi Chứng chỉ (CRL - Certificate Revocation List).
C. Thiết bị máy chủ khởi động lại.
D. Bị hacker đổi tên.
*Đáp án: B*
*Giải thích: Tương tự như thẻ ATM, chứng chỉ chỉ sống 1-3 năm. Hoặc nếu bạn báo mất khóa bí mật, CA sẽ đưa chứng chỉ của bạn vào "Danh sách đen" (CRL) để các trình duyệt từ chối.*

**Câu 27:** Các thuật toán mã hóa (AES, RSA) có bị hacker bẻ khóa theo thời gian không?
A. Không bao giờ. Chúng được chứng minh toán học bất khả chiến bại.
B. Có, vì theo Định luật Moore, năng lực vi xử lý (CPU/GPU) tăng liên tục khiến việc Vét cạn (Brute-force) những chiều dài khóa ngắn trở nên khả thi. Và nguy cơ tương lai đến từ sức mạnh của Máy tính Lượng tử.
C. Do máy chủ tự sinh ra lỗi.
D. Tự khóa sẽ hết hạn sau 1 năm.
*Đáp án: B*
*Giải thích: Mã hóa không phải là giấu cách làm (Kerckhoffs's principle). Nó phụ thuộc hoàn toàn vào độ to của chìa khóa. Siêu máy tính cần hàng tỷ năm giải bài toán RSA 2048, nhưng máy lượng tử (Shor's Algorithm) có thể giải trong vài ngày.*

**Câu 28:** VPN (Virtual Private Network) tạo đường hầm ở lớp nào nếu triển khai bằng giao thức IPsec?
A. Lớp Mạng (Network Layer).
B. Lớp Liên kết dữ liệu (Data Link).
C. Lớp Phiên (Session).
D. Lớp Vật lý (Physical).
*Đáp án: A*
*Giải thích: Lớp Mạng (Layer 3) là ngôi nhà của giao thức IP. IPsec hoạt động ở đây che chở trong suốt cho các gói tin Layer 4 bên trên.*

**Câu 29:** Cuộc tấn công Man-in-the-Middle (MITM) là việc hacker chen vào giữa Alice và Bob. Làm sao để chặn triệt để MITM trên kết nối Web?
A. Gửi dữ liệu vào ban đêm.
B. Phân mảnh gói tin làm đôi.
C. Sử dụng Chứng chỉ SSL/TLS được chứng thực bởi CA uy tín, khiến cho hacker không thể làm giả chứng chỉ giả mang Public Key của hắn (vì hacker không có Private Key của CA).
D. Dùng TCP thay cho UDP.
*Đáp án: C*
*Giải thích: Khi hacker chen giữa gửi cái Public Key của hắn cho Alice (giả vờ hắn là Bob), trình duyệt của Alice sẽ báo lỗi ngay lập tức vì cái Public key đó KHÔNG CÓ chữ ký chứng nhận của CA.*

**Câu 30:** Một ứng dụng nhắn tin bảo mật như Signal hay WhatsApp thường quảng bá tính năng E2EE (End-to-End Encryption). Nó có ý nghĩa gì?
A. Nghĩa là ứng dụng miễn phí.
B. Dữ liệu được mã hóa suốt quãng đường. Thậm chí chính máy chủ trung gian của công ty Signal/WhatsApp cũng KHÔNG có chìa khóa để giải mã tin nhắn, mà chỉ có 2 cái điện thoại ở 2 đầu mới có chìa khóa.
C. Nó mã hóa toàn bộ hình ảnh thành văn bản.
D. Nghĩa là gọi video không bị giật lag.
*Đáp án: B*
*Giải thích: E2E có nghĩa mã hóa và giải mã chỉ xảy ra tại thiết bị của người sử dụng (End-systems). Máy chủ của hãng chỉ làm trạm bưu điện chuyển cục gạch mã hóa, nên cảnh sát có đòi thu giữ server cũng vô ích.*

**Câu 31:** Mật mã Đối xứng (Symmetric-key cryptography) có một hạn chế (nhược điểm) CHÍ TỬ nhất trong môi trường mạng diện rộng là gì?
A. Tốc độ mã hóa quá chậm.
B. Vấn đề "Phân phối Khóa" (Key Distribution Problem). Hai bên giao tiếp (Ví dụ: Server Mỹ và Trình duyệt VN) CHƯA TỪNG GẶP NHAU bao giờ, làm sao để Gửi một chiếc Chìa Khóa Bí Mật chung duy nhất qua mạng Internet cho nhau mà không bị Kẻ nghe lén (Sniffer) trên đường chép lại chìa khóa đó?
C. Không thể mã hóa video.
D. Độ dài khóa quá lớn không lưu được vào RAM.
*Đáp án: B*
*Giải thích: Nếu tôi gửi chìa khóa vào phong bì, thằng hải quan sẽ bóc phong bì sao chép chìa khóa rồi dán lại. Sau này tôi gửi tài liệu (mã hóa), nó có chìa khóa, nó sẽ đọc được. Giải pháp là Mật mã Bất đối xứng (Public Key) của Diffie-Hellman.*

**Câu 32:** Hệ thống Mật mã Bất đối xứng (Asymmetric-key / Public-key cryptography) như RSA hoạt động dựa trên cơ chế:
A. Sử dụng cùng 1 chìa khóa cho cả 2 bên.
B. Mỗi người sở hữu MỘT CẶP KHÓA (1 Khóa Công khai - Public Key để phơi bày cho toàn thế giới, và 1 Khóa Bí mật - Private Key giữ chết trong người).
C. Không dùng khóa, chỉ dùng mã Hash.
D. Dựa vào địa chỉ MAC để tạo khóa.
*Đáp án: B*
*Giải thích: Ý tưởng điên rồ thay đổi nhân loại: Một cái ổ khóa có 2 chìa. Nếu Khóa bằng Chìa số 1, thì CHỈ CÓ THỂ mở bằng Chìa số 2. Nếu Khóa bằng Chìa số 2, thì CHỈ CÓ THỂ mở bằng Chìa số 1.*

**Câu 33:** Ứng dụng RSA vào Bảo mật: Nếu Alice muốn gửi một bức thư "Bí mật tuyệt đối" (Confidentiality) không ai đọc được cho Bob, Alice phải làm gì?
A. Mã hóa thư bằng Khóa Bí Mật của Alice.
B. Mã hóa thư bằng Khóa Bí Mật của Bob.
C. Lấy Khóa Công Khai (Public Key) của Bob (đang public trên mạng) để Mã Hóa thư. Bức thư đó giờ đây trở thành rác. CHỈ DUY NHẤT Bob dùng Khóa Bí Mật (Private Key) của chính anh ta mới giải mã được.
D. Bỏ qua mã hóa.
*Đáp án: C*
*Giải thích: Ổ khóa công khai của Bob gửi cho mọi người. Ai cũng có thể Bấm khóa gửi đồ cho Bob. Nhưng chỉ có Bob giữ Chìa khóa Bí mật để mở hộp.*

**Câu 34:** Ngược lại, nếu Alice muốn KÝ SỐ (Digital Signature) vào 1 Hợp đồng Điện tử để Gửi cho Bob, chứng minh rằng ĐÚNG LÀ ALICE KÝ (Không thể chối bỏ - Non-repudiation) và Bản Hợp Đồng CHƯA BỊ SỬA ĐỔI, Alice phải làm gì?
A. Mã hóa bản hợp đồng bằng Khóa Công khai của Bob.
B. Gửi qua cáp quang siêu bảo mật.
C. Alice dùng Khóa Bí Mật (Private Key) CỦA CHÍNH ALICE để "Mã hóa" một Bản Băm (Hash) của Hợp đồng. Bất kỳ ai (như Bob) dùng Khóa Công Khai của Alice đều "Giải mã" được Bản Băm đó. Sự "Giải mã thành công" chứng minh 100% người dùng Private Key đó là Alice.
D. Nhờ Google xác thực.
*Đáp án: C*
*Giải thích: Đây là linh hồn của Chữ ký điện tử VNPT/Viettel mà dân kế toán hay cắm USB Token để khai báo thuế. Bạn khóa bằng Private Key, thế giới mở bằng Public Key của bạn.*

**Câu 35:** Kẻ tấn công Man-in-the-Middle (Kẻ Trung Gian) lách qua Mật mã Bất đối xứng bằng thủ đoạn vô cùng nguy hiểm nào nếu không có Chứng chỉ số (Certificate)?
A. Đánh sập điện lưới máy chủ.
B. Trộm Khóa Bí mật.
C. Khi Alice xin Public Key của Bob. Kẻ Trung Gian (Trudy) đứng giữa CHẶN LẠI. Trudy gửi Public Key CỦA TRUDY cho Alice (nhưng giả danh là của Bob). Alice ngây thơ tin tưởng, dùng Public Key (của Hacker Trudy) để mã hóa dữ liệu nhạy cảm gửi đi. Trudy bắt được, dùng Private Key của mình mở ra lấy thẻ tín dụng, xong khóa lại bằng Public Key thật của Bob chuyển tiếp cho Bob để xóa dấu vết.
D. Rút cáp mạng.
*Đáp án: C*
*Giải thích: Bài toán lòng tin. Làm sao Alice biết cái Public Key vừa hiện lên trên màn hình ĐÚNG THẬT SỰ là của con ngừoi tên Bob chứ không phải của 1 thằng ất ơ ở nhà kế bên?*

**Câu 36:** Cơ quan Chứng nhận Số (Certificate Authority - CA) giải quyết Bài toán Lòng tin (Câu 35) cho toàn Internet bằng cách nào?
A. Sinh ra IP mới.
B. CA đóng vai trò là "Phòng Công Chứng" của Internet. CA dùng Khóa Bí Mật Cực Kỳ Siêu Bảo Mật của CA để KÝ SỐ LÊN cái Public Key của Bob. Tạo ra một tờ giấy chứng nhận: "Tôi là CA, tôi xin thề cái Public Key XYZ này ĐÚNG LÀ của Tổ chức tên Bob".
C. Cấm người dùng Internet giao dịch.
D. Chạy qua VPN.
*Đáp án: B*
*Giải thích: Máy tính Windows/Mac cài sẵn Public Key của các CA uy tín trên thế giới (như VeriSign, DigiCert) vào hệ điều hành. Do đó, Trình duyệt luôn tự động kiểm tra Dấu Mộc Đỏ của CA trước khi giao dịch với Trang Web lạ.*

**Câu 37:** Mã hóa Bất đối xứng (RSA) siêu bảo mật, thế nhưng HTTPS (SSL/TLS) chỉ dùng nó ở vài mili-giây Bắt tay ban đầu (Handshake) rồi SAU ĐÓ VỨT BỎ KHÔNG DÙNG NỮA để mã hóa Dữ liệu Phim/Ảnh, lý do là:
A. Vì RSA không mã hóa được phim.
B. Thuật toán toán học của RSA (Tính toán Số nguyên tố khổng lồ) tốn CHU KỲ CPU và TỐC ĐỘ cực kỳ khủng khiếp (Chậm hơn Mật mã Đối xứng như AES khoảng 100 đến 1000 lần). Nếu dùng RSA mã hóa luồng Video 4K thì Server sẽ cháy CPU và mạng giật tung chảo.
C. Vì BGP cấm RSA.
D. Do lỗi HĐH.
*Đáp án: B*
*Giải thích: Ứng dụng thực tế của TLS: Nó dùng RSA (Chậm/Bảo mật) để GỬI TÍN HIỆU THỎA THUẬN TẠO MỘT CÁI CHÌA KHÓA CHUNG MỚI TINH (Session Key / Khóa Đối xứng AES). Sau khi chốt xong chìa khóa đó, 2 bên dùng nó để mã hóa Phim/Ảnh ở Tốc độ bàn thờ.*

**Câu 38:** Giao thức IPsec (Internet Protocol Security) cung cấp 2 giao thức con để bảo vệ Datagram L3. "AH" (Authentication Header) làm nhiệm vụ gì?
A. Cung cấp chức năng Mã hóa toàn bộ dữ liệu (Confidentiality) chống xem trộm.
B. CHỈ cung cấp tính NGUYÊN VẸN (Data Integrity) và XÁC THỰC NGUỒN GỐC (Authentication), đồng thời CHỐNG PHÁT LẠI (Anti-replay). AH tuyệt đối KHÔNG MÃ HÓA NỘI DUNG (Dữ liệu vẫn lộ dưới dạng Text nếu bị tóm).
C. Phân bổ MAC tự động.
D. Làm DNS.
*Đáp án: B*
*Giải thích: Đừng nhầm lẫn giữa Bảo mật (Ai cũng đọc được nhưng không ai sửa được) với Kín đáo (Không ai đọc được). AH chỉ dán cái tem niêm phong. Muốn Kín đáo phải dùng giao thức ESP.*

**Câu 39:** Hàm Băm Mật Mã (Cryptographic Hash Function - VD: SHA-256) có 2 tính chất BẮT BUỘC nào biến nó thành linh hồn của Blockchain và Chữ Ký Số?
A. Tính một chiều (One-way: Không thể từ mã Hash dịch ngược lại File gốc) và Tính Chống va chạm (Collision Resistance: Gần như không thể tìm ra 2 File nội dung khác nhau mà lại sinh ra cùng một mã Hash giống hệt nhau).
B. Tự nén file và tự đổi MAC.
C. Có thể dễ dàng đảo ngược.
D. Tốc độ rất chậm.
*Đáp án: A*
*Giải thích: Hàm băm MD5/SHA giống như Máy Xay Thịt. Bỏ 1 con lợn (1GB Video) hay 1 con gà (10KB Text) vào xay, luôn nhả ra 1 dải thịt băm có độ dài CỐ ĐỊNH y hệt nhau (256 bits). Chỉ cần file gốc sai khác 1 bit, mã Hash thay đổi 100%.*

**Câu 40:** "Salting" (Thêm muối) trong việc lưu trữ Mật khẩu người dùng tại Cơ sở dữ liệu (Database) Web nhằm Chống lại điều gì?
A. Chống tấn công DDoS.
B. Bọn Hacker nếu chôm được toàn bộ Data, chúng sẽ dùng Bảng Cầu Vồng (Rainbow Tables - Tra cứu sẵn hàng tỷ mã Hash của các pass phổ biến `123456`) để tra ngược ra mật khẩu trong 1 giây. Việc Thêm Muối (Gắn một chuỗi ký tự ngẫu nhiên vào Mật khẩu trước khi Băm Hash) làm Bảng Cầu vồng vô dụng hoàn toàn.
C. Chặn IP nước ngoài.
D. Giảm dung lượng ổ cứng.
*Đáp án: B*
*Giải thích: Nếu DB bị rò rỉ, Hacker chỉ lấy được đống Hash (Băm). Nhưng với sức mạnh Card Đồ họa (GPU) ngày nay, việc bẻ mã hash yếu không tốn quá nhiều thời gian nếu không có Muối.*

**Câu 41:** Giao thức Bảo mật VPN (Virtual Private Network) tạo ra một "Đường hầm" (Tunnel). Bản chất "Đường hầm" đó là:
A. Việc kéo 1 sợi cáp vật lý.
B. Gói tin IP Nội bộ của Công ty ĐƯỢC MÃ HÓA CỨNG, sau đó bọc (Encapsulate) VÀO TRONG một Gói tin IP Ngoại biên (mang IP Công cộng). Gói IP Ngoại biên di chuyển trên Internet trần trụi, còn lõi bên trong hoàn toàn không thể đọc.
C. Xóa hết địa chỉ DNS.
D. Ngắt toàn bộ cáp đồng.
*Đáp án: B*
*Giải thích: Router ở Biên giới Công ty làm nhiệm vụ Đóng/Gói, biến rác thải mạng nội bộ thành những két sắt thép vứt lên xe tải Internet chở đi chi nhánh.*

**Câu 42:** "Botnet" thường được điều khiển theo phương thức C&C (Command and Control). Phương pháp ẩn mình kinh điển nhất của C&C hiện tại để tránh bị Cảnh sát bắt là gì?
A. Mở Port 80.
B. Hacker dùng "DGA" (Domain Generation Algorithm) - Thuật toán sinh tên miền tự động. Mạng lưới hàng triệu máy tính Botnet mỗi ngày tự động sinh ra hàng vạn tên miền rác ngẫu nhiên (Ví dụ `ajkhd123k.com`) rồi thử truy cập. Hacker chỉ việc lẳng lặng Đăng ký MỘT TRONG CÁC TÊN ĐÓ để Botnet tìm tới và nhận lệnh.
C. Gửi Fax.
D. Đóng card mạng.
*Đáp án: B*
*Giải thích: DGA là đòn đau đầu nhất đối với Lực lượng an ninh mạng, vì Tên miền chỉ sống đúng 24h và thay đổi thuật toán theo Ngày giờ. Cảnh sát không thể đánh sập kịp.*

**Câu 43:** Kỹ thuật "SQL Injection" tấn công Tầng Ứng dụng Bằng cách:
A. Tắt điện Database.
B. Cắm USB vào Server.
C. Người dùng (Hacker) nhập chuỗi Ký tự chứa các Câu lệnh Cơ sở dữ liệu ác ý (Ví dụ: `' OR 1=1 --`) vào ô "Đăng nhập" hay "Tìm kiếm". Nếu Lập trình viên Web bất cẩn KHÔNG kiểm tra làm sạch chuỗi nhập vào, Database Server sẽ ngây thơ THỰC THI CHÍNH LỆNH ĐÓ, làm nhả hết toàn bộ dữ liệu nội bộ ra ngoài hoặc Xóa sạch DB.
D. Bắt sóng Wi-Fi.
*Đáp án: C*
*Giải thích: Đây là lỗi kinh điển hạng nhất thế giới trong Bảo mật Web do sự bất cẩn của Thợ Code (Developer), chứ không phải lỗi của Kiến trúc Mạng.*

**Câu 44:** Firewall (Tường lửa) Stateless Packet Filtering (Bộ lọc Gói Phi trạng thái - Cổ điển) kiểm tra gì trên gói tin?
A. Không kiểm tra gì.
B. Mở tung gói tin đọc chữ.
C. Nó xét từng gói IP đơn lẻ độc lập đi qua nó. Chỉ nhìn vào 5 trường cơ bản: (IP Nguồn, IP Đích, Giao thức TCP/UDP, Port Nguồn, Port Đích) và so với một danh sách Rule có sẵn (ACL) để Drop hoặc Allow.
D. Đo đạc dung lượng.
*Đáp án: C*
*Giải thích: Stateless Firewall là anh lính gác ngốc nghếch. Nó thấy Gói tin báo TCP Port 80, IP Nguồn tốt, là nó cho vào. Nó không hề biết Gói tin đó thuộc phiên làm việc nào, có nguy hiểm ngầm hay không.*

**Câu 45:** Firewall "Stateful" (Tường lửa có Trạng thái) ưu việt hơn Stateless ở đặc điểm nào?
A. Rẻ tiền hơn.
B. Nó không cần dây cáp.
C. Nó cấp một vùng RAM chuyên dụng để DUY TRÌ BẢNG TRẠNG THÁI KẾT NỐI (Connection Tracking) của từng Phiên TCP/UDP đang diễn ra. Nó biết gói tin Đang Xin Vào cửa có HỢP LỆ (Là gói phản hồi cho một Lệnh Xin Ra trước đó của máy nội bộ) hay là Gói Khách Không Mời Tự Vào (Sẽ bị Block lập tức).
D. Chạy bằng AI tự tạo mã độc.
*Đáp án: C*
*Giải thích: Nếu PC 1 truy cập Facebook, Tường lửa Stateful ghi nhớ: "Phiên X vừa mở". Lát sau Facebook dội hàng tấn Data TCP về công ty, Tường lửa nhìn thấy "À, đây là data trả cho Phiên X, tôi cho vào".*

**Câu 46:** Giao thức EAP (Extensible Authentication Protocol) dùng ở đâu?
A. Làm giao thức mạng vệ tinh.
B. Đóng gói cho khung hình IP.
C. Nó là khung xác thực chủ yếu được nhúng bên trong chuẩn 802.1x (Mạng LAN doanh nghiệp) hoặc Wi-Fi (WPA-Enterprise) để trung chuyển thông tin xác thực từ Người dùng đến Máy chủ Bán kính (RADIUS Server).
D. Truyền tải điện thoại.
*Đáp án: C*
*Giải thích: Thiết bị Wi-Fi chỉ làm cầu trung chuyển gói EAP, Máy chủ RADIUS/Active Directory đằng sau bức rèm mới là người duyệt thẻ nhân viên thật sự.*

**Câu 47:** Tấn công BGP Hijacking (Cướp đường định tuyến BGP) gây hệ lụy:
A. Tăng băng thông.
B. Làm giảm bớt router.
C. Một Nhà cung cấp ISP cố ý hoặc vô ý Quảng bá sai lệch Bảng Định tuyến BGP lên Internet Toàn cầu (Báo rằng "TÔI SỞ HỮU DẢI MẠNG CỦA GOOGLE ĐÓ, ĐƯA GÓI TIN ĐÂY CHO TÔI"). Toàn bộ thế giới bị lừa (do BGP dựa trên lòng tin vỡ nát), và định tuyến mọi Traffic của Google vào tay Kẻ lừa đảo.
D. Biến đổi dữ liệu máy tính.
*Đáp án: C*
*Giải thích: BGP là "Giao thức theo cơ chế niềm tin bạn bè". Không có sự xác thực quyền sở hữu Dải IP trong BGP nguyên thủy. Hậu quả là có vụ Pakistan đã vô ý nhấn nút đánh sập luôn Youtube Toàn cầu trong nửa tiếng.*

**Câu 48:** Kỹ thuật "Cross-Site Request Forgery" (CSRF - Giả mạo Yêu cầu Chéo trang) hoạt động trên lỗ hổng niềm tin nào của Trình duyệt Web?
A. Không hỗ trợ mật khẩu.
B. Trình duyệt LUÔN TỰ ĐỘNG dính kèm Cookie Xác thực của một Trang Web (Ví dụ Ngân Hàng A) vào mọi HTTP Request (Cả POST/GET) được gửi tới Trang Web đó. Dù cái Lệnh gửi đó (Lệnh Chuyển tiền) lại xuất phát từ nút bấm Độc hại của một Trang Web Lừa Đảo (Trang B) mà nạn nhân vừa Vô Tình bấm vào ở Tab kế bên.
C. Tải phim quá chậm.
D. Router cấp nhầm IP.
*Đáp án: B*
*Giải thích: Ngân hàng A chỉ thấy có Lệnh chuyển tiền mang ĐÚNG Cookie của Nạn nhân nên ngây thơ duyệt luôn. Nó không biết Nạn nhân bấm lệnh này từ Web của Hacker. Biện pháp chống: CSRF Token ẩn trong Form.*

**Câu 49:** Dịch vụ DNSSEC (DNS Security Extensions) chèn thêm cái gì vào Truy vấn Tên miền để ngăn chặn "Đầu độc bộ đệm" (Cache Poisoning)?
A. Đăng nhập 2 lớp SMS.
B. Chữ ký Điện tử (Digital Signature). Khi Máy chủ DNS Local hỏi IP của `google.com`, Máy chủ Gốc sẽ không chỉ trả về Dòng IP `8.8.8.8`, mà còn Gửi kèm Chữ Ký Số Mã Hóa của nó. Máy Local sẽ Verify chữ ký đó bằng Public Key của Root DNS, đảm bảo 100% Gói Trả lời không bị Thằng Mạo Danh gửi.
C. Mã hóa IPsec.
D. Dùng TCP thay UDP.
*Đáp án: B*
*Giải thích: Một nỗ lực chậm chạp hàng thập kỷ của Nhân loại để vá lỗ hổng mù quáng của DNS. Hiện tại tỷ lệ triển khai DNSSEC toàn cầu vẫn chưa đạt 100%.*

**Câu 50:** Malware (Phần mềm độc hại) bao gồm nhiều thể loại. Trojan Horse khác với Virus ở điểm nào?
A. Trojan lây qua cáp điện.
B. Virus tự động lây nhiễm vào các tệp tin thực thi (exe) và phá hoại hệ thống. Trojan KHÔNG TỰ LÂY LAN, nó ẩn mình dưới dạng một phần mềm Hữu ích (Ví dụ Crack Game, Phần mềm kế toán). Người dùng TỰ MÌNH BẤM CHẠY Trojan, nó sẽ âm thầm mở "Cửa hậu" (Backdoor) trong hệ điều hành cho Hacker chui vào.
C. Bằng kích thước gói tin IP.
D. Mã hóa cao hơn.
*Đáp án: B*
*Giải thích: Rất nhiều vụ tấn công Doanh nghiệp xuất phát từ việc Nhân viên phòng Hành chính ham hố tải phần mềm Convert PDF miễn phí chứa Trojan trên mạng về bấm chạy.*

**Câu 51:** Sự khác nhau cơ bản giữa "Xác thực" (Authentication) và "Ủy quyền" (Authorization) trong bảo mật máy tính là gì?
A. Không có khác biệt.
B. Xác thực (Ai đang nói? - Who are you?) là chứng minh bạn đúng là nhân viên A thông qua Mật khẩu/Thẻ từ. Ủy quyền (Bạn được làm gì? - What can you do?) là kiểm tra xem nhân viên A có được phép mở Thư mục Mật của Công ty hay không sau khi đã qua cửa.
C. Xác thực dùng ở Router, Ủy quyền dùng ở Switch.
D. Xác thực là mua thẻ từ, Ủy quyền là in thẻ.
*Đáp án: B*
*Giải thích: Đăng nhập thành công (AuthN) không có nghĩa là bạn có quyền xóa máy chủ Database (AuthZ). 2 khái niệm cốt lõi của Access Control.*

**Câu 52:** Một gói mạng mã hóa SSL/TLS có thể bị chặn đứng và giải mã (Decrypt) theo thời gian thực để phân tích Virus (DPI) bởi Thiết bị Tường lửa Công ty nếu áp dụng cơ chế nào?
A. Cắt điện máy chủ.
B. Không thể nào, TLS là bất khả xâm phạm.
C. Sử dụng cơ chế SSL Inspection (Phân tích TLS). Tường lửa ở giữa đóng vai trò Man-in-the-Middle CHỦ ĐỘNG, nó dùng Chứng chỉ số Tự xưng (Đã ép cài ngầm vào máy tính Nhân viên trước) để giả mạo làm Server thực tế. Tường lửa bắt tin, giải mã ra đọc Text trong, xong tự Mã hóa lại một lớp TLS mới gửi ra Internet.
D. Dùng Router TP-Link.
*Đáp án: C*
*Giải thích: Do HTTPS hiện tại chiếm 95% Internet. Nếu Firewall cty không "giải mã giữa đường" (SSL Inspection), nó hoàn toàn "mù" và không thể biết bạn đang tải Code công ty lên Google Drive hay tải Virus về.*

**Câu 53:** Lỗ hổng "Buffer Overflow" (Tràn bộ đệm) ở Mức Hệ Điều Hành/Ứng dụng nguy hiểm vì:
A. Hacker có thể nhét Cáp mạng dài hơn vào máy tính.
B. Hacker gửi một Gói tin có dữ liệu (Payload) LỚN HƠN CỐ Ý SO VỚI MỨC KHAI BÁO. Nếu phần mềm máy chủ C không kiểm tra kỹ độ dài, Dữ liệu tràn ra khỏi giới hạn RAM cấp phát, đè bẹp lên Không gian thực thi Lệnh. Hacker nhét Dòng Lệnh Rác vào chỗ Tràn đó, ép CPU Server tự chạy Lệnh của Hacker.
C. Làm tràn đĩa cứng vật lý HDD.
D. Cháy màn hình điện thoại.
*Đáp án: B*
*Giải thích: Lỗ hổng Vĩ đại nhất lịch sử ngành phần mềm, khởi nguồn cho hàng trăm tỷ đô thiệt hại từ các siêu Virus lây lan (như Sasser, Blaster, WannaCry Server Message Block).*

**Câu 54:** Mạng ẩn danh Tor (The Onion Router) làm thế nào để Giấu nhẹm Địa chỉ IP gốc của Máy Gửi trước khi truy cập Web?
A. Đổi IP liên tục ngẫu nhiên mỗi 5 giây.
B. Không dùng IP.
C. Nó Đóng Bọc Đa Lớp (Kiểu củ hành). Gói dữ liệu Gốc của bạn bị Mã Hóa 3 lần. Gói tin đi qua 3 Nút Mạng Ngẫu Nhiên trên thế giới (Entry -> Middle -> Exit Node). Mỗi Nút chỉ được bóc 1 lớp vỏ và chỉ biết địa chỉ của Thằng Kế Trước và Thằng Kế Sau, TUYỆT ĐỐI không ai (Kể cả Web đích) biết được Đường đi trọn vẹn từ Bạn đến Web.
D. Xóa địa chỉ MAC.
*Đáp án: C*
*Giải thích: Thiết kế đỉnh cao của Tự do mạng, nhưng cũng là Mảnh đất màu mỡ cho Tội phạm buôn bán vũ khí, ma túy ở Web Chìm (Dark Web).*

**Câu 55:** Một trong những kỹ thuật đơn giản nhất để Phòng thủ trước Tấn công "Port Scanning" trên Mạng Cá Nhân là gì?
A. Tắt máy tính luôn.
B. Tắt ICMP Echo Request trên Tường lửa (Chặn Ping) và Không chạy các Dịch vụ Nền (Daemons) không sử dụng tới (Ví dụ Tắt Cổng RDP 3389, FTP 21). Mạng càng khép kín càng ít "Bề mặt Tấn công" (Attack Surface).
C. Không bao giờ cắm mạng dây.
D. Dùng mạng 3G 4G.
*Đáp án: B*
*Giải thích: Nếu Nhà không có Cửa Sổ (Port đóng), Trộm có đi vòng quanh cũng không chui vào được. Đừng mở Port 80 nếu bạn không rành về bảo mật web.*

**Câu 56:** Giao thức nào cung cấp cấu trúc mã hóa cho việc Truy cập Wi-Fi "Guest" (Khách) an toàn nhất, khi nhiều người lạ cùng dùng chung 1 Mật Khẩu PSK (Pre-shared key) ở Quán Cafe?
A. Chặn hết mạng khách.
B. Dùng Wi-Fi mở hoàn toàn không MK.
C. Trong thực tế WPA2-Personal, KHI CÙNG CÓ CHUNG 1 MK PSK, người lạ ở bàn bên dùng Sniffer CÓ THỂ bắt và GIẢI MÃ được Phiên lướt web (không SSL) của bạn nếu họ rình bắt được quá trình Handshake 4 bước. Tính riêng tư nội bộ là bằng 0.
D. IP tự động mã hóa máy trạm.
*Đáp án: C*
*Giải thích: Đó là sự thật phũ phàng của WPA2 Quán Cafe. Chỉ có chuẩn mới WPA3 (Dùng Thuật toán Trao đổi khóa Dragonfly SAE) mới ĐẢM BẢO dù 10 người có CHUNG 1 Pass Wi-Fi Quán, họ cũng KHÔNG THỂ giải mã được Phiên làm việc của người khác.*

**Câu 57:** Các thiết bị phần cứng Mã hóa chuyên dụng (Hardware Security Module - HSM) thường được các Ngân hàng dùng để:
A. Tự sửa ổ cứng hỏng.
B. Sinh sóng Wi-Fi mạnh hơn.
C. Tạo ra và Lưu trữ Cực Kỳ An Toàn Các Chìa Khóa Bí Mật Ký Số (Private Keys / Của Ngân hàng). Ngăn chặn tuyệt đối việc Hacker (dù chiếm được quyền Root Server) copy File Chìa khóa đem về nhà dùng dần. Việc giải mã CHỈ XẢY RA TRONG CHÍNH CON CHIP VẬT LÝ HSM không thể trích xuất ngược.
D. Truyền tải gói tin UDP.
*Đáp án: C*
*Giải thích: Không bao giờ để Chìa khóa gốc khỏa thân (Clear-text file) ở trong Ổ cứng của Server mềm (OS). Phải nhét vào cái hộp Đen sắt (HSM), búa đập là nó tự tiêu hủy Keys.*

**Câu 58:** Cấu trúc bảo vệ nhiều lớp trong Kiến trúc mạng Doanh nghiệp thường dùng khái niệm "DMZ" (Demilitarized Zone). Vùng Phi Quân Sự này nằm ở đâu?
A. Ở ngoài cổng rác.
B. Ở Tầng Vật Lý.
C. Vùng mạng vật lý Nằm GIỮA Internet và Mạng Nội bộ An toàn (LAN). Chứa các Máy Chủ Bắt Buộc Phải Đón Khách Ngoài (Web, Mail, DNS Server). Nếu Hacker chiếm được Máy Web ở DMZ, Hacker vẫn KHÔNG THỂ đâm xuyên vào Server Data/Kế toán đang nằm sâu trong LAN do bị 1 lớp Tường lửa nữa chặn lại.
D. Ổ đĩa mềm.
*Đáp án: C*
*Giải thích: Bạn không thể để cái Két Sắt tiền (Database) chung phòng với cái Phòng Khách tiếp dân (Web Server). DMZ là Cánh Cửa An Toàn Cách Ly 2 phòng đó ra.*

**Câu 59:** Tấn công "Dictionary Attack" (Từ điển) dùng vào mục đích gì?
A. Cắt cáp quang.
B. Bẻ khóa mã băm Mật khẩu bằng cách tự động Bơm hàng triệu Từ Có Ý Nghĩa (như password, 123456, admin, iloveyou, qwerty) lấy từ Kho Từ Điển vào Hàm Hash để so sánh với Hash bị trộm xem có khớp không. Nhanh hơn phương pháp Vét cạn mù quáng (Brute-force ký tự ngẫu nhiên).
C. Tắt cổng ICMP.
D. Phân bổ IP.
*Đáp án: B*
*Giải thích: 90% con người trên trái đất đặt Mật khẩu bằng Tên, Ngày sinh hoặc Các từ có nghĩa dễ nhớ. Từ điển sinh ra là để tóm cổ nhóm Lười biếng này trong 5 giây.*

**Câu 60:** Khái niệm "Honeypot" (Trạm trinh sát / Hũ mật) CÓ THỂ BỊ HACKER CẢNH GIÁC PHÁT HIỆN RA NẾU:
A. Bọn chúng mất điện máy tính.
B. Quản trị viên cấu hình Honeypot "Hoàn hảo" quá mức. Một Server tự dưng mở hàng chục Lỗ hổng nguy hiểm (Port rách nát), nhưng trong ổ cứng lại Toàn File Rác không có gì giá trị, Hacker lão luyện sẽ Nghi Ngờ và "Bỏ qua" không sập bẫy.
C. Rút dây mạng.
D. Quét ARP rác.
*Đáp án: B*
*Giải thích: Xây Honeypot là Nghệ thuật. Phải giả mạo giống y hệt thật, cho nó hoạt động lén lút, thậm chí cấy vài Database ảo chứa Email khách hàng ảo vào mới nhử được cá mập sa lưới.*

**Câu 61:** Mật mã hóa dòng (Stream Cipher) thường ứng dụng ở đâu tốt nhất so với Mã hóa khối (Block Cipher)?
A. Lưu trữ File nén ZIP trên ổ cứng.
B. Truyền tín hiệu Không Dây thời gian thực (Như Wi-Fi RC4 WEP/WPA). Bởi vì Mã hóa Dòng trộn (XOR) Mật mã VÀO TỪNG BIT một một cách liên tục khi dòng Dữ liệu tuôn chảy, không tốn thời gian chờ đệm (Buffering) một Khối to rồi mới nhồi mã như Block Cipher (AES).
C. Không áp dụng vào thực tế.
D. Sửa lỗi Checksum TCP.
*Đáp án: B*
*Giải thích: Stream Cipher cực nhanh và mượt mà, nhưng cực kỳ rủi ro nếu tái sử dụng lại Dòng Khóa (Key Stream) lần thứ hai (Lỗ hổng chết người của WEP).*

**Câu 62:** "IPsec" có hai giao thức mã hóa chính là Transport và Tunnel Mode. VPN Doanh nghiệp (Site-to-Site giữa 2 văn phòng) SẼ DÙNG CHẾ ĐỘ NÀO?
A. Tunnel Mode (Đường hầm). Máy trạm ở HN gửi 1 gói IP thường. Tường lửa HN sẽ GÓI TRỌN VẸN gói IP Thường này vào Két sắt, dán nhãn IP của Tường Lửa HN làm IP Nguồn Mới, IP Tường Lửa SG làm Đích. Kẻ gian trên mạng Internet CHỈ THẤY 2 bức tường lửa đang nói chuyện với nhau, Hoàn toàn Mù tịt không biết PC nào ở HN đang tải Data.
B. Transport Mode.
C. IPv6 Mode.
D. UDP Mode.
*Đáp án: A*
*Giải thích: Đỉnh cao giấu mặt ở Lớp 3. Bọn nghe lén ngoài Internet bị "Mù" hoàn toàn Lớp 3 nội bộ, vì Lớp 3 nội bộ đã biến thành Lớp Tải Trọng (Payload) rác nằm kín bưng trong IPsec Tunnel.*

**Câu 63:** Chức năng "Perfect Forward Secrecy" (PFS - Bảo mật Chuyển tiếp Hoàn hảo) trong cấu hình HTTPS bảo vệ cái gì ở Tương lai?
A. Làm ổ đĩa quay nhanh hơn.
B. Tránh bị phá máy tính.
C. Đảm bảo Rằng: Nếu 5 năm sau Hacker trộm được Private Key của Máy Chủ Web, Hacker đem cái Key đó Áp dụng vào cái ĐỐNG GÓI TIN HTTPS NÓ ĐÃ LƯU TRỮ NGHE LÉN TỪ 5 NĂM TRƯỚC -> HACKER VẪN KHÔNG THỂ GIẢI MÃ ĐƯỢC MỚ DATA CŨ ĐÓ. (Do mỗi Phiên giao dịch nó sinh ra một Session Key ngẫu nhiên dùng 1 lần rồi Hủy vĩnh viễn theo chuẩn Diffie-Hellman Ephemeral).
D. Không dùng Mật khẩu máy.
*Đáp án: C*
*Giải thích: PFS vá lỗ hổng cố hữu của RSA thuần: Nếu lộ Chìa khóa Chủ, thì Mọi đoạn hội thoại Quá khứ, Hiện tại, Tương lai đều lòi đuôi chuột.*

**Câu 64:** Mạng nội bộ muốn chống rò rỉ dữ liệu nhạy cảm (Data Loss Prevention - DLP), hệ thống DLP sẽ phải Quét (Scan) yếu tố nào cực sâu?
A. Scan IP đích có chứa chữ lạ.
B. Scan địa chỉ MAC.
C. DLP áp dụng DPI (Phân tích gói tin sâu Tầng 7) kết hợp Regex Nội dung. Ví dụ: Nó chặn đứng Mọi Email, Mọi Lệnh tải HTTP POST có chứa Chuỗi Ký tự mang ĐỊNH DẠNG SỐ THẺ TÍN DỤNG (xxxx-xxxx-xxxx-xxxx) hoặc Chữ "Tuyệt mật", không cho các luồng Dữ liệu này Xuyên qua Tường Lửa đi ra ngoài Internet.
D. Cấm TCP.
*Đáp án: C*
*Giải thích: Nhân viên cắm USB sao chép dữ liệu Công ty ra ngoài là tội hình sự. DLP là hệ thống An ninh chuyên săn bắt Kẻ thù từ BÊN TRONG CÔNG TY cố tình tuồn hàng ra ngoài.*

**Câu 65:** Chữ ký điện tử (Digital Signature) CÓ MỘT ĐIỂM KHÁC BIỆT CHÍ MẠNG nào so với Chữ ký Viết Tay bằng mực ngoài đời?
A. Ký xong mực phai đi.
B. Chữ ký tay luôn luôn y hệt nhau trên mọi tờ Hợp đồng. Còn Chữ ký Số bị PHỤ THUỘC VÀO NỘI DUNG (Toán học Băm - Hash) CỦA CHÍNH CÁI TÀI LIỆU ĐÓ. Tức là Chữ Ký Số gắn vào Hợp Đồng A sẽ khác Hoàn toàn Chữ Ký Số gắn vào Hợp Đồng B của Cùng 1 Người Ký.
C. Chữ ký số dễ bị xóa bằng Photoshop.
D. Không khác gì.
*Đáp án: B*
*Giải thích: Nếu Chữ ký số y hệt nhau, Kẻ lừa đảo chỉ việc Copy khối Chữ Ký ở Hợp đồng A, Paste chèn đè lên Hợp đồng Vay Tiền B là Xong đời nạn nhân.*

**Câu 66:** Tại sao Các Website nhỏ hay Cố tình lách qua Lỗi Chứng chỉ (Certificate Invalid / Hết hạn) của Trình duyệt bằng cách Cấu hình Chấp nhận Cảnh báo Đỏ (Proceed anyway)? Rủi ro là gì?
A. Rủi ro máy tính nổ tung.
B. Rủi ro Mất mạng Wi-Fi.
C. Nó làm VÔ HIỆU HÓA Toàn bộ Quyền năng Xác thực (Authentication) của Tổ chức CA. Người dùng đang nhắm mắt giao Mật khẩu/Thẻ tín dụng cho một Máy Chủ X ẩn danh (Có thể là Hacker đang Man-in-the-Middle ngụy tạo 1 Chứng chỉ Fake), mất tiền ráng chịu.
D. Router chậm 1 phút.
*Đáp án: C*
*Giải thích: Mọi công sức Mã hóa Toán học 256-bit phức tạp Trở nên Bằng Số 0, chỉ vì Trình duyệt con người ngớ ngẩn Bấm Nút "I understand the risk and Continue".*

**Câu 67:** Khái niệm "Vá Lỗi Mềm" (Virtual Patching) trên thiết bị Tường Lửa Ứng Dụng Web (WAF) là gì?
A. Tải phim nhanh.
B. Khi Phát hiện 1 Lỗ hổng Tràn bộ đệm MỚI TINH trên Nginx, Admin chưa kịp Update Nginx Code (Tốn 1 ngày). Admin chỉ việc Lên WAF viết 1 cái Dòng Luật chặn đứng mọi Yêu cầu HTTP chứa Ký tự lạ đó ngay ngoài cửa rào. Mặc dù Server Web BÊN TRONG VẪN LỖI, nhưng Mạng BÊN NGOÀI không cho ai chọc vào được Lỗi đó.
C. Bỏ qua Tầng Mạng IP.
D. Cấm TCP hoàn toàn.
*Đáp án: B*
*Giải thích: WAF là liều thuốc giảm đau tức thời cứu Mạng Doanh Nghiệp trong 5 Phút đầu tiên trước khi Team Developer khắc phục Code thảm họa.*

**Câu 68:** Khi Kẻ tấn công dò Mật khẩu bằng cách vét cạn (Brute-Force), làm sao Hệ thống mạng Cản trở hiệu quả nhất trước khi hắn thử thành công hàng triệu Pass?
A. Mã hóa đường truyền AES.
B. Tắt Wi-Fi.
C. Dùng chức năng "Rate Limiting" (Tạm khóa IP sau 5 lần Đăng nhập sai) kết hợp CAPTCHA. Giúp giảm thiểu Tốc độ dò mật mã từ 1 Triệu lần/Giây xuống còn 0.1 Lần/Giây. Buộc Hacker nản lòng bỏ cuộc.
D. Dùng TCP Tahoe.
*Đáp án: C*
*Giải thích: Không cần Toán học cao siêu. Bức rào trễ thời gian (Delay) của Lớp 7 là vũ khí đơn giản mà tàn nhẫn nhất bẻ gãy mọi loại máy móc dò mã.*

**Câu 69:** Một hệ thống mạng (LAN) Ảo hóa hoàn toàn Tách Biệt Mạng Khách và Mạng Nhân viên bằng Công nghệ gì tốt nhất?
A. Đổi mật khẩu router chung.
B. Chạy 2 DNS.
C. Sử dụng công nghệ VLAN. Mạng Khách (VLAN 10) bị ép Route thẳng từ Switch đi ra một cái Cổng Đường truyền Internet (Vứt rác ra ngoài luôn). Tuyệt đối cấm Định tuyến (Routing) qua lại giữa VLAN 10 và VLAN 20 (Nhân Viên) ở Tầng 3.
D. Rút cáp nguồn ra cắm lại.
*Đáp án: C*
*Giải thích: Cô lập Tầng 2 bằng VLAN, Chặn Tầng 3 bằng Lệnh Cấm Access Control List (ACL).*

**Câu 70:** Kỹ thuật "Network Address Translation" (NAT) Dù mang tiếng xấu Phá Chuẩn Internet, nhưng nó TÌNH CỜ TẠO RA một "Tấm Khiên Tường Lửa Bẩm Sinh" gì cho Mạng Gia đình?
A. Chặn virus ổ cứng.
B. Máy khách phía sau NAT Không Có Địa Chỉ IP Public. Hacker ngoài Internet Đứng Khóc vì Không Thể nào Nhắm Đích (Gửi SYN) TRỰC TIẾP đến IP 192.168.1.5 máy bạn để Hack lỗ hổng Windows được, trừ khi Bạn là người MỞ CỬA (Chủ động Nhấp Link Click gửi Request Ra Ngoài).
C. NAT giúp tải phim 8K nén.
D. Giúp điện thoại di động đổi màu.
*Đáp án: B*
*Giải thích: NAT Tự Dưng trở thành Bộ lọc Stateless siêu mạnh. Cứ từ ngoài chui vào mà không xin phép trước thì NAT vứt gói tin xuống cống. Giúp Hàng Tỉ máy tính dân dụng Lách qua cửa tử (Dù Win lậu, không Tường lửa cá nhân).*

**Câu 71:** Mạng Botnet (Mạng lưới máy tính ma) sinh ra để phục vụ Mục đích gì tàn phá Mạng Tầng 7 nhất?
A. Làm nóng máy tính cá nhân.
B. Huy động sức mạnh băng thông của 10.000 máy tính bị nhiễm vi rút (Zombies), ĐỒNG LOẠT Dội Hàng Triệu Lệnh HTTP GET / HTTP POST Vô Tri (DDoS Tầng Ứng dụng) vào Cổng 80 của một Trang Web Nạn nhân. Làm Hệ Điều Hành của Trang Web Cạn kiệt RAM, CPU và Băng Thông trong tích tắc.
C. Bắt wifi láng giềng.
D. Sửa cáp đồng thành quang.
*Đáp án: B*
*Giải thích: Đỉnh cao của sức mạnh Bầy kiến giết Voi. Bạn không cần 1 siêu máy tính của Hacker. Hacker chỉ cần ra lệnh cho 1 triệu con Kiến (Laptop, Tủ lạnh thông minh bị hack) nã rác vào bạn.*

**Câu 72:** Ứng dụng công cụ Nmap (Network Mapper) vào An ninh mạng có chức năng Trinh sát (Reconnaissance) quan trọng nào?
A. Giải nén video.
B. Nó là một Cỗ máy Quét Cổng (Port Scanner) vĩ đại. Nó Gửi Gói TCP SYN / UDP cào qua 65.535 Cổng của 1 Địa chỉ IP Đích để lập "Bản đồ Hiện Trạng": Xem Cổng 80 có Đang Mở (Web đang chạy không?), Cổng 22 có Đang Mở không. Từ đó, Kẻ tấn công Vạch Ra Lộ Trình Đâm kim Vào Lỗ Hổng Ứng Dụng tương ứng.
C. Mã hóa IP động.
D. Biến Router thành Switch.
*Đáp án: B*
*Giải thích: Biết địch biết ta. Không ai đâm đầu Hack mò. Phải quét Port trước để tìm Bề mặt Tấn công (Attack Surface).*

**Câu 73:** Lỗ hổng "Heartbleed" (Máu nhỏ giọt trái tim) kinh hoàng một thời trên OpenSSL lợi dụng tính năng Tầng Giao Vận nào?
A. TCP Window Size.
B. Lợi dụng Lỗ Hổng của Tiện Ích "Keep-Alive" (Heartbeat) Của TLS. Trình Khách Gửi: "Ê Server, tôi gửi cho anh chữ 'A' có độ dài 1000 Ký Tự nhé, Anh gửi trả tôi nhé". Server ngây thơ Lấy chữ 'A' Của Khách, Bốc thêm 999 Ký Tự RÁC Trong RAM CỦA SERVER (vô tình dính Mật khẩu, Thẻ tín dụng người khác) Gửi Trả Về cho Khách, Lộ Trắng Thông Tin Nhạy Cảm.
C. Tràn bộ đệm vật lý.
D. Phân bổ BGP.
*Đáp án: B*
*Giải thích: Do Lập trình viên C code sai hàm Check Độ Dài. Trình Khách nói điêu "Tôi gửi độ dài 1000", Server nhắm mắt bốc 1000 Ký tự trong RAM trả lại mà không thèm đếm số chữ Khách vừa đưa. Hàng tỷ Password bị trộm không tốn một giọt mồ hôi.*

**Câu 74:** Cơ chế "Intrusion Detection System" (IDS - Hệ thống phát hiện xâm nhập) khác với IPS (Prevention - Ngăn chặn) ở Thái Độ nào?
A. IDS nén data, IPS bung data.
B. IDS chỉ Giống Còi Báo Cháy. Nó Ngồi Trong Góc Nghe Lén (Sniff/Mirror Port), Phát Hiện Hacker Đang Hack -> Gửi Email Báo Động đỏ Cho Admin, Nhưng Bó Tay Đứng Nhìn. Còn IPS là Lính Gác Cầm Súng, Ngồi TRỰC TIẾP TRÊN ĐƯỜNG ĐI Của Dữ Liệu (In-line), Phát Hiện Hack -> DROP Cắt Luồng IP Ngay Lập Tức, Mạng Tạm Cứu Bàn Thua.
C. Cả 2 cùng bắt IP.
D. IDS đổi MAC, IPS đổi IPv6.
*Đáp án: B*
*Giải thích: IDS là Giám sát (Monitor), IPS là Hành động (Action). Mạng chậm đi 1 chút vì phải đi Xuyên qua IPS, nhưng bù lại được Bảo Vệ Trực Tiếp.*

**Câu 75:** Trong Giao thức IPsec, "Khóa Chia Sẻ Trước" (Pre-Shared Key - PSK) thường được cấu hình thế nào giữa Trụ sở Chính và Chi nhánh?
A. Nhập Mật Khẩu qua Web.
B. IT Admin của Công ty Lái Xe Đạp qua Cả 2 Nơi, ĐĂNG NHẬP VÀO 2 CỤC TƯỜNG LỬA, Gõ Thủ Công 1 Đoạn Chữ Cực Dài (Ví dụ: `CoNgTy@!123_BiMat`) Vào Bụng 2 Cục Sắt. Sau Đó 2 Cục Tường Lửa Tự Động Kết Nối IPsec, Tự Biết Băm Cái Chữ Đó Ra Làm Chìa Khóa Mật Mã Đều Nhau Mà Không Phải Gửi Lên Mạng Tranh Cướp Bị Nghe Lén Nữa.
C. Quét khuôn mặt.
D. Dùng IP tự khóa.
*Đáp án: B*
*Giải thích: Cách nông dân nhất nhưng lại là Cách Chống Đánh Cắp Chìa Khóa Qua Mạng An Toàn Nhất Thế Giới (Out-of-band Key Distribution).*

**Câu 76:** Bạn đang làm Quản trị viên Mạng (Network Admin) cho một hệ thống Web lớn, làm sao chặn đòn tấn công Phishing Mạo danh Tên miền Email Của Công ty Bạn Gửi Cho Khách Hàng?
A. Rút mạng LAN.
B. Cấu Hình Bản Ghi Mạng "DMARC" (Domain-based Message Authentication, Reporting, and Conformance). Nó Báo Cho Gmail Biết: "Nếu Gmail Thấy Một Cái Email Nào Mang Tên Công Ty Tôi, Nhưng CHECK IP NGUỒN Thấy THẤT BẠI (Sai SPF) Hoặc SAI CHỮ KÝ ĐIỆN TỬ (Sai DKIM) -> HÃY QUĂNG THƯ ĐÓ VÀO THÙNG RÁC SPAM CHO TÔI".
C. Lập Web bảo vệ TCP.
D. Cấm Port 80.
*Đáp án: B*
*Giải thích: DMARC, SPF, DKIM là "Chén Thánh" Bảo Vệ Danh Dự Tên Miền Email Tầng 7 của Thời Đại Số.*

**Câu 77:** Sự ra đời của Mạng Ảo Riêng VPN SSL (Như OpenVPN, WireGuard) chạy trên Nền Tảng Tầng Transport UDP ƯU VIỆT HƠN IPsec VPN truyền thống Lớp 3 ở điểm nào?
A. Nó biến Mạng thành Mạng vệ tinh.
B. Nó Vượt Tường Lửa Cực Tốt. IPsec Chạy Các Giao Thức Lạ (ESP/AH Lớp 3) Không Có Port -> Thường Xuyên Bị Các Cục NAT/Firewall Gia Đình Chặn Lại Bực Mình. SSL VPN Bọc Data Trong Cục TCP 443 (Như lướt Web HTTPS) Hay UDP 1194 Khỏe Re, Cứ Xuyên Mọi Loại NAT Mà Chạy Ngon Lành.
C. Bỏ qua DHCP và MAC.
D. Cắm thẳng vô CPU Máy Chủ.
*Đáp án: B*
*Giải thích: 90% nhân viên Work From Home Mùa Dịch xài SSL VPN (Tầng 4/7) thay vì IPsec, vì Nó "Thân thiện với NAT Nhà Trọ" vô cùng.*

**Câu 78:** Kỹ thuật Mật Mã Hóa Cơ Sở "Khóa Đối Xứng" Phổ Biến Nhất Hiện Nay Trọng Dụng Cho Việc Mã Hóa Dòng Chảy Dung Lượng Cao Là Gì?
A. DES cổ điển.
B. Chuẩn Mã Hóa Nâng Cao AES (Advanced Encryption Standard). Được Chính Phủ Mỹ Bảo Chứng, Tính Toán Qua Các Vòng Bảng Tra Cứu Phức Tạp Lập Thức Rối Mù Nội Dung Gốc.
C. BGP Routing.
D. Đổi Địa Chỉ IP Rác.
*Đáp án: B*
*Giải thích: AES-128 và AES-256 là linh hồn bảo vệ Dữ liệu Của Ngân Hàng, Giao Dịch, Két Sắt trên mọi hệ điều hành.*

**Câu 79:** Trong cuộc tấn công "Ransomware" (Mã độc Tống tiền) Mạng Nội Bộ, Giao Thức Tầng Ứng Dụng Nào Hay Bị Chọc Thủng Lỗ Hổng Lan Truyền Tốc Độ Kinh Hoàng Nhất Giữa Các Máy Windows?
A. Giao thức UDP.
B. Giao Thức BGP.
C. Giao Thức SMB (Server Message Block) / Tầng Chia Sẻ File. Lỗ Hổng EternalBlue Vĩ Đại Cho Phép Hacker Chui Quanh Hệ Thống Mạng Không Cần Pass, Lây Lan WannaCry Làm Tê Liệt Hàng Nghìn Bệnh Viện Tốn Tỷ Đô Bóp Nghẹt Tức Thì.
D. ARP MAC Lớp 2.
*Đáp án: C*
*Giải thích: Tắt Port 445 (SMB) Nếu Bạn Không Dùng Dịch Vụ Mạng Share Folder Nội Bộ, Sẽ Cứu Mạng Máy Tính Của Bạn Khỏi Tử Thần Lây Nhiễm Bầy Đàn.*

**Câu 80:** "Zero Trust Network" (Mạng Không Tin Cậy Bất Kỳ Ai) Khái Niệm Đình Đám Nhất Hiện Nay Khác Biệt Mạng Cũ Ở Logic Gì?
A. Nó Tin Mạng LAN.
B. Cổ Điển: Bạn Cắm Dây Trong Công Ty -> Bạn Là Người Nhà -> Tường Lửa Thả Cửa Hoàn Toàn Nội Bộ. Zero Trust: Bạn Ngồi Kế Bên Sếp Hay Ở Quán Cafe MỸ, BẠN VẪN LÀ KẺ ĐÁNG NGỜ. Hệ Thống Liên Tục Xác Thực Từng Cú Click, Từng IP, Từng App Trước Mỗi Hành Động Truy Cập Tài Nguyên Mạng Bất Kỳ Của Bạn.
C. Tắt Hệ Thống Web Tầng 80.
D. Giảm Tốc Độ Trình Duyệt.
*Đáp án: B*
*Giải thích: Biện Pháp Chữa Trị Bệnh "Chui Cổng Sau" Của Hacker Đâm Thủng Tường Lửa Rồi Nằm Vùng Trong Công Ty Tháng Trời Đọc Trộm Nội Bộ Mạng.*

**Câu 81:** "Biometric Authentication" (Xác thực Sinh trắc học) Trong Cấu Trúc An Ninh Ứng Dụng Thuộc Nhóm Xác Thực Nào Sau Đây?
A. Điều bạn BIẾT (Something you know - VD: Password).
B. Điều bạn CÓ (Something you have - VD: Thẻ từ, Chìa khóa, Điện thoại có OTP).
C. Điều bạn LÀ (Something you are - VD: Dấu vân tay, Mống mắt, Khuôn mặt).
D. Xác Thực Mạng BGP.
*Đáp án: C*
*Giải thích: Đăng nhập bằng FaceID iPhone vào Bank là yếu tố C (Vật lý cơ thể), kết hợp với Mật Khẩu (A) Tự Động Trở Thành Xác Thực 2 Yếu Tố Cực Kì Đáng Tin.*

**Câu 82:** Tấn công "Dictionary Attack" Sẽ DỄ DÀNG THẤT BẠI NHẤT Khi Quản Trị Hệ Thống Áp Dụng Quy Định Nào?
A. Cắm Cáp Quang Chống Đứt.
B. Cấu Hình Tường Lửa Chặn Cổng TCP 80.
C. Bắt Buộc Chính Sách Mật Khẩu Siêu Cứng (Password Complexity Policy): Phải Dài Ít Nhất 12 Ký Tự, Bao Gồm Chữ Hoa, Thường, Số, Ký Tự Đặc Biệt `@#$`. Tự Động Cản Trở Mọi Từ Điển Truyền Thống Xuyên Thủng.
D. Biến Server Thành P2P Mạng Lưới.
*Đáp án: C*
*Giải thích: Mật khẩu `AnhYeuEm123` bay màu trong 0.1 Giây Vét Cạn. Mật khẩu `A@1nH&Y!eU*3` Kéo Dài Thời Gian Giải Mã Của Siêu Máy Tính Lên Hàng Trăm Năm.*

**Câu 83:** Trong Một Buổi Phân Tích Sự Cố Tấn Công, Admin Tìm Thấy File `log` Tường Lửa Có Hàng Ngàn Dòng Cảnh Báo "UDP Flood Dội Vào Cổng 53". Anh Ta Suy Ra Hệ Thống Đang Gặp Lỗi Gì Ở Tầng Mạng Và Ứng Dụng?
A. Cáp L2 Sắp Nổ Tung.
B. Có Tội Phạm Đang Cố Gắng Gửi Thư Rác (Spam Email) Qua Tầng 7 Nhằm Phá Hoại.
C. Hacker Đang Dùng Botnet Nã Gói Tin Rác Tốc Độ Khủng Vào Dịch Vụ Máy Chủ Phân Giải Tên Miền (DNS) Nhằm Làm Ngập Cạn Mạng.
D. Cáp Đồng Tụt Áp Do Điện Dưới Chuẩn.
*Đáp án: C*
*Giải thích: Port 53 là Đích Nhắm Của DNS. Dựa Vào Tọa Độ Port Rác Mà Tường Lửa Chỉ Báo, Thợ Săn Lỗi Đọc Được Tư Duy Tấn Công Lớp Application Của Đối Thủ.*

**Câu 84:** Nếu Mạng Nội Bộ (LAN) Đang Dính Một Con Virus "Worm" (Sâu Tự Nhân Bản), Hiện Tượng Lớp Mạng Gì Tồi Tệ Nhất Hay Bị Quản Trị Viên Nhìn Thấy Bằng Công Cụ Bắt Gói Tin Mạng?
A. Sóng Wi-Fi Đột Ngột Tắt Nghẽn Sóng Lớp 1.
B. Sự Tăng Vọt Khủng Khiếp Của Cơn Bão Bắn Gói Tin Quét Port (Scan Network L3/L4) Bừa Bãi Ra Xung Quanh LAN Liên Tục, Làm Cạn Đáy CPU Switch Tầng L2 Và Router Tầng L3. Sâu Mạng Cố Tìm Kiếm Bạn Bè Lỗ Hổng Để Lan Sang.
C. Tên Miền Google Bị Dịch Sai Lệnh.
D. DNSSEC Bị Hỏng Mã Khóa Mật Khẩu.
*Đáp án: B*
*Giải thích: Worm khác Virus Thường Là Nó Chủ Động Liên Tục Đánh Sập Lưới Mạng Bằng Hành Vi Giao Tiếp Dữ Liệu Phát Ra Bốn Phương Tám Hướng Suốt Ngày Đêm Hút Sạch Băng Thông Khí Quyển.*

**Câu 85:** Phương Án Mã Hóa Điểm-Điểm (End-To-End Encryption - E2EE) Trên Các App Như Zalo / WhatsApp Nghĩa Là Gì?
A. Gửi Trắng Cho ISP Giải Mã Lại.
B. Gói Tin Được Máy A MÃ HÓA LUÔN TẠI MÁY, Chạy Qua Tầng L2, L3, Chạy Qua Hệ Thống MÁY CHỦ BƯU ĐIỆN CỦA ZALO, Máy Chủ Zalo CŨNG KHÔNG ĐỌC ĐƯỢC CHỮ NÀO (Mù Tịt), Chạy Tới Đích Vô Máy B, B Mới Giữ Khóa ĐÓ Mở Đọc. Máy Chủ OTT Không Thể Lén Nghe Điện Thoại.
C. Giữ Nguyên Chữ Thường Mã Hóa Ở Tầng 2.
D. Zalo Cấp Nhầm Mật Khẩu Lên Mạng.
*Đáp án: B*
*Giải thích: Không Ai Trên Trái Đất Đọc Được Ngoại Trừ Người Gửi Và Người Nhận - Biện Pháp Giao Tiếp Không Thể Bị Nghe Lén Cả Ở Tầng Trung Gian Của Giới Chủ App.*

**Câu 86:** Mật Mã Đa Lớp (Defense in Depth) Của Các Tập Đoàn An Ninh Áp Dụng Bố Cục Bảo Vệ Theo Nguyên Tắc Nào?
A. Để Chìa Khóa Ở Bàn Lễ Tân Công Ty.
B. Chỉ Dùng Mật Khẩu 128 Bit Mạnh Nhất Tại Website, Bỏ Qua Cáp L3.
C. Không Tập Trung Vào MỘT LỚP PHÒNG THỦ DUY NHẤT. Thiết Lập Firewall Ở L3 Mạng Biên, Dùng Port Security Ở L2 Switch, Dùng Mật Khẩu Dài Máy Chủ, Mã Hóa Ổ Cứng Khách, Dùng WAF Bảo Vệ L7 Dữ Liệu Tầng Ứng Dụng. Tầng Này Sập, Lớp Sau Vẫn Cản Bỏ Được Đòn Hacker Đột Kích Xuyên Thấu.
D. IPsec Tunnel Ở Tầng 5 Xuyên Không.
*Đáp án: C*
*Giải thích: Đừng Bao Giờ Giao Trứng Cho Cùng Một Giỏ. Đào Hào, Xây Thành, Lưới Thép, Mọi Tầng Mạng TCP/IP Đều Phải Phủ Đầy Răng Cưa Lớp Lưới.*

**Câu 87:** Giao Thức Bảo Mật "Kerberos" Có Lợi Ích Cực Lớn Của Hệ Thống Nội Bộ Ở Vấn Đề Gì?
A. Đóng Ngắt TCP Tức Thì 2s.
B. Chống Được IP Spoofing 100%.
C. Mô Hình Dịch Vụ Cấp Vé Trung Tâm (Ticket-Granting). Một User Trong Doanh Nghiệp Chỉ Đăng Nhập ĐÚNG 1 LẦN BAN SÁNG (SSO - Single Sign-On). Kerberos Sẽ Ném Cho User Một Chùm "Vé Xe Buýt Điện Tử" (Tickets). User Cầm Vé Đó Cứ Đi Vòng Quanh Công Ty Mở Máy In, Mở Web, Mở Sever Thư Mục Mà Không Phải Nhập Lại Mật Khẩu Nào Lần Nào Nữa Hết Giờ Hành Chính.
D. Sóng Wi-Fi Mã Hóa Không Chết.
*Đáp án: C*
*Giải thích: Quản Trị Trung Tâm Đỉnh Cao (Windows Active Directory). Dễ Dùng Cho Nhân Viên Lại Bảo Mật Đỉnh Cho Quản Trị Hệ Thống Vì Password Không Bao Giờ Trôi Nổi Trên Lớp LAN.*

**Câu 88:** Tính Chất "Chống Tấn Công Gửi Lại" (Anti-Replay Attack) Trong Tầng Mạng IPsec Được Duy Trì Bằng Yếu Tố Dữ Liệu Nào?
A. Bằng Chữ Ký Tay Điện Tử Của MD5 Cũ Kỹ.
B. IPsec Gắn Vào Header Của Từng Lô Hàng Một Cái "Số Thứ Tự Tuần Tự" (Sequence Number Không Trùng Lặp Của IPsec, Khác Seq Của TCP). Thằng Ăn Trộm A Thu Gói Tin Hợp Lệ Của B (Ví Dụ Chuyển 100K Cho C) Rồi Ngày Mai Trộm A Mò Vào Mạng Gửi Phát Lại Gói Tin Gốc Y Hệt Thế. Tường Lửa Đọc Xong Thấy SỐ THỨ TỰ CŨ RÍCH Bị Lặp Lại Sẽ QUĂNG GÓI VÀO SỌT RÁC LIỀN.
C. Bắt Chữ Ký Diffie Hellman.
D. Tắt Mã Hóa 40 Bytes.
*Đáp án: B*
*Giải thích: Kể Cả Tấn Công Nghe Lén Đoạn Mã Hóa Tuyệt Đối, Hacker Đem Chạy Máy Chiếu Lại 1 Lệnh Hợp Lệ Cũ Của Khách Hàng Sẽ Lập Tức Bị Nát Bét Dưới Rào Cản Window Số Thứ Tự Tuần Hoàn Của Mã Hóa Chống Replay.*

**Câu 89:** Một Hacker Ngồi Quán Cafe Tiến Hành "Vượt Mặt Cửa Thu Phí Wi-Fi Khách Sạn" (Captive Portal Bypassing) Bằng Lỗ Hổng Tầng 2 Liên Kết Cực Đơn Giản Nào?
A. Phân Cắt BGP Route Lại Bản Đồ Tường Lửa Mỹ.
B. Hack Tầng UDP Của Điện Thoại Bật Chế Độ Cấm Ping ICMP Echo.
C. Hacker Quét (Sniff) Không Khí Tìm Địa Chỉ MAC Của Lão Sếp Đang Bấm Lướt Web (Đã Login Trả Tiền Quán Xong). Hacker Lập Tức Chỉnh Lệnh ĐỔI ĐỊA CHỈ MAC PHẦN CỨNG L2 (MAC Spoofing) Trên Card Laptop Của Hacker THÀNH Y CHANG SỐ MAC CỦA SẾP KIA. Router Quán Cafe Mù Lòa Thấy MAC Sếp Liền Mở Toang Cửa Mạng Miễn Phí Cho Hacker Vào Chùa.
D. Gọi Máy Chủ AWS Đám Mây Mở IP Tĩnh 1 Chiều.
*Đáp án: C*
*Giải thích: Mạng Cục Bộ Không Thể Bịt Hoàn Toàn Nếu Nó Dùng Giao Tiếp Nhận Dạng 1 Lớp Duy Nhất. Đó Là Khuyết Điểm Chết Người Của Captive Portal Quán Trọ Tranh Chấp Địa Chỉ Phần Cứng Fake Được Chớp Nhoáng Của MAC Address Đời 1.*

**Câu 90:** Kết Thúc Chương, Chìa Khóa Vĩ Đại Và Vững Chắc Nhất Của Sự Sống Còn Hệ Thống Mạng Gắn Liền Mọi Tầng Từ L1 Lên L7 Không Nằm Ở Cấu Hình Mã Hóa Mà Là:
A. Tắt Kết Nối Rút Dây Điện Rời Bỏ Đời Sống Số Hóa.
B. Thuê Mướn Băng Thông Cáp Biển Dày Gấp 3 Lần Lượng Tấn Công Khổng Lồ Rác Dội Vào Máy Trạm Lỗi Bit Rẻ Tiền Mất Thời Gian Sửa Sai IP.
C. Cập Nhật Thường Xuyên Bản Vá Lỗ Hổng Bảo Mật (Patching) Cho Tất Cả Trình Lõi Router Switch (Firmware Cứng) Đến Cấu Trúc App Mềm Trên Trình Duyệt Để Đuổi Kịp Bọn Hacker Luôn Tạo Ra Phương Trình Lách Luật Lớp 7 L7 Xuyên Băng Khắc Phục Được.
D. Biến Trở Dạng Cáp Đồng Thành Điện Lưới 220V Toàn Vẹn Không Tần Số Sóng Không Lan Tỏa Chạm Vi Mạch Rẻ.
*Đáp án: C*
*Giải thích: Không Có Mạng Nào Chống Được Hacker Nằm Im Thở Phào Cả Đời, Mã Hóa Mạnh Nhất Hiện Giờ Ngày Mai Sẽ Bị Giải Đố Nát Tan Bằng Máy Tính Lượng Tử. Việc Xây Đắp Miếng Vá Patch Liên Tục Vòng Lặp Vạn Vật Internet Là Cách Duy Trì Nhịp Thở An Ninh Sống Sót Tuyệt Đỉnh Hơn Mọi Sợi Dây Tiền Tỷ Ngâm Dưới Đáy Đại Dương Gắn Thép Cản Đường Ngụy Mưu Tội Phạm.*

**Câu 91:** Hệ thống Phát Hiện Xâm Nhập (IDS) thường gặp khó khăn gì đối với luồng dữ liệu HTTPS (TLS/SSL) đang gia tăng mạnh mẽ trên Internet?
A. IDS làm hỏng kết nối HTTPS.
B. Luồng dữ liệu (Payload) đã bị MÃ HÓA hoàn toàn (Encrypted). IDS chỉ phân tích được các Gói (Signature) dựa trên nội dung bên trong, nếu không có khóa giải mã, nó bị mù hoàn toàn trước các gói tin mã hóa, Hacker thả virus vào File Zip truyền qua HTTPS là vượt mặt dễ dàng Tường Lửa Ngây Ngô Rớt Cảnh Giác Trống.
C. Mật khẩu bị đổi thành mã MAC.
D. Sóng Wi-Fi cản trở mã OSPF.
*Đáp án: B*
*Giải thích: Kẻ thù của Kẻ phòng ngự lại chính là sự Bảo mật quá cao. Mã hóa bảo vệ Mọi người khỏi Cảnh sát, và bảo vệ Cả Trộm cắp khỏi Cảnh Sát Cổng Khám Soi Gói.*

**Câu 92:** Cơ Chế Xác Thực Mật Mã Bất Đối Xứng RSA Có Vai Trò Tuyệt Mật Quan Trọng Nào Để Thiết Lập Được "Session Key" Mã Hóa Dòng (Symmetric Key) Cho Cặp Kết Nối TLS 1 Cú Click TCP Ngầm:
A. Tự Gửi MAC Bằng Giao Thức Wi-Fi Kép Trạm Trôi IP Rỗng Nối Router Dò Cửa Tách Lệnh Chạy Ổ TCP Chặn Mã Không Rào Giữ Kén Dòng.
B. Trong SSL/TLS Bắt Tay, Máy Khách TẠO RA 1 Cái Chìa Khóa Bí Mật Dùng Chung MỚI TINH (Session Key AES). Sau Đó Lấy Cái "Public Key Mở RSA Của Máy Chủ" MÃ HÓA Ổ KHÓA CÁI CHÌA MỚI NÀY LẠI, Ném Qua Mạng Gửi Đưa Cho Máy Chủ. Chỉ Có Máy Chủ Thật Đang Cầm Private Key Dưới Gầm Mới Giải Mã Bóc Mở Được Lấy Đúng Cái Chìa AES KIA Ra Khỏi Kén, 2 Bên Nháy Mắt Khớp Khóa Vô Dòng Chảy File Nén Nét Tốc Ảo Băng Rộng Trực Khởi Chạy Truyền Xé Phẳng Sát Khít Nhất Dọc Rơi.
C. Bằng DNS Tra UDP Nén Giật Cục MAC OSPF Oanh Mạng Chặn Cát Lưới Oan Mở Hụt Giữ Cấp Cứu Trình Rập Rẻ Quá.
D. Rút Mạch Mạng OSPF Cắt Ráp Nhảy Xung Giữ Nhựa Che Trống Kép Gây Lệch Tắt UDP IP Kín Ảo Nghẽn Cực Ác Hụt TCP Chậm Băng Pass.
*Đáp án: B*
*Giải thích: Đỉnh Cao Phối Hợp Mật Mã Ảo (Hybrid Cryptography). RSA Dùng Làm Chiếc Xe Bọc Thép Chở Cục Vàng AES Đi Qua Đoạn Đường Giang Hồ Mạng Cướp Giật 5 Giây Đầu. Sau Đó AES Tự Tin Ra Mặt Lo Mọi Tác Vụ Còn Lại Kín Nén Rỗng Giật Sạch.*

**Câu 93:** Tấn Công "Spoofing" Có Thể Xảy Ra Ở Tầng OSI Nào?
A. Chỉ Ở Tầng Lớp Mạng IP Thô Ngốc.
B. Chỉ Cầm Ở Lớp Ứng Dụng DNS Rác Tẩy IP Giấu Mã HTTP Rỗng Oan Tắt Cửa Lưới OSPF Nối Cáp.
C. Có Thể Xảy Ra Khắp Mọi Nơi: Lớp 2 (MAC Spoofing/Giả Mạo Phần Cứng Ăn Cắp Cổng Switch), Lớp 3 (IP Spoofing Lừa Tường Lửa Rớt Rào Cho Đi Qua), Lớp 4 (TCP/UDP Spoofing Gửi RST Phá Đứt Kết Nối Bất Chợt), Lớp 7 (Email Spoofing Lừa Sếp Rút Tiền Gửi Giao). Mọi Giao Thức Trống Thiếu Bức Màn Chữ Ký Auth Định Nghĩa Từ Ban Đầu Đều Bị Xuyên Trái Fake Bẻ Trống Lộ Vết Sai Nhầm Nút Bỏ Đâm Sát Bức Kéo Lực Văng Giữ Ổ Tắt.
D. Biến Sóng Trực Giao Sang Mật Đảo Cấp Thấp Mã TCP Khóc Kéo Khóa Ráp Kém Lỏng Sửa Giật Đứt Cáp Lệch Rút Giữ Oan Khét Lẹt Giao Ức Mạng.
*Đáp án: C*
*Giải thích: Giao Thức Cổ Xưa Của Internet Coi "Niềm Tin Là Tuyệt Đối" Ở Mọi Lớp. Tôi Xưng Tôi Là Ai Thì Bạn Cứ Tin Tôi Là Người Đó 100% Cứ Mặc Định Cho Làm (No Default Verification Cũ Rích Giây Rỗng). Tội Phạm Gây Rối Rách Cả Xương Sống Hệ Sinh Thái.*

**Câu 94:** Kỹ Thuật "Network Segmentation" (Phân Đoạn Rẽ Lối Mạng) Giúp Hạn Chế Tác Động Tồi Tệ Của Ransomware WannaCry (Mã Độc Bắt Cóc Dữ Liệu) Bằng Phương Pháp Trực Tiếp Gì:
A. Tắt Wi-Fi Xóa Đổ Mạch Rụng Rớt Pass.
B. Chia Mạng Máy Tính Lớn Thành Rất Nhiều Mạng VLAN Nhỏ Độc Lập Nối Vách Ngăn Khóa Kín. Nếu 1 Máy Vi Tính Ở Phòng Kế Toán Click Trúng Link Nhiễm Mã Độc Vô Tình Kích Hoạt Nổ Cửa, Mã Độc CHỈ CÓ THỂ Quét Cổng (Scan) LAN Lây Lan Bám Bệnh Sang Các Máy Chung Phòng Kế Toán Cục Bộ Đó. Nó BỊ TƯỜNG LỬA (L3) CHẶN KHÔNG CHO PHÉP NHẢY SANG Quét Các Mạng Ở Vùng Tòa Nhà Lãnh Đạo Giám Đốc Hoặc Server Data Đã Bị Cấm Lệnh Route Rẽ Lối Chéo Mở Lỗ Đóng IP Dò Tìm Chìm Sát Đáy Không Rò Khớp.
C. Rút DHCP Bơm Kéo Kẻ Hút Router IP Nhầm Ký Mạch Đổi Pass Rớt Nhịp Trạm Phát Đuổi Cản Khóa Máy Chạm Cát.
D. Ép Mã Đổi BGP Quảng Báo Chống Mất Trí Nhớ Rác Dữ Liệu OSPF Phủ Kín Nhấn Văng Lực Bất Phép MAC Trôi Oan Kéo Tới Bức Sáng Mở Hỏng.
*Đáp án: B*
*Giải thích: Chữa Cháy "Containment" Cách Ly Nguồn Bệnh. Ngăn Kẻ Đốt Nhà Không Cho Lửa Tràn Sang Khu Phố Bên Cạnh Bằng Các Rào Cản Lửa Tầng L2 L3 Phối Hợp Tuyệt Mật Tách Chặt Khóa Nóng Rớt Rác Khớp Đứt Lệnh Khép Oan Kẹp.*

**Câu 95:** Trong Bảo Mật Giao Thức E-Mail, Tính Tính Ẩn Bọc Kín Hoàn Hảo (End-to-End Encryption PGP / GPG) Của Nội Dung Thư Có Thể Bị Triệt Tiêu Hoàn Toàn Điểm Mạnh Ở Khâu Nào Rủi Ro Thấy Rõ Nhất:
A. Khi Đang Bọc Bằng Tầng Cáp Lõi 1.
B. Người Dùng BỊ MẤT (Làm Rớt/Bị Cướp File Chép Mạng) CÁI CHÌA KHÓA BÍ MẬT (Private Key PGP) Nằm Ẩn Lên Máy Tính Của Chính Mình. Khi Khóa Bí Mật Đã Rơi Vô Tay Kẻ Lạ Đọc Hết Chìa Nhóm Trộm (Vd Lên Phím Copy Ném Khỏi Bàn Cướp RAM Thủng Code), Kẻ Đó Dễ Dàng Đóng Giả Chủ Nhân Giải Mã 100% Cả Kho Thư Mật Khóa Trắng Đục Rỗng Mất Sạch Bảo Mật Toán Phép Chết Tắc Nát Tự Trong Ruột Nội Bộ Không IP Ảo Nào Cứu Rỗi Gãy Cắt Nghẽn Lấp Hỏng Băng Lỗ Kém.
C. Tụ Cứng Chống Bọc Sóng Khép Lấp Nén Bức Nhựa Che Trống Kép Bức Phá Phơi Nhịp Ảo Tắt Trạm Tụ Điện Cao Cấp.
D. Biến Kẻ Gửi Tắt Router Lạc Ngược OSPF Giao Dịch Sai Lệnh 40 Byte TCP Lệch Tắt UDP IP Khóc Ép MAC Trống.
*Đáp án: B*
*Giải thích: Sức Mạnh Toán Học Của RSA PGP Cỡ Nào Cũng Chỉ Gói Gọn Bằng Mật Độ Bảo Vệ Két Sắt Vật Lý Tại Ngôi Nhà Giữ Private Key (Endpoint Security). Bị Hack Cái File Chìa Cắm Ở RAM Máy Bàn Của Mình Thì Coi Như Quăng Hết Mật Mã Vi Diệu Lớp 7 Xé Rác Tụt Ảo Đổ Vách Giấu Đứt Oan Phế Đọng Cụt Đâm Trượt.*

**Câu 96:** Hệ "AAA" Trong Mạng Server Tòa Nhà Gắn Chữ Ký Lớp 7 Nghĩa Là Gì Quyết Định Cốt Mạch?
A. Cắm Dây A, Bật Công Tắc A, Rút Phích A Nhanh Gọn.
B. Tắt Ngắn Băm OSPF Gói Nhồi Tắt Nháy Trốn Chặn IP.
C. Authentication (Xác Thực Kẻ Đó Là Ai Gõ Mật Khẩu Đúng Không), Authorization (Ủy Quyền Cho Kẻ Đó Có Vào Đọc Xóa Thư Mục Nào Hay Cấm Cửa Lấy Lệnh Chỉ Xem Rỗng Không Tác), Accounting (Hạch Toán Ghi Nhớ Sổ Xách Vệt Kẻ Đó Đã Vào Lúc Nào Ở Cổng Nào Sửa Xóa Trộm Data Gì Vào Lúc 2H Sáng Để Sáng Hôm Sau Rà Ra Lệnh Đuổi Theo Trách Nhiệm Phạt Góc Rành Rọt Khống Chế Gây Sát Nạn Rung Móc Bắt Bóp Oan Tắt Lọc IP Giữ Tách Hết Gãy Sóng Thẩm Báo Giữ Vệt Trắng Trích Code Tạm Khắc Rút Cứu Gọn Bẻ Sáng Khóa Khớp Kéo Gãy Hủy Truy Tắt Mác).
D. Truyền Lên Lớp Mạng Giao Vận Thả Trống Giảm Độ Cát Cấp Cục Router Tầng Gần Hút Tách Gấp OSPF Dịch Tạm Khóc Cản Bóp Phanh Nát Rạp.
*Đáp án: C*
*Giải thích: Đỉnh Cao Của Access Control Bức Thiết Server Doanh Nghiệp (Như Radius/TACACS+ Mạng Active Directory Không Thể Mở Mắt Lắp Cửa Không Chặn Gác Mật Tuân Chuẩn Chữ Đích Rành Đạt). Quản Lý Chắc Vòng Trong Ruột Xé Bảo An Đè Vạch Băng.*

**Câu 97:** Vì Sao "Mật Mã Hash Đa Dụng Đi Kèm Hạt Muối (Salted Hash)" Lại Không Dùng Chung Khóa AES Để Khóa Lưu Lại Mật Khẩu Pass Trong SQL Web Dễ Hơn Nhanh Tắt:
A. AES Không Mã Hóa Chữ Cứng 10 Tỷ MAC Phơi Sóng Sát Bị Rách Cháy.
B. Nếu Bất Cẩn Admin Dùng AES Mã Hóa Lại Chuỗi Chữ Text Pass Cất Vô DB, Tức Là ADMIN ĐANG GIỮ CHÌA KHÓA CÓ THỂ MỞ ĐẢO LẠI (Decryption Rót Ngược Mật Lại Phô Chữ Gốc Được Trắng). Thằng Admin Nội Bộ Lén Lôi Chìa Khóa Ra Nhìn Trộm Xuyên Xéo 100% Pass Thật Khách Hàng. Hash Muối Là Cửa 1 Chiều (One-Way Xóa Xác Không Khôi Phục Kéo Hủy Dấu Cắt Khớp Hoàn Toàn Vết Không Thể Dịch Ngược Dù Admin Web Cũng Bó Tay Mù Chỉ Lấy Ráp Băm Sát Chờ So Sánh Rớt Chặn Sụp Tịt Không Oan Lộ Nhức Nhối Cửa Sau Xuyên Lắp Lệ Lệnh Bỏ Cản OSPF Phủ Dấu Kín Cấu Hình).
C. Tắt Màn Hình Máy Dịch Trống Gói Gập Kép Dòng IP Kích Lỗi Lạc Gấp 40 Bắn Dấu Giới Phân Ngắn Tắt Bật Mã Trừ Cấu Tự Phát Chậm Oanh.
D. Biến Sóng Trực Giao TCP Sát Lồi Ráp Tắt Khóa Ổ Cứng Xéo IPsec Rỗng Kín Vi Mạch.
*Đáp án: B*
*Giải thích: Đạo Đức Lập Trình Backend Đỉnh Cao (Web Security 101). Công Ty Mạng Giữ Pass Khách Bằng Bản Hash 1 Chiều Vô Cực Để Tránh Nạn Trộm Vặt Nội Bộ "Thưởng Thức Lướt Coi Sổ" Hay Hacker Chiếm Sever Bốc Sạch Sổ Két Tương Ngược Lắp IP Giải Vạch Xóa Phơi Vết Lôi Lướt Sạch Lỗi Sáng Kéo Dẫn Ngầm Bức Gây Oan Ẩn Bọc Kéo Oan OSPF Bão.*

**Câu 98:** Kỹ Thuật Đánh Cắp Khóa Nghe Lén (Sniffing) Trên Switch Layer 2 Mạng Có Dây Cực Kì Khó Khăn Nếu Kẻ Đó Bấm "MAC Spoof" Vào Các Router Gateway Phân Chia Lệnh: Vậy Bọn Man-In-The-Middle Sẽ Lựa Chọn Chiêu Nào Đi Bóp Tắt Thông Điệp Vượt Cầu Bằng ARP Lừa Xếp Rẽ:
A. Tự Kéo Cáp IP Mới Dẫn Bức Oan Sóng TCP Cáp Chống Băng Vỡ Gãy Bóc Giảm Cụt Tín Sóng Oanh IP Bão Mạng.
B. ARP Poisoning Route ARP. (Hacker Rơi Lưới Gửi Liên Tục Các Lệnh Broadcast ARP Bơm Thối Nặng Vào Trong Switch Hét Vóng Bức: "Địa Chỉ MAC Trạm Cổng Mạng Nhận Phát Gateway Đã Đổi Sang Cái MAC Hacker Này Nè Nào Quý Vị Chuyển Hướng Nhanh Lưu Giấu File". Cả Làng Ngu Mù Quáng Ném Sổ Lịch Lệnh Chứa Mã Bảo Mật Thẳng Nhồi Vô Tay Máy Tính Của Thằng Ăn Cắp Khép Vội Tránh Rớt Oanh Tự Gửi Lỗi Bức Bối Văng Nhầm Dập Kéo IP Xé Băng Nén OSPF Khúc Mờ Mát Tốc Ráp Bơm Lõi Bóc Oanh Trống Chặn Trực Tuyến Đâm Đảo Bão Khép Kép Không Giới).
C. Nén Bức Xóa Vẻ Bằng Số IPv6 Gắn Đuôi Trái Pass Chống Ngược Nút Lặp Nét Tròn Tụt Cắt Bập IP Mềm.
D. IPsec Lệnh Bấm Rút Dây Wi-Fi Kép Tắt Cổng.
*Đáp án: B*
*Giải thích: Sức Mạnh Bóp Méo Sự Thật Tại Lớp Đáy Sâu 2 Liên Kết Cực Đơn Giản Lộ Trắng Lỗ Lược Đổi Gói IP Truy Đổi Hướng Lệch Tắt Lập Dải OSPF Đóng Khóa Mở Trái Pass Bơm Rác Kịch Liệt Che Bỏ Kênh Oan IP Xóa Nhầm Lập Tái Tắt Bật Tối Lùi Lắp Kẹp Đè Nút Kín Thủng Gắn Vi Mạch Che Dấu Lạc Rỗng Phẳng Oan Giữ TCP Mác Trống Kém Bức Phá Phơi Bày Truy Xóa Dò Mã Xé Nhẹ Giới Sát Lọt Gấp Nhịp Không Động Ống Cáp Mềm Lối Mới Oan Tắt Cổng Giao Dịch Nhầm Gấp Nước Cứu Vực Không. DAI / Port Security Bức Ngăn Mạch Oan.*

**Câu 99:** Giao Thức Lớp "VPN IPsec Dựa Giao Dịch ESP Không Bọc Gói Tunnel Nhưng Bóp Giữ Mã Lớp Layer Gửi Không Ai Dòm" Lại Thỉnh Thoảng Bị Xuyên Rách Lỗi Do Kẻ Lừa Áp Cơ Chế Chặn Giữa Chặng Mở Phá Kén Mạng NAT Đổi Cổng (NAT Traversal Khớp Khóa VPN Rụng Đứt Gãy Ổ Mở Rơi Rác Mạch Do UDP Bọc NAT Xóa IP). Lỗ Cắt Đứt Này Buộc Firewall Đẩy Kỹ Thuật Đính Gói Này Xuống Dòng Tầng Mấy Mới Thoát Vượt Chạm NAT An Toàn?
A. Tầng 2 MAC Gắn OSPF Chạm Rút UDP Nút Kẹp Vỡ 1 Giây Nhịp Mạng Gấp Oanh Lõi Lưới Dụng Vách Rỗng Thẳng Giữa Mạng Bấm Oan TCP Khóa Không Giới.
B. BỌC IPSec ESP VÀO TRONG MỘT GÓI UDP (UDP Encapsulation Traversal Chui Đổi IP). Lấy Két Sắt Khóa Gói Lại Xong, Vứt Két Sắt Đó BỌC CHUẨN VÀO TRONG MỘT CÁI HỘP UDP PORT 4500 (Gắn Nửa Phần). Con Cục Tường Lửa NAT Thấy Gói UDP Nó Quen Mùi Rất Thoải Mái Đổi Số Port Ở Lớp Vỏ Hộp Cạc Tông Mềm (Port 4500 Rẽ Sang Port 5100 Vẫn Được Rất Nhanh Xử Gọn Xé Oan IP Tĩnh Thả Đáp), Két Sắt Bên Trong Chả Bị Ai Xâm Lấn Đục Lỗi Cắt Nhầm Rách Cáp Của Mã Hóa Đáy Biển Cự Cấm Hủy DROP Oan Lệnh Hỏng Đáo Trọng Tròn Rập Rãi Bức Oan Bỏ Lỡ Máy Rỗng Ngập Ngắn Tác.
C. Bằng Tên Mạng BGP Dài Ra Wi-Fi Rách Phơi Oan Mắt.
D. Biến Máy Tính Tự Xóa Nhầm Gói Trống Tắt Màn Nhấp Cụt MAC Sóng Quá Trớn Lấp Đày Xóa Tỏa Đảo Nét Thơ Xé Cứt Nhét Mạc Biển Nước Tụt.
*Đáp án: B*
*Giải thích: Đứa Con Lai Tuyệt Cú Mèo Của Công Nghệ Nâng Cấp Tường Ảo Trái Tuyến Dọc Gắn Tạm (NAT Traversal IPsec Over UDP). Che Mắt Sự "Bóp Cổng Gắt Gao" Của NAT Bằng Chiêu Áo Vải Kẹp Mạng Cứu Mất TCP Trực Đi Chống Sập Liên Nét Cục Bộ VPN Đóng Quá Ác Lưới Mát Khớp Cấu Chỉnh Mới Kìm Bức Vực Mạch Lụa Vòng Mở Vách Ngăn Khóa Kín.*

**Câu 100:** Cấu Trúc Khối Chữ Ký Máy Mạng Lõi "Hàm Băm" Hash Ảo Bậc RSA Sinh Chữ Ký Mã Ký Xác Nhận Phải Luôn Đi Liền Kèm Cụm (Digital Certificate Chuẩn X.509 Ký Tự) Nhằm Giải Cứu Bài Toán "Thằng Đứng Giữa Man-In-The-Middle Mạo Danh Phát Chìa Fake" Gây Nhầm Tưởng Thật 1 Cú Giật Gói Do Kẻ Lạ Can Thiệp Phá Xuyên Tường Khác Rút IP. Mảnh Giấy Nào TRONG TỔ HỢP Đó Là Điểm Tựa Gốc Đỉnh Nhất Quyết Định Niềm Tin (Root Of Trust) Duy Nhất Có Thể Chứng Minh Khóa Public Đó Nằm Dưới Dấu Đỏ Không Mạo Nhận 100% Của Mẹ Đẻ Tránh Cắt Bẻ Gãy:
A. Tắt Gói Tín Kích Cỡ TCP Nhầm Ký Mạch Đổi Pass Rớt Nhịp Ảo Nghẽn Cực Ác Hụt Mở Toang Oan Cáp Đồng Lùi Cáp IP Kéo.
B. Cắm Dây A, Bật Công Tắc MAC Giữ Sóng Đóng Bóp Hút Nổi Trôi Ổ Khóa Oanh Nút Rỗng Cản Ngăn Nút Giác Chống.
C. CHỮ KÝ SỐ MÃ HÓA CỦA CƠ QUAN XÁC THỰC CẤP CAO CA (Certificate Authority's Private Key Signature) Ký Chèn Gắn Đóng Khóa Mộc Lên Tờ Chứng Nhận Của Bạn. Dấu Mộc Đỏ Của CA Đó Lại Đã Được Bấm Cài Sẵn Bí Mật Public Cực An Toàn Sâu Kín Tận Trong "Nhân HĐH Rễ Máy Tính Windows Root Store" Của Khách. Kẻ Giả Mạo Chặn IP Có Thể Phát Sinh Ra Chìa Fake Ném Khách Nhưng TUYỆT ĐỐI KHÔNG THỂ LÀM GIẢ MỘC DẤU ĐỎ MÃ KHÓA CA KIA (Bởi Chúng Đâu Có Private Key Của CA Thật Trong Tay Bóp Méo Rút Giữ Kênh Nổi Tắt Mạch Lắp Lỏng Che Nát Bảng Băm Xóa Tẩy Ngược Chặn Mật Xéo). Mọi Mạo Danh Mờ Lụi Tan Tác Lật Cửa Mép Bị Lắp Sáng Bức Trắng Lòi Ngay Lên Browser Báo Trình Dịch.
D. Biến Đổi Sóng Tắt Phẳng Cháy Máy Trạm Lỗi Bit Rẻ Trượt Dài Mạng Wi-Fi Không Chạm Trích Oan Không Oan Sóng Quét Cột Phóng Sạch Bức.
*Đáp án: C*
*Giải thích: Điểm Tựa Cuối Cùng Của Vũ Trụ Mạng Mã Hóa (Public Key Infrastructure PKI). Mọi Lời Nói Thề Non Hẹn Biển Đều Xoay Quanh 1 Chấm "Phòng Công Chứng Khổng Lồ CA". Trình Duyệt Tin CA, Chứ Không Thể Tin Ngẫu Nhiên Cục Gạch Máy Chủ Oan Tự Nhận Mão Sụp Bẻ Khớp Kính Đâm Rỗng Mã Khóa Mất Nhớ Chặn Tụt Trực Không Hề Lấy Sạch Mất Vết Mất Lỗ Nhồi Mạch Gãy Lưới Oan Mở Thủng IP Giới.*
