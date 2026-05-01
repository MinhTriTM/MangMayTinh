# CHƯƠNG 1: TRẮC NGHIỆM TỔNG QUAN VỀ MẠNG MÁY TÍNH VÀ INTERNET

**Câu 1:** Trong kiến trúc mạng Internet, thuật ngữ "End system" (hệ thống đầu cuối) đồng nghĩa với thuật ngữ nào sau đây?
A. Router (Bộ định tuyến)
B. Switch (Bộ chuyển mạch)
C. Host (Máy chủ/máy trạm)
D. Communication link (Đường truyền)
*Đáp án: C*
*Giải thích: Host là cách gọi khác của end system, ám chỉ các thiết bị đầu cuối như máy tính, điện thoại, máy chủ nằm ở rìa của mạng.*

**Câu 2:** Chức năng cốt lõi của giao thức (protocol) trong mạng máy tính là gì?
A. Điều khiển tốc độ quay của quạt làm mát trong bộ định tuyến.
B. Định nghĩa định dạng (format), thứ tự của các thông điệp được gửi/nhận và các hành động xử lý các thông điệp đó.
C. Mã hoá toàn bộ dữ liệu trước khi truyền đi để chống lại hacker.
D. Thay thế hoàn toàn phần cứng mạng bằng các đoạn mã lập trình phần mềm.
*Đáp án: B*
*Giải thích: Giao thức mạng đóng vai trò như ngôn ngữ giao tiếp, quy định cấu trúc và cách thức các thiết bị nói chuyện với nhau.*

**Câu 3:** Theo kiến trúc phân tầng Internet (TCP/IP), tầng nào chịu trách nhiệm tìm đường (định tuyến) cho gói tin từ trạm nguồn tới trạm đích thông qua mạng lưới các router trên toàn cầu?
A. Tầng Ứng dụng (Application Layer)
B. Tầng Giao vận (Transport Layer)
C. Tầng Mạng (Network Layer)
D. Tầng Liên kết (Link Layer)
*Đáp án: C*
*Giải thích: Tầng mạng (Network Layer) sử dụng các giao thức định tuyến và địa chỉ IP để chuyển datagram xuyên qua mạng lõi (routers).*

**Câu 4:** Trong các công nghệ mạng truy cập sau đây, công nghệ nào cung cấp đường truyền bằng sợi cáp quang trực tiếp tới tận nhà người dùng?
A. DSL (Digital Subscriber Line)
B. Cable (Hệ thống truyền hình cáp)
C. Ethernet LAN
D. FTTH (Fiber to the Home)
*Đáp án: D*
*Giải thích: FTTH (Fiber to the Home) là mạng cáp quang kéo trực tiếp đến hộ gia đình, cung cấp băng thông rất lớn so với cáp đồng hay cáp đồng trục.*

**Câu 5:** Kỹ thuật nào được thiết kế để dành riêng (reserve) toàn bộ tài nguyên trên tuyến đường từ nguồn đến đích trong suốt thời gian kết nối, giống như mạng điện thoại truyền thống?
A. Chuyển mạch gói (Packet Switching)
B. Chuyển mạch kênh (Circuit Switching)
C. Chuyển mạch thông điệp (Message Switching)
D. Lưu và chuyển tiếp (Store-and-forward)
*Đáp án: B*
*Giải thích: Circuit Switching dành riêng tài nguyên (băng thông) trong suốt phiên kết nối, đảm bảo tốc độ nhưng gây lãng phí nếu không có dữ liệu truyền.*

**Câu 6:** Internet ngày nay sử dụng phương pháp chuyển mạch nào làm nền tảng cốt lõi?
A. Chuyển mạch kênh bằng FDM
B. Chuyển mạch gói (Packet Switching)
C. Chuyển mạch kênh bằng TDM
D. Mạng điện thoại chuyển mạch công cộng (PSTN)
*Đáp án: B*
*Giải thích: Internet dựa trên Packet Switching, chia sẻ băng thông theo nhu cầu (statistical multiplexing), linh hoạt nhưng có thể xảy ra trễ hàng đợi.*

**Câu 7:** Một gói tin có kích thước L = 10,000 bits được đẩy vào một liên kết có tốc độ R = 10 Mbps. Bỏ qua các loại độ trễ khác, thời gian cần thiết để bộ định tuyến đẩy toàn bộ gói tin này lên đường dây (Transmission Delay) là bao nhiêu?
A. 1 ms (miligiây)
B. 10 ms
C. 0.1 ms
D. 100 ms
*Đáp án: A*
*Giải thích: Transmission Delay = L / R = 10,000 bits / 10,000,000 bps = 0.001 giây = 1 ms.*

**Câu 8:** Khoảng cách giữa hai thành phố là 2.000 km. Tốc độ lan truyền của tín hiệu trong cáp quang là $2*10^8$ m/s. Trễ lan truyền (Propagation Delay) giữa hai thành phố này là:
A. 10 ms
B. 1 ms
C. 100 ms
D. 20 ms
*Đáp án: A*
*Giải thích: Propagation Delay = Khoảng cách (d) / Tốc độ truyền (v) = 2,000,000 m / (2*10^8 m/s) = 0.01 giây = 10 ms.*

**Câu 9:** Hiện tượng mất gói tin (Packet Loss) xảy ra tại một router chủ yếu là do nguyên nhân nào?
A. Router bị mất điện đột ngột.
B. Cáp quang bị đứt do thi công.
C. Tốc độ gói tin tới cổng vào của router quá lớn, làm tràn bộ đệm hàng đợi (buffer overflow) khiến router phải loại bỏ các gói tin đến sau.
D. Gói tin có chứa mã độc (virus) nên bị router tiêu diệt.
*Đáp án: C*
*Giải thích: Khi hàng đợi đầy, router không còn chỗ lưu trữ tạm thời các gói tin mới tới, dẫn đến việc phải drop (loại bỏ) chúng.*

**Câu 10:** Quá trình một bộ định tuyến (router) nhận một gói tin ĐẦY ĐỦ từ cổng vào, sau đó mới tiến hành đẩy gói tin đó ra cổng đích được gọi là nguyên lý gì?
A. Phân mảnh gói tin
B. Lưu và chuyển tiếp (Store-and-Forward)
C. Định tuyến đa đường (Multipath routing)
D. Chuyển mạch tế bào (Cell switching)
*Đáp án: B*
*Giải thích: Hầu hết các packet switch sử dụng cơ chế lưu-và-chuyển-tiếp, tạo ra một độ trễ bằng L/R tại mỗi chặng.*

**Câu 11:** Trong mô hình TCP/IP, đơn vị dữ liệu (PDU) tại tầng Giao vận (Transport Layer) được gọi là gì?
A. Message (Bản tin)
B. Datagram (Gói tin)
C. Segment (Đoạn tin)
D. Frame (Khung)
*Đáp án: C*
*Giải thích: Đơn vị dữ liệu: Application -> Message, Transport -> Segment, Network -> Datagram, Link -> Frame.*

**Câu 12:** Lớp nào CÓ trong mô hình OSI 7 tầng nhưng KHÔNG được tách biệt rõ ràng trong mô hình TCP/IP 5 tầng?
A. Tầng Ứng dụng (Application)
B. Tầng Giao vận (Transport)
C. Tầng Phiên (Session) và Tầng Trình diễn (Presentation)
D. Tầng Mạng (Network)
*Đáp án: C*
*Giải thích: Trong TCP/IP, chức năng của tầng Session và Presentation được gộp chung vào tầng Application.*

**Câu 13:** Giao thức nào dưới đây KHÔNG hoạt động ở tầng Ứng dụng?
A. HTTP
B. SMTP
C. FTP
D. IP
*Đáp án: D*
*Giải thích: IP (Internet Protocol) là giao thức cốt lõi của tầng Mạng (Network Layer).*

**Câu 14:** Khi bạn tải một file có dung lượng F = 32 Megabits mất 8 giây. Thông lượng trung bình (Average Throughput) của quá trình tải file này là bao nhiêu?
A. 4 Megabytes/s
B. 4 Megabits/s (Mbps)
C. 8 Megabits/s
D. 256 Megabits/s
*Đáp án: B*
*Giải thích: Average Throughput = Kích thước file / Thời gian = 32 Mbits / 8 s = 4 Mbps.*

**Câu 15:** Trên tuyến đường từ Client tới Server có 3 đoạn mạng với tốc độ lần lượt là R1 = 10 Mbps, R2 = 5 Mbps, R3 = 100 Mbps. Thông lượng đầu cuối tới đầu cuối (end-to-end throughput) lớn nhất xấp xỉ bằng bao nhiêu?
A. 115 Mbps
B. 10 Mbps
C. 100 Mbps
D. 5 Mbps
*Đáp án: D*
*Giải thích: Throughput bị giới hạn bởi liên kết có băng thông thấp nhất trên tuyến đường (bottleneck link), ở đây là 5 Mbps.*

**Câu 16:** Hành động thay đổi trái phép địa chỉ IP nguồn trong Header của gói tin để giả mạo là một người dùng hợp pháp được gọi là gì?
A. Packet Sniffing (Nghe lén gói tin)
B. IP Spoofing (Giả mạo IP)
C. DoS (Từ chối dịch vụ)
D. Man in the middle (Người đứng giữa)
*Đáp án: B*
*Giải thích: Spoofing là hành vi mạo danh địa chỉ IP nguồn để đánh lừa hệ thống đích.*

**Câu 17:** Các mạng máy tính ma (Botnet) gồm hàng trăm ngàn máy bị nhiễm malware thường bị hacker huy động để thực hiện cuộc tấn công nào sau đây?
A. SQL Injection
B. Đánh cắp mật khẩu ngân hàng
C. DDoS (Từ chối dịch vụ phân tán)
D. Thay đổi giao diện website (Defacement)
*Đáp án: C*
*Giải thích: Hacker điều khiển botnet cùng lúc gửi hàng triệu gói tin rác về một máy chủ để làm quá tải băng thông và sập dịch vụ (DDoS).*

**Câu 18:** Kỹ thuật ghép kênh theo tần số (FDM) trong chuyển mạch kênh hoạt động như thế nào?
A. Chia thời gian thành các khe, mỗi kết nối dùng 1 khe.
B. Băng thông của liên kết cáp được chia thành nhiều dải tần số nhỏ, mỗi kết nối được sử dụng riêng một dải tần số trong suốt phiên kết nối.
C. Mọi kết nối cùng dùng chung toàn bộ băng thông và phát sinh va chạm.
D. Gửi gói tin ngẫu nhiên lên đường cáp.
*Đáp án: B*
*Giải thích: FDM (Frequency-Division Multiplexing) cắt dọc băng thông thành các làn đường song song, mỗi cuộc gọi chạy trên một làn riêng.*

**Câu 19:** Khi một máy tính đóng gói (encapsulate) một bản tin để gửi đi, thứ tự thêm các lớp Header từ trên xuống dưới (từ ứng dụng ra cáp vật lý) là:
A. Application -> Link -> Network -> Transport -> Physical
B. Application -> Transport -> Network -> Link -> Physical
C. Link -> Network -> Transport -> Application
D. Transport -> Application -> Network -> Link
*Đáp án: B*
*Giải thích: Dữ liệu đi từ tầng cao xuống tầng thấp: Ứng dụng tạo Message, Giao vận thêm header tạo Segment, Mạng thêm header tạo Datagram, Liên kết thêm header/trailer tạo Frame.*

**Câu 20:** Độ trễ xử lý nút (Nodal Processing Delay) tại một router bao gồm những công việc gì?
A. Chờ đợi ở hàng đợi cho đến khi đường cáp rảnh.
B. Thời gian đẩy tín hiệu điện từ lên cáp quang.
C. Kiểm tra lỗi bit (checksum) ở header và quyết định cổng đầu ra cho gói tin.
D. Thời gian tín hiệu ánh sáng truyền trong cáp.
*Đáp án: C*
*Giải thích: Trễ xử lý là thời gian CPU của router đọc header, kiểm tra lỗi và tra bảng định tuyến. Thời gian này thường rất nhỏ (cỡ microsecond).*

**Câu 21:** Giao thức nào ở tầng Liên kết (Data Link Layer) được sử dụng phổ biến nhất trong các mạng LAN có dây?
A. Wi-Fi (IEEE 802.11)
B. 4G LTE
C. Ethernet (IEEE 802.3)
D. PPP
*Đáp án: C*
*Giải thích: Ethernet là chuẩn công nghệ thống trị tuyệt đối trong các mạng LAN nội bộ có dây.*

**Câu 22:** Việc chuẩn hóa các giao thức Internet để đảm bảo mọi thiết bị trên thế giới có thể giao tiếp với nhau được thực hiện bởi tổ chức nào, và tài liệu chuẩn hóa đó gọi là gì?
A. Tổ chức IEEE, gọi là chuẩn 802.
B. Tổ chức IETF, gọi là tài liệu RFC (Request for Comments).
C. Tổ chức ISO, gọi là mô hình OSI.
D. Tổ chức W3C, gọi là HTML.
*Đáp án: B*
*Giải thích: IETF (Internet Engineering Task Force) là nơi thảo luận và phê duyệt các chuẩn Internet dưới dạng tài liệu RFC.*

**Câu 23:** Khái niệm "Rìa mạng" (Network Edge) bao gồm những thiết bị nào?
A. Các bộ định tuyến (Router) đường trục quốc gia.
B. Các cáp quang dưới đáy biển.
C. Các thiết bị đầu cuối (Host) như máy tính cá nhân, điện thoại di động, máy chủ Web.
D. Các trạm phát sóng vệ tinh.
*Đáp án: C*
*Giải thích: Rìa mạng là nơi người dùng và các ứng dụng trực tiếp tương tác, gồm các hệ thống đầu cuối (client và server).*

**Câu 24:** Một phần mềm gián điệp bí mật ghi lại thao tác bàn phím của người dùng để trộm mật khẩu được xếp vào nhóm nào?
A. DoS
B. Packet Sniffer
C. Malware (Mã độc) dạng Spyware.
D. Worm
*Đáp án: C*
*Giải thích: Spyware là một loại mã độc được cài lén lút vào máy nạn nhân để theo dõi hành vi.*

**Câu 25:** Đặc điểm nào sau đây mô tả đúng nhất về mạng Truyền hình cáp (Cable access network) dùng để truy cập Internet?
A. Là môi trường truyền thông chuyên biệt không chia sẻ.
B. Là môi trường truyền thông chia sẻ (Shared medium), nơi tất cả các hộ gia đình dùng chung một đường cáp sẽ cùng chia sẻ tổng băng thông tải xuống.
C. Tốc độ tải lên (Upload) luôn bằng hoặc lớn hơn tải xuống (Download).
D. Không thể truyền đồng thời tín hiệu tivi và tín hiệu Internet.
*Đáp án: B*
*Giải thích: Khác với FTTH nối cáp quang riêng đến tận nhà, cáp đồng trục truyền hình là một bus chung, các nhà trong khu phố cùng chia sẻ băng thông.*

**Câu 26:** Hai chức năng chính của Lõi mạng (Network Core) là gì?
A. Định tuyến (Routing) và Chuyển tiếp (Forwarding).
B. Mã hóa (Encryption) và Giải mã (Decryption).
C. Hiển thị trang web và nén tệp tin.
D. Phát sóng Wi-Fi và quản lý pin thiết bị di động.
*Đáp án: A*
*Giải thích: Routing giúp tìm đường trên toàn cục, Forwarding giúp đẩy gói tin qua thiết bị nội bộ.*

**Câu 27:** Mạng riêng của tổ chức (Intranet) khác Internet ở điểm nào?
A. Dùng các giao thức hoàn toàn khác biệt với TCP/IP.
B. Là mạng khép kín của một cơ quan/doanh nghiệp, bị giới hạn truy cập từ bên ngoài, nhưng vẫn dùng chung kiến trúc và giao thức như Internet.
C. Tốc độ luôn luôn cao hơn Internet.
D. Không cần dùng Router.
*Đáp án: B*
*Giải thích: Intranet bản chất là một mạng IP nội bộ, bị tường lửa cô lập với Internet công cộng để bảo mật.*

**Câu 28:** Đơn vị đo lường cơ bản của băng thông (Bandwidth) mạng máy tính là gì?
A. Byte (B)
B. bit trên giây (bps)
C. Hertz (Hz)
D. Frame trên giây (fps)
*Đáp án: B*
*Giải thích: Tốc độ truyền dẫn trên mạng đo bằng số lượng bit đẩy lên đường cáp trong 1 giây (bps, Kbps, Mbps, Gbps).*

**Câu 29:** Nếu trễ lan truyền (Propagation Delay) quá lớn (ví dụ truyền qua vệ tinh địa tĩnh), nó sẽ ảnh hưởng tiêu cực nhất đến loại ứng dụng nào?
A. Truyền nhận Email
B. Tải tệp tin (File Download)
C. Gọi thoại hoặc Video thời gian thực (VoIP/Video Call)
D. Đọc báo điện tử
*Đáp án: C*
*Giải thích: Độ trễ vài trăm miligiây của vệ tinh khiến giọng nói bị delay, gây gián đoạn và cực kỳ khó chịu khi đàm thoại trực tiếp.*

**Câu 30:** Thiết bị nào sau đây thường được triển khai Tường lửa (Firewall) để bảo vệ mạng cục bộ khỏi Internet?
A. Edge Router (Bộ định tuyến biên)
B. Laptop của khách hàng
C. Cáp đồng trục
D. Trạm phát sóng Wi-Fi (AP)
*Đáp án: A*
*Giải thích: Tường lửa thường được cài đặt ở cửa ngõ giao tiếp giữa LAN và Internet, tức là trên Edge Router.*

**Câu 31:** Để xác định được đường đi ngắn nhất hoặc tốt nhất cho gói tin, các Router thực thi điều gì?
A. Thuật toán kiểm tra lỗi CRC
B. Thuật toán định tuyến (Routing Protocols/Algorithms)
C. Các hàm băm mật mã MD5
D. Giao thức DHCP
*Đáp án: B*
*Giải thích: Routing protocols (như OSPF, BGP) chạy các thuật toán để tìm và cấu hình đường đi cho gói tin.*

**Câu 32:** Yếu tố nào sau đây quyết định kích thước của Cửa sổ tắc nghẽn (Congestion Window) nếu TCP nằm trong Mạng Truy cập Không dây? (Câu hỏi mở rộng khái niệm)
A. Trễ hàng đợi
B. Tín hiệu RTS/CTS
C. Cơ chế chống rớt mạng của ứng dụng
D. Các phản hồi ACK hoặc Timeout (Mất gói)
*Đáp án: D*
*Giải thích: Hiện tượng mất gói, gây ra do tắc nghẽn hoặc do nhiễu không dây, đều sẽ dẫn đến Timeout hoặc thiếu ACK, khiến TCP thu hẹp cửa sổ truyền.*

**Câu 33:** Ứng dụng P2P (Peer-to-Peer) khác ứng dụng Client-Server ở điểm cốt lõi nào?
A. P2P cần một máy chủ cực mạnh để điều phối.
B. P2P cho phép máy tính cá nhân tự cung cấp tài nguyên trực tiếp cho nhau thay vì dựa vào máy chủ trung tâm.
C. P2P chỉ chạy trên cáp quang.
D. P2P không thể truyền tệp lớn.
*Đáp án: B*
*Giải thích: Mọi máy (Peer) trong mạng ngang hàng vừa là Client vừa là Server.*

**Câu 34:** ISP Tier-1 (Nhà cung cấp dịch vụ Internet cấp 1) có đặc điểm gì?
A. Cung cấp mạng trực tiếp cho các hộ gia đình ở nông thôn.
B. Phải trả tiền để kết nối với mạng của người khác.
C. Có mạng lưới đường trục quang phủ sóng toàn cầu và kết nối ngang hàng (peering) với các ISP Tier-1 khác mà không phải trả phí trung chuyển.
D. Chỉ cung cấp dịch vụ mạng di động vô tuyến.
*Đáp án: C*
*Giải thích: Tier-1 là tầng cao nhất của cấu trúc Internet, họ kết nối miễn phí với nhau và thu phí từ các ISP cấp dưới (Tier-2, Access ISP).*

**Câu 35:** Tại sao Packet Switching lại được cho là hiệu quả hơn Circuit Switching trong việc sử dụng băng thông Internet?
A. Vì nó không chia nhỏ gói tin.
B. Do hiện tượng "Statistical Multiplexing" (Ghép kênh thống kê), cho phép nhiều người dùng tận dụng khoảng thời gian rảnh rỗi của đường truyền, thay vì cấp phát cứng tài nguyên như Circuit Switching.
C. Vì Packet Switching đảm bảo gói tin không bao giờ bị trễ.
D. Vì nó dùng được trên mạng điện thoại bàn.
*Đáp án: B*
*Giải thích: Do dữ liệu máy tính thường truyền theo đợt (bursty), khi máy này ngưng truyền thì máy khác lập tức dùng được phần băng thông đó.*

**Câu 36:** Để giảm thiểu độ trễ xử lý (Nodal Processing Delay), các Router lõi hiện đại thường áp dụng biện pháp gì?
A. Cài đặt hệ điều hành Windows Server.
B. Sử dụng hoàn toàn cấu trúc phần mềm (Software) để chạy linh hoạt.
C. Sử dụng các mạch tích hợp phần cứng chuyên dụng (Hardware/ASIC) để tăng tốc độ tra cứu và chuyển mạch.
D. Gộp tầng Mạng và tầng Giao vận lại với nhau.
*Đáp án: C*
*Giải thích: Bảng định tuyến được đẩy vào phần cứng phần cứng chuyên dụng để xử lý gói tin ở tốc độ nanosecond.*

**Câu 37:** Kẻ tấn công dùng phương pháp "Packet Sniffing" có thể làm được điều gì?
A. Giả mạo địa chỉ IP để vượt qua tường lửa.
B. Làm ngập lụt băng thông của mạng.
C. Nghe trộm và sao chép toàn bộ nội dung của các gói tin truyền không mã hóa qua mạng cục bộ (ví dụ mạng Wi-Fi công cộng).
D. Đưa máy tính vào botnet.
*Đáp án: C*
*Giải thích: Sniffer đọc lén dòng dữ liệu chạy qua đường cáp/sóng không trung để dò mật khẩu nếu người dùng không dùng HTTPS.*

**Câu 38:** Sự cố nào dưới đây KHÔNG do nguyên nhân tràn hàng đợi (buffer overflow) gây ra?
A. Gói tin bị vứt bỏ (Packet Loss).
B. Tăng trễ hàng đợi (Queuing Delay).
C. Trễ lan truyền (Propagation Delay) tăng lên đột biến.
D. Ứng dụng phía trên (như TCP) phải truyền lại dữ liệu.
*Đáp án: C*
*Giải thích: Propagation delay phụ thuộc cứng vào khoảng cách cáp và tốc độ ánh sáng, không phụ thuộc vào tình trạng kẹt xe của router.*

**Câu 39:** Đơn vị đo đạc tốc độ lan truyền tín hiệu (v) trong cáp quang hoặc cáp đồng xấp xỉ bằng bao nhiêu?
A. Tốc độ âm thanh (340 m/s)
B. Bằng tốc độ ánh sáng trong chân không (3 * 10^8 m/s)
C. Tốc độ ánh sáng trong môi trường chất rắn (khoảng 2 * 10^8 m/s)
D. 100 Mbps
*Đáp án: C*
*Giải thích: Ánh sáng truyền trong cáp quang hay điện truyền trong đồng chậm hơn một chút so với tốc độ ánh sáng chân không, khoảng 2/3.*

**Câu 40:** Mô hình OSI phân bổ chức năng chuyển định dạng dữ liệu (ví dụ mã hóa văn bản, nén ảnh) vào tầng nào?
A. Application
B. Presentation (Trình diễn)
C. Session
D. Transport
*Đáp án: B*
*Giải thích: Tầng Presentation (Tầng 6 của OSI) có chức năng trình bày dữ liệu cho ứng dụng (mã hóa, nén).*

**Câu 41:** Một liên kết mạng bị "Nút thắt cổ chai" (Bottleneck) khi nào?
A. Khi kích thước gói tin lớn hơn MTU.
B. Khi liên kết đó có băng thông nhỏ nhất trên toàn bộ con đường từ nguồn đến đích, khiến nó giới hạn thông lượng tối đa của toàn mạng.
C. Khi liên kết đó kết nối với một máy chủ hỏng.
D. Khi cáp mạng bị thắt nút vật lý.
*Đáp án: B*
*Giải thích: Giống như ống nước, chỗ nhỏ nhất quyết định lượng nước chảy qua tối đa.*

**Câu 42:** Đâu là đặc trưng của mạng truy cập Không dây diện rộng (Wide-area wireless access networks)?
A. Phạm vi phủ sóng nhỏ, chỉ vài chục mét (Wi-Fi).
B. Được cung cấp bởi công ty điện lực qua đường dây điện.
C. Phủ sóng bán kính rộng hàng chục km nhờ các trạm thu phát của nhà mạng di động viễn thông (ví dụ 3G, 4G, 5G).
D. Phải dùng cáp đồng trục để nối vào điện thoại.
*Đáp án: C*
*Giải thích: 4G/5G là mạng truy cập vô tuyến bao trùm diện rộng ngoài trời.*

**Câu 43:** Kỹ thuật FDM và TDM thường thuộc kiến trúc mạng nào?
A. Chuyển mạch gói mạng máy tính.
B. Chuyển mạch kênh mạng viễn thông.
C. Mạng cảm biến không dây.
D. Chuyển đổi mã hóa.
*Đáp án: B*
*Giải thích: FDM (chia tần số) và TDM (chia khe thời gian) là hai cách để cắt nhỏ tài nguyên vật lý cố định cho các cuộc gọi thoại.*

**Câu 44:** Worm khác Virus máy tính ở điểm nào?
A. Worm làm cháy ổ cứng, Virus chỉ làm chậm máy.
B. Virus cần có sự thao tác/tương tác của người dùng (như mở file đính kèm, chạy ứng dụng) để lây nhiễm. Worm có khả năng lợi dụng lỗ hổng mạng để tự động lây nhiễm sang máy khác mà không cần người dùng can thiệp.
C. Worm chỉ lây trên điện thoại, Virus lây trên máy tính.
D. Không có khác biệt.
*Đáp án: B*
*Giải thích: Sự nguy hiểm của Worm (như WannaCry) là nó tự rà quét mạng và nhân bản tự động vào máy nạn nhân qua các cổng dịch vụ hở.*

**Câu 45:** Khi bạn mở một trang web, một gói HTTP Request sẽ được chuyển dần xuống qua bao nhiêu tầng của giao thức TCP/IP trước khi truyền vào cáp?
A. 4 tầng (Transport, Network, Link, Physical)
B. 3 tầng (Network, Link, Physical)
C. 5 tầng (Application, Session, Transport, Network, Link)
D. Chạy thẳng qua tầng Vật lý.
*Đáp án: A*
*Giải thích: Gói HTTP nằm ở tầng Application, nó sẽ đi xuống 4 tầng còn lại: Giao vận -> Mạng -> Liên kết -> Vật lý.*

**Câu 46:** Các trung tâm dữ liệu (Datacenter) khổng lồ của Google thường xây dựng hệ thống mạng kết nối riêng (Private network) để làm gì?
A. Để thu phí mạng của người dùng.
B. Bỏ qua hoàn toàn các chuẩn TCP/IP để dùng chuẩn riêng nhanh hơn.
C. Tránh phải trả cước phí lưu lượng trung chuyển khổng lồ cho các ISP Tier-1 và tăng cường độ ổn định, kiểm soát khi kết nối toàn cầu.
D. Để hạn chế số người dùng tìm kiếm.
*Đáp án: C*
*Giải thích: Google/Microsoft tự rải cáp quang xuyên biển tạo Content Provider Network riêng, bypass hệ thống Internet công cộng ở nhiều quốc gia để tự quản lý lưu lượng.*

**Câu 47:** Gói tin ở Tầng Mạng (Network Layer) gọi là Datagram. Vậy Datagram bị bóc Header khi nó đi tới thiết bị mạng nào?
A. Link-layer Switch
B. Máy tính nguồn
C. Router (Bộ định tuyến)
D. Hub
*Đáp án: C*
*Giải thích: Router hoạt động đến Tầng 3. Nó lột lớp vỏ Link-layer Frame ra, đọc Header của Datagram Tầng 3, xử lý, rồi đóng vỏ Link-layer mới trước khi truyền đi.*

**Câu 48:** Băng thông (Bandwidth) khác với Thông lượng (Throughput) như thế nào?
A. Không khác biệt gì.
B. Băng thông là dung lượng đo được trên ổ cứng, Thông lượng đo trên cáp.
C. Băng thông là tốc độ truyền dữ liệu LÝ THUYẾT tối đa của đường truyền vật lý, trong khi Thông lượng là lượng dữ liệu THỰC TẾ truyền được ở một thời điểm, có tính đến nhiễu và chia sẻ mạng.
D. Thông lượng chỉ dành cho gói tin bị lỗi.
*Đáp án: C*
*Giải thích: Giống như đường cao tốc có 4 làn xe (Băng thông), nhưng vì kẹt xe nên tốc độ chạy thực tế chỉ đạt 20km/h (Thông lượng).*

**Câu 49:** Theo định nghĩa của IETF, tài liệu đặc tả chi tiết về cách hoạt động của một giao thức Internet như TCP hay HTTP được gọi là gì?
A. Giao diện (Interface)
B. Bằng sáng chế (Patent)
C. RFC (Request for Comments)
D. IEEE Document
*Đáp án: C*
*Giải thích: Các tài liệu chuẩn của tổ chức kỹ thuật Internet IETF được ban hành dưới cái tên truyền thống là RFC.*

**Câu 50:** Sự kết hợp giữa Giao thức (Protocol) và Phân tầng (Layering) mang lại lợi thế lớn nhất nào cho việc phát triển Internet?
A. Tăng tính phức tạp để ngăn hacker tìm hiểu.
B. Cố định hoàn toàn kiến trúc mạng, không bao giờ thay đổi.
C. Tính Module hóa. Các nhà phát triển ứng dụng (trên tầng Application) chỉ cần giao tiếp qua giao diện chuẩn mà không cần quan tâm đến việc ở dưới cáp quang hay sóng Wi-Fi (Physical Layer) truyền tín hiệu như thế nào.
D. Giảm số lượng thiết bị vật lý.
*Đáp án: C*
*Giải thích: Module hóa nhờ layering giúp công nghệ phần mềm và công nghệ vật liệu mạng (cáp quang, wifi) có thể phát triển độc lập mà vẫn tương thích với nhau qua TCP/IP.*

**Câu 51:** Trong kiến trúc mạng, tại sao việc chuyển mạch gói (packet switching) lại được ưa chuộng hơn chuyển mạch kênh (circuit switching) đối với Internet?
A. Chuyển mạch gói luôn cung cấp băng thông được đảm bảo cho mỗi phiên kết nối.
B. Chuyển mạch gói cho phép nhiều người dùng chia sẻ tài nguyên mạng hiệu quả hơn, phù hợp với lưu lượng dữ liệu dạng bùng nổ (bursty).
C. Chuyển mạch gói không bị giới hạn bởi độ trễ hàng đợi (queueing delay).
D. Chuyển mạch gói yêu cầu thiết lập trước một mạch vật lý chuyên dụng.
*Đáp án: B*
*Giải thích: Chuyển mạch gói tận dụng phương pháp ghép kênh thống kê (statistical multiplexing), cho phép băng thông liên kết được sử dụng hiệu quả hơn khi người dùng không truyền dữ liệu liên tục.*

**Câu 52:** Độ trễ truyền dẫn (transmission delay) của một gói tin phụ thuộc vào các yếu tố nào sau đây?
A. Chiều dài đường truyền vật lý và tốc độ lan truyền tín hiệu.
B. Kích thước gói tin và tốc độ truyền (băng thông) của liên kết.
C. Mức độ tắc nghẽn tại router và tốc độ xử lý của router.
D. Số lượng router trên đường đi từ nguồn đến đích.
*Đáp án: B*
*Giải thích: Độ trễ truyền dẫn được tính bằng công thức L/R, trong đó L là chiều dài gói tin (bits) và R là tốc độ truyền của liên kết (bits/sec).*

**Câu 53:** Độ trễ lan truyền (propagation delay) khác với độ trễ truyền dẫn (transmission delay) ở điểm nào?
A. Lan truyền phụ thuộc vào kích thước gói tin, truyền dẫn phụ thuộc vào khoảng cách.
B. Lan truyền phụ thuộc vào khoảng cách vật lý giữa 2 router, truyền dẫn phụ thuộc vào băng thông và kích thước gói.
C. Lan truyền là thời gian router xử lý header, truyền dẫn là thời gian đẩy bit ra đường truyền.
D. Cả hai là một, chỉ là cách gọi khác nhau trong các giáo trình khác nhau.
*Đáp án: B*
*Giải thích: Lan truyền (d/s) đo thời gian tín hiệu đi qua cáp, truyền dẫn (L/R) đo thời gian thiết bị đẩy toàn bộ gói tin ra đường truyền.*

**Câu 54:** Một gói tin có kích thước 1000 bytes được gửi qua một liên kết có tốc độ 10 Mbps. Thời gian truyền dẫn (transmission delay) xấp xỉ là bao nhiêu?
A. 0.1 ms
B. 0.8 ms
C. 1 ms
D. 8 ms
*Đáp án: B*
*Giải thích: Kích thước L = 1000 bytes = 8000 bits. Tốc độ R = 10 Mbps = 10^7 bps. Delay = L/R = 8000 / 10,000,000 = 0.0008 giây = 0.8 ms.*

**Câu 55:** Thành phần nào của độ trễ mạng là nguyên nhân chính dẫn đến hiện tượng mất gói (packet loss)?
A. Processing delay
B. Transmission delay
C. Propagation delay
D. Queueing delay
*Đáp án: D*
*Giải thích: Khi hàng đợi (buffer) tại router bị đầy do lưu lượng đến quá nhanh, các gói tin đến sau sẽ bị loại bỏ (drop/loss).*

**Câu 56:** Thông lượng đầu cuối (end-to-end throughput) trong một đường truyền gồm nhiều chặng (multi-hop) thường được quyết định bởi yếu tố nào?
A. Liên kết có tốc độ cao nhất (Highest-capacity link).
B. Liên kết có tốc độ thấp nhất (Bottleneck link).
C. Trung bình cộng tốc độ của tất cả các liên kết.
D. Tốc độ xử lý của router cuối cùng.
*Đáp án: B*
*Giải thích: Liên kết nút cổ chai (bottleneck link) quyết định thông lượng tổng thể vì dữ liệu không thể đi nhanh hơn tốc độ của đoạn chậm nhất trên toàn tuyến.*

**Câu 57:** Trong mô hình OSI, tầng nào chịu trách nhiệm chia dữ liệu thành các frame và phát hiện lỗi ở cấp độ node-to-node (như qua cáp mạng)?
A. Physical Layer
B. Data Link Layer
C. Network Layer
D. Transport Layer
*Đáp án: B*
*Giải thích: Tầng Liên kết dữ liệu (Data Link) đóng gói dữ liệu thành frames, kiểm soát truy cập môi trường và thực hiện kiểm tra lỗi giữa các thiết bị kề nhau.*

**Câu 58:** Đâu là sự khác biệt chính giữa tầng Giao vận (Transport) và tầng Mạng (Network)?
A. Tầng Giao vận cung cấp giao tiếp host-to-host; Tầng Mạng cung cấp giao tiếp process-to-process.
B. Tầng Giao vận cung cấp giao tiếp process-to-process; Tầng Mạng cung cấp giao tiếp host-to-host.
C. Tầng Giao vận xử lý định tuyến (routing); Tầng Mạng xử lý đảm bảo tin cậy (reliability).
D. Không có sự khác biệt, hai tầng này thực hiện cùng một chức năng.
*Đáp án: B*
*Giải thích: Tầng mạng chuyển gói tin từ máy này sang máy khác (Dựa vào IP). Tầng giao vận phân phối dữ liệu từ máy tính đến đúng ứng dụng/tiến trình (dựa vào Port).*

**Câu 59:** Botnet là thuật ngữ dùng để chỉ:
A. Một mạng lưới các máy chủ cung cấp dịch vụ web tốc độ cao.
B. Mạng lưới các thiết bị bị lây nhiễm mã độc và bị hacker điều khiển từ xa để thực hiện các cuộc tấn công.
C. Một tập hợp các chương trình diệt virus chạy trên máy tính người dùng.
D. Giao thức tự động cấp phát địa chỉ IP cho các thiết bị di động.
*Đáp án: B*
*Giải thích: Botnet thường được sử dụng để phát động tấn công từ chối dịch vụ phân tán (DDoS) hoặc gửi thư rác quy mô lớn.*

**Câu 60:** Malware nào sau đây có khả năng tự sao chép và tự lây lan qua mạng sang các hệ thống khác mà không cần người dùng thao tác trực tiếp (như click vào file đính kèm)?
A. Virus
B. Trojan horse
C. Worm
D. Spyware
*Đáp án: C*
*Giải thích: Sâu máy tính (Worm) có khả năng tự lây lan bằng cách khai thác lỗ hổng mạng, không như Virus cần sự can thiệp của người dùng (chạy file) để kích hoạt.*

**Câu 61:** Packet sniffer là gì?
A. Một thiết bị phần cứng giúp tăng tốc độ mạng.
B. Một phần mềm hoặc phần cứng đọc thụ động mọi gói tin truyền qua một môi trường mạng chia sẻ (như WiFi).
C. Một giao thức bảo mật dùng để mã hóa gói tin.
D. Một loại virus phá hủy cấu trúc gói tin IPv4.
*Đáp án: B*
*Giải thích: Packet sniffer "ngửi" và sao chép các gói tin đi qua interface mạng, thường được dùng để phân tích mạng hoặc đánh cắp mật khẩu (nếu không mã hóa).*

**Câu 62:** "IP spoofing" là kỹ thuật tấn công nào sau đây?
A. Thay đổi địa chỉ MAC của card mạng.
B. Sinh ra hàng triệu gói tin để làm quá tải server.
C. Giả mạo địa chỉ IP nguồn trong gói tin để đóng giả làm một host tin cậy.
D. Nghe lén dữ liệu trên đường truyền không dây.
*Đáp án: C*
*Giải thích: IP spoofing liên quan đến việc tạo ra các gói tin có địa chỉ IP nguồn giả mạo để che giấu danh tính hoặc lừa hệ thống bảo vệ.*

**Câu 63:** Chức năng encapsulation (đóng gói) hoạt động như thế nào khi một bản tin đi từ tầng Application xuống tầng Physical?
A. Mỗi tầng bóc đi header của tầng trên và gửi dữ liệu thô xuống tầng dưới.
B. Mỗi tầng thêm header riêng của mình vào thông điệp nhận được từ tầng trên.
C. Dữ liệu được nén lại nhỏ hơn qua mỗi tầng.
D. Dữ liệu được chia nhỏ thành các byte tĩnh và chèn vào một khung cố định.
*Đáp án: B*
*Giải thích: Đóng gói (encapsulation) là quá trình các tầng thêm thông tin điều khiển (header/trailer) của riêng nó vào payload trước khi chuyển xuống tầng thấp hơn.*

**Câu 64:** Trong mô hình TCP/IP, đơn vị dữ liệu (PDU) tại tầng Transport được gọi là gì?
A. Frame
B. Datagram
C. Segment
D. Message
*Đáp án: C*
*Giải thích: Tại tầng Application là Message, tầng Transport là Segment, tầng Network là Datagram (hoặc Packet), tầng Link là Frame.*

**Câu 65:** Tier-1 ISPs (Nhà cung cấp dịch vụ Internet cấp 1) có đặc điểm nào sau đây?
A. Trả phí cho các ISP cấp 2 để được định tuyến lưu lượng.
B. Kết nối trực tiếp với tất cả các thiết bị đầu cuối của người dùng.
C. Nằm ở trung tâm mạng Internet toàn cầu và kết nối ngang hàng (peer) trực tiếp với các Tier-1 ISP khác mà không phải trả phí trung chuyển (transit fee).
D. Chỉ cung cấp dịch vụ mạng cục bộ trong một quốc gia.
*Đáp án: C*
*Giải thích: Tier-1 ISPs là cấp cao nhất, họ tạo thành "xương sống" của Internet và peer với nhau theo thỏa thuận settlement-free.*

**Câu 66:** Quá trình chuyển địa chỉ dạng tên miền (ví dụ: www.google.com) thành địa chỉ IP do hệ thống nào đảm nhiệm?
A. DHCP
B. ARP
C. DNS
D. NAT
*Đáp án: C*
*Giải thích: Domain Name System (DNS) đóng vai trò như một danh bạ điện thoại của Internet, phân giải tên miền con người dễ đọc thành địa chỉ IP để máy tính giao tiếp.*

**Câu 67:** Chuyển mạch gói (packet switching) áp dụng nguyên lý nào để truyền dữ liệu?
A. Cấp phát tĩnh băng thông cho mỗi kết nối.
B. Dữ liệu được gửi đi một cách liên tục không chia nhỏ.
C. Lưu và chuyển tiếp (Store-and-forward transmission).
D. Thiết lập đường dẫn vật lý cố định từ nguồn đến đích trước khi truyền.
*Đáp án: C*
*Giải thích: Switch/Router phải nhận toàn bộ gói tin (store) trước khi có thể bắt đầu chuyển tiếp (forward) nó ra đường liên kết tiếp theo.*

**Câu 68:** Đặc điểm nào KHÔNG phải của đường truyền vệ tinh địa tĩnh (Geostationary satellite)?
A. Được đặt ở độ cao khoảng 36.000 km so với bề mặt Trái Đất.
B. Tốc độ lan truyền tín hiệu tức thời, độ trễ bằng không.
C. Độ trễ lan truyền (propagation delay) xấp xỉ 280 mili-giây.
D. Phù hợp để phủ sóng các khu vực hẻo lánh không có cáp quang.
*Đáp án: B*
*Giải thích: Do khoảng cách lớn (lên và xuống), tín hiệu vô tuyến (truyền với tốc độ ánh sáng) mất khoảng 240-300 ms để truyền, tạo ra độ trễ lan truyền đáng kể.*

**Câu 69:** Hệ thống mạng nào sau đây có thể sử dụng giao thức CSMA/CD để giải quyết đụng độ?
A. Mạng Wi-Fi (802.11)
B. Mạng di động 4G/LTE
C. Mạng Ethernet truyền thống (Ethernet LAN sử dụng cáp đồng trục hoặc hub)
D. Mạng quang thụ động (PON)
*Đáp án: C*
*Giải thích: CSMA/CD (Carrier Sense Multiple Access with Collision Detection) được thiết kế cho mạng Ethernet có dây (môi trường chia sẻ).*

**Câu 70:** Tầng nào trong mô hình OSI tương đương với tầng Internet trong mô hình TCP/IP?
A. Tầng Application (Ứng dụng)
B. Tầng Transport (Giao vận)
C. Tầng Network (Mạng)
D. Tầng Data Link (Liên kết dữ liệu)
*Đáp án: C*
*Giải thích: Tầng Internet trong TCP/IP giải quyết các vấn đề về địa chỉ IP và định tuyến, tương đương chức năng của tầng Network trong OSI.*

**Câu 71:** Tấn công DDoS (Distributed Denial of Service) khác với DoS (Denial of Service) ở điểm nào?
A. DDoS nhắm vào tầng Vật lý, DoS nhắm vào tầng Ứng dụng.
B. DDoS phá hủy dữ liệu của máy chủ, DoS chỉ làm gián đoạn dịch vụ.
C. DDoS sử dụng một lượng lớn các nguồn tấn công phân tán (như botnet), DoS thường xuất phát từ một máy tính duy nhất.
D. DDoS thực hiện qua mạng Wi-Fi, DoS thực hiện qua mạng có dây.
*Đáp án: C*
*Giải thích: "Distributed" trong DDoS có nghĩa là phân tán. Kẻ tấn công huy động hàng ngàn thiết bị bị xâm nhập (zombies/botnet) đồng loạt gửi yêu cầu đến mục tiêu.*

**Câu 72:** Ứng dụng nào sau đây thường yêu cầu băng thông được bảo đảm (guaranteed throughput) nhưng có thể chịu được việc mất một số gói tin?
A. Truyền tệp (File Transfer Protocol - FTP)
B. Duyệt web (HTTP)
C. Gọi điện thoại video (Video/Audio streaming)
D. Email (SMTP)
*Đáp án: C*
*Giải thích: Các ứng dụng thời gian thực như gọi video có thể bỏ qua vài frame hình ảnh/âm thanh mà không ảnh hưởng lớn, nhưng cần băng thông ổn định để tránh bị giật (jitter).*

**Câu 73:** Trong mạng cáp đồng trục truyền hình (Cable network), đặc điểm nào mô tả việc chia sẻ băng thông của công nghệ HFC (Hybrid Fiber Coax)?
A. Mỗi hộ gia đình có một cáp quang riêng kết nối thẳng đến ISP.
B. Các hộ gia đình trong một khu phố chia sẻ một mạng cáp đồng trục chung nối tới router trung tâm (CMTS).
C. Không có sự chia sẻ, băng thông được cấp phát cố định 100 Mbps cho mọi người dùng.
D. Chỉ chia sẻ băng thông cho chiều tải lên (upload), chiều tải xuống (download) là riêng biệt.
*Đáp án: B*
*Giải thích: HFC là một môi trường chia sẻ (shared broadcast medium), do đó tốc độ truy cập có thể giảm khi có nhiều người cùng sử dụng đồng thời.*

**Câu 74:** Loại cáp xoắn đôi (Twisted Pair - TP) được xoắn lại với nhau nhằm mục đích gì?
A. Để tăng độ bền cơ học, tránh bị đứt khi kéo cáp.
B. Để dễ dàng mã hóa tín hiệu ánh sáng.
C. Để giảm nhiễu điện từ (crosstalk) từ các cặp dây liền kề và môi trường bên ngoài.
D. Để tăng tốc độ lan truyền của dòng điện.
*Đáp án: C*
*Giải thích: Các dây cáp được xoắn với số vòng xoắn nhất định/mét giúp triệt tiêu từ trường sinh ra bởi dòng điện chạy trong dây, từ đó giảm nhiễu chéo.*

**Câu 75:** Trong môi trường mạng Wi-Fi (802.11), người ta sử dụng giao thức nào để kiểm soát truy cập môi trường vô tuyến?
A. CSMA/CD
B. CSMA/CA
C. Token Passing
D. ALOHA
*Đáp án: B*
*Giải thích: Wi-Fi sử dụng CSMA/CA (Collision Avoidance - Tránh đụng độ) vì tín hiệu vô tuyến dễ bị suy hao, thiết bị khó có thể vừa phát vừa nghe để phát hiện đụng độ như cáp đồng.*

**Câu 76:** Phát biểu nào sau đây mô tả đúng nhất về "Trễ xử lý tại nút" (Nodal Processing Delay)?
A. Thời gian đẩy tín hiệu lên đường dây cáp quang.
B. Thời gian tín hiệu di chuyển từ router này sang router kia.
C. Thời gian router kiểm tra lỗi bit ở header, xác định đường đi tiếp theo.
D. Thời gian gói tin phải chờ trong bộ đệm khi đường truyền bận.
*Đáp án: C*
*Giải thích: Processing delay thường ở mức micro-giây, bao gồm việc tính toán checksum, phân tích IP đích và tra cứu bảng định tuyến.*

**Câu 77:** Router thực hiện việc định tuyến (routing) bằng cách dựa vào thông tin nào trong gói tin?
A. Địa chỉ MAC nguồn.
B. Địa chỉ IP đích.
C. Cổng Port nguồn.
D. Số Sequence Number.
*Đáp án: B*
*Giải thích: Tại tầng Network, router đọc địa chỉ IP đích trong header của datagram và đối chiếu với Bảng định tuyến (Forwarding Table) để chọn giao diện đầu ra phù hợp.*

**Câu 78:** Mạng chuyển mạch kênh (Circuit Switching) thường sử dụng hai phương pháp để chia sẻ đường truyền là gì?
A. FDM (Frequency Division Multiplexing) và TDM (Time Division Multiplexing).
B. TCP và UDP.
C. CSMA và ALOHA.
D. IPv4 và IPv6.
*Đáp án: A*
*Giải thích: Trong chuyển mạch kênh, tài nguyên truyền dẫn được chia theo phổ tần số (FDM - mỗi kết nối một dải tần) hoặc theo thời gian (TDM - mỗi kết nối một khe thời gian).*

**Câu 79:** Nếu băng thông của một liên kết là R bps, và có N phiên kết nối chia sẻ đường truyền bằng TDM (Time Division Multiplexing), mỗi phiên sẽ nhận được tốc độ tối đa là bao nhiêu trong khe thời gian của nó?
A. R bps
B. R/N bps
C. N*R bps
D. Không thể xác định được.
*Đáp án: A*
*Giải thích: Trong TDM, trong đúng khe thời gian (time slot) được cấp phát, thiết bị đó được sử dụng TOÀN BỘ băng thông R của liên kết. Tuy nhiên, tốc độ trung bình theo thời gian sẽ là R/N.*

**Câu 80:** "Traceroute" là một công cụ mạng được sử dụng để làm gì?
A. Xóa bộ nhớ cache của DNS.
B. Liệt kê tất cả các thiết bị đang kết nối vào mạng Wi-Fi nội bộ.
C. Xác định và đo lường thời gian trễ đến từng router trên đường đi từ nguồn đến đích.
D. Mã hóa tất cả các truy vấn web ra bên ngoài mạng.
*Đáp án: C*
*Giải thích: Traceroute sử dụng cơ chế TTL (Time to Live) của gói tin IP để khám phá từng "trạm trung chuyển" (router) và tính toán RTT (Round Trip Time) đến từng nút.*

**Câu 81:** Liên kết điểm-điểm (Point-to-point link) khác với liên kết quảng bá (Broadcast link) ở chỗ:
A. Liên kết điểm-điểm có nhiều máy tính kết nối vào một kênh truyền chung.
B. Liên kết điểm-điểm chỉ có duy nhất một nút gửi và một nút nhận ở hai đầu.
C. Liên kết điểm-điểm luôn dùng cáp quang, broadcast luôn dùng sóng vô tuyến.
D. Cáp đồng trục luôn là liên kết điểm-điểm.
*Đáp án: B*
*Giải thích: Point-to-point (như cáp nối trực tiếp 2 router) chỉ có 2 thực thể giao tiếp. Broadcast (như Wi-Fi, Ethernet Hub) có nhiều thiết bị cùng lắng nghe trên môi trường truyền.*

**Câu 82:** Lợi ích chính của việc sử dụng "Kiến trúc phân tầng" (Layered Architecture) trong thiết kế mạng là gì?
A. Làm tăng tốc độ truyền dữ liệu tổng thể.
B. Giảm bớt số lượng thiết bị phần cứng cần thiết.
C. Giảm độ phức tạp, cho phép thay đổi cấu trúc/công nghệ của một tầng mà không ảnh hưởng đến các tầng khác.
D. Loại bỏ hoàn toàn khả năng bị tấn công DDoS.
*Đáp án: C*
*Giải thích: Phân tầng cung cấp tính module hóa. Chẳng hạn, khi chuyển từ IPv4 sang IPv6 ở tầng mạng, các ứng dụng (HTTP, FTP) ở tầng trên không cần phải viết lại.*

**Câu 83:** Trong hệ thống thông tin liên lạc, một "RFC" (Request for Comments) là gì?
A. Một thuật toán dùng để mã hóa mật khẩu.
B. Một tài liệu tiêu chuẩn chính thức của IETF mô tả các giao thức mạng Internet.
C. Một lệnh trên Command Prompt để kiểm tra kết nối mạng.
D. Tên gọi khác của tổ chức quản lý tên miền quốc tế (ICANN).
*Đáp án: B*
*Giải thích: RFC là các tài liệu tiêu chuẩn kỹ thuật (ví dụ RFC 2616 định nghĩa HTTP/1.1, RFC 793 định nghĩa TCP) do nhóm đặc trách kỹ thuật Internet (IETF) ban hành.*

**Câu 84:** Băng thông rộng (Broadband) tại nhà (như FTTH) có đặc tính nào phổ biến liên quan đến tốc độ tải lên và tải xuống?
A. Bất đối xứng (Asymmetric) - Tốc độ tải xuống thường cao hơn tốc độ tải lên.
B. Đối xứng (Symmetric) - Tốc độ tải lên và tải xuống luôn bằng nhau.
C. Tải lên luôn cao gấp đôi tải xuống để hỗ trợ sao lưu đám mây.
D. Băng thông thay đổi liên tục theo tần số vô tuyến.
*Đáp án: A*
*Giải thích: Người dùng cá nhân thường tiêu thụ dữ liệu (xem video, lướt web) nhiều hơn là tạo ra dữ liệu, do đó các ISP cấu hình đường truyền có tốc độ download > upload (như ADSL, nhiều gói GPON).*

**Câu 85:** Mạng Intranet là gì?
A. Một phần của Internet bị ẩn đi và chỉ có thể truy cập bằng trình duyệt Tor.
B. Mạng máy tính nội bộ của một tổ chức sử dụng các giao thức Internet (TCP/IP) nhưng bị cô lập khỏi Internet công cộng.
C. Một mạng diện rộng kết nối nhiều quốc gia thông qua cáp quang biển.
D. Một hình thức mạng chỉ sử dụng các thiết bị không dây.
*Đáp án: B*
*Giải thích: Intranet (mạng nội bộ) dùng công nghệ web/IP nhưng giới hạn truy cập cho nhân viên của một công ty, thường được bảo vệ bởi Firewall.*

**Câu 86:** Mạng Extranet có điểm gì khác với Intranet?
A. Extranet chỉ sử dụng cáp đồng trục.
B. Extranet là mạng Intranet nhưng được mở rộng một phần quyền truy cập cho một số đối tác, nhà cung cấp bên ngoài.
C. Extranet là tên gọi khác của Internet toàn cầu.
D. Extranet không sử dụng giao thức IP mà dùng giao thức độc quyền.
*Đáp án: B*
*Giải thích: Extranet cấp quyền truy cập bảo mật một phần mạng nội bộ cho các đối tác kinh doanh hoặc khách hàng được chọn lọc.*

**Câu 87:** Một Server Farm (Trang trại máy chủ) trong các Data Center hiện đại thường được tổ chức thành kiến trúc nào?
A. Một máy tính mainframe khổng lồ duy nhất.
B. Hàng ngàn máy chủ nhỏ liên kết với nhau bằng các mạng tốc độ cực cao, hoạt động song song để xử lý yêu cầu.
C. Một chuỗi các router không có thiết bị đầu cuối.
D. Mạng lưới các thiết bị di động kết nối qua 5G.
*Đáp án: B*
*Giải thích: Các hệ thống như Google, Amazon sử dụng mô hình điện toán đám mây (cloud computing) dựa trên các cluster/server farm gồm rất nhiều máy chủ commodity hardware.*

**Câu 88:** Trong các phương tiện truyền dẫn, tín hiệu truyền trong sợi cáp quang (Optical Fiber) dễ bị ảnh hưởng bởi nhiễu điện từ (EMI) như thế nào?
A. Rất dễ bị ảnh hưởng, giống như cáp đồng.
B. Ít bị ảnh hưởng hơn cáp xoắn đôi nhưng nhiều hơn cáp đồng trục.
C. Hoàn toàn miễn nhiễm với nhiễu điện từ.
D. Phụ thuộc vào tốc độ truyền dẫn.
*Đáp án: C*
*Giải thích: Cáp quang sử dụng xung ánh sáng truyền trong sợi thủy tinh, nên từ trường/điện trường bên ngoài không thể tác động gây nhiễu.*

**Câu 89:** Một byte chứa bao nhiêu bit?
A. 4
B. 8
C. 16
D. 32
*Đáp án: B*
*Giải thích: Kiến thức cơ sở: 1 byte = 8 bits.*

**Câu 90:** Lưu lượng (Traffic intensity) tại một nút mạng được xác định bởi tỷ số La/R, trong đó L là kích thước gói, a là tốc độ gói đến trung bình, R là băng thông liên kết. Nếu La/R > 1, điều gì sẽ xảy ra?
A. Hàng đợi sẽ rỗng, mạng hoạt động hoàn hảo.
B. Hàng đợi sẽ tăng dần đến vô hạn, dẫn đến độ trễ vô hạn và mất gói.
C. Tốc độ truyền của gói tin sẽ tự động tăng lên để đáp ứng.
D. Router sẽ nén gói tin lại để giảm L.
*Đáp án: B*
*Giải thích: La (bit/s) là tốc độ bit trung bình đến hàng đợi. R (bit/s) là tốc độ đẩy bit đi. Nếu tốc độ đến lớn hơn tốc độ đẩy đi (La/R > 1), hàng đợi sẽ tràn.*

**Câu 91:** Hệ thống định vị toàn cầu (GPS) và truyền hình vệ tinh (DTH) thường sử dụng loại liên kết nào?
A. Point-to-Point trên cáp quang
B. Broadcast (Quảng bá) vô tuyến vệ tinh
C. Chuyển mạch ảo (Virtual Circuit)
D. Mạng LAN vòng (Token Ring)
*Đáp án: B*
*Giải thích: Vệ tinh phát tín hiệu xuống Trái Đất và bất kỳ chảo thu nào nằm trong vùng phủ sóng đều có thể nhận tín hiệu (Broadcast).*

**Câu 92:** Tại sao các router trong lõi mạng Internet (Network Core) không triển khai các cơ chế đảm bảo truyền tin cậy (Reliable Data Transfer) và kiểm soát luồng?
A. Vì router không có đủ RAM.
B. Để đơn giản hóa và tối đa hóa tốc độ xử lý gói tin; các chức năng phức tạp được đẩy về các hệ thống đầu cuối (tầng Transport).
C. Vì lỗi trên cáp quang ngày nay là hoàn toàn bằng 0.
D. Vì giao thức IP nghiêm cấm việc kiểm tra lỗi.
*Đáp án: B*
*Giải thích: Đây là nguyên lý End-to-End. Mạng lõi chỉ tập trung làm nhiệm vụ duy nhất là "vận chuyển nhanh nhất có thể" (best-effort), việc đảm bảo tính toàn vẹn và tin cậy do TCP ở host 2 đầu lo.*

**Câu 93:** "Cước phí phẳng" (Flat-rate pricing) trong dịch vụ Internet băng rộng hộ gia đình có nghĩa là:
A. Người dùng trả tiền theo từng MB dung lượng sử dụng.
B. Người dùng trả tiền theo thời gian kết nối thực tế tính bằng phút.
C. Người dùng trả một khoản phí cố định hàng tháng không phụ thuộc vào lưu lượng tải về.
D. Người dùng chỉ trả tiền khi tốc độ vượt quá mức cam kết.
*Đáp án: C*
*Giải thích: Đa số các gói Internet cáp quang hộ gia đình (FTTH) hiện nay thu phí cố định hàng tháng (flat-rate).*

**Câu 94:** Kẻ tấn công có thể giả mạo gói tin từ một IP nội bộ đáng tin cậy để truy cập trái phép. Biện pháp phổ biến nhất mà các Router ở biên giới mạng (Border Router) sử dụng để chống lại kỹ thuật IP Spoofing này là gì?
A. Mã hóa tất cả các gói tin bằng mật khẩu.
B. Cài đặt các bộ lọc gói tin (Ingress Filtering) để loại bỏ các gói tin đi từ bên ngoài vào nhưng mang địa chỉ nguồn nội bộ.
C. Tăng băng thông của router để xử lý khối lượng lớn gói tin.
D. Vô hiệu hóa giao thức IP và chuyển sang dùng địa chỉ MAC.
*Đáp án: B*
*Giải thích: Router biên có thể được cấu hình kiểm tra: nếu một gói tin đi từ cổng kết nối với Internet vào mà mang IP Source thuộc dải LAN bên trong, đó chắc chắn là giả mạo.*

**Câu 95:** Trong kiến trúc mạng, "Mặt phẳng điều khiển" (Control Plane) của bộ định tuyến có trách nhiệm gì?
A. Trực tiếp chuyển tiếp từng gói tin từ cổng vào ra cổng ra (Forwarding).
B. Tính toán và duy trì bảng định tuyến thông qua các thuật toán (như OSPF, BGP) để thiết lập đường đi.
C. Giải mã video streaming.
D. Mã hóa nội dung email người dùng.
*Đáp án: B*
*Giải thích: Control Plane lo "Logic não bộ" (tính toán đường đi), Data/Forwarding Plane lo "Cơ bắp" (đẩy gói tin đi theo bản đồ đã tính).*

**Câu 96:** Công nghệ SDN (Software-Defined Networking) tách rời 2 thành phần nào của hệ thống định tuyến truyền thống?
A. Tầng Application và tầng Transport.
B. Mặt phẳng điều khiển (Control plane) và mặt phẳng dữ liệu (Data/Forwarding plane).
C. Mạng LAN và mạng WAN.
D. Địa chỉ MAC và địa chỉ IP.
*Đáp án: B*
*Giải thích: SDN đưa phần điều khiển (Control Plane) tập trung vào một Server/Controller, trong khi các Router/Switch chỉ còn làm nhiệm vụ Data Plane (chuyển tiếp đơn thuần).*

**Câu 97:** Hiện tượng "đầu ruồi" (Head-of-Line blocking - HOL) trong router hoặc switch mạng xảy ra khi nào?
A. Khi gói tin ở đầu hàng đợi bị chặn và không thể chuyển tiếp do cổng đầu ra bận, khiến các gói tin phía sau trong cùng hàng đợi cũng phải chờ, dù đích đến của chúng đang rảnh.
B. Khi gói tin bị lỗi checksum ở phần Header.
C. Khi độ dài của gói tin vượt quá chỉ số MTU của cáp mạng.
D. Khi tín hiệu cáp quang bị chặn lại do bụi bẩn trên đầu nối.
*Đáp án: A*
*Giải thích: HOL Blocking thường gặp ở kiến trúc Input-queued switch, khi gói tin xếp hàng đầu tiên bị vướng sẽ cản trở toàn bộ hàng phía sau giống như bị kẹt xe đèn đỏ.*

**Câu 98:** Thuật ngữ "Store-and-forward" (Lưu và chuyển tiếp) trong mạng chuyển mạch gói ngụ ý điều gì khi một bộ định tuyến nhận một gói tin có L bit?
A. Router nhận bit đầu tiên và lập tức đẩy nó ra cổng đích.
B. Router nhận toàn bộ L bit của gói tin vào bộ đệm, sau đó mới tiến hành chuyển tiếp gói tin đó.
C. Router lưu một bản sao của gói tin vào ổ cứng vĩnh viễn trước khi chuyển.
D. Router chỉ lưu giữ phần Header, còn dữ liệu sẽ bị loại bỏ.
*Đáp án: B*
*Giải thích: Store-and-forward yêu cầu toàn bộ gói tin phải được nhận đủ (để kiểm tra tính toàn vẹn) trước khi bit đầu tiên được truyền đi ra đường liên kết tiếp.*

**Câu 99:** Điều nào sau đây là ưu điểm của mạng riêng ảo (VPN - Virtual Private Network)?
A. Nó tăng băng thông cáp quang của ISP gấp đôi.
B. Nó cung cấp các kết nối an toàn, mã hóa dữ liệu truyền qua cơ sở hạ tầng Internet công cộng.
C. Nó thay thế hoàn toàn giao thức TCP bằng UDP để tăng tốc độ.
D. Nó cho phép kết nối máy tính mà không cần bất kỳ địa chỉ IP nào.
*Đáp án: B*
*Giải thích: VPN tạo một đường hầm mã hóa (tunnel) trên mạng Internet công cộng để các chi nhánh công ty hoặc người làm từ xa có thể kết nối an toàn vào mạng Intranet.*

**Câu 100:** Các giao thức như HTTP, SMTP, FTP, DNS hoạt động ở tầng nào của mô hình TCP/IP?
A. Network Layer (Tầng Mạng)
B. Transport Layer (Tầng Giao vận)
C. Application Layer (Tầng Ứng dụng)
D. Physical Layer (Tầng Vật lý)
*Đáp án: C*
*Giải thích: Đây đều là các giao thức cấp độ ứng dụng mạng tương tác trực tiếp với phần mềm của người dùng (trình duyệt, email client).*

**Câu 101:** Một trong những lợi thế lớn của kiến trúc mạng client-server so với kiến trúc P2P (Peer-to-Peer) là gì?
A. Dễ dàng quản lý, bảo mật tập trung và kiểm soát dữ liệu tốt hơn.
B. Có khả năng tự mở rộng (self-scalability) tốt hơn khi số lượng người dùng tăng đột biến.
C. Không yêu cầu bất kỳ phần cứng máy chủ chuyên dụng nào.
D. Có thể hoạt động mà không cần kết nối Internet.
*Đáp án: A*
*Giải thích: Client-server tập trung hóa quản trị tại máy chủ, dễ backup và bảo mật. Tuy nhiên nó dễ bị điểm mù (single point of failure) và khó mở rộng quy mô lớn (scale) như P2P.*

**Câu 102:** BitTorrent là một ví dụ điển hình của loại kiến trúc ứng dụng mạng nào?
A. Client-Server
B. Peer-to-Peer (P2P)
C. Master-Slave
D. Cloud Computing
*Đáp án: B*
*Giải thích: Trong BitTorrent, các máy khách (peers) tự chia sẻ trực tiếp các phần nhỏ của tệp tin cho nhau mà không cần đi qua máy chủ trung tâm tải file.*

**Câu 103:** Thuật ngữ "Socket" trong lập trình mạng có thể được ví như:
A. Mã PIN của thẻ ATM.
B. Cánh cửa giữa một ứng dụng (tiến trình) và giao thức tầng giao vận (Transport protocol).
C. Địa chỉ vật lý của card mạng.
D. Cáp kết nối giữa màn hình và CPU.
*Đáp án: B*
*Giải thích: Ứng dụng gửi và nhận thông điệp qua "socket". API của Socket quy định cách một ứng dụng giao tiếp với hệ điều hành và mạng.*

**Câu 104:** Hai yếu tố nào được sử dụng để xác định duy nhất một tiến trình (process) đang chạy trên một thiết bị đích trên Internet?
A. Tên miền (Domain Name) và Địa chỉ MAC.
B. Địa chỉ IP và Số cổng (Port Number).
C. Địa chỉ IPv4 và Địa chỉ IPv6.
D. Giao thức HTTP và HTTPS.
*Đáp án: B*
*Giải thích: IP dùng để định tuyến gói tin đến đúng máy tính. Số cổng (Port) dùng để phân phối dữ liệu cho đúng tiến trình ứng dụng trên máy đó (vd: port 80 cho Web server).*

**Câu 105:** Giao thức tầng giao vận nào cung cấp dịch vụ truyền dữ liệu tin cậy (reliable data transfer)?
A. UDP
B. TCP
C. IP
D. ICMP
*Đáp án: B*
*Giải thích: TCP cung cấp truyền dẫn tin cậy (kiểm tra lỗi, truyền lại gói mất, thứ tự đúng) và kiểm soát luồng/tắc nghẽn. UDP không cung cấp các dịch vụ này (best-effort).*

**Câu 106:** Tại sao các ứng dụng Streaming video hoặc Game Online thường sử dụng UDP thay vì TCP?
A. Vì UDP có tính bảo mật cao hơn, mã hóa dữ liệu mặc định.
B. Vì TCP chậm hơn do các cơ chế bắt tay (handshake), xác nhận (ACK) và truyền lại khi mất gói.
C. Vì UDP là giao thức duy nhất hỗ trợ truyền video.
D. Vì các router Internet ưu tiên đường đi ngắn nhất cho UDP.
*Đáp án: B*
*Giải thích: Các ứng dụng thời gian thực ưu tiên "độ trễ thấp", thà mất một ít khung hình (video giật nhẹ) còn hơn là video bị đứng khựng lại để chờ TCP truyền lại gói tin bị mất.*

**Câu 107:** Việc gán tài nguyên (như băng thông) cho người dùng trong mạng chuyển mạch gói (Packet Switching) dựa trên cơ chế nào?
A. Cấp phát tĩnh định kỳ (Static Allocation)
B. Theo yêu cầu (On-demand) - Cạnh tranh giành tài nguyên
C. Dựa trên số lượng cổng kết nối (Port-based)
D. Chạy theo thời gian thực phân bổ bởi máy chủ DNS
*Đáp án: B*
*Giải thích: Trong chuyển mạch gói, người dùng không được đảm bảo hoặc cấp trước băng thông cố định. Dữ liệu được truyền khi có, và các gói tin cạnh tranh (cùng xếp hàng) để qua router.*

**Câu 108:** Khái niệm "Access Network" (Mạng truy cập) thường ám chỉ đoạn mạng nào?
A. Các siêu máy tính xử lý lượng dữ liệu khổng lồ của Google.
B. Kết nối giữa các nhà mạng viễn thông quốc tế.
C. Đoạn mạng kết nối hệ thống đầu cuối của người dùng đến router biên đầu tiên (edge router) của ISP.
D. Mạng nội bộ kết nối các router bên trong Data Center.
*Đáp án: C*
*Giải thích: Access Network là các công nghệ như Wi-Fi tại nhà, mạng di động 4G/5G, cáp quang FTTH - "Chặng đường cuối" (last mile) nối người dùng vào Internet.*

**Câu 109:** Trong bối cảnh mạng không dây, hiện tượng "Multipath propagation" (Đa đường truyền) là gì?
A. Tín hiệu mạng được gửi đi nhiều lần qua cùng một đường truyền.
B. Tín hiệu vô tuyến dội lại từ các vật thể (tường, tòa nhà) khiến đầu thu nhận được nhiều bản sao của cùng một tín hiệu ở các thời điểm khác nhau.
C. Mạng Wi-Fi và mạng 4G cùng được sử dụng để tải một file.
D. Việc thiết lập nhiều router trên đường đi để tăng tốc độ.
*Đáp án: B*
*Giải thích: Sóng vô tuyến truyền trong không gian sẽ phản xạ, khúc xạ và tán xạ, gây ra hiện tượng đa đường (Multipath), làm mờ hay nhiễu tín hiệu gốc tại đầu thu.*

**Câu 110:** Chức năng "Flow Control" (Kiểm soát luồng) của giao thức mạng nhằm mục đích:
A. Ngăn chặn một trạm phát gửi dữ liệu quá nhanh làm tràn bộ đệm của trạm thu.
B. Điều chỉnh tốc độ truyền để tránh tắc nghẽn ở các bộ định tuyến trong lõi mạng.
C. Chuyển hướng lưu lượng truy cập sang đường liên kết khác khi cáp bị đứt.
D. Phân bổ đều địa chỉ IP cho các máy khách.
*Đáp án: A*
*Giải thích: Flow control (Kiểm soát luồng) là sự đồng bộ hóa tốc độ giữa nút gửi và nút nhận. Congestion control (Kiểm soát tắc nghẽn) là việc điều tiết tốc độ để tránh tắc nghẽn trên toàn mạng lưới router.*

**Câu 111:** Trong các tiêu chuẩn của cáp Ethernet, "1000Base-T" ám chỉ loại cáp và tốc độ nào?
A. Cáp quang, 1000 Mbps.
B. Cáp đồng trục, 1000 Mbps.
C. Cáp xoắn đôi, 1000 Mbps (1 Gbps).
D. Sóng vô tuyến, tần số 1000 MHz.
*Đáp án: C*
*Giải thích: Tiền tố "1000" chỉ tốc độ 1000 Mbps (1 Gbps), "Base" là Baseband (băng tần cơ sở), và "T" thường đại diện cho Twisted Pair (cáp đồng xoắn đôi).*

**Câu 112:** Tại sao các tuyến cáp quang biển quốc tế thường là mục tiêu bảo vệ quan trọng của an ninh mạng quốc gia?
A. Vì chúng chứa các bản ghi mã nguồn hệ điều hành.
B. Vì chúng truyền tải phần lớn lưu lượng truy cập Internet liên lục địa; nếu đứt sẽ gây gián đoạn nghiêm trọng liên lạc quốc tế.
C. Vì chúng cung cấp điện năng cho các vệ tinh.
D. Vì cáp quang dễ bị nhiễu điện từ bởi tàu ngầm.
*Đáp án: B*
*Giải thích: Hơn 95% lưu lượng thoại và dữ liệu liên lục địa đi qua cáp quang biển (không phải vệ tinh), do đó chúng là cơ sở hạ tầng mạng trọng yếu.*

**Câu 113:** Đâu là đặc trưng cơ bản của mô hình điện toán Đám mây (Cloud Computing) về mặt cung cấp tài nguyên mạng?
A. Tài nguyên được cấp phát cố định vĩnh viễn và không thể thay đổi.
B. Mọi dữ liệu phải lưu trữ cục bộ trên máy tính người dùng trước khi đồng bộ.
C. Tài nguyên (Server, Storage, Network) được cung cấp theo nhu cầu (on-demand), tính phí theo mức sử dụng thực tế (pay-as-you-go).
D. Chỉ cung cấp dịch vụ trên các hệ thống mạng không dây.
*Đáp án: C*
*Giải thích: Cloud Computing cho phép doanh nghiệp thuê hạ tầng IT linh hoạt thay vì phải mua và tự quản lý các máy chủ vật lý, giống như việc trả tiền điện, nước.*

**Câu 114:** "ISP" là viết tắt của cụm từ nào?
A. Internet Security Protocol
B. Internal System Process
C. Internet Service Provider
D. Integrated Server Platform
*Đáp án: C*
*Giải thích: Internet Service Provider (Nhà cung cấp dịch vụ Internet), ví dụ như VNPT, Viettel, FPT Telecom.*

**Câu 115:** Phương pháp chuyển mạch nào thiết lập một "Đường hầm" vật lý ảo (chức năng như ống nước nối thông) độc quyền giữa nguồn và đích trước khi truyền?
A. Packet Switching
B. Datagram Switching
C. Circuit Switching
D. Message Switching
*Đáp án: C*
*Giải thích: Chuyển mạch kênh (Circuit Switching - dùng trong hệ thống điện thoại truyền thống) luôn dành riêng (reserve) tài nguyên mạch cho mỗi cuộc gọi từ lúc bắt đầu tới lúc kết thúc.*

**Câu 116:** Thuật ngữ "Throughput" (Thông lượng) được định nghĩa là:
A. Tốc độ lan truyền tín hiệu ánh sáng trong sợi quang.
B. Lượng dữ liệu thực tế được truyền thành công từ máy nguồn đến máy đích trong một đơn vị thời gian (bps).
C. Tần số của sóng Wi-Fi đang sử dụng.
D. Dung lượng lưu trữ của ổ cứng máy chủ.
*Đáp án: B*
*Giải thích: Trong khi "Bandwidth" (băng thông) là tốc độ truyền dẫn lý thuyết tối đa, "Throughput" là lượng bit thực tế đến được đích trong 1 giây (thường nhỏ hơn hoặc bằng băng thông).*

**Câu 117:** Mất gói (Packet Loss) do tràn bộ đệm tại Router có thể dẫn đến hậu quả gì ở tầng TCP của thiết bị gửi?
A. Mạch vật lý bị ngắn mạch.
B. TCP sẽ bỏ qua và không gửi lại dữ liệu đó.
C. TCP sẽ phát hiện việc không có phản hồi (ACK) và tiến hành truyền lại gói tin (Retransmission).
D. Thiết bị gửi lập tức ngắt kết nối Internet.
*Đáp án: C*
*Giải thích: TCP đảm bảo độ tin cậy. Khi gói tin rớt tại router, đích không nhận được nên không gửi biên nhận (ACK). Sau khoảng thời gian chờ (Timeout), TCP nguồn sẽ gửi lại gói tin.*

**Câu 118:** Cơ chế nào giúp router tránh được việc các gói tin IP lặp vô tận trong mạng do cấu hình định tuyến sai (ví dụ: vòng lặp định tuyến - routing loop)?
A. Checksum ở IP Header.
B. Trường TTL (Time to Live) ở IP Header.
C. Sử dụng địa chỉ MAC thay cho IP.
D. Mã hóa gói tin bằng giao thức IPSec.
*Đáp án: B*
*Giải thích: Field TTL (Time To Live) trong gói IPv4 được khởi tạo bởi nguồn (vd: 64). Mỗi khi qua 1 router, TTL giảm đi 1. Nếu TTL = 0, router sẽ drop gói tin để ngăn nó lặp mãi mãi.*

**Câu 119:** Phishing là hình thức tấn công an ninh mạng nào?
A. Chiếm quyền điều khiển router mạng lõi.
B. Gửi email hoặc tin nhắn giả mạo một tổ chức uy tín (ngân hàng, dịch vụ) để lừa người dùng cung cấp thông tin nhạy cảm (mật khẩu, thẻ tín dụng).
C. Gửi quá tải gói tin để đánh sập web server.
D. Tiêm mã SQL độc hại vào cơ sở dữ liệu.
*Đáp án: B*
*Giải thích: Phishing là lừa đảo (social engineering) dựa trên tâm lý người dùng thay vì tấn công kỹ thuật thuần túy vào hệ thống mạng.*

**Câu 120:** "Port Scanning" (Quét cổng) là một hoạt động thường được thực hiện ở giai đoạn nào của một cuộc tấn công mạng?
A. Giai đoạn phá hoại (Destruction)
B. Giai đoạn trinh sát, thu thập thông tin (Reconnaissance)
C. Giai đoạn từ chối dịch vụ (DoS)
D. Giai đoạn lây nhiễm Virus
*Đáp án: B*
*Giải thích: Port scan giúp hacker thăm dò xem các cổng (port) nào đang mở và dịch vụ/ứng dụng nào đang chạy trên máy chủ mục tiêu (ví dụ tìm xem port 80 - web, port 22 - SSH có mở không) để tìm lỗ hổng khai thác.*

**Câu 121:** Mạng PAN (Personal Area Network) thường bao phủ một khu vực có bán kính khoảng bao nhiêu?
A. Hàng ngàn Kilomet.
B. Vài chục đến vài trăm Kilomet.
C. Trong phạm vi một phòng hoặc một khoảng không gian nhỏ (vài mét) quanh một cá nhân.
D. Toàn bộ một khuôn viên trường đại học.
*Đáp án: C*
*Giải thích: PAN điển hình nhất là mạng kết nối giữa điện thoại và tai nghe Bluetooth, hoặc đồng hồ thông minh với tầm hoạt động rất ngắn.*

**Câu 122:** Thành phần nào trong kiến trúc phần mềm mạng máy tính thường được cài đặt sẵn bên trong Hệ điều hành (OS)?
A. Trình duyệt Web (Chrome, Firefox).
B. Client game online.
C. Cấu trúc các tầng Network và Transport (như TCP/IP stack).
D. Mã nguồn của trang web HTML.
*Đáp án: C*
*Giải thích: Phần mềm cho tầng Ứng dụng (Application) do lập trình viên viết, nhưng việc triển khai tầng Transport (TCP/UDP) và tầng Network (IP) là một phần nhân của hệ điều hành (Windows, Linux).*

**Câu 123:** Chuẩn IEEE 802.3 là chuẩn kỹ thuật quy định cho loại hình mạng nào?
A. Wi-Fi
B. Ethernet LAN
C. Mạng di động 4G
D. Bluetooth
*Đáp án: B*
*Giải thích: Các giao thức LAN có dây phổ biến đều thuộc chuẩn IEEE 802.3 (Ethernet). Wi-Fi là chuẩn IEEE 802.11.*

**Câu 124:** Thiết bị nào sau đây hoạt động ở Tầng 2 (Data Link Layer) và có khả năng đọc địa chỉ MAC để chuyển tiếp Frame?
A. Hub
B. Repeater
C. Switch
D. Router
*Đáp án: C*
*Giải thích: Hub và Repeater là thiết bị tầng 1 (chỉ khuyếch đại tín hiệu điện). Switch là thiết bị tầng 2, có bảng địa chỉ MAC (MAC table) để chuyển mạch Frame một cách thông minh.*

**Câu 125:** Một trong những lợi ích của Mạng riêng ảo (VPN) đối với nhân viên làm việc từ xa (Work from home) là:
A. Tăng tốc độ đường truyền Internet tại nhà của họ lên mức Gigabit.
B. Cung cấp kết nối an toàn vào mạng nội bộ công ty như thể họ đang cắm dây trực tiếp vào switch của văn phòng.
C. Miễn phí cước Internet hàng tháng.
D. Thay thế hoàn toàn phần mềm diệt virus trên máy tính cá nhân.
*Đáp án: B*
*Giải thích: VPN thiết lập một liên kết logic bảo mật qua Internet, định tuyến mọi lưu lượng của máy nhân viên vào mạng Intranet nội bộ của công ty.*

**Câu 126:** Kỹ thuật nào trong mạng lõi cho phép hệ thống phân biệt các gói tin thuộc các ứng dụng (như Web, Video) để ưu tiên truyền trước (QoS - Quality of Service)?
A. Đóng gói toàn bộ dữ liệu.
B. Gắn cờ (Tagging/Marking) trong Header để xác định độ ưu tiên của gói tin.
C. Sử dụng địa chỉ MAC thay thế IP.
D. Xóa bớt nội dung của gói tin.
*Đáp án: B*
*Giải thích: Các giao thức như Differentiated Services (DiffServ) ở tầng IP sử dụng một trường (TOS/DSCP) trong Header để đánh dấu mức độ ưu tiên của gói tin.*

**Câu 127:** Đặc điểm chính của đường cáp quang lõi đơn (Single-mode fiber) so với lõi đa (Multi-mode fiber) là gì?
A. Khoảng cách truyền dẫn ngắn hơn rất nhiều.
B. Đường kính lõi rất nhỏ (khoảng 8-10 micro mét), chỉ cho phép một tia sáng (mode) truyền dọc trục, độ suy hao cực thấp, dùng cho khoảng cách xa.
C. Lõi rất to, ánh sáng phản xạ liên tục, truyền dữ liệu chậm.
D. Chi phí rẻ hơn, thường dùng trong hệ thống mạng nội bộ LAN.
*Đáp án: B*
*Giải thích: Single-mode dùng nguồn sáng Laser, ít tán sắc, nên dùng để kéo cáp quang biển hoặc xuyên quốc gia.*

**Câu 128:** Băng thông (Bandwidth) thường được đo bằng đơn vị nào?
A. Hertz (Hz)
B. Bits per second (bps)
C. Bytes
D. B và A đều đúng trong các ngữ cảnh kỹ thuật khác nhau.
*Đáp án: D*
*Giải thích: Trong kỹ thuật viễn thông (vật lý), băng thông đo độ rộng dải tần số (Hz). Trong khoa học máy tính (mạng logic), băng thông chỉ tốc độ truyền dữ liệu (bps).*

**Câu 129:** Trong mô hình Client-Server, một đặc điểm quan trọng của Server là:
A. Luôn có IP động để bảo mật.
B. Luôn luôn trong trạng thái chờ nhận các yêu cầu kết nối từ Client, và thường có một địa chỉ IP tĩnh.
C. Khởi xướng kết nối tới Client trước.
D. Chỉ xử lý một Client duy nhất tại một thời điểm.
*Đáp án: B*
*Giải thích: Máy chủ (Server) là thiết bị cung cấp dịch vụ, nó phải ở trạng thái "lắng nghe" tại một địa chỉ cố định để Client có thể tìm đến.*

**Câu 130:** Trong thuật ngữ mạng, RFC (Request For Comments) là các tài liệu mô tả:
A. Các lệnh Unix cơ bản.
B. Cấu trúc mạng nội bộ của các công ty công nghệ lớn.
C. Các đề xuất, chuẩn kỹ thuật giao thức mạng (ví dụ: HTTP, TCP/IP) do IETF công bố.
D. Bảng giá dịch vụ của các ISP.
*Đáp án: C*
*Giải thích: RFC là các chuẩn mở để bất kỳ ai phát triển phần mềm/thiết bị cũng có thể tuân thủ, giúp các thiết bị khác hãng nói chung ngôn ngữ.*

**Câu 131:** Đâu KHÔNG phải là một môi trường truyền dẫn vật lý trong mạng?
A. Sóng siêu âm.
B. Cáp quang.
C. Cáp đồng xoắn đôi.
D. Sóng điện từ (vô tuyến).
*Đáp án: A*
*Giải thích: Sóng siêu âm thường dùng trong radar, y tế, hoặc thông tin dưới nước tầm ngắn, không phải là phương tiện phổ biến cho mạng máy tính.*

**Câu 132:** Khi một trình duyệt web yêu cầu một trang web từ máy chủ, nó đóng vai trò gì trong kiến trúc mạng?
A. Máy chủ (Server)
B. Máy khách (Client)
C. Bộ định tuyến (Router)
D. Bộ chuyển mạch (Switch)
*Đáp án: B*
*Giải thích: Máy khách là ứng dụng khởi tạo yêu cầu, máy chủ là ứng dụng tiếp nhận và phản hồi yêu cầu.*

**Câu 133:** Tầng nào trong mô hình OSI KHÔNG tồn tại trực tiếp như một tầng độc lập trong mô hình TCP/IP?
A. Transport Layer (Tầng Giao vận)
B. Presentation Layer (Tầng Trình diễn)
C. Network Layer (Tầng Mạng)
D. Application Layer (Tầng Ứng dụng)
*Đáp án: B*
*Giải thích: Mô hình OSI có tầng Trình diễn và Phiên (Session), trong TCP/IP chức năng của 2 tầng này (nếu cần) được gộp chung vào tầng Application.*

**Câu 134:** Để kết nối các mạng LAN lại với nhau và định tuyến dữ liệu giữa chúng, thiết bị nào sau đây là phù hợp nhất?
A. Hub
B. Switch Layer 2
C. Router
D. Repeater
*Đáp án: C*
*Giải thích: Router hoạt động ở tầng Mạng (Network Layer - Layer 3), có khả năng phân tích IP và định tuyến dữ liệu giữa các dải mạng (Subnet/LAN) khác nhau.*

**Câu 135:** Độ tin cậy (Reliability) trong truyền dẫn dữ liệu mạng có nghĩa là:
A. Dữ liệu phải được mã hóa 100%.
B. Tốc độ truyền luôn đạt mức tối đa ghi trên cáp.
C. Đảm bảo dữ liệu gửi đi tới đích nguyên vẹn, không bị lỗi bit, không bị mất, trùng lặp và đúng thứ tự.
D. Hệ thống mạng không bao giờ bị mất điện.
*Đáp án: C*
*Giải thích: Độ tin cậy trong giao thức (như TCP) quan tâm đến tính vẹn toàn và đầy đủ của luồng dữ liệu logic giữa 2 tiến trình ứng dụng.*

**Câu 136:** Tấn công "Man-in-the-middle" (MITM) là loại tấn công nào?
A. Kẻ tấn công làm quá tải máy chủ bằng các lệnh ping.
B. Kẻ tấn công đánh cắp thiết bị vật lý.
C. Kẻ tấn công chen ngang vào giữa kết nối giao tiếp của hai thiết bị, bí mật nghe lén hoặc giả mạo dữ liệu gửi qua lại.
D. Kẻ tấn công mã hóa tệp tin và đòi tiền chuộc.
*Đáp án: C*
*Giải thích: Trong MITM, A tưởng đang gửi thông tin cho B, nhưng thực chất đang gửi cho Hacker, Hacker ghi lại thông tin rồi chuyển tiếp cho B.*

**Câu 137:** Kiến trúc mạng nào mà các node vừa đóng vai trò là máy khách yêu cầu dịch vụ, vừa đóng vai trò là máy chủ cung cấp dịch vụ cho các node khác?
A. Client-Server
B. Point-to-Multipoint
C. Peer-to-Peer (P2P)
D. Mạng hình sao (Star topology)
*Đáp án: C*
*Giải thích: P2P (mạng ngang hàng) phân tán tài nguyên. Ví dụ trong BitTorrent, bạn vừa tải file về (Client) vừa tải file lên cho người khác (Server).*

**Câu 138:** Đóng gói dữ liệu (Encapsulation) tại thiết bị phát diễn ra theo thứ tự nào (từ trên xuống dưới trong mô hình OSI)?
A. Application -> Transport -> Network -> Data Link -> Physical
B. Physical -> Data Link -> Network -> Transport -> Application
C. Network -> Transport -> Application -> Data Link -> Physical
D. Transport -> Network -> Data Link -> Application -> Physical
*Đáp án: A*
*Giải thích: Khi phát, ứng dụng sinh ra data, chuyển xuống Transport đóng gói thành Segment, Network đóng thành Packet, Data Link đóng thành Frame, truyền dạng bit ở Physical.*

**Câu 139:** Ở tầng Data Link (Liên kết dữ liệu), đơn vị dữ liệu được gọi là gì?
A. Datagram
B. Segment
C. Frame
D. Bit
*Đáp án: C*
*Giải thích: Data Link tạo ra các Khung (Frame), bao quanh Packet của tầng Network bằng MAC Header và FCS Trailer.*

**Câu 140:** Điểm khác biệt quan trọng của IPv6 so với IPv4 ở thiết kế Header là:
A. IPv6 Header thay đổi độ dài liên tục.
B. IPv6 Header có kích thước cố định (40 bytes), lược bỏ các trường ít dùng (như checksum, fragmentation) để router xử lý nhanh hơn.
C. IPv6 loại bỏ trường địa chỉ đích.
D. IPv6 yêu cầu mọi thiết bị phải dùng Wi-Fi.
*Đáp án: B*
*Giải thích: Header IPv6 gọn gàng và cố định độ dài, việc phân mảnh được đẩy về End-system để giảm tải cho Router trên mạng lõi.*

**Câu 141:** Mạng di động (Cellular network) chia khu vực địa lý thành các:
A. Router.
B. Cell (Tế bào/Ô).
C. Switch.
D. Server.
*Đáp án: B*
*Giải thích: "Cellular" (Tế bào) ngụ ý việc chia vùng phủ sóng thành các ô nhỏ hình lục giác, mỗi ô do một trạm phát sóng (Base Station) quản lý.*

**Câu 142:** "Propagation speed" (Tốc độ lan truyền tín hiệu) trên cáp đồng xoắn đôi khoảng bao nhiêu so với tốc độ ánh sáng trong chân không (c = 3x10^8 m/s)?
A. Bằng chính xác c.
B. Lớn hơn c.
C. Khoảng 2x10^8 m/s (khoảng 2/3 c).
D. Rất chậm, khoảng 340 m/s (tốc độ âm thanh).
*Đáp án: C*
*Giải thích: Trong môi trường vật chất (đồng, thủy tinh), tín hiệu điện/ánh sáng truyền chậm hơn so với trong chân không.*

**Câu 143:** Cổng kết nối (Interface) trên Router là nơi:
A. Nối cáp màn hình vào router.
B. Nơi kết nối vật lý đường truyền (link) vào bộ định tuyến, và mỗi interface thường có một địa chỉ IP riêng.
C. Để cắm ổ cứng lưu trữ phim.
D. Chứa nút nguồn của router.
*Đáp án: B*
*Giải thích: Router kết nối nhiều mạng với nhau. Mỗi cổng của router cắm vào một mạng (Subnet) và cần có IP thuộc mạng đó làm Default Gateway.*

**Câu 144:** Đâu là đặc điểm cơ bản của hệ thống thông tin theo phương pháp Broadcast (Quảng bá)?
A. Gửi gói tin từ một nút đến một nút đích duy nhất cụ thể (Unicast).
B. Gửi gói tin từ một nút đến một nhóm nút cụ thể (Multicast).
C. Gửi gói tin từ một nút đến tất cả các nút khác trên cùng môi trường mạng.
D. Không gửi dữ liệu gì, chỉ nhận.
*Đáp án: C*
*Giải thích: Broadcast (Quảng bá) giống như dùng loa phóng thanh, tất cả thiết bị trên đường truyền đó đều nhận được và xử lý thông điệp.*

**Câu 145:** Hiện tượng tắc nghẽn (Congestion) trong mạng xảy ra khi:
A. Có sự cố đứt cáp quang dưới biển.
B. Tốc độ bit do các máy tính phát vào mạng vượt quá khả năng xử lý và chuyển tiếp của các bộ định tuyến (router) trên mạng.
C. Cáp đồng bị nhiễu do đường dây điện.
D. Máy tính chạy quá nhiều phần mềm diệt virus.
*Đáp án: B*
*Giải thích: Tắc nghẽn là vấn đề về "lưu lượng", khi có quá nhiều xe (gói tin) dồn vào một nút giao thông hẹp (router) cùng lúc.*

**Câu 146:** Khi một gói tin đi từ nguồn đến đích qua mạng Internet, địa chỉ nào trong gói tin sẽ THAY ĐỔI mỗi khi qua một Router?
A. Địa chỉ IP nguồn.
B. Địa chỉ IP đích.
C. Địa chỉ MAC nguồn và MAC đích.
D. Cổng (Port) ứng dụng.
*Đáp án: C*
*Giải thích: Địa chỉ IP đại diện cho End-to-End (từ trạm đầu đến trạm cuối) nên không đổi. Địa chỉ MAC đại diện cho Link-to-Link (nhảy từ node này sang node kề cận) nên sẽ được ghi đè (đóng gói lại Frame) ở mỗi router.*

**Câu 147:** Một lý do tại sao cáp đồng trục (Coaxial cable) tốt hơn cáp xoắn đôi không bọc chống nhiễu (UTP) ở tần số cao là gì?
A. Nó nhẹ hơn rất nhiều.
B. Cấu trúc lõi đồng nằm chính giữa, bọc bởi lớp cách điện và lưới kim loại đan bên ngoài giúp cản trở nhiễu điện từ bên ngoài tốt hơn.
C. Nó truyền dữ liệu bằng tia sáng chứ không phải xung điện.
D. Nó rẻ hơn UTP 10 lần.
*Đáp án: B*
*Giải thích: Cáp đồng trục (dùng trong truyền hình cáp) có lớp shield (lưới kim loại) chống nhiễu (EMI) cực tốt, cho phép băng thông cao và khoảng cách xa hơn UTP.*

**Câu 148:** Đơn vị quy chuẩn để truyền dữ liệu trên Internet (Datagram) thường quy định một trường kích thước tối đa mà một Frame của đường truyền bên dưới (như Ethernet) có thể tải, đó là:
A. Bandwidth
B. Throughput
C. MTU (Maximum Transmission Unit)
D. TTL (Time to Live)
*Đáp án: C*
*Giải thích: MTU là kích thước lớn nhất (thường là 1500 bytes cho Ethernet) của một gói tin IP mà mạng có thể truyền đi mà không cần cắt nhỏ (fragmentation).*

**Câu 149:** Trong mô hình TCP/IP, trách nhiệm "Kiểm tra tính toàn vẹn" (Error Checking) của tín hiệu vật lý khi truyền qua sợi cáp quang thường thuộc về tầng nào?
A. Application
B. Transport
C. Data Link
D. Network
*Đáp án: C*
*Giải thích: Tầng Liên kết dữ liệu (Data Link) thường có bộ tạo mã lỗi (FCS) để kiểm tra xem một Frame có bị biến đổi bit trong quá trình đi qua môi trường truyền vật lý hay không.*

**Câu 150:** Giao thức nào cho phép các thiết bị trong mạng tự động xin cấp phát địa chỉ IP một cách linh hoạt, thay vì cấu hình thủ công?
A. DNS
B. DHCP
C. HTTP
D. FTP
*Đáp án: B*
*Giải thích: Dynamic Host Configuration Protocol (DHCP) tự động gán địa chỉ IP, Subnet Mask, Gateway và IP của DNS server cho thiết bị khi vừa kết nối mạng.*

**Câu 151:** Trong các công nghệ truyền tải băng rộng (Broadband), "FTTH" là viết tắt của:
A. File Transfer To Home
B. Fiber To The Home
C. Fast Telecom Transfer Hub
D. Frequency Time Transmission Header
*Đáp án: B*
*Giải thích: FTTH là công nghệ cáp quang đưa trực tiếp đến tận thiết bị quang (ONT/ONU) tại nhà người dùng, cung cấp tốc độ RẤT cao.*

**Câu 152:** Trong chuyển mạch gói (Packet Switching), nếu một gói tin đến một router khi bộ đệm (buffer) của cổng đích đã đầy, thì điều gì sẽ xảy ra?
A. Gói tin sẽ tự động quay lại máy phát.
B. Gói tin bị vứt bỏ (Packet Loss / Dropped).
C. Router sẽ nén gói tin lại để tiết kiệm bộ đệm.
D. Gói tin sẽ được chuyển sang cổng khác không liên quan.
*Đáp án: B*
*Giải thích: Khi không còn chỗ chứa trong hàng đợi (buffer overflow), các gói tin đến sẽ bị loại bỏ, buộc máy phát (dựa trên TCP) phải gửi lại sau.*

**Câu 153:** Yếu tố "Throughput" (Thông lượng) đầu cuối chịu ảnh hưởng lớn nhất bởi:
A. Cấu hình máy tính của người dùng.
B. Dải tần số của sóng Wi-Fi.
C. Liên kết có băng thông thấp nhất trên tuyến đường (Bottleneck link).
D. Số lượng trình duyệt web đang mở.
*Đáp án: C*
*Giải thích: Nước không thể chảy qua ống nhanh hơn đoạn ống nhỏ nhất của nó.*

**Câu 154:** "Sniffing" trên mạng Wi-Fi công cộng không có mật khẩu nguy hiểm như thế nào?
A. Hacker có thể kiểm soát chuột và bàn phím máy tính của bạn.
B. Các gói tin bay trong không gian bị bắt lại bởi card mạng của hacker ở chế độ Promiscuous, làm lộ mật khẩu, cookie nếu không được mã hóa (HTTPS).
C. Hacker có thể cắt đứt cáp quang từ xa.
D. Mạng Wi-Fi tự động mã hóa mọi thứ nên không hề nguy hiểm.
*Đáp án: B*
*Giải thích: Packet Sniffing nguy hiểm vì kẻ nghe lén không cần kết nối vào máy bạn mà chỉ thu sóng vô tuyến trôi nổi trong không gian xung quanh.*

**Câu 155:** Mã độc tống tiền (Ransomware) ảnh hưởng đến dữ liệu người dùng mạng bằng cách nào?
A. Xóa hoàn toàn dữ liệu.
B. Chia sẻ dữ liệu công khai trên Internet.
C. Mã hóa toàn bộ dữ liệu trên thiết bị và yêu cầu nạn nhân trả tiền chuộc để lấy khóa giải mã.
D. Ẩn các thư mục và file.
*Đáp án: C*
*Giải thích: Ransomware sử dụng các thuật toán mã hóa mạnh, thường lây lan qua email phishing hoặc lỗ hổng giao thức mạng (như SMB trong WannaCry).*

**Câu 156:** Trong mạng LAN, địa chỉ MAC (Media Access Control) có độ dài là bao nhiêu bit?
A. 32 bit
B. 48 bit
C. 64 bit
D. 128 bit
*Đáp án: B*
*Giải thích: MAC Address (ví dụ 00:1A:2B:3C:4D:5E) dài 48 bit, thường được gán cứng (burned-in) vào ROM của card mạng (NIC) bởi nhà sản xuất.*

**Câu 157:** Điểm giao cắt (Internet Exchange Point - IXP) trong kiến trúc ISP dùng để làm gì?
A. Là nơi lưu trữ toàn bộ phim của Netflix.
B. Là trạm phát sóng Wi-Fi khổng lồ của một quốc gia.
C. Nơi các ISP khác nhau kết nối trực tiếp thiết bị định tuyến của họ với nhau để trao đổi lưu lượng ngang hàng (peering) mà không tốn phí qua ISP cấp cao hơn.
D. Cổng chuyển đổi từ IPv4 sang IPv6.
*Đáp án: C*
*Giải thích: IXP giúp giảm độ trễ, giảm chi phí chuyển tiếp (transit) bằng cách cho phép 2 ISP nối tắt (peer) với nhau (vd: VNPT nối trực tiếp FPT).*

**Câu 158:** Một trong các công nghệ kết nối mạng diện rộng (WAN) kiểu cũ dựa trên việc cấp phát các khe thời gian (time slot) cho điện thoại là công nghệ nào?
A. TDM (Time-Division Multiplexing) trên đường dây T1/E1.
B. ADSL
C. 5G
D. Gigabit Ethernet
*Đáp án: A*
*Giải thích: TDM chia một khung thời gian thành nhiều khe nhỏ, mỗi cuộc gọi/phiên được cấp 1 khe cố định, đảm bảo không bị nghẽn mạch (Circuit Switching).*

**Câu 159:** Tầng "Presentation" (Trình diễn) trong OSI đóng vai trò chính là gì?
A. Chuyển địa chỉ MAC thành địa chỉ IP.
B. Đảm bảo dữ liệu gửi từ ứng dụng nguồn có thể đọc được bởi ứng dụng đích (chuyển đổi định dạng, nén, mã hóa).
C. Khởi tạo, duy trì và kết thúc các phiên kết nối.
D. Định tuyến luồng video đến màn hình.
*Đáp án: B*
*Giải thích: Tầng này lo về Syntax và Semantics của dữ liệu. Ví dụ, đổi mã EBCDIC sang ASCII, mã hóa SSL/TLS, nén JPEG/MPEG.*

**Câu 160:** Cổng mặc định (Default port) cho dịch vụ HTTPS (Web bảo mật) là bao nhiêu?
A. 21
B. 80
C. 443
D. 25
*Đáp án: C*
*Giải thích: Port 80 là HTTP không mã hóa. Port 443 là HTTPS (HTTP over TLS/SSL).*

**Câu 161:** "Ping" là một tiện ích dựa trên giao thức nào để kiểm tra sự tồn tại (reachability) của một trạm trên mạng?
A. HTTP
B. TCP
C. UDP
D. ICMP
*Đáp án: D*
*Giải thích: Ping gửi gói tin ICMP Echo Request và chờ nhận ICMP Echo Reply từ máy đích.*

**Câu 162:** Việc "Cập nhật bảng định tuyến" (Routing update) giữa các Router diễn ra ở Mặt phẳng (Plane) nào của hệ thống mạng?
A. Data Plane (Mặt phẳng dữ liệu)
B. Control Plane (Mặt phẳng điều khiển)
C. Management Plane (Mặt phẳng quản trị)
D. Physical Plane (Mặt phẳng vật lý)
*Đáp án: B*
*Giải thích: Logic tính toán đường đi, trao đổi thông tin định tuyến (OSPF, BGP) đều diễn ra trên Control Plane.*

**Câu 163:** Mạng "Mesh" (Cấu hình lưới) có ưu điểm vượt trội nào so với "Star" (Cấu hình sao)?
A. Rẻ hơn và tốn ít dây dẫn hơn.
B. Có tính dự phòng cao (Fault tolerance), khi một đường đứt vẫn còn đường khác.
C. Dễ cài đặt hơn.
D. Khôn cần dùng đến Router.
*Đáp án: B*
*Giải thích: Lưới có nhiều liên kết dự phòng giữa các node, tăng độ tin cậy nhưng chi phí cáp/cổng rất cao (thường dùng ở lõi mạng).*

**Câu 164:** Các thiết bị "Internet of Things" (IoT) kết nối mạng thường đối mặt với thách thức lớn nhất là gì?
A. Kích thước vật lý quá lớn.
B. Không có địa chỉ MAC.
C. Năng lực xử lý yếu, dung lượng pin ít và bảo mật kém dễ bị lợi dụng thành Botnet.
D. Chỉ kết nối được qua cáp quang.
*Đáp án: C*
*Giải thích: Camera IP, bóng đèn thông minh... thường dùng mật khẩu mặc định, phần cứng yếu không có mã hóa tốt, dễ bị hack (như vụ botnet Mirai).*

**Câu 165:** Giao thức nào chuyên dùng để gửi thư điện tử (Email) từ một Mail Client đến Mail Server?
A. POP3
B. IMAP
C. SMTP
D. FTP
*Đáp án: C*
*Giải thích: SMTP (Simple Mail Transfer Protocol) dùng để GỬI (Push) email. POP3 và IMAP dùng để KÉO/NHẬN (Pull) email về máy người dùng.*

**Câu 166:** Hiện tượng suy hao tín hiệu (Attenuation) trên đường truyền cáp đồng xảy ra khi:
A. Tín hiệu bị hacker chặn lại.
B. Cường độ tín hiệu điện bị giảm dần (yếu đi) khi truyền qua một khoảng cách dài do điện trở của dây dẫn.
C. Có nhiều máy tính cùng truy cập.
D. Nhiệt độ môi trường quá thấp.
*Đáp án: B*
*Giải thích: Attenuation giới hạn khoảng cách tối đa của cáp đồng (ví dụ UTP dài tối đa khoảng 100m) trước khi cần một Repeater để khuếch đại lại.*

**Câu 167:** Khi truy cập trang web www.example.com, trước khi trình duyệt tải được nội dung, ứng dụng phải thực hiện thao tác nào đầu tiên để biết được IP của example.com?
A. Gửi gói tin Broadcast ARP.
B. Truy vấn hệ thống DNS (Domain Name System).
C. Gửi lệnh Ping trực tiếp.
D. Dò mật khẩu Wi-Fi.
*Đáp án: B*
*Giải thích: Trình duyệt phải phân giải tên miền (example.com) thành địa chỉ IP (vd: 93.184.216.34) qua DNS thì tầng Transport (TCP) mới biết đích đến để tạo kết nối.*

**Câu 168:** Tại sao cấu trúc mạng theo Layered (Phân tầng) giúp dễ dàng phát triển và cải tiến các ứng dụng mạng mới?
A. Vì ứng dụng không cần quan tâm đến cách định tuyến, cách đóng khung hay loại cáp vật lý. Mọi thứ bên dưới đã trong suốt (transparent).
B. Vì ứng dụng mới sẽ tự điều khiển phần cứng trực tiếp.
C. Vì cấu trúc tầng cấm các ngôn ngữ lập trình phức tạp.
D. Vì tầng Ứng dụng là tầng duy nhất trên Internet.
*Đáp án: A*
*Giải thích: Tính module hóa. Bạn viết một ứng dụng gọi video (Application), bạn chỉ đẩy dữ liệu xuống socket (Transport), bạn không cần biết người dùng đang dùng Wi-Fi hay Cáp quang, IPv4 hay IPv6.*

**Câu 169:** Trong kỹ thuật mạng di động (3G/4G/5G), "Handover" (Chuyển giao) là cơ chế gì?
A. Đổi SIM khi hết tiền.
B. Quá trình hệ thống tự động duy trì cuộc gọi hoặc luồng dữ liệu khi người dùng (thiết bị di động) di chuyển từ vùng phủ sóng của Cell/Trạm phát sóng này sang vùng phủ sóng của Cell/Trạm phát sóng khác.
C. Bật tắt chế độ máy bay.
D. Chuyển từ Wi-Fi sang 4G.
*Đáp án: B*
*Giải thích: Handover (hay Handoff) đảm bảo liên lạc không bị gián đoạn khi người dùng trên ô tô di chuyển tốc độ cao ngang qua các trạm BTS khác nhau.*

**Câu 170:** "Payload" trong thuật ngữ phân tích gói tin ám chỉ phần nào?
A. Phần Header của giao thức chứa địa chỉ.
B. Phần dữ liệu thực sự mang thông tin hữu ích mà tầng trên giao phó (không bao gồm Header/Trailer của tầng hiện tại).
C. Mã phát hiện lỗi ở cuối gói tin.
D. Nguồn điện cấp cho cáp mạng.
*Đáp án: B*
*Giải thích: Ví dụ: Với tầng Network (IP Packet), Payload chính là Segment của tầng Transport. Với một xe tải chở hàng, Payload là thùng hàng chứ không phải là đầu kéo.*

**Câu 171:** Một đường liên kết vệ tinh (Satellite link) có băng thông rất cao (ví dụ: 10 Gbps) nhưng độ trễ lan truyền cũng rất cao (250 ms). Đối với ứng dụng Telnet (gõ phím và xem kết quả tức thì trên server từ xa), liên kết này mang lại trải nghiệm như thế nào?
A. Rất mượt mà vì băng thông cao.
B. Rất tệ vì Telnet cần độ trễ thấp (low RTT), băng thông cao không giúp ích nhiều cho các gói tin rất nhỏ chứa 1 ký tự gõ phím.
C. Không thể sử dụng được vì Telnet bị cấm trên vệ tinh.
D. Mượt mà nhưng tốn nhiều pin.
*Đáp án: B*
*Giải thích: Ứng dụng tương tác như Telnet/SSH gửi 1 phím tốn rất ít bit (không cần băng thông lớn), nhưng cần thời gian phản hồi nhanh (RTT nhỏ). Độ trễ cao sẽ làm chữ hiện lên màn hình bị chậm.*

**Câu 172:** Kỹ thuật FDM (Frequency Division Multiplexing) chia sẻ một môi trường truyền bằng cách:
A. Cắt thời gian thành các rãnh siêu nhỏ.
B. Gán cho mỗi người dùng một địa chỉ MAC khác nhau.
C. Chia dải tần số của môi trường truyền thành nhiều kênh tần số hẹp hơn, mỗi kết nối dùng một tần số riêng biệt, phát cùng lúc.
D. Mã hóa gói tin bằng các khóa công khai khác nhau.
*Đáp án: C*
*Giải thích: Tương tự như đài FM, cùng một lúc có nhiều kênh phát trên không khí, mỗi kênh (VOV, XoneFM) chiếm một dải tần số riêng (102MHz, 104MHz...).*

**Câu 173:** Thiết bị "Modem" cáp đồng (ADSL/VDSL) có chức năng chính là gì?
A. Lọc các trang web độc hại.
B. Chuyển đổi tín hiệu số (digital) của máy tính thành tín hiệu tương tự (analog) để truyền trên dây điện thoại, và ngược lại.
C. Phát sóng Wi-Fi (Modem thuần túy không có chức năng này, thường được tích hợp thành Wireless Router).
D. Định tuyến IP giữa các quốc gia.
*Đáp án: B*
*Giải thích: Modulator-Demodulator (Điều chế và Giải điều chế) giúp tín hiệu số 0/1 "cưỡi" lên sóng mang analog tần số cao trên đường dây điện thoại cũ.*

**Câu 174:** Trong số liệu đo lường, khái niệm "Jitter" là chỉ báo về:
A. Tốc độ cao nhất đạt được trong một phút.
B. Tỷ lệ mất gói tin trên mạng.
C. Sự biến thiên (không ổn định) của độ trễ gói tin (Delay variation) giữa các gói tin liên tiếp.
D. Số lượng kết nối bị đứt.
*Đáp án: C*
*Giải thích: Jitter cực kỳ quan trọng đối với VoIP (gọi thoại). Nếu gói 1 đến trễ 10ms, gói 2 trễ 50ms, gói 3 trễ 5ms, sự chênh lệch này làm giọng nói bị méo.*

**Câu 175:** Để tăng tính dự phòng, các doanh nghiệp thường đăng ký Internet (Multi-homing) bằng cách nào?
A. Nối hai máy tính với cùng một modem.
B. Kết nối mạng nội bộ của họ tới hai hoặc nhiều ISP khác nhau cùng lúc.
C. Mua hai gói cước từ cùng một ISP.
D. Sử dụng 2 card mạng để gắn 2 dây vào cùng một Switch.
*Đáp án: B*
*Giải thích: Multi-homing giúp doanh nghiệp không bị rớt mạng kể cả khi một ISP bị sự cố cáp đứt.*

**Câu 176:** Thuật ngữ "Store-and-forward" (Lưu và chuyển tiếp) gây ra loại trễ (delay) nào trong mạng?
A. Transmission Delay (Trễ truyền dẫn)
B. Propagation Delay (Trễ lan truyền)
C. Nodal Processing Delay (Trễ xử lý nút)
D. A và C đều đúng.
*Đáp án: A*
*Giải thích: Do phải chờ nhận đủ toàn bộ L bit (phụ thuộc vào tốc độ đường truyền đầu vào) rồi mới đẩy tiếp, trễ truyền dẫn tích lũy tại mỗi nút.*

**Câu 177:** Lợi thế của cấu trúc mạng (Network Topology) dạng "Bus" là gì?
A. Dễ cô lập vị trí cáp bị đứt.
B. Có thể hỗ trợ số lượng node vô hạn mà không suy giảm tốc độ.
C. Chi phí cáp thấp và dễ dàng thêm mới node (trong các mô hình cũ).
D. Hoàn toàn không xảy ra xung đột dữ liệu (collision).
*Đáp án: C*
*Giải thích: Mạng Bus cổ điển (như Ethernet 10Base-2 dùng 1 trục cáp đồng trục chung) tốn rất ít dây. Nhưng nếu trục chính đứt, toàn mạng tê liệt.*

**Câu 178:** Loại phần mềm độc hại nào ghi lại lịch sử thao tác bàn phím (Keystrokes) của người dùng một cách bí mật?
A. Ransomware
B. Keylogger (Một dạng Spyware)
C. Botnet
D. DDoS tool
*Đáp án: B*
*Giải thích: Keylogger được hacker cài cắm để theo dõi mọi phím gõ, nhằm đánh cắp mật khẩu, số thẻ tín dụng.*

**Câu 179:** Để đánh giá "Băng thông" thực tế kết nối từ nhà bạn ra quốc tế, bạn có thể sử dụng công cụ nào dưới đây?
A. Lệnh `ipconfig` hoặc `ifconfig`.
B. Truy cập các trang web đo kiểm tốc độ như Speedtest.net chọn server quốc tế.
C. Lệnh `arp -a`.
D. Nhìn vào tốc độ "100 Mbps" hiển thị trên kết nối mạng góc phải màn hình Windows.
*Đáp án: B*
*Giải thích: Tốc độ hiện trên Windows (100Mbps hoặc 1Gbps) chỉ là tốc độ từ máy bạn tới Modem/Switch trong nhà. Tốc độ ra quốc tế phải đo bằng việc tải/up thực tế đến server nước ngoài.*

**Câu 180:** Khái niệm "Full-Duplex" trong truyền thông có nghĩa là:
A. Thiết bị chỉ có thể gửi hoặc nhận trong một thời điểm (như bộ đàm).
B. Thiết bị có thể gửi và nhận dữ liệu đồng thời trên cùng một liên kết mà không bị đụng độ (như điện thoại, cáp mạng hiện đại).
C. Tốc độ truyền tải đạt mức tối đa.
D. Mạng hỗ trợ cả IP và MAC.
*Đáp án: B*
*Giải thích: Switch hiện đại và cáp UTP 4 cặp dây cho phép gửi (Tx) trên một cặp và nhận (Rx) trên một cặp khác đồng thời (Full-duplex), triệt tiêu collision.*

**Câu 181:** Tại sao kiến trúc OSI (7 tầng) thường được sử dụng trong giáo dục và lý thuyết, trong khi bộ giao thức TCP/IP (4 hoặc 5 tầng) lại là kiến trúc thống trị Internet thực tế?
A. Vì OSI chỉ do một người viết ra.
B. Vì các chuẩn của OSI được đưa ra trước khi giao thức thực tế được xây dựng phổ biến; trong khi TCP/IP được xây dựng thực tế rồi mới chuẩn hóa.
C. Vì OSI nhanh hơn TCP/IP.
D. Vì TCP/IP có bản quyền và đắt tiền hơn.
*Đáp án: B*
*Giải thích: TCP/IP phát triển từ dự án ARPANET của Bộ Quốc phòng Mỹ, tập trung vào tính thực tiễn (các giao thức hoạt động tốt). OSI là một mô hình thiết kế tham chiếu, hoàn thiện quá trễ so với sự bùng nổ của TCP/IP.*

**Câu 182:** Ký hiệu "bps" (bits per second) khác với "Bps" (Bytes per second) như thế nào?
A. Giống nhau hoàn toàn.
B. 1 Bps = 8 bps (1 Byte/giây = 8 bits/giây).
C. bps dùng cho cáp quang, Bps dùng cho Wi-Fi.
D. bps là viết hoa, Bps là viết thường.
*Đáp án: B*
*Giải thích: Các nhà mạng (ISP) bán gói cước tính bằng Megabit/s (Mbps), nhưng phần mềm tải file (như IDM, Chrome) tính tốc độ tải bằng Megabyte/s (MB/s). 1 MB/s bằng khoảng 8 Mbps.*

**Câu 183:** Nếu mạng LAN (cục bộ) của bạn sử dụng dải IP Private (ví dụ 192.168.1.x), công nghệ nào trên Router cho phép nhiều máy tính trong mạng truy cập Internet ra ngoài chỉ với một địa chỉ IP Public duy nhất?
A. DHCP (Dynamic Host Configuration Protocol)
B. NAT (Network Address Translation)
C. DNS (Domain Name System)
D. ARP (Address Resolution Protocol)
*Đáp án: B*
*Giải thích: NAT thực hiện biên dịch IP nội bộ (cùng với Port) thành 1 IP Public của Router khi gói tin đi ra Internet và làm ngược lại khi gói tin từ Internet về.*

**Câu 184:** Phương tiện vật lý nào sau đây bị giới hạn tầm nhìn thẳng (line-of-sight) và không thể đi xuyên tường tốt?
A. Cáp đồng.
B. Cáp quang.
C. Sóng siêu vi định hướng cao (Microwave) và sóng Milimet (trong 5G).
D. Sóng vô tuyến FM.
*Đáp án: C*
*Giải thích: Tần số càng cao (như sóng Microwave, mmWave 5G) bước sóng càng ngắn, do đó năng lượng xuyên phá vật cản càng kém và dễ bị hấp thụ bởi mưa, cây cối, tường nhà.*

**Câu 185:** Theo cách phân loại quy mô mạng, mạng lưới kết nối các chi nhánh của một tập đoàn xuyên quốc gia được gọi là gì?
A. LAN (Local Area Network)
B. PAN (Personal Area Network)
C. WAN (Wide Area Network)
D. MAN (Metropolitan Area Network)
*Đáp án: C*
*Giải thích: Mạng diện rộng (WAN) bao phủ không gian lớn (quốc gia, liên lục địa), sử dụng kết nối của các nhà cung cấp dịch vụ viễn thông.*

**Câu 186:** Giao thức nào hoạt động ở Tầng Ứng dụng (Application Layer)?
A. OSPF
B. TCP
C. FTP
D. IPv4
*Đáp án: C*
*Giải thích: FTP (File Transfer Protocol) là một giao thức ứng dụng để truyền tập tin.*

**Câu 187:** Trong cấu trúc liên kết Internet, các "Nội dung số" khổng lồ như YouTube, Facebook thường sử dụng hệ thống nào để lưu trữ bản sao dữ liệu gần người dùng (Edge of network) nhằm tăng tốc độ tải và giảm tắc nghẽn ở lõi mạng?
A. Content Delivery Networks (CDNs)
B. Storage Area Networks (SANs)
C. Tier-1 ISPs
D. Data Link Switches
*Đáp án: A*
*Giải thích: CDN (như Akamai, Cloudflare, Google Edge Network) đặt các máy chủ cache dữ liệu video/ảnh ở các ISP địa phương. Người dùng Việt Nam xem Youtube thường tải từ server CDN đặt ngay tại Việt Nam chứ không phải từ Mỹ.*

**Câu 188:** Trong một kiến trúc bảo mật mạng, một thiết bị/phần mềm được cấu hình để phân tích lưu lượng truy cập qua lại giữa LAN nội bộ và Internet để block các lưu lượng khả nghi được gọi là gì?
A. Modem
B. Firewall (Tường lửa)
C. DNS Server
D. Repeater
*Đáp án: B*
*Giải thích: Tường lửa kiểm tra header (và đôi khi là nội dung) của gói tin dựa trên tập quy tắc (ACL) để quyết định Cho phép (Allow) hay Chặn (Drop/Deny).*

**Câu 189:** Gói tin "Broadcast" tại Tầng 2 (MAC) có địa chỉ đích là gì (hệ thập lục phân)?
A. 00:00:00:00:00:00
B. FF:FF:FF:FF:FF:FF
C. 127.0.0.1
D. 255.255.255.255
*Đáp án: B*
*Giải thích: Địa chỉ MAC FF:FF:FF:FF:FF:FF có nghĩa là "gửi cho tất cả các thiết bị trên đoạn LAN hiện tại".*

**Câu 190:** "Trễ Hàng đợi" (Queueing Delay) có thể là 0 (không có trễ) trong trường hợp nào?
A. Khi gói tin rất dài.
B. Khi bộ định tuyến (router) hoàn toàn rỗng, gói tin đến được chuyển tiếp ra đường truyền ngay lập tức (La/R xấp xỉ 0).
C. Khi băng thông đường truyền bằng 0.
D. Trễ hàng đợi không bao giờ bằng 0.
*Đáp án: B*
*Giải thích: Nếu tốc độ xử lý và tốc độ đầu ra của router đủ đáp ứng tốc độ các gói tin đến mà không bị dồn ứ, gói tin sẽ không phải chờ.*

**Câu 191:** Điểm khác biệt giữa Virus và Worm là gì?
A. Virus không phá hoại, Worm có phá hoại.
B. Virus cần sự tương tác của con người (như mở file đính kèm) để kích hoạt, Worm tự khai thác lỗ hổng và nhân bản tự động qua mạng.
C. Virus lây qua mạng Wi-Fi, Worm lây qua mạng LAN.
D. Cả hai là một.
*Đáp án: B*
*Giải thích: Worm độc lập và tự túc, chúng có thể tự tìm kiếm các máy có lỗ hổng (như chưa cập nhật bản vá Windows) để tự động thâm nhập và lây lan cực nhanh.*

**Câu 192:** Mạng Botnet thường thực hiện kiểu tấn công nào hiệu quả nhất?
A. SQL Injection
B. Tấn công từ chối dịch vụ phân tán (DDoS)
C. Bắt gói tin (Sniffing) trong mạng LAN cá nhân.
D. Phishing
*Đáp án: B*
*Giải thích: Hàng ngàn máy tính bị nhiễm (zombies) đồng loạt gửi request làm máy chủ đích cạn kiệt tài nguyên (Băng thông, RAM, CPU).*

**Câu 193:** Chuẩn kết nối không dây tầm ngắn (khoảng 10m) thường dùng để kết nối chuột, bàn phím, tai nghe với máy tính là:
A. Wi-Fi 802.11ac
B. WiMAX 802.16
C. Bluetooth 802.15.1
D. LTE 4G
*Đáp án: C*
*Giải thích: Bluetooth là chuẩn PAN phổ biến nhất cho thiết bị ngoại vi.*

**Câu 194:** Độ dài tiêu chuẩn của một địa chỉ IPv4 là bao nhiêu bit?
A. 16 bit
B. 32 bit
C. 64 bit
D. 128 bit
*Đáp án: B*
*Giải thích: IPv4 sử dụng 32 bit (vd: 192.168.1.1), cung cấp khoảng 4.3 tỷ địa chỉ.*

**Câu 195:** Trong kiến trúc Client-Server, máy chủ Web (Web server) sử dụng giao thức HTTP ở cổng (Port) mặc định nào để chờ kết nối?
A. 21
B. 22
C. 25
D. 80
*Đáp án: D*
*Giải thích: Port 80 là port chuẩn cho HTTP. 21 (FTP), 22 (SSH), 25 (SMTP).*

**Câu 196:** "Giao thức không kết nối" (Connectionless) trong tầng mạng ám chỉ điều gì?
A. Không cần cắm cáp vật lý.
B. Gói tin được gửi đi ngay lập tức mà không cần thiết lập trước một "mạch ảo" hay bắt tay (handshake) thông báo trước với máy nhận.
C. Máy nhận không cần kết nối Internet.
D. Không thể kết nối quá 2 máy tính.
*Đáp án: B*
*Giải thích: Giao thức IP là connectionless (mỗi gói tin Datagram tự định vị đường đi độc lập và không báo trước). Trái ngược với Connection-oriented (như chuyển mạch kênh hay TCP).*

**Câu 197:** Cơ quan nào quản lý không gian địa chỉ IP và hệ thống tên miền cấp cao nhất trên toàn cầu?
A. Liên Hợp Quốc (UN)
B. ICANN (Internet Corporation for Assigned Names and Numbers)
C. Microsoft
D. IETF
*Đáp án: B*
*Giải thích: ICANN, và tổ chức con của nó là IANA (Internet Assigned Numbers Authority) quản lý các khối IP, Autonomous System Number (ASN) và Domain Root.*

**Câu 198:** Đặc tính "Khả năng mở rộng" (Scalability) của Internet được thiết kế dựa trên nguyên tắc nào?
A. Hệ thống có một máy chủ trung tâm cực mạnh điều khiển toàn bộ định tuyến.
B. Kiến trúc phân cấp (Hierarchical) và phân tán (Distributed) - như hệ thống ISP, hệ thống DNS.
C. Bắt buộc mọi máy tính dùng cùng một hệ điều hành.
D. Dùng mạng cáp đồng trục thay vì cáp quang.
*Đáp án: B*
*Giải thích: Mạng có thể to ra hàng tỷ thiết bị vì không có một trung tâm duy nhất nào làm "Nút thắt cổ chai". Tên miền, định tuyến, phân bổ IP đều theo hình cây phân cấp.*

**Câu 199:** Gói tin ở tầng Giao vận (Transport Layer) gọi là Segment. Khi gửi, tầng Transport sẽ gắn thêm thông tin gì vào Header để giúp HĐH đích phân phát dữ liệu cho đúng ứng dụng?
A. Địa chỉ IP
B. Số Port nguồn và Port đích (Source & Destination Port)
C. Địa chỉ MAC
D. URL của trang web
*Đáp án: B*
*Giải thích: Port (Ví dụ: Đích 80, Nguồn 53421) giúp hệ điều hành biết đẩy gói tin này cho tiến trình Trình duyệt (Chrome/Firefox).*

**Câu 200:** Điều gì sẽ xảy ra nếu cáp quang kết nối máy tính của bạn với Router Wi-Fi bị đứt ngầm?
A. Bạn không thể truy cập Internet nhưng vẫn in được qua máy in Wi-Fi (nếu Router và máy in không hỏng).
B. Tốc độ sẽ chậm đi một nửa.
C. Giao thức IP tự động nhảy sang sóng Wi-Fi (nếu máy tính không có card Wi-Fi).
D. Router sẽ bị cháy chập.
*Đáp án: A*
*Giải thích: Máy tính (PC) đứt dây LAN đến Router (LAN down). Các kết nối mạng nội bộ giữa PC và phần còn lại sẽ bị cắt đứt. Các thiết bị khác (như Laptop, Điện thoại) dùng sóng Wi-Fi kết nối vào Router vẫn hoạt động bình thường, và Router vẫn cấp mạng Internet cho chúng.*

**Câu 201:** Trong phân tầng mạng, mỗi tầng (Layer n) cung cấp dịch vụ cho tầng nào?
A. Tầng ngay bên trên nó (Layer n+1).
B. Tầng ngay bên dưới nó (Layer n-1).
C. Tất cả các tầng.
D. Tầng ngang hàng bên máy nhận.
*Đáp án: A*
*Giải thích: Tầng dưới (Network) truyền gói tin giúp tầng trên (Transport). Tầng trên (Transport) gọi dịch vụ của tầng dưới.*

**Câu 202:** Khi một file dung lượng 10MB được truyền từ máy A sang máy B qua giao thức TCP, file đó sẽ được:
A. Nén lại thành 1 gói tin 10MB duy nhất để gửi.
B. Gửi liên tục thành một dòng bit không đứt quãng.
C. Được tầng Giao vận chia nhỏ thành nhiều Segment, đóng gói, gắn số thứ tự (Sequence number) và gửi đi.
D. TCP sẽ bỏ qua file này nếu nó quá lớn.
*Đáp án: C*
*Giải thích: Để tránh chiếm kênh truyền quá lâu, và để dễ dàng truyền lại nếu có lỗi, dữ liệu lớn phải được chia nhỏ (Segmentation).*

**Câu 203:** Tốc độ đo đạc thực tế băng thông truyền hình ảnh của camera an ninh về trung tâm ghi hình (tính bằng Mbps) là đại lượng nào?
A. Băng thông giới hạn vật lý (Bandwidth)
B. Thông lượng (Throughput)
C. Trễ xử lý (Nodal delay)
D. Jitter
*Đáp án: B*
*Giải thích: Thông lượng (Throughput) là tốc độ mà dữ liệu payload hữu ích thực sự được chuyển tải thành công qua mạng tại một thời điểm đo lường.*

**Câu 204:** Sự kiện nào đánh dấu bước ngoặt đưa mạng ARPANET ra công chúng và dần trở thành Internet thương mại như ngày nay?
A. Sự ra đời của cáp quang biển.
B. Việc ngừng sử dụng giao thức TCP/IP.
C. Sự ra đời của World Wide Web (WWW) do Tim Berners-Lee phát minh vào đầu những năm 1990.
D. Việc phát minh ra điện thoại di động 5G.
*Đáp án: C*
*Giải thích: Web với giao thức HTTP, ngôn ngữ HTML và trình duyệt đồ họa đã biến Internet (trước đó chỉ dùng text/dòng lệnh cho học thuật/quân sự) thành công cụ dễ tiếp cận với đại chúng.*

**Câu 205:** Bảng định tuyến (Forwarding Table / Routing Table) trong Router lưu trữ thông tin gì để chuyển tiếp gói tin?
A. Danh sách các mật khẩu Wi-Fi xung quanh.
B. Ánh xạ (Map) giữa các dải địa chỉ IP đích và cổng giao diện ra tương ứng của Router (Outgoing interface).
C. Địa chỉ MAC của tất cả máy tính trên Internet toàn cầu.
D. Tên miền trang web và nội dung file HTML.
*Đáp án: B*
*Giải thích: Khi đọc IP đích (Ví dụ: 14.15.16.x), Router tra bảng xem IP này phải được đẩy ra cổng số mấy (Ví dụ: GigabitEthernet 0/1) để đến trạm kế tiếp gần đích nhất.*

**Câu 206:** Đâu là đặc điểm KHÔNG ĐÚNG về cáp quang đa mode (Multi-mode fiber)?
A. Sử dụng nguồn sáng LED hoặc Laser công suất thấp.
B. Lõi sợi quang có đường kính lớn hơn so với Single-mode (50 hoặc 62.5 micromet).
C. Có thể truyền tín hiệu đi xa hàng ngàn km không cần bộ khuếch đại (Repeater).
D. Xảy ra hiện tượng tán sắc (dispersion) do nhiều tia sáng truyền theo các góc khác nhau (mode).
*Đáp án: C*
*Giải thích: Cáp quang Multi-mode chỉ dùng cho khoảng cách ngắn (thường < 2km, dùng trong các toà nhà hoặc Data Center) do hiện tượng tán sắc mode làm tín hiệu nhòe dần theo khoảng cách.*

**Câu 207:** Việc phân mảnh gói tin IP (IP Fragmentation) ở mạng IPv4 có thể xảy ra ở đâu?
A. Chỉ ở thiết bị nguồn.
B. Chỉ ở thiết bị đích.
C. Ở thiết bị nguồn hoặc ở bất kỳ Router nào dọc đường nếu kích thước gói (Datagram) vượt quá MTU của liên kết tiếp theo.
D. IP không hỗ trợ phân mảnh gói.
*Đáp án: C*
*Giải thích: Trái ngược với IPv6 (chỉ phân mảnh ở nguồn), Router IPv4 khi nhận một gói IP 1500 bytes mà đường link out chỉ hỗ trợ 500 bytes (MTU), nó sẽ băm gói 1500 bytes thành 3 mảnh nhỏ (Fragments).*

**Câu 208:** Giao thức nào cung cấp chức năng "Dịch vụ thư mục" (Directory Service) trong mạng cục bộ của doanh nghiệp (VD: quản lý tài khoản nhân viên, máy tính)?
A. DHCP
B. DNS
C. LDAP / Active Directory
D. FTP
*Đáp án: C*
*Giải thích: LDAP (Lightweight Directory Access Protocol) quản lý người dùng, nhóm, cấp quyền (ví dụ Windows Server Active Directory).*

**Câu 209:** Tốc độ truyền (Transmission rate) của một liên kết phụ thuộc vào:
A. Tốc độ ánh sáng trong chân không.
B. Năng lực phần cứng (chip xử lý tín hiệu) của bộ thu/phát và cấu trúc vật lý của dây cáp (băng thông).
C. Chiều dài thực tế của dây cáp dài bao nhiêu km.
D. Dung lượng RAM của thiết bị gửi.
*Đáp án: B*
*Giải thích: "Băng thông ống nước" to hay nhỏ phụ thuộc vào Card mạng (1Gbps hay 10Gbps) và sợi cáp hỗ trợ (Cat5e hay Cat6a).*

**Câu 210:** Tại sao trong kiến trúc mạng ngang hàng (P2P), sự "Churn" (Sự biến động tham gia/rời bỏ của các máy khách) là một thách thức lớn?
A. Vì nó gây mất điện máy chủ.
B. Vì người dùng (peers) có thể ngắt kết nối Internet bất cứ lúc nào, làm mất các phần tệp tin mà họ đang chia sẻ cho người khác.
C. Vì router không định tuyến được P2P.
D. Vì P2P bắt buộc dùng địa chỉ MAC động.
*Đáp án: B*
*Giải thích: Tính ổn định của P2P phụ thuộc hoàn toàn vào máy khách. Nếu các máy "Seed" tắt nguồn hết, những người đang tải dở sẽ không lấy được mảnh dữ liệu còn thiếu.*

**Câu 211:** "Checksum" trong các Header (IPv4, TCP, UDP) dùng để làm gì?
A. Mã hoá toàn bộ mật khẩu người dùng.
B. Xác minh độ ưu tiên (QoS) của gói tin.
C. Kiểm tra xem các bit trong Header (và đôi khi là payload) có bị biến đổi sai lệch trong quá trình truyền qua đường vật lý hay không.
D. Định danh máy chủ.
*Đáp án: C*
*Giải thích: Checksum là kỹ thuật băm/tính toán đơn giản (Cộng bù 1) các từ 16-bit. Máy thu sẽ tính lại và so sánh với Checksum máy phát gửi; nếu sai -> bit bị lật (nhiễu).*

**Câu 212:** Một trong các nguyên tắc thiết kế quan trọng của mạng Internet là nguyên lý End-to-End (E2E argument). Nguyên lý này phát biểu điều gì?
A. Bộ định tuyến mạng lõi phải kiểm tra và loại bỏ virus.
B. Mọi máy tính trên mạng đều phải là Router.
C. Các tính năng phức tạp (như độ tin cậy, bảo mật) nên được đặt ở các hệ thống đầu cuối (End-systems/Hosts), giữ cho mạng lõi (routers) đơn giản, nhanh và vô trạng thái (stateless).
D. Phải dùng cáp điểm-điểm (End-to-End cable) nối thẳng 2 máy với nhau.
*Đáp án: C*
*Giải thích: Triết lý "Dumb Network, Smart Terminals": Mạng chỉ lo "đẩy cục gạch", máy tính/điện thoại ở hai đầu tự lo kiểm lỗi, bảo mật, mã hóa. Điều này làm Internet rẻ, dễ mở rộng, router không bị quá tải bộ nhớ.*

**Câu 213:** Thuật ngữ "ISP Transit" ám chỉ việc:
A. Các ISP cấp thấp trả tiền cho ISP cấp cao hơn để lưu lượng mạng của họ được định tuyến đi vào phần còn lại của Internet toàn cầu.
B. ISP cấp 1 trả tiền cho ISP cấp 2.
C. Việc truyền tải file qua giao thức FTP.
D. Thay thế cáp đồng bằng cáp quang biển.
*Đáp án: A*
*Giải thích: Transit là quan hệ mua bán (Nhà phân phối bán sỉ cho Cửa hàng lẻ). Peering là quan hệ đổi chác ngang hàng không tốn phí.*

**Câu 214:** Cơ chế "Piggybacking" (Cõng/Quá giang) trong giao thức TCP là gì?
A. TCP mang theo virus.
B. Bản tin phản hồi ACK được "cõng" (ghép chung) vào gói tin chứa Dữ liệu (Data) gửi theo chiều ngược lại, thay vì gửi một gói ACK riêng rẽ trống rỗng để tiết kiệm băng thông.
C. Đóng gói UDP vào TCP.
D. Hai máy tính dùng chung 1 IP.
*Đáp án: B*
*Giải thích: Thay vì: B -> A: [Đây là ACK cho gói 1], rồi B -> A: [Đây là Data gói 2]. B sẽ gom: B -> A: [Data gói 2 + Tiện thể ACK luôn gói 1]*

**Câu 215:** Trong mạng Wi-Fi bảo mật, giao thức nào hiện đang là tiêu chuẩn mã hóa an toàn nhất (tính đến thập niên 2020)?
A. WEP
B. WPA (TKIP)
C. WPA2
D. WPA3
*Đáp án: D*
*Giải thích: WPA3 (ra mắt 2018) cung cấp các thuật toán mã hoá mạnh mẽ hơn (bảo vệ chống brute-force) thay thế cho WPA2.*

**Câu 216:** Một hệ thống mạng cục bộ ảo (VLAN) thực hiện chức năng gì trên Switch?
A. Thay thế hoàn toàn Router bằng Switch.
B. Phát Wi-Fi từ Switch cáp đồng.
C. Phân tách logic (mềm) một Switch vật lý thành nhiều Switch ảo, phân lập các Broadcast domain (miền quảng bá) độc lập ngay cả khi chúng cắm chung trên 1 thiết bị.
D. Biến đổi tốc độ port 100Mbps thành 1Gbps.
*Đáp án: C*
*Giải thích: VLAN giúp nhóm các nhân viên phòng Kế toán vào VLAN 10, phòng IT vào VLAN 20 trên cùng 1 Switch. Broadcast của VLAN 10 không lan sang VLAN 20, tăng cường an ninh và giảm rác mạng.*

**Câu 217:** Trạm trinh sát (Honeypot) trong an ninh mạng được dùng để làm gì?
A. Đo kiểm tra tốc độ download web.
B. Một hệ thống giả mạo được cố tình cấu hình nhiều lỗ hổng để "thu hút" hacker tấn công, nhằm ghi nhận phương thức, công cụ, hoặc đánh lạc hướng chúng khỏi máy chủ thực sự.
C. Nén dữ liệu truyền thông.
D. Bẻ khóa mật khẩu Wi-Fi.
*Đáp án: B*
*Giải thích: Honeypot (Hũ mật) là bẫy giăng ra. Hacker chui vào tấn công tưởng vớ bở, nhưng thực ra mọi thao tác đang bị quản trị viên mạng theo dõi.*

**Câu 218:** Theo mô hình tham chiếu OSI, "Đóng gói" dữ liệu (Encapsulation) thực chất là thao tác:
A. Mã hóa nội dung dữ liệu thành các ký tự không đọc được (Encryption).
B. Thêm một phần thông tin điều khiển (Header / Trailer) đặc thù của tầng tương ứng vào dữ liệu được nhận từ tầng trên.
C. Giải nén file Zip.
D. Ghép nhiều luồng dữ liệu vào một kênh truyền chung.
*Đáp án: B*
*Giải thích: Tưởng tượng như gửi thư: Viết thư (Application data) -> Bỏ vào phong bì ghi người nhận (TCP Header) -> Bỏ vào túi đựng thư của bưu điện (IP Header) -> Bỏ lên thùng xe tải (Frame).*

**Câu 219:** Hiện tượng "Broadband over Power Lines" (BPL - Truyền mạng qua đường điện) dùng để:
A. Tăng điện áp để cháy máy của hacker.
B. Gửi tín hiệu mạng tần số cao chạy đè lên đường dây điện lưới (tần số 50/60Hz), biến ổ cắm điện trong nhà thành cổng kết nối mạng (PLC - Power Line Communication).
C. Tránh bị sét đánh.
D. Thay pin cho Laptop từ xa.
*Đáp án: B*
*Giải thích: Công nghệ này (như HomePlug AV) giúp nhà không đi sẵn cáp LAN vẫn có mạng dây từ phòng này sang phòng khác thông qua ổ cắm điện âm tường.*

**Câu 220:** Đâu là đặc trưng cơ bản phân biệt "Network" (tầng Mạng) và "Data Link" (tầng Liên kết) trong việc định tuyến gói tin?
A. Network chuyển gói tin giữa 2 máy tính nằm trên 2 mạng (Subnet) khác nhau; Data Link chuyển gói tin giữa 2 thiết bị kề nhau trong CÙNG một mạng (cùng Subnet/Segment).
B. Network dùng tốc độ nhanh hơn Data link.
C. Network truyền qua vệ tinh, Data Link truyền qua cáp.
D. Không có khác biệt nào.
*Đáp án: A*
*Giải thích: Network giải quyết bài toán Toàn cầu (Đi từ VN sang Mỹ). Data link giải quyết bài toán Cục bộ (Đi từ Router VNPT nhà bạn ra cái trạm BTS của khu phố).*

**Câu 221:** Phương thức truyền nào sau đây KHÔNG đảm bảo gói tin sẽ đến nơi?
A. TCP (Transmission Control Protocol)
B. UDP (User Datagram Protocol)
C. HDLC
D. IPsec
*Đáp án: B*
*Giải thích: UDP là giao thức "best-effort" (cố gắng hết sức). Nó ném gói tin lên mạng và quên đi, không cần biết (hay chờ ACK) gói tin đó rớt hay sống.*

**Câu 222:** Để truy cập một máy chủ ở xa và điều khiển nó qua giao diện dòng lệnh bằng giao thức mã hóa an toàn, giao thức nào thường được sử dụng thay thế cho Telnet?
A. FTP
B. SSH (Secure Shell)
C. SMTP
D. ICMP
*Đáp án: B*
*Giải thích: Telnet gửi mật khẩu dưới dạng văn bản gốc (clear-text) nên dễ bị Sniffing. SSH mã hóa toàn bộ phiên làm việc bằng khóa mật mã (public key cryptography).*

**Câu 223:** Lệnh `tracert` (trên Windows) / `traceroute` (trên Linux/Mac) hoạt động bằng cách thay đổi liên tục giá trị của trường nào trong IP Header?
A. TTL (Time to Live)
B. Source IP
C. Checksum
D. Protocol Type
*Đáp án: A*
*Giải thích: Tracert gửi gói 1 với TTL=1, Router 1 trừ đi 1 (còn 0) sẽ drop gói và gửi lỗi về (ICMP Time Exceeded) -> ta biết được IP Router 1. Sau đó gửi gói 2 với TTL=2 để khám phá Router 2...*

**Câu 224:** "Mạng biên" (Network Edge) trong cấu trúc liên kết mạng bao gồm:
A. Cáp quang dưới đáy đại dương.
B. Các hệ thống đầu cuối (máy tính, server, điện thoại) và các thiết bị thu phát cục bộ (modem, router Wi-Fi nhà).
C. Các Router công suất lớn kết nối giữa quốc gia này với quốc gia khác.
D. Các vệ tinh địa tĩnh.
*Đáp án: B*
*Giải thích: Edge (Rìa/Biên) là nơi người dùng và ứng dụng ngự trị. Core (Lõi) là các router liên kết khổng lồ làm nhiệm vụ vận chuyển hàng hóa trên đường cao tốc.*

**Câu 225:** Chức năng chính của Cổng thông tin (Gateway) là gì?
A. Chỉ khuếch đại điện áp của cáp UTP.
B. Nó là một điểm nút mạng (Node) đóng vai trò là "Cửa ngõ" kết nối hai mạng có kiến trúc, giao thức khác nhau (ví dụ từ LAN ra WAN Internet, hoặc từ IP sang mạng điện thoại truyền thống PSTN).
C. Lọc quảng cáo web.
D. Gửi gói tin ngược lại nguồn.
*Đáp án: B*
*Giải thích: Ví dụ: Router gia đình chính là một Default Gateway. Nó vừa định tuyến (routing), biên dịch IP (NAT) để làm trung gian giữa mạng LAN riêng và Internet công cộng.*

**Câu 226:** Khái niệm "Datagram" dùng để chỉ đơn vị gói tin của tầng nào trong kiến trúc TCP/IP?
A. Application
B. Transport
C. Network (Internet Layer)
D. Physical
*Đáp án: C*
*Giải thích: IP Datagram (hoặc IP Packet) là đơn vị đóng gói của tầng Mạng, bao gồm IP Header + Payload.*

**Câu 227:** Tại sao mạng Internet thiết kế theo cấu trúc (topology) phi tập trung (tựa như mạng nhện lưới) thay vì hình sao tập trung (một Hub trung tâm duy nhất trên thế giới)?
A. Vì chi phí dây dẫn cho hình sao đắt hơn.
B. Tăng tính sống còn (Survivability) của hệ thống. Nếu một hoặc một cụm router/liên kết bị đánh sập (như trong chiến tranh), mạng vẫn tìm được đường vòng qua vùng đứt gãy.
C. Để tăng tốc độ xử lý gói tin.
D. Vì không có quốc gia nào muốn máy chủ đặt ở nước khác.
*Đáp án: B*
*Giải thích: Thiết kế phi tập trung (Decentralized) do DARPA của quân đội Mỹ nghiên cứu (ARPANET) nhằm đảm bảo thông tin liên lạc không bao giờ bị cắt đứt khi mất một trạm.*

**Câu 228:** "Cookie" trên trình duyệt Web (tầng Application) nhằm giải quyết vấn đề cốt lõi gì của giao thức HTTP?
A. Bảo vệ mật khẩu khỏi Hacker.
B. Hỗ trợ TCP mã hóa luồng dữ liệu.
C. Giải quyết tính chất Vô trạng thái (Stateless) của HTTP, giúp Web Server "nhớ" thông tin, trạng thái người dùng (ví dụ: đã đăng nhập, giỏ hàng) qua nhiều lần Request liên tiếp.
D. Lưu trữ file ảnh và video để xem offline.
*Đáp án: C*
*Giải thích: HTTP là stateless (Mỗi Request đứng độc lập, server trả lời xong là "quên" bạn ngay). Nhờ Browser gửi kèm cái mã Cookie trong mỗi Request sau đó, Server mới nhận ra "À, đây là ông khách lúc nãy đã bỏ món A vào giỏ".*

**Câu 229:** Kỹ thuật ghép kênh theo bước sóng quang (WDM - Wavelength Division Multiplexing) hoạt động dựa trên nguyên lý gì?
A. Cắt ánh sáng thành các xung chớp tắt rất nhanh.
B. Truyền đồng thời nhiều chùm tia sáng có màu sắc (bước sóng) khác nhau qua CÙNG MỘT sợi cáp quang, mỗi bước sóng mang một kênh dữ liệu riêng biệt.
C. Chuyển ánh sáng thành tín hiệu siêu âm.
D. Nén dữ liệu video ở tầng Application.
*Đáp án: B*
*Giải thích: Tương tự như FDM ở vô tuyến điện. WDM cho phép 1 sợi cáp quang nhỏ bằng sợi tóc có thể truyền hàng trăm kênh Gbps cùng lúc bằng cách dùng các màu sáng khác nhau (hồng ngoại).*

**Câu 230:** Các thông điệp thông báo lỗi hoặc tình trạng mạng như "Destination Unreachable" (Đích đến không thể chạm tới) được định nghĩa và truyền đi bởi giao thức nào đi kèm cùng tầng với IP?
A. UDP
B. ARP
C. ICMP (Internet Control Message Protocol)
D. HTTP
*Đáp án: C*
*Giải thích: ICMP (Tầng Network) là cơ chế báo cáo lỗi của Internet. Khi Router không tìm được đường hoặc TTL = 0, nó gửi thông điệp ICMP trả về nguồn.*

**Câu 231:** Theo thuật ngữ mạng, khi một hệ thống cuối (End system) được trang bị nhiều card mạng (Network Interface Card) để kết nối vật lý với nhiều đường truyền (link) khác nhau, nó được gọi là máy chủ gì?
A. Máy chủ DNS
B. Máy chủ Multihomed
C. Máy chủ Cloud
D. Máy chủ P2P
*Đáp án: B*
*Giải thích: Multihomed là khái niệm khi 1 thiết bị/hệ thống có ít nhất 2 IP gán vào 2 interface kết nối ra 2 đường mạng khác nhau (để cân bằng tải hoặc dự phòng).*

**Câu 232:** Trong mạng chuyển mạch gói (Packet Switching), việc xác định tuyến đường (Routing) thường được thực hiện theo:
A. Từng gói tin (Per-packet), gói trước đi đường A, gói sau có thể đi đường B nếu bảng định tuyến cập nhật do tắc nghẽn.
B. Cố định cho toàn bộ một phiên kết nối từ đầu đến cuối.
C. Mọi gói tin luôn đi theo đường cáp quang, tránh dùng cáp đồng.
D. Định tuyến ngẫu nhiên (Random).
*Đáp án: A*
*Giải thích: Đây là tính chất của mạng Datagram (như IP Internet). Các gói tin độc lập (không cần mạch ảo tĩnh) nên nếu có sự cố trên đường đi, router sẽ linh hoạt bẻ nhánh các gói đến sau đi đường khác.*

**Câu 233:** Trong kỹ thuật mạng di động 4G LTE/5G, phần lõi mạng kết nối các trạm phát sóng (eNodeB / gNodeB) về Internet được gọi tên là gì?
A. Edge Network
B. Evolved Packet Core (EPC) hoặc 5G Core (5GC)
C. Radio Access Network (RAN)
D. Cloud Computing Network
*Đáp án: B*
*Giải thích: RAN (Mạng truy cập vô tuyến) là phần từ điện thoại đến trạm phát. EPC/5GC (Mạng lõi) lo việc xác thực SIM, định tuyến IP, cấp IP và kết nối trạm ra Internet vĩ mô.*

**Câu 234:** Hành vi "Nghe lén" (Sniffing) dữ liệu nếu được thực hiện bằng cách chia sẻ chung một Switch thì sẽ gặp khó khăn gì so với dùng Hub?
A. Không có sự khác biệt.
B. Switch luôn mã hóa dữ liệu.
C. Switch thực hiện chuyển mạch thông minh (unicast) từ cổng nguồn thẳng đến cổng đích, do đó cổng của kẻ nghe lén không nhận được các Frame của người khác (khác với Hub luôn Broadcast rác ra mọi cổng).
D. Switch ngăn chặn cài đặt phần mềm sniffer.
*Đáp án: C*
*Giải thích: Hub truyền tín hiệu theo dạng Bus ảo (Broadcast), ai cắm vào Hub cũng nghe được. Switch cách ly vùng đụng độ (Collision domain) nên an toàn hơn, muốn sniff Switch thường phải cấu hình Port Mirroring hoặc dùng kỹ thuật tấn công ARP Spoofing.*

**Câu 235:** Tại sao thuật toán định tuyến trong mạng thường cố gắng tìm đường đi "ngắn nhất" (Shortest path)?
A. Để tiết kiệm chi phí cáp mạng.
B. Để giảm thiểu thời gian trễ (delay) từ điểm nguồn đến đích, tính bằng số hop (trạm trung chuyển) hoặc thông số chi phí (cost) của các liên kết.
C. Để tăng số lượng gói tin đi qua.
D. Để bảo mật tốt hơn.
*Đáp án: B*
*Giải thích: Định tuyến tìm đường ngắn nhất (như Dijkstra OSPF) giúp tiết kiệm tài nguyên mạng, giảm độ trễ và giảm tải cho các liên kết không cần thiết.*

**Câu 236:** Kẻ tấn công gửi một lượng lớn gói tin yêu cầu cấp IP đến máy chủ DHCP nội bộ nhằm làm máy chủ hết sạch quỹ IP cấp cho người dùng hợp lệ. Tấn công này gọi là gì?
A. DHCP Starvation (Làm cạn kiệt DHCP)
B. ARP Spoofing
C. Phishing
D. Man in the Middle
*Đáp án: A*
*Giải thích: Bằng cách giả lập hàng ngàn địa chỉ MAC giả (MAC flooding), hacker xin sạch các IP trong Pool (Hồ chứa IP) của máy chủ DHCP, dẫn đến tình trạng từ chối dịch vụ cho các thiết bị mới cắm vào.*

**Câu 237:** Loại phương tiện truyền dẫn vật lý nào sử dụng cơ chế phản xạ toàn phần (Total Internal Reflection) để dẫn tín hiệu?
A. Cáp đồng xoắn đôi
B. Sóng cực ngắn
C. Cáp quang (Optical fiber)
D. Cáp đồng trục
*Đáp án: C*
*Giải thích: Tia sáng chiếu vào lõi cáp quang (Core) ở một góc độ nhỏ hơn góc giới hạn, nó sẽ đập vào lớp vỏ phản xạ (Cladding) và bật ngược lại vào trong, liên tục zic-zắc tiến tới.*

**Câu 238:** Địa chỉ IP Private (IP nội bộ) khác với IP Public (IP công cộng) như thế nào về khả năng định tuyến?
A. IP Private không thể được cấp phát.
B. IP Private được phép tự do xuất hiện và định tuyến chuyển tiếp qua các Router lõi trên mạng Internet công cộng toàn cầu.
C. IP Private KHÔNG thể được định tuyến trên mạng Internet công cộng; các Router biên (nhà cung cấp) mặc định sẽ loại bỏ gói tin nào có IP đích là IP Private nằm ngoài mạng đó.
D. Không có khác biệt.
*Đáp án: C*
*Giải thích: IP Private (Ví dụ 10.x.x.x, 192.168.x.x) được dùng lặp đi lặp lại miễn phí ở hàng triệu mạng LAN gia đình. Muốn ra Internet, chúng BẮT BUỘC phải đi qua bộ chuyển đổi NAT thành IP Public.*

**Câu 239:** Khi bạn nhập www.facebook.com vào thanh địa chỉ nhưng máy báo "DNS server is not responding", lỗi này có nghĩa là gì?
A. Cáp mạng bị rút ra.
B. Máy chủ DNS không phản hồi yêu cầu dịch tên miền www.facebook.com sang địa chỉ IP, do đó trình duyệt không biết IP nào để kết nối tới máy chủ Facebook.
C. Facebook đã chặn IP máy tính của bạn.
D. Facebook bị sập.
*Đáp án: B*
*Giải thích: Dù mạng vật lý (cáp, Wi-Fi) vẫn tốt, mạng Internet (ping ra IP public) vẫn sống, nhưng Dịch vụ phân giải tên bị lỗi, bạn chỉ có thể truy cập Web nếu nhớ trực tiếp IP của chúng.*

**Câu 240:** Khái niệm Tầng 1 (Physical Layer) liên quan đến yếu tố nào dưới đây?
A. HTTP
B. Địa chỉ IP
C. Điện áp tĩnh, tín hiệu điện/quang học, tần số sóng, cấu trúc cáp vật lý.
D. MAC Address
*Đáp án: C*
*Giải thích: Tầng 1 quản lý phần cứng cơ bản nhất, định nghĩa cách 1 bit '0' hoặc '1' được mã hoá thành xung điện (bao nhiêu volt), sóng điện từ hay chớp sáng.*

**Câu 241:** Tầng (Layer) cao nhất trong cả 2 mô hình OSI và TCP/IP giao tiếp trực tiếp với người sử dụng mạng là tầng nào?
A. Network Layer
B. Physical Layer
C. Application Layer (Tầng Ứng dụng)
D. Transport Layer
*Đáp án: C*
*Giải thích: Tầng ứng dụng gồm các phần mềm mà người dùng thao tác trực tiếp trên màn hình: Web Browser (HTTP), Email App (SMTP), Game online...*

**Câu 242:** "Anycast" là kiểu gửi thông điệp mạng có tính chất gì?
A. Gửi cho tất cả mọi thiết bị (Broadcast).
B. Gửi từ 1 thiết bị cho 1 thiết bị duy nhất (Unicast).
C. Gửi từ 1 thiết bị đến cho node GẦN NHẤT (về mặt khoảng cách định tuyến) trong một nhóm các máy chủ có cùng chia sẻ chung 1 địa chỉ IP Anycast.
D. Không phải khái niệm của mạng máy tính.
*Đáp án: C*
*Giải thích: BGP Anycast thường dùng cho DNS Root server (VD: 8.8.8.8). Nhiều Server Google trên thế giới dùng chung IP 8.8.8.8, truy vấn từ VN sẽ tự động được đưa đến Server 8.8.8.8 ở VN hoặc Sing do định tuyến tìm đường ngắn nhất.*

**Câu 243:** Tại sao các router đôi khi được gọi là các thiết bị Tầng 3 (Layer-3 devices)?
A. Vì chúng dùng chuẩn cáp Cat3.
B. Vì chúng hoạt động lên tới Tầng 3 (Network Layer) để kiểm tra các trường Header của IP Datagram (ví dụ IP đích) để ra quyết định định tuyến.
C. Vì chúng chỉ kết nối được 3 máy tính.
D. Vì chúng không thể thực hiện chức năng vật lý.
*Đáp án: B*
*Giải thích: Switch L2 xem MAC, Router L3 xem IP để chuyển tiếp dữ liệu.*

**Câu 244:** Băng thông rộng bất đối xứng ADSL (Asymmetric Digital Subscriber Line) sử dụng môi trường vật lý nào để cung cấp Internet?
A. Cáp quang.
B. Đường dây điện thoại đồng (Twisted-pair copper telephone line) đang có sẵn.
C. Sóng điện thoại di động.
D. Cáp đồng trục truyền hình.
*Đáp án: B*
*Giải thích: ADSL tận dụng dây đồng điện thoại cũ, sử dụng các dải tần số cao hơn tần số giọng nói (Voice) để tải dữ liệu, tiết kiệm chi phí triển khai cáp mới.*

**Câu 245:** Công nghệ Wi-Fi tại nhà (Ví dụ: IEEE 802.11 b/g/n) hoạt động trên các băng tần phổ biến nào?
A. 100 MHz
B. 900 MHz
C. Băng tần công nghiệp ISM không cần xin cấp phép, phổ biến là 2.4 GHz và 5 GHz.
D. Ánh sáng nhìn thấy.
*Đáp án: C*
*Giải thích: Băng tần 2.4 GHz có khả năng xuyên tường tốt hơn nhưng dễ bị nhiễu do trùng sóng Bluetooth, lò vi sóng. Băng tần 5 GHz nhanh hơn, ít nhiễu nhưng vùng phủ sóng hẹp hơn.*

**Câu 246:** Sự khác biệt giữa mạng LAN (Local Area Network) và VLAN (Virtual LAN) là gì?
A. LAN sử dụng Switch, VLAN sử dụng Router.
B. LAN sử dụng cáp đồng, VLAN sử dụng Wi-Fi.
C. LAN dựa trên vị trí kết nối vật lý (cắm vào cùng 1 Switch). VLAN là sự phân tách logic, có thể nhóm các cổng trên nhiều Switch vật lý khác nhau thành một mạng nội bộ chung.
D. Không có khác biệt thực sự.
*Đáp án: C*
*Giải thích: VLAN hoạt động dựa trên việc gắn thẻ (Tagging - IEEE 802.1q) vào Frame ở Switch, giúp mạng cục bộ cực kỳ mềm dẻo về mặt quản lý mà không phụ thuộc thiết kế đi dây cáp điện.*

**Câu 247:** Điểm khác biệt mấu chốt giữa tín hiệu Tương tự (Analog) và tín hiệu Số (Digital) khi truyền tải dữ liệu?
A. Analog chỉ truyền được giọng nói, Digital chỉ truyền được văn bản.
B. Analog là các làn sóng điện từ/âm thanh có biên độ biến thiên liên tục vô hạn; Digital là chuỗi các xung rời rạc, mức điện áp chỉ mang giá trị 0 hoặc 1 rõ ràng, dễ chống nhiễu và dễ sửa lỗi hơn.
C. Analog truyền qua cáp, Digital truyền qua không khí.
D. Digital chậm hơn rất nhiều so với Analog.
*Đáp án: B*
*Giải thích: Tín hiệu Digital cho khả năng khôi phục lại bit 1 nếu tín hiệu bị nhiễu giảm điện áp một chút (từ 5V rớt xuống 4.5V thì máy tính vẫn hiểu là bit 1).*

**Câu 248:** Giao thức HTTP/1.1 (thường dùng trong web) sử dụng kết nối TCP liên tục (Persistent Connection) có lợi thế gì?
A. Ngăn cản Virus xâm nhập qua port 80.
B. Tránh phải thực hiện quá trình bắt tay TCP 3 bước (3-way handshake) mất thời gian cho MỖI bức ảnh nhỏ trên cùng một trang web; dùng lại kết nối cũ cho nhiều file gửi nối tiếp.
C. Chuyển đổi TCP thành UDP.
D. Mã hóa nội dung trang web.
*Đáp án: B*
*Giải thích: Mở kết nối TCP (handshake) mất ít nhất 1 RTT (Round Trip Time). Persistent Connection giữ kết nối TCP mở một lúc sau khi tải xong HTML để tải tiếp CSS/JS/Images mà không mất thêm RTT thiết lập lại TCP.*

**Câu 249:** Thông lượng truyền qua mạng di động (3G/4G) của người dùng sẽ bị giảm sút nghiêm trọng nếu:
A. Thiết bị đang ở quá xa trạm thu phát sóng (BTS), cường độ tín hiệu (Signal-to-Noise Ratio) giảm, tỷ lệ lỗi bit (BER) tăng.
B. Nằm yên một chỗ (không di chuyển).
C. Tắt kết nối Wi-Fi.
D. Đặt máy tính lên bàn kính.
*Đáp án: A*
*Giải thích: Giao thức mạng vô tuyến (MAC layer) thường tự động giảm tốc độ truyền (dùng kiểu điều chế thấp hơn) hoặc phải gửi lại frame liên tục khi sóng yếu và nhiễu (noise) lấn át sóng chính.*

**Câu 250:** Cuối cùng, mục đích tối thượng của mọi công nghệ kết nối Mạng máy tính là gì?
A. Bán được nhiều thiết bị phần cứng cáp quang và Router.
B. Nâng cao xung nhịp CPU của máy tính.
C. Cung cấp môi trường truyền dẫn thông tin (bit) để phục vụ việc giao tiếp, trao đổi dữ liệu cho các ỨNG DỤNG của người dùng cuối một cách nhanh, an toàn, và đáng tin cậy nhất.
D. Phát triển trí tuệ nhân tạo.
*Đáp án: C*
*Giải thích: Hệ thống viễn thông và máy tính sinh ra là để phục vụ lớp Ứng dụng (Application), lớp tương tác trực tiếp với con người (như nhắn tin, video call, chuyển khoản ngân hàng).*
