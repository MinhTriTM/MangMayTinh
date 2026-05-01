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

**Câu 101:** Kỹ thuật Steganography (Giấu thư) trong an toàn thông tin có nghĩa là gì?
A. Mã hóa thông điệp thành một chuỗi ký tự ngẫu nhiên
B. Kỹ thuật che giấu sự tồn tại của thông điệp bên trong một phương tiện mang khác (như hình ảnh, âm thanh, video), sao cho người ngoài không hề biết có thông tin bí mật đang được truyền đi
C. Tạo ra chữ ký số để xác thực nguồn gốc
D. Một phương thức tấn công từ chối dịch vụ
*Đáp án: B*
*Giải thích: Trong khi Cryptography (Mật mã học) che giấu "nội dung" thông điệp (người ta biết có thông điệp mã hóa ở đó nhưng không đọc được), thì Steganography che giấu luôn cả "sự tồn tại" của thông điệp. Một bức ảnh số bình thường trên website có thể chứa thông điệp giấu kín bên trong các bit dữ liệu thưa.*

**Câu 102:** Tính chất Non-repudiation (Chống chối bỏ) trong an ninh mạng được thực hiện hiệu quả nhất nhờ vào công nghệ nào sau đây?
A. Mã hóa đối xứng (Symmetric Encryption)
B. Tường lửa (Firewall)
C. Chữ ký số (Digital Signatures) sử dụng Khóa riêng (Private Key)
D. Hàm băm (Hash Functions) đơn thuần
*Đáp án: C*
*Giải thích: Chữ ký số giải quyết tính chống chối bỏ. Vì chỉ có Alice mới sở hữu Khóa riêng của cô ấy, nếu một văn bản được ký bằng Khóa riêng đó và giải mã/kiểm chứng thành công bằng Khóa công khai của Alice, thì không ai khác ngoài Alice có thể tạo ra chữ ký đó. Alice không thể chối bỏ việc mình đã gửi thông điệp.*

**Câu 103:** Kẻ tấn công sử dụng công cụ Nmap gửi các gói tin TCP với cờ SYN được bật tới một loạt các cổng trên máy chủ mục tiêu. Kỹ thuật này được gọi là gì?
A. SYN Flood DoS Attack
B. Port Scanning (Quét cổng - SYN Stealth Scan)
C. IP Spoofing
D. ARP Cache Poisoning
*Đáp án: B*
*Giải thích: Gửi gói TCP SYN là kỹ thuật cốt lõi của Port Scanning (Quét cổng rà quét lỗ hổng). Nmap chờ xem cổng mục tiêu phản hồi bằng SYN-ACK (cổng đang mở) hay RST (cổng đóng) để lập bản đồ các dịch vụ đang chạy trên Server.*

**Câu 104:** Phương pháp tấn công "Phishing" (Lừa đảo qua mạng) nhắm vào đối tượng/tầng nào yếu nhất trong hệ thống bảo mật?
A. Tầng vật lý (Physical Layer)
B. Giao thức định tuyến OSPF
C. Thuật toán mã hóa AES
D. Yếu tố Con người (Social Engineering / Human factor)
*Đáp án: D*
*Giải thích: Phishing không cố gắng bẻ khóa công nghệ mà lừa gạt tâm lý con người. Hacker gửi email giả mạo ngân hàng/nhà cung cấp dịch vụ yêu cầu người dùng tự nguyện nhấp vào liên kết độc hại hoặc tự cung cấp mật khẩu, OTP.*

**Câu 105:** Sự khác biệt cốt lõi giữa IDS (Intrusion Detection System) và IPS (Intrusion Prevention System) là gì?
A. IDS hoạt động ở Layer 3, IPS hoạt động ở Layer 7
B. IDS chỉ là phần mềm, IPS luôn là thiết bị phần cứng
C. IDS chỉ theo dõi và phát ra cảnh báo khi phát hiện bất thường/tấn công (Giám sát thụ động), trong khi IPS được đặt trên đường truyền (in-line) và có khả năng TỰ ĐỘNG CHẶN (drop) các gói tin mang mã độc trước khi chúng đến đích (Phòng chống chủ động)
D. IDS dùng để mã hóa dữ liệu, IPS dùng để giải mã
*Đáp án: C*
*Giải thích: Chữ "Detection" (Phát hiện) so với "Prevention" (Ngăn chặn). IPS can thiệp trực tiếp vào luồng traffic để cắt đứt liên lạc của luồng dữ liệu độc hại ngay lập tức.*

**Câu 106:** "Zero-Day Exploit" (Khai thác Zero-Day) là gì?
A. Cuộc tấn công xảy ra vào đúng nửa đêm
B. Cuộc tấn công khai thác một lỗ hổng phần mềm hoặc phần cứng chưa từng được biết đến, mà chính nhà sản xuất cũng chưa phát hiện ra hoặc chưa có bản vá (patch) để khắc phục
C. Virus máy tính xóa toàn bộ dữ liệu ổ cứng về mức số không
D. Hành động tấn công nhằm làm sập toàn bộ hệ thống ngay trong ngày đầu tiên triển khai
*Đáp án: B*
*Giải thích: Zero-day (Ngày Không) chỉ việc thời gian (số ngày) mà nhà sản xuất có để vá lỗ hổng tính từ lúc nó bị hacker khai thác là bằng 0. Đây là loại tấn công cực kỳ nguy hiểm vì các phần mềm diệt virus hoặc tường lửa chữ ký (signature-based) thường không thể nhận diện được.*

**Câu 107:** Trong IPSec, chế độ (mode) nào mã hóa TRỌN VỘN toàn bộ gói tin IP ban đầu (bao gồm cả IP Header của máy gửi gốc), sau đó bọc nó vào bên trong một gói tin IP mới với IP Header mới (thường là IP của Router/VPN Gateway)?
A. Transport Mode
B. Tunnel Mode
C. ESP Mode
D. AH Mode
*Đáp án: B*
*Giải thích: Tunnel Mode (Chế độ đường hầm) thường được dùng cho các kết nối VPN site-to-site (giữa hai Router). Nó giấu kín cấu trúc IP bên trong mạng nội bộ, chỉ phơi bày địa chỉ IP của hai Gateway VPN ở bên ngoài Internet.*

**Câu 108:** Trong IPSec Transport Mode, thành phần nào của gói tin IP gốc BỊ mã hóa nếu sử dụng giao thức ESP (Encapsulating Security Payload)?
A. Chỉ mã hóa phần IP Header gốc
B. Mã hóa toàn bộ gói tin IP
C. Chỉ mã hóa phần Payload (TCP/UDP Header và dữ liệu ứng dụng) nằm sau IP Header gốc, IP Header gốc vẫn giữ nguyên để định tuyến
D. Không mã hóa gì cả, chỉ thêm mã xác thực
*Đáp án: C*
*Giải thích: Transport Mode (Chế độ vận chuyển) thường dùng cho kết nối Host-to-Host (Client to Server). Nó chỉ bảo vệ dữ liệu tải (payload) và giữ nguyên IP Header gốc để hệ thống mạng bên dưới vẫn có thể định tuyến gói tin từ đầu đến cuối.*

**Câu 109:** Tường lửa phân tích trạng thái (Stateful Packet Inspection - SPI Firewall) vượt trội hơn tường lửa lọc gói tin không trạng thái (Stateless Packet Filter) ở khả năng nào?
A. Lọc nội dung email để tìm mã độc
B. Có khả năng ghi nhớ "trạng thái" của các kết nối mạng đang hoạt động (ví dụ: đang trong trạng thái TCP 3-way handshake hay Established). Từ đó nó biết một gói tin đến là hợp lệ thuộc về một phiên đã được phép, hay là một gói tin giả mạo đánh lừa
C. Tốc độ xử lý siêu nhanh (wire-speed) do không cần tra bảng bộ nhớ
D. Mã hóa được tất cả lưu lượng đi qua nó
*Đáp án: B*
*Giải thích: Stateless Firewall chỉ kiểm tra từng gói tin đơn lẻ dựa trên IP/Port. Stateful Firewall thông minh hơn, nó lập một Bảng trạng thái kết nối (Connection State Table). Nếu mạng nội bộ khởi tạo một kết nối HTTP ra ngoài, Firewall sẽ tự động cho phép gói phản hồi từ web server đi ngược vào trong mà không cần lập cấu hình "cho phép Inbound port 80".*

**Câu 110:** Lỗ hổng "Buffer Overflow" (Tràn bộ đệm) thường bị khai thác để đạt được mục đích gì?
A. Làm sập nguồn điện của máy chủ
B. Chèn một đoạn mã độc (như Shellcode) vào vùng nhớ bị tràn và thao túng thanh ghi điều khiển của CPU (ví dụ Instruction Pointer) để ép chương trình thực thi đoạn mã độc đó (chiếm quyền điều khiển hệ thống - RCE)
C. Tăng tốc độ băng thông mạng
D. Đoán mật khẩu mã hóa WEP
*Đáp án: B*
*Giải thích: Do phần mềm lập trình kém không kiểm tra giới hạn độ dài của dữ liệu đầu vào. Hacker gửi lượng dữ liệu lớn hơn kích thước bộ đệm cho phép, dữ liệu thừa sẽ tràn sang vùng nhớ bên cạnh (vùng chứa địa chỉ con trỏ lệnh), cho phép chiếm quyền (Remote Code Execution).*

**Câu 111:** Tấn công "SQL Injection" (Tiêm mã SQL) xảy ra ở tầng nào trong mô hình OSI?
A. Tầng Liên kết dữ liệu (Layer 2)
B. Tầng Mạng (Layer 3)
C. Tầng Giao vận (Layer 4)
D. Tầng Ứng dụng (Layer 7)
*Đáp án: D*
*Giải thích: SQL Injection nhắm vào các ứng dụng Web (Layer 7) có tương tác với cơ sở dữ liệu. Hacker nhập các lệnh SQL ác ý thông qua các form đăng nhập hoặc URL để thao túng cơ sở dữ liệu (đánh cắp thông tin, xóa dữ liệu).*

**Câu 112:** Kỹ thuật nào là cách phòng thủ cơ bản và hiệu quả nhất chống lại tấn công SQL Injection cho các lập trình viên Web?
A. Cài đặt phần mềm diệt virus mạnh nhất trên Web Server
B. Sử dụng "Prepared Statements" (Truy vấn được chuẩn bị trước / Tham số hóa - Parameterized Queries) để tách biệt rạch ròi giữa câu lệnh SQL và dữ liệu đầu vào của người dùng
C. Dùng giao thức HTTPS thay vì HTTP
D. Tăng kích thước bộ đệm của cơ sở dữ liệu
*Đáp án: B*
*Giải thích: Prepared Statements ép cơ sở dữ liệu xử lý chuỗi nhập vào từ người dùng CHỈ như là dữ liệu thuần túy (Data/Value), chứ không bao giờ xem đó là mã lệnh thao tác thực thi (Executable Code), từ đó vô hiệu hóa hoàn toàn SQL Injection.*

**Câu 113:** Sự khác biệt chính giữa Virus máy tính và Worm (Sâu máy tính) là gì?
A. Virus phá hoại phần cứng, Worm phá hoại phần mềm
B. Virus cần phải lây nhiễm/đính kèm vào một tập tin thực thi (file host) khác và CẦN sự tương tác của người dùng (như click mở file) để kích hoạt. Còn Worm là chương trình độc lập, CÓ THỂ TỰ ĐỘNG sao chép và tự lây lan sang các máy khác qua lỗ hổng mạng mà không cần người dùng thao tác
C. Virus có kích thước lớn hơn Worm
D. Worm dễ bị phần mềm diệt virus phát hiện hơn
*Đáp án: B*
*Giải thích: Tính tự lan truyền tự động qua môi trường mạng (khai thác lỗ hổng OS hoặc dùng mật khẩu yếu) là đặc trưng nguy hiểm nhất của Worm (ví dụ: sâu WannaCry lây lan qua lỗ hổng SMB của Windows).*

**Câu 114:** "Trojan Horse" (Ngựa chiến thành Troy) trong an ninh mạng là loại phần mềm độc hại có đặc điểm gì?
A. Nó tự nhân bản với tốc độ cực nhanh trên môi trường mạng
B. Nó ngụy trang thành một phần mềm hợp pháp, hữu ích (ví dụ phần mềm bẻ khóa, game) để đánh lừa người dùng tự tay tải về và cài đặt, mở "cửa hậu" (backdoor) cho kẻ tấn công kiểm soát máy tính
C. Nó chuyên đi xóa các file hệ thống
D. Nó là một loại tường lửa phần cứng do hacker cài cắm
*Đáp án: B*
*Giải thích: Lấy cảm hứng từ sự tích con ngựa gỗ thành Troy, phần mềm độc hại này ẩn chứa bên trong một lớp vỏ bọc vô hại. Khi người dùng tự tay mở nó lên, mã độc bên trong sẽ âm thầm thực thi quyền truy cập trái phép.*

**Câu 115:** Cuộc tấn công Ransomware (Mã độc tống tiền) thường thực hiện hành vi nào sau đây trên máy tính nạn nhân?
A. Âm thầm theo dõi thao tác gõ phím (Keylogger)
B. Sử dụng thuật toán mã hóa khóa công khai (như RSA/AES) để mã hóa toàn bộ dữ liệu quan trọng của nạn nhân, sau đó đòi tiền chuộc (thường là Bitcoin) để trao lại chìa khóa giải mã
C. Đánh cắp băng thông mạng để tấn công máy chủ khác
D. Xóa ngay lập tức bộ nhớ ROM
*Đáp án: B*
*Giải thích: Ransomware (như WannaCry, Petya) biến dữ liệu của nạn nhân thành các khối mã hóa không thể đọc được. Điểm mấu chốt là chìa khóa giải mã (Private key) chỉ nằm trên máy chủ của hacker.*

**Câu 116:** Trong một môi trường PKI (Hạ tầng khóa công khai), danh sách các chứng chỉ số (Digital Certificates) đã bị máy chủ CA thu hồi trước khi hết hạn (ví dụ do lộ khóa bí mật hoặc nhân viên nghỉ việc) được gọi là gì?
A. ACL (Access Control List)
B. DNS (Domain Name System)
C. CRL (Certificate Revocation List) hoặc kiểm tra qua giao thức OCSP trực tuyến
D. NAT Table
*Đáp án: C*
*Giải thích: CA định kỳ phát hành Danh sách Thu hồi Chứng chỉ (CRL). Các trình duyệt hoặc ứng dụng khi xác thực chứng chỉ phải kiểm tra xem chứng chỉ đó có nằm trong CRL hay không, hoặc hỏi trực tiếp CA thông qua giao thức OCSP (Online Certificate Status Protocol).*

**Câu 117:** Mật mã đường cong elliptic (ECC - Elliptic-curve cryptography) cung cấp lợi thế gì đáng kể so với mật mã RSA truyền thống?
A. Dễ lập trình hơn bằng ngôn ngữ C++
B. Cung cấp cùng một mức độ bảo mật (độ khó giải mã) nhưng sử dụng kích thước chiều dài khóa (Key length) NHỎ HƠN RẤT NHIỀU so với RSA (ví dụ: ECC 256-bit tương đương RSA 3072-bit), giúp việc tính toán cực kỳ nhanh và tiết kiệm tài nguyên trên thiết bị di động/IoT
C. Không thể bị bẻ khóa bởi máy tính lượng tử
D. Không cần dùng đến khóa công khai
*Đáp án: B*
*Giải thích: Ưu điểm tuyệt đối của thuật toán đường cong Elliptic là hiệu suất cực cao (tiêu tốn ít RAM, CPU, pin) trong khi vẫn đảm bảo mã hóa phi đối xứng siêu mạnh.*

**Câu 118:** Giao thức RADIUS (Remote Authentication Dial-In User Service) thực hiện việc mã hóa dữ liệu giữa máy khách NAS (Network Access Server / Access Point) và máy chủ xác thực RADIUS Server như thế nào?
A. Mã hóa toàn bộ gói tin từ đầu đến cuối
B. Không mã hóa gì cả
C. Chỉ mã hóa phần trường chứa Mật khẩu (Password field) của người dùng bằng một "Shared Secret" (Khóa bí mật chia sẻ chung), trong khi phần tên đăng nhập (Username) và các thông số khác được gửi dạng bản rõ (plaintext)
D. Mã hóa bằng chứng chỉ số RSA
*Đáp án: C*
*Giải thích: Một hạn chế thiết kế lịch sử của RADIUS là nó chỉ bảo vệ thuộc tính mật khẩu. Trong khi TACACS+ (một giao thức tương tự của Cisco) thì mã hóa toàn bộ payload của gói tin xác thực.*

**Câu 119:** Tấn công "Cross-Site Scripting" (XSS) chủ yếu xảy ra do lỗi gì trên ứng dụng Web?
A. Cấu hình sai Tường lửa (Firewall)
B. Ứng dụng Web tiếp nhận dữ liệu từ người dùng (như comment trên diễn đàn) nhưng không lọc (Sanitize/Encode) các ký tự đặc biệt, khiến mã kịch bản độc hại (thường là JavaScript) của hacker bị nhúng vào trang web và ĐƯỢC THỰC THI TRÊN TRÌNH DUYỆT CỦA CÁC NẠN NHÂN KHÁC khi họ mở trang web đó ra xem
C. Rò rỉ mật khẩu của cơ sở dữ liệu
D. Lỗi tràn bộ đệm trên máy chủ web Apache
*Đáp án: B*
*Giải thích: Mục tiêu của XSS (khác với SQLi nhắm vào Database) là nhắm vào người dùng truy cập trang web (client-side). Mã JavaScript độc hại chạy trên trình duyệt nạn nhân có thể đánh cắp Cookie phiên làm việc (Session ID) và gửi về máy hacker.*

**Câu 120:** Loại tấn công XSS nào nguy hiểm nhất vì đoạn mã độc được lưu trữ vĩnh viễn trên cơ sở dữ liệu của máy chủ web và sẽ kích hoạt trên bất kỳ trình duyệt của người dùng nào truy cập vào trang chứa nội dung đó?
A. Reflected XSS
B. DOM-based XSS
C. Stored XSS (Persistent XSS)
D. Blind XSS
*Đáp án: C*
*Giải thích: Stored XSS là loại mà payload độc hại (ví dụ: `<script>stealCookie()</script>`) được lưu luôn vào Database (qua một bình luận bài viết, profile user). Bất cứ ai vào xem bình luận đó đều bị dính mã độc.*

**Câu 121:** Giao thức bảo mật TLS (Transport Layer Security) trong quá trình "Handshake" (bắt tay) giai đoạn đầu sử dụng loại mật mã nào để hai bên thỏa thuận chung một Khóa phiên (Session Key)?
A. Mật mã đối xứng thuần túy (AES)
B. Hàm Băm (MD5, SHA-1)
C. Mật mã phi đối xứng / Khóa công khai (Asymmetric Cryptography, ví dụ: RSA hoặc Diffie-Hellman)
D. Thuật toán mã hóa dòng RC4
*Đáp án: C*
*Giải thích: Việc tạo ra Khóa đối xứng dùng một lần (Session Key) để mã hóa hàng loạt dữ liệu (Bulk encryption) yêu cầu hai bên phải "bắt tay" trao đổi thông số bí mật một cách an toàn qua đường truyền không an toàn. Điều này bắt buộc phải dùng sức mạnh của Mã hóa Phi đối xứng.*

**Câu 122:** Lỗ hổng "Heartbleed" (Trái tim rỉ máu) khét tiếng là một lỗi lập trình nghiêm trọng nằm trong thư viện mã nguồn mở nào?
A. Apache HTTP Server
B. OpenSSL (Trong việc xử lý gói tin "Heartbeat" mở rộng của TLS)
C. Lõi nhân (Kernel) hệ điều hành Linux
D. Trình duyệt Google Chrome
*Đáp án: B*
*Giải thích: Heartbleed do lỗi bộ nhớ (bounds-checking) của OpenSSL. Kẻ tấn công có thể "hỏi" máy chủ một gói tin Heartbeat lừa gạt, khiến máy chủ trả về (rò rỉ) 64KB bộ nhớ RAM ngẫu nhiên đang chạy, làm lộ vô số mật khẩu, cookie và cả Khóa Private Key của chứng chỉ số SSL.*

**Câu 123:** Khái niệm "Honeypot" (Hũ mật) trong an ninh mạng là một thiết bị hoặc hệ thống được thiết lập với mục đích gì?
A. Nơi chứa các bản sao lưu (backup) dữ liệu tuyệt mật
B. Cố tình giả lập thành một mục tiêu hấp dẫn, dễ bị tổn thương để dụ dỗ tin tặc (hacker) tấn công vào đó. Qua đó hệ thống có thể theo dõi hành vi, thu thập kỹ thuật tấn công (TTPs) của hacker hoặc đánh lạc hướng chúng khỏi máy chủ thật
C. Máy chủ chuyên để quét virus cho email
D. Thuật toán băm mật khẩu nâng cao
*Đáp án: B*
*Giải thích: Giống như cái bẫy ruồi, Honeypot không chứa giá trị thực sự cho tổ chức, bất kỳ lưu lượng nào quét hoặc tấn công vào Honeypot đều chắc chắn 100% là hành vi độc hại.*

**Câu 124:** Để bảo vệ tính bảo mật và chống lại tấn công nghe lén (Sniffing) trong một mạng LAN nội bộ (Layer 2), quản trị viên nên áp dụng công nghệ nào trên các switch?
A. Sử dụng Hub thay cho Switch
B. Port Security (Bảo mật cổng vật lý, giới hạn số lượng địa chỉ MAC) và DHCP Snooping/Dynamic ARP Inspection
C. Tắt giao thức STP
D. Đặt IP tĩnh cho mọi máy
*Đáp án: B*
*Giải thích: Đa số các cuộc tấn công Layer 2 (MAC Flooding ép switch thành Hub để nghe lén, ARP Spoofing) có thể bị chặn bởi các tính năng kiểm soát lớp 2 tích hợp sẵn trên các Switch được quản lý (Managed Switch) như Port Security và cấu hình DAI (Dynamic ARP Inspection).*

**Câu 125:** "Botnet" là thuật ngữ dùng để chỉ một hệ thống bao gồm:
A. Các robot vật lý trong dây chuyền sản xuất được kết nối mạng
B. Mạng lưới hàng ngàn, hàng triệu máy tính/thiết bị IoT (như camera, router) bị nhiễm mã độc "Zombie" và bị điều khiển từ xa bí mật (Command and Control - C&C) bởi hacker để thực hiện các chiến dịch phát tán thư rác (Spam) hoặc Tấn công từ chối dịch vụ phân tán (DDoS) với quy mô khổng lồ
C. Hệ thống phần mềm chatbot trí tuệ nhân tạo
D. Các máy chủ đào tiền ảo hợp pháp
*Đáp án: B*
*Giải thích: Sức mạnh của các cuộc tấn công DDoS quy mô cấp quốc gia (ví dụ Botnet Mirai) đến từ việc huy động đồng thời tài nguyên của hàng vạn thiết bị ngây thơ đã bị cấy mã độc Bot.*

**Câu 126:** Cơ chế bảo mật "MAC Address Filtering" (Lọc địa chỉ MAC) trên các router Wi-Fi gia đình có được xem là biện pháp bảo mật mạnh mẽ chống lại hacker chuyên nghiệp không? Tại sao?
A. Có, vì địa chỉ MAC là duy nhất trên toàn thế giới và không thể bị giả mạo phần cứng
B. Không, vì hacker sử dụng phần mềm phân tích mạng vô tuyến dễ dàng chụp (sniff) được các khung tin MAC hợp pháp đang bay trong không khí (vì MAC Header không bị mã hóa) và có thể sử dụng công cụ để "nhái" (MAC Spoofing/Cloning) địa chỉ MAC đó để vượt qua màng lọc dễ dàng
C. Có, vì bộ lọc này mã hóa toàn bộ dữ liệu ở mức Layer 2
D. Không, vì máy tính có thể đổi địa chỉ IP
*Đáp án: B*
*Giải thích: Lọc MAC chỉ cản trở được người dùng bình thường vô tình kết nối, hoàn toàn vô tác dụng với kẻ tấn công có chủ ý vì địa chỉ MAC gửi đi luôn ở dạng bản rõ.*

**Câu 127:** VPN (Virtual Private Network) sử dụng kỹ thuật cốt lõi nào để cho phép các nhân viên làm việc từ xa (Remote worker) truy cập vào mạng doanh nghiệp một cách an toàn qua đường truyền Internet công cộng không tin cậy?
A. Tunneling (Đóng gói dữ liệu bọc trong một đường hầm mã hóa, ví dụ dùng IPSec, OpenVPN, WireGuard) để dữ liệu không bị đọc trộm hay sửa đổi trên đường đi
B. Thay đổi định tuyến của các gói tin TCP bằng BGP
C. Tạo ra một mạng cáp quang riêng biệt trên toàn cầu
D. Sử dụng thuật toán băm (Hash) lên toàn bộ file dữ liệu
*Đáp án: A*
*Giải thích: Mạng Ảo Riêng ảo hóa một kết nối điểm-điểm riêng biệt thông qua sự hỗn mang của Internet, bằng cách thiết lập cơ chế Tunnel (đóng gói) kết hợp mã hóa siêu mạnh.*

**Câu 128:** Trong xác thực mạng (Authentication), ba yếu tố cơ bản (3 factors) để xác minh danh tính người dùng là gì?
A. Mã PIN, Mật khẩu, Câu hỏi bí mật
B. Something you KNOW (Thứ bạn biết - vd: Mật khẩu), Something you HAVE (Thứ bạn có - vd: Token, SMS OTP, Smartcard), Something you ARE (Thứ thuộc về bạn - Sinh trắc học vd: Vân tay, Mống mắt)
C. Tên đăng nhập, Mật khẩu, Mật mã
D. IP, Địa chỉ MAC, Tọa độ GPS
*Đáp án: B*
*Giải thích: Hệ thống Xác thực Đa yếu tố (MFA - Multi-Factor Authentication) mạnh mẽ phải kết hợp ít nhất 2 trong 3 yếu tố khác biệt này lại với nhau (ví dụ: rút tiền ATM cần Thẻ - Have, và mã PIN - Know).*

**Câu 129:** Kỹ thuật "Sandboxing" (Hộp cát) trong bảo mật máy tính đóng vai trò gì?
A. Là vùng chứa rác dữ liệu
B. Là môi trường cô lập nghiêm ngặt, khép kín (thường là một máy ảo cách ly), dùng để chạy thử hoặc phân tích hành vi của các tập tin/phần mềm nghi ngờ là mã độc một cách an toàn mà không sợ lây nhiễm ra hệ điều hành thực tế
C. Là quá trình làm phân mảnh đĩa cứng
D. Mã hóa các tập tin log của hệ thống
*Đáp án: B*
*Giải thích: Các giải pháp phòng chống APT (Advanced Persistent Threat) hiện đại đưa mọi file tải về vào một Sandbox (hộp cát). Nếu file đó âm thầm thay đổi Registry hệ thống hoặc đòi quyền Admin, nó sẽ bị tiêu diệt ngay.*

**Câu 130:** Trong lĩnh vực mã hóa, "Salting" (Thêm muối) là thao tác gì khi lưu trữ mật khẩu trong cơ sở dữ liệu?
A. Mã hóa mật khẩu thành dạng nhị phân
B. Cắt ngắn mật khẩu cho bớt dung lượng
C. Thêm một chuỗi ký tự ngẫu nhiên duy nhất (Salt) vào mật khẩu ban đầu CỦA TỪNG NGƯỜI DÙNG trước khi đưa qua Hàm Băm (Hash). Nhằm bảo vệ mật khẩu chống lại các cuộc tấn công quét bảng tra cứu từ điển tính sẵn (Rainbow Tables Attack) và tránh việc 2 người có mật khẩu giống nhau thì sinh ra mã băm giống nhau
D. Nén mật khẩu bằng thuật toán Zip
*Đáp án: C*
*Giải thích: Hàm băm Hash("password123") luôn ra cùng một chuỗi ở bất kỳ đâu. Kẻ tấn công có thể tính trước bảng băm của tỷ mật khẩu. Salting là việc sinh ra Hash("password123" + "j7H9k2"). Salt được lưu công khai kèm theo Hash trong Database. Khiến kẻ tấn công không thể dùng bảng băm có sẵn mà phải tính lại từ đầu cho từng user.*

**Câu 131:** Tấn công "Denial of Service" (DoS) tập trung khai thác điểm yếu gì của hệ thống mục tiêu?
A. Mật khẩu yếu của quản trị viên hệ thống
B. Khai thác sự hữu hạn của tài nguyên hệ thống (Băng thông mạng, CPU, Bộ nhớ RAM, hoặc Bảng trạng thái kết nối) bằng cách làm tràn ngập các yêu cầu rác, khiến hệ thống tê liệt và KHÔNG THỂ phục vụ các yêu cầu hợp pháp của người dùng thật
C. Sao chép trộm mã nguồn (Source Code) trang web
D. Tấn công vật lý vào máy chủ
*Đáp án: B*
*Giải thích: Nguyên lý cốt lõi của DoS (và phiên bản phân tán DDoS) không nhằm mục đích lấy cắp dữ liệu, mà là cản trở, đình trệ sự vận hành của thiết bị/dịch vụ mạng bằng sự áp đảo tài nguyên (như băng thông hay bộ nhớ phiên kết nối TCP).*

**Câu 132:** Kỹ thuật "ARP Spoofing" (Giả mạo ARP) cho phép kẻ tấn công nội bộ (Local Attacker) thực hiện hành vi nguy hiểm nào?
A. Xóa ổ đĩa C của máy chủ
B. Vượt qua tường lửa mạng bằng cách đổi port
C. Đánh lừa máy nạn nhân (và có thể cả Gateway/Router) tin rằng địa chỉ MAC của máy kẻ tấn công chính là địa chỉ MAC của Default Gateway. Qua đó, toàn bộ dữ liệu đi Internet của nạn nhân sẽ bị "lái" (redirect) chạy xuyên qua máy tính của kẻ tấn công, thiết lập cuộc tấn công Man-in-the-Middle (Đứng giữa) ở Layer 2
D. Đọc được thư mục chia sẻ (SMB) được cài pass
*Đáp án: C*
*Giải thích: Giao thức phân giải địa chỉ (ARP) thiếu cơ chế xác thực. Bất kỳ máy tính nào trong mạng LAN cũng có thể gửi các bản tin ARP Reply (ARP Reply mạo danh IP của Router nhưng kèm theo MAC của Hacker) để đầu độc bảng lưu trữ ARP (ARP Cache Poisoning) của máy trạm khác.*

**Câu 133:** Cơ chế bảo mật IPsec có hai giao thức thành phần chính chịu trách nhiệm về mã hóa và chứng thực là:
A. TCP và UDP
B. IKE (Internet Key Exchange) và ISAKMP
C. AH (Authentication Header) và ESP (Encapsulating Security Payload)
D. SSL và TLS
*Đáp án: C*
*Giải thích: Giao thức IPsec quy định 2 framework truyền tải: AH (chỉ cung cấp tính toàn vẹn và xác thực nguồn gốc cho gói tin IP, KHÔNG mã hóa) và ESP (cung cấp khả năng bảo mật bằng cách MÃ HÓA toàn bộ Payload, kết hợp cả tính toàn vẹn).*

**Câu 134:** Lỗ hổng "Path Traversal" (Duyệt qua thư mục - hoặc Directory Traversal) trên web server là kỹ thuật khai thác gì?
A. Sử dụng phần mềm tự động dò tìm (crawl) toàn bộ URL của website
B. Thay đổi giao thức HTTP sang HTTPS
C. Chèn các chuỗi ký tự đặc biệt (ví dụ: `../` hoặc `%2e%2e%2f`) vào tham số URL hoặc Form nhập liệu để đánh lừa máy chủ web truy cập vào và đọc các tập tin hệ thống nhạy cảm (ví dụ `/etc/passwd` trên Linux hoặc file cấu hình database) nằm NGOÀI thư mục gốc của trang web (Web root directory)
D. Tạo ra hàng loạt các thư mục rỗng làm đầy ổ cứng
*Đáp án: C*
*Giải thích: Lập trình viên thiết kế tính năng tải file nhưng không kiểm soát (sanitize) chặt đường dẫn tên file mà user truyền lên. User có thể gọi tệp `../../../windows/system32/config/sam` để ăn trộm database mật khẩu Windows.*

**Câu 135:** Mật mã khóa bất đối xứng (Public Key Cryptography - như RSA) giải quyết bài toán lớn nhất nào của Mật mã khóa đối xứng (Symmetric Encryption - như AES)?
A. Giải quyết vấn đề tốc độ mã hóa chậm
B. Giải quyết bài toán "Phân phối khóa" (Key Distribution Problem). Trong khóa đối xứng, Alice và Bob ở xa nhau không biết cách nào để trao đổi Khóa bí mật chung một cách an toàn mà không sợ bị kẻ trộm trên đường bắt được khóa đó
C. Giải quyết vấn đề kích thước file mã hóa quá lớn
D. Giải quyết bài toán bảo vệ hệ điều hành
*Đáp án: B*
*Giải thích: Nếu chưa gặp nhau bao giờ, làm sao bạn gửi khóa két sắt qua bưu điện mà không sợ bị nhân viên mở xem trộm chìa khóa? Mã hóa phi đối xứng cho phép Bob gửi công khai "Ổ khóa đã mở" (Khóa Public), Alice nhét dữ liệu vào, bấm khóa lại gửi đi, và chỉ duy nhất "Chìa khóa" (Khóa Private) trong túi Bob mới mở được hòm.*

**Câu 136:** Tấn công Phân mảnh gói tin (IP Fragmentation Attack, ví dụ Teardrop Attack) lợi dụng điểm yếu nào của hệ thống?
A. Tấn công vào lỗ hổng bảo mật của giao thức FTP
B. Việc gửi các mảnh cắt (fragments) của gói tin IP được tạo ra một cách có chủ ý bị lỗi chồng chéo phần bù (overlapping offset) hoặc kích thước bất hợp lý, làm cho bộ đệm ghép nối gói tin (reassembly) của hệ điều hành đích bị tính toán nhầm, gây lỗi tràn bộ đệm và treo máy (Kernel Panic/Blue Screen)
C. Gửi hàng triệu gói tin ICMP Echo siêu nhỏ
D. Đổi cờ IP header liên tục
*Đáp án: B*
*Giải thích: Các giao thức truyền thông TCP/IP quy định nếu một gói tin lớn (Layer 3) đi qua một liên kết có MTU nhỏ hơn, nó phải bị cắt nhỏ thành các IP Fragment. Nếu thiết kế HĐH xử lý các fragment cố tình "chèn" lên nhau (Offset) một cách kém cỏi, HĐH sẽ sụp đổ.*

**Câu 137:** Kỹ thuật Phân tích phần mềm độc hại (Malware Analysis) theo phương pháp Động (Dynamic Analysis) khác với phương pháp Tĩnh (Static Analysis) như thế nào?
A. Phân tích động là chỉ dịch ngược mã lệnh Assembly ra mã nguồn mà không chạy chương trình (Static Analysis)
B. Phân tích động (Dynamic Analysis) là quá trình THỰC SỰ CHẠY (Execute) đoạn mã độc đó bên trong một môi trường cô lập, bị giám sát nghiêm ngặt (như Sandbox) để ghi nhận những hành vi thực tế của nó (ví dụ: tạo file mới, sửa registry, gọi API hệ thống, kết nối ra mạng C&C)
C. Phân tích động là quét file bằng 10 trình diệt virus khác nhau
D. Phân tích tĩnh dùng trên Linux, động dùng trên Windows
*Đáp án: B*
*Giải thích: Mã độc hiện đại thường được đóng gói (Packer) và làm rối mã (Obfuscation), khiến việc đọc mã tĩnh rất khó khăn. Nhưng khi được kích hoạt chạy, nó phải giải nén chính nó ra RAM và bộc lộ hành vi thực sự, đây là cơ sở của phân tích động (Behavioral Analysis).*

**Câu 138:** Tường lửa Ứng dụng Web (WAF - Web Application Firewall) có chức năng bảo vệ chuyên sâu ở đặc điểm nào mà Tường lửa mạng (Network Firewall) truyền thống không làm được?
A. Chặn đứng giao thức ICMP Ping
B. Hiểu và phân tích cấu trúc sâu bên trong các giao thức Layer 7 (như HTTP/HTTPS), có thể nhận diện và lọc bỏ các mẫu câu lệnh tấn công đặc thù của Web (như SQL Injection, XSS, Cookie Poisoning) thay vì chỉ nhìn vào IP và Port 80/443
C. Đổi IP tĩnh thành IP động
D. Giới hạn số lượng kết nối tối đa mỗi giây cho Port 21
*Đáp án: B*
*Giải thích: Tường lửa mạng (Layer 3/4) cho phép mọi thứ chạy qua Port 80/443 đi vào Web Server. Tuy nhiên, lưu lượng HTTP đó có thể chứa câu lệnh `DROP TABLE users;` của SQLi. Chỉ có WAF mới phân tích sâu (Deep Packet Inspection) ngữ cảnh nội dung trang web để bắt chữ.*

**Câu 139:** Tấn công "Session Hijacking" (Cướp phiên làm việc) là tình trạng kẻ tấn công đánh cắp được thông tin nhạy cảm nào để mạo danh người dùng truy cập ứng dụng?
A. Lấy cắp được địa chỉ MAC của nạn nhân
B. Lấy cắp được mật khẩu đăng nhập của quản trị viên
C. Đánh cắp được Chuỗi định danh Phiên làm việc (Session ID / Session Token) hoặc Cookie hợp lệ (đang còn hiệu lực) của người dùng đã đăng nhập thành công. Từ đó kẻ tấn công "ốp" chuỗi ID này vào trình duyệt của mình và đi thẳng vào tài khoản mà KHÔNG CẦN biết mật khẩu
D. Đổi được mã PIN OTP từ tin nhắn điện thoại
*Đáp án: C*
*Giải thích: Việc đăng nhập giống như xuất trình giấy tờ ở quầy lễ tân để lấy "thẻ khách" (Session Cookie). Mọi tương tác sau đó với các tầng, hệ thống web chỉ xem xét thẻ này. Session Hijacking (qua nghe lén trên Wi-Fi hở hoặc lỗi XSS) là hành vi trộm cắp chiếc thẻ từ đang đeo trên cổ khách.*

**Câu 140:** Giao thức nào cung cấp cơ chế bảo vệ phân giải tên miền (DNS) bằng cách thêm vào thông tin xác thực Nguồn gốc và Tính toàn vẹn bằng Chữ ký Số (Digital Signatures), chống lại vấn nạn DNS Spoofing / Cache Poisoning?
A. DNSCrypt
B. HTTPS
C. DNSSEC (Domain Name System Security Extensions)
D. IPsec
*Đáp án: C*
*Giải thích: DNS ban đầu được thiết kế hoàn toàn không có bảo mật (gửi plain text và không có chứng thực người gửi trả lời). DNSSEC thêm các bản ghi RRSIG (Resource Record Signature) mã hóa bằng khóa bảo mật, cho phép trình duyệt xác minh chắc chắn 100% IP trả về là của máy chủ chứa tên miền xịn (như google.com) chứ không phải do hacker giả dạng.*

**Câu 141:** Cấu hình "DMZ" (Demilitarized Zone - Vùng phi quân sự) trong thiết kế kiến trúc mạng doanh nghiệp nhằm mục đích gì?
A. Chứa tất cả các máy tính của nhân viên kế toán
B. Tạo một mạng con riêng biệt (được kiểm soát bởi Firewall), dùng để phơi bày (expose) các máy chủ cung cấp dịch vụ công cộng trực tiếp cho Internet bên ngoài (như Web Server, Email Server, DNS Server). Tuy nhiên, các máy chủ DMZ này BỊ CẤM hoặc bị hạn chế rất khắt khe việc truy cập NGƯỢC VÀO mạng nội bộ an toàn (Intranet)
C. Để nâng cao tốc độ tải của máy chủ ảo hóa
D. Dành riêng cho thiết bị Internet vạn vật (IoT) trong nhà
*Đáp án: B*
*Giải thích: Bất kỳ Server nào mở port ra Internet đều có nguy cơ bị hacker xâm nhập và chiếm quyền điều khiển. Thiết kế DMZ cô lập các máy chủ rủi ro cao này ở một mạng đệm riêng. Nếu hacker hạ được máy Web Server, tường lửa phía sau vẫn chặn đứng không cho chúng lan truyền (lateral movement) vào máy chứa Database nội bộ.*

**Câu 142:** Trong An toàn thông tin, Nguyên tắc "Least Privilege" (Đặc quyền tối thiểu) mang ý nghĩa gì?
A. Mọi nhân viên phải được cấp quyền xem dữ liệu của đồng nghiệp
B. Mỗi tài khoản người dùng, chương trình phần mềm, hệ thống hay tiến trình CHỈ ĐƯỢC CẤP QUYỀN TRUY CẬP (như Đọc, Ghi, Thực thi) vào những tài nguyên thiết yếu NHẤT, VỪA ĐỦ ĐỂ HOÀN THÀNH nhiệm vụ cụ thể của nó và hoàn toàn không thể truy cập các quyền thừa mứa khác
C. Tối thiểu phải có ba người giám sát một hệ thống
D. Đặc quyền cao nhất luôn ưu tiên cho quản trị hệ thống root
*Đáp án: B*
*Giải thích: Nguyên lý thiết kế bảo mật kinh điển. Ví dụ, một nhân viên chăm sóc khách hàng chỉ có quyền (Role) đọc thông tin đơn hàng, chứ không có quyền xóa hay chỉnh sửa (Update/Delete) đơn hàng. Nếu tài khoản nhân viên này bị lộ, hacker cũng bị giới hạn quyền phá hoại hệ thống xuống mức thấp nhất.*

**Câu 143:** Mã độc "Rootkit" sử dụng thủ đoạn nào để che giấu triệt để sự hiện diện của nó khỏi các phần mềm Antivirus và Quản trị viên hệ thống?
A. Xóa luôn phần mềm diệt virus khỏi máy tính
B. Chiếm quyền điều khiển và thay đổi (hooking) ở các tầng cực sâu của hệ thống, thường là nhân hệ điều hành (Kernel-mode), để trực tiếp "bóp méo" thông tin trả về của hệ thống (ví dụ: khi Antivirus yêu cầu HĐH liệt kê danh sách các tiến trình (processes) đang chạy, Rootkit sẽ lọc và giấu tên tiến trình mã độc của nó)
C. Nén dữ liệu mã độc bằng định dạng .rar có pass
D. Chạy từ đĩa mềm không có mã hệ điều hành
*Đáp án: B*
*Giải thích: Chữ "Root" nghĩa là quyền cao nhất. Một chương trình diệt virus (hoạt động ở User-mode hoặc bị lừa ở Kernel) phải dựa vào hàm API của Windows để truy quét. Nếu Rootkit đã sửa đổi nhân của hàm API đó, thì Virus Scanner giống như đang bị mù màu, không thể thấy được cái không được hệ thống báo cáo.*

**Câu 144:** Cuộc tấn công "Dictionary Attack" (Tấn công tự điển) để phá vỡ mật khẩu khác biệt với "Brute-force Attack" (Tấn công vét cạn) ở điểm nào?
A. Vét cạn chỉ nhắm vào mã hóa WEP
B. Tấn công tự điển sử dụng một danh sách có sẵn (Wordlist) chứa hàng triệu từ vựng phổ biến, mật khẩu từng bị rò rỉ (như "123456", "password", "iloveyou") để thử, trong khi Vét cạn thử MỌI TỔ HỢP KÝ TỰ có thể xảy ra một cách mù quáng (ví dụ a, b, c... aaaaa, aaaab...)
C. Tấn công tự điển tốn nhiều CPU hơn vét cạn
D. Tự điển phải dùng AI để đoán
*Đáp án: B*
*Giải thích: Do người dùng có thói quen đặt mật khẩu rất dễ nhớ và có nghĩa, Dictionary Attack thường bẻ khóa thành công tới 70-80% tài khoản trong một tổ chức một cách nhanh chóng. Brute-force có thể mất tới hàng tỷ năm để thử nghiệm.*

**Câu 145:** Tính năng "Data Execution Prevention" (DEP) kết hợp với "ASLR" (Address Space Layout Randomization) trong các hệ điều hành hiện đại (Windows/Linux) nhằm mục đích chống lại loại tấn công nào?
A. Tấn công SQL Injection
B. Tấn công giả mạo MAC Address
C. Ngăn chặn các cuộc tấn công khai thác lỗ hổng bộ nhớ (Memory Corruption Exploits) như Tràn bộ đệm (Buffer Overflow) thực thi đoạn shellcode độc hại
D. Chống lại cuộc tấn công nghe lén không dây
*Đáp án: C*
*Giải thích: DEP ngăn không cho mã lệnh thực thi (chạy) trên các vùng nhớ vốn chỉ dành để chứa Dữ liệu (vùng Stack/Heap). ASLR trộn tung ngẫu nhiên cấu trúc địa chỉ nhớ của các file DLL/hệ thống mỗi lần khởi động, khiến hacker không thể biết trước mã lệnh hệ thống độc hại nằm ở "địa chỉ bộ nhớ" nào để thực hiện lệnh "JUMP" tới.*

**Câu 146:** Phương thức "Social Engineering" thường kết hợp tạo ra một bối cảnh gây áp lực lớn (như giả danh công an báo có lệnh bắt, sếp báo khẩn cấp cần chuyển tiền) nhằm tác động vào bản năng sinh học nào của con người?
A. Trí tuệ sáng tạo
B. Lợi dụng lòng tham, sự sợ hãi, khẩn cấp (Urgency) hoặc uy quyền (Authority) để thao túng nạn nhân bỏ qua hoàn toàn các bước suy nghĩ lý trí và kiểm tra bảo mật tiêu chuẩn, vội vã đưa ra thông tin nhạy cảm
C. Khả năng ghi nhớ siêu tốc
D. Khả năng nhận diện khuôn mặt
*Đáp án: B*
*Giải thích: Hacking con người luôn dễ hơn hacking một bức tường lửa. Các hacker tạo ra "ngụy biện xã hội" và kịch bản (Pretexting) rất tinh vi, thao túng tâm lý nạn nhân tiết lộ mật khẩu OTP mà không hệ thống công nghệ nào ngăn chặn nổi.*

**Câu 147:** Lỗ hổng bảo mật "CSRF" (Cross-Site Request Forgery - Giả mạo yêu cầu qua trang web chéo) hoạt động bằng cách nào?
A. Ăn cắp tài khoản ngân hàng bằng mã độc cài vào bàn phím (Hardware Keylogger)
B. Bẻ khóa mật khẩu MD5 bằng máy đào coin
C. Lừa một người dùng (đã đăng nhập sẵn và có Session hợp lệ ở trang Ngân hàng A) truy cập vào một trang web độc hại của Hacker. Trang web độc hại đó sẽ ngầm chứa mã lệnh (ví dụ chèn vào 1 thẻ `<img>` ẩn) để âm thầm gửi một yêu cầu (Request) giả mạo tới Ngân hàng A (như chuyển tiền sang ví hacker). Ngân hàng A thấy request mang Cookie hợp lệ của nạn nhân nên đồng ý thực hiện giao dịch
D. Hacker giả lập làm máy chủ Web
*Đáp án: C*
*Giải thích: Cốt lõi của CSRF là Trình duyệt (Browser) có cơ chế "tự động đính kèm Cookie" đối với các request bay đến tên miền đích (Ngân hàng A), dù request đó được kích hoạt từ một tab khác (Trang web Hacker). Khác với XSS, Hacker không cần (và không thể) lấy cắp được Session ID, chúng chỉ MƯỢN quyền ưu tiên của bạn đang có để ra lệnh bậy bạ.*

**Câu 148:** Giải pháp phòng thủ phổ biến nhất đối với lỗ hổng CSRF trên các ứng dụng Web hiện nay là gì?
A. Thay thế toàn bộ mã nguồn PHP bằng Python
B. Tắt JavaScript trong trình duyệt
C. Sử dụng cơ chế "Anti-CSRF Token" (Một chuỗi mã token ngẫu nhiên, bí mật, chỉ dùng 1 lần, được máy chủ Web sinh ra và nhúng ẩn (hidden field) vào các biểu mẫu Form HTML/API request. Nếu hacker gửi lệnh từ web khác, họ không thể đoán được Token này nên máy chủ từ chối lệnh)
D. Xác thực vân tay
*Đáp án: C*
*Giải thích: Máy chủ xác minh ngoài việc kiểm tra Cookie (chứng minh bạn là bạn), nó kiểm tra thêm Token (chứng minh Request chuyển tiền này THỰC SỰ xuất phát từ chính cái nút bấm TRÊN MÀN HÌNH GIAO DIỆN HỢP PHÁP của ngân hàng chứ không phải bay từ web khác sang).*

**Câu 149:** Trong mô hình bảo mật thông tin (CIA Triad), thành phần thứ ba của bộ ba "Bảo mật (Confidentiality) - Toàn vẹn (Integrity) - ..." là gì?
A. Availability (Tính sẵn sàng / Khả dụng)
B. Accountability (Tính giải trình)
C. Authentication (Xác thực)
D. Authorization (Ủy quyền)
*Đáp án: A*
*Giải thích: CIA Triad là nền tảng của mọi tiêu chuẩn An toàn thông tin. Hệ thống an toàn nhất thế giới bằng cách rút dây cáp mạng ra khỏi ổ điện sẽ đạt được Confidentiality và Integrity tuyệt đối, nhưng lại đánh mất giá trị Availability (người dùng hợp pháp lúc cần vào thì không dùng được).*

**Câu 150:** Giao thức mạng "Kerberos" (Thần khuyển 3 đầu canh cổng địa ngục) chuyên được sử dụng trong mạng nội bộ doanh nghiệp (đặc biệt là Microsoft Active Directory) để thực hiện tác vụ bảo mật chính nào?
A. Mã hóa file ổ cứng (như BitLocker)
B. Lọc nội dung website nhân viên truy cập
C. Cung cấp cơ chế xác thực tập trung (Authentication) sử dụng hệ thống "Vé" (Tickets) và mã hóa đối xứng mạnh. Người dùng đăng nhập một lần (Single Sign-On - SSO) lấy Ticket-Granting Ticket (TGT), sau đó dùng TGT để lấy các vé chứng nhận danh tính đi mở các cánh cửa truy cập khác vào máy chủ Email, File Share mà không phải nhập lại mật khẩu và không bao giờ gửi mật khẩu qua mạng
D. Đồng bộ hóa thời gian các máy chủ (NTP)
*Đáp án: C*
*Giải thích: Kerberos được phát triển tại MIT, là trái tim của hệ thống phân quyền doanh nghiệp. Dựa vào mô hình Đối tượng thứ ba tin cậy (KDC), nó chứng minh người dùng chính chủ an toàn trên môi trường LAN rủi ro (mà mọi gói tin đều có thể bị xem lén).*

**Câu 151:** Kỹ thuật "Spear Phishing" (Lừa đảo bằng giáo) khác biệt như thế nào so với các chiến dịch Phishing thông thường?
A. Sử dụng phần mềm độc hại để gửi email
B. Là các cuộc tấn công lừa đảo có mục tiêu cụ thể, được cá nhân hóa cao độ. Kẻ tấn công đã thu thập thông tin về nạn nhân (tên, chức vụ, dự án đang làm) để thiết kế một email lừa đảo trông cực kỳ đáng tin cậy và có liên quan trực tiếp đến nạn nhân
C. Chỉ tấn công vào điện thoại di động
D. Gửi email hàng loạt đến hàng triệu địa chỉ cùng lúc
*Đáp án: B*
*Giải thích: Phishing thường thả lưới diện rộng, hi vọng có vài con cá cắn câu. Spear Phishing ngắm chuẩn xác vào một cá nhân (như CFO hoặc kế toán), email thường giả mạo từ sếp tổng yêu cầu chuyển khoản khẩn cấp, tỷ lệ thành công rất cao.*

**Câu 152:** "Whaling" (Săn cá voi) là một dạng cụ thể của Spear Phishing nhắm vào đối tượng nào?
A. Những người dùng không có kiến thức về IT
B. Nhân viên phòng IT
C. Các lãnh đạo cấp cao (C-level executives như CEO, CFO, Chủ tịch) của một tổ chức, những người có quyền quyết định tài chính và quyền truy cập vào thông tin tối mật
D. Hacker khác
*Đáp án: C*
*Giải thích: Khái niệm "Săn cá voi" ám chỉ việc giăng bẫy những nhân vật chóp bu. Những người này thường bận rộn và có quyền lực, nên nếu lừa được họ, hậu quả sẽ cực kỳ nghiêm trọng.*

**Câu 153:** Thuật ngữ "Vishing" là sự kết hợp của Voice và Phishing. Hành vi này được thực hiện qua kênh giao tiếp nào?
A. Email
B. Tin nhắn văn bản (SMS)
C. Cuộc gọi điện thoại (Voice Calls), thường sử dụng VoIP và giả mạo số điện thoại (Caller ID Spoofing) để đóng giả công an hoặc ngân hàng nhằm đe dọa nạn nhân
D. Mạng xã hội
*Đáp án: C*
*Giải thích: Kẻ lừa đảo gọi điện trực tiếp, dùng kỹ năng tâm lý (thường dọa dẫm nạn nhân dính líu đến ma túy, rửa tiền) để ép nạn nhân chuyển tiền hoặc cung cấp mã OTP.*

**Câu 154:** "Smishing" là hình thức lừa đảo qua phương tiện nào?
A. Smart TV
B. Tin nhắn văn bản (SMS / Text Messages), thường chứa đường link độc hại hoặc yêu cầu gọi lại số điện thoại lừa đảo
C. Mạng xã hội Snapchat
D. Diễn đàn ngầm
*Đáp án: B*
*Giải thích: Smishing (SMS Phishing) lợi dụng tâm lý người dùng thường tin tưởng tin nhắn SMS hơn email, và điện thoại màn hình nhỏ khiến việc kiểm tra URL giả mạo khó khăn hơn.*

**Câu 155:** Trong quá trình điều tra sự cố bảo mật mạng (Digital Forensics), "Chuỗi hành trình sản phẩm" (Chain of Custody) đóng vai trò gì?
A. Là quy trình mã hóa dữ liệu ổ cứng
B. Là tài liệu ghi chép lại toàn bộ quá trình thu thập, bảo quản, kiểm soát và phân tích các bằng chứng kỹ thuật số (như ổ cứng, log máy chủ) từ hiện trường cho đến tòa án, đảm bảo bằng chứng không bị thay đổi hoặc giả mạo
C. Là chuỗi các cuộc tấn công của hacker
D. Là vòng đời của một phần mềm mã độc
*Đáp án: B*
*Giải thích: Nếu không có Chain of Custody rõ ràng, luật sư của bị cáo có thể phản bác rằng bằng chứng đã bị công an hoặc bên thứ ba sửa đổi, khiến bằng chứng mất giá trị pháp lý trước tòa.*

**Câu 156:** Kỹ thuật nào được sử dụng để chứng minh một bản sao ổ cứng (Disk Image) dùng để điều tra pháp y kỹ thuật số giống hệt 100% với ổ cứng gốc của nghi phạm?
A. Chụp ảnh màn hình
B. Tính toán và so sánh giá trị băm (Cryptographic Hash - như MD5, SHA-256) của cả ổ cứng gốc và bản sao. Nếu hai giá trị băm khớp nhau tuyệt đối, chứng tỏ bản sao chưa bị thay đổi một bit nào
C. Sao chép thông thường bằng Ctrl+C và Ctrl+V
D. Sử dụng mã hóa RSA
*Đáp án: B*
*Giải thích: Các công cụ Forensic tạo bản sao bit-by-bit (như lệnh `dd` trong Linux) và tính mã băm. Đây là bằng chứng không thể chối cãi về tính nguyên vẹn của chứng cứ số.*

**Câu 157:** Lỗ hổng "Command Injection" (Tiêm lệnh hệ điều hành) cho phép kẻ tấn công làm gì?
A. Sửa đổi cấu trúc HTML của trang web
B. Lợi dụng các ứng dụng web thực thi lệnh hệ thống (ví dụ hàm `system()`, `exec()` trong PHP) mà không kiểm tra dữ liệu đầu vào, cho phép kẻ tấn công chèn thêm các lệnh hệ điều hành (Shell commands) tùy ý để chạy trên máy chủ
C. Lấy cắp mật khẩu từ trình duyệt
D. Tấn công từ chối dịch vụ vào DNS
*Đáp án: B*
*Giải thích: Ví dụ ứng dụng web có tính năng Ping IP do người dùng nhập. Hacker nhập `127.0.0.1; rm -rf /`. Nếu ứng dụng web gọi thẳng lệnh này xuống hệ điều hành (như Linux Shell), lệnh xóa toàn bộ ổ đĩa sẽ được thực thi.*

**Câu 158:** Khái niệm "Air Gap" (Khoảng trống không khí) trong kiến trúc mạng an toàn nhất có nghĩa là gì?
A. Đặt máy chủ trong phòng không có không khí (chân không) để làm mát
B. Hệ thống mạng (như máy tính điều khiển nhà máy điện hạt nhân) hoàn toàn bị cô lập vật lý, KHÔNG CÓ BẤT KỲ KẾT NỐI VẬT LÝ HAY KHÔNG DÂY nào với Internet hoặc các mạng không an toàn khác
C. Sử dụng sóng Wi-Fi thay vì cáp quang
D. Khoảng cách vật lý giữa 2 tường lửa
*Đáp án: B*
*Giải thích: Air Gap là biện pháp bảo mật cuối cùng. Ngay cả vậy, Air gap vẫn có thể bị phá vỡ thông qua con đường vật lý (như cắm USB chứa mã độc Stuxnet vào máy tính bên trong mạng Air gap).*

**Câu 159:** Stuxnet là một mã độc nổi tiếng trong lịch sử an ninh mạng vì lý do gì?
A. Nó là virus máy tính đầu tiên được tạo ra
B. Nó là mã độc đầu tiên được thiết kế để phá hoại vật lý các cơ sở hạ tầng công nghiệp (máy ly tâm làm giàu uranium của Iran), đánh dấu kỷ nguyên của chiến tranh mạng không gian ảo tác động ra thế giới thực
C. Nó đánh cắp số lượng thẻ tín dụng lớn nhất lịch sử
D. Nó là mã độc tống tiền đầu tiên
*Đáp án: B*
*Giải thích: Stuxnet cực kỳ tinh vi, nó sử dụng nhiều Zero-day, lây qua USB (vượt qua Air Gap), nhắm vào hệ thống SCADA của Siemens và điều khiển máy ly tâm quay quá tốc độ đến mức tự phá hủy, trong khi vẫn gửi báo cáo bình thường về màn hình của kỹ sư.*

**Câu 160:** Trong quản lý rủi ro an ninh thông tin, "Vulnerability" (Lỗ hổng) khác với "Threat" (Mối đe dọa) như thế nào?
A. Chúng là một
B. Lỗ hổng là một điểm yếu trong hệ thống (như lỗi phần mềm, quy trình kém), còn Mối đe dọa là tác nhân (như Hacker, Virus, Thiên tai) có khả năng khai thác lỗ hổng đó để gây hại
C. Lỗ hổng là do con người, Mối đe dọa là do máy móc
D. Lỗ hổng chỉ liên quan đến phần mềm, Mối đe dọa liên quan đến phần cứng
*Đáp án: B*
*Giải thích: Một ổ khóa hỏng là Lỗ hổng (Vulnerability). Một tên trộm đi ngang qua là Mối đe dọa (Threat). Nếu có ổ khóa hỏng mà không có trộm, hoặc có trộm nhưng ổ khóa tốt, rủi ro (Risk) sẽ thấp.*

**Câu 161:** "Phishing" và "Pharming" khác nhau chủ yếu ở điểm nào?
A. Phishing lừa đảo qua email, Pharming lừa đảo qua điện thoại
B. Phishing cố gắng lừa người dùng tự bấm vào một link giả. Còn Pharming độc hại hơn, nó đầu độc hệ thống DNS (DNS Spoofing) hoặc sửa file Hosts, khiến người dùng dù gõ ĐÚNG ĐỊA CHỈ TRANG WEB (ví dụ bank.com) vẫn bị điều hướng âm thầm đến máy chủ giả mạo của hacker
C. Pharming chỉ nhắm vào các trang trại nông nghiệp thông minh
D. Phishing dùng để cài mã độc, Pharming dùng để lấy mật khẩu
*Đáp án: B*
*Giải thích: Pharming nguy hiểm hơn rất nhiều vì người dùng không hề làm gì sai (họ không click link lạ, họ gõ đúng địa chỉ trang web quen thuộc), nhưng vẫn bị dẫn đến trang web giả mạo do hệ thống phân giải tên miền đã bị hắc.*

**Câu 162:** Chức năng "Data Loss Prevention" (DLP - Chống thất thoát dữ liệu) trong doanh nghiệp giám sát và ngăn chặn điều gì?
A. Ngăn chặn hacker xóa dữ liệu
B. Giám sát, phân tích nội dung dữ liệu (như số thẻ tín dụng, mã nguồn, tài liệu mật) đang được sử dụng (endpoint), lưu trữ (storage) hoặc truyền qua mạng (network), và tự động ngăn chặn hành vi gửi dữ liệu nhạy cảm đó ra ngoài (ví dụ copy ra USB, upload lên Dropbox cá nhân, gửi email ra ngoài)
C. Khôi phục dữ liệu từ các bản sao lưu
D. Ngăn chặn các cuộc tấn công DDoS
*Đáp án: B*
*Giải thích: DLP chống lại rủi ro từ "Người trong cuộc" (Insider Threat), dù là vô tình hay cố ý làm rò rỉ bí mật thương mại của công ty ra bên ngoài.*

**Câu 163:** Chuẩn bảo mật ISO/IEC 27001 chủ yếu tập trung vào việc gì?
A. Thiết lập cấu hình cho Router Cisco
B. Xây dựng một Hệ thống Quản lý An toàn Thông tin (ISMS - Information Security Management System) bài bản cho tổ chức, bao gồm chính sách, quy trình quản lý rủi ro và tuân thủ
C. Viết mã nguồn an toàn cho C++
D. Chuẩn hóa các thuật toán mã hóa
*Đáp án: B*
*Giải thích: ISO 27001 không nói bạn phải dùng phần mềm Firewall nào, mà nó đưa ra khung sườn (framework) về quy trình: Bạn phải kiểm kê tài sản ra sao, đánh giá rủi ro thế nào, và phải có chính sách an ninh gì để bảo vệ dữ liệu.*

**Câu 164:** Tấn công "Watering Hole" (Hố nước) là chiến thuật mà hacker thực hiện như thế nào?
A. Tấn công vào các nhà máy lọc nước
B. Thay vì tấn công trực tiếp vào công ty mục tiêu (rất khó vì bảo mật mạnh), hacker sẽ tìm hiểu xem nhân viên công ty đó hay truy cập vào các trang web nào (ví dụ diễn đàn ngành nghề, trang tin tức chuyên ngành). Sau đó hacker hack các trang web "hố nước" này và cài mã độc. Khi nhân viên mục tiêu truy cập, họ sẽ bị nhiễm mã độc
C. Tạo ra một mạng Wi-Fi công cộng giả mạo gần công ty mục tiêu
D. Làm ngập lụt hệ thống mạng bằng các gói tin ICMP
*Đáp án: B*
*Giải thích: Tên gọi lấy từ thế giới động vật: thú săn mồi không đuổi theo con mồi mà nằm chờ ở "Hố nước" - nơi con mồi chắc chắn sẽ đến uống nước. Đây là một dạng tấn công có chủ đích (APT) rất thâm hiểm.*

**Câu 165:** Khái niệm "Threat Intelligence" (Tình báo mối đe dọa) cung cấp cho các trung tâm giám sát an ninh (SOC) thông tin gì?
A. Mật khẩu của các hacker
B. Dữ liệu thời gian thực được phân tích chuyên sâu về các chiến dịch tấn công mới, các dấu hiệu xâm phạm (IoC - Indicators of Compromise như IP độc hại, mã băm malware, domain của botnet) giúp tổ chức chủ động phòng thủ trước khi bị tấn công
C. Tình báo về hoạt động kinh doanh của đối thủ
D. Thông tin về các bản vá lỗi phần mềm của Microsoft
*Đáp án: B*
*Giải thích: Threat Intelligence giúp chuyển đổi tư thế an ninh từ bị động (đợi bị đánh rồi mới báo động) sang chủ động (biết trước IP này là máy chủ C&C của mã độc mới, tự động đưa vào danh sách đen (Blacklist) của Firewall).*

**Câu 166:** Tấn công "Man-in-the-Browser" (MitB) là một dạng tấn công tinh vi nhắm vào dịch vụ ngân hàng trực tuyến, nó hoạt động như thế nào?
A. Sửa file hosts để đổi hướng tên miền ngân hàng
B. Mã độc (thường là tiện ích mở rộng hoặc Trojan) lây nhiễm trực tiếp vào Trình duyệt Web của nạn nhân. Nó có thể thay đổi nội dung trang web hiển thị TRƯỚC KHI trình duyệt mã hóa TLS gửi đi (ví dụ: nạn nhân chuyển 1 triệu cho mẹ, MitB đổi thành chuyển 10 triệu cho hacker ngay trên giao diện web, trong khi máy chủ ngân hàng vẫn nhận được lệnh hợp lệ qua TLS)
C. Cài đặt một trạm phát sóng Wi-Fi giả
D. Đánh cắp cơ sở dữ liệu của trình duyệt Firefox
*Đáp án: B*
*Giải thích: MitB nguy hiểm ở chỗ nó nằm giữa người dùng và cơ chế bảo mật TLS của trình duyệt. Nó có thể vượt qua cả OTP vì nạn nhân tự tay nhập OTP để xác thực cho một giao dịch mà họ bị MitB lừa hiển thị sai thông tin trên màn hình.*

**Câu 167:** Kỹ thuật "Fuzzing" (Kiểm thử mờ) trong kiểm thử bảo mật phần mềm (Penetration Testing) là làm gì?
A. Xóa mờ mã nguồn để bảo mật
B. Tự động bơm (inject) một lượng khổng lồ các dữ liệu ngẫu nhiên, dị dạng, hoặc bất hợp lệ (invalid/unexpected data) vào các ngõ vào (input) của chương trình phần mềm, nhằm mục đích làm chương trình bị treo (crash) hoặc rò rỉ bộ nhớ, từ đó phát hiện ra các lỗ hổng Zero-day
C. Quét các cổng mạng đang mở
D. Kiểm tra tính hợp lệ của mật khẩu
*Đáp án: B*
*Giải thích: Fuzzing là cách hiệu quả nhất để tìm ra lỗi Tràn bộ đệm (Buffer Overflow) hoặc lỗi xử lý ngoại lệ. Các Fuzzer sẽ gửi hàng triệu request rác vào phần mềm cho đến khi phần mềm báo lỗi.*

**Câu 168:** Tính năng "HSTS" (HTTP Strict Transport Security) giúp bảo vệ trang web khỏi loại tấn công nào?
A. Tấn công DDoS
B. Tấn công Man-in-the-Middle thông qua kỹ thuật "SSL Stripping" (Hạ cấp kết nối HTTPS xuống HTTP không mã hóa). HSTS ép buộc trình duyệt của người dùng LUÔN LUÔN kết nối bằng HTTPS, từ chối mọi nỗ lực kết nối bằng HTTP trần
C. Tấn công SQL Injection
D. Tấn công Brute-force mật khẩu
*Đáp án: B*
*Giải thích: Khi hacker đứng giữa mạng Wi-Fi quán cafe, họ có thể lừa trình duyệt nạn nhân giao tiếp bằng HTTP thay vì HTTPS (SSL Stripping). Nếu website có HSTS, trình duyệt sẽ biết trang web này bắt buộc phải dùng HTTPS, nếu kết nối không mã hóa, nó sẽ tự động chặn ngay lập tức.*

**Câu 169:** Phương pháp "Risk Acceptance" (Chấp nhận rủi ro) trong quản lý an ninh thông tin được sử dụng khi nào?
A. Khi tổ chức không có tiền để mua phần mềm diệt virus
B. Khi rủi ro quá lớn và chắc chắn xảy ra
C. Khi chi phí (tiền bạc, thời gian) để triển khai các biện pháp khắc phục/bảo vệ lớn hơn rất nhiều so với giá trị thiệt hại nếu rủi ro đó thực sự xảy ra
D. Khi không biết rủi ro đó là gì
*Đáp án: C*
*Giải thích: Không có hệ thống nào an toàn 100%. Nếu một rủi ro (như server sập 5 phút) chỉ gây thiệt hại 1 triệu đồng, nhưng để thiết lập hệ thống chống sập tiêu tốn 100 triệu đồng, thì quyết định kinh doanh hợp lý nhất là "Chấp nhận" rủi ro đó.*

**Câu 170:** Kỹ thuật "Pass-the-Hash" (Chuyền mã băm) là một thủ đoạn xâm nhập phổ biến trong môi trường mạng Windows (Active Directory). Nó hoạt động ra sao?
A. Hacker bẻ khóa mã băm thành mật khẩu bản rõ rồi mới đăng nhập
B. Hacker lấy cắp được hàm băm (Hash) mật khẩu NTLM/LanMan của người dùng (từ bộ nhớ máy tính bị nhiễm) và SỬ DỤNG TRỰC TIẾP mã băm đó để xác thực với các máy chủ khác trong mạng mà KHÔNG CẦN phải tốn công bẻ khóa (crack) mã băm đó ra mật khẩu gốc
C. Hacker tạo ra mật khẩu mới và băm nó
D. Hacker truyền mã độc qua các thiết bị lưu trữ USB
*Đáp án: B*
*Giải thích: Trong giao thức xác thực NTLM của Windows, máy chủ chỉ cần nhận đúng mã Hash là cấp quyền đăng nhập. Kẻ tấn công không cần biết mật khẩu thật của bạn là "IloveYou123", chúng chỉ cần quẳng cái chuỗi băm (Hash) trộm được cho Server là có thể đăng nhập thành công. Đây là kỹ thuật leo thang đặc quyền cực kỳ nguy hiểm.*

**Câu 171:** Lỗ hổng "Rogue DHCP Server" (Máy chủ DHCP giả mạo) trong mạng nội bộ gây ra hậu quả gì?
A. Tăng băng thông mạng lên mức quá tải
B. Máy chủ giả mạo cấp phát địa chỉ IP cho các máy trạm mới kết nối, kèm theo đó là cấp địa chỉ IP của Default Gateway hoặc DNS Server là MÁY CỦA KẺ TẤN CÔNG. Từ đó, toàn bộ lưu lượng của nạn nhân bị định tuyến qua máy hacker (Tấn công Man-in-the-Middle)
C. Làm hỏng phần cứng của Router chính
D. Thay đổi địa chỉ MAC của máy trạm
*Đáp án: B*
*Giải thích: Khi máy tính cắm cáp mạng, nó gửi gói broadcast xin IP. Nếu Rogue DHCP Server phản hồi nhanh hơn DHCP Server thật, máy tính sẽ nhận cấu hình mạng "độc hại", giao nộp mọi dữ liệu mạng cho hacker.*

**Câu 172:** Cơ chế bảo vệ nào trên Switch (Layer 2) được sinh ra đặc biệt để ngăn chặn tấn công Rogue DHCP Server?
A. Spanning Tree Protocol (STP)
B. Port Security
C. DHCP Snooping
D. VLAN Trunking Protocol (VTP)
*Đáp án: C*
*Giải thích: DHCP Snooping quy định chỉ có các cổng mạng (ports) được quản trị viên thiết lập là "Trusted" (Tin cậy - nối với DHCP Server thật) mới được phép gửi các bản tin DHCP Reply. Nếu ai đó cắm Rogue DHCP vào cổng mạng nhân viên (Untrusted port), Switch sẽ tự động chặn đứng các gói tin cấp IP giả mạo.*

**Câu 173:** Loại mã độc nào được thiết kế đặc biệt để khai thác sức mạnh xử lý (CPU/GPU) của máy tính nạn nhân một cách âm thầm nhằm tạo ra tiền điện tử (Cryptocurrency) cho kẻ tấn công?
A. Ransomware
B. Cryptojacking (Malware đào tiền ảo)
C. Spyware
D. Adware
*Đáp án: B*
*Giải thích: Cryptojacking (hoặc Coinminer) không đánh cắp hay phá hoại dữ liệu, nó "đánh cắp" điện năng và làm máy tính của nạn nhân chậm đi trông thấy, quạt tản nhiệt quay liên tục do CPU phải giải các thuật toán đào coin (như Monero) 100% công suất.*

**Câu 174:** Trong đánh giá an ninh (Penetration Testing), "Red Team" (Đội đỏ) và "Blue Team" (Đội xanh) có vai trò đối lập nhau như thế nào?
A. Red Team là đội IT, Blue Team là đội nhân sự
B. Red Team đóng vai trò là những Kẻ Tấn Công (Offensive) chủ động tìm cách xâm nhập vào hệ thống bằng mọi kỹ thuật thực tế nhất, trong khi Blue Team đóng vai trò là những Người Phòng Thủ (Defensive) chịu trách nhiệm phát hiện, ngăn chặn và ứng phó với các đợt tấn công của Red Team
C. Red Team viết phần mềm, Blue Team kiểm thử phần mềm
D. Red Team bảo vệ máy chủ, Blue Team bảo vệ mạng lưới
*Đáp án: B*
*Giải thích: Mô hình tập trận Red Team/Blue Team (và Purple Team là sự kết hợp) giúp tổ chức đánh giá chính xác năng lực phòng thủ thực tế (không chỉ là máy móc mà còn là phản ứng của con người trong Đội Xanh) trước các cuộc tấn công tinh vi (APT).*

**Câu 175:** Cuộc tấn công "BGP Hijacking" (Cướp quyền định tuyến BGP) làm xáo trộn Internet toàn cầu bằng cách nào?
A. Làm đứt cáp quang dưới biển
B. Một nhà mạng (ISP) độc hại hoặc bị cấu hình sai, phát đi thông báo định tuyến BGP (BGP Route Announcement) khẳng định rằng HỌ là con đường ngắn nhất (hoặc là chủ sở hữu) để đi đến một dải IP cụ thể (ví dụ IP của Google). Kết quả là toàn bộ lưu lượng Internet gửi đến Google sẽ bị "lái" về máy chủ của ISP độc hại đó
C. Tấn công từ chối dịch vụ vào các máy chủ DNS Root
D. Thay đổi bảng định tuyến tĩnh trên các máy tính cá nhân
*Đáp án: B*
*Giải thích: Border Gateway Protocol (BGP) hoạt động dựa trên sự "tin tưởng mù quáng". Nếu một router BGP lớn nói "Tôi là đường đến YouTube", các router khác sẽ cập nhật bảng định tuyến theo. Nếu tin tặc cướp được BGP, chúng có thể tạo ra "Hố đen" (Blackhole) hút sạch lưu lượng Internet hoặc tiến hành nghe lén quy mô quốc gia.*

**Câu 176:** Thuật ngữ "Airgap" (Khoảng trống không khí) có thể bị vượt qua (Bypassed) bởi kỹ thuật tấn công vô cùng tinh vi nào sau đây?
A. Gửi email chứa mã độc
B. Sử dụng các kênh ẩn vật lý (Covert Physical Channels) như biến tần số nhấp nháy của đèn LED ổ cứng, sóng âm siêu âm phát ra từ loa/quạt tản nhiệt, hoặc bức xạ điện từ từ cáp màn hình máy tính để truyền tải dữ liệu bị đánh cắp ra thiết bị thu âm/thu sóng của hacker đặt gần đó
C. Chèn mã độc qua quảng cáo Google
D. Quét cổng qua mạng Internet
*Đáp án: B*
*Giải thích: Máy tính Air-gapped không cắm dây mạng, không có Wi-Fi. Các chuyên gia bảo mật và hacker cấp quốc gia (State-sponsored) đã nghiên cứu ra các cách truyền dữ liệu ra ngoài bằng cách thay đổi tốc độ quay của quạt làm mát CPU tạo ra âm thanh đặc biệt, hoặc bức xạ nhiệt, bắt bằng micro trên điện thoại bị nhiễm mã độc gần đó.*

**Câu 177:** Chữ ký số (Digital Signature) trong một tài liệu điện tử sử dụng kết hợp hai công nghệ mật mã nào?
A. Mã hóa đối xứng và mã hóa phi đối xứng
B. Hàm băm (Hash Function) và Mã hóa Khóa phi đối xứng (Public-Key Cryptography - Cụ thể là mã hóa băm bằng Khóa Private)
C. RSA và AES
D. WEP và WPA
*Đáp án: B*
*Giải thích: Người gửi dùng hàm Hash tính ra bản băm của văn bản (đảm bảo Toàn vẹn). Sau đó dùng Khóa Private (riêng tư) của mình để MÃ HÓA bản băm đó tạo thành Chữ ký số (đảm bảo Chống chối bỏ). Người nhận dùng Khóa Public để giải mã chữ ký số và so sánh bản băm.*

**Câu 178:** Chức năng chính của "MAC" (Message Authentication Code - Mã xác thực thông điệp) trong truyền thông an toàn là gì?
A. Mã hóa toàn bộ thông điệp
B. Xác thực địa chỉ MAC vật lý của card mạng
C. Đảm bảo Tính Toàn Vẹn (Integrity) và Xác thực Nguồn Gốc (Authenticity) của dữ liệu bằng cách sử dụng chung một Khóa Bí Mật (Shared Secret Key) giữa người gửi và người nhận để tạo ra một đoạn mã nhỏ đính kèm thông điệp (ví dụ HMAC)
D. Nén thông điệp
*Đáp án: C*
*Giải thích: MAC giống như Chữ ký số nhưng dùng Mã hóa Đối xứng (chia sẻ chung 1 khóa). Người nhận dùng chung khóa đó để tính toán lại MAC và so sánh. Vì cần Khóa bí mật chung nên MAC không có tính chống chối bỏ (Non-repudiation) tốt như Chữ ký số (dùng khóa Private riêng biệt).*

**Câu 179:** Lỗ hổng "Typosquatting" (Kỹ thuật "Ngồi xổm" tên miền sai chính tả) là một biến thể của Phishing, kẻ tấn công thực hiện thủ đoạn nào?
A. Tấn công làm thay đổi nội dung trang web chính hãng
B. Đăng ký các tên miền gần giống hệt với các trang web nổi tiếng (ví dụ `goggle.com` hoặc `faceb00k.com`), tạo giao diện giống hệt bản gốc, để phục kích những người dùng gõ sai chính tả trên thanh trình duyệt, từ đó dụ họ nhập mật khẩu hoặc tải mã độc
C. Hack máy chủ DNS để trỏ sai tên miền
D. Thay đổi giao diện màn hình máy tính
*Đáp án: B*
*Giải thích: Đây là một dạng kỹ nghệ xã hội rất phổ biến. Người dùng do vội vàng hoặc bất cẩn gõ sai tên miền, và thay vì nhận được lỗi 404, họ vào ngay một trang web giả mạo do hacker lập ra sẵn.*

**Câu 180:** "Cơ chế cách ly vi mô" (Microsegmentation) trong các trung tâm dữ liệu hiện đại (Đám mây / SDN) nhằm mục đích bảo mật gì?
A. Tăng tốc độ đường truyền quang
B. Thay vì chỉ có một bức tường lửa lớn bảo vệ vòng ngoài (Perimeter), Microsegmentation tạo ra các phân vùng mạng hoặc tường lửa cực nhỏ bảo vệ TỪNG MÁY CHỦ ẢO (VM) hoặc TỪNG ỨNG DỤNG (Workload) riêng lẻ. Giúp ngăn chặn sự lây lan mã độc (Lateral Movement) nếu một máy chủ nội bộ bị xâm nhập
C. Thu nhỏ phần cứng máy chủ
D. Chia nhỏ file log để lưu trữ
*Đáp án: B*
*Giải thích: Trong mô hình bảo mật truyền thống (Mô hình quả trứng: vỏ cứng, lòng đỏ mềm), nếu hacker chọc thủng tường lửa ngoài cùng, chúng có thể tự do tấn công các máy tính bên trong. Microsegmentation (Zero Trust Network) coi mọi máy tính bên trong đều không an toàn và phải tự thiết lập ranh giới bảo vệ riêng.*

**Câu 181:** Kỹ thuật "VLAN Hopping" (Nhảy VLAN) khai thác điểm yếu nào trong thiết lập mạng của Switch (Switching)?
A. Cổng mạng bị hở mạch
B. Tấn công vào các cổng Trunk (Trunk Ports) hoặc sử dụng kỹ thuật "Double Tagging" (Gắn thẻ VLAN kép) để đẩy gói tin ra khỏi VLAN hiện tại (ví dụ VLAN của khách) và nhảy sang một VLAN khác (ví dụ VLAN quản trị) mà không cần đi qua thiết bị định tuyến (Router/Firewall)
C. Chiếm quyền điều khiển bảng định tuyến OSPF
D. Làm tràn bộ nhớ ARP của Switch
*Đáp án: B*
*Giải thích: Lỗ hổng này thường xảy ra do quản trị viên cấu hình cổng kết nối với máy trạm là "Dynamic Desirable" hoặc "Trunk", cho phép hacker gửi gói tin giả mạo chuẩn 802.1Q chứa 2 lớp thẻ VLAN. Switch lớp ngoài sẽ lột thẻ thứ nhất và đẩy nó vào mạng, Switch thứ hai sẽ thấy thẻ thứ hai và đẩy nó vào VLAN đích trái phép.*

**Câu 182:** Để phòng ngừa sự cố mất mát dữ liệu do thiên tai, tấn công mã độc Ransomware tàn phá hệ thống chính, chiến lược nào là quan trọng và hiệu quả nhất trong An toàn thông tin?
A. Cài đặt nhiều phần mềm diệt virus
B. Thiết lập Tường lửa phần cứng đắt tiền
C. Chiến lược Sao lưu dữ liệu (Backup) theo quy tắc 3-2-1 (3 bản sao, trên 2 phương tiện khác nhau, có 1 bản lưu trữ ở địa điểm khác (Off-site) và tốt nhất là bất biến (Immutable) hoặc tách rời ngoại tuyến (Offline/Air-gapped))
D. Tăng số lượng nhân viên bảo vệ máy chủ
*Đáp án: C*
*Giải thích: Nếu Ransomware mã hóa luôn cả dữ liệu trên ổ đĩa Backup gắn trực tiếp trên máy chủ, công ty sẽ mất tất cả. Nguyên tắc 3-2-1 với ít nhất một bản backup được cách ly hoàn toàn (offline) là "liều thuốc giải" cuối cùng cho Ransomware.*

**Câu 183:** Mã độc "Polymorphic Malware" (Mã độc đa hình) gây khó khăn cho phần mềm diệt virus truyền thống bằng cách nào?
A. Nó tự động tải về nhiều loại virus khác nhau
B. Nó liên tục thay đổi đoạn mã của chính mình (nhưng giữ nguyên chức năng phá hoại) mỗi lần lây nhiễm sang file mới bằng cách sử dụng các thuật toán mã hóa khác nhau hoặc sắp xếp lại mã lệnh. Việc này làm thay đổi cấu trúc tệp tin (và giá trị Hash), khiến công nghệ quét bằng "chữ ký" (Signature-based) của Antivirus trở nên vô dụng
C. Nó giả dạng thành tập tin Word
D. Nó chạy trong bộ nhớ RAM
*Đáp án: B*
*Giải thích: Mã độc đa hình giống như một con virus cúm liên tục biến chủng. Để phát hiện chúng, các phần mềm diệt virus hiện đại phải dùng đến Heuristics (Phân tích suy cấu) hoặc Behavioral Analysis (Phân tích hành vi), chứ không thể dựa vào nhận diện hình dáng (signature).*

**Câu 184:** Phương pháp mã hóa E2EE (End-to-End Encryption - Mã hóa đầu cuối) trong các ứng dụng nhắn tin (như WhatsApp, Signal) đảm bảo tính riêng tư như thế nào?
A. Chỉ mã hóa dữ liệu từ người dùng đến máy chủ của công ty
B. Mã hóa dữ liệu ngay trên thiết bị của người gửi và chỉ được giải mã trên thiết bị của người nhận đích. Ngay cả máy chủ trung gian chuyển tiếp tin nhắn (hoặc nhà mạng, công ty cung cấp ứng dụng) cũng CHỈ THẤY BẢN MÃ và không có chìa khóa để đọc được nội dung tin nhắn
C. Mã hóa toàn bộ kết nối Internet
D. Yêu cầu nhập mật khẩu mỗi lần đọc tin nhắn
*Đáp án: B*
*Giải thích: E2EE đảm bảo rằng "Chìa khóa riêng tư" (Private Key) được tạo ra và nằm chết trên điện thoại của hai bên nhắn tin. Máy chủ (Server) chỉ đóng vai trò là bưu điện chuyển phát các gói hàng đã bị khóa kín.*

**Câu 185:** Lỗ hổng "Logic Bomb" (Bom logic) trong phát triển phần mềm là gì?
A. Một đoạn mã làm sập hệ thống ngay lập tức khi chạy
B. Một đoạn mã độc hại được chèn (thường bởi người trong cuộc/nhân viên lập trình) nằm im lìm trong phần mềm hợp pháp. Nó sẽ chỉ được "Kích nổ" (thực thi phá hoại, xóa dữ liệu) khi một ĐIỀU KIỆN LÝ THUYẾT (Logic condition) nhất định được thỏa mãn (ví dụ: đến một ngày giờ cụ thể, hoặc khi tên của nhân viên đó bị xóa khỏi cơ sở dữ liệu nhân sự)
C. Tấn công phá vỡ cấu trúc cơ sở dữ liệu
D. Phần mềm tự động tải quảng cáo
*Đáp án: B*
*Giải thích: Khác với virus lây lan tự động, Logic Bomb thường là đòn trả thù của những nhân viên IT hoặc lập trình viên khi bị đuổi việc. Họ chèn đoạn code: `If (User == 'John' is False) then Delete_All_Database()`.*

**Câu 186:** Nguyên tắc "Defense in Depth" (Phòng thủ chiều sâu / Phòng thủ nhiều lớp) trong an ninh mạng khuyên các tổ chức nên làm gì?
A. Chỉ đầu tư vào loại Firewall mạnh nhất và đắt tiền nhất
B. Sử dụng nhiều cơ chế/lớp bảo vệ khác nhau (như Firewall, IPS, Antivirus, Phân quyền, Mã hóa, Đào tạo nhân viên) xếp chồng lên nhau. Nếu kẻ tấn công xuyên thủng một lớp (ví dụ vượt qua Firewall), thì vẫn còn các lớp khác (như xác thực MFA, mã hóa ổ cứng) cản trở hoặc ngăn chặn chúng
C. Giấu hệ thống mạng sâu dưới lòng đất
D. Liên tục thay đổi địa chỉ IP của máy chủ
*Đáp án: B*
*Giải thích: Tương tự như lâu đài thời trung cổ có hào nước, tường thành cao, rồi đến lính canh, cửa sắt. Phòng thủ nhiều lớp loại bỏ nguy cơ phụ thuộc vào một Điểm yếu đơn lẻ (Single Point of Failure).*

**Câu 187:** Trong kỹ thuật mật mã, tính "Forward Secrecy" (Bảo mật chuyển tiếp) mang ý nghĩa gì quan trọng đối với giao thức bảo mật như TLS?
A. Đảm bảo dữ liệu gửi đi nhanh hơn
B. Khóa phiên (Session Key) được dùng để mã hóa dữ liệu chỉ tồn tại ngắn hạn và KHÔNG THỂ BỊ DẪN XUẤT NGƯỢC LẠI kể cả khi kẻ tấn công đánh cắp được Khóa riêng (Private Key) dài hạn của máy chủ trong tương lai. Nhờ đó, các đoạn chat/giao dịch trong quá khứ đã thu thập bị mã hóa vẫn an toàn tuyệt đối
C. Có thể mã hóa được các gói tin lỗi
D. Mã hóa tương thích với các thuật toán mới
*Đáp án: B*
*Giải thích: Nếu không có Forward Secrecy, hacker có thể kiên nhẫn ghi lại (sniff) toàn bộ lưu lượng web (bị mã hóa) của ngân hàng trong 1 năm. Đến cuối năm, hacker bằng cách nào đó ăn cắp được Private Key của máy chủ ngân hàng, chúng có thể đem chìa khóa đó giải mã lại toàn bộ dữ liệu 1 năm qua. Với thuật toán (như ECDHE) hỗ trợ Forward Secrecy, Khóa phiên bị vứt bỏ sau mỗi kết nối, Private Key có lộ cũng vô dụng với dữ liệu cũ.*

**Câu 188:** Giao thức mạng "SNMPv3" cải thiện lỗ hổng chết người nào của các phiên bản SNMPv1 và SNMPv2c cũ trong việc quản lý thiết bị mạng (Router/Switch)?
A. Bổ sung thêm tính năng kiểm tra lỗi phần cứng
B. SNMPv1/v2c gửi chuỗi xác thực "Community String" (như mật khẩu quản trị) ở dạng bản rõ (plaintext) không mã hóa, dễ bị nghe lén. SNMPv3 bổ sung khả năng Mã hóa dữ liệu, Xác thực mạnh và Kiểm soát quyền truy cập chi tiết
C. Hỗ trợ địa chỉ IPv6
D. Tăng tốc độ truyền tải thông số cấu hình
*Đáp án: B*
*Giải thích: Mọi lệnh quản trị từ xa cấu hình cho Router của mạng dùng SNMPv1/2 đều có thể bị hacker "đứng giữa" mạng LAN tóm được bằng Wireshark và đọc được mật khẩu (Community String) quản trị mạng.*

**Câu 189:** Hành động "Dumpster Diving" (Lục thùng rác) trong kỹ nghệ xã hội (Social Engineering) là gì?
A. Hacker vào thùng rác Recycle Bin của máy tính để tìm file đã xóa
B. Hacker hoặc gián điệp thực sự bới móc thùng rác vật lý của công ty/cá nhân để tìm kiếm các tài liệu, biên lai, bản nháp mật khẩu, sơ đồ mạng hoặc giấy tờ chứa thông tin nhạy cảm đã bị vứt bỏ mà không qua máy hủy giấy (Shredder)
C. Phục hồi dữ liệu từ ổ cứng hỏng
D. Dọn dẹp bộ nhớ đệm (Cache) của trình duyệt web
*Đáp án: B*
*Giải thích: Một tờ giấy note ghi pass Wi-Fi hoặc một hóa đơn đối tác vứt thùng rác có thể cung cấp đủ thông tin (pretext) để hacker thực hiện một cuộc gọi điện thoại lừa đảo (Vishing) hoàn hảo.*

**Câu 190:** Để giảm thiểu rủi ro từ lỗ hổng "Zero-day", biện pháp phòng vệ (Mitigation) nào thường được các chuyên gia an ninh khuyến nghị triển khai dù chưa có bản vá lỗi (Patch)?
A. Đợi nhà sản xuất phát hành bản vá rồi mới làm việc tiếp
B. Tắt hoàn toàn hệ thống mạng
C. Áp dụng "Virtual Patching" (Vá ảo) bằng cách cập nhật luật (Rules) cho Tường lửa Ứng dụng Web (WAF) hoặc Hệ thống Ngăn chặn Xâm nhập (IPS) để chặn đứng dấu hiệu (Signature) hoặc hành vi khai thác lỗ hổng đó ngay trên đường truyền mạng, bảo vệ ứng dụng bị lỗi ở phía sau
D. Đổi mật khẩu tất cả người dùng
*Đáp án: C*
*Giải thích: Vá ảo (Virtual Patching) là cách thức mua thêm thời gian quý giá cho đội ngũ IT (có thể mất vài tuần để test và cài đặt bản vá phần mềm chính thức) mà vẫn đảm bảo hệ thống không bị khai thác.*

**Câu 191:** Mối đe dọa "Insider Threat" (Mối đe dọa từ người trong cuộc) đặc biệt khó phát hiện và phòng chống vì lý do nào?
A. Vì họ sử dụng các công cụ hack siêu việt
B. Vì người trong cuộc (Nhân viên, Đối tác, Nhà thầu) ĐÃ ĐƯỢC CẤP SẴN QUYỀN TRUY CẬP HỢP PHÁP (tài khoản, thẻ từ, mật khẩu) và vượt qua các bức tường lửa bên ngoài, họ có thể lạm dụng quyền hạn này để đánh cắp hoặc phá hoại dữ liệu một cách dễ dàng
C. Vì phần mềm Antivirus không quét máy của nhân viên
D. Vì họ luôn làm việc ẩn danh
*Đáp án: B*
*Giải thích: Kẻ cướp ở bên ngoài thì khó vào, nhưng nếu bảo vệ hoặc thủ quỹ của ngân hàng là kẻ cướp (đã có sẵn chìa khóa) thì việc phá hoại hệ thống an ninh từ bên trong là vô cùng dễ dàng và khó bị nghi ngờ.*

**Câu 192:** Kỹ thuật "Rate Limiting" (Giới hạn tỷ lệ/tần suất) trên các API và Web Server là phương pháp chủ đạo để phòng thủ các cuộc tấn công nào sau đây?
A. Phishing (Lừa đảo)
B. Brute-force/Credential Stuffing (Dò mật khẩu liên tục) và Tấn công từ chối dịch vụ (DDoS) lớp ứng dụng bằng cách làm chậm hoặc khóa tạm thời các IP gửi quá nhiều Request trong một khoảng thời gian ngắn
C. Tấn công SQL Injection
D. Mã độc tống tiền Ransomware
*Đáp án: B*
*Giải thích: Nếu một kẻ tấn công cố gắng nhập thử 10.000 mật khẩu khác nhau trong 1 phút, việc áp dụng Rate Limiting (ví dụ chỉ cho phép sai pass 5 lần/phút) sẽ làm chậm quá trình dò pass của chúng xuống đến mức vô dụng (hoặc khóa luôn tài khoản/IP đó).*

**Câu 193:** Chuẩn "OWASP Top 10" là tài liệu vô cùng nổi tiếng và quan trọng trong lĩnh vực nào của an toàn thông tin?
A. Cấu hình bảo mật mạng không dây
B. Danh sách 10 rủi ro bảo mật nghiêm trọng và phổ biến nhất trong việc Phát triển và Bảo mật Ứng dụng Web (Web Application Security) được cập nhật định kỳ, là kim chỉ nam cho các lập trình viên
C. Top 10 phần mềm diệt virus tốt nhất
D. Các phương pháp mã hóa dữ liệu cơ sở dữ liệu
*Đáp án: B*
*Giải thích: Dự án Mở về Bảo mật Ứng dụng Web (OWASP) liên tục công bố các nguy cơ như Injection, Broken Authentication, XSS... giúp định chuẩn hóa việc rà soát mã nguồn (Code Review) và Penetration Testing cho Web.*

**Câu 194:** Khi người dùng cố gắng vào một trang web HTTPS, trình duyệt cảnh báo "Chứng chỉ bảo mật không hợp lệ (Invalid Certificate) hoặc bị cảnh báo Tên miền không khớp (Name Mismatch)". Hành động an toàn nhất người dùng nên làm là gì?
A. Bấm nút "Bỏ qua cảnh báo và tiếp tục truy cập" (Proceed anyway) vì đó là lỗi của trình duyệt
B. Cài đặt chứng chỉ đó vào máy để hết báo lỗi
C. Dừng truy cập ngay lập tức vì hệ thống mạng (ví dụ Wi-Fi công cộng) rất có thể đang bị tấn công đánh chặn (Man-in-the-Middle - MitM) lừa gạt trình duyệt bằng một chứng chỉ số giả mạo
D. Tải lại trang web nhiều lần
*Đáp án: C*
*Giải thích: Trình duyệt cảnh báo nghĩa là nó không thể xác minh (PKI) máy chủ đang kết nối thực sự là máy chủ hợp pháp. Rất nhiều người có thói quen bấm "Proceed anyway" và rơi ngay vào bẫy MITM của Hacker đang đứng giữa môi trường Wi-Fi.*

**Câu 195:** Trong mật mã học, "Kích thước không gian khóa" (Key Space Size) quyết định yếu tố nào của hệ thống mã hóa?
A. Dung lượng ổ cứng cần thiết để lưu trữ thuật toán
B. Tốc độ truyền tải qua mạng internet
C. Độ khó và thời gian cần thiết để một kẻ tấn công có thể bẻ khóa thuật toán bằng phương pháp thử toàn bộ các khóa (Brute-force attack). Không gian khóa càng lớn (ví dụ 256-bit so với 128-bit), hệ thống càng mất nhiều thời gian theo cấp số nhân để phá vỡ
D. Dung lượng của gói tin đã mã hóa
*Đáp án: C*
*Giải thích: Một khóa 128-bit có $2^{128}$ tổ hợp. Tăng thêm 1 bit (129-bit) thì độ khó tăng lên gấp đôi. Do máy tính ngày càng mạnh, kích thước khóa (key length) liên tục phải tăng lên để đảm bảo an toàn.*

**Câu 196:** "Rainbow Table" (Bảng cầu vồng) là công cụ mà hacker sử dụng để tiết kiệm thời gian khi thực hiện việc gì?
A. Tìm kiếm các cổng mở trên hệ thống mạng
B. Xóa dấu vết trong file nhật ký (Log files)
C. Bẻ khóa (Crack) hàng loạt các bản băm mật khẩu (Password Hashes) bị đánh cắp bằng cách sử dụng các bảng dữ liệu khổng lồ tính toán sẵn giá trị băm của hàng tỷ mật khẩu thông dụng, thay vì phải chạy thuật toán tính băm (hashing) lại từ đầu cho từng lần đoán
D. Khai thác lỗi SQL Injection
*Đáp án: C*
*Giải thích: Tính băm Hash(MD5) của một mật khẩu tốn rất ít thời gian CPU, nhưng tính băm của 1 tỷ mật khẩu (Brute force) thì tốn rất nhiều. Rainbow Table tính sẵn mọi trường hợp và lưu vào ổ cứng (Terabytes). Khi có mã băm của nạn nhân, hacker chỉ việc "Tra cứu ngược" (Lookup) trên bảng này cực nhanh. Salting là khắc tinh của Rainbow Table.*

**Câu 197:** Hệ thống "SIEM" (Security Information and Event Management) trong các Trung tâm điều hành an ninh (SOC) giải quyết bài toán lớn nào?
A. Tự động mã hóa tất cả dữ liệu máy tính công ty
B. Phân phát IP cho các thiết bị mạng
C. Thu thập, tập trung hóa (Centralize) và phân tích tương quan (Correlation) hàng triệu dòng nhật ký (Log/Events) khổng lồ được đổ về từ hàng trăm thiết bị khác nhau (Firewall, Server, Antivirus...) theo thời gian thực. Giúp phát hiện ra các chuỗi hành vi tấn công tinh vi (như APT) đang lẩn khuất giữa biển dữ liệu rác
D. Chống lại cuộc tấn công DDoS vào hệ thống DNS
*Đáp án: C*
*Giải thích: Một nỗ lực đăng nhập sai trên Windows Server không có ý nghĩa gì. Nhưng 100 lần đăng nhập sai từ Server A, kết hợp với Firewall báo cáo Server A đang gửi file lạ ra IP nước ngoài. SIEM (như Splunk, QRadar) sẽ phân tích tương quan (Correlation) 2 sự kiện này và ngay lập tức nháy đèn đỏ báo động có tấn công APT.*

**Câu 198:** "Zero Trust Architecture" (Kiến trúc Không tin cậy) xóa bỏ hoàn toàn khái niệm nào trong các mô hình bảo mật mạng truyền thống?
A. Khái niệm xác thực mật khẩu
B. Khái niệm mã hóa dữ liệu
C. Khái niệm "Vùng tin cậy mặc định" (Default Trust) hay "Mạng nội bộ an toàn". Nó yêu cầu mọi luồng dữ liệu, dù xuất phát từ bên trong LAN hay ngoài Internet, dù là nhân viên hay giám đốc, đều phải bị coi là thù địch và PHẢI XÁC THỰC LẠI, KIỂM TRA QUYỀN HẠN LIÊN TỤC (Verify explicitly) trước khi được truy cập bất kỳ tài nguyên nào
D. Khái niệm Tường lửa (Firewall)
*Đáp án: C*
*Giải thích: Triết lý cốt lõi của Zero Trust là "Never trust, always verify" (Không bao giờ tin, luôn luôn xác minh). Ngay cả khi bạn đang ngồi trong trụ sở công ty cắm cáp mạng LAN, bạn cũng không có quyền truy cập Server Kế toán nếu không có chứng thực danh tính (Identity-driven security).*

**Câu 199:** Giải pháp bảo mật "EDR" (Endpoint Detection and Response) là thế hệ tiếp theo, vượt trội hơn các phần mềm Antivirus (AV) truyền thống ở khả năng nào?
A. Cập nhật mẫu virus tự động qua mạng nhanh hơn
B. EDR không chỉ dựa vào việc so khớp chữ ký mẫu (Signature) mã độc, mà nó GIÁM SÁT LIÊN TỤC và GHI LẠI toàn bộ hành vi của máy trạm (Tiến trình đang chạy, kết nối mạng, thay đổi Registry). Từ đó sử dụng Trí tuệ nhân tạo (AI/ML) phân tích hành vi để phát hiện và cô lập ngay lập tức các mối đe dọa vô hình (như Fileless Malware hay Zero-day) mà AV truyền thống bỏ lọt
C. Có dung lượng cài đặt nhỏ hơn nhiều
D. Hoạt động như một Firewall phần cứng
*Đáp án: B*
*Giải thích: EDR giống như camera an ninh hộp đen gắn trên mỗi máy tính cá nhân (Endpoint). Nó ghi nhận hành vi "bất thường" (Anomaly). Ví dụ: file Word tự nhiên chạy lệnh PowerShell ẩn để tải file từ mạng -> EDR lập tức chặn đứng (Response) tiến trình Word đó vì đó là hành vi của mã độc Macro, dù file Word chưa từng bị nhận diện là Virus.*

**Câu 200:** Theo khái niệm "Bảo mật phòng thủ chủ động", thuật ngữ "Kill Chain" (Chuỗi tiêu diệt mạng - Cyber Kill Chain) do Lockheed Martin phát triển được sử dụng để làm gì?
A. Mô tả các bước thiết lập mã hóa dữ liệu
B. Chia nhỏ quá trình tấn công xâm nhập mạng của một chiến dịch APT (Advanced Persistent Threat) thành các Giai đoạn (Phases) mang tính cấu trúc (Từ Thăm dò, Vũ khí hóa, Chuyển giao, Khai thác, Cài đặt, Điều khiển C&C, đến Thực hiện mục tiêu). Giúp đội phòng thủ có thể chèn các biện pháp đánh chặn (Break the chain) ở bất kỳ khâu nào để làm thất bại toàn bộ cuộc tấn công
C. Tấn công ngược lại máy chủ của hacker
D. Làm đứt liên kết mạng của thiết bị nhiễm virus
*Đáp án: B*
*Giải thích: Cyber Kill Chain cung cấp một tư duy chiến lược cực kỳ xuất sắc. Hacker phải thực hiện thành công một chuỗi 7 bước liên hoàn để trộm dữ liệu. Người phòng thủ chỉ cần phá vỡ ĐÚNG MỘT MẮT XÍCH (ví dụ chặn bước Chuyển giao Email chứa mã độc, hoặc chặn kết nối C&C ra ngoài), thì toàn bộ nỗ lực tấn công APT của tin tặc đều đổ sông đổ biển.*
