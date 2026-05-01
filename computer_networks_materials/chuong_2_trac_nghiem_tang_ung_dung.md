# CHƯƠNG 2: TRẮC NGHIỆM TẦNG ỨNG DỤNG (APPLICATION LAYER)

**Câu 1:** Trong kiến trúc mạng Client-Server, máy chủ (Server) bắt buộc phải có đặc điểm nào sau đây để các máy khách (Client) có thể tìm và kết nối ổn định?
A. Phải luôn thay đổi địa chỉ IP động để tăng tính bảo mật.
B. Phải có một địa chỉ IP tĩnh, cố định và luôn luôn hoạt động (always-on).
C. Phải chủ động khởi tạo liên lạc tới các máy khách.
D. Chỉ hoạt động trong giờ hành chính.
*Đáp án: B*
*Giải thích: Do client luôn là người chủ động gọi kết nối, server phải ở đó chờ sẵn (always-on) và phải giữ nguyên địa chỉ nhà (IP tĩnh) thì client mới gõ cửa được.*

**Câu 2:** Kiến trúc mạng ngang hàng (P2P - Peer-to-Peer) giải quyết vấn đề lớn nhất nào của kiến trúc Client-Server truyền thống?
A. Vấn đề mã hóa dữ liệu.
B. Vấn đề bảo mật chống lại virus.
C. Nút thắt cổ chai (bottleneck) ở máy chủ khi có lượng lớn người dùng tải dữ liệu cùng lúc, nhờ khả năng tự mở rộng băng thông (mỗi client tự làm server cho người khác).
D. Phân giải tên miền (DNS).
*Đáp án: C*
*Giải thích: P2P tự phân phối gánh nặng truyền tải băng thông cho tất cả các máy cùng tải file, biến nhược điểm đông người thành ưu điểm.*

**Câu 3:** Khái niệm "Socket" trong lập trình mạng máy tính là gì?
A. Là cổng kết nối vật lý (RJ45) để cắm dây mạng vào máy tính.
B. Là giao diện phần mềm lập trình (API) kết nối giữa tiến trình của Ứng dụng (Application process) và giao thức tầng Giao vận (Transport layer).
C. Là một cửa sổ của trình duyệt web.
D. Là đoạn mã hóa mật khẩu của Router.
*Đáp án: B*
*Giải thích: Socket là cánh cửa ảo do hệ điều hành cung cấp. Ứng dụng đẩy data vào socket, hệ điều hành sẽ nhặt data đó bỏ vào TCP hoặc UDP để truyền đi.*

**Câu 4:** Để xác định chính xác một tiến trình ứng dụng (ví dụ: máy chủ Web HTTP) đang chạy trên một máy tính từ xa trong hàng chục tiến trình khác, ta cần sử dụng thông tin định danh nào?
A. Địa chỉ IP của máy tính đó.
B. Địa chỉ MAC của máy tính đó.
C. Địa chỉ IP của máy đó kết hợp với Số hiệu cổng (Port Number) của tiến trình.
D. Tên của hệ điều hành.
*Đáp án: C*
*Giải thích: IP dẫn đường gói tin tới đúng chiếc máy tính phần cứng. Port dẫn đường gói tin lọt vào đúng ứng dụng phần mềm bên trong máy tính đó.*

**Câu 5:** Giao thức TCP cung cấp dịch vụ gì cho các ứng dụng ở tầng trên?
A. Không đảm bảo gói tin tới đích.
B. Tốc độ truyền cực kỳ nhanh nhờ bỏ qua kết nối.
C. Truyền tải dữ liệu tin cậy (không lỗi, không mất, đúng thứ tự) và có cơ chế kiểm soát tắc nghẽn luồng.
D. Phân giải tên miền ra địa chỉ IP.
*Đáp án: C*
*Giải thích: TCP là bảo chứng cho sự tin cậy. Dữ liệu ném vào TCP chắc chắn sẽ đến tay người nhận hoàn hảo, hoặc TCP sẽ báo lỗi nếu mạng sập.*

**Câu 6:** Giao thức UDP (User Datagram Protocol) phù hợp nhất với loại ứng dụng mạng nào dưới đây?
A. Gửi email (SMTP)
B. Chuyển tiền ngân hàng
C. Hội thoại Video thời gian thực (Video Call/VoIP)
D. Tải tệp tin (FTP)
*Đáp án: C*
*Giải thích: Video call nhạy cảm với thời gian (delay) hơn là mất mát. UDP nhẹ, nhanh, không bắt tay lằng nhằng, rớt vài khung hình (vài gói tin) không ảnh hưởng nghiêm trọng.*

**Câu 7:** HTTP là giao thức "Phi trạng thái" (Stateless). Điều này có nghĩa là gì đối với máy chủ Web?
A. Máy chủ không mã hóa dữ liệu.
B. Máy chủ không hề lưu giữ thông tin hay ghi nhớ bất kỳ trạng thái nào về các yêu cầu trước đó của cùng một Client.
C. Máy chủ sẽ ngắt kết nối Internet nếu trạng thái đường truyền kém.
D. Trình duyệt không thể lưu Bookmark.
*Đáp án: B*
*Giải thích: Nếu bạn request trang A, sau đó 1 giây lại request trang A, máy chủ Stateless sẽ phục vụ bạn lại từ đầu y hệt một người hoàn toàn lạ mặt.*

**Câu 8:** Công cụ nào sinh ra để vá lại lỗ hổng "Phi trạng thái" của HTTP, giúp các trang web e-commerce có thể nhớ được bạn đã bỏ mặt hàng gì vào giỏ hàng?
A. DNS Records
B. HTML5
C. Caching (Proxy)
D. Cookies
*Đáp án: D*
*Giải thích: Cookies được server đóng dấu lên trình duyệt. Các yêu cầu sau của trình duyệt sẽ mang theo cái dấu đó (Cookie ID) để Server nhận diện người quen.*

**Câu 9:** Chữ "S" trong chuẩn HTTPS đại diện cho giao thức mã hóa nào hoạt động ngay dưới tầng HTTP để bảo vệ dữ liệu khỏi nghe lén?
A. SMTP
B. SSL/TLS
C. SSH
D. SAN
*Đáp án: B*
*Giải thích: HTTPS thực chất là HTTP chạy trên nền Transport Layer Security (TLS), trước đây gọi là SSL.*

**Câu 10:** Sự khác biệt giữa Web Caching (Proxy Server) và Origin Server (Máy chủ gốc) là gì?
A. Origin server nằm ở gần người dùng hơn.
B. Web cache chỉ lưu giữ BẢN SAO của các nội dung web phổ biến, giúp giảm độ trễ cho người dùng nội bộ, trong khi Origin Server là nơi thực sự lưu bản gốc do nhà phát triển web tải lên.
C. Web cache dùng để phát video, Origin server dùng để lưu HTML.
D. Web cache là thuật ngữ khác của thẻ SD.
*Đáp án: B*
*Giải thích: Mạng công ty mua 1 con Proxy làm Web Cache để mọi nhân viên đọc chung báo VnExpress một cách siêu tốc mà không làm tốn băng thông chung ra Internet.*

**Câu 11:** Nếu một trang HTML cơ sở chứa 10 hình ảnh nhúng, khi sử dụng HTTP/1.0 Non-persistent (Không bền bỉ), trình duyệt sẽ phải mở bao nhiêu kết nối TCP?
A. 1 kết nối duy nhất
B. 10 kết nối
C. 11 kết nối (1 cho HTML + 10 cho ảnh)
D. 2 kết nối
*Đáp án: C*
*Giải thích: Non-persistent tức là cứ tải xong 1 file thì đóng luôn TCP. Vậy 11 đối tượng sẽ phải trải qua 11 lần quá trình bắt tay TCP.*

**Câu 12:** Lợi ích của HTTP/1.1 Persistent (Bền bỉ) so với bản Non-persistent là gì?
A. Máy chủ dùng Cookie tốt hơn.
B. Trình duyệt không cần phải xin lại IP từ DNS.
C. Kết nối TCP được giữ MỞ sau khi tải file đầu tiên, giúp tiết kiệm RTT (Round Trip Time) và tài nguyên CPU cho các tệp tin tiếp theo lấy từ cùng một máy chủ.
D. Hình ảnh trên web sẽ tự động nén nhỏ lại.
*Đáp án: C*
*Giải thích: Không phải lặp lại bắt tay 3 bước TCP cho mỗi tấm ảnh, làm tăng tốc độ hiển thị trang lên rất nhiều.*

**Câu 13:** Trong hệ thống Thư điện tử (Email), giao thức SMTP được sử dụng cho giai đoạn nào?
A. Để người dùng đọc thư trên điện thoại di động (Pull).
B. Để đính kèm các tệp tin lớn.
C. Để GỬI ĐẨY (Push) thư từ máy tính của người gửi lên Mail Server và đẩy từ Mail Server này sang Mail Server khác.
D. Để mã hóa thư rác (Spam).
*Đáp án: C*
*Giải thích: SMTP (Simple Mail Transfer Protocol) là một Push Protocol. Nó chỉ có chức năng đẩy thư ra đi.*

**Câu 14:** Giao thức nào thường được sử dụng để KÉO (Pull) thư từ Mail Server về phần mềm như Microsoft Outlook của máy khách?
A. SMTP
B. IMAP hoặc POP3
C. FTP
D. SNMP
*Đáp án: B*
*Giải thích: POP3 (tải về cục bộ rồi xóa trên server) và IMAP (duy trì trạng thái đồng bộ nhiều thư mục trên server) là các Pull protocol dành cho nhận email.*

**Câu 15:** Vì sao ứng dụng truy vấn DNS lại sử dụng tầng giao vận UDP thay vì TCP?
A. Vì dữ liệu truy vấn của DNS thường lớn hàng chục Megabyte.
B. Vì DNS ưu tiên tốc độ phản hồi cực nhanh, không muốn tốn 1 RTT để thiết lập bắt tay, và bản tin DNS nhỏ nên nếu rớt có thể gửi lại ngay lập tức.
C. Vì UDP an toàn và bảo mật hơn chống lại tin tặc.
D. Vì router từ chối các kết nối TCP port 53.
*Đáp án: B*
*Giải thích: Truy vấn DNS là: "Ông ơi IP của google là gì?" - "Đây 142.250.x.x". Thông điệp quá nhỏ, dùng TCP bắt tay sẽ làm chậm đi rất nhiều.*

**Câu 16:** Các máy chủ Root DNS (Gốc) trả về thông tin gì khi được hỏi về một địa chỉ IP (ví dụ www.google.com)?
A. Trả về chính xác địa chỉ IP của www.google.com
B. Trả về địa chỉ IP của một Máy chủ TLD (Top-Level Domain) quản lý đuôi .com.
C. Trả về lỗi 404.
D. Trả về địa chỉ của modem mạng nhà bạn.
*Đáp án: B*
*Giải thích: DNS là hệ thống phân cấp. Root chỉ biết đường chỉ tay đến TLD (.com, .org). TLD lại chỉ tay về Authoritative (máy chủ của Google).*

**Câu 17:** Thuật toán nào giúp hệ thống BitTorrent lựa chọn các máy ngang hàng (Peer) nào để ưu tiên Upload (gửi dữ liệu)?
A. Cây khung (Spanning Tree).
B. FIFO (Đến trước phục vụ trước).
C. Tit-for-tat (Hòn bấc ném đi, hòn chì ném lại) - ưu tiên các máy nào đang download lại cho mình với tốc độ cao nhất.
D. Bầu chọn ngẫu nhiên.
*Đáp án: C*
*Giải thích: Tit-for-tat ngăn chặn hiện tượng "Free-rider" (chỉ tải về không chịu tải lên) trong mạng P2P, ép mọi người phải cống hiến băng thông.*

**Câu 18:** Kỹ thuật DASH (Dynamic Adaptive Streaming over HTTP) dùng trong Netflix và YouTube có nguyên lý gì đặc biệt?
A. Chuyển tín hiệu truyền hình cáp vào trong cáp quang.
B. Video được lưu thành hàng trăm file nhỏ (chunks) với các chất lượng/độ phân giải khác nhau. Trình duyệt tự đo tốc độ mạng hiện tại để linh hoạt chọn tải đoạn file chất lượng cao hay thấp phù hợp để chống giật (buffering).
C. Mã hóa video bằng RSA để chống vi phạm bản quyền.
D. Tự động tắt máy chủ nếu có quá nhiều người xem.
*Đáp án: B*
*Giải thích: Chữ Adaptive (Thích ứng) cho thấy việc chuyển đổi mượt mà giữa mờ/nét tùy vào đường truyền mạng lúc đang xem.*

**Câu 19:** Hạ tầng CDN (Content Delivery Network) mang lại lợi ích gì cho các website toàn cầu?
A. Cấm truy cập từ các quốc gia bị liệt vào sổ đen.
B. Dùng một Server siêu to khổng lồ duy nhất đặt ở Mỹ để phục vụ 8 tỷ người.
C. Giảm đáng kể độ trễ bằng cách đưa các cụm máy chủ lưu trữ bản sao nội dung (Replica Cache) lại gần sát với vị trí địa lý của khách hàng nhất có thể.
D. Giảm dung lượng file video.
*Đáp án: C*
*Giải thích: CDN là chìa khóa để Internet không bị nghẽn cổ chai khi hàng triệu người cùng xem một trận chung kết bóng đá.*

**Câu 20:** Lệnh nào là một HTTP Method dùng để gửi dữ liệu mẫu (Form) của người dùng từ Trình duyệt lên Server?
A. SEND
B. UPLOAD
C. GET
D. POST
*Đáp án: D*
*Giải thích: GET chủ yếu để yêu cầu nội dung (với tham số đính kèm ở URL), còn POST để nộp cục dữ liệu lớn (form, upload) giấu trong phần body của message.*

**Câu 21:** Nếu một bản ghi DNS thuộc kiểu "MX" (Mail Exchanger), trường dữ liệu giá trị (Value) của nó sẽ cung cấp thông tin gì?
A. Địa chỉ IPv4 của trang web.
B. Địa chỉ IP của máy chủ DNS.
C. Tên miền thực (Canonical name) của một bí danh.
D. Tên (Hostname) của hệ thống máy chủ phụ trách nhận Thư điện tử cho tên miền đó.
*Đáp án: D*
*Giải thích: Khi bạn gửi mail tới @gmail.com, giao thức ngầm hỏi DNS "Record MX của gmail.com là gì" để biết Mail Server đích ở đâu mà đẩy tới bằng SMTP.*

**Câu 22:** Máy chủ DNS có thẩm quyền (Authoritative DNS Server) là gì?
A. Máy chủ quản lý các tên miền .com và .org.
B. Máy chủ DNS nội bộ của nhà cung cấp dịch vụ Internet (như VNPT, FPT) đứng ra hỏi giùm bạn.
C. Máy chủ thuộc sở hữu của tổ chức chứa thông tin ánh xạ IP gốc, chính xác tuyệt đối do chính tổ chức đó cấu hình cho website của họ.
D. Máy chủ dùng chung của Google (8.8.8.8).
*Đáp án: C*
*Giải thích: Authoritative là điểm kết thúc cuối cùng của chuỗi tra cứu phân giải tên miền. Tổ chức tự quản lý IP của mình trên máy chủ này.*

**Câu 23:** Cổng (Port) là khái niệm ở Tầng Giao vận, nhưng là thứ sống còn để thiết lập Socket ở Tầng Ứng dụng. Dải cổng được cấp phép chuẩn (Well-known ports) giới hạn từ đâu đến đâu?
A. Từ 0 đến 65535
B. Từ 0 đến 1023
C. Từ 1024 đến 49151
D. Từ 0 đến 255
*Đáp án: B*
*Giải thích: IANA quy định dải port từ 0 đến 1023 cho các giao thức mạng hệ thống phổ biến (HTTP 80, FTP 21, SSH 22).*

**Câu 24:** Thông điệp HTTP Response từ Server mang theo một mã trạng thái "404 Not Found" ở ngay dòng đầu tiên (Status line). Điều này có ý nghĩa gì?
A. Trình duyệt bị mất kết nối mạng.
B. Yêu cầu thành công, dữ liệu nằm ở dưới.
C. Máy chủ không hiểu được cú pháp yêu cầu.
D. Tài liệu (đối tượng) mà trình duyệt yêu cầu không tồn tại trên máy chủ.
*Đáp án: D*
*Giải thích: Mã 2xx là thành công. 3xx là điều hướng. 4xx là lỗi do khách hàng yêu cầu sai (vd: file không có). 5xx là lỗi sập server nội bộ.*

**Câu 25:** Quá trình "Truy vấn đệ quy" (Recursive Query) trong DNS khác với "Truy vấn lặp" (Iterative Query) ở điểm nào?
A. Trong đệ quy, máy chủ DNS được hỏi sẽ tự mình gánh trách nhiệm liên hệ tiếp với máy chủ khác để tìm bằng được kết quả trả về, thay vì chỉ tay "hãy đi hỏi ông kia" như Iterative.
B. Đệ quy chỉ dùng trong mạng LAN, lặp dùng trên Internet.
C. Truy vấn lặp nhanh hơn đệ quy gấp đôi.
D. Truy vấn đệ quy không thể bị bắt gói tin.
*Đáp án: A*
*Giải thích: Cấu hình mặc định thường là máy bạn hỏi đệ quy lên Local DNS. Sau đó Local DNS làm công việc cực nhọc là đi hỏi Lặp (Iterative) lên Root, TLD...*

**Câu 26:** Ứng dụng "Skype" hoặc "Zoom" yêu cầu tiêu chí nào khắt khe nhất từ phía dịch vụ mạng?
A. Không bao giờ được mất một byte dữ liệu nào.
B. Độ trễ và jitter thời gian thực (Timing / Delay) phải cực thấp.
C. Băng thông tối thiểu 1 Gbps.
D. Mã hóa RSA 4096-bit.
*Đáp án: B*
*Giải thích: Ứng dụng đàm thoại trực tiếp đòi hỏi độ trễ thường < 150ms để tạo cảm giác tự nhiên. Mất vài pixel khung hình vẫn chấp nhận được.*

**Câu 27:** Mạng P2P có đặc điểm gì giúp việc phát tán file trở nên "Tự mở rộng" (Self-scalability)?
A. Máy chủ được tự động phân bổ RAM.
B. Khi càng nhiều Peer tham gia mạng để download, tổng nhu cầu tải về tăng, nhưng ĐỒNG THỜI năng lực upload của toàn mạng cũng tăng lên tương xứng do chính các peer đó đóng góp.
C. Mạng dùng cáp quang nên tự động giãn nở băng thông.
D. ISP không thể kiểm soát được dữ liệu.
*Đáp án: B*
*Giải thích: Khác với Client-server, P2P mang theo định lý "mỗi người đến ăn tiệc đều mang theo một đĩa thức ăn".*

**Câu 28:** Trong BitTorrent, thuật ngữ "Choked" và "Unchoked" mô tả trạng thái gì giữa các peer?
A. Mạng bị đứt cáp và mạng đã nối lại.
B. Hành động máy trạm A ngắt không gửi data (Choke) hoặc đồng ý mở vòi gửi data (Unchoke) cho máy trạm B dựa trên thuật toán đánh giá tốc độ trao đổi.
C. Bị nhiễm virus và đã diệt virus.
D. Mã hóa và giải mã file zip.
*Đáp án: B*
*Giải thích: Tit-for-tat duy trì 4 peer "unchoked" (gửi dữ liệu) và choke tất cả những người còn lại để phạt những kẻ xài chùa.*

**Câu 29:** Nếu một Server muốn thông báo cho Client về việc điều hướng trang web (ví dụ truy cập http://abc.com bị đẩy sang https://abc.com), mã phản hồi HTTP nào sẽ được dùng?
A. 200 OK
B. 301 Moved Permanently (Hoặc các mã 3xx)
C. 403 Forbidden
D. 500 Internal Server Error
*Đáp án: B*
*Giải thích: Các mã 3xx dùng cho Redirect. Trình duyệt nhận được sẽ tự động tải địa chỉ mới nằm trong trường header Location.*

**Câu 30:** Ứng dụng mạng (Network Application) chạy trên nền hệ điều hành được gọi chung là gì?
A. Frame
B. Thread
C. Protocol
D. Tiến trình (Process)
*Đáp án: D*
*Giải thích: Bất kỳ phần mềm nào đang được thực thi trên OS (như Chrome, Apache, Zoom) đều là một Process. Các Process này liên lạc qua Socket.*

**Câu 31:** Ứng dụng mạng có thể sử dụng các "Socket" để giao tiếp. Phát biểu nào sau đây ĐÚNG về Socket?
A. Socket là một thiết bị phần cứng nằm giữa CPU và Card mạng.
B. Socket là giao diện lập trình (API) giữa tầng Ứng dụng (Application) và tầng Giao vận (Transport), thông qua đó tiến trình gửi và nhận thông điệp.
C. Mọi loại Socket đều sử dụng giao thức TCP.
D. Socket chỉ dùng cho việc truy cập Web.
*Đáp án: B*
*Giải thích: Socket là cánh cửa lập trình. Tiến trình đẩy thông điệp qua cánh cửa đó ra ngoài mạng và hệ điều hành sẽ phụ trách việc chuyển đi qua giao thức tầng giao vận tương ứng.*

**Câu 32:** Yêu cầu (Requirement) nào sau đây mà giao thức TCP KHÔNG cung cấp cho tầng ứng dụng?
A. Đảm bảo dữ liệu đến đích không bị lỗi (Data integrity).
B. Đảm bảo thông lượng tối thiểu (Minimum Throughput Guarantee).
C. Chuyển giao dữ liệu đúng thứ tự (In-order delivery).
D. Kiểm soát tắc nghẽn (Congestion control).
*Đáp án: B*
*Giải thích: TCP cung cấp sự tin cậy (reliability), nhưng nó không thể đảm bảo một tốc độ bit (throughput) cụ thể hay thời gian trễ (delay) cụ thể, điều này phụ thuộc vào tình trạng mạng vật lý.*

**Câu 33:** Giao thức nào ở tầng Giao vận phù hợp nhất cho các ứng dụng yêu cầu truyền tệp tin chính xác tuyệt đối như FTP?
A. UDP
B. RTP
C. TCP
D. ICMP
*Đáp án: C*
*Giải thích: FTP cần tính toàn vẹn 100%. Nếu mất 1 byte mã nguồn, tệp đó sẽ bị hỏng. Do đó TCP với cơ chế truyền lại là bắt buộc.*

**Câu 34:** Giao thức nào phù hợp nhất cho việc truyền tải âm thanh/video thời gian thực qua mạng (như gọi Skype, Zoom)?
A. TCP
B. HTTP
C. UDP
D. SMTP
*Đáp án: C*
*Giải thích: Gọi điện thời gian thực cần độ trễ thấp nhất có thể. UDP không mất thời gian thiết lập kết nối (handshake) và không chờ đợi để truyền lại gói lỗi (làm tăng trễ).*

**Câu 35:** Tại sao DNS sử dụng UDP thay vì TCP cho các truy vấn phân giải tên miền thông thường?
A. Vì UDP bảo mật hơn TCP.
B. Truy vấn DNS thường rất nhỏ (vừa 1 gói tin) và cần phản hồi cực nhanh. Sử dụng TCP phải mất 3-way handshake làm chậm quá trình phân giải.
C. Vì các máy chủ DNS không hỗ trợ TCP.
D. Vì dữ liệu DNS thường có lỗi nên dùng UDP để không phải sửa lỗi.
*Đáp án: B*
*Giải thích: Tốc độ là ưu tiên số một của truy vấn DNS (thường dùng port 53 UDP). Nếu UDP bị mất gói, DNS client (trình duyệt) chỉ đơn giản gửi lại truy vấn UDP khác sau vài giây timeout.*

**Câu 36:** Trong kiến trúc mạng P2P, khái niệm "Tự mở rộng" (Self-scalability) có nghĩa là gì?
A. Hệ thống có khả năng tự động thuê thêm máy chủ Cloud khi có tải.
B. Băng thông của mạng tự động được tăng gấp đôi.
C. Mỗi một người dùng tham gia vào tải file mới (peer) không chỉ tạo ra yêu cầu tải về mà còn đóng góp khả năng tải lên cho mạng lưới.
D. File dữ liệu tự động thay đổi kích thước cho vừa băng thông.
*Đáp án: C*
*Giải thích: Càng nhiều người download trong torrent thì lượng băng thông upload đóng góp vào hệ thống càng lớn, giúp việc chia sẻ file khổng lồ không bị sập.*

**Câu 37:** Mã trạng thái (Status code) HTTP nào bắt đầu biểu thị các lỗi do phía máy khách (Client Error) gây ra, ví dụ như gửi sai định dạng hay yêu cầu file không tồn tại?
A. 2xx (Ví dụ: 200 OK)
B. 3xx (Ví dụ: 301 Moved Permanently)
C. 4xx (Ví dụ: 404 Not Found)
D. 5xx (Ví dụ: 500 Internal Server Error)
*Đáp án: C*
*Giải thích: Mã 4xx chỉ ra rằng client (trình duyệt) đã gửi một yêu cầu có vấn đề (VD: 400 Bad Request, 403 Forbidden, 404 Not Found).*

**Câu 38:** Giao thức HTTP là giao thức "vô trạng thái" (stateless). Khẳng định này có nghĩa là gì?
A. Nó không dùng địa chỉ IP.
B. Trình duyệt không thể lưu giữ lịch sử.
C. Máy chủ web không giữ lại bất kỳ thông tin nào về các yêu cầu trước đó của máy khách. Mỗi request là hoàn toàn độc lập.
D. HTTP không thể được mã hóa.
*Đáp án: C*
*Giải thích: Server nhận HTTP Request, gửi HTTP Response và ngay lập tức quên đi ai vừa hỏi. Thiết kế này giúp Server giảm tải cực lớn vì không phải duy trì bộ nhớ về từng phiên.*

**Câu 39:** Cơ chế nào giúp các website nhận diện người dùng (ví dụ: giỏ hàng, đăng nhập) mặc dù HTTP là vô trạng thái?
A. MAC Address Filtering
B. Giao thức FTP kết hợp
C. Cookies và Sessions
D. DHCP
*Đáp án: C*
*Giải thích: Lần đầu truy cập, Server tạo một Cookie (Mã định danh) và gửi về cho Browser. Các lần request sau, Browser gắn kèm Cookie này lên Header để Server biết "người quen".*

**Câu 40:** Web Cache (Proxy Server) mang lại lợi ích gì cho tổ chức/doanh nghiệp cài đặt nó?
A. Tăng băng thông tối đa của ISP lên gấp đôi.
B. Giảm thời gian phản hồi cho các yêu cầu của client (do lấy từ cache cục bộ) và giảm lượng lưu lượng truyền ra đường kết nối Internet của tổ chức.
C. Thay thế hoàn toàn chức năng của máy chủ DNS.
D. Ngăn chặn mọi cuộc tấn công DDoS.
*Đáp án: B*
*Giải thích: Proxy giữ bản sao các trang web phổ biến. Nếu nhiều người trong công ty cùng đọc 1 báo, trang báo đó chỉ được tải về 1 lần từ Internet rồi lưu ở Proxy, giảm tải cực tốt.*

**Câu 41:** "Conditional GET" (GET có điều kiện) trong giao thức HTTP sử dụng trường Header nào để hỏi máy chủ xem file đã bị thay đổi kể từ lần cuối tải xuống hay chưa?
A. User-Agent:
B. Content-Type:
C. If-Modified-Since:
D. Cookie:
*Đáp án: C*
*Giải thích: Trình duyệt gửi "If-Modified-Since: [Ngày tháng]", nếu Server thấy file chưa đổi từ ngày đó, nó trả về mã 304 Not Modified kèm thân trống, giúp tiết kiệm băng thông.*

**Câu 42:** Khi sử dụng Webmail (như Gmail trên trình duyệt), giao thức nào được sử dụng ĐỂ GIAO TIẾP GIỮA trình duyệt của bạn và máy chủ của Google?
A. SMTP
B. POP3
C. IMAP
D. HTTP/HTTPS
*Đáp án: D*
*Giải thích: Khác với dùng ứng dụng Outlook (dùng IMAP/POP3), Webmail bản chất là một trang web, mọi tương tác (xem thư, gửi thư) từ máy bạn đến Server của hãng diễn ra qua HTTPS.*

**Câu 43:** Giao thức SMTP (Simple Mail Transfer Protocol) sử dụng cổng TCP mặc định nào?
A. 21
B. 25
C. 80
D. 110
*Đáp án: B*
*Giải thích: Port mặc định của SMTP dùng để chuyển tiếp mail (Mail transfer) là 25 (hoặc 587 cho submission có mã hóa).*

**Câu 44:** Sự khác biệt chính giữa việc tải thư về bằng giao thức POP3 và IMAP là gì?
A. POP3 dùng cho gửi thư, IMAP dùng cho nhận thư.
B. POP3 luôn mã hóa, IMAP không mã hóa.
C. POP3 mặc định tải thư về máy trạm và xoá trên máy chủ (chỉ quản lý trên 1 thiết bị). IMAP đồng bộ hóa trạng thái thư (đọc, chưa đọc, thư mục) giữ nguyên trên máy chủ (quản lý đa thiết bị).
D. Không có khác biệt.
*Đáp án: C*
*Giải thích: IMAP hiện đại hơn, cho phép bạn đọc 1 email trên điện thoại và nó sẽ lập tức báo "Đã đọc" khi bạn xem trên máy tính, vì mọi thứ nằm trên Server.*

**Câu 45:** Trong bản tin HTTP Request, dòng đầu tiên (Request line) chứa thông tin gì?
A. Phương thức (Method) như GET/POST, URL được yêu cầu và Phiên bản HTTP.
B. Địa chỉ IP của máy khách.
C. Thông tin về hệ điều hành và trình duyệt (User-Agent).
D. Cookie của phiên làm việc.
*Đáp án: A*
*Giải thích: Cấu trúc cơ bản của Request line: `[Method] [URL] [HTTP Version]\r\n` (Ví dụ: `GET /index.html HTTP/1.1`).*

**Câu 46:** Phương thức HTTP nào thường dùng để gửi dữ liệu từ biểu mẫu (Form) lên máy chủ, trong đó dữ liệu được đặt trong phần "thân" (Body) của Request?
A. GET
B. POST
C. HEAD
D. DELETE
*Đáp án: B*
*Giải thích: Mặc dù GET cũng có thể gửi dữ liệu (qua URL parameters), POST an toàn và chứa được nhiều dữ liệu hơn vì nó để dữ liệu (như password, file) vào Body của Request.*

**Câu 47:** Hệ thống tên miền (DNS) được tổ chức theo kiến trúc nào?
A. Cơ sở dữ liệu tập trung (Centralized Database) tại 1 máy chủ duy nhất.
B. Mạng ngang hàng P2P không có phân cấp.
C. Cơ sở dữ liệu phân tán theo cấu trúc phân cấp (Hierarchical Distributed Database).
D. Chuỗi khối (Blockchain).
*Đáp án: C*
*Giải thích: Để tránh trở thành nút cổ chai (bottleneck) hay điểm chết tập trung (single point of failure) của toàn thế giới, DNS tổ chức dạng cây: Root DNS -> TLD DNS (.com, .net) -> Authoritative DNS.*

**Câu 48:** Các máy chủ DNS quản lý cấp cao nhất (Root DNS servers) có chức năng gì?
A. Chứa địa chỉ IP của tất cả các trang web trên thế giới.
B. Cung cấp địa chỉ IP của các máy chủ quản lý tên miền mức cao nhất (TLD servers) như .com, .org, .edu.
C. Trực tiếp phục vụ các truy vấn từ máy tính cá nhân.
D. Đóng vai trò là tường lửa cho mạng Internet.
*Đáp án: B*
*Giải thích: Root Server chỉ làm nhiệm vụ "chỉ đường". Nếu bạn hỏi ".com", nó sẽ bảo "tôi không rõ www.google.com, nhưng đây là địa chỉ của máy chủ quản lý đuôi .com, hãy sang đó hỏi".*

**Câu 49:** TLD (Top-Level Domain) servers quản lý những tên miền nào?
A. Tên miền gốc (Root).
B. Tên miền cao cấp như .com, .net, .org và các tên miền quốc gia như .vn, .jp.
C. Tên miền phụ (Subdomain) như mail.google.com.
D. Tên miền nội bộ trong LAN.
*Đáp án: B*
*Giải thích: Tổ chức quản lý .com TLD server sẽ giữ danh sách địa chỉ các máy chủ có thẩm quyền (Authoritative) của từng công ty mua tên miền (ví dụ google.com).*

**Câu 50:** Máy chủ DNS có thẩm quyền (Authoritative DNS server) là gì?
A. Máy chủ DNS do ISP cung cấp để truy vấn hộ người dùng.
B. Máy chủ DNS do tổ chức sở hữu tên miền tự duy trì (hoặc thuê), chứa bản ghi IP thật (A record) gắn với tên miền của tổ chức đó (ví dụ mail.yahoo.com).
C. Máy chủ ảo trên Cloud.
D. Root Server.
*Đáp án: B*
*Giải thích: Đây là điểm đến cuối cùng của chuỗi tra cứu DNS. Nếu bạn sở hữu "cty-toi.vn", bạn phải cấu hình máy chủ này để nói cho thế giới biết IP máy chủ web của "cty-toi.vn" là bao nhiêu.*

**Câu 51:** Truy vấn DNS đệ quy (Recursive Query) hoạt động như thế nào?
A. Máy khách gửi yêu cầu đến Local DNS, Local DNS sẽ lần lượt đi hỏi Root, TLD, và Authoritative thay cho máy khách, sau đó trả kết quả cuối cùng về.
B. Local DNS trả về địa chỉ của máy chủ khác để máy khách tự đi hỏi tiếp.
C. Máy khách tự kết nối đồng thời đến hàng ngàn máy chủ DNS.
D. Yêu cầu sẽ quay ngược lại nếu máy chủ bận.
*Đáp án: A*
*Giải thích: Đệ quy là "giao khoán" công việc. Máy khách khoán cho Local DNS Server (của ISP). Local DNS Server sẽ vất vả đi tìm (bằng phương pháp lặp - iterative) và báo kết quả cuối cho client.*

**Câu 52:** Mục đích của việc lưu bộ nhớ đệm (DNS Caching) tại Local DNS server là gì?
A. Giúp tăng dung lượng ổ cứng của server.
B. Giảm độ trễ cho người dùng và giảm lưu lượng truy vấn lên các máy chủ Root/TLD.
C. Ngăn chặn người dùng truy cập các web xấu.
D. Thay thế địa chỉ MAC.
*Đáp án: B*
*Giải thích: Nếu một người vừa vào vnexpress.net, Local DNS sẽ nhớ IP đó. Khi người khác cũng hỏi vnexpress.net, nó trả lời ngay từ cache mà không cần đi hỏi vòng quanh thế giới nữa.*

**Câu 53:** Bản ghi (Resource Record - RR) loại 'A' trong DNS chứa thông tin gì?
A. Cặp (Tên miền, Địa chỉ IPv6).
B. Cặp (Tên miền, Tên bí danh).
C. Cặp (Tên miền, Địa chỉ IPv4).
D. Cặp (Tên miền, Tên máy chủ Mail).
*Đáp án: C*
*Giải thích: Record Type A (Address) ánh xạ Hostname (ví dụ: relay1.bar.foo.com) thành địa chỉ IPv4 (ví dụ: 145.37.93.126).*

**Câu 54:** Bản ghi loại 'CNAME' (Canonical Name) trong DNS dùng để làm gì?
A. Chứa IP của máy chủ.
B. Tạo bí danh (Alias), trỏ một tên miền này (ví dụ: www.ibm.com) sang tên miền chính tắc (ví dụ: servereast.backup2.ibm.com).
C. Trỏ đến tên miền của máy chủ quản lý thư (Mail Server).
D. Chứa địa chỉ IPv6.
*Đáp án: B*
*Giải thích: CNAME rất hữu ích khi các dịch vụ (như web, ftp) cùng chạy trên 1 server. CNAME giúp nhóm các tên phụ trỏ về 1 tên chính (A record).*

**Câu 55:** Giao thức phân phối nội dung video phổ biến hiện nay (như trên YouTube, Netflix) là HTTP Streaming (DASH). DASH là viết tắt của:
A. Dynamic Audio/Video Streaming over HTTP
B. Direct Access to Streaming Host
C. Dynamic Adaptive Streaming over HTTP
D. Data Allocation System for HTTP
*Đáp án: C*
*Giải thích: DASH cho phép video được cắt thành nhiều chunk nhỏ, mỗi chunk có nhiều độ phân giải khác nhau (1080p, 720p). Trình duyệt (Client) tự động đo băng thông hiện tại để tải chunk có chất lượng phù hợp (Adaptive).*

**Câu 56:** Ứng dụng P2P BitTorrent quản lý nhóm các peers (máy khách) đang tải chung một file thông qua cơ chế nào?
A. Máy chủ Web trung tâm.
B. Máy chủ DNS.
C. Tracker (Máy theo dõi).
D. Router lõi.
*Đáp án: C*
*Giải thích: Tracker là một máy chủ cơ sở dữ liệu giữ danh sách địa chỉ IP của các peers hiện đang tham gia chia sẻ một file (torrent) cụ thể, giúp các peers mới tìm thấy nhau.*

**Câu 57:** Trong BitTorrent, chính sách "tit-for-tat" (Có qua có lại) được áp dụng để giải quyết vấn đề gì?
A. Vấn đề vi phạm bản quyền.
B. Vấn đề các peer chỉ muốn tải xuống mà không chịu tải lên (Free-riding).
C. Vấn đề băng thông thấp của cáp đồng.
D. Vấn đề mã hóa gói tin.
*Đáp án: B*
*Giải thích: Thuật toán choking (bóp nghẹt): Một peer thường chỉ gửi data cho 4 peers nào đang gửi data cho nó với tốc độ nhanh nhất. Nếu bạn không upload, bạn sẽ không được ai gửi data.*

**Câu 58:** Cấu trúc thông điệp email bao gồm 2 phần cơ bản theo chuẩn RFC 5322 là:
A. Header và Body (Thân thư).
B. Tên miền và IP.
C. Dữ liệu nén và mã giải nén.
D. Source Port và Destination Port.
*Đáp án: A*
*Giải thích: Header chứa các dòng `To:`, `From:`, `Subject:`. Body chứa thông điệp thực sự ở dạng text (ASCII).*

**Câu 59:** Vì sao chuẩn MIME (Multipurpose Internet Mail Extensions) được ra đời để bổ sung cho giao thức Email?
A. Để tăng tốc độ chuyển thư.
B. Vì SMTP ban đầu CHỈ có khả năng truyền ký tự văn bản chuẩn (ASCII 7-bit); MIME giúp email có thể gửi các ký tự quốc tế, file đính kèm (ảnh, word, mp3) bằng cách mã hoá chúng về ASCII.
C. Để mã hóa bảo mật chống đọc trộm.
D. Để thay thế hoàn toàn TCP bằng UDP.
*Đáp án: B*
*Giải thích: Các file nhị phân (binary) như ảnh JPEG không thể nhét trực tiếp vào SMTP cổ điển. MIME dùng phương pháp như Base64 để đổi nhị phân sang các ký tự chữ cái an toàn trước khi đẩy vào SMTP.*

**Câu 60:** Một máy chủ CDN (Content Delivery Network) giải quyết khó khăn gì cho các ứng dụng xem video streaming toàn cầu?
A. Nó miễn phí toàn bộ cước Internet cho người dùng.
B. Khắc phục việc một máy chủ duy nhất bị quá tải và độ trễ quá cao đối với người dùng ở xa nửa vòng trái đất bằng cách phân phối bản sao video đến gần người dùng nhất.
C. Nó mã hóa video thành định dạng không thể vi phạm bản quyền.
D. Thay đổi địa chỉ MAC của người dùng.
*Đáp án: B*
*Giải thích: Khoảng cách địa lý tạo ra độ trễ. CDN rút ngắn khoảng cách mạng (network distance) bằng cách đặt Edge Server vào các ISP của từng quốc gia.*

**Câu 61:** Lệnh `nslookup` hoặc `dig` trong Command Prompt được sử dụng chủ yếu để tương tác với dịch vụ nào?
A. HTTP
B. FTP
C. DNS
D. DHCP
*Đáp án: C*
*Giải thích: Các lệnh này dùng để truy vấn trực tiếp vào hệ thống DNS (VD: xin bản ghi MX, bản ghi A của một tên miền) nhằm gỡ lỗi mạng.*

**Câu 62:** Các ứng dụng mạng hiện đại thường sử dụng mã hóa ở tầng ứng dụng hoặc tầng giao vận. Ví dụ của giao thức mã hóa hoạt động "nằm giữa" Tầng ứng dụng và Tầng giao vận TCP là gì?
A. SSL/TLS (Secure Sockets Layer / Transport Layer Security)
B. IPSec
C. WPA2
D. HTTP
*Đáp án: A*
*Giải thích: TLS cung cấp một "Socket an toàn" (Secure Socket). Giao thức ứng dụng (như HTTPS) đẩy dữ liệu thô vào TLS, TLS mã hóa rồi đẩy xuống TCP Socket.*

**Câu 63:** Một đặc điểm chung của các ứng dụng mạng là chúng được thiết kế để chạy trên:
A. Các bộ chuyển mạch lõi (Core Switches).
B. Các bộ định tuyến biên (Edge Routers).
C. Các hệ thống đầu cuối (End Systems / Hosts) như PC, Smartphone, Server.
D. Cáp sợi quang học.
*Đáp án: C*
*Giải thích: Các ứng dụng không chạy trên thiết bị trung tâm (Router/Switch - chúng chỉ làm nhiệm vụ dẫn đường ở Tầng 3 trở xuống). Mọi tiến trình xử lý nằm ở viền của mạng (Hosts).*

**Câu 64:** Mối quan hệ giữa "Process" (Tiến trình) và "Program" (Chương trình) là gì?
A. Chúng là một và hoàn toàn giống nhau.
B. Process là một Program đang trong quá trình thực thi trên máy tính; nhiều Process có thể cùng chạy chung một Program.
C. Process là phần cứng, Program là phần mềm.
D. Program là giao thức, Process là dữ liệu.
*Đáp án: B*
*Giải thích: Program chỉ là các dòng code nằm tĩnh trên ổ cứng (như file chrome.exe). Khi bạn click đúp chạy nó, hệ điều hành nạp nó lên RAM, nó trở thành một Process.*

**Câu 65:** Định danh (Identifier) nào mà một máy tính sử dụng để nhận biết và đẩy dữ liệu nhận từ mạng lên đúng Tiến trình (Process) ứng dụng?
A. Địa chỉ IP.
B. Tên miền.
C. Địa chỉ MAC.
D. Số Port (Cổng).
*Đáp án: D*
*Giải thích: Có thể có cả tiến trình Web và Mail cùng chạy trên 1 máy có cùng 1 IP. OS nhìn vào Port đích (vd: 80 -> Web, 25 -> Mail) để gõ cửa giao dữ liệu.*

**Câu 66:** Port number (Số hiệu cổng) có cấu trúc độ dài bao nhiêu bit?
A. 8 bit (0 - 255)
B. 16 bit (0 - 65,535)
C. 32 bit
D. 48 bit
*Đáp án: B*
*Giải thích: Số cổng dài 16 bit. Từ 0-1023 là "Well-known ports" dành cho các dịch vụ chuẩn quốc tế (HTTP, FTP...).*

**Câu 67:** Khi trình duyệt gửi Request bằng phương thức HTTP GET, tham số (parameters) của yêu cầu (ví dụ từ khóa tìm kiếm) thường được đặt ở đâu?
A. Ẩn bên trong Body của HTTP Request.
B. Mã hóa thành một file đính kèm.
C. Gắn trực tiếp nối tiếp vào cuối URL (Ví dụ: `?q=mang+may+tinh`).
D. Trong trường Cookie.
*Đáp án: C*
*Giải thích: Phương thức GET để lộ dữ liệu form trên thanh địa chỉ, do đó không bao giờ được dùng GET để gửi mật khẩu (dù có mã hóa HTTPS thì cũng lộ ở lịch sử duyệt web).*

**Câu 68:** HTTP/2.0 cải thiện một vấn đề lớn của HTTP/1.1 bằng cách nào?
A. Bỏ hoàn toàn TCP chuyển sang UDP.
B. Xóa bỏ trường Header.
C. Cho phép ghép kênh (Multiplexing) - gửi nhiều yêu cầu (request/response) đồng thời trên cùng MỘT kết nối TCP duy nhất, khắc phục hiện tượng Head-of-Line blocking ở mức ứng dụng.
D. Bắt buộc nén file thành .zip.
*Đáp án: C*
*Giải thích: HTTP/1.1 (pipeline) vẫn gửi/nhận theo thứ tự (tuần tự), ảnh lớn mắc kẹt làm JS nhỏ phải chờ. HTTP/2 cắt nhỏ thành các frame nhị phân, xen kẽ tải song song cùng lúc.*

**Câu 69:** Các máy chủ Email sử dụng tập hợp các lệnh nào để giao tiếp (ví dụ: HELO, MAIL FROM, RCPT TO, DATA)?
A. HTTP
B. FTP
C. POP3
D. SMTP
*Đáp án: D*
*Giải thích: Đây là các command chuẩn bằng văn bản thuần túy (ASCII) của giao thức gửi thư SMTP (RFC 5321).*

**Câu 70:** Một trong những lợi ích lớn nhất của việc thiết kế DNS thành mô hình phân tán là:
A. Tăng tính dễ bị tổn thương trước tấn công DDoS tại một điểm.
B. Máy chủ dễ quản lý và bảo trì hơn.
C. Tránh tình trạng sập toàn hệ thống mạng nếu một máy chủ gặp sự cố (Single point of failure).
D. Giảm số lượng tên miền có thể đăng ký.
*Đáp án: C*
*Giải thích: Nếu toàn bộ mạng dùng 1 cái máy tính duy nhất phân giải IP, khi máy tính đó đứt cáp, toàn bộ Internet sẽ "mù đường" không truy cập được web.*

**Câu 71:** Ứng dụng "Skype" nổi tiếng với việc kết hợp kiểu kiến trúc mạng nào trong những ngày đầu phát triển?
A. Chỉ thuần túy Client-Server.
B. Kiến trúc P2P lai (Hybrid P2P) - dùng một số máy khách mạnh (Super Node) làm máy chủ chuyển tiếp danh bạ và lưu lượng cho các máy yếu hơn.
C. Mạng dạng vòng (Token Ring).
D. Chuyển mạch kênh (Circuit Switching) truyền thống.
*Đáp án: B*
*Giải thích: Skype ban đầu tận dụng các máy tính mạnh của chính người dùng (Super Nodes) để làm đường kết nối định tuyến thoại, giúp giảm tải hoàn toàn chi phí máy chủ trung tâm.*

**Câu 72:** Tầng Application trong bộ giao thức TCP/IP bao gồm các chức năng tương đương với những tầng nào trong mô hình OSI?
A. Application, Presentation, Session.
B. Application, Transport, Network.
C. Transport, Session.
D. Application, Data Link.
*Đáp án: A*
*Giải thích: Do tính chất linh hoạt, TCP/IP thiết kế gộp (hoặc để ngỏ) việc kiểm soát định dạng dữ liệu (Presentation) và quản lý phiên (Session) cho chính các nhà lập trình ứng dụng tự xử lý bên trong Application Layer.*

**Câu 73:** Trong giao thức truyền tệp FTP (File Transfer Protocol), khác biệt cơ bản nhất về cách quản lý kết nối TCP so với HTTP là gì?
A. FTP dùng kết nối UDP.
B. FTP chỉ dùng một cổng kết nối duy nhất là Port 80.
C. FTP thiết lập HAI kết nối TCP riêng biệt: Một kết nối điều khiển (Control connection - Port 21) để gửi lệnh và một kết nối dữ liệu (Data connection - Port 20) để truyền file.
D. Không có khác biệt.
*Đáp án: C*
*Giải thích: Cơ chế này được gọi là Out-of-band control. Lệnh (như dir, get) chạy trên đường 21 độc lập với luồng data khổng lồ tải trên đường 20, giúp server không bị kẹt nhận lệnh khi đang tải file.*

**Câu 74:** Dịch vụ nào dựa trên giao thức tầng ứng dụng thường yêu cầu lưu lượng (throughput) ĐÀN HỒI (Elastic) thay vì YÊU CẦU BĂNG THÔNG TỐI THIỂU (Bandwidth guarantee)?
A. Video Streaming HD (như Netflix).
B. Cầu truyền hình (Video Conferencing).
C. Chuyển tệp tin (File transfer/FTP) và Email.
D. Gọi điện thoại VoIP.
*Đáp án: C*
*Giải thích: Tải file hay email có được băng thông bao nhiêu cũng tốt, nhanh thì xong sớm, chậm thì xong muộn, không bị "giật lag" hay vô dụng như gọi thoại/video nếu thiếu băng thông.*

**Câu 75:** Tại sao tấn công DDoS thường hay nhắm vào các máy chủ DNS gốc (Root Servers)?
A. Để cướp tiền từ thẻ tín dụng của khách hàng.
B. Vì các Root Server có mật khẩu yếu.
C. Nếu làm sập hoặc làm chậm Root Server, toàn bộ cơ chế phân giải tên miền bị ngưng trệ, khiến một vùng hoặc toàn bộ Internet không thể truy cập bằng tên (như một cuộc tấn công vào "bản đồ" Internet).
D. Để ăn cắp mã nguồn của Windows.
*Đáp án: C*
*Giải thích: Tấn công làm sập DNS Root là tấn công vào trái tim của mạng. Tuy nhiên, hệ thống Root hiện tại có hệ thống Anycast và bộ đệm (Cache) đồ sộ giúp giảm thiểu rủi ro này rất nhiều.*

**Câu 76:** Ứng dụng Telnet gửi dữ liệu bằng định dạng nào qua đường truyền?
A. Mã hóa AES-256.
B. Tín hiệu Analog.
C. Ký tự văn bản thuần (Clear-text / ASCII), dễ bị đọc trộm bằng sniffer.
D. Giao thức nhị phân nén.
*Đáp án: C*
*Giải thích: Do lỗ hổng bảo mật nghiêm trọng (mật khẩu bị phơi bày), Telnet hiện nay hầu hết được thay thế bằng SSH (Secure Shell) sử dụng mã hóa.*

**Câu 77:** Để một trang web hiển thị các file video, ảnh, audio, HTTP sử dụng trường Header nào trong gói tin Response để báo cho Trình duyệt biết loại tệp nó đang nhận là gì (để chọn phần mềm mở cho đúng)?
A. User-Agent
B. Content-Length
C. Content-Type (Ví dụ: text/html, image/jpeg)
D. Cache-Control
*Đáp án: C*
*Giải thích: Header Content-Type là ứng dụng của chuẩn MIME, giúp Browser không hiển thị các ký tự vô nghĩa khi nhận một file ảnh mà sẽ hiển thị thành hình ảnh.*

**Câu 78:** Mạng P2P "BitTorrent" giải quyết "Hiện tượng nghẽn cổ chai" (Flash Crowd - một tệp đột nhiên có hàng triệu người tải cùng lúc) rất tốt vì:
A. Server trung tâm sẽ tự động mua thêm RAM.
B. Mỗi người tải một mảng tệp tin về sẽ ngay lập tức trở thành một nguồn phát mảng đó cho người đến sau, tổng băng thông phục vụ (upload capacity) TĂNG theo số lượng người dùng.
C. Torrent nén file xuống còn 1% kích thước ban đầu.
D. Torrent chặn tải khi có quá 100 người dùng.
*Đáp án: B*
*Giải thích: Đây là sức mạnh của P2P. Trái với Client-Server (càng đông càng chậm do server quá tải), P2P càng đông thì nguồn cung (seeders/peers upload) càng lớn, tốc độ tải có thể càng nhanh.*

**Câu 79:** Dịch vụ "Dynamic DNS" (DDNS) dùng để làm gì?
A. Tránh bị tấn công DDoS.
B. Tự động mã hóa truy vấn DNS.
C. Cập nhật tự động (ánh xạ) một tên miền cố định trỏ về một địa chỉ IP WAN thường xuyên bị thay đổi (IP động) của người dùng gia đình (ví dụ khi lắp camera tại nhà).
D. Cấp IP nội bộ cho máy tính.
*Đáp án: C*
*Giải thích: Các ISP thường cấp IP động cho hộ gia đình (reset modem là đổi IP). Nếu bạn muốn truy cập camera ở nhà qua một tên miền, DDNS sẽ giúp tự động cập nhật bản ghi khi IP đổi.*

**Câu 80:** "User-Agent" trong HTTP Request header cung cấp cho Web Server thông tin gì?
A. Mật khẩu của người dùng.
B. Địa chỉ IP của Proxy.
C. Tên và phiên bản của Trình duyệt Web (Browser) và Hệ điều hành mà máy khách đang sử dụng.
D. Thông tin định tuyến của gói tin.
*Đáp án: C*
*Giải thích: Server dùng User-Agent (VD: Mozilla/5.0... iPhone... Safari) để phản hồi phiên bản trang web phù hợp (phiên bản Mobile hay Desktop).*

**Câu 81:** Khái niệm "Web Socket" xuất hiện trong HTML5 giúp giải quyết vấn đề gì của HTTP truyền thống?
A. Vấn đề nén ảnh.
B. Mở ra một kết nối TCP duy trì liên tục, cho phép giao tiếp hai chiều (Full-duplex), Server có thể chủ động "đẩy" (Push) dữ liệu về Client mà không cần Client phải gửi Request hỏi liên tục (Polling).
C. Ngăn chặn Cookie.
D. Mã hóa video 4K.
*Đáp án: B*
*Giải thích: Các ứng dụng chat thời gian thực, bảng giá chứng khoán dùng Web Socket rất hiệu quả, vì không phải liên tục gửi các Request trống rỗng để hỏi "Có tin mới chưa?".*

**Câu 82:** "Authoritative DNS Server" (Máy chủ có thẩm quyền) của một trường Đại học phải chứa bản ghi gì để cho phép thế giới gửi Email đến hòm thư `sv@daihoc.edu.vn`?
A. Bản ghi A
B. Bản ghi CNAME
C. Bản ghi MX (Mail Exchanger)
D. Bản ghi NS (Name Server)
*Đáp án: C*
*Giải thích: Bản ghi MX trỏ tên miền (daihoc.edu.vn) sang tên máy chủ quản lý thư (ví dụ mail.daihoc.edu.vn). Sau đó bản ghi A sẽ dịch mail.daihoc.edu.vn sang IP để SMTP gửi đến.*

**Câu 83:** Sự khác biệt giữa mô hình P2P "Tập trung" (như Napster đời đầu) và "Phân tán hoàn toàn" (như Gnutella hay BitTorrent dùng DHT) là gì?
A. P2P tập trung chỉ chạy trên LAN.
B. P2P tập trung sử dụng MỘT máy chủ cơ sở dữ liệu làm nơi chỉ mục tìm kiếm (như sổ danh bạ) để tìm ai giữ file; P2P phân tán loại bỏ hoàn toàn máy chủ này, việc tìm kiếm dựa trên thuật toán hỏi lan truyền.
C. P2P phân tán phải dùng máy chủ DNS của Google.
D. Không có khác biệt.
*Đáp án: B*
*Giải thích: Napster sụp đổ vì máy chủ trung tâm giữ danh bạ bị kiện và rút phích cắm. Các thế hệ P2P sau dùng DHT (Distributed Hash Table) để rải sổ danh bạ cho tất cả các máy khách.*

**Câu 84:** "Mã phản hồi" (Response Status Code) 301 Moved Permanently trong HTTP có ý nghĩa gì đối với trình duyệt?
A. Yêu cầu đăng nhập lại.
B. Tài nguyên (URL) đã bị xóa vĩnh viễn khỏi Server.
C. Tài nguyên đã được chuyển vị trí cố định sang một URL mới (được cung cấp trong Header `Location`); Trình duyệt nên tự động chuyển hướng sang URL mới.
D. Máy chủ đang bận, xin thử lại sau.
*Đáp án: C*
*Giải thích: 301 dùng rất nhiều cho SEO (Tối ưu tìm kiếm) khi thay đổi cấu trúc tên miền, giúp không bị mất "bookmark" của người dùng cũ.*

**Câu 85:** Khi thiết kế một ứng dụng Game Online thời gian thực đòi hỏi phản hồi chuyển động nhân vật tính bằng mili-giây, lập trình viên nên chọn giao thức nào để truyền dữ liệu tọa độ?
A. TCP với Persistent HTTP.
B. FTP.
C. UDP.
D. SMTP.
*Đáp án: C*
*Giải thích: Toạ độ nhân vật gửi đi liên tục (ví dụ 60 lần/giây). Nếu mất 1 gói, nhân vật chỉ khựng 1/60s. Nếu dùng TCP, khi rớt gói, TCP sẽ bắt dòng game "đứng im" để đợi gói tin được phát lại -> giật lag kinh hoàng.*

**Câu 86:** Giao thức SMTP sử dụng phương thức truyền thống nào để giao tiếp giữa client và server?
A. Đẩy (Push)
B. Kéo (Pull)
C. Đồng bộ hóa mảng (Array Sync)
D. Giao tiếp UDP
*Đáp án: A*
*Giải thích: SMTP là một giao thức PUSH (bạn viết thư xong, đẩy nó vào khe cửa máy chủ bưu điện). HTTP hoặc POP3 là PULL (bạn mở hòm thư, lôi thư về nhà).*

**Câu 87:** Khi người dùng gửi một bức ảnh qua hệ thống Email dùng SMTP, điều gì diễn ra ngầm ở tầng Ứng dụng?
A. Bức ảnh bị nén thành file zip.
B. Giao thức chuyển sang dùng FTP tự động.
C. Bức ảnh nhị phân được mã hóa theo chuẩn Base64 của MIME thành một chuỗi các ký tự ASCII, sau đó gắn vào Body thư và gửi đi, người nhận sẽ giải mã chuỗi đó thành ảnh.
D. Bức ảnh được chia nhỏ và gửi qua UDP.
*Đáp án: C*
*Giải thích: SMTP là giao thức ASCII 7-bit cũ kỹ. Nó không hiểu byte ảnh (có thể chứa ký tự điều khiển ngẫu nhiên làm hỏng cấu trúc lệnh), nên Base64 biến nhị phân thành các ký tự A-Z, 0-9 an toàn.*

**Câu 88:** Thuật ngữ "API" (Application Programming Interface) thường gặp trong dịch vụ Web hiện đại đóng vai trò gì?
A. Cổng vật lý cắm cáp quang.
B. Quy tắc để mã hóa MAC address.
C. Tập hợp các hàm, giao thức và công cụ chuẩn hóa cho phép các phần mềm/ứng dụng khác nhau giao tiếp và trao đổi dữ liệu với nhau (Ví dụ RESTful API qua HTTP).
D. Tên gọi khác của IPv6.
*Đáp án: C*
*Giải thích: Web không chỉ cho người xem (HTML), mà ngày nay còn thiết kế các API (JSON/XML) để App điện thoại hay máy chủ của công ty khác gọi tới lấy dữ liệu tự động.*

**Câu 89:** Một "Socket" TCP được định danh duy nhất (Uniquely identified) ở hệ điều hành thông qua bộ 4 thông số (4-tuple) nào?
A. IP nguồn, IP đích, Địa chỉ MAC, Tên miền.
B. IP đích, Port đích, Địa chỉ MAC.
C. IP nguồn (Source IP), Port nguồn (Source Port), IP đích (Destination IP), Port đích (Destination Port).
D. Giao thức, Phiên bản, MTU, Tốc độ truyền.
*Đáp án: C*
*Giải thích: 4 thông số này (cộng với giao thức là TCP) giúp máy chủ Web phân biệt được 1000 người cùng đang xem trang web (mọi người đều có IP đích và Port đích là máy chủ 80, nhưng IP nguồn và Port nguồn của 1000 người là khác nhau).*

**Câu 90:** Giao thức nào cung cấp cấu trúc cho việc phân giải địa chỉ MAC thành địa chỉ IP, nhưng LẠI KHÔNG NẰM TRONG TẦNG ỨNG DỤNG?
A. DNS
B. ARP
C. HTTP
D. FTP
*Đáp án: B*
*Giải thích: Mặc dù ARP phân giải IP (L3) sang MAC (L2), nó hoạt động ở ranh giới giữa tầng Mạng và Liên kết (trong LAN), không phải là ứng dụng giao tiếp với người dùng như DNS.*

**Câu 91:** Sự khác biệt giữa mạng ngang hàng P2P "thuần túy" và cấu trúc lai (Hybrid) là:
A. P2P thuần túy chỉ dùng cáp quang.
B. P2P thuần túy không có bất kỳ máy chủ (server) thường trực nào, mọi node đều bình đẳng. Cấu trúc lai có một máy chủ trung tâm để lưu chỉ mục hoặc điều phối kết nối.
C. Mạng lai bắt buộc phải dùng IPv6.
D. P2P thuần túy nhanh hơn nhiều so với P2P lai.
*Đáp án: B*
*Giải thích: Ví dụ Gnutella là thuần túy (không máy chủ). Napster là lai (có máy chủ giữ danh bạ). BitTorrent thực tế cũng lai vì nó cần có Tracker Server để máy khách tìm nhau lúc ban đầu.*

**Câu 92:** Tính năng "Cookie" có nguy cơ về quyền riêng tư (Privacy) vì lý do nào?
A. Cookie chứa mã độc lây lan virus.
B. Cookie cho phép máy chủ theo dõi thói quen duyệt web của người dùng, phân tích hành vi và bán dữ liệu cho các công ty quảng cáo (Ví dụ: Third-party cookies).
C. Cookie xoá các dữ liệu quan trọng trong máy.
D. Cookie tự động tắt trình duyệt.
*Đáp án: B*
*Giải thích: Cookie "bên thứ 3" (được nhúng từ các mạng quảng cáo trên nhiều web khác nhau) có thể theo vết bạn trên khắp Internet để hiển thị quảng cáo theo ngữ cảnh.*

**Câu 93:** Hệ thống DNS chống lại độ trễ mạng bằng cách sử dụng cơ chế nào phổ biến nhất?
A. Định tuyến đa điểm (Multicasting) trên toàn cầu.
B. Gửi dữ liệu nén.
C. Lưu bộ đệm (Caching) ở nhiều cấp độ (Trình duyệt, Máy tính, Router mạng LAN, Local DNS Server) để phân giải tên miền ngay lập tức mà không cần truy vấn ra Internet.
D. Tăng băng thông cáp quang.
*Đáp án: C*
*Giải thích: Hầu hết các tên miền bạn truy cập hàng ngày (google, facebook) đều đã được lưu trong bộ nhớ đệm (Cache) của máy tính hoặc nhà mạng, nên bạn không cảm nhận được độ trễ DNS.*

**Câu 94:** Thời gian RTT (Round Trip Time) trong giao thức HTTP đóng vai trò gì trong việc thiết lập một phiên giao dịch web đơn giản (HTTP/1.0 không dùng persistent)?
A. RTT không ảnh hưởng đến HTTP.
B. 1 RTT để thiết lập TCP, 1 RTT để gửi Request và nhận Response, tổng cộng ít nhất là 2 RTT mới lấy được một đối tượng nhỏ (như file HTML).
C. Nó là thời gian để nén file.
D. Là thời gian trình duyệt phân tích mã HTML.
*Đáp án: B*
*Giải thích: Với độ trễ mạng là 100ms (1 chiều, 2 chiều RTT=200ms). Bắt tay TCP mất 200ms, sau đó HTTP Get mất 200ms nữa. Do đó trễ mạng có tác động cực lớn đến tải trang.*

**Câu 95:** Trong HTTP, trường Header `Host:` (được thêm từ HTTP/1.1) giải quyết vấn đề gì trên các Web Server hiện đại?
A. Vấn đề mật khẩu yếu.
B. Nó chỉ định Tên miền mà máy khách muốn truy cập, cho phép một máy chủ (một IP duy nhất) có thể lưu trữ và phục vụ hàng trăm Website khác nhau (Shared/Virtual Hosting).
C. Nó mã hóa thân trang web.
D. Chứa địa chỉ MAC của Host.
*Đáp án: B*
*Giải thích: Rất nhiều trang web nhỏ thuê chung 1 máy chủ (chung 1 IP). Khi Request bay đến IP đó, máy chủ phải nhìn vào Header `Host: web-cua-toi.com` để mở đúng thư mục mã nguồn.*

**Câu 96:** Dịch vụ nào dưới đây là ví dụ điển hình của ứng dụng sử dụng mô hình Client-Server?
A. Chia sẻ file qua giao thức BitTorrent.
B. Truy cập một trang tin tức qua trình duyệt Web.
C. Đồng bộ hóa sổ cái trong mạng lưới tiền ảo Bitcoin.
D. Gọi điện thoại VoIP trực tiếp bằng một ứng dụng P2P.
*Đáp án: B*
*Giải thích: Trình duyệt luôn là Client (chủ động yêu cầu), Server báo chí (luôn bị động lắng nghe) chờ phản hồi.*

**Câu 97:** HTTP Message (Thông điệp HTTP) thuộc kiểu dữ liệu nào?
A. Văn bản dạng Text (đối với phần Header) theo chuẩn ASCII, con người có thể đọc được bằng phần mềm bắt gói tin (nếu không mã hóa).
B. Luôn luôn là dữ liệu nhị phân không thể đọc bằng mắt.
C. Luôn được mã hóa theo chuẩn Base64.
D. Chỉ chứa các tín hiệu Analog.
*Đáp án: A*
*Giải thích: Khác với các giao thức nhị phân (như HTTP/2), HTTP/1.1 có phần Header và Control bằng Text, mỗi dòng kết thúc bằng bộ ký tự Carriage Return / Line Feed (CRLF).*

**Câu 98:** Đặc tính "Out-of-band" của điều khiển trong giao thức FTP có nghĩa là:
A. Thiết bị không có ăng-ten để truyền sóng vô tuyến.
B. Lệnh và Dữ liệu được gửi chung trên một kênh để tiết kiệm.
C. Các thông điệp điều khiển (đăng nhập, tải file) được truyền trên một kết nối TCP riêng biệt (Port 21) so với dữ liệu thực tế (Port 20), tránh xung đột.
D. Mất điện thì FTP vẫn tải được file.
*Đáp án: C*
*Giải thích: So với HTTP (In-band) gửi Lệnh (GET) và Dữ liệu trên CÙNG một kết nối TCP, FTP (Out-of-band) tách hai việc đó sang hai "đường ống" khác nhau.*

**Câu 99:** Để ngăn chặn kẻ xấu đăng ký tất cả tên miền đẹp, ICANN đã phân bổ quyền bán/đăng ký tên miền cho:
A. Các ISP địa phương.
B. Các công ty Đăng ký Tên miền (Domain Registrars) được ủy quyền (như GoDaddy, Namecheap...).
C. Chính phủ các nước.
D. Quân đội.
*Đáp án: B*
*Giải thích: Registrars là các đại lý thương mại thu phí để đăng ký tên miền của bạn vào hệ thống CSDL gốc của TLD Server.*

**Câu 100:** Bạn đang xem một bộ phim Full HD trên Netflix. Giả sử đường truyền nhà bạn rớt mạng trong 5 giây, nhưng bộ phim trên tivi VẪN PHÁT BÌNH THƯỜNG không bị gián đoạn. Công nghệ nào đang hoạt động?
A. Cáp quang có khả năng tích điện.
B. TCP nén phim siêu việt.
C. Kỹ thuật Client Buffering (Lưu đệm phía máy khách).
D. Phim được truyền bằng vệ tinh.
*Đáp án: C*
*Giải thích: Ứng dụng xem video luôn tải trước một lượng dữ liệu (VD: 10 giây video tới) và cất vào Buffer trên RAM. Nhờ cái "hồ chứa" nhỏ này, các dao động nhỏ của mạng bị triệt tiêu, mang lại cảm giác mượt mà.*

**Câu 101:** Quá trình phân giải DNS (DNS Resolution) thường sử dụng cổng UDP mặc định nào?
A. 21
B. 25
C. 53
D. 80
*Đáp án: C*
*Giải thích: Port 53 được sử dụng trên cả UDP (cho truy vấn phân giải thường) và TCP (cho truyền tải dữ liệu vùng Zone transfer giữa các máy chủ DNS).*

**Câu 102:** "DASH" (Dynamic Adaptive Streaming over HTTP) yêu cầu máy khách (Client) phải thực hiện việc gì liên tục?
A. Thay đổi địa chỉ MAC mỗi 5 phút.
B. Giám sát băng thông hiện có và tình trạng bộ đệm để quyết định yêu cầu (HTTP GET) đoạn video chất lượng cao hay thấp cho vài giây tiếp theo.
C. Thiết lập lại kết nối TCP mỗi giây.
D. Xin cấp lại địa chỉ IP từ Router.
*Đáp án: B*
*Giải thích: Đặc tính "Thích ứng" (Adaptive) là do Client hoàn toàn chủ động, nếu mạng lag, client tự tải bản 480p, mạng ngon lại tự lấy bản 1080p, server chỉ bị động phục vụ.*

**Câu 103:** Một mạng máy tính P2P (như BitTorrent) khác với mô hình phân tán CDN ở chỗ:
A. CDN thuộc sở hữu và quản lý của một công ty (cơ sở hạ tầng chuyên dụng), P2P dựa vào nguồn lực phân tán của chính người dùng cuối tự nguyện đóng góp.
B. CDN dùng UDP, P2P dùng TCP.
C. CDN là miễn phí, P2P có phí.
D. Không có khác biệt.
*Đáp án: A*
*Giải thích: CDN (như Akamai) dùng hàng ngàn Server đắt tiền do họ mua và đặt khắp thế giới. Torrent dùng PC của người dùng ở nhà.*

**Câu 104:** Thuật ngữ "Socket API" do hệ điều hành nào đi tiên phong phát triển?
A. Windows
B. macOS
C. Unix/Berkeley (BSD Sockets)
D. Android
*Đáp án: C*
*Giải thích: Giao diện lập trình mạng (API) mà chúng ta đang dùng ngày nay bắt nguồn từ Berkeley Sockets trên HĐH Unix thập niên 80.*

**Câu 105:** Chức năng chính của giao thức DHCP trong mạng LAN là gì?
A. Phân giải tên miền.
B. Chuyển tiếp email nội bộ.
C. Cấp phát động địa chỉ IP, Subnet Mask, Default Gateway và IP của máy chủ DNS cho thiết bị khi chúng xin gia nhập mạng.
D. Tạo mã hóa WPA2 cho Wi-Fi.
*Đáp án: C*
*Giải thích: Thay vì phải gõ tay tĩnh từng IP cho điện thoại, PC (rất dễ trùng lặp), Router đóng vai trò máy chủ DHCP sẽ lo việc quản lý kho IP tự động.*

**Câu 106:** Một giao thức Application (tầng ứng dụng) TỰ ĐỊNH NGHĨA (Proprietary protocol) là:
A. Giao thức đã được chuẩn hóa bởi RFC (như HTTP).
B. Giao thức do một công ty tự tạo ra cho ứng dụng riêng của họ (ví dụ Skype, Zoom), không công khai cấu trúc cho thế giới biết.
C. Giao thức chỉ chạy trên phần cứng cụ thể.
D. Giao thức không sử dụng port.
*Đáp án: B*
*Giải thích: Không phải mọi ứng dụng đều dùng HTTP hay SMTP mở. Nhiều công ty tạo giao thức đóng để bảo mật, tối ưu, độc quyền.*

**Câu 107:** Bản ghi MX (Mail Exchanger) trong hệ thống DNS phải luôn đi kèm với bản ghi nào để hoàn tất quá trình định vị?
A. CNAME Record
B. TXT Record
C. A Record (Bản ghi A để dịch tên máy chủ Mail đó sang IP)
D. PTR Record
*Đáp án: C*
*Giải thích: Nếu MX bảo rằng "Mail server của cty.com là mail1.cty.com", thì SMTP sender phải hỏi tiếp "Thế IP của cái thằng mail1.cty.com là bao nhiêu?" thông qua bản ghi A.*

**Câu 108:** Kỹ thuật "Pipeline" trong HTTP/1.1 có mục đích gì?
A. Nén dữ liệu video truyền đi.
B. Gửi nhiều Request liên tiếp trên một kết nối TCP mà KHÔNG CẦN CHỜ phản hồi (Response) của Request trước về tới. Máy chủ sẽ trả Response theo đúng thứ tự.
C. Thay thế cáp bằng ống nước.
D. Biến đổi HTTP thành UDP.
*Đáp án: B*
*Giải thích: Tương tự như đặt hàng, thay vì đặt món A -> đợi lấy món A xong -> mới đặt món B (tốn thời gian chờ). Pipeline cho phép bạn đặt liên tục A,B,C và nhà bếp sẽ trả ra A,B,C.*

**Câu 109:** Trong P2P Torrent, một "Seeder" là ai?
A. Người chỉ tải xuống.
B. Người giám sát mạng.
C. Một thiết bị máy khách (peer) đã có TOÀN BỘ 100% tệp tin hoàn chỉnh và đang tiếp tục tải nó lên (upload) cho các peer khác.
D. Hacker.
*Đáp án: C*
*Giải thích: Leecher (Người hút máu) là người đang tải dở và chia sẻ mảnh vỡ. Khi tải xong 100%, Leecher biến thành Seeder.*

**Câu 110:** Giao thức nào ở tầng Application chuyên đảm trách việc đồng bộ thời gian (Time synchronization) giữa máy tính của bạn và các máy chủ chuẩn giờ quốc tế?
A. FTP
B. NTP (Network Time Protocol)
C. SNMP
D. DNS
*Đáp án: B*
*Giải thích: Đồng hồ Windows/Mac của bạn tự động chính xác từng giây là nhờ giao thức NTP chạy ngầm liên tục hỏi giờ các cụm máy chủ giờ chuẩn.*

**Câu 111:** Lệnh HTTP GET và HTTP HEAD khác nhau cơ bản ở điểm nào?
A. Không có khác biệt.
B. HEAD nhanh hơn GET do bỏ qua DNS.
C. HEAD yêu cầu máy chủ chỉ trả về các dòng Header (metadata, thông tin trạng thái, kích thước), tuyệt đối KHÔNG trả về thân dữ liệu (Body) như GET.
D. HEAD yêu cầu nhập mật khẩu.
*Đáp án: C*
*Giải thích: HEAD rất hữu dụng để kiểm tra xem một tệp lớn có thay đổi không, dung lượng bao nhiêu, có tồn tại không (dựa vào header) trước khi dùng GET để tải toàn bộ thân file xuống.*

**Câu 112:** Trạng thái "403 Forbidden" trong giao thức HTTP có nghĩa là:
A. Tệp tin không tồn tại.
B. Yêu cầu sai cú pháp.
C. Máy khách có thể giao tiếp với máy chủ, nhưng máy chủ từ chối cung cấp dữ liệu do vấn đề phân quyền (không có quyền truy cập).
D. Máy chủ đang tắt.
*Đáp án: C*
*Giải thích: Khác với 401 Unauthorized (yêu cầu đăng nhập), 403 nghĩa là dù bạn là ai (kể cả đã đăng nhập), bạn cũng không có quyền xem thư mục/tài nguyên này.*

**Câu 113:** Kiến trúc "RESTful API" sử dụng phương thức nào của HTTP để thực hiện chức năng "Tạo mới một bản ghi" (Create) trên máy chủ?
A. GET
B. HEAD
C. POST (hoặc đôi khi PUT)
D. DELETE
*Đáp án: C*
*Giải thích: REST là quy ước chuẩn hóa (GET: Đọc, POST: Tạo, PUT: Cập nhật, DELETE: Xóa) giúp các ứng dụng giao tiếp mạch lạc.*

**Câu 114:** Ứng dụng P2P sử dụng Distributed Hash Table (DHT) giải quyết vấn đề gì?
A. Mã hóa dữ liệu tuyệt đối an toàn.
B. Tìm xem máy khách nào đang giữ file mà KHÔNG CẦN sử dụng một Server Tracker trung tâm làm sổ cái.
C. Rút gọn địa chỉ IP.
D. Biến router thành switch.
*Đáp án: B*
*Giải thích: DHT chia sổ cái ra làm hàng triệu mảnh, mỗi máy khách giữ một đoạn sổ cái. Muốn tìm ai giữ file X, các máy tính dùng thuật toán toán học truyền tay nhau hỏi rất nhanh để tìm ra địa chỉ.*

**Câu 115:** Trong mạng phân phối nội dung (CDN), kỹ thuật nào khiến máy khách tự động được hướng (redirect) tới máy chủ CDN gần nhất thay vì máy chủ gốc?
A. Định tuyến bằng BGP Anycast.
B. Sự can thiệp của các Authoritative DNS Server do CDN kiểm soát, chúng trả về IP của máy chủ CDN địa phương thay vì IP máy chủ gốc.
C. Sử dụng công cụ FTP.
D. Cả A và B đều được dùng tùy hạ tầng.
*Đáp án: D*
*Giải thích: Khi bạn tìm IP của netflix.com, DNS của Netflix sẽ đo lường xem bạn đang ở VN, nó sẽ trả về IP của Server VN thay vì Mỹ.*

**Câu 116:** Quá trình "Base64 Encoding" dùng trong email thực chất là gì?
A. Kỹ thuật mã hóa mật khẩu không thể giải mã.
B. Kỹ thuật chuyển đổi các chuỗi nhị phân (8-bit bytes) thành một tập ký tự an toàn gồm 64 chữ cái/số có thể in ra (printable ASCII characters).
C. Kỹ thuật nhân IP lên 64 lần.
D. Chuẩn cáp mạng quang học mới.
*Đáp án: B*
*Giải thích: Do SMTP cũ chỉ dùng 7-bit ASCII, khi nhét 1 byte (8-bit) của ảnh vào sẽ làm gãy giao thức. Base64 chia khối 3 bytes (24 bit) thành 4 cụm 6-bit (mỗi cụm 1 ký tự ASCII) giúp truyền file nhị phân an toàn.*

**Câu 117:** Mật độ phân bổ của máy chủ CDN "Enter Deep" khác với "Bring Home" ở điểm nào?
A. Không có khác biệt.
B. Enter Deep (như Akamai) đặt hàng ngàn cụm Server nhỏ SÂU vào TẬN TRONG các ISP vùng/nhỏ; Bring Home (như Limelight) đặt ít cụm Server khổng lồ ở CÁC ĐIỂM NÚT TRUNG TÂM (IXP) kết nối nhiều ISP.
C. Enter deep là máy chủ vệ tinh, Bring home là máy chủ mặt đất.
D. Enter Deep dùng cáp đồng, Bring Home dùng cáp quang.
*Đáp án: B*
*Giải thích: Akamai muốn server ở thật gần người dùng (vào tận phòng máy của ISP VNPT, FPT), chi phí lớn. Các hãng khác tối ưu bằng cách cắm server vào điểm trung chuyển quốc gia (IXP).*

**Câu 118:** HTTP/3 (phiên bản mới nhất của HTTP) sử dụng giao thức giao vận (Transport) TỰ ĐỊNH NGHĨA (dựa trên UDP) nào để khắc phục hoàn toàn nhược điểm của TCP?
A. IPsec
B. QUIC (do Google phát triển)
C. FTP
D. SCTP
*Đáp án: B*
*Giải thích: TCP có độ trễ kết nối (3-way handshake) quá cao. QUIC dùng UDP làm nền tảng (không bắt tay phức tạp) và TỰ xây dựng lại tính tin cậy, bảo mật bên trong không gian User-space, giúp tải web cực nhanh.*

**Câu 119:** "Mail Access Protocol" (Giao thức truy cập thư) dùng để:
A. Chuyển thư từ máy của tôi đến máy chủ bưu điện.
B. Chuyển thư giữa các máy chủ bưu điện của Google và Yahoo.
C. Lấy (Kéo/Pull) thư từ máy chủ bưu điện (sau khi nó nằm trong hộp thư của tôi) về ứng dụng quản lý thư trên máy tính của tôi (như POP3, IMAP).
D. Gửi email hàng loạt (spam).
*Đáp án: C*
*Giải thích: Gửi dùng PUSH (SMTP). Nhận dùng PULL (POP3/IMAP).*

**Câu 120:** Dịch vụ nào trên mạng sử dụng giao thức SNMP (Simple Network Management Protocol)?
A. Đọc báo online.
B. Giám sát và cấu hình các thiết bị mạng từ xa (Router, Switch, Server) bởi các quản trị viên hệ thống.
C. Truyền thanh Radio.
D. Gửi SMS.
*Đáp án: B*
*Giải thích: SNMP (dùng UDP port 161) là công cụ chủ đạo của IT System Admin để thu thập số liệu (như RAM, CPU router đang tải bao nhiêu) hoặc gửi cảnh báo khi cáp đứt.*

**Câu 121:** Một giao dịch SMTP điển hình yêu cầu loại dữ liệu đầu vào nào để báo hiệu KẾT THÚC phần nội dung thư (Message Body)?
A. Gõ phím ESC.
B. Nhập chữ `END`.
C. Nhập một dấu chấm `.` đứng ĐƠN ĐỘC trên MỘT DÒNG DUY NHẤT kèm CRLF.
D. Đóng cửa sổ Command Prompt.
*Đáp án: C*
*Giải thích: Đây là quy ước cổ điển của SMTP (RFC 5321). Gõ `\r\n.\r\n` máy chủ sẽ hiểu là viết xong thư và cho phép gửi đi.*

**Câu 122:** Thuật ngữ "Port Forwarding" (Chuyển tiếp cổng) cấu hình trên Router gia đình có ý nghĩa gì đối với tầng Ứng dụng?
A. Làm router chạy nhanh hơn.
B. Yêu cầu Router khi nhận được gói tin (từ Internet) nhắm vào một Port X của Router (Public IP), thì chuyển hướng (Dịch NAT) gói tin đó vào một IP Private và Port cụ thể bên trong mạng LAN, giúp máy đó đóng vai trò làm Server phục vụ ra ngoài.
C. Đổi chuẩn Wi-Fi sang Bluetooth.
D. Khoá tất cả truy cập Internet.
*Đáp án: B*
*Giải thích: Do IP LAN bị ẩn sau NAT, người ngoài Internet không thấy máy chủ Web nhỏ bạn tự cài ở nhà. Port Forwarding tạo một "cánh cửa" xuyên tường NAT để người ngoài đi vào đúng máy bạn.*

**Câu 123:** Tại sao UDP phù hợp hơn TCP đối với các trò chơi nhập vai trực tuyến nhiều người chơi (MMORPG - có yếu tố chuyển động hành động nhanh)?
A. UDP không bị tính cước Internet.
B. Các trò chơi này sinh ra rất nhiều gói tin nhỏ mang toạ độ nhân vật. Nếu một gói bị mất, vị trí mới sẽ được cập nhật ở gói sau đó vài mili-giây. TCP với cơ chế chờ đợi, nhận lại và đảm bảo đúng thứ tự sẽ làm giật khung hình (Lag spike).
C. Game không dùng mạng.
D. UDP tự động tạo đồ họa đẹp hơn.
*Đáp án: B*
*Giải thích: Trì hoãn việc di chuyển nhân vật chờ 1 gói tin TCP bị lạc 1 giây trước là vô nghĩa trong thời gian thực.*

**Câu 124:** Một trong những nhược điểm lớn nhất của DNS khi xét về an ninh gốc rễ (trước khi DNSSEC ra đời) là gì?
A. Nó dùng mật khẩu dễ đoán.
B. Không hỗ trợ Windows.
C. Nó không có cơ chế XÁC THỰC (Authentication) máy chủ trả lời, dẫn đến bị tấn công giả mạo (DNS Spoofing / Cache Poisoning), kẻ tấn công lừa trình duyệt vào trang web giả của ngân hàng.
D. DNS quá chậm.
*Đáp án: C*
*Giải thích: UDP không có kiểm tra chặt chẽ. Nếu Hacker (ngồi chung Wi-Fi) nhanh tay hơn gửi đáp án giả (trỏ facebook thành IP của hacker) về máy tính trước máy chủ DNS thật, máy tính sẽ tin và vào nhầm trang giả.*

**Câu 125:** Dịch vụ thư mục "Active Directory" của Microsoft dựa rất nhiều vào dịch vụ tầng mạng/ứng dụng nào để các máy tính có thể "tìm thấy" máy chủ quản lý (Domain Controller) trong mạng LAN?
A. HTTP
B. DNS
C. FTP
D. SMTP
*Đáp án: B*
*Giải thích: AD tích hợp chặt chẽ với DNS nội bộ. Máy tính trạm truy vấn các bản ghi SRV (Service Record) trên DNS để định vị IP của máy chủ đăng nhập (Logon server).*

**Câu 126:** Kỹ thuật "URL Rewriting" (Viết lại URL) được dùng làm giải pháp dự phòng cho việc gì nếu Trình duyệt của người dùng tắt tính năng Cookie?
A. Chống copy văn bản.
B. Duy trì trạng thái/phiên làm việc (Session) bằng cách gắn trực tiếp ID Nhận dạng vào chuỗi tham số trong thanh địa chỉ URL mỗi khi người dùng click vào trang mới.
C. Nén video web.
D. Cấp IP tĩnh.
*Đáp án: B*
*Giải thích: Khi không có Cookie để nhớ Session ID ngầm, Web Server ép Session ID đó lộ thiên ngay trên thanh URL (vd: `index.php?session_id=123xyz`), tuy nhiên cách này dễ bị đánh cắp nếu chia sẻ link.*

**Câu 127:** Một gói tin có chỉ số cổng nguồn (Source Port) là ngẫu nhiên sinh ra (ví dụ 51234) và cổng đích (Destination Port) là 443. Điều này ngụ ý máy tính gửi đang đóng vai trò gì?
A. Máy chủ FTP.
B. Máy khách (Client) đang cố gắng thiết lập kết nối HTTPS đến một máy chủ Web.
C. Máy chủ DNS.
D. Máy tính đang bị nhiễm vi rút.
*Đáp án: B*
*Giải thích: Ephemeral Ports (cổng động, số lớn) được Hệ điều hành máy khách (Client) cấp phát ngẫu nhiên cho Browser để định danh chính Browser đó, còn Port đích 443 là cổng "nghe" chuẩn (Well-known) của máy chủ Web bảo mật.*

**Câu 128:** Trong HTTP, Web Cache (Proxy) khi nhận một request từ Client sẽ làm gì ĐẦU TIÊN?
A. Đi hỏi máy chủ gốc (Origin Server) luôn để lấy file.
B. Kiểm tra trong ổ cứng/RAM của chính nó xem đối tượng đó có tồn tại và CÒN HẠN SỬ DỤNG (Fresh) hay không.
C. Nén request lại.
D. Từ chối yêu cầu.
*Đáp án: B*
*Giải thích: Nếu đối tượng đã có trong Cache và còn mới (chưa bị quá hạn sửa đổi), Proxy sẽ trả thẳng nó về cho Browser (rất nhanh). Nếu quá hạn, nó mới dùng Conditional GET hỏi Server gốc.*

**Câu 129:** Khi một máy khách tải nhiều khối dữ liệu (chunks) của file Torrent, nó làm sao biết mảnh nào để tải?
A. Nó tự tải ngẫu nhiên không cần hỏi.
B. Nó lấy "Bitfield" (bản đồ mảnh) từ các Peer khác để biết đối phương đang có những mảnh nào, và ưu tiên tải các mảnh "hiếm nhất" (Rarest-first) trong hệ thống trước.
C. Nó phải hỏi máy chủ DNS.
D. Nó làm theo lệnh của ISP.
*Đáp án: B*
*Giải thích: Rarest-first rất thông minh: Nếu mảnh X chỉ có 1 người giữ, mọi người sẽ đua nhau tải mảnh X về, nhân rộng nó lên thành 10 người giữ, để phòng trường hợp người kia tắt máy thì mảnh X không bị tuyệt chủng.*

**Câu 130:** Trong công nghệ truyền hình cáp IP (IPTV), luồng video truyền từ máy chủ tới hàng ngàn Tivi của khách hàng trong một khu vực (đang xem cùng một kênh thời sự) thường được tối ưu băng thông lõi bằng phương pháp truyền tải nào?
A. Unicast TCP
B. Multicast (Đa hướng - IP Multicast)
C. FTP
D. P2P
*Đáp án: B*
*Giải thích: Thay vì phát 1000 luồng video riêng lẻ (Unicast) làm sập băng thông, Multicast chỉ phát 1 luồng video DUY NHẤT. Khi đến Router khu vực, Router mới "nhân bản" luồng đó ra cho các tivi đăng ký xem, tiết kiệm cực lớn tài nguyên mạng.*

**Câu 131:** Trong giao thức SSH, khóa công khai (Public Key) đóng vai trò gì trong việc thiết lập một kết nối an toàn?
A. Cấp IP cho máy trạm.
B. Mã hoá toàn bộ tệp tin trước khi tải.
C. Cho phép máy chủ gửi một "thách thức" mà chỉ có máy khách sở hữu khóa bí mật (Private Key) tương ứng mới có thể giải mã để chứng minh danh tính (Xác thực không cần mật khẩu).
D. Chạy một dịch vụ Web ẩn.
*Đáp án: C*
*Giải thích: Đăng nhập SSH bằng Public Key an toàn hơn gõ mật khẩu (Password-auth) vì nó chống lại phương pháp dò tìm mật khẩu (Brute-force) và nghe lén.*

**Câu 132:** Một trong các nhược điểm của việc sử dụng FTP (kết nối tiêu chuẩn chưa mã hóa) so với SFTP (SSH File Transfer Protocol) là gì?
A. FTP chậm hơn 10 lần.
B. FTP không hỗ trợ truyền ảnh.
C. FTP truyền tải mật khẩu đăng nhập dưới dạng văn bản gốc (clear-text) không mã hoá.
D. FTP không thể tiếp tục tải file khi bị đứt.
*Đáp án: C*
*Giải thích: Giống như Telnet, FTP thông thường rất kém bảo mật. Kẻ nghe lén bắt được gói tin là sẽ thấy ngay User và Pass của bạn.*

**Câu 133:** Thuật ngữ "API Gateway" (Cổng giao tiếp API) thường được đặt ở đâu trong một kiến trúc hệ thống Web lớn (Microservices)?
A. Đặt bên trong cơ sở dữ liệu.
B. Đặt ngay trước các máy chủ dịch vụ ẩn bên trong, đóng vai trò là cửa ngõ duy nhất (Entry point) tiếp nhận mọi HTTP Request từ phía Client, thực hiện kiểm tra quyền, phân tải, trước khi chuyển hướng đến dịch vụ con phù hợp.
C. Ở hệ điều hành máy khách.
D. Đặt tại nhà cung cấp cáp quang.
*Đáp án: B*
*Giải thích: Nó giống như cô lễ tân. Bạn không thể tự xông vào từng phòng ban làm việc, mà phải qua lễ tân để kiểm tra thẻ và lễ tân sẽ chỉ/gọi người xuống làm việc với bạn.*

**Câu 134:** Máy chủ tên miền "Local DNS Server" của một trường đại học hoặc tổ chức doanh nghiệp thường đóng vai trò là gì trong quá trình phân giải?
A. Máy chủ Root.
B. Máy chủ TLD.
C. Bộ định tuyến (Router).
D. Máy chủ đại lý (Proxy) đại diện cho máy tính của người dùng để thực hiện các truy vấn đệ quy ra Internet.
*Đáp án: D*
*Giải thích: Máy cá nhân chỉ hỏi Local DNS, và giao phó "Mày đi tìm hộ tao đi". Local DNS sẽ chạy loăng quăng trên Internet đi tìm kết quả mang về.*

**Câu 135:** Khi cấu hình máy chủ Web Nginx hoặc Apache, việc bật giao thức "Keep-Alive" liên quan đến tính năng nào của HTTP?
A. Conditional GET.
B. Persistent Connections (Kết nối TCP duy trì/thường trực).
C. Cookies.
D. DNS Caching.
*Đáp án: B*
*Giải thích: Giữ cho kênh TCP không bị đóng ngay sau khi tải xong HTML, để tải tiếp các ảnh/CSS một cách nhanh nhất.*

**Câu 136:** Tên miền (Domain) ".edu" trong hệ thống DNS thuộc cấp nào?
A. Root Level
B. Top-Level Domain (TLD)
C. Second-Level Domain
D. Host Level
*Đáp án: B*
*Giải thích: TLD là đuôi cao nhất ngay sau dấu chấm cuối (ngoại trừ root `.` ngầm định). Các đuôi .com, .org, .vn, .gov đều là TLD.*

**Câu 137:** Tác dụng của bản ghi TXT trong DNS thường được ứng dụng hiện đại sử dụng để làm gì?
A. Để lập bản đồ mạng.
B. Để chứa các chứng thực xác nhận quyền sở hữu tên miền, và các cấu hình bảo mật thư điện tử (như SPF, DKIM) để chống thư giả mạo (Spam/Phishing).
C. Để cấm truy cập mạng.
D. Để chuyển IP sang MAC.
*Đáp án: B*
*Giải thích: TXT (Text) ban đầu chỉ để ghi chú, nhưng giờ nó rất quan trọng. Khi bạn dùng Gmail gửi từ tên miền cty.com, Google sẽ bảo bạn chèn 1 mã vào bản ghi TXT để chứng minh bạn thực sự sở hữu cty.com.*

**Câu 138:** Khái niệm "Bandwidth Throttling" (Bóp nghẹt băng thông) mà các ISP thỉnh thoảng thực hiện áp dụng nhiều nhất đối với loại hình lưu lượng tầng Ứng dụng nào?
A. P2P (như BitTorrent) và Video Streaming.
B. Email.
C. Ping ICMP.
D. Dịch vụ DNS.
*Đáp án: A*
*Giải thích: Các ứng dụng như Torrent ngốn băng thông rất tàn bạo 24/7. Để tránh làm chậm mạng của người khác, ISP có thể dùng phần mềm nhận diện gói tin (DPI) để cố tình làm chậm Torrent lại.*

**Câu 139:** Giao thức WebSocket (ws:// và wss://) bắt đầu quá trình kết nối bằng cách:
A. Sinh ra một cổng UDP mới.
B. Bắt tay 3 bước với một giao thức hoàn toàn mới.
C. Gửi một HTTP Request thông thường kèm Header `Upgrade: websocket` để yêu cầu máy chủ đổi phương thức giao tiếp trên cùng 1 liên kết TCP hiện tại sang giao thức WebSocket.
D. Bỏ qua hoàn toàn TCP.
*Đáp án: C*
*Giải thích: WebSocket "quá giang" (piggyback) lên đường mở của HTTP. Khi Server đồng ý (101 Switching Protocols), ống nước đó chuyển từ một chiều (HTTP) sang ống nước thông hai chiều thực sự.*

**Câu 140:** Giao thức SMTP sử dụng mô hình đẩy (Push), vậy nếu một công ty muốn một hệ thống máy chủ thư nội bộ nhận thư TỪ Internet, thì Cổng bảo mật tường lửa (Firewall) của họ phải làm gì?
A. Đóng tất cả các port.
B. Mở cổng TCP 25 theo chiều Inbound (Từ ngoài vào) hướng tới IP của máy chủ thư.
C. Cấm giao thức TCP.
D. Dùng lệnh Ping.
*Đáp án: B*
*Giải thích: Vì SMTP là Push, máy chủ bưu điện của Google/Yahoo ngoài Internet sẽ CHỦ ĐỘNG kết nối đến Port 25 của máy chủ công ty bạn. Nếu Firewall đóng, thư sẽ bị dội ngược lại.*

**Câu 141:** Giao thức truy cập thư IMAP có tính năng nào vượt trội mà POP3 không có liên quan đến việc duy trì trạng thái?
A. IMAP tự động xóa thư sau 1 ngày.
B. IMAP cho phép tạo và quản lý các thư mục (Folder) thư điện tử trực tiếp TRÊN MÁY CHỦ, đồng bộ trạng thái "đã đọc/chưa đọc" qua lại giữa nhiều thiết bị.
C. IMAP luôn dùng UDP.
D. IMAP mã hóa cả tên miền.
*Đáp án: B*
*Giải thích: Đây là lý do chúng ta dùng IMAP cho các ứng dụng Outlook/Apple Mail hiện nay. Xóa thư trên điện thoại thì máy tính cũng tự động mất theo vì đồng bộ 2 chiều với Server.*

**Câu 142:** Trong mô hình Client-Server, một yêu cầu rất quan trọng đối với máy chủ (Server) nếu xét trên khía cạnh khả dụng mạng là:
A. Luôn thay đổi địa chỉ IP.
B. Máy chủ phải luôn hoạt động 24/7 (always-on) và thường yêu cầu một địa chỉ IP tĩnh (Static IP) đã biết để Client có thể tìm tới bất cứ lúc nào.
C. Máy chủ tự động tắt lúc 12h đêm.
D. Máy chủ ẩn MAC.
*Đáp án: B*
*Giải thích: Nếu IP Server đổi liên tục, DNS cập nhật không kịp, Client sẽ "mù" không tìm thấy đích đến. IP tĩnh là yêu cầu bắt buộc của hạ tầng Server.*

**Câu 143:** Các công nghệ ứng dụng OTT (Over-The-Top) như Zalo, Messenger, WhatsApp thực chất hoạt động như thế nào so với nền tảng của nhà mạng viễn thông?
A. Chúng thay thế cột sóng của nhà mạng.
B. Chúng sử dụng sóng radio riêng không cần Internet.
C. Chúng là các dịch vụ ở tầng Ứng dụng, "cưỡi" trên nền hạ tầng kết nối dữ liệu Internet IP hiện có của nhà mạng (3G/4G/Cáp quang), bỏ qua các dịch vụ nghe/gọi/SMS truyền thống.
D. Bắt buộc kết nối qua vệ tinh.
*Đáp án: C*
*Giải thích: Việc Zalo/Viber ra đời gọi điện/nhắn tin miễn phí bằng IP (OTT) đã lấy đi doanh thu thoại và SMS cực lớn của các nhà mạng viễn thông.*

**Câu 144:** Khái niệm "Load Balancer" (Bộ cân bằng tải) ở tầng Ứng dụng / Mạng thường có mục đích gì khi người dùng truy cập một Website siêu lớn?
A. Phân phát dữ liệu trên 2 sợi cáp cho đều.
B. Đóng vai trò làm máy chủ DNS duy nhất.
C. Tiếp nhận toàn bộ lưu lượng (Request) và phân bổ/chia đều chúng xuống một cụm (cluster) nhiều máy chủ Web (Backend) nằm phía sau, giúp hệ thống không bị quá tải cục bộ.
D. Cấp IP cho máy trạm.
*Đáp án: C*
*Giải thích: Facebook có hàng chục vạn server nhưng bạn chỉ kết nối vào 1 địa chỉ. Bộ phân tải (VD: HAProxy, Nginx) sẽ đứng ngoài cửa nhận khách và xếp họ vào bàn trống.*

**Câu 145:** Mã trạng thái (Status code) 503 "Service Unavailable" báo hiệu nguyên nhân sự cố thường xuất phát từ đâu?
A. Trình duyệt người dùng hỏng.
B. Gõ sai đường dẫn web.
C. Máy chủ web đang bị quá tải (overloaded) hoặc đang được bảo trì, không thể phục vụ Request.
D. Hết pin máy tính.
*Đáp án: C*
*Giải thích: Mã 5xx là lỗi thuộc về phía Hệ thống Máy chủ (Server Error).*

**Câu 146:** Phương thức "Polling" (Hỏi dò) trong các ứng dụng mạng cổ điển để lấy dữ liệu thời gian thực có nhược điểm chí mạng nào?
A. Dùng quá nhiều RAM máy chủ.
B. Máy khách phải liên tục (VD cứ mỗi 1 giây) gửi một HTTP Request đến Server để hỏi "Có dữ liệu mới không?", gây tốn kém khủng khiếp băng thông và tài nguyên CPU cho những request rác vô ích.
C. Không hỗ trợ DNS.
D. Bị cấm bởi ICANN.
*Đáp án: B*
*Giải thích: Polling là giải pháp tồi (như con trẻ ngồi trên xe hỏi bố mẹ "Đã đến nơi chưa?" mỗi 1 phút). WebSocket hoặc Web Push ra đời để thay thế (đến nơi bố mẹ tự gọi).*

**Câu 147:** Định dạng tệp tin JSON (JavaScript Object Notation) ngày nay thường thay thế cho XML trong việc trao đổi dữ liệu qua Web API vì:
A. JSON mã hoá mạnh hơn XML.
B. JSON được tổ chức theo tiêu chuẩn của quân đội.
C. JSON gọn nhẹ hơn, tiết kiệm băng thông (ít ký tự đóng gói `<tag>`) và rất tự nhiên/dễ phân tích cú pháp cho JavaScript trên Trình duyệt.
D. JSON dùng UDP.
*Đáp án: C*
*Giải thích: Cấu trúc JSON dạng `{ "key": "value" }` nhẹ và truyền tải ít dung lượng rác qua mạng hơn so với XML.*

**Câu 148:** Khái niệm "Deep Packet Inspection" (DPI - Phân tích gói tin sâu) cho phép thiết bị tường lửa (Firewall) thực hiện điều gì?
A. Đọc địa chỉ IP.
B. Quét được tầng Application (Tầng 7). Nó mở phần Payload dữ liệu ra để xem nội dung bên trong có chứa phần mềm độc hại, từ khoá cấm, hay nhận diện đó là luồng BitTorrent hay Skype để chặn/ưu tiên.
C. Sửa cáp quang đứt.
D. Nối 2 dây đồng thành 1.
*Đáp án: B*
*Giải thích: Firewall truyền thống chỉ kiểm tra IP/Port. DPI can thiệp rất sâu vào nội dung (như một hải quan kiểm tra tận trong từng gói hàng nhỏ) rất tốn CPU nhưng chính xác tuyệt đối.*

**Câu 149:** Trong mô hình IoT (Internet of Things), giao thức tầng ứng dụng MQTT (Message Queuing Telemetry Transport) được thiết kế ưu tiên cho môi trường nào?
A. Tải phim 4K.
B. Trình duyệt Web đồ hoạ cao.
C. Các cảm biến/thiết bị có năng lực phần cứng siêu nhỏ, dùng băng thông tối thiểu và môi trường mạng chập chờn, không ổn định.
D. Mạng dây Ethernet Gigabit.
*Đáp án: C*
*Giải thích: MQTT cực nhẹ (Header chỉ 2 byte). Thiết bị nhiệt độ chỉ thỉnh thoảng gửi một gói 10 bytes qua mạng 3G/4G tậm tịt, dùng MQTT là hoàn hảo.*

**Câu 150:** Giao thức nào hoạt động ở cả giao diện Web (qua trình duyệt) lẫn các phần mềm trò chuyện nội bộ của công ty (như Microsoft Teams/Slack) để mã hóa dữ liệu end-to-end bảo vệ nội dung chat?
A. DHCP
B. ARP
C. TLS/SSL
D. ICMP
*Đáp án: C*
*Giải thích: Bảo mật (Mã hóa đường truyền) trên Web hay App phần lớn hiện nay đều gọi sự trợ giúp của thư viện TLS ở tầng dưới cùng của Application/trên đỉnh của Transport.*

**Câu 151:** Trong BitTorrent, tệp tin gốc cần chia sẻ sẽ được cắt nhỏ thành các mảnh (pieces/chunks) thường có kích thước là bao nhiêu?
A. 1 Byte
B. 1 KB
C. 256 KB hoặc 512 KB
D. 1 GB
*Đáp án: C*
*Giải thích: Việc chia thành các mảnh nhỏ (ví dụ 256KB) giúp các peer dễ dàng tải song song nhiều mảnh từ nhiều người khác nhau cùng một lúc, tăng tốc độ tổng thể.*

**Câu 152:** Đặc điểm chính của ứng dụng "Skype" liên quan đến việc định tuyến thoại là gì (đặc biệt trong giai đoạn P2P truyền thống của nó)?
A. Định tuyến toàn bộ qua một máy chủ duy nhất của Microsoft.
B. Sử dụng các "Super Node" (Máy tính của người dùng có kết nối mạng mạnh) để định tuyến dữ liệu thoại cho các người dùng khác nhằm tránh tường lửa và NAT.
C. Sử dụng truyền hình vệ tinh.
D. Không dùng giao thức IP.
*Đáp án: B*
*Giải thích: Do nhiều máy khách nằm ẩn sau NAT nội bộ không thể gọi trực tiếp nhau, Skype dùng các máy có IP Public (Super Nodes) làm trung gian kết nối.*

**Câu 153:** Một trong các nhược điểm của việc ứng dụng sử dụng quá nhiều các thẻ "Cookie" là gì?
A. Tăng băng thông mạng lên tối đa.
B. Giảm bớt số lượng máy chủ DNS.
C. Cookie được thêm vào Header của mỗi HTTP Request gửi đi, nếu Cookie quá lớn có thể làm tăng đáng kể "đầu cước" (overhead) không cần thiết trên đường truyền.
D. Tự động mã hoá ổ cứng máy tính.
*Đáp án: C*
*Giải thích: Cookie bay qua lại giữa Client và Server liên tục. Nếu lưu quá nhiều thông tin vào Cookie, băng thông cho Header đôi khi còn lớn hơn cả tải trọng (Payload).*

**Câu 154:** "Spam Email" (Thư rác) là một vấn đề lớn đối với giao thức SMTP chủ yếu do đặc tính nào của SMTP?
A. Mật khẩu SMTP luôn bằng 0.
B. SMTP theo chuẩn gốc không tích hợp sẵn tính năng xác thực (Authentication) người gửi gốc một cách chặt chẽ, rất dễ giả mạo (Spoof) trường "MAIL FROM".
C. SMTP yêu cầu cáp quang.
D. DNS tự tạo ra thư rác.
*Đáp án: B*
*Giải thích: Hacker dễ dàng tạo lệnh SMTP gõ "MAIL FROM: donald.trump@whitehouse.gov" và Server mặc định cũng không kiểm chứng. Do đó các giao thức chống spam như SPF, DKIM, DMARC phải ra đời sau này.*

**Câu 155:** Ứng dụng "Web Browser" (Trình duyệt) đóng vai trò gì trong việc hiển thị một trang Web?
A. Là máy chủ lưu trữ file web.
B. Chỉ gửi thư.
C. Đọc HTML lấy về từ Server, thông dịch, vẽ kết cấu đồ hoạ, tải thêm ảnh/CSS/JS (bằng các Request phụ) và kết xuất (Render) ra màn hình tương tác.
D. Giải phân giải DNS cấp 1.
*Đáp án: C*
*Giải thích: Trình duyệt không chỉ là "người vận chuyển" mà là một hệ điều hành thu nhỏ (Render Engine, Javascript Engine) để biến các dòng code thô thành giao diện trực quan.*

**Câu 156:** Khái niệm "Root Name Servers" (Máy chủ tên miền gốc) bao gồm bao nhiêu cụm máy chủ lôgic được quản lý toàn cầu?
A. 13
B. 128
C. 500
D. Vô số
*Đáp án: A*
*Giải thích: Theo kiến trúc gốc, có 13 cụm Root Server (từ A.root-servers.net đến M.root-servers.net). Thực tế vật lý là hàng ngàn máy chủ dùng chung 13 địa chỉ IP Anycast này.*

**Câu 157:** Bản ghi DNS dùng để định tuyến thư điện tử (Email) trong một tên miền gọi là gì?
A. A
B. NS
C. MX
D. CNAME
*Đáp án: C*
*Giải thích: MX (Mail Exchanger) record xác định máy chủ nào (có thể có nhiều mức ưu tiên) chịu trách nhiệm nhận thư cho một Domain.*

**Câu 158:** Một trong những lợi ích của việc "Phân chia dữ liệu thành mảnh nhỏ" (Chunking) trong truyền dẫn Video Streaming là gì?
A. Tránh bị đánh cắp bản quyền.
B. Cho phép điều chỉnh chất lượng (Độ phân giải / Bitrate) ngay lập tức thích ứng với sự thay đổi của chất lượng mạng tại mỗi thời điểm tải từng mảnh.
C. Tránh mã hóa.
D. Biến tín hiệu số thành tương tự.
*Đáp án: B*
*Giải thích: DASH chia video 10 phút thành hàng trăm đoạn nhỏ 2-10 giây. Đoạn 1 đang lag thì tải bản SD, đoạn 2 mạng ngon lại tải lại bản HD. Nếu không chia mảnh, bạn phải chọn chết 1 chuẩn từ đầu.*

**Câu 159:** Lệnh FTP dùng để chuyển chế độ truyền tải dữ liệu giữa máy khách và máy chủ sang dạng "Thụ động" (Passive mode) giải quyết bài toán gì?
A. Ngăn chặn download.
B. Khắc phục việc máy khách nằm sau Tường lửa / NAT không thể cho phép máy chủ chủ động mở kết nối Data vào máy khách (như ở Active Mode).
C. Chuyển từ TCP sang UDP.
D. Biến chữ thường thành chữ hoa.
*Đáp án: B*
*Giải thích: Khi gọi Passive (PASV), Client báo: "Tôi bị chặn Firewall rồi, Server hãy mở 1 port đi, tôi sẽ CHỦ ĐỘNG chui ra kết nối với Server".*

**Câu 160:** Cấu trúc URL (Uniform Resource Locator) `http://www.google.com:80/index.html` có các thành phần nào?
A. Giao thức HTTP, Hostname (www.google.com), Port (80), Đường dẫn (Path: /index.html).
B. Tên công ty, Máy chủ, IP.
C. Địa chỉ MAC.
D. Mã bảo mật.
*Đáp án: A*
*Giải thích: URL cung cấp cú pháp chuẩn mực để xác định vị trí mọi tài nguyên trên Internet bao gồm cả Giao thức để lấy tài nguyên đó.*

**Câu 161:** Phương thức HTTP `PUT` thường có tính chất Idempotent (Lũy đẳng). Điều này có nghĩa là:
A. Tốc độ thực thi rất cao.
B. Gửi cùng một Request PUT một lần hay hàng ngàn lần liên tiếp thì Trạng thái cuối cùng của tài nguyên trên Server đều GIỐNG HỆT NHAU.
C. Xóa vĩnh viễn tệp tin.
D. Yêu cầu nhập mật mã.
*Đáp án: B*
*Giải thích: PUT thường dùng để Update/Ghi đè. Ghi đè `A=5` 100 lần thì kết quả `A` vẫn bằng 5. Trái lại, POST không có tính lũy đẳng (ví dụ Đặt hàng: gửi 2 lần có thể bị tính tiền 2 lần).*

**Câu 162:** Hiện tượng "XSS" (Cross-Site Scripting) là một lỗ hổng bảo mật Web (Application Layer). Tin tặc lợi dụng XSS bằng cách:
A. Gửi gói Ping khổng lồ.
B. Chèn các đoạn mã độc (thường là JavaScript) vào các trang web bị lỗi, khi người dùng khác truy cập trang web, mã độc sẽ thực thi trên Trình duyệt của họ để lấy cắp Cookie/Session.
C. Xóa mã nguồn máy chủ.
D. Chặn Wi-Fi.
*Đáp án: B*
*Giải thích: Ví dụ: hacker comment mã script vào 1 bài báo, bất kỳ ai đọc bài báo đó sẽ tự động chạy mã script và bị trộm Cookie gửi cho hacker.*

**Câu 163:** Trong Web hiện đại, khái niệm "Single Page Application" (SPA) ám chỉ thiết kế web nào?
A. Trang web chỉ có 1 dòng chữ.
B. Trang web tải lại (reload) toàn bộ HTML từ server mỗi khi click link.
C. Trang web chỉ tải một bản HTML duy nhất lúc ban đầu; các thao tác chuyển trang sau đó chỉ tải thêm DỮ LIỆU (qua AJAX/API) và cập nhật động nội dung thông qua Javascript mà không phải F5 reload lại trang.
D. Mọi thứ phải xem ngoại tuyến.
*Đáp án: C*
*Giải thích: Các ứng dụng như Facebook, Gmail là SPA. Trải nghiệm rất mượt mà giống như một App Desktop vì không bao giờ có độ trễ chớp đen màn hình (Full page load).*

**Câu 164:** Máy chủ tên miền "TLD DNS Server" của miền ".vn" được vận hành bởi ai?
A. Google
B. ICANN
C. VNNIC (Trung tâm Internet Việt Nam)
D. Microsoft
*Đáp án: C*
*Giải thích: Các mã quốc gia (ccTLD - country-code TLD) được giao cho các tổ chức quản lý viễn thông quốc gia đó toàn quyền duy trì.*

**Câu 165:** Phương thức TCP (Transmission Control Protocol) đảm bảo "Đúng thứ tự" (In-order) của luồng dữ liệu bằng cách nào ở tầng Giao vận để hỗ trợ tầng Ứng dụng?
A. Dùng cáp xoắn.
B. Đánh số thứ tự (Sequence Number) cho từng gói tin. Máy nhận sẽ giữ trong Buffer (bộ đệm) và sắp xếp lại các gói tin theo số Sequence trước khi đẩy lên Application, dù chúng đến trước hay sau.
C. Dùng DNS tra cứu.
D. TCP không hỗ trợ đúng thứ tự.
*Đáp án: B*
*Giải thích: Mạng gói (Datagram) định tuyến độc lập, gói 2 có thể đến trước gói 1 do đi đường tắt. Trình duyệt Web (Application) nhận dữ liệu từ TCP luôn ở trạng thái đã được sắp xếp gọn gàng (nhờ Sequence Number).*

**Câu 166:** Tính năng "Auto-Scaling" (Tự động co giãn) ở tầng điện toán đám mây hỗ trợ cho Web Application như thế nào?
A. Co giãn màn hình điện thoại.
B. Giám sát lưu lượng Web, nếu quá tải (CPU > 80%), hệ thống tự động sinh thêm (clone) các Server mới và đẩy vào Load Balancer, nếu lưu lượng giảm, tự động hủy Server đi để tiết kiệm tiền.
C. Co giãn cáp quang.
D. Biến TCP thành P2P.
*Đáp án: B*
*Giải thích: Đây là xương sống của nền kinh tế Cloud. Web mua vé ca nhạc có thể cần 100 Server lúc mở bán, nhưng chỉ cần 1 Server lúc bình thường.*

**Câu 167:** Khác biệt giữa "Push Notification" (Thông báo đẩy) trên điện thoại và Email là gì về giao thức?
A. Email dùng Push, Notification dùng Pull.
B. Cả 2 đều dùng chuẩn SMTP.
C. Thông báo đẩy duy trì một liên kết TCP (hoặc dùng cổng MQTT riêng) luôn mở với Server (ví dụ Apple APNs, Google FCM), để khi có tin, Server dội lệnh xuống Đánh thức điện thoại ngay lập tức mà không cần App đó đang chạy.
D. Không có khác biệt.
*Đáp án: C*
*Giải thích: Tính năng này giúp điện thoại cực kỳ tiết kiệm pin. Nó không phải liên tục dùng phần mềm Chat để đi hỏi xem có tin nhắn mới không.*

**Câu 168:** "Reverse Proxy" (Proxy ngược) bảo vệ máy chủ Web (Backend) bằng cách:
A. Cắt đứt hoàn toàn Internet.
B. Đứng chặn TRƯỚC mặt các máy chủ Web. Toàn bộ Request từ ngoài Internet phải đập vào Reverse Proxy trước (người ngoài không thấy IP thật của Web Server).
C. Tắt cổng 80.
D. Cấp mã MAC động.
*Đáp án: B*
*Giải thích: Ngoài việc cân bằng tải, Reverse Proxy (Ví dụ Nginx, Cloudflare) giấu nhẹm IP gốc của Server, chống tấn công DDoS và làm SSL Termination (Giải mã HTTPS giúp Server).*

**Câu 169:** Mạng truyền tải nội dung CDN có thể giảm "Jitter" (Biến thiên độ trễ) cho Video Streaming bằng cách nào?
A. Nén video lại một nửa.
B. Bỏ TCP.
C. Server CDN được đặt trong ISP địa phương (ngay sát người dùng), số lượng chặng (Hops) qua các Router từ server tới client chỉ còn 1-2 bước, triệt tiêu tối đa các nút thắt cổ chai gây Jitter trên mạng lõi.
D. Kéo cáp từ CDN đến tận máy khách.
*Đáp án: C*
*Giải thích: Càng đi qua nhiều mạng của các quốc gia khác nhau, rủi ro tắc nghẽn, dao động độ trễ (Jitter) càng cao.*

**Câu 170:** "Cơ sở dữ liệu phân tán" (Distributed Database) của hệ thống DNS đảm bảo tính chất nào?
A. Mọi thay đổi IP được cập nhật ngay lập tức sau 1 mili-giây trên toàn cầu.
B. Không bao giờ lưu Cache.
C. Khả năng mở rộng khổng lồ (Scalability) và độ chịu lỗi cao (Fault Tolerance), không phụ thuộc vào sức mạnh của bất kỳ phần cứng trung tâm nào.
D. Cấm quyền sở hữu.
*Đáp án: C*
*Giải thích: DNS là một trong những hệ thống mạng thành công và vĩ đại nhất từng được con người thiết kế, phục vụ hàng tỷ thiết bị mà rất hiếm khi sập.*

**Câu 171:** Trong khi sử dụng trình duyệt Web (ví dụ Chrome), bạn có thể mở 10 tab khác nhau kết nối tới 10 trang web khác nhau. Máy tính phân biệt dữ liệu của tab nào về tab đó dựa vào đâu?
A. Dựa vào Địa chỉ MAC của từng trang web.
B. Dựa vào địa chỉ IP của Router.
C. Trình duyệt mở 10 "Socket" khác nhau. Mỗi kết nối TCP có một Cổng Nguồn (Source Port) duy nhất (ví dụ: 50111, 50112...). Khi gói tin trả về, Hệ điều hành nhìn Source Port ban đầu để trả về đúng Tab (Process) đó.
D. Trình duyệt chia màn hình theo khung lưới tĩnh.
*Đáp án: C*
*Giải thích: Tính năng Multiplexing / Demultiplexing của tầng Transport (Port) là chìa khóa để một hệ điều hành có thể chạy đồng thời hàng chục ứng dụng mạng mà không bị lẫn lộn dữ liệu.*

**Câu 172:** Giao thức nào là "Vô trạng thái" (Stateless) nhưng lại thường được các lập trình viên sử dụng thêm cơ chế khác để giả lập "Có trạng thái" (Stateful) khi xây dựng ứng dụng web phức tạp?
A. TCP
B. HTTP
C. FTP
D. SMTP
*Đáp án: B*
*Giải thích: HTTP là stateless. Nhưng Web App (như Lazada) lại là Stateful. App giải quyết bằng cách dùng Cookie/Session, Token, hoặc Local Storage nhúng vào luồng HTTP.*

**Câu 173:** Việc đăng nhập tài khoản qua OAuth 2.0 (như nút "Đăng nhập bằng Google/Facebook" trên các web khác) mang lại lợi ích gì cho người dùng so với đăng ký mật khẩu truyền thống?
A. Mật khẩu được rút ngắn đi.
B. Trang web mới chỉ được cấp quyền sử dụng các thông tin cơ bản (qua Token) mà không hề biết mật khẩu thật của bạn tại Google/Facebook, giúp tránh lộ mật khẩu gốc nếu trang web đó bị hack.
C. Tự động mã hóa phần cứng.
D. Miễn phí Internet.
*Đáp án: B*
*Giải thích: OAuth 2.0 là chuẩn Ủy quyền (Authorization) ở tầng Application. Bạn cho phép Web A truy cập thông tin profile của bạn ở Web B mà không cần đưa chìa khóa két sắt (Password) cho Web A.*

**Câu 174:** Máy khách Email (Mail Client) sử dụng giao thức nào để NHẬN (tải) thư về mà Giao thức đó sẽ TỰ ĐỘNG XÓA thư trên Server sau khi tải về (theo cấu hình mặc định gốc)?
A. IMAP
B. POP3
C. HTTP
D. FTP
*Đáp án: B*
*Giải thích: Cấu hình "Download and Delete" của POP3 từ thời dung lượng đĩa máy chủ còn đắt đỏ. Thư đã lấy về máy tính thì biến mất khỏi Server.*

**Câu 175:** Cấu trúc phân cấp của máy chủ DNS từ trên xuống dưới (Root -> TLD -> Authoritative) giúp thực hiện nguyên lý mạng nào sau đây?
A. Phân cấp IP tĩnh.
B. Phân quyền và phân giải quyết tập trung.
C. Phân tán dữ liệu, phân tải truy vấn và ủy quyền phân giải tên miền cho các cấp quản lý thấp hơn, tránh tắc nghẽn ở nút trung tâm.
D. Định tuyến ngẫu nhiên (Random routing).
*Đáp án: C*
*Giải thích: Root không cần biết mọi IP. Nó chỉ cần biết "Ai quản lý .com". TLD .com không cần biết IP của "sv1.google.com", nó chỉ cần biết "Ai là Authoritative Server của google.com".*

**Câu 176:** Trong HTTP/1.1, dòng `Connection: keep-alive` trong Header có ý nghĩa gì đối với máy chủ Web?
A. Xin cấp thêm băng thông.
B. Yêu cầu tải video.
C. Yêu cầu máy chủ đừng vội đóng kết nối TCP sau khi phản hồi xong; hãy giữ nó mở một lát (vd: 15s) để Client có thể gửi thêm các HTTP Request khác (ảnh, js) thông qua chính ống TCP này.
D. Lệnh buộc máy chủ khởi động lại.
*Đáp án: C*
*Giải thích: Persistent Connection (Keep-Alive) là chuẩn trong HTTP/1.1, giúp giảm RTT thiết lập TCP, nhưng cũng gây tốn RAM cho Server nếu duy trì quá nhiều kết nối không làm gì (Idle).*

**Câu 177:** Kỹ thuật "Content Negotation" (Đàm phán nội dung) trong HTTP cho phép máy chủ và máy khách thoả thuận điều gì?
A. Thoả thuận giá cước mạng.
B. Thoả thuận xem ai gửi trước.
C. Thoả thuận về loại ngôn ngữ (Language), định dạng file (Accept: text/html hay application/json) hoặc cách thức mã hóa/nén (Accept-Encoding: gzip) phù hợp nhất với máy khách.
D. Đàm phán địa chỉ MAC.
*Đáp án: C*
*Giải thích: Trình duyệt gửi `Accept-Language: vi-VN` báo cho Server ưu tiên trả về bản tiếng Việt nếu Server hỗ trợ Đa ngôn ngữ (Multilingual).*

**Câu 178:** Trạng thái mã lỗi 500 "Internal Server Error" trên Web thường do nguyên nhân nào gây ra?
A. Lỗi do người dùng gõ sai tên miền.
B. Lỗi do rớt mạng Wi-Fi của máy khách.
C. Lỗi cấu hình, lỗi mã nguồn (Code bug), hoặc lỗi kết nối cơ sở dữ liệu (Database) TẠI MÁY CHỦ Web (Backend).
D. Lỗi chưa nạp tiền cước Internet.
*Đáp án: C*
*Giải thích: 500 là lỗi phổ biến nhất báo hiệu "Server bị hỏng/lỗi xử lý nội bộ" (ví dụ hàm code PHP bị lỗi chia cho 0).*

**Câu 179:** Giao thức SMTP có thể hiểu được chữ cái, nhưng nó không trực tiếp gửi được dấu Tiếng Việt (có dấu) nếu không được xử lý bằng cấu trúc nào?
A. Chuyển sang FTP.
B. Thay đổi card mạng.
C. Sử dụng chuẩn mở rộng MIME với khai báo `Content-Type: text/plain; charset=UTF-8` để quy định cách biên dịch ký tự Unicode.
D. Dùng lệnh ICMP.
*Đáp án: C*
*Giải thích: SMTP nguyên thủy chỉ nhận bảng mã ASCII chuẩn (không có dấu tiếng Việt). MIME giúp đóng gói dữ liệu Unicode (UTF-8) một cách an toàn qua SMTP.*

**Câu 180:** Mạng phân phối nội dung (CDN) có thể chống lại các cuộc tấn công DDoS ở mức ứng dụng (Application Layer DDoS) tốt hơn máy chủ cá nhân vì:
A. Chúng có thể tắt mạng.
B. Chúng sử dụng toàn thiết bị cũ.
C. Bề mặt phân tán của CDN rất lớn với dung lượng băng thông (Capacity) khổng lồ, và chúng có các hệ thống tường lửa (WAF - Web Application Firewall) có khả năng lọc lưu lượng rác ngay tại Edge (Rìa) mạng.
D. CDN mã hóa toàn bộ trang web.
*Đáp án: C*
*Giải thích: DDoS gửi 100 Gbps rác tới Server cá nhân (có cổng 1 Gbps) sẽ làm sập mạng. CDN như Cloudflare có tổng mạng hàng chục Tbps, họ sẽ nuốt trọn số rác đó và phân tán chúng đi.*

**Câu 181:** Tại sao DNS lại hoạt động trên Port 53 UDP thay vì TCP cho các lệnh truy vấn phân giải tiêu chuẩn (A Record Lookup)?
A. UDP bảo mật hơn TCP.
B. UDP nhẹ, tốc độ phản hồi nhanh (Không cần RTT thiết lập bắt tay 3 bước). Một gói tin Request và một gói Response duy nhất nằm lọt trong giới hạn 512 bytes truyền thống.
C. UDP nén file tốt hơn.
D. UDP đảm bảo đúng thứ tự truy vấn.
*Đáp án: B*
*Giải thích: Tốc độ là vua. Nếu DNS chậm 1 giây thì bạn phải đợi trang web "quay mòng mòng" trắng xóa thêm 1 giây. Dù vậy, DNS over TCP vẫn được hỗ trợ nếu gói Response > 512 bytes (ví dụ truy vấn DNSSEC).*

**Câu 182:** "DNS Cache Poisoning" (Đầu độc bộ đệm DNS) nguy hiểm nhất đối với dịch vụ nào?
A. Nghe nhạc mp3.
B. Chơi game offline.
C. Các dịch vụ cần độ tin cậy tuyệt đối như Đăng nhập Internet Banking ngân hàng (kẻ gian đầu độc DNS của nhà mạng để trỏ tên miền ngân hàng sang IP của Web giả mạo hòng lấy mã OTP).
D. Tính năng tính toán của máy tính.
*Đáp án: C*
*Giải thích: Máy tính tin tưởng mù quáng vào kết quả do Local DNS trả về. DNSSEC ra đời để mã hóa và ký số điện tử (Digital Signature) vào bản ghi DNS nhằm chống lại hình thức đầu độc này.*

**Câu 183:** Nếu một kiến trúc P2P (ngang hàng) được thiết lập tại văn phòng cho 50 máy tính thay thế cho một Máy chủ Chia sẻ File (File Server), ưu điểm kinh tế rõ rệt nhất là:
A. Tốc độ mạng LAN tăng lên 10G.
B. Mỗi máy cần cài ít RAM hơn.
C. Tiết kiệm được chi phí mua một máy chủ chuyên dụng (Dedicated Server) đắt tiền, và không cần thuê người quản trị máy chủ.
D. Không cần dùng Router.
*Đáp án: C*
*Giải thích: Mọi PC tự chia sẻ ổ cứng của mình với người khác (ví dụ: Windows File Sharing / Workgroup).*

**Câu 184:** Bạn đang thiết kế ứng dụng gọi Video nhóm. Nếu sử dụng kiểu mạng P2P lưới (Mesh: mỗi người kết nối trực tiếp với TẤT CẢ mọi người) cho phòng họp 10 người, điều gì sẽ làm thiết bị di động quá tải?
A. Tốn nhiều dung lượng ổ cứng.
B. Điện thoại phải "Nhân bản" và tải lên (Upload) luồng Video của bạn cho tận 9 người khác đồng thời, làm nghẽn băng thông Upload của mạng gia đình và cạn kiệt CPU.
C. Độ phân giải bị cố định 360p.
D. Không thể mã hóa video.
*Đáp án: B*
*Giải thích: Với P2P Full Mesh, Băng thông Upload = N x Bitrate. Đây là lý do các ứng dụng họp như Zoom/Teams thường dùng mô hình Client-Server (qua MCU/SFU Server) để trộn Video rồi mới gửi xuống điện thoại để tiết kiệm băng thông.*

**Câu 185:** "Web Cookie" có hai loại chính là Session Cookie và Persistent Cookie. Đặc điểm của Session Cookie là gì?
A. Lưu trong RAM của trình duyệt và tự xóa ngay khi bạn ĐÓNG trình duyệt.
B. Lưu dưới dạng file văn bản vĩnh viễn trên ổ cứng.
C. Dùng để đăng nhập nhiều trang web cùng lúc.
D. Chỉ chứa video.
*Đáp án: A*
*Giải thích: Cookie phiên (Session Cookie) giúp bạn giữ trạng thái đăng nhập khi đang xem web. Tắt trình duyệt (Chrome/Edge) mở lại, bạn sẽ phải đăng nhập lại. Persistent Cookie (có HSD dài hạn) giúp "Nhớ mật khẩu" cả tuần.*

**Câu 186:** Khi gõ URL có dạng `ftp://username:password@ftp.example.com` lên thanh địa chỉ, điều gì xảy ra ở tầng Ứng dụng?
A. Máy tính sẽ khởi động phần mềm duyệt mail.
B. Trình duyệt tự gọi một FTP Client nội bộ, trích xuất thông tin xác thực trên URL để đăng nhập vào máy chủ FTP example.com.
C. Tên miền bị vô hiệu hoá.
D. Trình duyệt đóng kết nối TCP.
*Đáp án: B*
*Giải thích: URI Schema (`ftp://`, `mailto://`, `http://`) nói cho Hệ điều hành biết phải dùng Protocol/App nào để xử lý Request đó.*

**Câu 187:** Trong RESTful API, phương thức HTTP DELETE thực hiện chức năng nào theo quy ước?
A. Xoá mọi thứ trên ổ cứng người dùng.
B. Yêu cầu máy chủ Backend tìm và Xóa (Xóa logic hoặc vật lý) một tài nguyên cụ thể (Ví dụ: DELETE /users/123 -> xoá tài khoản 123 khỏi DB).
C. Xóa thư mục mạng.
D. Xóa Cookie.
*Đáp án: B*
*Giải thích: HTTP Method cung cấp Ngữ nghĩa (Semantics) rõ ràng thay vì phải tạo hàng tá URL phức tạp (Ví dụ: POST thay vì dùng URL /action=xoa).*

**Câu 188:** Đâu KHÔNG PHẢI là một lợi ích của việc "Đồng bộ hóa thư mục" qua Cloud Storage (như Google Drive, Dropbox)?
A. Cho phép truy cập dữ liệu từ nhiều thiết bị.
B. Tăng thêm khả năng khôi phục (Backup/Disaster Recovery) khi ổ cứng cục bộ bị hỏng.
C. Ứng dụng client ngầm theo dõi các file thay đổi, dùng HTTP/API để đẩy file lên đám mây tự động.
D. Nén file cục bộ lại 100 lần.
*Đáp án: D*
*Giải thích: Cloud Storage không "nén ảo thuật" đĩa cứng của bạn. Nó tạo ra một "phiên bản song sinh" của thư mục nhà bạn tại Máy chủ Server (Mô hình Client-Server).*

**Câu 189:** Để bảo vệ tên miền khỏi việc người lạ gửi thư lừa đảo (Giả danh `boss@cty.com`), người quản trị IT cấu hình một bản ghi "SPF" (Sender Policy Framework) ở DNS. Bản ghi này có nhiệm vụ gì?
A. Mã hóa thư.
B. Nó là một bản ghi loại TXT liệt kê danh sách CÁC ĐỊA CHỈ IP HỢP LỆ (của các máy chủ bưu điện thật) được phép gửi Email với tư cách là `cty.com`. Máy chủ nhận sẽ check IP nguồn để quyết định Nhận hay quăng vào Spam.
C. Dịch tên người gửi thành MAC.
D. Chỉ đường cho Web server.
*Đáp án: B*
*Giải thích: Khi hacker ở VN (IP 1.2.3.4) gửi thư giả `boss@cty.com`. Gmail nhận được sẽ tra SPF của cty.com thấy (Chỉ IP 8.8.8.8 mới được gửi). Gmail thấy 1.2.3.4 mạo danh -> Đánh dấu SPAM lập tức.*

**Câu 190:** Để một tiến trình Server chờ kết nối từ Client, ở tầng Socket API, nó phải thực thi hàm nào để "lắng nghe"?
A. `bind()`
B. `send()`
C. `listen()` và `accept()`
D. `connect()`
*Đáp án: C*
*Giải thích: `listen()` là "tôi sẵn sàng rồi, để điện thoại trên bàn nhé". `accept()` là hành động "nhấc máy" khi có chuông gọi đến (khi một client gọi `connect()`).*

**Câu 191:** Mạng P2P có đặc tính "chịu lỗi" (Fault tolerance) tốt hơn Client-Server tập trung vì sao?
A. P2P luôn dùng cáp quang ngầm.
B. Do tài nguyên lưu trữ và tính toán được PHÂN TÁN khắp nơi. Máy tính A hỏng thì bạn có thể chuyển sang tải từ máy tính B, C, D (vẫn có file đó).
C. P2P không dùng hệ thống tệp.
D. IP của P2P là tĩnh tuyệt đối.
*Đáp án: B*
*Giải thích: Mạng ngang hàng (Blockchain, Torrent) không bao giờ sụp đổ miễn là còn ít nhất 1 node đang sống sót và nắm giữ dữ liệu.*

**Câu 192:** Tại sao các tệp video chất lượng 4K ít khi được truyền trên giao thức SMTP?
A. SMTP cấm video 4K.
B. Video 4K không chạy được trên Windows.
C. Kích thước file cực lớn, trong khi cấu trúc mã hóa Base64 của MIME qua SMTP làm phình to tệp tin thêm 33%, và nhiều máy chủ Email (như Gmail) giới hạn đính kèm ở mức 25MB.
D. IP không hỗ trợ gói lớn.
*Đáp án: C*
*Giải thích: Đính kèm file qua email cực kỳ vô lý nếu file quá to. Các nhà cung cấp chuyển sang cách đẩy file lên Google Drive (Cloud HTTP) rồi gắn 1 cái Link vào email.*

**Câu 193:** Chuẩn HTTP/1.0, mỗi lần tải một file HTML và 3 cái ảnh, thì máy khách phải làm gì?
A. Mở 1 kết nối TCP.
B. Mở 4 kết nối TCP độc lập (1 cho HTML, 3 cho ảnh) do TCP bị đóng ngay sau mỗi file (Non-persistent).
C. Đổi sang giao thức UDP.
D. Mở 1 UDP và 3 TCP.
*Đáp án: B*
*Giải thích: Non-persistent (Không bền vững) ở HTTP/1.0 làm trình duyệt kiệt sức vì RTT khởi tạo (handshake) bị lặp lại quá nhiều lần.*

**Câu 194:** Khi bạn thiết kế một App tin nhắn nội bộ công ty (Intranet Chat), điều quan trọng nhất về bảo mật ở tầng Ứng dụng mà bạn cần triển khai là gì?
A. Mã hóa Base64 cho mọi tin nhắn.
B. Gắn địa chỉ MAC vào tin nhắn.
C. Triển khai giao thức TLS/SSL (để mã hóa End-to-End hoặc Client-to-Server) bảo vệ đoạn chat khỏi bị ai đó dùng Packet Sniffer cắm vào cổng Switch đọc trộm.
D. Chạy qua VPN.
*Đáp án: C*
*Giải thích: Nếu viết một ứng dụng TCP Socket thuần (truyền String), mọi ký tự đều lỏa thể (clear-text) bay qua mạng. App chat buộc phải "bọc" kết nối bằng thư viện TLS (Ví dụ HTTPS, WSS).*

**Câu 195:** "Head-of-line blocking" trong giao thức HTTP/1.1 (Pipeline) xảy ra theo cơ chế nào?
A. Gói tin bị kẹt ở bộ đệm Router.
B. Máy chủ nhận được yêu cầu lấy file Video 10GB và file Icon 10KB. Vì gửi tuần tự trên 1 ống TCP, file Video to đùng chèn cứng đường truyền, file Icon nhỏ bé đứng xếp hàng phía sau phải chờ mỏi mòn mới được gửi.
C. Lỗi đọc ổ cứng.
D. Client khóa TCP.
*Đáp án: B*
*Giải thích: Vấn đề giống việc mua 1 món hàng nhỏ nhưng phải đứng tính tiền sau người mua 100 món. HTTP/2 giải quyết bằng cách "băm" Video và Icon thành mảnh nhỏ và gửi xen kẽ (Multiplexing).*

**Câu 196:** "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36..." là một header thường bị Hacker lợi dụng để làm gì?
A. Trộm tài khoản ngân hàng.
B. Kẻ tấn công có thể giả mạo (Spoof) chuỗi User-Agent này thành chuỗi của Google Bot (Trình thu thập dữ liệu web của Google) nhằm đánh lừa Tường lửa hoặc để lách qua các hàng rào chống chặn IP.
C. Bắt gói tin Wi-Fi.
D. Cấp sai IP cho nạn nhân.
*Đáp án: B*
*Giải thích: Header này có thể gõ bừa được. Kẻ xấu thường viết script cào dữ liệu (Scraping) giả danh là trình duyệt Firefox xịn để Server không cấm cửa (Ban).*

**Câu 197:** Dịch vụ DNS (Domain Name System) là thành phần hạ tầng quan trọng, do đó Port nào dưới đây LUÔN LUÔN CẦN MỞ trên Tường lửa đối với máy tính cá nhân để lướt Web bình thường?
A. Mở Port 53 UDP chiều ra (Outbound).
B. Đóng Port 80.
C. Mở Port 25 UDP.
D. Đóng toàn bộ Port.
*Đáp án: A*
*Giải thích: Nếu tường lửa máy bạn cấm Port 53 ra ngoài, Browser không thể gọi hàm `gethostbyname()`, do đó không đổi chữ google.com ra IP được, gây sập Web hoàn toàn.*

**Câu 198:** Vì sao các mạng Botnet lại thích sử dụng cấu trúc điều khiển P2P thay vì dùng Máy chủ ra lệnh trung tâm (C&C Server) cổ điển?
A. P2P dễ lập trình hơn.
B. P2P chạy trên UDP.
C. Máy chủ C&C tĩnh rất dễ bị cơ quan an ninh mạng xác định IP, thu giữ phần cứng và đánh sập toàn bộ Botnet. Mô hình P2P cho phép Botnet phát lệnh lan truyền không có máy chủ cố định.
D. P2P tự tạo ra virus mới.
*Đáp án: C*
*Giải thích: Botnet hiện đại (như Zeus, Mirai có P2P module) khiến việc "chặt đầu rắn" trở nên vô vọng. Không có Server đầu sỏ, các PC ma tự rỉ tai nhau để nhận lệnh tấn công.*

**Câu 199:** Một "Proxy Đảo ngược" (Reverse Proxy) và một "Proxy Chuyển tiếp" (Forward Proxy) khác nhau về đối tượng phục vụ như thế nào?
A. Không khác biệt.
B. Forward Proxy bảo vệ và giấu IP của MÁY KHÁCH (Người lướt web). Reverse Proxy bảo vệ và giấu IP của MÁY CHỦ (Web Server).
C. Cả 2 cùng giấu IP máy khách.
D. Cả 2 cùng giấu IP máy chủ.
*Đáp án: B*
*Giải thích: Khi bạn cài ứng dụng VPN hoặc Fake IP, bạn đang dùng Forward Proxy (Server Web nghĩ bạn ở Mỹ). Khi bạn cấu hình Cloudflare cho trang web của bạn, bạn dùng Reverse Proxy (Khách vào web nghĩ Server bạn ở Mỹ).*

**Câu 200:** Mã trạng thái `200 OK` của HTTP phản hồi cho máy khách biết điều gì?
A. Web yêu cầu đăng nhập.
B. Đường dẫn sai.
C. Request đã được Máy chủ tiếp nhận thành công và kết quả yêu cầu đang được trả về ngay trong Body.
D. Mất kết nối DB.
*Đáp án: C*
*Giải thích: 200 OK là tín hiệu "Vạn sự như ý" của Web. Trình duyệt bắt đầu nhận và vẽ HTML.*

**Câu 201:** Trong cấu trúc Tên miền `www.hust.edu.vn`, thuật ngữ `.edu` thể hiện điều gì?
A. Chỉ định đây là hệ thống DNS gốc.
B. Top-Level Domain (TLD) dành cho Khối giáo dục (Education).
C. Tên miền do quân đội cung cấp.
D. Địa chỉ MAC.
*Đáp án: B*
*Giải thích: Các đuôi (TLD) mang ý nghĩa phân loại tổ chức hoặc quốc gia. edu (Trường học), gov (Chính phủ), com (Thương mại).*

**Câu 202:** Khi một máy trạm truy cập Internet, thông số `Default Gateway` cấu hình trong card mạng IP thường sẽ trỏ về thiết bị nào?
A. Switch mạng LAN.
B. Modem cáp quang.
C. Địa chỉ IP LAN (Interface) của Bộ định tuyến (Router) trong nhà bạn, thiết bị chịu trách nhiệm chuyển gói tin RA KHỎI subnet hiện tại.
D. Máy chủ DNS Google (8.8.8.8).
*Đáp án: C*
*Giải thích: Gateway (Cổng ra vào) là nơi PC gửi mọi gói tin có đích đến KHÔNG NẰM TRONG mạng cục bộ. Router nhà bạn sẽ tóm lấy gói đó và ném ra Internet.*

**Câu 203:** Kỹ thuật nào giúp các lập trình viên gọi thực thi một hàm (Function) nằm trên một máy chủ Mạng khác ở xa y hệt như gọi hàm trên máy tính cục bộ?
A. FTP
B. RPC (Remote Procedure Call)
C. DHCP
D. ARP
*Đáp án: B*
*Giải thích: RPC (và sau này là gRPC) đóng gói các tham số hàm, chuyển qua mạng, Server chạy hàm, gói kết quả trả về. Nó che giấu đi sự phức tạp của tầng Mạng đối với Lập trình viên.*

**Câu 204:** Dịch vụ "Web Hosting" thực chất là việc bạn đang thuê thứ gì?
A. Thuê một sợi cáp mạng.
B. Thuê không gian Ổ cứng (Storage), CPU, RAM và IP Public trên một Máy chủ (Server) đang chạy liên tục phần mềm Web Server (như Apache/Nginx) ở một Data Center.
C. Thuê một tên miền đẹp.
D. Mua đứt một phần mềm duyệt web.
*Đáp án: B*
*Giải thích: Đưa Web lên mạng (Deploy) nghĩa là cóp code từ laptop ném lên một cái máy tính mạnh hơn, cắm mạng 24/7 (Hosting) để thiên hạ truy cập.*

**Câu 205:** Vì sao chuẩn mã hóa HTTP sang HTTPS trở thành "Bắt buộc" trên mọi trang web thế kỷ 21?
A. Nó giúp hình ảnh net hơn.
B. Nó bảo vệ quyền riêng tư người dùng khỏi bị Sniffing mật khẩu, đồng thời chứng thực (Authentication) trang web đó LÀ THẬT bằng Chứng chỉ số (Digital Certificate), chống trang giả mạo (Phishing).
C. Nó tăng kích thước file.
D. Cáp quang bắt buộc dùng mã hóa.
*Đáp án: B*
*Giải thích: HTTP gửi Text gốc. HTTPS dùng SSL/TLS mã hóa dữ liệu. CA (Certificate Authority) cấp thẻ chứng minh trang web đó thực sự là của ngân hàng VCB, chứ không phải trang lừa đảo.*

**Câu 206:** Giao thức nào chuyên xử lý việc chia sẻ Tên máy tính thành Địa chỉ IP trên các mạng nội bộ (Local/Multicast) thay cho DNS?
A. PING
B. mDNS (Multicast DNS) / Bonjour
C. OSPF
D. RIP
*Đáp án: B*
*Giải thích: Khi bạn cắm máy in HP vào mạng Wi-Fi nhà, mDNS giúp laptop Macbook tìm ra tên máy in là `HP-Printer.local` mà không cần bạn phải tự thiết lập Máy chủ DNS.*

**Câu 207:** Cấu trúc JSON `{"name":"John", "age":30}` được đóng gói ở khu vực nào của một gói tin HTTP POST?
A. Headers
B. Request Line
C. Message Body (Thân thông điệp)
D. URL Parameters
*Đáp án: C*
*Giải thích: HTTP Header chứa metadata (`Content-Type: application/json`), HTTP Body chứa Dữ liệu tải trọng thực sự (JSON string).*

**Câu 208:** Phương thức HTTP `OPTIONS` thường được Trình duyệt tự động kích hoạt trước khi gửi dữ liệu sang một tên miền KHÁC với tên miền hiện tại. Hành động này gọi là gì?
A. Tấn công DDoS.
B. Truy vấn Preflight Request để kiểm tra CORS (Cross-Origin Resource Sharing) xem Web B có cấp quyền cho phép Trình duyệt lấy tài nguyên không.
C. Mã hoá Cookie.
D. Đăng xuất tài khoản.
*Đáp án: B*
*Giải thích: Vì tính bảo mật (Same-origin policy), Trình duyệt sẽ rụt rè gửi hàm OPTIONS hỏi Web B: "Ê, tao đang đứng ở Web A, tao gửi file cho mày có được không?". Nếu Web B bảo "OK", thì trình duyệt mới dám gửi lệnh POST.*

**Câu 209:** Cơ chế "Long Polling" trong thiết kế Web thời gian thực cải tiến điều gì so với "Polling" thường?
A. Giảm dung lượng file tải.
B. Máy khách gửi Request, Máy chủ CỐ TÌNH CHƯA TRẢ LỜI NGAY, treo/giữ kết nối đó đến khi thực sự CÓ TIN NHẮN MỚI thì mới trả về. Sau đó Client lập tức gửi Request Long Polling mới.
C. Bỏ qua DNS hoàn toàn.
D. Chạy qua UDP.
*Đáp án: B*
*Giải thích: Khắc phục nhược điểm "hỏi liên tục" gây tốn tài nguyên. Máy chủ chỉ phản hồi khi có Data, giúp App phản hồi tin nhắn tức thì (Real-time).*

**Câu 210:** Định dạng XML và JSON là chuẩn quy định về yếu tố nào ở Tầng Presentation/Application?
A. Băng thông cáp.
B. Cú pháp và Định dạng cấu trúc (Syntax & Semantics) cho dữ liệu truyền tải, giúp 2 máy tính khác HĐH (Windows và Linux) vẫn đọc hiểu dữ liệu của nhau.
C. Thay đổi IP.
D. Đóng gói Frame L2.
*Đáp án: B*
*Giải thích: XML và JSON định nghĩa cách dữ liệu được diễn đạt. Dù server viết bằng Java, client viết bằng Swift (iOS), chúng vẫn nói chung một ngôn ngữ JSON.*

**Câu 211:** Một đặc tính vô cùng quan trọng của các ứng dụng phi tập trung (DApp) chạy trên nền tảng Blockchain (như Web3) là gì?
A. Phải có một máy chủ trung tâm cực mạnh ở Thung lũng Silicon.
B. Không sử dụng tầng Application.
C. Backend của ứng dụng là các Hợp đồng thông minh (Smart Contract) chạy trên mạng lưới P2P gồm hàng ngàn máy tính toàn cầu, không thể bị đánh sập hay bị kiểm duyệt bởi một thực thể duy nhất.
D. Dùng TCP/IP nhưng không có địa chỉ MAC.
*Đáp án: C*
*Giải thích: Web2 lưu dữ liệu ở Server Amazon/Google. Web3 lưu dữ liệu phân tán trên mạng lưới ngang hàng (P2P).*

**Câu 212:** "MIME type" (hoặc Media Type) có định dạng `text/html` báo cho hệ thống biết điều gì?
A. Rằng đây là một file văn bản định dạng HTML để trình duyệt tự hiểu cách render.
B. Rằng tốc độ mạng rất chậm.
C. Rằng tệp tin chứa virus.
D. Đóng cổng 80.
*Đáp án: A*
*Giải thích: Trình duyệt nhìn `text/html` sẽ vẽ web, nhìn `image/png` sẽ vẽ ảnh, nhìn `application/pdf` sẽ mở trình đọc PDF.*

**Câu 213:** "Rate Limiting" (Giới hạn tốc độ) là kỹ thuật ở API dùng để:
A. Tăng băng thông.
B. Kiểm soát số lượng Request mà một Client (IP) được phép gửi đến Server trong 1 phút, nhằm chống lại Brute-force mật khẩu hoặc Spam/DDoS.
C. Mã hóa kết nối.
D. Thay đổi DNS.
*Đáp án: B*
*Giải thích: Ví dụ API Server sẽ chặn nếu bạn gọi API 100 lần trong 1 giây (trả về lỗi HTTP 429 Too Many Requests).*

**Câu 214:** Ứng dụng quản lý mạng (NMS) thường vẽ các biểu đồ băng thông. Nó dùng giao thức nào đi gom dữ liệu từ thiết bị Switch/Router?
A. HTTPS
B. SMTP
C. SNMP (Simple Network Management Protocol)
D. LDAP
*Đáp án: C*
*Giải thích: NMS dùng SNMP gửi các lệnh GET để rút dữ liệu về lượng traffic đã đi qua các port của Switch.*

**Câu 215:** Trong kiến trúc mạng, "Thin Client" (Máy khách mỏng) là mô hình như thế nào?
A. Máy tính siêu mỏng nhẹ của Apple.
B. Thiết bị cá nhân có phần cứng rất yếu (ít RAM, CPU), MỌI TÁC VỤ xử lý nặng nề, lưu trữ file đều được đẩy hoàn toàn lên Máy chủ (Server) trên Cloud. Máy khách chỉ làm nhiệm vụ hiển thị màn hình (như VDI / Cloud Gaming).
C. Điện thoại bị chai pin.
D. Router bỏ túi.
*Đáp án: B*
*Giải thích: Ứng dụng Cloud Gaming (GeForce Now) là một Thin Client. Máy tính bạn chỉ cần xem Video màn hình do Server gửi về.*

**Câu 216:** Phương thức "Server-Sent Events" (SSE) trên HTTP có điểm khác biệt với WebSocket là gì?
A. SSE là giao thức bảo mật.
B. WebSocket mở liên kết HAI CHIỀU (Client gửi, Server gửi). SSE mở liên kết MỘT CHIỀU (Chỉ Server được quyền Đẩy - Push dữ liệu liên tục về cho Client).
C. SSE chạy qua cổng 21.
D. SSE dùng giao thức ARP.
*Đáp án: B*
*Giải thích: Nếu ứng dụng chỉ cần lấy Tỷ số bóng đá (Server báo liên tục về), dùng SSE nhẹ hơn WebSocket.*

**Câu 217:** Ứng dụng FTP khi sử dụng ở chế độ "Active Mode", ai là người chủ động khởi tạo kết nối Mạng dữ liệu (Data Connection Port 20)?
A. Máy trạm (Client) gọi cho Máy chủ (Server).
B. Máy chủ (Server) gọi ngược lại cho Máy trạm (Client).
C. Không cần khởi tạo.
D. Gọi qua DNS.
*Đáp án: B*
*Giải thích: Ở Active Mode, Client nói "Tôi đang chờ ở Port 5000". Server chủ động dùng Port 20 kết nối vào Port 5000 của Client. Rất rủi ro nếu Client có tường lửa chặn kết nối in-bound.*

**Câu 218:** Tên miền Quốc tế có ký tự đặc biệt (ví dụ `tiếngviệt.vn`) được mã hoá ngầm thành chuẩn ASCII (như `xn--tingvit-cwa90b.vn`) bằng kỹ thuật nào trong DNS?
A. Base64
B. UTF-8
C. Punycode
D. IPsec
*Đáp án: C*
*Giải thích: DNS Root chỉ làm việc với bảng chữ cái ASCII [a-z,0-9]. Punycode giúp đổi các ký tự Quốc tế (IDN) thành chuỗi ASCII để Server hiểu.*

**Câu 219:** Trong quá trình "Bắt tay" (Handshake) thiết lập SSL/TLS, thao tác nào quan trọng nhất để Server chứng minh nó là thật (không mạo danh)?
A. Gửi cho Client 1 GB dữ liệu ngẫu nhiên.
B. Server gửi cho Client "Chứng chỉ số" (Digital Certificate) của mình, chứa Khóa công khai (Public Key) đã được ký duyệt (Signed) bởi một Tổ chức xác thực uy tín (CA).
C. Server bắt Client đọc thẻ tín dụng.
D. Tắt mã hóa.
*Đáp án: B*
*Giải thích: Giống như Xuất trình Căn cước công dân có mộc đỏ của Công an. Client kiểm tra mộc đỏ (Chữ ký CA), nếu hợp lệ thì tin tưởng đây đúng là Server ngân hàng.*

**Câu 220:** Giao thức nào hoạt động dựa trên cơ sở dữ liệu phi tập trung, thường được dùng để thay thế DNS nội bộ trong các hệ điều hành Apple?
A. DNSSEC
B. FTP
C. Bonjour / mDNS
D. HTTPS
*Đáp án: C*
*Giải thích: Công nghệ Zero-configuration networking (Bonjour của Apple) dùng Multicast DNS để tự phát hiện máy in, màn hình Apple TV trong mạng LAN nội bộ.*

**Câu 221:** Một Email Message (Thông điệp) khi được Client A soạn và bấm GỬI, nó sẽ đi qua các chặng nào theo lý thuyết SMTP/IMAP?
A. Client A -> SMTP -> Mail Server A -> Internet SMTP -> Mail Server B -> IMAP -> Client B.
B. Client A -> Client B trực tiếp.
C. Client A -> FTP Server -> Client B.
D. Client A -> HTTP -> DNS -> Client B.
*Đáp án: A*
*Giải thích: Máy gửi đẩy thư lên Server Bưu điện của nó. Bưu điện của nó tự tìm đường đẩy sang Bưu điện của người nhận. Máy nhận lấy thư từ Bưu điện người nhận về đọc.*

**Câu 222:** Kích thước MTU chuẩn thường gặp nhất trên giao diện mạng cáp (Ethernet) là bao nhiêu, quyết định giới hạn chia nhỏ Segment của tầng Transport?
A. 512 bytes
B. 1500 bytes
C. 9000 bytes (Jumbo frames)
D. Vô cực
*Đáp án: B*
*Giải thích: TCP phải chia dữ liệu thành Segment có kích thước MSS (Maximum Segment Size) thường là 1460 bytes, để cộng thêm 40 byte IP/TCP Header là vừa tròn 1500 bytes (MTU).*

**Câu 223:** Lệnh `nslookup -type=mx google.com` yêu cầu máy chủ DNS cung cấp thông tin gì?
A. IP của máy chủ Web Google.
B. Tên của các máy chủ quản lý hộp thư Email nhận `@google.com`.
C. Thời gian sống của DNS.
D. Mật khẩu Wi-Fi.
*Đáp án: B*
*Giải thích: `type=mx` là yêu cầu tra cứu bản ghi loại MX (Mail Exchanger) để biết Google dùng Mail server tên gì.*

**Câu 224:** HTTP/1.0, HTTP/1.1 và HTTP/2.0 đều sử dụng giao thức giao vận bên dưới là:
A. UDP
B. ICMP
C. TCP
D. QUIC
*Đáp án: C*
*Giải thích: Toàn bộ gia đình HTTP truyền thống đều xây dựng trên độ tin cậy của ống dẫn TCP. Bắt đầu từ HTTP/3 mới chuyển sang UDP/QUIC.*

**Câu 225:** Khi người dùng thay đổi ISP (Ví dụ từ Viettel sang VNPT), họ có bắt buộc phải thay đổi địa chỉ Tên miền website cá nhân (VD: ten-toi.com) không?
A. Có, tên miền phải đi theo ISP.
B. Không, Tên miền là độc lập với mạng vật lý. Người dùng chỉ cần vào hệ thống DNS trỏ lại bản ghi A sang địa chỉ IP Public mới do ISP VNPT cấp là Website hoạt động bình thường với tên cũ.
C. Có, phải nộp tiền mua tên miền khác.
D. Web sẽ sập vĩnh viễn.
*Đáp án: B*
*Giải thích: DNS tạo ra mức ảo hóa Lớp ứng dụng hoàn hảo. Tên miền như biển số xe, khi bạn đổi nhà (đổi IP), bạn chỉ lên ủy ban (DNS Server) cập nhật địa chỉ hộ khẩu mới, mọi người vẫn dùng biển số cũ để tìm bạn.*

**Câu 226:** Web Cookie có thể bị kẻ tấn công lấy cắp qua đường truyền không mã hoá. Lập trình viên Web có thể thêm cờ (Flag) nào vào Header Set-Cookie để yêu cầu Trình duyệt CHỈ GỬI Cookie này khi liên kết là HTTPS?
A. Secure Flag
B. HttpOnly Flag
C. Domain Flag
D. Path Flag
*Đáp án: A*
*Giải thích: Nếu gắn thẻ `Secure`, kể cả khi người dùng truy cập web bằng HTTP (không mã hóa), Browser sẽ KHÔNG đính kèm Cookie đó, phòng ngừa gói tin bị Sniffing dọc đường.*

**Câu 227:** Thẻ "HttpOnly" trên Web Cookie có chức năng bảo mật gì?
A. Chỉ dùng được trên cáp đồng.
B. Nó CHẶN (Ngăn cản) mã lệnh Javascript (nhạy cảm ở phía Client) gọi hàm `document.cookie` để đọc Cookie đó, giúp chống lại hình thức trộm Cookie qua mã độc XSS.
C. Buộc phải dùng cáp quang.
D. Đổi Cookie sang địa chỉ IP.
*Đáp án: B*
*Giải thích: Cookie HttpOnly chỉ được Browser tự động gắn vào Header để gửi đi cho Server, JavaScript không thể chạm tay vào.*

**Câu 228:** Lệnh `wget` hoặc `curl` trong Linux/Mac được sử dụng ở tầng Ứng dụng để làm gì?
A. Xoá RAM máy tính.
B. Giao tiếp với các giao thức HTTP, FTP, HTTPS qua giao diện dòng lệnh (Command Line) để tải nội dung trang web hoặc file, thường dùng trong tự động hóa và tạo API request.
C. Mã hóa toàn bộ ổ đĩa.
D. Dịch tên miền.
*Đáp án: B*
*Giải thích: Curl giống như một "Trình duyệt không có giao diện đồ họa", rất mạnh để debug API.*

**Câu 229:** Hệ thống P2P "Skype" (đời cũ) sử dụng công cụ/dịch vụ trung tâm duy nhất làm gì dù nó là ứng dụng phân tán?
A. Làm kho chứa File.
B. Lưu trữ toàn bộ tin nhắn chat.
C. Máy chủ Login Central (Đăng nhập trung tâm) để xác thực tài khoản và kiểm tra xem người dùng có Online không, sau đó mới thả cho các máy khách tự tìm đường P2P gọi cho nhau.
D. Để cấp phát IP.
*Đáp án: C*
*Giải thích: Dù P2P, tài khoản và mật khẩu bắt buộc phải quản lý ở hệ thống Tập trung (Client-Server) để đảm bảo bảo mật và duy nhất.*

**Câu 230:** Định lý CAP trong việc phân tán cơ sở dữ liệu (Cloud/DNS/Web Services) chỉ ra rằng một hệ thống phân tán chỉ có thể đáp ứng tối đa 2 trên 3 đặc tính nào?
A. Control, Area, Protocol.
B. CPU, ALU, Program.
C. Consistency (Nhất quán), Availability (Khả dụng), Partition tolerance (Khả năng chịu chia cắt mạng).
D. Connection, Authentication, Privacy.
*Đáp án: C*
*Giải thích: Trong kiến trúc hệ thống mạng Application lớn, không thể có ứng dụng nào thỏa mãn cả 3. Ví dụ: DNS hy sinh Tính nhất quán (đổi IP đôi khi mất 24h mới cập nhật hết) để đánh đổi lấy Tính Khả dụng cực cao.*

**Câu 231:** Kiến trúc Microservices (Dịch vụ vi mô) đang thay thế kiến trúc Monolithic (Nguyên khối) trong phát triển Web Application. Ứng dụng mạng hỗ trợ mô hình này như thế nào?
A. Gom tất cả vào 1 file EXE duy nhất.
B. Các Module nhỏ lẻ (như Thanh toán, Đơn hàng, Người dùng) chạy ở các Máy chủ (Container) độc lập khác nhau và giao tiếp với nhau QUA MẠNG bằng các HTTP API (REST/gRPC), thay vì gọi hàm trực tiếp trong RAM.
C. Bỏ qua tầng Application.
D. Dùng duy nhất IP tĩnh cho mọi dịch vụ.
*Đáp án: B*
*Giải thích: Mạng đóng vai trò sống còn trong Microservices vì mọi giao tiếp nội bộ giờ đây đều trở thành Network Request.*

**Câu 232:** Trong CDN, khái niệm "Cache Hit Ratio" (Tỉ lệ Hit) ám chỉ:
A. Tỉ lệ số lượng Hacker tấn công.
B. Tỉ lệ % các yêu cầu Web (Requests) được trả lời NGAY TỪ BỘ NHỚ ĐỆM của CDN mà không phải chuyển ngược về Máy chủ Gốc (Origin Server) lấy dữ liệu.
C. Mức phần trăm dung lượng CPU bị quá tải.
D. Số lượng gói tin rớt mạng.
*Đáp án: B*
*Giải thích: Tỉ lệ này càng cao (vd > 95%), có nghĩa là CDN hoạt động cực kỳ hiệu quả, Server Gốc gần như được "ngồi chơi".*

**Câu 233:** Phương thức nào sau đây của HTTP được dùng cho mục đích "Chẩn đoán" hoặc gỡ lỗi, yêu cầu Máy chủ trả ngược lại nguyên vẹn thông điệp Request mà nó nhận được?
A. OPTIONS
B. TRACE
C. PUT
D. PATCH
*Đáp án: B*
*Giải thích: TRACE giúp lập trình viên hoặc Tester nhìn thấy Request của họ có bị các Proxy trung gian bóp méo, thêm bớt Header hay không.*

**Câu 234:** Một trong các lý do khiến Streaming Video cần sử dụng Giao thức Tầng Ứng dụng thông minh (như DASH) thay vì chỉ tải Video như File tĩnh (FTP) là gì?
A. DASH nén file tốt hơn FTP.
B. Video qua DASH không bị dính mã độc.
C. DASH cho phép nhảy cóc (Seek/Tua nhanh) video và chọn chất lượng mạng linh hoạt. Tải File tĩnh buộc phải nhận theo thứ tự từ đầu đến cuối 1 chất lượng duy nhất.
D. File tĩnh cấm dùng TCP.
*Đáp án: C*
*Giải thích: Nếu xem File dạng HTTP thô hoặc FTP, bạn phải đợi tải 50% file mới tua đến đoạn giữa được. DASH băm nhỏ video, nên bạn tua đến đoạn 50%, Browser chỉ cần Get chunk số 500.*

**Câu 235:** Tại sao mật khẩu được truyền qua phương thức POST (khi nhập vào form Web) CÓ THỂ an toàn hơn khi truyền qua phương thức GET, mặc dù CẢ HAI ĐỀU CHƯA MÃ HOÁ (nếu chạy trên HTTP)?
A. POST mạnh hơn GET 10 lần.
B. POST dùng TCP, GET dùng UDP.
C. GET gắn mật khẩu lên URL, dễ bị lộ trên màn hình, lưu trong lịch sử Web (History), Bookmark, và các Log của Router/Proxy. POST gói mật khẩu trong Body, ẩn khỏi các bản ghi bề nổi.
D. POST tự tạo HTTPS.
*Đáp án: C*
*Giải thích: Cả 2 đều kém bảo mật nếu bị Sniff (nghe lén dọc đường) khi không có HTTPS. Nhưng GET còn nguy hiểm hơn vì phơi bày lộ liễu trên thanh URL và các file Log của Server.*

**Câu 236:** Tính năng "Virtual Hosting" (Lưu trữ ảo) của Máy chủ Web Apache / Nginx giúp giải quyết trực tiếp vấn đề hạn chế nào của Internet?
A. Thiếu điện năng.
B. Sự khan hiếm của không gian địa chỉ IPv4 (Một IP Public có thể cõng hàng trăm Website khác tên miền nhờ phân biệt qua Header `Host:`).
C. Tốc độ quay của ổ cứng.
D. Mạng Wi-Fi bị tắc nghẽn.
*Đáp án: B*
*Giải thích: Nếu mỗi Domain `.com` phải mua 1 IP độc lập, 4 tỷ IP của IPv4 đã hết sạch từ những năm 2000. Shared Hosting giúp tối ưu tài nguyên IP công cộng.*

**Câu 237:** Lỗ hổng DDoS "Amplification" (Tấn công khuếch đại) thường lợi dụng Giao thức mạng có đặc tính nào?
A. Giao thức chỉ yêu cầu 1 kết nối duy nhất.
B. Giao thức chạy trên nền UDP không có xác thực (ví dụ DNS, NTP, Memcached). Hacker gửi 1 gói tin Request giả mạo rất nhỏ (50 bytes) nhưng Server sẽ dội 1 gói Response trả lời CỰC KỲ LỚN (3000 bytes) về cho IP nạn nhân (Do bị Spoof).
C. Giao thức dùng cáp quang.
D. TCP 3-way handshake.
*Đáp án: B*
*Giải thích: Tính phi kết nối (Connectionless) của UDP khiến DNS Server không biết gói hỏi có phải của nạn nhân thật hay không. Kẻ gian "mượn dao giết người", biến DNS Server thành pháo đài nã đạn khổng lồ vào nạn nhân.*

**Câu 238:** SMTP là viết tắt của:
A. Server Message Transfer Protocol
B. Secure Mail Transmission Protocol
C. Simple Mail Transfer Protocol
D. Short Message Text Protocol
*Đáp án: C*
*Giải thích: "Simple" (Đơn giản) vì nó được thiết kế từ thập niên 80 với các lệnh văn bản thuần tuý cực kỳ nguyên thuỷ (HELO, MAIL, DATA).*

**Câu 239:** Ứng dụng "Torrent" cần có Port Forwarding hoặc UPnP bật trên Router vì sao?
A. Torrent cần mã hoá Wi-Fi.
B. Để máy tính của người dùng khác trên Internet CÓ THỂ CHỦ ĐỘNG KHỞI TẠO kết nối đến máy bạn để xin tải mảnh ghép. Nếu bị Router NAT chặn, bạn chỉ có thể hút (leech) mà không làm Seeder hiệu quả được.
C. Để tăng dung lượng ổ cứng.
D. Để cấp IP.
*Đáp án: B*
*Giải thích: Nếu 2 người dùng đều bị Firewall chặn kết nối Inbound, họ không thể gọi điện thẳng cho nhau. Một người phải mở Port (Chọc lủng NAT) để người kia gọi vào.*

**Câu 240:** Header `Referer` (hay Referrer) trong HTTP Request thường được các Website (như Facebook) sử dụng để làm gì?
A. Để biết loại Trình duyệt.
B. Để tìm Địa chỉ IP.
C. Để biết MÁY KHÁCH VỪA CLICK LINK TỪ TRANG WEB NÀO sang trang hiện tại (Nhằm phân tích hành vi, thống kê nguồn truy cập hoặc chống tấn công CSRF).
D. Để nén file.
*Đáp án: C*
*Giải thích: Nếu bạn click 1 link Tiki trên Facebook, trình duyệt gửi cho Tiki 1 request kèm `Referer: facebook.com`. Tiki dùng nó để tính tiền hoa hồng cho Facebook.*

**Câu 241:** Mã phản hồi (Status Code) 502 "Bad Gateway" xuất hiện trên trình duyệt thường có nghĩa là:
A. Proxy hoặc Load Balancer (Đóng vai trò Gateway) ở tầng ngoài cùng nhận được Request của bạn, mang đi hỏi Server Backend bên trong nhưng Server Backend từ chối hoặc trả về phản hồi lỗi/không hợp lệ.
B. Quên mật khẩu.
C. Lỗi cáp Wi-Fi.
D. Trình duyệt chưa cập nhật.
*Đáp án: A*
*Giải thích: Lỗi này xảy ra nhiều trên các mô hình Microservices, khi cái "cửa ngõ" Nginx chạy bình thường, nhưng ứng dụng NodeJS bên trong bị sập.*

**Câu 242:** Kỹ thuật CORS (Cross-Origin Resource Sharing) trong Trình duyệt nhằm nới lỏng chính sách nào của Web?
A. Tắt Tường lửa.
B. Bỏ qua Same-Origin Policy (Chính sách cùng nguồn gốc). CORS cho phép một trang web ở tên miền A lấy được API/Dữ liệu từ một tên miền B, miễn là B có Header cấp phép `Access-Control-Allow-Origin: A`.
C. Chống mã hóa.
D. Khóa chặn Cookie.
*Đáp án: B*
*Giải thích: Web A (abc.com) dùng Javascript tải ngầm dữ liệu từ API B (api.xyz.com) mặc định sẽ bị Trình duyệt khoá (vì nghi ngờ bị trộm dữ liệu chéo). B phải chủ động gật đầu (CORS) thì Trình duyệt mới thả.*

**Câu 243:** Tại sao Mạng Ứng dụng lớn (Big Tech) ngày nay dùng mô hình "Event-driven" (Hướng sự kiện - Message Broker như Kafka, RabbitMQ) thay vì gọi API đồng bộ liên tục?
A. Vì nó chặn IP nội bộ.
B. Gọi API đồng bộ (Synchronous) bắt hệ thống phải "chờ". Gửi tin vào Message Queue (Không đồng bộ) giúp hệ thống A nhả việc ngay, hệ thống B tự động bóc tin ra xử lý dần, chống SẬP SERVER KHI LƯU LƯỢNG ĐỘT BIẾN (Spike/Flash crowd).
C. Nó mã hóa toàn bộ dữ liệu.
D. Bắt buộc dùng IPv6.
*Đáp án: B*
*Giải thích: Đặt hàng Shopee ngày 11/11. Server không đủ sức ghi DB ngay, nó quăng 1000 đơn vào hàng đợi (Queue). Hệ thống chốt đơn từ từ nhặt ra xử lý. Tránh sập toàn tập.*

**Câu 244:** Header `Content-Encoding: gzip` trong HTTP mang lại tác dụng kinh tế nào nhất?
A. Tránh bị lộ mật khẩu.
B. Giảm 70-80% dung lượng thực tế của các file Văn bản (HTML, CSS, JS) truyền qua cáp mạng, giúp tăng tốc độ tải trang lên cực cao và giảm tiền cước băng thông cho cả Khách và Chủ.
C. Thay thế hình ảnh.
D. Chạy Web Socket.
*Đáp án: B*
*Giải thích: Các file Code (Text) lặp lại từ khoá rất nhiều (như thẻ `<div>`), nên thuật toán Nén (Gzip/Brotli) hoạt động vô cùng hiệu quả.*

**Câu 245:** "Web Crawler" (Google Bot) là phần mềm hoạt động ở tầng Ứng dụng. Nó gom dữ liệu toàn cầu bằng hành vi nào?
A. Đánh cắp ổ cứng.
B. Nó liên tục gửi các lệnh HTTP GET lấy file HTML, sau đó phân tích các thẻ `<a>` (link) trong nội dung để nhảy sang các trang web khác, tạo thành tấm bản đồ chỉ mục khổng lồ (Indexing).
C. Nghe lén cáp quang.
D. Quét Port DNS.
*Đáp án: B*
*Giải thích: Bot giống như một con nhện đi theo các sợi tơ (Hyperlinks) liên kết giữa các web để "cào" và lập chỉ mục nội dung về Google Search.*

**Câu 246:** Thuật ngữ "Stateful Protocol" (Giao thức có trạng thái) có nghĩa là:
A. Thiết bị bắt buộc phải cố định vị trí.
B. Giao thức yêu cầu duy trì, ghi nhớ bối cảnh (Context) và lịch sử của toàn bộ phiên kết nối (như FTP). Client và Server phải tốn RAM để nhớ "Chúng ta đang làm đến bước nào rồi".
C. Không hỗ trợ Windows.
D. Luôn chạy qua UDP.
*Đáp án: B*
*Giải thích: Ví dụ FTP là Stateful. Bạn đăng nhập -> Mở thư mục /abc -> FTP Server NHỚ rằng bạn đang đứng ở /abc để lấy file. HTTP (Stateless) thì không nhớ gì sất.*

**Câu 247:** Trong môi trường Email doanh nghiệp, việc cấu hình bản ghi "Autodiscover" hoặc "SRV" ở Máy chủ DNS giúp ích gì cho Tầng Ứng dụng?
A. Tự động mã hóa thư.
B. Ngăn chặn spam.
C. Giúp Ứng dụng (như Outlook, Apple Mail) TỰ ĐỘNG cấu hình các thông số máy chủ (IMAP/SMTP Server, Port, Tên miền) chỉ với việc người dùng nhập mỗi Email và Mật khẩu.
D. Thay đổi IP động.
*Đáp án: C*
*Giải thích: Cấu hình tay các port 993, 587, SSL/TLS rất phức tạp với người dùng thường. Nhờ bản ghi SRV trên DNS, Outlook tự tìm đến máy chủ lấy file cấu hình về dùng.*

**Câu 248:** Khi máy tính bạn ở VN tải một file qua giao thức HTTP từ máy chủ Mỹ, và một lúc sau bạn bè của bạn (cùng công ty) cũng tải chính file đó. Để tối ưu tốc độ cho bạn bè, công ty cài đặt một HTTP Proxy Cache (Squid). Máy chủ Mỹ có nhận được Request thứ hai không?
A. Có, nó luôn được nhận.
B. Không, yêu cầu thứ hai sẽ bị Proxy chặn ngay trong công ty và Proxy tự trả file lại cho người dùng thứ hai, Máy chủ Mỹ hoàn toàn không biết sự tồn tại của người thứ hai (nếu file Cache còn hạn).
C. Proxy tự động gửi yêu cầu xóa file.
D. Máy chủ Mỹ chuyển thành P2P.
*Đáp án: B*
*Giải thích: Proxy đóng vai trò "Mua sỉ bán lẻ". Proxy đi Mỹ lấy file về (Mua sỉ). Sau đó bạn bè hỏi, Proxy đem file trong kho ra đưa luôn (bán lẻ), không tốn vé máy bay sang Mỹ nữa.*

**Câu 249:** "Digital Signature" (Chữ ký số) trong Email ứng dụng khóa bảo mật gì?
A. Hash Code.
B. Asymmetric Key (Khoá bất đối xứng). Gửi bằng Khóa bí mật (Private Key) của người ký; Người nhận kiểm chứng (Verify) bằng Khóa công khai (Public Key) của người đó, chứng minh thư không bị giả mạo.
C. Mật khẩu Wi-Fi.
D. Header TCP.
*Đáp án: B*
*Giải thích: Không ai có Private Key ngoài bạn, nên nếu Public Key của bạn ráp vào mã đó thành công, chắc chắn 100% người gửi là bạn (Tính chống chối bỏ - Non-repudiation).*

**Câu 250:** Trong lịch sử, Ứng dụng/Giao thức mạng (Application Layer) đầu tiên châm ngòi cho sự bùng nổ của mạng Internet và làm thay đổi thế giới là gì?
A. BitTorrent
B. Skype (VoIP)
C. World Wide Web (HTTP/HTML/Trình duyệt) do Tim Berners-Lee phát minh năm 1989.
D. Zalo
*Đáp án: C*
*Giải thích: Trước WWW, Internet chỉ là các dòng lệnh (FTP/Telnet/Email lệnh Text) rất khô khan. WWW mang giao diện siêu liên kết (hyperlinks) và Đồ họa tới, tạo nên kỷ nguyên Internet hiện đại.*
