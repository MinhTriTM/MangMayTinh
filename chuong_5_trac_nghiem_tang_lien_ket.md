# CHƯƠNG 5: TRẮC NGHIỆM TẦNG LIÊN KẾT (DATA LINK LAYER) VÀ LAN

**Câu 1:** Đơn vị dữ liệu (PDU) của Tầng Liên kết (Data Link Layer) được gọi là gì?
A. Datagram
B. Segment
C. Frame (Khung)
D. Message
*Đáp án: C*
*Giải thích: Đơn vị ở tầng Liên kết là Khung. Khung này chứa Payload là IP Datagram từ tầng Mạng chuyển xuống.*

**Câu 2:** Tầng Liên kết thường được thực thi và xử lý hoàn toàn bởi bộ phận cứng nào trên máy tính?
A. Ổ cứng HDD
B. Cạc mạng (Network Interface Card - NIC) hoặc Chipset mạng.
C. Bàn phím
D. Card đồ họa (VGA)
*Đáp án: B*
*Giải thích: Do tính chất tốc độ cực cao, việc đóng khung, tính toán mã lỗi CRC, dò tìm xung đột mạng được "đúc cứng" vào mạch chip của NIC thay vì chạy trên CPU phần mềm.*

**Câu 3:** Kỹ thuật phát hiện lỗi bằng "Mã kiểm tra chẵn lẻ hai chiều" (Two-dimensional parity) có tính năng ưu việt gì so với chẵn lẻ một chiều?
A. Tiết kiệm dung lượng gói tin hơn.
B. Không những phát hiện được có lỗi, mà còn chỉ ra tọa độ CHÍNH XÁC của 1 bit bị lỗi để phần cứng có thể tự động LẬT NGƯỢC bit đó (Tự Sửa Lỗi - FEC).
C. Có thể phát hiện và sửa được 100 bit lỗi liên tiếp.
D. Có khả năng mã hóa dữ liệu thành văn bản bí mật.
*Đáp án: B*
*Giải thích: Xếp bit thành ma trận (hàng ngang, cột dọc). Giao điểm của hàng báo lỗi và cột báo lỗi chính là vị trí của cái bit bị lật. Máy nhận tự sửa mà không cần báo gửi lại.*

**Câu 4:** Khi hệ thống tính toán mã CRC (Cyclic Redundancy Check) ở tầng Liên kết, dữ liệu được nhìn nhận dưới con mắt toán học như thế nào?
A. Một ma trận chữ số.
B. Một phương trình vi phân.
C. Một đa thức nhị phân (Binary Polynomial).
D. Một con số Hexadecimal.
*Đáp án: C*
*Giải thích: Các bit dữ liệu (vd: 1011) được coi là hệ số của đa thức (x^3 + x + 1). Gói tin chia cho đa thức sinh G, phần dư D là mã CRC.*

**Câu 5:** Hiện tượng "Xung đột" (Collision) trong một mạng cục bộ (LAN) mang ý nghĩa vật lý là gì?
A. Tường lửa chặn gói tin.
B. Router không biết đường đi.
C. Khi hai hay nhiều máy tính CÙNG phát tín hiệu năng lượng (sóng vô tuyến hoặc điện áp) vào CÙNG một môi trường truyền thông dùng chung (Shared medium), làm cho các tín hiệu điện từ hòa trộn, bóp méo và triệt tiêu nhau.
D. Khi máy tính cắm nhầm dây nguồn.
*Đáp án: C*
*Giải thích: Trong cáp đồng trục cũ hoặc sóng Wi-Fi, hai máy nói cùng lúc thì tín hiệu dội vào nhau thành đống nhiễu loạn.*

**Câu 6:** CSMA/CD (Carrier Sense Multiple Access with Collision Detection) là giao thức nổi tiếng giải quyết đa truy cập. Cụm từ "Collision Detection" đóng vai trò tiết kiệm băng thông như thế nào?
A. Tránh va chạm xảy ra.
B. Thiết bị trong khi đang phát sẽ dò mức điện áp của dây cáp. Nếu vọt lên, nó biết là có đụng độ. Nó HỦY ngay việc phát nốt các bit còn lại của khung (tránh phí thời gian) và báo tín hiệu nhiễu để mọi người đều ngưng.
C. Giới hạn số lượng máy tính kết nối vào LAN.
D. Xóa bộ nhớ đệm của Switch.
*Đáp án: B*
*Giải thích: Ethernet rất nhạy, đang nói mà thấy có tiếng hét của đứa khác là cúp miệng luôn, không bướng bỉnh nói đến cùng.*

**Câu 7:** Sau khi phát hiện đụng độ (Collision) bằng CSMA/CD, máy tính phải chờ bao lâu trước khi cố gắng thử gửi lại?
A. Chờ 1 giây.
B. Chờ 1 mili-giây.
C. Áp dụng thuật toán "Lùi lại ngẫu nhiên nhị phân" (Binary Exponential Backoff): Lấy ngẫu nhiên số lần trễ trong khoảng mốc rộng dần (từ 0 đến 2^n - 1) với n là số lần đụng độ liên tiếp.
D. Lập tức gửi lại không cần chờ.
*Đáp án: C*
*Giải thích: Đụng 1 lần, chờ từ {0, 1} slot. Đụng 2 lần, chờ từ {0, 1, 2, 3}. Đụng càng nhiều mạng càng nghẽn, thời gian chờ càng phải dàn đều để giảm nhiệt.*

**Câu 8:** Các giao thức như "Polling" (Hỏi dò vòng quanh từ Master) hoặc "Token Passing" (Truyền thẻ bài) thuộc nhóm giải pháp nào để ngăn ngừa va chạm mạng?
A. Nhóm Truy cập ngẫu nhiên (Random Access).
B. Nhóm Định tuyến động (Dynamic Routing).
C. Nhóm Luân phiên (Taking-Turns).
D. Nhóm Phân chia tần số (Frequency Partitioning).
*Đáp án: C*
*Giải thích: Nhóm này yêu cầu trật tự xếp hàng: Đến lượt mới được nói. Ưu điểm là không có va chạm, nhưng bị "Điểm yếu độc tôn": Rớt thẻ bài hoặc Master chết là hỏng toàn bộ mạng.*

**Câu 9:** Đặc trưng cốt lõi của một thiết bị Hub (Bộ tập trung) là gì?
A. Cực kỳ thông minh, hoạt động ở Tầng mạng.
B. Thiết bị ở Tầng Vật lý (Layer 1), nó nhận tín hiệu điện từ 1 cổng, sao chép tín hiệu đó và khuếch đại ném thẳng ra TẤT CẢ các cổng còn lại một cách hoàn toàn vô điều kiện.
C. Chỉ chuyển tiếp tín hiệu ra 1 cổng duy nhất.
D. Có bảng học địa chỉ IP.
*Đáp án: B*
*Giải thích: Hub là thiết bị "mù", làm việc thuần vật lý. Do tính khuếch đại bừa bãi nên nó biến toàn bộ mạng LAN thành một Môi trường xung đột (Collision Domain) khổng lồ.*

**Câu 10:** Khác với Hub, thiết bị Switch (Bộ chuyển mạch) thông minh hơn ở điểm nào?
A. Switch hoạt động ở Tầng Giao vận.
B. Switch đọc trường IP đích.
C. Switch hoạt động ở Tầng 2, biết đọc Địa chỉ MAC đích của Khung Ethernet, kiểm tra "Bảng địa chỉ MAC" của mình và chỉ ĐẨY KHUNG CÓ CHỌN LỌC ra ĐÚNG cổng nối với máy nhận.
D. Switch rẻ tiền hơn Hub rất nhiều.
*Đáp án: C*
*Giải thích: Switch chia rẽ các Miền Xung Đột (Collision Domain). Nếu A gửi cho B qua Switch, thì C cũng có thể gửi cho D ngay lúc đó mà không hề đụng độ với luồng A-B.*

**Câu 11:** Thiết bị Switch xây dựng "Bảng địa chỉ MAC" (Switch Table) bằng thuật toán Tự Học (Self-Learning) như thế nào?
A. Nhờ kỹ thuật viên nhập tay từng dòng lệnh.
B. Switch đọc trường ĐỊA CHỈ MAC NGUỒN của mọi khung tin khi nó vừa chui vào Cổng (Port) nào đó, và học lỏm ghi lại "À, máy có MAC này nằm ở nhánh Cổng này".
C. Bằng cách gửi gói tin BGP.
D. Switch kết nối lên Google để tải về.
*Đáp án: B*
*Giải thích: Switch là thiết bị cắm-và-chạy (Plug-and-play). Không cần ai dạy, nó tự nhìn trộm MAC nguồn để vẽ nên bản đồ các cổng nối với các máy.*

**Câu 12:** Khi Switch gặp một Khung có MAC Đích mà trong bảng học lỏm của nó CHƯA CÓ, nó phản ứng thế nào?
A. Vứt (Drop) gói tin đó ngay.
B. Báo lỗi về máy nguồn.
C. Lập tức biến thành Hub tạm thời: Flood (Phát tán) gói tin đó ra TẤT CẢ các cổng còn lại ngoại trừ cổng nó vừa nhận, để đảm bảo máy đích có nhận được.
D. Tự tạo ra một MAC ngẫu nhiên.
*Đáp án: C*
*Giải thích: Trạng thái mù đường. Khi máy đích nhận được và trả lời lại, lập tức Switch sẽ học được máy đích nằm ở cổng nào, lần sau sẽ không Flood nữa.*

**Câu 13:** ARP (Address Resolution Protocol) giải quyết nhiệm vụ gì trong mạng cục bộ?
A. Cấp phát IP tự động.
B. Dịch địa chỉ IP của một máy tính (đã biết trước) ra thành địa chỉ vật lý MAC tương ứng để có thể đóng khung Ethernet.
C. Chống xung đột cáp quang.
D. Giám sát băng thông video.
*Đáp án: B*
*Giải thích: Tầng 3 có IP, nhưng để đi ra cáp đồng của Tầng 2 phải có MAC. ARP là quyển sổ danh bạ tra cứu IP -> MAC trong cùng 1 LAN.*

**Câu 14:** Thông điệp truy vấn ARP (ARP Query) được phát đi dưới định dạng nào?
A. Unicast
B. Multicast
C. Broadcast (Gửi đến MAC đích FF:FF:FF:FF:FF:FF) tới tất cả các thiết bị trong mạng con (Subnet).
D. Anycast
*Đáp án: C*
*Giải thích: Vì không biết máy kia MAC gì nên phải la làng lên (Broadcast): "Ê, anh nào mang IP 192.168.1.100 khai báo MAC cho tôi với!". Chỉ máy nào đúng IP đó mới trả lời.*

**Câu 15:** Điều gì ngăn cách hai miền phát tán (Broadcast Domains) khác nhau?
A. Hub
B. Switch Tầng 2
C. Cáp đồng
D. Router (Bộ định tuyến)
*Đáp án: D*
*Giải thích: Tín hiệu ARP Broadcast chỉ lanh quanh trong LAN. Router khi nhận được gói Broadcast FF:FF:FF... nó sẽ chặn đứng lại (Drop), không bao giờ cho rò rỉ sang mạng LAN khác. Router chia cắt Broadcast domains.*

**Câu 16:** Địa chỉ MAC khác với địa chỉ IP ở cấu trúc hình thức như thế nào?
A. MAC không thay đổi, IP có thay đổi.
B. MAC dài 128 bit, IP dài 32 bit.
C. Địa chỉ MAC dài 48 bit (6 bytes) và thường được viết theo định dạng Thập lục phân (Hexadecimal), ví dụ: 00:1A:2B:3C:4D:5E.
D. IP ghi cứng vào phần cứng, MAC cấu hình bằng phần mềm.
*Đáp án: C*
*Giải thích: Kích thước 48 bit cho phép tạo ra khoảng 281 nghìn tỷ MAC duy nhất do nhà sản xuất (như Intel, Broadcom) gán chết vào card mạng (burned in ROM).*

**Câu 17:** Payload (Dữ liệu chở kèm) TỐI THIỂU của một khung Ethernet chuẩn (ví dụ mang IP Datagram) là bao nhiêu byte?
A. 0 byte
B. 20 bytes
C. 46 bytes (Nếu ít hơn, phải thêm các bit đệm - Padding).
D. 1500 bytes.
*Đáp án: C*
*Giải thích: Thiết kế của Ethernet chuẩn hóa kích thước gói tin tối thiểu để sóng đụng độ CSMA/CD có đủ thời gian quay về máy phát. Do đó payload bèo nhất phải 46 byte. Nhỏ quá thì chèn thêm dữ liệu rác.*

**Câu 18:** Công nghệ VLAN (Virtual LAN) trên Switch cho phép quản trị viên làm được việc gì?
A. Gộp 10 Switch lại thành 1 siêu Switch.
B. Dùng một Switch phần cứng (Physical Switch) duy nhất để phân chia logic thành NHIỀU mạng LAN nhỏ, tách biệt hoàn toàn các miền Broadcast và tăng tính bảo mật nội bộ.
C. Biến mạng dây thành mạng Wi-Fi.
D. Bỏ qua hoàn toàn địa chỉ MAC.
*Đáp án: B*
*Giải thích: VLAN giúp cắm phòng Kế toán và phòng Kỹ thuật chung 1 cái Switch 24 port nhưng Kỹ thuật không thể ping được Kế toán (trừ khi dùng Router) và Broadcast của Kế toán không bay sang phòng Kỹ thuật.*

**Câu 19:** Khái niệm "Trunk Port" trong mô hình có VLAN dùng để làm gì?
A. Cắm trực tiếp vào máy tính giám đốc.
B. Chỉ định cổng phát Wi-Fi.
C. Nối đường truyền cáp DUY NHẤT kết nối hai Switch VLAN với nhau, mang trên nó các khung thuộc ĐA DẠNG nhiều VLAN khác nhau bằng cách gán thêm thẻ định danh 802.1Q (VLAN Tag).
D. Dùng để cấu hình IP cho Router.
*Đáp án: C*
*Giải thích: Nếu không có Trunk, bạn phải cắm 1 sợi dây riêng cho VLAN Kế toán, 1 sợi cho Kỹ thuật giữa 2 Switch. Trunk port dồn hết vào 1 sợi dây, thêm cái thẻ 4-byte VLAN ID vào Frame để đầu kia bóc ra phân loại.*

**Câu 20:** Nếu máy tính của bạn ở Hà Nội gửi gói tin đến một máy tính ở New York, địa chỉ MAC đích của khung Ethernet khởi hành từ máy bạn là gì?
A. Địa chỉ MAC của máy New York.
B. Địa chỉ MAC của cáp quang biển.
C. Địa chỉ MAC của chính máy tính bạn.
D. Địa chỉ MAC của Cổng vào (Interface) trên Default Gateway Router nhà bạn.
*Đáp án: D*
*Giải thích: Rất quan trọng! Địa chỉ MAC KHÔNG ĐI XA ĐƯỢC. Khung Ethernet chỉ đi đến trạm trung chuyển (Router nhà bạn). Máy bạn sẽ dùng ARP hỏi MAC của Router và gửi khung cho Router. Sau đó Router xé khung, định tuyến IP, đóng Khung mới và nhắm tới Router tiếp theo.*


**Câu 21:** Trong một miền đụng độ (Collision Domain) sử dụng CSMA/CD, khi số lượng máy tính muốn truyền dữ liệu cùng lúc tăng lên rất nhiều, hiện tượng gì sẽ xảy ra đối với băng thông thực tế (Throughput) khả dụng?
A. Throughput không thay đổi vì băng thông được chia đều.
B. Throughput tăng lên do có nhiều máy tham gia.
C. Throughput giảm sút nghiêm trọng do phần lớn thời gian đường truyền bị lãng phí cho các vụ đụng độ (Collisions) và khoảng thời gian lùi lại ngẫu nhiên chờ đợi (Backoff).
D. Giao thức chuyển sang dùng Token Passing tự động.
*Đáp án: C*
*Giải thích: Hiệu suất (Efficiency) của CSMA/CD đi xuống khi mạng tải quá cao vì va chạm xảy ra liên tục, máy tính chỉ mải miết chờ lùi lại mà không truyền được dữ liệu hữu ích.*

**Câu 22:** Công thức để tính số trạm (host) tối thiểu cần cung cấp mã MAC là:
A. Mọi trạm đều dùng IP, không cần MAC.
B. MAC chỉ có trên Router.
C. Mỗi bộ chuyển đổi mạng (Network Adapter/Interface) gắn vào thiết bị đều phải có một địa chỉ MAC duy nhất toàn cầu.
D. Mọi trạm trong cùng LAN có chung 1 MAC.
*Đáp án: C*
*Giải thích: Laptop của bạn có 1 MAC cho cổng dây LAN (Ethernet NIC), và 1 MAC hoàn toàn khác cho cạc không dây (Wi-Fi NIC).*

**Câu 23:** Cấu trúc khung Ethernet chuẩn của IEEE 802.3 chứa một trường gọi là "Preamble" (Tiền tố) dài 8 byte ở đầu khung. Mục đích của Preamble là gì?
A. Để chứa địa chỉ IP Nguồn.
B. Đánh thức phần cứng máy nhận, đồng bộ hóa nhịp đồng hồ (clock synchronization) giữa máy phát và máy thu bằng chuỗi bit 10101010 trước khi đổ dữ liệu thực sự vào.
C. Kiểm tra lỗi phần cứng.
D. Báo hiệu cho các máy khác im lặng.
*Đáp án: B*
*Giải thích: Do không có đồng hồ chung, máy thu cần một đoạn nhạc dạo đầu (101010...) nhịp nhàng để khóa khớp tốc độ bắt bit của nó với tốc độ bit của máy phát.*

**Câu 24:** Một giao thức MAC theo phương pháp "Channel Partitioning" (Phân chia kênh) như TDM (Time Division) có ưu điểm và nhược điểm nào rõ nét nhất?
A. Ưu: Rất phức tạp. Nhược: Xung đột liên tục.
B. Ưu: Tận dụng 100% băng thông khi chỉ có 1 người dùng. Nhược: Chia không công bằng.
C. Ưu: Chia sẻ hoàn toàn công bằng và KHÔNG bao giờ có va chạm. Nhược: Lãng phí vô ích khi mạng ít người tải (VD có 10 khe nhưng 9 người im lặng, 1 người có nhiều data vẫn chỉ được dùng 1/10 băng thông).
D. Ưu: Truyền song song IP và MAC. Nhược: Bị Hacker dễ tấn công.
*Đáp án: C*
*Giải thích: Phân chia kênh (TDMA, FDMA) cứng ngắc giống như chia làn đường cố định. Làn xe buýt trống rỗng nhưng xe con vẫn kẹt, không được lấn làn.*

**Câu 25:** Vì sao ngày nay trong mạng nội bộ (LAN) của các doanh nghiệp, hiện tượng đụng độ (Collision) dường như KHÔNG còn tồn tại?
A. Vì họ dùng giao thức IP bản mới.
B. Vì tất cả doanh nghiệp đều dùng cấu trúc mạng sao (Star topology) xoay quanh các thiết bị Hub truyền thống.
C. Vì doanh nghiệp sử dụng toàn bộ cáp quang.
D. Vì họ triển khai các bộ chuyển mạch Switch hoạt động ở chế độ Full-Duplex (Song công toàn phần), mỗi nút mạng có sợi truyền và sợi nhận riêng biệt tới cổng Switch, cách ly hoàn toàn Collision Domain.
*Đáp án: D*
*Giải thích: Switched Ethernet với Full-duplex khiến card mạng vừa truyền vừa nhận cùng lúc mà không chạm sóng, loại bỏ vĩnh viễn CSMA/CD khỏi cuộc sống thực tế.*

**Câu 26:** Mối tương quan giữa ARP Table và Switch Table (MAC Table) là gì?
A. Chúng là một. Cả hai đều ánh xạ IP sang MAC.
B. Switch Table chứa cấu hình IP của nhà mạng.
C. ARP Table nằm trong Máy tính cá nhân / Router dùng để ánh xạ (IP -> MAC). Switch Table nằm trong Switch dùng để ánh xạ (MAC -> Cổng vật lý số mấy).
D. Chạy ở Tầng Giao vận.
*Đáp án: C*
*Giải thích: Máy tính cần ARP để biết ghi MAC Đích là gì vào Frame. Switch nhận được Frame đó cần Switch Table để biết xuất cái Frame đó ra lỗ nào.*

**Câu 27:** Mạng Token Ring sử dụng cơ chế nào để giải quyết vấn đề đa truy cập?
A. Lắng nghe sóng mạng (Carrier Sense).
B. Tự động tránh va chạm.
C. Có một Master dò quanh các máy.
D. Truyền tay một "thẻ bài" (Token) luân phiên. Máy nào nắm thẻ bài mới có quyền bơm khung dữ liệu lên vòng cáp.
*Đáp án: D*
*Giải thích: Kiến trúc Taking-turns (luân phiên) bằng thẻ bài ngăn đụng độ tuyệt đối, nhưng nếu máy cầm thẻ bị sập nguồn làm mất thẻ thì mạng "chết lâm sàng".*

**Câu 28:** Mạng Ethernet chuẩn 1000BASE-T sử dụng loại cáp truyền thông nào?
A. Cáp quang đa mốt.
B. Cáp đồng trục.
C. Cáp đồng đôi xoắn (Twisted-pair copper wire) tốc độ 1 Gigabit/giây.
D. Sóng vô tuyến.
*Đáp án: C*
*Giải thích: "T" ám chỉ Twisted-pair. 1000 chỉ 1000 Mbps = 1 Gbps.*

**Câu 29:** Nếu một thiết bị đang thực hiện CSMA/CD và đụng độ lần thứ 3 liên tiếp, khoảng lùi thời gian ngẫu nhiên (Backoff) của nó sẽ được rút từ tập số nào?
A. {0, 1, 2, 3}
B. {0, 1, 2, 3, 4, 5, 6, 7}
C. {0, 1, ..., 15}
D. Cố định 3 giây.
*Đáp án: B*
*Giải thích: Công thức là rút ngẫu nhiên K từ {0, 1, ..., 2^n - 1}. Với n = 3, $2^3 - 1 = 7$. Vậy tập là {0..7}.*

**Câu 30:** Khi Máy A khởi động và có IP tĩnh, nhưng nó không biết IP đó có bị máy nào khác trong LAN đang dùng trùng hay không. Nó dùng cơ chế ARP đặc biệt nào để dò tìm sự trùng lặp (Duplicate IP)?
A. Proxy ARP.
B. Gratuitous ARP (Gửi ARP Request truy vấn chính địa chỉ IP của bản thân mình).
C. Reverse ARP (RARP).
D. Gửi email lên máy chủ.
*Đáp án: B*
*Giải thích: Gratuitous ARP la lên "Ai dùng IP 192.168.1.10 thì lên tiếng". Vì nó chính là thằng 10, nếu không ai lên tiếng nghĩa là IP chưa bị trùng.*

**Câu 31:** Nhiệm vụ cơ bản nhất của Tầng Liên kết dữ liệu (Data Link Layer) là gì?
A. Cung cấp Dịch vụ DNS và gửi Email.
B. Định tuyến đường đi liên lục địa của Gói tin IP.
C. Vận chuyển gói tin qua MỘT MẮT XÍCH DUY NHẤT (Ví dụ: Từ máy tính này sang Router kế bên trên cùng một đoạn cáp vật lý / LAN).
D. Phân bổ IP mạng.
*Đáp án: C*
*Giải thích: Đơn vị đóng gói ở tầng này là Frame (Khung). Nếu Tầng Mạng (L3) là Giám đốc lập Kế hoạch đi từ Hà Nội vào SG, thì Tầng Liên kết (L2) là Tài xế lái Xe đò chở bạn từ Bến xe Giáp Bát ra Nút giao Pháp Vân.*

**Câu 32:** Đặc tính của Kênh truyền (Link) ở Tầng Liên kết Data Link được chia làm 2 loại cơ bản nhất là:
A. Kênh Analog và Kênh Digital.
B. Kênh Liên kết Điểm-Điểm (Point-to-Point, như cáp quang nối 2 router) và Kênh Liên kết Quảng bá (Broadcast, nhiều máy cùng chung một không gian sóng Wi-Fi hoặc một cáp đồng trục).
C. Kênh Vệ tinh và Kênh Đáy biển.
D. Kênh Mở và Kênh Đóng.
*Đáp án: B*
*Giải thích: Giao tiếp qua Kênh Điểm-Điểm rất sướng vì 1 mình 1 đường, không sợ va chạm đụng độ. Giao tiếp trên Kênh Broadcast thì hỗn loạn, phải có cảnh sát giao thông (Giao thức MAC).*

**Câu 33:** Địa chỉ Vật lý ở Tầng Liên kết được gọi bằng thuật ngữ gì trong mạng Ethernet / Wi-Fi?
A. IPv4 Address.
B. Port Number.
C. MAC Address (Media Access Control Address).
D. VLAN ID.
*Đáp án: C*
*Giải thích: Dài 48 bit (6 byte). MAC giống như Số Chứng Minh Nhân Dân, nó là ĐỊNH DANH PHẦN CỨNG dính liền với cái card mạng từ khi xuất xưởng, không thay đổi theo vị trí địa lý.*

**Câu 34:** Giao thức MAC (Đa truy nhập - Multiple Access Protocol) ra đời để giải quyết vấn đề cốt lõi gì của môi trường Liên kết Quảng bá (Broadcast Link)?
A. Đổi IP.
B. Ngăn chặn Hiện tượng Xung đột/Đụng độ (Collision) khi có 2 hoặc nhiều thiết bị cùng GỬI TÍN HIỆU điện/vô tuyến ĐỒNG THỜI vào không gian chung, làm tín hiệu bị méo mó, nhiễu rác.
C. Giải nén video.
D. Định tuyến lại mạng.
*Đáp án: B*
*Giải thích: Nếu trong 1 phòng họp (Broadcast) ai cũng tranh nhau mở loa phát biểu (Collision), chẳng ai nghe được ai. Giao thức MAC quy định "Luật giơ tay phát biểu".*

**Câu 35:** Phương pháp điều khiển truy nhập đường truyền (MAC) nào cho phép cấp cố định một dải Tần số vô tuyến riêng biệt cho từng điện thoại gọi điện?
A. TDMA
B. CSMA/CD
C. FDMA (Frequency Division Multiple Access - Đa truy nhập phân chia theo Tần số).
D. Slotted ALOHA
*Đáp án: C*
*Giải thích: Một ví dụ điển hình là nghe Đài Radio. Bạn bật VOV Giao thông (104.5 MHz), và bật Đài XoneFM (102 MHz) cùng lúc nhưng không bị nhiễu sóng vì chúng đã được "Phân tần".*

**Câu 36:** Phương pháp TDM (Time Division Multiplexing - Chia theo thời gian) có nhược điểm gì LỚN NHẤT so với việc dùng Internet truyền thống?
A. Rất khó sửa chữa.
B. Rất tốn điện năng.
C. Lãng phí tài nguyên kênh truyền thê thảm nếu người dùng RẢNH (không có dữ liệu gửi). Dù không nói gì, khe thời gian đó vẫn bị chiếm dụng mà người khác không được xài ké.
D. Làm đứt cáp quang.
*Đáp án: C*
*Giải thích: Bạn thuê hẳn 1 phòng họp cho 24 tiếng, nhưng bạn chỉ họp 10 phút rồi về ngủ. 23h50 phút còn lại phòng họp bị khóa, người ngoài cửa không được vào. Đó là TDM tĩnh.*

**Câu 37:** Giao thức CSMA/CD (Carrier Sense Multiple Access with Collision Detection) được chuẩn hóa và sử dụng ĐỘC TÔN cho mạng nào?
A. Mạng Wi-Fi.
B. Mạng 4G LTE.
C. Mạng Ethernet LAN Có Dây dạng cũ (Half-duplex / Dùng Hub đồng trục).
D. Mạng quang P2P.
*Đáp án: C*
*Giải thích: Carrier Sense (Nghe ngóng đường truyền xem có ai đang nói không, im thì mới được nói). Collision Detection (Đang nói mà nghe thấy thằng khác cũng nói xen vào thì lập tức DỪNG NGAY ĐỂ TRÁNH NHIỄU, đợi 1 lúc sau nói lại).*

**Câu 38:** Tại sao Wi-Fi (802.11) KHÔNG DÙNG được cơ chế "Phát hiện đụng độ" (Collision Detection - CD) của Ethernet có dây?
A. Sóng Wi-Fi mạnh quá.
B. Vì Môi trường vô tuyến rất phức tạp. Sóng phát ra từ Ăng-ten thiết bị Gửi luôn lấn át (chói tai) khiến nó không thể vừa hát to vừa nghe ngóng xem tín hiệu của người khác có va chạm với nó ngoài không gian hay không. Hơn nữa do Vấn đề Điểm mù (Hidden Terminal).
C. Do dùng mật khẩu WPA.
D. Wi-Fi không có MAC.
*Đáp án: B*
*Giải thích: CSMA/CD cần 1 sợi cáp đồng nhất tĩnh. Không gian vô tuyến thì có tiếng vang, có suy hao. Máy tính phát Wi-Fi là "điếc" tạm thời, chỉ biết gào xong rồi cầu nguyện Máy nhận gửi ACK.*

**Câu 39:** Để thay thế cho chức năng CD (Detection - Phát hiện đụng độ), Wi-Fi sử dụng giao thức MAC nào?
A. Token Ring.
B. FDMA.
C. CSMA/CA (Collision Avoidance - Tránh đụng độ). Nó dùng thêm các thông điệp nhỏ là RTS (Request to Send - Xin phép gửi) và CTS (Clear to Send - Cho phép gửi) để đặt gạch phòng họp trước khi phát biểu.
D. BGP Routing.
*Đáp án: C*
*Giải thích: CSMA/CA giống như bạn lên bục phát biểu, bạn phải bốc bộ đàm hỏi chủ toạ (Access Point): "Tôi nói nhé?". Chủ toạ gật đầu "Ok", thì bạn mới phát Data. Đổi lấy tốc độ chậm để an toàn tối đa.*

**Câu 40:** "Vấn đề Trạm ẩn" (Hidden Terminal Problem) trong mạng không dây là hiện tượng gì?
A. Trạm giấu địa chỉ IP.
B. Hacker ẩn danh đánh cắp dữ liệu.
C. Máy A và Máy C đều muốn gửi cho Bộ phát B ở giữa. Nhưng A và C đứng ở khoảng cách quá xa không thể thu sóng (Nghe ngóng / Carrier Sense) thấy nhau. A tưởng không khí vắng lặng, C cũng tưởng vắng lặng, Cùng phát cho B. Hậu quả là B bị "Đinh tai nhức óc" do 2 sóng đập vào nhau.
D. Rớt mạng do tường dày.
*Đáp án: C*
*Giải thích: Tình huống oái oăm chỉ có ở vô tuyến. RTS/CTS (như câu 39) giải quyết việc này. B nhận RTS của A, B sẽ hét lên CTS. C nghe được lệnh CTS của B sẽ im lặng đợi.*

**Câu 41:** Cấu trúc của Khung mạng Ethernet (Ethernet Frame) ở Tầng Liên Kết chứa các trường thông tin quan trọng nào?
A. Source IP và Destination IP.
B. Source Port và Destination Port.
C. Preamble (Lời mở đầu đồng bộ), Destination MAC, Source MAC, Type (Chỉ định gói bên trong là IPv4 hay ARP), Data (Payload IP), và FCS (Kiểm tra mã CRC 32-bit).
D. Mật khẩu kết nối.
*Đáp án: C*
*Giải thích: Header và Trailer của Frame L2 bọc kỹ càng gói IP Packet L3.*

**Câu 42:** Trong Ethernet, 8 Byte đầu tiên của Frame gọi là "Preamble" (Lời nói đầu: `10101010...10101011`) dùng để làm gì?
A. Làm mật khẩu truy cập LAN.
B. Đánh thức đồng hồ (Clock synchronization) phần cứng của Card mạng Máy nhận, giúp Máy nhận đồng bộ hóa chu kỳ xung nhịp và chuẩn bị sẵn sàng bắt đúng các byte Data ngay phía sau.
C. Không làm gì.
D. Tính độ dài cáp mạng.
*Đáp án: B*
*Giải thích: Tín hiệu điện chạy trên cáp đồng có thể trôi trượt (Drift). Chuỗi 1010 xen kẽ này dội liên tục vào mắt Cảm biến như máy gõ nhịp giúp 2 máy bắt nhịp hoàn hảo trước khi nhảy vào bản nhạc Data.*

**Câu 43:** Kỹ thuật Sửa sai Lỗi bit (Error Detection) ở Tầng 2 thường ưu việt và tinh vi hơn Tầng 4 (Checksum TCP) thông qua thuật toán nào?
A. Đếm số ký tự chẵn lẻ (Parity Check).
B. Cộng bù 1.
C. Tính toán Mã Kiểm tra Độ dư thừa theo chu trình (CRC - Cyclic Redundancy Check) bằng đa thức toán học. Đặt ở Trường FCS cuối Frame, giúp bắt 99.999% các lỗi nhiễu vỡ vụn bit.
D. Không kiểm tra lỗi.
*Đáp án: C*
*Giải thích: FCS ở Frame L2 rất mạnh vì nó được xử lý cực kỳ nhanh bằng cấu trúc mạch Logic Phần cứng (ASIC) bên trong con Chip điều khiển card mạng.*

**Câu 44:** Khi Thiết bị A (có IP A, MAC A) muốn gửi cho Thiết bị B (có IP B, nhưng CHƯA BIẾT MAC B), A sẽ thực hiện thao tác gì ĐẦU TIÊN (nếu chúng cùng chung 1 mạng LAN)?
A. Đóng kết nối TCP.
B. Gửi thẳng vào Router.
C. Dừng tất cả mọi việc lại, Máy A tự động phát hành MỘT GÓI TIN QUẢNG BÁ ARP (ARP Request: MAC đích là FF:FF:FF:FF:FF:FF) gào lên với toàn thể nhân viên trong phòng "Ai có IP là B, làm ơn cho tôi xin cái số thẻ MAC của bạn".
D. Xóa bộ nhớ DNS.
*Đáp án: C*
*Giải thích: Gói tin không thể đi đâu nếu không đóng gói được Lớp 2 (Vì không có MAC Destination để ghi lên phong bì). ARP là Phao cứu sinh móc nối L3 xuống L2.*

**Câu 45:** "Bảng ARP" (ARP Cache / ARP Table) lưu trong Máy tính và Router có tác dụng gì?
A. Lưu trữ IP của Website.
B. Lưu trữ Tên miền DNS.
C. Ghi nhớ tạm thời (Trong vài phút) danh sách ánh xạ (Map) giữa Địa chỉ IP của các máy nội bộ và Địa chỉ MAC tương ứng của chúng. Tránh việc MỖI gói tin xuất phát đều phải Gào lên Broadcast ARP rác mạng.
D. Chứa thông số cấu hình Firewall.
*Đáp án: C*
*Giải thích: ARP Cache giống Danh bạ điện thoại thu nhỏ của Tầng Liên Kết. Lâu lâu xóa đi để cập nhật phòng khi có máy hỏng hóc/thay card mạng (MAC).*

**Câu 46:** Giao thức nào thực thi việc "Cấp phát IP Động" (DHCP) tận dụng khả năng gì của Tầng Liên kết để "Tìm" thấy máy chủ DHCP khi máy khách thậm chí CHƯA CÓ một cái IP nào?
A. Gửi qua kết nối TCP 3 bước.
B. Nó đẩy gói tin DHCP Discover vào 1 khung Broadcast MAC (FF:FF:FF:FF:FF:FF) và IP Đích Broadcast (255.255.255.255). Frame này chạy quanh phòng LAN, tới Router DHCP, Router sẽ nhận được và tiến hành cấp IP.
C. Dùng DNS cấp IP.
D. Phải gõ IP bằng tay.
*Đáp án: B*
*Giải thích: DHCP là một quá trình kì diệu kiểu "Con gà, quả trứng". Khi chưa có tên tuổi (IP), thiết bị lấy cái "CMND vật lý" (MAC) và hét toáng lên "Ông quản lý kho ơi, MAC tôi là X, cấp cho tôi xin cái IP".*

**Câu 47:** Chức năng hoạt động kinh điển của Cầu nối Tầng 2 (Switch Layer 2) khác với Hub chia mạng như thế nào?
A. Không khác biệt.
B. Hub chỉ là Tầng 1 (Vật lý), nó nhận tín hiệu điện 1 cổng rồi "Bơm vọt" Mù quáng ra mọi cổng (Broadcast rác). Switch ở Tầng 2 cực kỳ thông minh, nó có TRÍ NHỚ (Switch Table), biết chính xác máy tính MAC nào đang cắm ở cổng nào, và chuyển mạch ƯU TIÊN ĐÍCH DANH (Unicast) đến đúng cổng đó.
C. Hub nhanh hơn Switch.
D. Switch có chức năng đổi cáp mạng.
*Đáp án: B*
*Giải thích: Hub làm mọi máy trong mạng phải tranh nhau "Cãi nhau" (Chung Collision Domain). Switch cắt mạng ra thành nhiều "Phòng riêng", 2 máy nói chuyện không ai nghe thấy (Micro-segmentation).*

**Câu 48:** Bộ chuyển mạch (Switch) làm thế nào để TỰ HỌC (Self-learning) và xây dựng được cái Trí nhớ (Switch Table/ MAC Table) của nó?
A. Nhập tay từ Admin.
B. Trực giác.
C. Nó "Học lỏm". Khi Máy A (Cắm cổng 1) gửi 1 gói tin cho B. Khung Frame đi qua Switch, Switch lập tức LƯU LẠI ĐỊA CHỈ MAC NGUỒN CỦA A và ghi vào sổ: "À, tao ghi nhận MAC của thằng A nằm ở Cổng số 1".
D. Nó tải bảng MAC từ Internet xuống.
*Đáp án: C*
*Giải thích: Plug-and-play tự nhiên. Bạn mua cục mạng TPLink về cắm là xong. Cục TPLink ngồi rình, ai nói chuyện đi qua nó thì nó lôi sổ ra ghi MAC của người đó vào cổng cắm. Vài giây sau là nó thuộc lòng toàn bộ nhà mạng.*

**Câu 49:** Nếu Switch nhận được Frame có Đích đến là MAC B, nhưng trong Bảng MAC của nó CHƯA CÓ bản ghi nào về B, nó sẽ xử lý sao?
A. Drop vứt bỏ luôn.
B. Báo lỗi ICMP.
C. Nó sẽ thực hiện thao tác "Flood" (Lụt/Ngập): Bơm phát Frame này ra TẤT CẢ các cổng còn lại (Trừ cổng nhận vào). Khi B (Ở một cổng nào đó) nhận được và trả lời lại, Switch sẽ tức khắc "Học" được vị trí của B.
D. Gọi điện hỏi ISP.
*Đáp án: C*
*Giải thích: Switch khi "Mù thông tin" thì hành xử ngốc nghếch giống y hệt cái Hub. Lụt (Flooding) là cách phòng thủ cuối cùng để giao hàng khi chưa thuộc bản đồ.*

**Câu 50:** Tấn công "MAC Flooding" vào Tầng 2 nhằm đánh sập Switch được thực hiện như thế nào?
A. Gửi Virus qua mạng.
B. Hacker dùng phần mềm sinh ra hàng vạn Frame với Địa chỉ MAC Nguồn ngẫu nhiên liên tục gửi vào Switch. Bảng MAC của Switch (chỉ lưu được cỡ 8000 dòng) lập tức BỊ TRÀN BỘ NHỚ. Khi đầy, Switch biến thành một Hub ngu ngốc (Lụt gói tin ra mọi cổng), Hacker tha hồ Sniff nghe lén dữ liệu của phòng máy.
C. Tắt cổng 80 của mạng.
D. Thay đổi Router.
*Đáp án: B*
*Giải thích: Switch an toàn vì nó gửi thư kín. Nhưng khi RAM nó nổ tung, nó buộc phải vứt thư vung vãi cho mọi người đọc. Đây là tấn công Tầng Liên Kết kinh điển (Giải pháp là dùng Port Security chặn giới hạn MAC/cổng).*

**Câu 51:** Giao thức Spanning Tree Protocol (STP) được sinh ra để bảo vệ các Tầng 2 (Switches) khỏi thảm họa gì?
A. Tấn công DDoS.
B. Vòng lặp Định tuyến.
C. Bão Quảng bá (Broadcast Storm) gây ra bởi các VÒNG LẶP VẬT LÝ (Loop). Khi cắm dây cáp kết nối dự phòng thừa thãi tạo thành mạch kín giữa các Switch, STP sẽ sử dụng thuật toán Bầu chọn rễ cây (Root Bridge) và TỰ ĐỘNG KHÓA (Block) các Cổng dư thừa về mặt Logic, phá vỡ vòng tròn tử thần.
D. Tránh hư dây cáp.
*Đáp án: C*
*Giải thích: Nếu 3 Switch cắm tạo hình tam giác. 1 gói Broadcast tung ra sẽ chạy lòng vòng nhân bản 3 cái switch đó suốt đời (vì Tầng 2 không có TTL để chết tự nhiên như Tầng 3).*

**Câu 52:** Mạng VLAN (Virtual LAN) cấu hình trên Switch thực tế giải quyết yêu cầu kỹ thuật nào?
A. Làm tăng lượng MAC Table.
B. Tách một Broadcast Domain Vật lý to đùng (1 Switch 48 cổng) thành nhiều Broadcast Domain Lô-gic nhỏ (Ví dụ: VLAN 10 cho Kế toán, VLAN 20 cho IT). Các máy ở 2 VLAN khác nhau KHÔNG THỂ gọi ARP nhau hay liên lạc nhau nếu không có Router Lớp 3 can thiệp.
C. Bật chức năng Wi-Fi ảo.
D. Biến Switch L2 thành Máy tính.
*Đáp án: B*
*Giải thích: Sức mạnh mềm dẻo. Hôm qua Kế toán ngồi tầng 1, hôm nay lên lầu 5. IT chỉ việc đăng nhập Switch cấu hình cổng Tầng 5 vào VLAN 10, người Kế toán vẫn giữ nguyên mạng cũ mà không phải kéo lại dây điện.*

**Câu 53:** Để 2 Switch truyền hàng chục VLAN khác nhau qua MỘT SỢI CÁP VẬT LÝ DUY NHẤT nối giữa chúng, chúng sử dụng chuẩn kỹ thuật nào?
A. Trunking (Đường ống Trunk - IEEE 802.1Q). Switch Gửi sẽ GẮN THÊM một cái Tag VLAN 4-Byte (Có VLAN ID) vào Frame L2. Switch Nhận sẽ dọc Tag đó, ném gói tin vào đúng VLAN tương ứng và bóc Tag ra giao cho máy tính.
B. CSMA/CD.
C. Mã hóa IPsec.
D. Dùng mạng MPLS.
*Đáp án: A*
*Giải thích: Đóng gói (Tagging) Lớp 2. Máy tính cùi bắp không biết VLAN là gì (Untagged). Chỉ có Switch mới "nói tiếng" Tagged 802.1Q với nhau trên đường Trunk vĩ đại.*

**Câu 54:** Dòng Byte "FCS" (Frame Check Sequence) trong khung Ethernet được tính bằng phép toán nào?
A. Phép mã hóa SHA-1.
B. CRC (Cyclic Redundancy Check). Một phép chia đa thức hệ nhị phân dư.
C. Cộng dồn IP.
D. Nhân chéo Checksum.
*Đáp án: B*
*Giải thích: CRC siêu việt hơn Checksum TCP/IP ở điểm nó phát hiện được các lỗi "lật bit chùm" (Burst errors - sấm sét làm méo 1 cụm 5 bit liên tiếp), trong khi Checksum cộng bù rất dễ bỏ sót lỗi dạng này.*

**Câu 55:** Công nghệ cáp Ethernet tốc độ Gigabit (1000BASE-T) sử dụng mấy cặp dây đồng xoắn?
A. 1 cặp.
B. 2 cặp (Giống Fast Ethernet 100Mbps 100BASE-TX).
C. 4 cặp (Cả 8 sợi dây đồng trong cáp Cat5e/Cat6 đều được tận dụng để truyền và nhận dữ liệu song công đồng thời).
D. Cáp quang.
*Đáp án: C*
*Giải thích: Fast Ethernet 100M ngày xưa chỉ dùng 4 sợi (2 sợi phát, 2 sợi nhận). Lên tới 1Gbps, công nghệ tận dụng sức mạnh cả 8 sợi (Full 4 Pairs) với kỹ thuật khử nhiễu dội điện tử siêu việt.*

**Câu 56:** Môi trường truyền dẫn chia sẻ (Shared Medium) của Wi-Fi bị hạn chế Tốc độ so với Cáp LAN trực tiếp do yếu tố vật lý nào?
A. Băng thông vô tuyến quá hẹp.
B. Thiết bị Wi-Fi là loại Half-duplex (Bán song công). Thiết bị CHỈ CÓ THỂ PHÁT hoặc CHỈ CÓ THỂ NHẬN trong một thời điểm (không thể vừa hát vừa nghe). Trong khi Cáp đồng là Full-duplex.
C. Ăng-ten Wi-Fi bị cháy.
D. Giao thức UDP.
*Đáp án: B*
*Giải thích: Vì không có ống dẫn riêng rẽ như cáp đồng 8 sợi. Tất cả sóng điện từ hòa chung vào không khí. Đây là giới hạn lớn nhất của vô tuyến.*

**Câu 57:** Trong mạng 802.11 (Wi-Fi), "Access Point" (AP - Bộ phát) hoạt động ở tầng nào của mô hình TCP/IP?
A. Tầng Ứng dụng.
B. Tầng Giao vận.
C. Tầng Liên kết dữ liệu (Data Link / Tầng 2) và Tầng Vật lý (Tầng 1). Nó hoạt động như một Bridge (Cầu nối) Lớp 2 chuyển đổi từ Frame không dây (802.11) sang Frame có dây (802.3 Ethernet).
D. Tầng Mạng (Lớp 3).
*Đáp án: C*
*Giải thích: AP (Bộ phát sóng thuần) chỉ làm việc chuyển phát MAC, không cấp IP, không định tuyến (Khác với cục Router gia đình đa năng vừa là AP vừa là NAT/DHCP Router).*

**Câu 58:** Đơn vị PDU (Protocol Data Unit) của tầng Liên kết Dữ liệu (Data Link Layer) tên là gì?
A. Datagram
B. Segment
C. Frame (Khung). Chứa tải trọng IP Datagram bên trong nó.
D. Bits
*Đáp án: C*
*Giải thích: Frame là đơn vị bọc cuối cùng trước khi chuyển hóa thành các xung điện (Bit) ném xuống Tầng 1 (Physical).*

**Câu 59:** Tấn công "ARP Spoofing" (Giả mạo ARP) để thiết lập kỹ thuật Man-in-the-Middle diễn ra như thế nào trên Tầng L2?
A. Tấn công bằng phần mềm Virus.
B. Kẻ tấn công (Máy C) dội các GÓI ARP REPLY GIẢ mạo liên tục vào Mạng LAN gào lên: "Tôi (Máy C) có Địa chỉ MAC của Router Gateway (Máy R)!". Máy nạn nhân (A) mù quáng tin và lưu vào ARP Cache. Sau đó MỌI dữ liệu ra mạng của A đều dâng tận miệng máy C của Hacker (C đọc lén rồi chuyển tiếp cho R).
C. Phá hủy bảng MAC của Switch.
D. Mã hóa mật khẩu người dùng.
*Đáp án: B*
*Giải thích: Lỗ hổng khổng lồ của ARP là nó Trust (Tin cậy tuyệt đối) vào mọi thứ nó nghe được mà không cần Xác thực (No Auth).*

**Câu 60:** Khái niệm "Collision Domain" (Miền Đụng độ) được ĐỊNH NGHĨA như thế nào trong Mạng Máy tính?
A. Phạm vi điện áp cáp đồng.
B. Vùng mạng vật lý mà ở đó, Nếu có 2 thiết bị CÙNG GỬI gói tin một lúc thì tín hiệu của chúng SẼ ĐÂM VÀO NHAU và bị hủy hoại. Các cổng của HUB thuộc chung 1 miền đụng độ. Các cổng của SWITCH thì tách biệt MỖI CỔNG LÀ 1 miền đụng độ RIÊNG BIỆT (cách ly rủi ro).
C. Số IP được chia trong LAN.
D. Khu vực dùng DNS.
*Đáp án: B*
*Giải thích: Switch đã giết chết Hub vì nó chém nát cái Miền Đụng Độ chung khổng lồ thành vô số đường ống cá nhân an toàn.*

**Câu 61:** "MAC Address" được cấp phát và quản lý bởi tổ chức nào trên thế giới?
A. Microsoft.
B. IEEE (Viện Kỹ sư Điện và Điện tử). IEEE cấp Dải tiền tố 24-bit OUI (Organizationally Unique Identifier) cho các Nhà sản xuất Card mạng (như Intel, Broadcom) để đảm bảo không có 2 card mạng nào trên đời bị trùng số MAC (Lý thuyết).
C. Liên Hợp Quốc.
D. Chính phủ Mỹ.
*Đáp án: B*
*Giải thích: 3 byte đầu của MAC thể hiện Tên Công ty sản xuất. 3 byte sau là Số sê-ri do công ty tự đánh.*

**Câu 62:** "Broadcast Domain" (Miền Quảng bá) được chặn (Block) lại bởi thiết bị phần cứng nào?
A. Hub
B. Repeater
C. Switch (L2)
D. Router (L3). Router TUYỆT ĐỐI không bao giờ cho các Frame Quảng bá (Đích FF:FF:FF...) nhảy qua cổng của nó (Trừ khi cấu hình Helper). Do đó nó cắt dứt dải LAN bão táp rác rưởi.
*Đáp án: D*
*Giải thích: Switch (Tầng 2) chặn Miền Đụng Độ (Collision Domain). Router (Tầng 3) cao cấp hơn, chặn Miền Quảng Bá (Broadcast Domain).*

**Câu 63:** Cáp quang được ưu tiên sử dụng trong các Đường dẫn "Backbone" (Mạng lõi) nối các Tòa nhà / Quốc gia vì đặc tính vật lý nào ở Tầng 1?
A. Truyền qua không khí.
B. Miễn nhiễm 100% với Nhiễu Điện Từ (EMI) và Suy hao cực thấp (Độ tin cậy cực cao, cho phép truyền Terabits/s vượt cự ly HÀNG TRĂM KM mà không cần khuếch đại). Cáp đồng UTP chết đứng ở vạch 100 Mét.
C. Có sẵn mật mã bên trong.
D. Rẻ tiền hơn cáp đồng 100 lần.
*Đáp án: B*
*Giải thích: Ánh sáng trong thuỷ tinh là nhà vô địch truyền dẫn không đối thủ. Nhược điểm duy nhất là đắt tiền và thi công mối hàn quá phức tạp so với cắm cáp RJ45.*

**Câu 64:** Thiết bị Cầu nối (Bridge) và Bộ chuyển mạch (Switch) có quan hệ như thế nào?
A. Không có gì chung.
B. Bridge chạy Tầng Mạng, Switch chạy Tầng Liên kết.
C. Về bản chất, Switch là một cái "Cầu nối Đa Cổng" (Multi-port Bridge). Switch là thế hệ nâng cấp phần cứng (ASIC) của Bridge mềm ngày xưa. Cả 2 đều chuyển mạch L2 dựa trên MAC.
D. Bridge là Wi-Fi.
*Đáp án: C*
*Giải thích: Cầu nối (Bridge) nguyên thủy chỉ có 2 cổng để nối 2 dải cáp dồng trục LAN cổ lỗ sĩ.*

**Câu 65:** Giao thức MAC trong Ethernet (802.3) khi phát hiện đụng độ (Collision) bằng cách nào?
A. Cáp bị nóng lên.
B. Thiết bị phát vươn tai nghe chính dây điện của nó. Nếu Năng lượng Tín hiệu (Điện áp) vọt lên Gấp Đôi mức bình thường, nó biết ngay tín hiệu của mình đã "chập" vào tín hiệu thằng khác trên dây.
C. Bằng báo lỗi DNS.
D. Không kiểm tra được.
*Đáp án: B*
*Giải thích: Việc vừa nói (phát 5V) vừa nghe (thấy sóng đập lại thành 10V) là cơ sở vật lý cho chuẩn CSMA/CD.*

**Câu 66:** Tại sao Giao thức ALOHA thuở sơ khai lại sụp đổ (Hiệu suất truyền đạt < 18%) trên các kênh truyền Broadcast?
A. Nó dùng cáp quá cũ.
B. Giao thức ALOHA (nguyên thủy) quá mù quáng. Cứ có dữ liệu là phát KHÔNG THEO DÕI, KHÔNG NGHE NGÓNG đường truyền (No Carrier Sense). Hàng tá máy cùng phát gây nổ tung đụng độ, băng thông bị nướng sạch vào các gói tin rác hỏng.
C. Vì thiếu IPv6.
D. Chạy bằng tần số âm thanh.
*Đáp án: B*
*Giải thích: Bài học đau đớn từ ĐH Hawaii. Sau này nâng cấp lên CSMA (Phải Hít thở/Nghe ngóng trước khi Hét lên).*

**Câu 67:** Quá trình "Exponential Backoff" (Lùi thì thời gian Cấp số nhân) của CSMA/CD Ethernet được sử dụng ĐỂ LÀM GÌ sau khi xảy ra Đụng độ?
A. Để cắt đứt mạng.
B. Khi 2 máy A và B đụng độ, chúng đều ngừng phát. Nếu cùng mở lại lập tức sẽ đụng tiếp. Chúng sẽ chọn Ngẫu nhiên một số thời gian chờ. Nếu đụng lần 2, biên độ chờ Ngẫu nhiên Tăng Lên GẤP ĐÔI. Giúp dàn đều đám đông ra, tránh chen lấn hẻm hẹp.
C. Tăng tốc độ cáp.
D. Khởi động lại IP.
*Đáp án: B*
*Giải thích: CSMA/CD giải quyết bài toán "kẹt xe nhường đường" cực kỳ dân chủ và tinh tế trên nền mạng ngang hàng tự trị.*

**Câu 68:** Chuẩn 802.1x dùng ở Tầng Liên Kết (VLAN/LAN) có tính năng Bảo mật gì đặc sắc cho Mạng Doanh Nghiệp?
A. Mã hóa nội dung Web HTTP.
B. Quản lý việc Xác thực Cổng cắm (Port-based Authentication). Khi bạn cắm dây LAN vào tường, Switch L2 sẽ CHẶN CỔNG đó lại, yêu cầu Máy bạn phải Trình Tài khoản (User/Pass) lên Server (RADIUS). Đúng người thì Cổng LAN mới mở ra cấp IP.
C. Đánh chặn Virus Trojan.
D. Phân phát IP cho Khách hàng.
*Đáp án: B*
*Giải thích: Chống lại việc Hacker trà trộn vào văn phòng mang laptop cắm trộm dây mạng để moi dữ liệu nội bộ.*

**Câu 69:** Công nghệ "Power over Ethernet" (PoE - Cấp nguồn qua cáp mạng) chạy ở Lớp VẬT LÝ lợi dụng điều gì?
A. Mạng 4G.
B. Bơm Dòng điện một chiều (DC) Công suất thấp chạy trên chính 4 cặp dây đồng xoắn của cáp UTP (Cùng lúc với tín hiệu Dữ liệu tần số cao) để CHẠY/CẤP NGUỒN cho Camera IP, Điện thoại Bàn, hoặc Cục phát Wi-Fi (AP) mà không cần đi kéo dây cắm điện lưới riêng 220V.
C. Truyền mạng qua điện lưới.
D. Cáp quang điện.
*Đáp án: B*
*Giải thích: Sự kết hợp hoàn hảo Tầng 1. Switch PoE đắt tiền hơn nhưng tiết kiệm cả mớ tiền kéo ống gen điện thi công cho các kỹ sư toà nhà.*

**Câu 70:** Tầng liên kết dữ liệu "Data Link" (Layer 2) trong chuẩn IEEE 802 được chẻ nhỏ ra thành hai Tiểu tầng (Sublayers) quan trọng nào?
A. TCP và UDP.
B. IP và MAC.
C. LLC (Logical Link Control - Giao tiếp với lớp Mạng, đồng bộ chuẩn hóa khung Frame) và MAC (Media Access Control - Giao tiếp với phần cứng, điều khiển nhường đường).
D. Physical và Network.
*Đáp án: C*
*Giải thích: Việc chia đôi giúp Phần mềm L3 (IP) ở trên chỉ làm việc với 1 chuẩn LLC thống nhất, trong khi bên dưới MAC có thể thả nổi cho Cáp đồng (802.3) hay Wi-Fi (802.11) thay đổi tùy thích.*

**Câu 71:** Tín hiệu "Inter-Frame Gap" (Khoảng cách giữa các Frame) tối thiểu được bắt buộc trên cáp Ethernet (ví dụ chuẩn 96 bit-times) nhằm mục đích gì?
A. Để làm chậm mạng xuống thu phí.
B. Để Router có thời gian tra IP.
C. Cho phép thiết bị NHẬN (Receiver) có một khoảng TRỐNG THỜI GIAN NHỎ NHOI "nghỉ xả hơi" để làm sạch Bộ đệm Nhận (Receive Buffer), xử lý phần cứng Frame vừa chui vào trước khi bị cái Frame tiếp theo dội tới tấp vào mặt.
D. Tránh nhiễu điện từ.
*Đáp án: C*
*Giải thích: Ở Tốc độ 1 Gbps, 2 Frame dính liền nhau có thể làm treo Chip xử lý mạng. Khoảng nghỉ ngắt quãng vật lý (Gap) là cứu cánh ở cấp độ vi mạch.*

**Câu 72:** Một bộ Hub 10-port (Tầng 1) và một Switch 10-port (Tầng 2). Thiết bị nào cung cấp BĂNG THÔNG TỔNG (Aggregate Bandwidth) cao hơn trên lý thuyết?
A. Hub
B. Bằng nhau.
C. Switch cung cấp cao hơn gấp 10 LẦN. Vì 10 Port của Hub chia sẻ chung 1 cái Ống Nước 100Mbps. Còn Switch 10 Port là 10 cái Ống Nước ĐỘC LẬP (Mỗi ống 100Mbps), tổng năng lực chuyển mạch nội bộ là 1Gbps.
D. Hub mạnh hơn vì không tốn RAM.
*Đáp án: C*
*Giải thích: Đây là lý do Hub tuyệt chủng. Hub là ngã tư không đèn đỏ. Switch là mạng lưới cầu vượt đa tầng.*

**Câu 73:** Công nghệ "Cut-Through Switching" (Chuyển mạch Cắt ngang) trên các Switch cao cấp hoạt động như thế nào so với Store-and-Forward?
A. Nó dùng kéo cắt dây.
B. Nó CHỈ ĐỌC 6 byte đầu tiên (Địa chỉ MAC Đích) của cái Frame đang chạy dở vào Cổng. Tra bảng MAC xong, nó XẢ LỖ BƠM NGAY phần đầu Frame đó chạy ra Cổng Đích LẬP TỨC (Dù phần Đuôi Frame vẫn chưa nhận xong). Giảm độ trễ chuyển mạch xuống mức vi mô (micro-second).
C. Tắt cổng khi tràn.
D. Đọc hết IP rồi mới đẩy đi.
*Đáp án: B*
*Giải thích: Đánh đổi lại, Cut-through có thể Vô ý Chuyển tiếp cả các Frame bị lỗi rác (Vì chưa nhận đến phần đuôi FCS để kiểm tra lỗi đã bơm đi mất rồi).*

**Câu 74:** Lệnh `arp -a` trên Hệ điều hành Windows cung cấp thông tin gì cho người sử dụng?
A. Mật khẩu Wi-Fi lưu trong máy.
B. Hiển thị nội dung BẢNG ARP CACHE (Bộ đệm ARP) hiện tại của máy tính, bao gồm danh sách các Cặp (Địa chỉ IP cục bộ <-> Địa chỉ MAC phần cứng) mà máy tính đã Lén học được trong vài phút qua trên mạng LAN.
C. Danh sách các máy chủ DNS.
D. Tốc độ cáp hiện tại.
*Đáp án: B*
*Giải thích: Nếu bạn ping IP 192.168.1.10. Bạn gõ `arp -a` sẽ thấy xuất hiện cái Dòng chữ `192.168.1.10 --- 00-11-22-33-44-55` trong máy bạn.*

**Câu 75:** Trong môi trường Data Center Ảo hóa, các Máy ảo (Virtual Machines) cắm chung vào một "vSwitch" (Switch Ảo bằng phần mềm của VmWare/HyperV). Giao thức Tầng 2 (như MAC/ARP) có chạy qua Switch Ảo này không?
A. Hoàn toàn Không.
B. Chạy qua UDP.
C. Hoàn toàn Có. Switch ảo chạy trong RAM mô phỏng HOÀN HẢO Y HỆT 100% Hành vi của Switch Vật lý Lớp 2 (Học MAC, Chuyển tiếp, Chặn Broadcast). Các Máy ảo vẫn gọi ARP nhau và dùng MAC để liên lạc trong LAN Ảo.
D. Dùng TCP giả lập.
*Đáp án: C*
*Giải thích: Sự ảo hóa vĩ đại giúp hợp nhất Hàng ngàn mạng cáp rườm rà thành các dòng Code bằng C/C++ chạy mượt mà trên bộ nhớ RAM Máy chủ.*

**Câu 76:** Ứng dụng "VLAN Trunking Protocol" (VTP) của hãng Cisco giải quyết nỗi khổ gì của Quản trị viên Mạng LAN?
A. Cắm cáp sai cổng.
B. Virus phá ổ cứng.
C. Khi công ty có 50 cái Switch, thay vì phải Login vào từng Switch một để gõ lệnh TẠO MỚI VLAN 10 bằng tay 50 lần. Quản trị viên chỉ cấu hình VLAN 10 trên Switch Gốc (Server), giao thức VTP tự động rải lệnh Cập nhật Đồng bộ VLAN đó cho 49 Switch còn lại.
D. Xin cấp IP tĩnh.
*Đáp án: C*
*Giải thích: VTP là vũ khí tự động hóa Lớp 2 cực mạnh nhưng cũng rất nguy hiểm (Nếu cắm nhầm Switch rác có VTP Revision cao hơn, nó sẽ đè bẹp xóa sạch cấu hình VLAN mạng lõi của toàn cơ quan).*

**Câu 77:** Định dạng Địa chỉ MAC được HĐH biểu diễn dạng hệ Hexa: `00:1A:2B:3C:4D:5E`. OUI (Mã Công ty) chiếm phần nào?
A. Toàn bộ.
B. Bị ẩn đi.
C. 3 Byte đầu tiên (24 bit) từ trái sang phải (`00:1A:2B`). Bằng cách tra CSDL IEEE, bạn biết ngay cái Card mạng đó do Apple hay Asus hay Intel sản xuất.
D. Chứa ở 3 Byte cuối.
*Đáp án: C*
*Giải thích: Quản trị mạng thường dùng OUI để chặn tự động tất cả các thiết bị "Lạ" có hãng sản xuất không thuộc danh mục Công ty mua sắm.*

**Câu 78:** Giao thức "Link Aggregation" (Gộp đường truyền / LACP 802.3ad / EtherChannel) làm nhiệm vụ gì ở Tầng Liên Kết?
A. Chia cáp làm 2 đường nhỏ.
B. Bó 2 sợi cáp quang 1Gbps nối giữa 2 Switch lại THÀNH MỘT SỢI CÁP ẢO SIÊU TO KHỔNG LỒ có Băng thông 2Gbps. Giúp Tăng tốc độ và Tạo dự phòng ngầm (Đứt 1 dây thì băng thông giảm chứ kết nối Logic L2 không bị sập).
C. Kéo cáp dài thêm 100m.
D. Khóa chặn virus cổng LAN.
*Đáp án: B*
*Giải thích: Nếu không có Gộp đường truyền (EtherChannel), khi bạn cắm 2 sợi cáp giữa 2 Switch, giao thức Spanning Tree (STP) sẽ LẬP TỨC KHÓA BỎ 1 SỢI (để chống Loop bão Broadcast). Phí phạm 1 sợi dây.*

**Câu 79:** Tại sao giao thức ARP lại tiềm ẩn một LỖ HỔNG LỚN cho an ninh mạng LAN?
A. Nó chậm chạp gây giật mạng.
B. ARP KHÔNG CÓ TRẠNG THÁI (Stateless). Máy tính có thể NHẬN và LƯU TRỮ VÀO BẢNG ARP một "Gói Phản hồi ARP Reply" (với MAC giả của Hacker) MẶC DÙ MÁY TÍNH CHƯA HỀ GỬI LỜI HỎI ARP NÀO. Máy tính ngây thơ cập nhật đè MAC cũ, đưa đầu vào rọ.
C. Nó mã hóa bằng pass yếu.
D. Chặn tường lửa.
*Đáp án: B*
*Giải thích: Hành vi "Tin người lạ mù quáng" (Gratuitous ARP) này khiến mạng LAN nội bộ mong manh như trò chơi trẻ con trước công cụ ARP Spoofing như Netcut, Ettercap.*

**Câu 80:** "Half-Duplex" (Bán song công) trên các thẻ mạng cổ lỗ sĩ thường yêu cầu phải chạy kèm giao thức gì để chống hỗn loạn?
A. DNS
B. TCP
C. CSMA/CD. Nếu chạy Full-Duplex (Mỗi chiều Gửi/Nhận chạy riêng biệt trên các cặp lõi dây độc lập), thì sự Đụng độ (Collision) bị TRIỆT TIÊU TOÀN TẬP, Lúc đó Giao thức MAC CSMA/CD bị VÔ HIỆU HÓA vì thừa thãi.
D. UDP
*Đáp án: C*
*Giải thích: Ngày nay cắm cáp quang hoặc cáp đồng CAT6 vào Switch đều là Full-Duplex. Cơ chế chống đụng độ Tầng 2 đã chìm vào sách Lịch sử.*

**Câu 81:** "VLAN Tag" (Nhãn VLAN chuẩn 802.1Q) được CHÈN VÀO vị trí nào của Khung Ethernet (Ethernet Frame)?
A. Đính kèm ở Cuối (Trailer FCS).
B. Đè lên MAC Nguồn.
C. Bị "Nhồi" Cắt Ngang vào CHÍNH GIỮA phần Header Lớp 2. Nằm ngay sau phần Địa chỉ MAC (Nguồn/Đích) và ngay trước phần Kiểu dữ liệu (Type). Frame bị phình dài thêm 4 Bytes (Từ 1518 lên 1522 Bytes).
D. Gắn vào IP Header.
*Đáp án: C*
*Giải thích: Mọi Switch khi xử lý Frame đều bị bắt buộc đọc 12 Byte đầu tiên (MAC Đích + MAC Nguồn). Ngay sau đó nếu nó thấy Type = 0x8100, nó biết NGAY ĐÂY LÀ GÓI TIN ĐÃ BỊ DÁN NHÃN VLAN (Chỉ được phép đi vào các cổng Trunk).*

**Câu 82:** Thuật toán nào của Switch xử lý Bão Broadcast / Loop Tầng 2 tốt nhất theo chuẩn IEEE?
A. Routing RIP.
B. BGP.
C. RSTP (Rapid Spanning Tree Protocol - 802.1w) hoặc MSTP. Phiên bản "Nhanh" (Rapid) giải quyết vấn đề Hội tụ lại đường đi (Từ Khóa chặn chuyển sang Mở thông cổng) cực nhanh (Vài mili-giây) khi cáp chính bị đứt, thay vì ngồi Mất mạng đợi Hội tụ chậm 50 giây như STP nguyên bản (802.1d).
D. DHCP.
*Đáp án: C*
*Giải thích: Trong Data Center ngân hàng, mạng đứt 50 giây là hàng triệu giao dịch bị huỷ. Giao thức Tầng 2 cũng phải liên tục tiến hoá vươn tới sự hoàn mỹ về Tốc độ Hội tụ (Convergence time).*

**Câu 83:** Một "Default VLAN" (VLAN gốc) trên cấu hình gốc của hầu hết Switch Cisco là VLAN số mấy?
A. VLAN 0
B. VLAN 1. Tất cả các Cổng khi xuất xưởng chưa cấu hình gì đều bị nhốt vào một rọ VLAN 1. Chúng thông nhau như 1 Hub khổng lồ. Việc đầu tiên của Admin khi bảo mật mạng là tống các máy ra khỏi VLAN 1 và vứt bỏ nó.
C. VLAN 100
D. VLAN 9999
*Đáp án: B*
*Giải thích: Lỗ hổng lớn nếu mua Switch về cắm dùng luôn (Plug and Play) mà không cấu hình phân vùng (Segmentation).*

**Câu 84:** Nếu Router nhận gói IP ở Cổng WAN từ Mạng Mỹ về Mạng VN. Nó đẩy gói IP đó xuống Tầng Liên Kết (Cáp LAN) để ném vào Máy chủ Web nội bộ. Quá trình đó gọi là:
A. Mã hóa.
B. Encapsulation (Đóng gói). Gói L3 (IP) được đút vào vỏ L2 (Frame Ethernet) với Cổng MAC nguồn là MAC Của Router Nội Bộ, và MAC Đích là MAC Của Máy Chủ Web. Tầng L2 không hề biết gói IP bên trong đã đi nửa vòng trái đất.
C. Phân đoạn Segment.
D. Phân giải DNS.
*Đáp án: B*
*Giải thích: Lệnh "bơm" vào dây vật lý phải khoác chiếc áo giáp Frame L2.*

**Câu 85:** Mạng LAN không dây (WLAN / 802.11 Wi-Fi) khác với LAN có dây (Ethernet 802.3) ở đặc điểm Tầng 2 nào?
A. Wi-Fi không có MAC.
B. Frame Wi-Fi bọc 4 Địa chỉ MAC (Chứ không phải 2 như cáp đồng). Nó cần phân biệt "Nguồn Gốc (Laptop), Đích Cuối (Điện Thoại), Trạm Phát đi (AP 1), Trạm Phát đến (AP 2)" để phục vụ định tuyến vô tuyến cục bộ qua nhiều Trạm trung gian (Mesh/WDS).
C. Wi-Fi dùng IP tầng 2.
D. Ethernet có 4 MAC.
*Đáp án: B*
*Giải thích: Sự phức tạp của Môi trường không khí bắt Tầng Liên kết phải gồng gánh thêm vai trò Dẫn Đường (Routing nhẹ) giữa các Trạm phát sóng (Access Point).*

**Câu 86:** Mạng di động Tế Bào (4G/LTE) sử dụng Kiến trúc Đa truy nhập Phương tiện (MAC) nào phức tạp và ưu việt hơn hẳn CSMA của Wi-Fi?
A. Rút cáp.
B. Phân bổ rác rải rác ngẫu nhiên.
C. OFDMA (Orthogonal Frequency-Division Multiple Access - Đa truy nhập phân chia Tần số Trực giao). Chia một Dải sóng rộng thành Hàng ngàn Làn sóng (Sóng mang phụ) cực hẹp đặt sát sạt nhau. Trạm phát (eNodeB) là Vua, cấp phát từng làn sóng này cho hàng ngàn điện thoại riêng biệt theo Mili-giây, tuyệt đối KHÔNG xảy ra XUNG ĐỘT (Collision).
D. Truyền âm thanh siêu âm.
*Đáp án: C*
*Giải thích: Wi-Fi là đám đông Hét vào Không gian (Cạnh tranh vô tổ chức CSMA/CA). 4G/5G là Quân đội xếp hàng (Được cấp Lệnh/Slot tần số rõ ràng bằng OFDMA), do đó 4G/5G rất ổn định ở nơi đông người (SVĐ).*

**Câu 87:** Switch (Bộ chuyển mạch) được đánh giá năng lực phần cứng qua chỉ số "Switching Capacity" (Băng thông Backplane). Nếu một Switch có 24 Cổng Gigabit (1Gbps). Băng thông Backplane "Non-blocking" (Không nghẽn cự tuyệt) lý tưởng tối thiểu phải là bao nhiêu để Switch cân hết 24 cổng tải tối đa 2 chiều cùng lúc (Full-duplex)?
A. 24 Gbps.
B. 10 Gbps.
C. 48 Gbps. (24 cổng x 1 Gbps (Tải) + 24 cổng x 1 Gbps (Up) = 48 Gbps chạy trong bụng mạch phần cứng).
D. 100 Mbps.
*Đáp án: C*
*Giải thích: Nếu Switch dỏm (hàng rẻ tiền) ghi "24 cổng 1G" nhưng Backplane chip trong bụng chỉ chạy được "10Gbps". Thì khi cả cơ quan cắm 24 máy tính tải File cực hạn, Switch sẽ nghẽn mạch nội bộ và rớt gói (Drop L2).*

**Câu 88:** "Jumbo Frames" trong mạng Ethernet L2 có kích thước lớn hơn 1500 byte (có thể lên 9000 bytes) được áp dụng tại môi trường nào?
A. Cáp đồng điện thoại ADSL.
B. Wi-Fi Công cộng.
C. Hệ thống Máy chủ Data Center Mạng SAN (Storage Area Network). Việc đẩy cái thùng xe tải to gấp 6 lần (9000 bytes) giúp Máy chủ đỡ mỏi tay băm nhỏ dữ liệu (TCP Segmentation), giảm 80% xung nhịp hao phí CPU để Máy chủ tập trung làm Siêu máy tính tính toán.
D. Vệ tinh ngoài vũ trụ.
*Đáp án: C*
*Giải thích: Một ví dụ điển hình về việc tối ưu Tầng 2 giúp Hỗ trợ giảm tải cho Tầng 4 (TCP).*

**Câu 89:** Tại Tầng Liên kết, làm sao Frame "Bắt đầu" (Start) và "Kết thúc" (End) được đánh dấu trong Dòng bit Nhị phân tuôn chảy trên dây cáp?
A. Dùng mật khẩu ASCII.
B. Cắm điện / Tắt điện.
C. Kỹ thuật "Bit Stuffing / Byte Stuffing" (Chèn bit/byte cờ). Người ta quy ước một Chuỗi Bit Đặc Biệt (Ví dụ `01111110` HDLC) làm Cờ (Flag). Cắm 1 cờ ở Đầu, 1 cờ ở Đuôi. Nếu trong ruột Payload Data vô tình xuất hiện một chuỗi giống hệt Cờ, Tầng Liên kết tự động CHÈN THÊM một Bit rác `0` vào giữa để HĐH Đích không nhầm là Kết thúc Frame. HĐH Đích sẽ tự xóa Bit rác đi.
D. Dùng TCP Checksum.
*Đáp án: C*
*Giải thích: Cách mạng Kỹ thuật số L1-L2. Nó giải bài toán: "Làm sao Máy biết Đâu là Data, Đâu là Tín hiệu Dừng" bằng chính bản thân ngôn ngữ Nhị phân.*

**Câu 90:** Giao thức Liên kết Tầng 2 nào đã Thống trị tuyệt đối và Bức tử hầu hết các hệ thống Mạng Cục bộ (LAN) cổ điển khác (như Token Ring của IBM hay FDDI của Viễn thông)?
A. Wi-Fi.
B. Ethernet (IEEE 802.3).
C. USB cáp mạng.
D. IPsec.
*Đáp án: B*
*Giải thích: Ethernet chiến thắng vì nó ĐƠN GIẢN, RẺ TIỀN, và có khả năng tương thích ngược (Backward Compatible) không tưởng (Từ 10Mbps cáp đồng trục năm 1980 đến 400Gbps Cáp quang năm nay đều chung 1 Cấu trúc Frame).*

**Câu 91:** Để bảo vệ tính bảo mật nội bộ trong Switch Layer 2, tính năng "Port Security" (Bảo mật cổng) được cấu hình trên cổng của Switch nhằm mục đích:
A. Mã hóa nội dung HTTP.
B. Chỉ cho phép DUY NHẤT một (hoặc vài) Địa chỉ MAC cụ thể được phép cắm vào Cổng vật lý đó. Nếu kẻ lạ rút cáp cắm laptop vào (mang MAC lạ), Switch lập tức KHÓA CỔNG (Shutdown) bằng phần cứng ngay lập tức.
C. Đổi IP liên tục.
D. Biến Switch thành Hub.
*Đáp án: B*
*Giải thích: Tính năng cứng rắn nhất ở Lớp 2 để chống sự xâm nhập từ người bên trong tòa nhà (Ví dụ: khách đến chơi văn phòng rút cáp mạng của máy in cắm vào máy mình để tải dữ liệu).*

**Câu 92:** Một nhược điểm của công nghệ Wi-Fi 2.4 GHz so với 5 GHz là hiện tượng "Nhiễu Đồng Kênh" (Co-channel Interference) xảy ra khi nào?
A. Khi sóng Wi-Fi bị tắc trong cáp đồng.
B. Băng tần 2.4 GHz quá hẹp (Chỉ có khoảng 11-14 Kênh nhỏ), và các Kênh này BỊ CHỒNG LẤN lên nhau (Ví dụ Kênh 1 bị đè một phần bởi Kênh 2, 3). Khi nhà kế bên dùng Kênh 1, nhà bạn dùng Kênh 2, hai sóng sẽ đâm chéo làm giảm thê thảm Băng thông của nhau.
C. Đăng nhập nhầm pass.
D. Sóng Wi-Fi bị tường hấp thụ.
*Đáp án: B*
*Giải thích: Nguyên lý thiết lập Wi-Fi cơ bản: Chỉ có 3 Kênh (1, 6, 11) trên băng tần 2.4GHz là HOÀN TOÀN TÁCH BIỆT (Non-overlapping).*

**Câu 93:** Một "Trạm phát gốc" (Base Station) trong Mạng Di động (như 4G eNodeB) khác với cục phát Wi-Fi (AP) ở nhà về Khả năng Quản lý Phương tiện như thế nào?
A. Trạm gốc dùng dây cáp.
B. Wi-Fi là một "Sân chơi vô chủ", mọi thiết bị phải tự gào thét tranh giành (CSMA). Trạm Di động 4G là một "Tổng tư lệnh", nó LÊN LỊCH CHÍNH XÁC đến từng mili-giây (Scheduling) cho mỗi điện thoại khi nào được Phát, khi nào được Nghe (TDMA/OFDMA). Không có xung đột rác.
C. Trạm gốc chỉ tải Web.
D. Không khác gì.
*Đáp án: B*
*Giải thích: Thiết kế Cellular sinh ra để phục vụ Hàng triệu người đi xe tốc độ cao không bị rớt mạch, nên cấu trúc Tầng Liên Kết (MAC) của Di động cực kỳ độc tài và tinh vi.*

**Câu 94:** Kỹ thuật "Forward Error Correction" (FEC - Sửa lỗi tiến) sử dụng phổ biến trong Vệ tinh, Wi-Fi 4G khác gì với cơ chế Sửa lỗi của TCP?
A. Mã hóa virus mạng.
B. TCP sửa lỗi bằng cách Yêu cầu Truyền Lại toàn bộ cục dữ liệu (Tốn thời gian RTT chờ đợi). FEC thì KHÔNG TRUYỀN LẠI. Nó đính kèm các Mã Sửa Lỗi Toán học cực mạnh ĐI CÙNG TÍN HIỆU NGAY TỪ ĐẦU, Máy nhận dùng Toán học tự khôi phục lại các bit rách nát mà không phải hỏi lại.
C. Yêu cầu cáp quang lõi.
D. Biến TCP thành ARP.
*Đáp án: B*
*Giải thích: Vệ tinh ping mất 500ms. Gửi lại TCP thì độ trễ vọt lên 1000ms. FEC hi sinh 20% dung lượng băng thông để "nhồi" mã sửa sai, bù lại Giảm Jitter và Cứu sống mạch dữ liệu ngay tức thì ở Tầng Vật lý/Liên Kết.*

**Câu 95:** Trong Wi-Fi, khung Frame mang tên "Beacon" (Bản tin Báo hiệu) được Access Point (Cục phát) phát ra rải rác mỗi 100ms nhằm:
A. Tắt điện điện thoại.
B. Chứa Tên của Wi-Fi (SSID - Service Set Identifier), Tốc độ hỗ trợ, và Chuẩn bảo mật. Để Điện thoại của bạn mở lên "Quét" (Scan) không khí sẽ hiện ra danh sách các Wi-Fi xung quanh để chọn kết nối.
C. Thay thế IP.
D. Mở Port 80.
*Đáp án: B*
*Giải thích: Bạn có thể vào cài đặt Router tích vào ô "Hide SSID" (Ẩn Wi-Fi). Lập tức Router sẽ ngưng rêu rao tên nó trong Beacon. Người khác sẽ không thấy Wi-Fi nhà bạn trên điện thoại.*

**Câu 96:** Sự kiện "Handover" (Chuyển giao) của điện thoại ở mạng Di động (ví dụ 4G) khi bạn lái xe từ Cột Sóng A sang Cột Sóng B. Chức năng Lớp 2 đóng vai trò gì?
A. Khởi động lại hệ điều hành Android.
B. Chặn cuộc gọi.
C. Điện thoại và Cột sóng liên tục đo Cường độ tín hiệu vô tuyến (RSRP/RSRQ). Khi tín hiệu Cột A yếu, Cột B mạnh lên, Mạng lõi (Control plane) điều hướng Luồng Dữ liệu ảo (Tunnel L2) của bạn CẮT TỪ CỘT A CẮM SANG CỘT B chỉ trong vài mili-giây. Bạn tải phim không đứt.
D. Chuyển điện thoại về 2G.
*Đáp án: C*
*Giải thích: Đây là sự vĩ đại của Mạng di động (Mobility) so với Mạng cáp quang. Mọi thứ được định tuyến bẻ lái (Rerouting) ngay tại Lớp Liên kết mà Máy tính (Lớp 4 TCP) không hề hay biết.*

**Câu 97:** Kỹ thuật "Carrier Aggregation" (Ghép sóng mang) trong Mạng 4G LTE-A / 5G có ý nghĩa gì đối với Tầng Liên kết Dữ liệu (MAC)?
A. Buộc phải cắm dây vào điện thoại.
B. Nén tín hiệu âm thanh thành văn bản.
C. Tổng hợp (Gộp) NHIỀU dải tần số vô tuyến RỜI RẠC (Ví dụ băng tần 1800Mhz và băng tần 2600Mhz) vào làm MỘT ỐNG DẪN ẢO SIÊU TO (Virtual Pipe) duy nhất tại Lớp MAC. Tăng tốc độ download trên điện thoại lên tới hàng Gigabit.
D. Biến đổi Wi-Fi thành 5G.
*Đáp án: C*
*Giải thích: Nó giống như khái niệm "Trunking/Etherchannel gộp 2 dây mạng" của Switch, nhưng thực hiện vô hình bằng Gộp các Dải Sóng Độc Lập ngoài không gian.*

**Câu 98:** Mạng Ethernet chia sẻ dùng kiến trúc dạng "Bus" (như 10BASE2 cáp đồng trục) đã tuyệt diệt vì lý do chí mạng nào ở Lớp Vật lý?
A. Tốn cáp.
B. Không cắm được mạng LAN.
C. Sợi cáp là Một đường ống hở chạy thông từ nhà này sang nhà khác. Nếu ông A ở giữa rút khớp nối (T-connector) hoặc đứt cáp ở giữa, TÍN HIỆU TOÀN MẠNG DỘI NGƯỢC (Reflection) gây nát toàn bộ mạng của tất cả những người trên Bus. Tính chịu lỗi (Fault tolerance) bằng 0.
D. Cáp chạy bằng pin.
*Đáp án: C*
*Giải thích: Mô hình Star (Sao) có Switch ở giữa lên ngôi. Bạn rút dây máy bạn thì kệ bạn, Switch tự ngắt port của bạn, cả cơ quan vẫn làm việc bình thường.*

**Câu 99:** Địa chỉ MAC `FF:FF:FF:FF:FF:FF` được sử dụng để Quảng bá (Broadcast L2) cho Toàn miền. Có địa chỉ MAC Multicast riêng không?
A. Không có MAC Multicast.
B. Chỉ dùng MAC của Router làm Multicast.
C. CÓ. Chuẩn quy định MAC Multicast bắt đầu bằng chuỗi 24-bit đặc biệt (ví dụ `01:00:5E` cho IPv4 Multicast). Nó giúp Cạc Mạng (Phần cứng) nhận biết đây là gói tin Đa hướng. Nếu Máy tính không Đăng ký tham gia nhóm xem Tivi (Multicast group), Cạc mạng CỨNG SẼ TỰ VỨT gói tin đó đi NGAY LẬP TỨC để cứu RAM và CPU khỏi bị đánh thức.
D. Dùng IP làm MAC.
*Đáp án: C*
*Giải thích: Sự can thiệp thông minh của Phần cứng (Hardware Filter). Trình điều khiển (NIC Driver) dặn con Chip: "Tao không xem Tivi. Nếu mày thấy gói tin mang MAC có chữ 01:00:5E, mày vứt luôn ở ngoài cho tao, đừng làm tao tỉnh ngủ".*

**Câu 100:** Cuối cùng, Tầng Vật Lý (Physical Layer - Layer 1) làm nhiệm vụ gì cho Tầng Liên Kết (Data Link - Layer 2)?
A. Tìm đường OSPF.
B. Mã hóa SSL mật khẩu mạng.
C. Nhận các Khung (Frame) chứa dãy bit 0 và 1 từ Tầng 2, rồi "Biến hình" (Modulation/Điều chế) chúng thành Tín hiệu Vật chất (Mức điện áp cao/thấp trên cáp đồng, hay Chớp/Tắt trên cáp quang, hay Biên độ/Pha sóng điện từ trên không gian) đẩy ra môi trường thực. Và thao tác ngược lại ở đầu thu.
D. Chỉ huy Router định tuyến.
*Đáp án: C*
*Giải thích: Tầng 1 là Nô lệ của máy tính. Nó không quan tâm Data chứa Game hay chứa Virus. Nó chỉ nhìn thấy chuỗi Nhị phân dài vô tận và nhắm mắt Biến Đổi thành Dòng Điện tuôn chảy.*

**Câu 101:** Chuẩn kỹ thuật Ethernet (IEEE 802.3) ban đầu được thiết kế để truyền tải dữ liệu trên cáp đồng trục (Coaxial). Ngày nay nó chủ yếu sử dụng loại cáp gì?
A. Cáp USB.
B. Cáp HDMI.
C. Cáp đồng xoắn đôi (Twisted Pair - UTP) với các cổng cắm RJ-45 và Cáp quang học (Fiber Optic) cho môi trường công nghiệp lõi.
D. Truyền qua sóng vệ tinh.
*Đáp án: C*
*Giải thích: UTP rẻ, mềm dẻo, đi dây dễ dàng đã hoàn toàn lật đổ đế chế cáp đồng trục to, cứng và dễ hỏng mạng cổ điển.*

**Câu 102:** "CRC" (Cyclic Redundancy Check) ở đuôi (Trailer) của một Khung Frame bị sai khác so với kết quả do Switch tính toán lại. Hành động tức thì của Switch là:
A. Tự sửa lại cho đúng.
B. Gửi trả lại bằng TCP.
C. Lặng lẽ Loại bỏ (Drop/Discard) Frame đó ngay lập tức, không thèm báo cáo (No ACK) với máy gửi vì bản chất Ethernet L2 không có tính năng truyền lại tin cậy (Unreliable).
D. Truyền lại qua Wi-Fi.
*Đáp án: C*
*Giải thích: Cực kì lạnh lùng. Rách vỏ là vứt sọt rác, kệ cho Tầng TCP bên trên lo phần than vãn xin gửi lại.*

**Câu 103:** Thuật toán Spanning Tree Protocol (STP) mất bao lâu để "Hội tụ" (Đưa mạng từ trạng thái Đứt cáp sang Trạng thái Ổn định bình thường)?
A. Khoảng 0.1 Giây.
B. Thường mất khoảng 30 đến 50 Giây (Vượt qua các giai đoạn Listening, Learning rồi mới Forwarding). Trong nửa phút đó Mạng Công Ty hoàn toàn tê liệt. Do vậy mới có sự ra đời của RSTP thay thế.
C. Mất 1 phút rưỡi.
D. Nhanh tức thì.
*Đáp án: B*
*Giải thích: Chậm chạp nhưng Đảm bảo an toàn không xảy ra Bão Vòng Lặp. 50s trong giới IT là sự chờ đợi dài như 1 thế kỷ.*

**Câu 104:** Lệnh `ipconfig /all` trên Windows (hoặc `ifconfig` Linux) cung cấp địa chỉ MAC dưới nhãn "Physical Address". MAC này có thể bị đổi bởi người dùng không?
A. Tuyệt đối không vì nó khắc cứng.
B. Về mặt Vật lý trên Chip Mạng (NIC ROM) thì KHÔNG THỂ. Tuy nhiên, về mặt Phần mềm (Software/Driver), Hệ điều hành cho phép "Che Giấu" (MAC Spoofing/Cloning) bằng cách viết đè một chuỗi MAC ảo giả mạo lên Khung L2 khi xuất dữ liệu ra cáp, đánh lừa mạng LAN dễ dàng.
C. Đổi được bằng mật khẩu.
D. Phải gọi điện cho nhà sản xuất.
*Đáp án: B*
*Giải thích: Đặc tính này sinh ra tính năng "MAC Randomization" trên điện thoại để chống theo dõi khi vào Wi-Fi quán cafe.*

**Câu 105:** Kỹ thuật "VLAN Tagging" 802.1Q chèn một chuỗi 4 Byte vào Khung. Trường VLAN ID (VID) trong đó chiếm 12 bit. Vậy một Switch có khả năng phân tách TỐI ĐA theo lý thuyết bao nhiêu VLAN?
A. 100 VLAN.
B. 256 VLAN.
C. 4096 VLAN ($2^{12}$). (Từ số 0 đến 4095, trừ 2 số đặc biệt).
D. Không giới hạn.
*Đáp án: C*
*Giải thích: Đây là một giới hạn lớn đối với các Cloud Data Center khổng lồ khi có hàng vạn máy chủ. Công nghệ VXLAN (Virtual Extensible LAN) ra đời gỡ giới hạn L2 này đẩy lên 16 Triệu VLAN.*

**Câu 106:** Switch Store-and-Forward (Lưu trữ và Chuyển tiếp) có một lợi thế TUYỆT ĐỐI HƠN hẳn Switch Cut-Through là gì?
A. Tốc độ chuyển mạch siêu âm.
B. Nó NHẬN VÀ ĐỌC HẾT TOÀN BỘ FRAME VÀO RAM. Sau đó NÓ KIỂM TRA MÃ CRC FCS (Ở đuôi chót). NẾU SAI -> VỨT. Không bao giờ có chuyện Gói Tin Rác Bị Hỏng lọt ra cổng thứ 2 gây lãng phí Băng thông Mạng Lưới.
C. Cut-through hay lưu RAM.
D. Làm mát cáp quang.
*Đáp án: B*
*Giải thích: Chậm một phần ngàn giây nhưng bù lại Không gian LAN cực kỳ sạch sẽ, không có rác.*

**Câu 107:** Trong Tầng Liên Kết (MAC), thuật ngữ "Collision" (Xung đột/Đụng độ) ngụ ý sự cố ở cấp độ nào?
A. Lỗi phần mềm Virus.
B. Trùng địa chỉ IP nội bộ.
C. Xung đột Điện áp Vật lý. Hai hay nhiều điện áp điện từ trộn lẫn vào nhau trên cùng 1 đoạn cáp hở, biến luồng Byte 0 1 thành Điện Áp Rác Khổng Lồ, làm bộ cảm biến Tầng 1 Máy tính đọc không ra chữ gì, hỏng sạch dữ liệu.
D. Do rút cáp đột ngột.
*Đáp án: C*
*Giải thích: Sóng chập sóng thì tạo ra Sóng Nhiễu. Tín hiệu điện từ không thể nhận dạng được bit nào nữa.*

**Câu 108:** Giao thức Liên kết Tầng 2 nào Chuyên Dụng Trên ĐƯỜNG TRUYỀN DIỆN RỘNG (WAN) Giữa 2 Router Quay Dây Nối Với Nhau?
A. CSMA/CD Wi-Fi.
B. Ethernet 802.3.
C. Giao thức Điểm-Điểm (PPP - Point to Point Protocol) hoặc HDLC. Thiết kế siêu mỏng cho Liên kết Độc Tôn Đường Ngầm Xuyên Lục Địa (Không Cần Địa Chỉ MAC VÌ Không Có Ai Khác Chung Dây Tranh Giành).
D. Giao thức OSPF.
*Đáp án: C*
*Giải thích: LAN dùng Ethernet có MAC. WAN P2P dùng PPP không cần MAC (Vì đường hầm chỉ có Đầu và Đuôi, tống vô ống chắc chắn tự ra đầu bên kia, MAC vô nghĩa).*

**Câu 109:** Trong P2P PPP Protocol (Giao thức Điểm-Điểm), có chèn tính năng Bắt Nhập Mật Khẩu Nào Nổi Tiếng Thời Kéo Dây Quay Số (Dial-up)?
A. WEP WPA2.
B. TLS.
C. Tính năng PAP (Password Authentication Protocol) hoặc CHAP (Challenge Handshake). Khi Modem Gọi Lên Tổng Đài Viễn Thông, Phải Gửi User/Pass Xác Thực. Sai Pass -> Tổng Đài Ngắt Cáp Cúp Mạng Ngay Lập Tức Ở Lớp Liên Kết.
D. Khóa RSA Diffie.
*Đáp án: C*
*Giải thích: Đỉnh cao cấu hình PPPoE (PPP over Ethernet) trên Modem Cáp Quang VNPT/FPT nhà bạn hiện nay chính là đang bọc công nghệ Mật khẩu PPP vô Tầng Liên kết để nhà mạng tính cước.*

**Câu 110:** Giao Thức Wi-Fi Sử Dụng Khoảng "DIFS" Để Nhường Đường Gửi Data. Còn Chờ Lời Đáp Lại Xác Nhận (ACK) Thì Máy Phải Chờ Khoảng Cực Ngắn Nào Để Ưu Tiên Cao Hơn Data Mới?
A. RTS Space.
B. CTS.
C. SIFS (Short Inter-Frame Space - Khoảng Không Cực Ngắn). Trạm Đích Nhận Data Xong, Nó Đợi Xíu Bằng SIFS (Tức Là Nó Được Cướp Diễn Đàn Tranh Nói Trước Tất Cả Những Kẻ Đang Nhẫn Nhịn Chờ Bằng DIFS Cực Lâu). Đảm Bảo ACK Trả Về Khẩn Cấp Báo Rằng Dữ Liệu An Toàn Trước Khi Các Máy Khác Cướp Kênh Sóng Phá Hỏng Nhịp.
D. IPsec Tunnel.
*Đáp án: C*
*Giải thích: Nghệ Thuật Ứng Xử Phân Cấp Lịch Sự Rất Logic (ACK Lệnh Nhỏ Nhanh Luôn Quan Trọng Hơn Cục Data Vô Bờ).*

**Câu 111:** Bão Đụng Độ Của Ethernet (CSMA/CD) Có Khả Năng Xảy Ra Dữ Dội Không Kiểm Soát Làm Sập Mạng Nếu Admin Thiết Kế Mạng Lỗi Gì:
A. Tắt IP DHCP Mất Gateway Rớt.
B. Đấu Nối Chuỗi Liên Tiếp QUÁ NHIỀU BỘ HUB (Repeater) Kéo Mạng Quá Xa Khỏi Chuẩn Giới Hạn Cáp Vật Lý Gây Trễ Dòng. Máy A Và B Đang Phát Cách Quá Lâu Chậm Tiếng Trọng Sóng Đụng Nhau Khuya Mới Nhận Biết (Late Collision Vỡ Ngập). Mạch Càng To Bão Càng Nát Lớn Tần Suất Gián Đoạn Cháy Vô Vọng.
C. Khóa Chặn Trống Trơn Sóng Đổ Hết Pass Wi-Fi Ra Thường.
D. Biến L2 Thành UDP Dữ Dội Cắt.
*Đáp án: B*
*Giải thích: Luật 5-4-3 Phế Cổ Từng Khóa Giới Hạn Chiều Rộng Mạng Vòng Ethernet Hub Bọn L1 Cho Ổn Định Xung Lỗi Nhấp Rối Cảm Dụng Trì Sát Tốc Đánh Hết Trống Xéo Đi Ngược Bẫy Tụt Cắt Bập Trạm Đọc.*

**Câu 112:** Tại Sao Ở Đời Máy Phát Cáp 10G/40G Khủng Của Ethernet Không Ai Thèm Xài Giao Thức Chống Xung Đột (CSMA/CD) Nữa:
A. Do Lỗi Mạch.
B. Bởi Nó 100% HOẠT ĐỘNG CHẠY SONG CÔNG TOÀN PHẦN (FULL-DUPLEX) TRÊN CÁC LÕI SỢI CÁP QUANG/ĐỒNG TÁCH BIỆT RỜI ĐƯỜNG GỬI - ĐƯỜNG NHẬN SIÊU TỐC NỘI BỘ VÀ NỐI THẲNG TRỰC TIẾP VỚI CỔNG SWITCH (Point-To-Point Từng Máy). Chẳng Có Sợi Dây Dính Chùm Nào Với Ai Cả Nữa Để Mà Va Đập Đụng Độ Tai Nạn.
C. Giới Tính Của Mạng BGP Dài Ra Phá Nát Sóng Căng Rập.
D. UDP Che Khóa Mạng IP.
*Đáp án: B*
*Giải thích: Đỉnh Của Cấu Trúc Là Đạp Bỏ Những Lỗi Thô Sơ Sân Chơi Cũ Lạc Cấp Lùi Cục Chậm Biển Góp Tiếng Ầm. Thế Giới Mạng Tinh Khiết Sạch Boong Chóp L2 Vụt Cao Tốc Vô Hình Bay Đứt Không 1 Hạt Bụi Đụng Chạm Sóng Sạch Kín Tách Rẽ Mạch Kép Lặn Phun Sóng Điện Chạy Sáng Loáng Vèo Thoát.*

**Câu 113:** Đa Nhập Mạch MIMO Không Dây Lợi Dụng Trò Lừa Hiện Tượng Gì?
A. Hủy Âm Không Có Sự Khúc Xạ Gãy Nhập Sóng Vệ Tinh Kém.
B. HIỆN TƯỢNG ĐA ĐƯỜNG TRUYỀN (Multipath) Bắn Sóng Vô Tường Chắn Sàn Xi Măng Dội Búng Lại Loạn Xạ, Làm Nhiều Sóng Va Đập Bay Tới Cùng Bức Giao Thoa Phá Vỡ (Fading) Thành Mớ Hỗn Độn Nhòe Mờ Ở Chuẩn B G Đời Cũ Cực Khổ Tịt Sóng Góc Kẹt. MIMO Thay Vì Xóa Đi Sợ, Nó Đón Thu Cả 3-4 Tia Loạn Đập Bức Tường Về Rồi Dùng Chíp Toán Vi Xử Ma Trận Ghép Xoắn Cộng Hưởng (Spatial Multiplexing) Hút Gộp Đủ Mọi Tốc Sóng Bay Bắn Đánh Bức Rớt Tốc Vút Cao Gấp Tỷ Lần Phẳng Đường.
C. Máy Tắt Cảm Nén.
D. Biến Sóng Trực Giao Sang Mật Đảo Cấp Thấp Mã TCP.
*Đáp án: B*
*Giải thích: Dấu Ấn Bác Học Của Công Trình Không Dây Cải Tạo Địch Thành Của Mình Góp Sức Chuyển Động Nhân Không Nét Thủng Không Trói Vực Lập Ló Tối Đẩy Sóng Phát Mọi Nơi Bay Dội Kẹt Gập Gẫy Thúc Kéo Nhấn Nhịp Nhịp Độ Mạch Trơn Giọng Cao Tít Ngấm Tận Hốc Sâu Cực Sống Tốt Giữ Vững Tóc.*

**Câu 114:** Chuẩn Mạng Wi-Fi Không Dây (IEEE 802.11) KHÔNG DÙNG THẲNG ĐƯỢC 100% Trên Khung Sườn Mạng Cáp Lõi Của Dân Dụng (Ethernet 802.3) Bắt Buộc Kẻ Đứng Trạm Cục Giao Tiếp Bật Dịch Thuật Giữa Biên Sóng Wi-Fi Nhập Mạng Có Dây Cầm Lệnh MAC Gì Sửa Hồn Điển Bẻ Cong Khung Frame Cầu Nối Rập Kín:
A. Tắt Gói Tín Kích Cỡ Giảm Đầu MAC Lẻ Trống Bó Mã Dịch Thụ Rẽ Sóng Rỗng Xéo Vệt Gập OSPF Đè.
B. Access Point (Bộ Phát Bắt Wi-Fi) ĐÓNG VAI TRÒ TRANSLATOR (Ngôn Ngữ Biên Dịch Viên) L2. Khung Tới Wi-Fi Khép Bọc Mật Mã Bảo Vệ AES Gắn Dán Đội Lệnh RTS/CTS. Trạm Thu Lấy Giấy Gói Đó Giải Mã Chữ Rách Rập Ra Chuẩn Đều Viết Lại Frame Mới Format Ethernet Dán Cộp Đầu Ethernet Header Tuốt Chân Ném Vào Dây Cáp Thùng Switch Để Nhận Rành Đuổi Mở Truy Nhanh Bật Rộng Đi Internet Gửi Server Bình Thường Hoàn Toàn Tắt Biến Lốt Wi-Fi Cũ Lỗi Giữ Nguyên Chớp.
C. Bằng Lệnh IP Mở Rút NAT Cụt Khóa Nhớ RAM Bơm Chìm Nhấp ARP.
D. Không Sửa Đóng IPsec Thay OSPF Kép Cửa Router Rời Chóp Chết Chống IP.
*Đáp án: B*
*Giải thích: Đây Chính Là Cầu Nối Cầu Giấy Hai Thế Giới Khác Nhau Nhưng Tương Đồng (Bridge Translator L2). AP Chạy Tách Nhiệm Cắt Frame Gọt Vỏ Đổi Vỏ Dáng Lưng Để Thiết Bị PC Switch Không Quen Chuẩn Sóng Cũng Nhận Chơi Tốt Frame Đồng Dây Rất Êm Ái Cứu Dẫn Khớp Nhập Thích.*

**Câu 115:** Cơn Ác Mộng Của "Sóng Di Động Tế Bào Sập Mạng Cục Bộ Đông Người Lễ Hội" Thể Hiện Kẽ Hở Cấu Trúc Khối Vô Tuyến:
A. Do Khóa Dây Điện Tụt Nguồn Lõi Áp Pin Trạm Cụt Tắt Sạc Chìm Chậm Trì Mạch Cháy Đột Đảo Khóc IP Rách Mốc Vết Ngàm Cáp Lỏng Mỏng Mật.
B. Căn Bệnh Năng Lực Dung Lượng Hệ Thống Chia Kênh Phức Tạp LTE (Capacity L2 Slicing). MỘT Cột Trạm CHỈ Sở Hữu Một Giải Tần Vô Tuyến Sóng Quá Eo Hẹp Phổ Chừng 20 Mhz Băng. Dù Kỹ Thuật Có Cao (OFDMA Băm Trăm Kênh Trục Nhỏ Từng Mini Giây Giành Giựt Nhau Giữ Trật Tự 1 Trăm Điện Thoại Gọi). Khi 50 Ngàn Sinh Viên Quây Trong SVĐ Kéo Data, Không Còn Kênh Mini Nào Thừa Slot (RBs Cạn Kiệt Nặng Nề Lấp Khe Tắt Vách Rỗng). Tín Hiệu Rớt Đứt Lìa Drop Lệch Nhảy Văng Máy Từ Chối Không Mở Mạng Dù 5 Vạch Sóng Cột Lù Lù Áp Chạm Bóc Nghẽn Cực Sống Nghẽn Ứ.
C. Vì App Facebook Gây Lỗi Mã L7 Phá Quét DNS Dội Ngược Lụt Sập Ping Băm Tát Quật.
D. Dùng Chuyển Mạch UDP Kìm Rỗng TCP Lấp Băng.
*Đáp án: B*
*Giải thích: Tần Số Là Lẽ Sống Băng Bờ Không Khí Tầm Chứa Giới Hạn Cứng. Vô Tuyến Khác Cáp Quang Là Bạn KHÔNG THỂ BỔ SUNG CẮM THÊM 100 SỢI DÂY VÔ TẦN VÔ TÂM CỨU MẠNG BĂNG, TẦN SỐ CỦA ĐẤT NƯỚC LÀ DUY NHẤT. CÁCH DUY NHẤT CỨU ĐÔNG LÀ THÊM VẠN TRẠM SMALL CELL NỐI VỆ TINH PHỤ LÒI GẦN SÁT TẦM CHE.*

**Câu 116:** Khảo Sát Bảng MAC Của Switch Doanh Nghiệp Thường Phải Cập Nhật Thay Đổi Nóng "Gỡ Lọc Rác Aging Lão Hóa Cấp Bách Lẹ Hơn" Giây Bình Thường 5 Phút Rất Nhanh Vì Trường Hợp Sự Cố Nào Xáo Trộn Sóng Mạng Mối Mọt:
A. Sụp Tường Lửa Ngắn Dòng ARP Nhớ IP Khởi Dữ Dập Ping Bức Nhấp Gập Trút.
B. Sự Tác Động Spanning Tree Protocol (STP Cắt Dây Rối Định Cắt Mở Trạm Cấp Đổi Vòng Đảo Lộn Rẽ Cổng Mới Phụ Backup Bật Thông Mạch). Toàn Bộ Địa Chỉ Khách MAC Học Ở Cổng A Trước Đó Đã Sang Trú Đóng Dịch Chuyển Hướng Quẹo Chạy Trào Nhanh Cổng B Bất Thường Dạt Tít Xa. Công Tắc Bắt Buộc Flush (Xóa Trắng Tẩy Lướt Bảng RAM Tức Tốc Vô Hình Xóa Bỏ Kẹt Lỗi) Đổ Trống Sạch Rồi Thu Thu Thập Học Cập Nhật Cấu Trúc Lại Kẻo Dữ Liệu Gọi Khóc Lầm Cửa Tịt Lối Tường Rơi Túi Quẳng Chạy Khống Trọng Quỹ.
C. Ổ Cứng Nổ Tốc Tăng Vệ Tinh Kéo Mã L5 Dồn Sát Cầu Sáng Giữa Dòng Xoắn IP UDP Tĩnh.
D. DNS Tự Ngắt Lỗi Văng Tốc Đụng Độ Nhau Mở Cửa 404 Báo Đáo Hạn Vượt Đích Kính Tắt Tức Hút Dồn Trôi Hư Hại Khét.
*Đáp án: B*
*Giải thích: Tính Ứng Dụng Thiết Kế Ảo Diệu Thay Đổi Định Tuyến LAN Lớp 2 Chống Gãy Đứt Ùn Ứ Hồi Hợp Giảm Thiết Kế Bù Tụ Đổ Bảng Tẩy Nóng Liên Động Khớp Liên Hòa Mạng Trống Hấp Nạp Data Nóng Sang Phụ.*

**Câu 117:** Mạng Điểm Sáng Trực Tuyến PPP Kéo Giữ Liên Lạc Modem Kết IP L3 Truyền Thống, Chống Nghẽn Lọc Check Sát Mạng Rác Gói Đọc Sót Bit Thì Cần "Trailer Dữ Điểm" Gì Đệm Đuôi Phá Kén Chốt Mạch Giống Ai:
A. Tắt Ngắn Băm Gói Nhồi 40 Byte TCP Header Kèm Option Rác Kín Bức Cản Kẹp Nút Cứng Đè Nhận Ức Báo Lụa Kéo Thêm Dây.
B. FCS Mã Lỗi Kép Dây (Frame Check Sequence Chứa Mã Thuật Kéo Dịch Chia Dư CRC Y Hệt Lỗ Chạm Bản Sinh Đôi Với Cấu Trúc Khung Mạch Cứng Dây LAN Ethernet Kẹp Đuôi Dưới Dừng Bảo Đảm Máy Đầu Bên Ráp Lấp Hoàn Hảo Phẳng An Tâm Vớt Bỏ Gói Hư Hỏng Nhòe Loạn Phá Kém Hủy Mắc Nghẹt Mạch). Mạng PPP Có Bọc FCS CRC Kéo Khóa Kiểm Hỏng Trắng Sập Cục Dữ Gọn Cáp Chạm Điện Cứng Xóa Nhầm Lụi Tắt.
C. IPv4 Kẹp Gói IPv6 Kín Vi Mạch Hết IP Nặng Ác Không.
D. IPsec Dán Sóng Tắt Phẳng UDP Giao.
*Đáp án: B*
*Giải thích: Bất Kỳ Tầng Mạng Vận Chuyển Vật Lý Nào L2 Chở Che Dù Có Dây Sóng Trạm LAN WAN BẮT BUỘC ĐỀU PHẢI TRANG BỊ MÃ CRC CUỐI BÀI ĐỂ THANH KIẾM CHẶN LỖI LẬT ĐỔ BIT CỨU TOÀN VẸN MÁY NHẬN KHỎI ĂN TÁP RÁC TỪ SÉT BÃO NHIỄU RỐI.*

**Câu 118:** Đặc Điểm Giao Tiếp Của Giao Thức L2 Cần Sửa Ráp Thiết Kế Frame 802.1Q Bóp Chặn VLAN: Vứt Máy Cũ Không Cập Nhật, Sẽ Nhận Dòng Gói VLAN Đội Lốt Kẻ Gian Thẩm Vô Bắn Nhầm Lỗi Giật Điện Cấm Cửa Vì Nguyên Cớ Gì Khủng:
A. Tên Giao Thức Đổi UDP 0.
B. Cấu Trúc Gói Thẻ Nhãn VLAN ID Nâng Tổng Khối Khung Frame Dài Ra Tối Đa Khủng Nhất Thành 1522 Bytes Vươn Trượt Dài Lố Xé Rào Cản MTU 1518 Bytes Khung Cổ Lỗi Mắc Mạng Khung Cổ Xưa Cứng Rập Kín Khuôn Nhỏ Rập Vỡ Khối Nhầm Frame Quá Cỡ Sai Xóa Dội Sóng Hủy DROP Tắt Báo Khẩn "Giant Frame Bị Vứt Vô Sọt Rác Bức Hỏng Nhắn Không Ai Đọc Bóp Xé Phẳng Biến Sát Khét Lẹt Giao Ức Đứt Vực Sâu Kẹp Dính Nén Lắp Phủi Trượt Rớt Sạch Rỗng Không Hề Xót Thảm Oan Nhục Lớn".
C. Lấp Chập Dây Nhầm Điện.
D. Biến Kẻ Gửi Tắt Router Lạc Ngược Rỗng Trọng Khóa Rìa Kín Lướt Ping Vất Gây Cáp Xóa Rơi Biển Vắng Nhịp Xé.
*Đáp án: B*
*Giải thích: MTU Ethernet Truyền Thống Phải Nâng Cấp Nới Khung Jumbo Cho Phép Trượt Bó Nới Size Dây Cho Chuẩn Tag Mới Xỏ Qua Ráp Tắt Lọt Thẳng Xuyên Mạng Doanh Nghiệp An Bình Hoạt Trơn Rõ Ràng. Tránh Rác Nhầm Khung To Hư Nhựa Tắt Chập. Giữ Định Chuẩn To Lớn Dài Hơi.*

**Câu 119:** Phép Đo Tính Hữu Ích Của 1 Cục Router Nhúng Tay Gán Ngăn Mạng L3 Kết Tầng L2 Liên Lạc Khác Biệt Nào So Cục Tường Lửa Ngăn Máy Ở Phòng Nhân Sự Chặn Nhân Sự Chặt Che Mắt Giữ Máy Cầm LAN Kín Không Rò IP Ra Quầy Lễ Tân Khách Đi Ngang Ngoài Bề Wi-Fi Vứt:
A. Đổ Cáp Vừa Kéo Không Cho Hở ARP Dưới Sóng Kém Nhắn.
B. Mọi Cục L3 Router BẤT KỲ ĐỀU CẮT NGANG THÔNG LIÊN LẠC L2 TRỰC DIỆN SÓNG VẶN (Vứt Bỏ Triệt Tiêu Gói Phát Sóng Ảo Quảng Bá Bão Của FF:FF Broadcast Giữa 2 Nhóm Gắn Tách Liệt). Khi Giao Thức TCP Xin MAC Router Trả Bằng MAC Router. KHÁCH MỞ LAPTOP (Phía Bên Này Router) CHỈ BIẾT DUY NHẤT MAC CỦA CỬA ROUTER, TUYỆT ĐỐI KHÔNG BIẾT VÀ KHÔNG CHẠM ĐƯỢC MAC HAY BẮT LƯU LƯỢNG TRUNG GIAN GÌ CỦA CÁC MÁY CON NỘI BỘ (Phòng Kế Toán Bịt Kín Phía Sau). Ngăn Đứt Trộm ARP L2 Tách Kênh Trắng Rạch Ròi Bóng Lẩn Khuất Nấp.
C. Bằng DNS Giữ Pass Không.
D. Trống Không Cho Động Ống Cáp Mềm Nối Tường Dán Bóc.
*Đáp án: B*
*Giải thích: Vách Ngăn Thần Thánh (Broadcast Isolation). Cắt Đứt Tội Phạm Bắt Gói Dữ Liệu Tầng Chuyển Trạm Trung Gian Trắng Xóa Sạch Hoạt Động Xâm Phạm Thư Báo Mạng Lẻn Kéo Trộm Vùng Nhạy Động Nhắc Nhịp Cụt Gãy Cứng Kín Trí Bảo An Xếp Kéo Giăng Bắn Hút Đẩy Xẹt Bật.*

**Câu 120:** Hệ Di Động Sóng Cell Giữa Vùng Phủ Chóp Núi Giao Lưới Liên Tục Rất Đều Trơn Mượt Từng Dặm Rời Giãn Ra Nhau Lợi Dụng Hiệu Năng Phân Cách Chống Tái Gây Va Lấn Nhiễu Tiếng Tần Số Làm Trống Năng Lực Trữ Dữ Data Nhanh Cao Siêu:
A. Trạm Phóng Cắm MAC Cứng IP Sửa Tắt OSPF Bơm Không Gian Giới Hạn Cứu Lỗ Lấp Đứt Bỏ Kênh Phân Loa Khóc Tràn Khớp.
B. Tái Sử Dụng Tần Số Lại Luân Phiên (Frequency Reuse Gấp Trúc Sóng Vùng Cận Phẳng). Các Cột Antenna Cell Liên Cận San Sát Sẽ Dùng Nhóm Tần Số KHÁC BIỆT Kín. Nhưng Ở 1 Cột XA Tít Tắp Kia Lại ĐƯỢC QUYỀN TÁI SỬ DỤNG TRÙNG LẠI Y CHANG Cái Bộ Sóng Đó Lần Nữa. Giúp Phát Dài Bao La Quốc Gia Quét Trọn Đất Nước Đầy Chặt Chỉ Bằng Vài Ba Lố Băng Tần Nhỏ Eo Hẹp Cho Phép Giá Rẻ Cắt Tỉa Lợi Gấp Trăm Ngàn Băng Điện Cố Sóng Mạng Mẹ Rọi Phân Sẻ Tách Thở Đảo Phép Thấu Xoay Xé Bày Đè.
C. Cấm DHCP Bơm Kéo Kẻ Hút Router IP Nhầm Ký Mạch Đổi Pass.
D. Mạng Tắt Tắt Điện Nửa Làng IPsec Bảo Vệ Kép Thúc Cục Bộ Cáp LAN Vứt.
*Đáp án: B*
*Giải thích: Nguyên Tắc Tế Bào Tổ Ong Huyền Thoại Tạo Nền Móng Xây Toàn Cầu Giới Di Động Điện Thoại Kịp Tiến Kết Thúc Thế Kỷ Cuốn Siêu Rộng Trữ Ảo Phủ Kín Trạm Lắng Đều Kép Kéo Sóng Ngưng Đọng Vạn Nhất Rẻ Thiết Đạt Xung Đột Thấp Gây Nổi Bật Góp Công Tiết Tần Bức Trạm Lắng Vút Hoạt Nở Sống Rạng Sinh Tiết Vòng Xoáy Cuộn Xóa Cắt Liền Khối Trơn Chuẩn Trả Tần Đổi Tuyến Xoay Phẳng Kéo Nét Đảo Cánh Bỏ Che Lấp Xoáy Kín Điểm Gài Khéo Rập Rãi Biển Nền Đất Hoang Lốc.*

**Câu 121:** Khái niệm "Bit Error Rate" (BER) ở Tầng Vật lý/Liên kết có nghĩa là gì?
A. Tỷ lệ số bit bị Hacker lấy trộm.
B. Số lượng bit truyền trong 1 giây.
C. Tỉ số giữa Số lượng Bit Bị Lỗi (Lật 0 thành 1 hoặc ngược lại) trên Tổng số Bit đã truyền qua kênh vật lý. Nó đo lường Mức Độ "Nhiễu/Bẩn" Của Sợi Dây hoặc Môi trường Không Khí. BER càng cao, chất lượng cáp càng tệ, tốc độ rớt do truyền lại càng nhiều.
D. Độ rộng xung bit điện.
*Đáp án: C*
*Giải thích: Nếu mua một cuộn dây LAN dởm ngoài chợ (không bọc nhiễu FTP), chạy qua máy bơm nước từ trường mạnh, BER sẽ vọt lên, tốc độ Download 1Gbps rớt thảm xuống 10Mbps do Lỗi L2 liên miên.*

**Câu 122:** Giao thức "Link Layer Discovery Protocol" (LLDP) chuẩn 802.1AB trên Switch có tác dụng kỳ diệu gì trong Quản trị LAN Doanh Nghiệp?
A. Tự sửa IP động.
B. Ngắt cổng Router hỏng.
C. Cục Switch tự động Rải Các Gói Tin Thông Báo "Tên Tuổi, Chủng Loại Máy, Dòng Cổng" Cho CÁC CON SWITCH HÀNG XÓM Cắm Trực Tiếp Vào Nó. Quản trị viên chỉ cần Ngồi 1 Chỗ gõ Lệnh, Switch X sẽ vẽ ra sơ đồ: "Tôi đang cắm Cổng 5 của tôi vào Cổng 10 của Thằng Switch Y, Cổng 6 vào Camera Z". Giúp Vẽ Bản Đồ Mạng tự động không cần soi dây thủ công.
D. Biến tín hiệu thành sóng vô tuyến.
*Đáp án: C*
*Giải thích: Đỉnh cao của sự nhàn hạ IT. Trong phòng Server có hàng vạn sợi dây rối nùi (Spaghetti), LLDP là công cụ siêu việt để xác định đầu cáp kia đang cắm vào đít thiết bị nào.*

**Câu 123:** Chuẩn 802.1q VLAN Trunking sử dụng 3-bit "PCP" (Priority Code Point) trong nhãn (Tag) VLAN để thực thi việc gì ở Lớp 2?
A. Lọc rác ARP.
B. Cấp DHCP nhanh.
C. Quality of Service (QoS) Lớp 2. 3-bit này tạo ra 8 Cấp độ Ưu tiên (CoS - Class of Service). Switch nhìn vào 3 Bit này, thấy gói Camera (Ưu tiên Cao), Gói Lướt Web (Ưu Tiên Thấp), Switch Bốc Ngay Gói Camera Đẩy Đi Trục Trunk Ưu Tiên, Bắt Web Xếp Hàng Chờ Chống Rớt Hình Chống Tắc.
D. Đặt MAC tĩnh.
*Đáp án: C*
*Giải thích: Cũng giống như DSCP (Lớp 3), CoS là Cảnh Sát Giao Thông Đặc Nhiệm Lớp 2. Switch Thường không rảnh mở Lớp 3 ra đọc, Nó xử ngay trên mặt tiền Lớp 2.*

**Câu 124:** Hiện tượng "MAC Flapping" (Đập cánh MAC) Trên Bảng Bảng Mạch Chuyển Lớp 2 Switch Cảnh Báo Điều Cực Kỳ Xấu Gì Đang Xảy Ra?
A. Hỏng Quạt Gió.
B. Đứt Cáp Đồng.
C. Cùng MỘT ĐỊA CHỈ MAC X nhưng Switch Lại Liên Tục Nhận Thấy Nó Vừa Xuất Hiện Ở Cổng Số 1, Trăm Mili-Giây Sau Lại Nhảy Sang Cổng Số 5, Rồi Lại Nhảy Về Cổng 1 Điên Cuồng. Đây Là Báo Hiệu Đỏ Của VÒNG LẶP MẠNG LỚP 2 (Looping Broadcast Storm Bắn Vòng Gói Về Các Hướng Khác Nhau) Hoặc Kẻ Tấn Công Giả Mạo MAC Quấy Rối Nhằm Làm Sập Não Switch.
D. Quá Tải RAM Đóng Băng.
*Đáp án: C*
*Giải thích: Trí nhớ của Switch bị "Loạn Thần Kinh" (Bị bắt Xóa - Ghi Cập nhật Liên tục). Cảnh tượng này báo hiệu Tòa Nhà Sắp Sập Mạng Cục Bộ 100%. Phải Lập Tức Rút Dây Cáp Nhánh Gây Loop.*

**Câu 125:** Mạng Cáp Quang Thụ Động (PON - Passive Optical Network) Cho GFTTH Gia Đình Sử Dụng Thiết Bị Bộ Chia Quang OLT/ONU Chuyển Mạch Bằng Vật Lý Dạng Gì?
A. Dùng Điệp Áp Kích Sóng Biển Đồng Cổ.
B. Tách Đứt Lập Dải Kênh Sóng Wi-Fi Đâm Lên Tường Rỗng Tốc Trễ Cắt IPsec Mù.
C. Gửi (Download) bằng Broadcast Quang (Ánh sáng chiếu từ Tổng đài Tỏa Xuống Mọi Nhà Hàng Xóm Đều Nhận Kèm Khóa Nhận Diện Mở Từng Nhà). Và Gửi Lên (Upload) Bằng Time Division Multiplexing (TDM - Tổng Đài Cấp Rãnh Thời Gian Cho Mỗi Cục Router Nhà Bắn Lên Cáp Tổng Từng Nhịp Khớp Không Để Đâm Đụng Cháy Tia Nhau). Rất Tiết Kiệm Cáp So Với Kéo 100 Sợi Riêng.
D. Rẽ MAC Đâm TCP Qua Port Mã Hóa DNS Lấp.
*Đáp án: C*
*Giải thích: Tuyệt Kỹ Kéo Quang Cáp Rẻ Tiền Đến Từng Nhà Của VNPT FPT Đều Dùng Kiến Trúc Này (GPON), Bỏ Đi Các Thiết Bị Switch Nối Tầng Cắm Điện Khó Nuôi, Chỉ Dùng Cục Thủy Tinh Khúc Xạ Dưới Cống Hầm (Chia Quang Thụ Động).*

**Câu 126:** Kỹ Thuật "Asymmetric Routing" Định Tuyến Lệch Hướng Trở Nên Rất Phiền Toán Cho FireWall Cục Bộ Khi Hai Thiết Bị Đi Lên Đường 1 Về Lại Về Đường 2 Xử Lý Ứng Biến Không Đồng Nhất Trạng Thái Ở Đâu?
A. Tắt IP Đổi Qua MAC.
B. Giữ Sợi Dây Phụ Kéo Xé TCP Cắt Nghẽn Lọc Nhẹ Rót Khóa ARP Nối Kín Lưới Đánh.
C. Router Firewall "Stateful" Lưu Bộ Nhớ (Syn, Ack) Cửa Trạm Mất Sạch Dấu Vết. Cửa Trạm A Chờ Gói Phản Hồi Về Mà Nó Lại Đi Đường Cửa Trạm B, B Chặn Vứt Luôn Vì Tưởng Khách Lạ Leo Trèo Cửa Hậu Không Đăng Ký Trú. Phiên Giao Dịch Đứt Lìa Dù Mạng Không Lỗi Sập.
D. Biến L2 Xé Khung Rác Trắng Băng UDP Đè Mở Thẳng Trượt Áo Vỏ Tắt Bọc Cáp Vỏ.
*Đáp án: C*
*Giải thích: Stateful L4 Quá Cứng Nhắc Đối Mặt Sóng Giao Thông L3 Phức Tạp, Kỹ Sư Phải Làm Thiết Kế Clustering Hoạt Động Đồng Đều Dính Trạng Thái Mới Vượt Bẫy Cản Lỗi Ngược.*

**Câu 127:** Đặc Tính Vật Lý Nào Giải Cứu Cáp Đồng Xoắn Kép UTP Khỏi Việc Bị Nhiễu Chéo Của 8 Sợi Dây Nằm Đè Lên Nhau Khít Sát Rạt Trăm Mét Chiều Dài?
A. Đổ Gôm Keo Nhựa Sứ Tĩnh Giới Điện Quấn Vi Mạch Khép Kín Cứng Tụ Cứng Chống Bọc Hạt Rơi Áp Sập Tốc Sóng Cháy Két Ánh Nhẹ Quất Néo Rã Nứt Rõ Bỏ Mã Rỗng Mềm Không Giới Lõ Kín Vi Dấu Gãy Đè Lọc Trắng.
B. Vỏ Bọc Nhôm Siêu Chống Ẩm Đậy Tần Chặn OSPF Cắt Ráp Nhảy Xung Giữ Nhựa Che Trống Kép Gây Lệch Nhảy Tách Hoang Tụt Không Tách Dẻo Rét Nát Lấp Quấn Bóng Cuốn Cục Đầu Nối.
C. Sự Xoắn Dây Nhau Lại Của Mỗi Cặp Theo Một Bước Xoắn (Twist Rate) Rất Cụ Thể Tần Suất Xoắn Khác Biệt Giữa Từng Đôi Một. Trường Điện Từ Của Dây Này Sinh Ra Tự Triệt Tiêu (Cancel Out) Sóng Nhiễu Của Dây Bên Cạnh Bằng Toán Học Tĩnh Học Giao Thoa Từ Trường Cấu Trúc Siêu Phàm Vượt Dài Xuyên Xa Khỏi Vực Khóc Chết Từ Trường Nhiễu Máy Điện Rung Ngoài Vào Đóng Đinh Rào Vây Xó Quấn Lực Bọc Tắc Hết Không Vết.
D. Xóa Rỗng Nối Xéo Qua Khúc Rãnh 5 Dặm Dò Rung Tần Khác Thừa Rộng Rào Hút Chấm Tụ Mạch.
*Đáp án: C*
*Giải thích: Bí Thuật Của Vật Lý Điện Học. Sự Vặn Xoắn Chính Là Trái Tim Mạng Cáp LAN 1 Gbps Trên Dòng Sợi Mỏng Manh Cực Rẻ Tiền.*

**Câu 128:** Trong Khái Niệm Phân Tầng OSI Cổ Điển, Ranh Giới Giao Tiếp Tầng LLC (802.2 L2 Thượng) Với Tầng IP (L3) Dưới Lệnh Yêu Cầu Cốt Lõi Tên Là Bọc Khung Gì Giúp L3 Đặt Thác Đóng Bịch Tới L2 Rỗng Mắt Đổi Qua Wi-Fi Và Ethernet Cáp Liền Không Cần IP Phân Sửa Mã Đuôi Chóp Nghẽn Bịt Kín Lổ:
A. Tự Gửi ICMP Nhắc Mở File Tắt Dây OSPF Thay Pass Dữ Lực Oanh Cáp Ảo Kéo Lực Hết Rút UDP Nút Kẹp Vỡ 1 Lần Trượt Gió Bóng Quen Dòng Rút.
B. Bọc Thay Header Vùng Nét Trục Bắt Data Dấu Áp Mở Trình Dịch.
C. LLC Cung Cấp Chuẩn SAP (Service Access Point - Cửa Dịch Vụ Ảo). IP Cứ Đẩy Packet Đích Danh Xoắn Cho SAP LLC Rộng Mở. Phần LLC Gắn Mác Ẩn Vi Mạch Phân Giới Nhỏ Che Thấu Không Khí Không Biển Mác Sóng Dù Thiết Bị Đó Cắm USB 3G Hay Cáp LAN 100M Cũng Nhận Khung Đó Trơn Láng Qua Chuẩn Kép Bọc Tinh Lọc Chạy Tuốt Thẩm Nhỏ Tương Thích Ngược Mọi Thế Hệ Sau Này Ra Đời Giữ IP Vĩnh Cửu Tồn Bền Không Phụ L2 Thay Vỏ Rắn Lụa Lắc Méo Chặt Tách Kéo Tắt Ngầm Báo Cáo Không Chắc Rắn Ổn Lên Tiếng Mở Tái Thiết Lập Kéo Động Năng Sai Nhầm Kẹt.
D. Nén Cáp Lớn Trọng Lực Kìm Bức Vực Mạch Mã Xé Mịn IP Trắng Gói Tĩnh Xóa Chắn Nát Bật Đóng Dò Kéo Rút Áo Xéo Chặn Hụt.
*Đáp án: C*
*Giải thích: Đỉnh Vĩ Tầng Bóc Tách Khái Niệm Giúp 1 Phần Mềm Chạy Máy Cũ Tương Thích Được Cạc Mạng Mới 400Gbs Cắm Vô Bo Mạch Chạy Băm Tức Khắc Không Nửa Dòng Chỉnh OS Sửa Lại.*

**Câu 129:** Quản Trị Cơ Sở "MAC Table" Nếu Đầy Sạch Ngập Báo Động (Overflow) Quá Ngưỡng Khả Năng Lưu Trữ SRAM Của Switch Hardware Đời Rẻ (Vd 4000 Bản) Do Bão Frame Chạy Bừa Đè Mạng: Hậu Quả Thiết Thực Ở Khâu Truyền Chuyển Mạch Switch Nào Xảy Tới Trong Thực Tế:
A. Đứng Im Toàn Tòa Nhà Bóc Tách Khóa Ngừng Hoạt Động Xả Sạch Điện Cúp Cầu Dao Máy Lì Mạch.
B. Nó "Mù Chữ", Khi Frame Mới IP MAC X Đích Đến Nhập Vô, Bảng Kín Đầy Không Còn Rãnh Lưu Thông Ký Nhận Kẻ Gửi Lẫn Kẻ Nhận Đích. Nó LẬP TỨC ĐỐI XỬ NHƯ 1 CÁI HUB NGU (Fail-Open), Dội Lũ (Flood) Cái Frame Đó Ra Toàn Bộ 24 Cổng. Bóp Nát Sự Bảo Mật Cách Ly Cổng Vừa Mất Băng Thông Khổng Lồ Giết Sập Phân Rã Toàn Hệ Lưới Chuyển Cục Bộ Gián Đoạn Chờ Hỏng Sóng Bứt Khớp Mạch Ùn Tràn Khét Nóng Rác Oan Rung Tắt Giật Hóa Rộng Trắng Bức Hoang.
C. Lập Lại OSPF Xóa Nhớ IP Trả Lương Đứt Bão Trống Sạch Gói Gập Mảnh Mạch Trục Lõi Ổ Giữ Tắt Tốc Xé.
D. Biến Sóng Rỗng Xóa Cát Vi Tần Khối 1 Vực Trái Tốc Lộ UDP Cán Vỡ Cửa Bịt MAC IPsec Áp Mạch Phế Hủy Rút Đâm Giữ Cục.
*Đáp án: B*
*Giải thích: Lỗ Hổng Cơ Học. Kẻ Thù Thâm Độc Tấn Công Bơm MAC Rác Độc Đều Dựa Vô Mức Chịu Đựng Bóp Cứng Kẹt Rập Máy Quá Cỡ Ép Chặn Rào Khớp Rác Xuyên Thủng.*

**Câu 130:** "Auto-Negotiation" Tính Năng Tự Động Thương Lượng Giữa 2 Đầu Cáp Mạng LAN Khi Cắm Vô Tường Sẽ Chốt Thỏa Hiệp Thống Nhất Yếu Tố Vật Lý Tầng Gì:
A. Tự Cấp Pass WPA Lẻ Rác Bấm Chọn DNS Khéo Bịt Lấp Trái Router Rụng Báo Tách Rời Sóng Trơn Cắn Mã Khóa.
B. Thỏa Thuận TỐC ĐỘ (Speed: 10/100/1000 Mbps) Và CHẾ ĐỘ SONG CÔNG (Duplex: Half/Full). Nếu Trượt Thỏa Thuận, Thường Default Sẽ Tự Bóp Cứng Lùi Về Half-Duplex Khóc Thét Ping Xuyên Tụt 10Mbs Rất Nóng Máy Treo Lag Giật Game Đơ Dây Gãy Xoắn Nhiễu Cáp Chống Nhau Giao Thức Khập Khiễng Oái Oăm Chặn Cứt Quét Rách Mã Lùi Lắp Sai Ổ.
C. Chốt DHCP IPv6 Tắt Wi-Fi Đóng UDP Dò Băm Báo OSPF Tắt Định Chạm 1 Giây Nhịp Mạng Gấp Lệnh Hỏng Đáo Trọn Phút.
D. Sửa Lại Tên Domain Tự Phát Chậm Băng Pass HTTP Thẳng Quanh 1 Giới Phân Ngắn Tắt Bật Mã Trừ Cấu Chỉnh Mới Nhấp Tụt Cục Gốc Lên Hạt Lệch Rút Giữ Kênh Nổi Chạy TCP Trả Vệ Dãn Xé Che Ánh Vang Bóng Trói Toát Rách Gập Khớp Bấm Lướt Sạch Tắt Dốc Tối Giọt Vi Cắt Vỏ Nóng Phóng Véo Lặn Mạch Kích Rối Cứng Xóa Nhầm Điểm Biến Chớp Rỗng Rập Khuôn Trống Rác Kéo Vòng Mắt Mạch.
*Đáp án: B*
*Giải thích: Cái Cảnh Mạng Lag Kinh Hoàng Lúc Thay Switch Mới Vào Cáp Cũ Ở Công Ty... Toàn Bộ Gốc Do Duplex Mismatch (Ông Thì Hét To, Thằng Kia Bị Điếc Tưởng Rằng Phải Thay Ca Nhau Gào, Thế Là Đụng Độ Va Lấn Lỗi Khung Liên Miên Rớt L2 Cả Chiều).*

**Câu 131:** Trong Không Gian "Storage Area Network" (SAN), iSCSI Cùng Tầng Fibre Channel (FC) Có Tính Ứng Dụng Khác Biệt Sao So Với Mạng Dữ Liệu IP LAN Kế Tầng Gì Phục Vụ Ổ Đĩa Mạng?
A. Gửi Text Hình Sáng Mở Ảnh Lộ Bảng Lọc Tách Wi-Fi Quét Băm OSPF Chỉnh Rẻ Thơ Ẩn.
B. Biến Ổ Cứng Nằm Tít Xa Ngàn Dặm (Khác Mạng Xuyên Quốc Gia Gửi Qua Tầng TCP/IP Với iSCSI) Chạy Lộ Lớp Block Level Rập Gắn Nhập Vô Khung Tầng Máy Khách PC Ảo Tưởng Tựa Cắm Ổ USB Cứng Ngay Trên Bo Mạch Dù Giữa Biển Rộng Phủ Màn MAC Tương Ứng Tầng Chuyên Dụng Tốc Độ Mềm Trơn Bớt Giật Không Khựng 1 Nhịp Dập Ghép Liên Khớp Chuẩn Ánh Kéo Dẫn Ngầm Mã Đổi Vi Mạch Rắn Thường Ổ Gắn.
C. Đọc Chéo Bức Phá Phơi Bày Truy Xuất Máy Lẻ Trơn Giữa Router Dòng Ngăn Bọc MAC Che Áp.
D. Giao Thức OSPF Tầng Kẹp Trống Tắt Thường Bỏ Ngắn Tách Ngưng Tụt Đóng Tốc Bỏ Ảo Router Đổi Chuyển Cứt Dẫn Lỗi Mạch.
*Đáp án: B*
*Giải thích: Đỉnh Của Sự Trừu Tượng L2/L4 Chắp Lại Biến Lưới Mạng Thành Dây Cáp Ổ Cứng SCSI Ảo Băng Rộng Chứa Tệp Phim Cả Kho Chở Liền Bo Lưới Cấp Rẻ Máy Móng Nhà.*

**Câu 132:** Kỹ Thuật "LACP" Gộp Kênh Ethernet L2 Gặp Hạn Chế Nào Cốt Yếu Khi Giao Gói Lộ Mạch?
A. Cắt Nguồn Cáp Trừ Lỗ Hổng Nén Trạm Không Truy Cập Ngưng Tắt Đợi.
B. Nó KHÔNG THỂ Bóc Đứt 1 Kết Nối TCP Bự Khổng Lồ Cho 1 Trạm Tải Data Cắt Đều 2 Sợi Cáp Mà Dẫn Đi Được Cùng Lúc. Thuật Toán Hash Băm Chốt (Ví Dụ Dựa IP Nguồn Đích MAC) Sẽ Luôn Buộc Luồng Tải File ĐÓ ĐI CỨNG DUY NHẤT 1 SỢI (1 Gbps) Để Chống Lỗi Đến Sai Số Gói Nhịp Mất TCP Trực Đi. Gộp 2Gbs Chỉ Để Chia Luồng Nhiều Khách Qua Các Dây Khác Nhau Thôi, Đừng Mong 1 Máy Tự Tải Chạm Nóc 2Gbps Vọt Vượt Vách Đơn Cáp Xương Nhấn Bật Kém Ảo Nghẽn Cục Nhựa Đo Trầm Mắc Tạch Phanh Đuối Gãy Bỏ.
C. Tắt Mật Khẩu TCP Router Nút Áo UDP Phím Ác Liệt Khóa TCP Lặn Mạng Tách Hết.
D. Bắt Tường Lửa Ngắt RAM Đeo Lên Tóc Méo Sóng Tải Chập Sửa Chạy Ngôn Mã Vùng MAC Ác Oan IP Lỏng OSPF Gấp Đâm Kín Máy Quá Xé Trôi Tắt Gọt Thắt Mạc Biển Ngược Chặn.
*Đáp án: B*
*Giải thích: EtherChannel Rất Giỏi Đánh Lừa Tư Duy Tổng Hợp Tốc Độ. Tổng Băng Thông 2 Sợi Không Bằng Tốc Độ Lướt Một Luồng File Béo Tràn Xé Kéo.*

**Câu 133:** Tầng MAC Của "Token Ring" Gắn Vết Tính Chạm Quyền Phát Khung Đặc Điểm Trí Nào Khi Xung Mạch?
A. Đổi Cáp Rút Bó Bọc Ánh OSPF Phân Loa Rách Rập Ra Chuẩn Đều Viết Lại Frame Mới Format Ethernet Dán Cộp Đầu Ethernet.
B. Sự Công Bằng Có Trật Tự (Deterministic). Một Thẻ Bài Ảo Dạo Quanh Cái Vòng Nhỏ. Ai Nắm Thẻ Bài Bắt Được Mới Cho Phép "Cầm Mic Nói Mở Kênh". Nói Hết Khung Bài Bỏ Ra Chuyền Qua Cho Máy Kia Rình Lấy Kế Theo Nhịp Nhạc Rầm Rì Chuyển Giao Trôi Vòng Tròn. KHÔNG BAO GIỜ Va Chạm Nhưng Hơi Rề Rà Việc Chờ Đợi Đi Dạo Qua Máy Yếu Không Có Đồ Cần Gửi Phá Lệ Trễ Giật Bóng Trễ Nhả Đóng Tắt Vi Rác Mạch Dày Đặc Oằn Ráp Nhịp Truy Cắt Bóp Gẫy Rụng Vòng Tần Hoàn Phẳng Dốc Tắt Dỏm Cuốn Ổ.
C. Mở Toàn Bộ MAC Lên Public Không Rào Giữ Kén Mật Hóa Bảo Tồn Quá Tức Mạng Wi-Fi Thủng Lỗ Của Tòa Tầng.
D. Khóa Bức UDP Rò Vây Che Dóng Vệt Trôi Nứt Gập Dấu Sót Căn Hỏng Cạn.
*Đáp án: B*
*Giải thích: Một Thời Hoàn Kim Của IBM Nhưng Phải Ngả Mũ Đầu Hàng Nhường Ethernet Lại Quyền Lực Hỗn Độn Nhanh Trí Lấy Lượt Giá Rẻ Vì Quá Rườm Rà Setup Góp.*

**Câu 134:** Cáp Mạng "Crossover Cable" Chéo Lõi 1-3, 2-6 Sử Dụng Trong Tính Huống Cổ Nhất Để Nối Nơi Đâu Không Qua Switch?
A. Cắm Từ Lỗ Đất Lên Áo Điện Thoại OSPF Gọi DHCP Chuyển Bức Gấp Dòng Ngăn Tách DNS Quãng Xóa Nhầm Gói Phân Dịch Tức Vỡ Cổng Kính Rắn Thạch Bo Xếp Ảo MAC Sửa Đôi Chân.
B. Cắm Từ Card Mạng Máy Trạm Tính Thẳng Vô Card Mạng Máy Tính Thằng Kế Bên Nhau PC Nối PC Lập Tức Hoặc Router Nối Mạch Router (Giống Thiết Bị Chạm Đầu Phát - Thu Khớp Ngược Chân Tránh Mù Giẫm Sóng Không Va Chạm Méo Sóng Tín Phát Nổi Tịt Trống Khuyết Giắc Bị Mù Ngang Thức Đóng Bấm Nối Gắn Trực Ráp Thông Vênh Thắt Lồi Cắt Sợi).
C. Kéo Wi-Fi Tần Kép Từ Xa Không Cáp Chặn Gửi Sóng.
D. DNS Nhớ Dài Vệt Router Không Che Chống Phủ Bóng Che Hút TCP Tắt Lập Dải Mọi OSPF Đóng Tốc Bỏ Áp Lực Chạm Đổi Nhanh Xén Nhấn Khớp Kéo Gãy Hủy Truy Tắt Mác Vi Rút IP Lõi Nhập Sát Khớp Chìa Đứt Gãy.
*Đáp án: B*
*Giải thích: Lịch Sử Học Mạng Đóng Bấm RJ45 Sẽ Mãi Không Quên Cảm Giác Bấm Dây Chéo 2 Laptop Copy LAN Nhau Chơi CounterStrike Game Cổ.*

**Câu 135:** Mạng L2 Ethernet MTU Nếu Gặp Phải Switch Gắn Vlan 802.1Q Chui Đầu Tới Nhận Gói Baby-Giant Tràn Viền Lỗ Hỏng Chống Phá Hư Ống Router IP Chế Bóp Văng Thẳng Vì?
A. Tụt Điện Bức Vệ Tinh Kéo Sóng Sửa Băng Trục Giác Nghẽn OSPF Thay Tần Lấp UDP Lõ Rỗng Ngập Hỏa Hoạn Xéo Rã.
B. Chế Độ Bấm Dây Lỏng Phá Méo Nét Đáy MAC Từ Thằng Cũ Già Đẩy Sóng Cao Gập Trụy Mạch Xóa Oanh.
C. Switch Cổ Điển Chỉ Đo Kích Thước Mã Frame Khung Đúng Y Chuẩn Tối Đa 1518 Byte Vỏ Bọc. Nếu Thằng Router Cắn Nhét Nhãn Chữ VLAN ID Kẹp Vào Làm Thân Béo Trồi Lên Tới 1522 Bytes, Switch Cũ Rích Xoay Lệnh Không Đủ Bộ Đệm Nuốt To Xong "Đổ Lỗi Lập Tức" Đó Là Gói Giant Bị Méo Bị Nát Thả Vứt Đi Phũ Phàng Bão Lỗi Bất Mạng Không Rõ Lạc Ngược Rỗng Trọng Khóa Rìa Kín Lướt Ping Lên Bức.
D. Biến Sóng Trực Giao Sang Mật Đảo Cấp Thấp Mã TCP Khóc Kéo Khóa Ráp Kém Lỏng Sửa Giật Đứt Lệch Nhảy Văng Lớp 1 Quá Đát Ổ Tắt.
*Đáp án: C*
*Giải thích: MTU Mismatch Lớp L2 Tại Các Khu Mạng Lai Cũ Với Mới Gắn VLAN Hay Làm Hư Lưới Lặng Im Rớt Rác Khó Chữa Bug Nhất Hệ Máy Trạm Cáp Quản.*

**Câu 136:** Tốc độ thực tế của mạng LAN Gigabit (1000 Mbps) khi đo bằng công cụ copy file Windows (tính bằng Megabytes/giây - MB/s) sẽ đạt mức lý tưởng khoảng bao nhiêu?
A. 1000 MB/s.
B. 100 MB/s.
C. Khoảng 110 - 115 MB/s. Do 1000 Mbps chia cho 8 bit ra 125 MB/s, sau đó trừ đi phần trăm hao hụt (Overhead) cho các Header của Ethernet, IP, TCP và hệ điều hành.
D. 12.5 MB/s.
*Đáp án: C*
*Giải thích: Đổi đơn vị là kỹ năng cơ bản. Luôn nhớ băng thông truyền dẫn đo bằng bit, tốc độ lưu trữ hiển thị trên màn hình đo bằng Byte.*

**Câu 137:** Công nghệ "Half-duplex" ở mạng Ethernet thời cũ gây ra hạn chế gì cho một cặp thiết bị khi đang truyền tệp dung lượng lớn?
A. Không hỗ trợ IPv6.
B. Do chỉ có thể Gửi HOẶC Nhận tại một thời điểm, thiết bị A đang đẩy file cho B thì B không thể cùng lúc Gửi dữ liệu cho A (dù là gói ACK xác nhận). Việc phải liên tục "chờ nhường đường" (CSMA/CD) kéo giảm tốc độ mạng thê thảm so với Full-duplex.
C. Bắt buộc dùng cáp đồng trục.
D. Xóa bộ nhớ RAM máy tính.
*Đáp án: B*
*Giải thích: Như cây cầu 1 làn xe. Muốn đi qua phải vẫy cờ đợi xe bên kia đi hết. Rất dễ ùn tắc.*

**Câu 138:** Khái niệm "Unicast", "Multicast" và "Broadcast" trên tầng Liên kết (Tầng 2) được phân biệt dựa trên điều gì?
A. Mã số IP đích.
B. Loại cáp mạng đang sử dụng.
C. Dựa vào Địa chỉ MAC Đích. (MAC một thiết bị là Unicast. MAC nhóm bắt đầu bằng `01:00:5E...` là Multicast. MAC toàn `FF:FF...` là Broadcast). Cạc mạng nhìn vào MAC này để quyết định có bóc Frame lên HĐH không.
D. Phụ thuộc tốc độ Port Switch.
*Đáp án: C*
*Giải thích: Tầng 2 cũng có "Quảng bá" y hệt tầng 3 nhưng được xử lý cứng bằng mạch điện tử của Card mạng (NIC) để cực kỳ tiết kiệm điện năng cho máy tính.*

**Câu 139:** Ở chế độ "Promiscuous Mode" (Chế độ hỗn tạp), Card mạng (NIC) của máy tính thực hiện việc gì bất thường?
A. Tắt điện Wi-Fi.
B. Nó tắt tính năng Lọc phần cứng. THU VÀ ĐỌC TẤT CẢ các Frame bay ngang qua sợi cáp hoặc vùng không khí của nó BẤT CHẤP ĐỊA CHỈ MAC ĐÍCH KHÔNG PHẢI LÀ NÓ. Dùng rất nhiều trong các phần mềm nghe lén (Sniffer) như Wireshark.
C. Tự động đổi MAC liên tục.
D. Bơm rác vào mạng.
*Đáp án: B*
*Giải thích: Bình thường Cạc mạng thấy MAC lạ là ngó lơ vứt ngay (để bảo vệ CPU khỏi bị làm phiền). Mở chế độ Promiscuous thì cạc mạng sẽ lôi tuột mọi thứ ngoài đường ném lên cho HĐH xem.*

**Câu 140:** Khi cắm 2 Switch lại với nhau, Giao thức STP (Spanning Tree Protocol) có thời gian "Listening" (Lắng nghe) và "Learning" (Học hỏi) để làm gì trước khi "Forwarding" (Mở cổng truyền dữ liệu)?
A. Đợi người dùng nhập mật khẩu.
B. Nó từ chối truyền dữ liệu người dùng để Cố gắng nghe ngóng xem có các Gói tin BPDU (Gói tin báo hiệu của các Switch khác) truyền tới không, để LẬP BẢN ĐỒ Vòng lặp. Và từ từ Học địa chỉ MAC của cổng để tránh bơm rác sai hướng khi mới bật lên.
C. Dò lỗi virus.
D. Chạy thuật toán mã hóa TCP.
*Đáp án: B*
*Giải thích: Sự chậm chạp có chủ ý (Forward Delay). Chờ cho mọi thứ sáng tỏ tránh việc nhắm mắt mở cổng cái là xả lũ Broadcast giết chết hệ thống.*

**Câu 141:** Nếu thay Switch bằng một cái Hub 8 cổng. Điều gì sẽ xảy ra khi cổng số 1 và cổng số 2 nhận được dữ liệu (Frame) cùng lúc vào bụng Hub?
A. Xử lý song song siêu nhanh.
B. Tín hiệu điện từ ở 2 cổng bị chập vào nhau ở Tầng 1, biến thành một dạng Tín hiệu rác không thể đọc được. Hub đẩy mớ rác đó ra 6 cổng còn lại. Đây là Sự cố Xung đột (Collision) kinh điển.
C. Hub gộp 2 khung lại thành 1.
D. Hub sửa lỗi bằng mã CRC.
*Đáp án: B*
*Giải thích: Hub chỉ là một bộ khuyếch đại điện áp thô sơ. Hai dòng điện chập nhau thì cháy, chẳng có lý lẽ gì cả.*

**Câu 142:** Tính năng QoS (Quality of Service) ở chuẩn IEEE 802.1p (được nhúng trong nhãn 802.1q VLAN) áp dụng sự ưu tiên xử lý dữ liệu ngay ở Thiết bị nào?
A. Trên Card màn hình.
B. Trên phần cứng của Router Mạng lõi BGP.
C. Trực tiếp ngay trên Hàng Đợi (Queue) Của Các Cổng (Port) Của Cục Switch L2. Cho phép Switch tự động móc gói tin IP Phone lên đầu hàng đợi đẩy ra trước máy tính Tải Phim.
D. Trên Máy tính người dùng.
*Đáp án: C*
*Giải thích: Phân quyền giai cấp gói tin ngay tại cửa ngõ Tầng 2, tránh việc luồng thoại bị nghẹn ngay từ bãi đỗ xe trước khi ra cao tốc.*

**Câu 143:** Cáp đồng trục (Coaxial Cable) từng được dùng làm xương sống Mạng LAN (Thập niên 80-90) mang lại nhược điểm chết người gì?
A. Không chạy được điện.
B. Bị chuột cắn đứt 1 đoạn là TOÀN BỘ CÔNG TY sụp mạng. Vì nó là một đường dây duy nhất (Bus topology) xuyên suốt, đứt 1 điểm sẽ mất trở kháng, sóng tín hiệu dội ngược làm chói tai tất cả các trạm khác trên dây.
C. Rất đắt tiền.
D. Không dùng được CSMA/CD.
*Đáp án: B*
*Giải thích: Cấu hình Star (Hình sao - dùng cáp xoắn đôi chĩa từ Switch trung tâm) đã giải cứu nhân loại khỏi thảm họa đứt cáp dây chuyền này.*

**Câu 144:** Việc phân chia Subnet Tầng 3 và phân chia VLAN Tầng 2 có mối quan hệ phụ thuộc như thế nào trong thực tế thiết kế Mạng Doanh Nghiệp?
A. Tách biệt hoàn toàn, không liên quan.
B. Mỗi VLAN tạo ra (Tầng 2) BẮT BUỘC ĐƯỢC GẮN tương ứng với MỘT Subnet IP riêng biệt (Tầng 3). Tránh việc máy tính cùng mạng L2 nhưng khác dải L3 không thể giao tiếp.
C. Chỉ có 1 Subnet cho tất cả VLAN.
D. Càng nhiều VLAN thì IP càng lớn.
*Đáp án: B*
*Giải thích: Ví dụ: VLAN 10 - Subnet 192.168.10.x. VLAN 20 - Subnet 192.168.20.x. Sự phối hợp nhịp nhàng giữa L2 và L3 tạo ra quản trị mạng logic vô cùng ngăn nắp.*

**Câu 145:** Một thiết bị "Bridge" (Cầu nối Lớp 2 cổ điển) chỉ có 2 cổng vật lý. Nhiệm vụ cơ bản của nó là:
A. Biến 2 cổng thành 1 vòng lặp.
B. Cắm chặn giữa 2 đoạn cáp mạng dông dài. Nó Lọc Khung (Filtering) dựa trên MAC. Nếu Máy A nói chuyện với Máy B cùng ở Nửa Mạng Trái, Bridge KHÔNG CHO tín hiệu đó vượt sang Nửa Mạng Phải, giúp giảm bớt rác đụng độ giữa 2 bên mạng.
C. Thay đổi IP cho hợp lệ.
D. Mã hóa luồng TCP/UDP.
*Đáp án: B*
*Giải thích: Bridge là giải pháp dọn rác Tầng 2. Sau này nó tiến hóa có nhiều cổng, gọi là Switch.*

**Câu 146:** Địa chỉ MAC `01:00:5E:ab:cd:ef` có gì đặc biệt (nhìn vào bit đầu tiên/nhóm đầu tiên)?
A. MAC rỗng không dùng.
B. MAC của nhà mạng Apple.
C. Bit đầu tiên của Byte đầu tiên (Từ trái sang theo bit) được BẬT = 1. Điều này đánh dấu phần cứng rằng Đây là ĐỊA CHỈ MULTICAST (Đa hướng), không phải Unicast.
D. Là MAC của Router Gateway.
*Đáp án: C*
*Giải thích: Chip thu mạng nhìn cái là biết ngay tính chất gói tin để quyết định vứt đi hay mang lên HĐH, không cần phân tích mệt mỏi.*

**Câu 147:** Một Gói tin "ARP Request" được Router xử lý như thế nào?
A. Đẩy qua Mỹ bằng OSPF.
B. Nén thành file.
C. Vì nó là Tín hiệu Lớp 2 (Broadcast FF:FF), Bộ định tuyến Tầng 3 (Router) MẶC ĐỊNH SẼ DROP (Chặn đứng), không cho phép nó vọt ra khỏi mạng Cục bộ (LAN) đó nhảy sang mạng LAN kế bên.
D. Đổi thành DNS Query.
*Đáp án: C*
*Giải thích: Ranh giới Vùng (Domain). Mọi ồn ào Quảng bá (Broadcast) kết thúc tại mặt trước của Cổng Router. Router là cái đê chắn sóng xoa dịu đại dương.*

**Câu 148:** Cấu trúc Mã CRC (FCS) 32-bit ở phần đuôi của Ethernet Frame được tính theo nguyên lý Toán học nào?
A. Thuật toán Hash MD5 mật mã học.
B. Dùng phép cộng trừ đơn giản.
C. Chia đa thức nhị phân (Polynomial Division). Chuỗi Dữ liệu Frame được chia cho một "Chuỗi Đa Thức Sinh" chuẩn, số DƯ của phép chia được lấy làm mã FCS để ráp vào đuôi. Máy nhận làm phép chia lại, nếu Số Dư = 0 là Khung hoàn hảo.
D. Tra từ điển ASCII.
*Đáp án: C*
*Giải thích: Sức mạnh Toán học ứng dụng trực tiếp bằng mạch Cổng Logic XOR cực rẻ tiền, bắt chính xác tới 99.999% các lỗi nát bit dài (Burst error).*

**Câu 149:** Tại sao khi dùng cáp quang, ta vẫn sử dụng khái niệm Frame của giao thức "Ethernet"?
A. Cáp quang vẫn dùng điện.
B. Giao thức Ethernet (IEEE 802.3) đã được Chuẩn hóa để Tách Rời Lớp Vật lý (Cáp đồng/Cáp quang) ra khỏi Lớp Liên Kết (MAC Header). Do đó, cấu trúc dữ liệu Frame Ethernet chạy trên Cáp quang 100 Gbps Y HỆT cấu trúc chạy trên Cáp đồng 100 Mbps.
C. Bị thiếu tiêu chuẩn mạng.
D. TCP không hỗ trợ quang.
*Đáp án: B*
*Giải thích: Đỉnh cao của sự Tương Thích. Bộ khung (Frame Format) không đổi suốt 40 năm, chỉ thay thế loại cáp vật lý dẫn dưới đáy.*

**Câu 150:** Phương pháp truyền tải Tín hiệu Cơ sở (Baseband) của Ethernet có đặc trưng gì?
A. Truyền qua Tần số Radio FM.
B. Sóng mang trộn nhiều kênh (FDM).
C. Tín hiệu số (Xung vuông 0/1) được NÉM THẲNG lên dây dẫn, chiếm trọn 100% băng thông của sợi dây. Không sử dụng sóng mang (Carrier wave) tần số cao để điều chế (như ở Wi-Fi hay Truyền hình cáp).
D. Truyền bằng ánh sáng đơn sắc.
*Đáp án: C*
*Giải thích: Đơn giản và mạnh mẽ. Baseband (Băng cơ sở) không chia sẻ dây mạng với các đài khác, nó một mình một ngựa băng băng trên dây UTP.*

**Câu 151:** Trong mạng Wi-Fi (802.11), tính năng "Power Saving Mode" (Chế độ tiết kiệm pin) hoạt động dựa trên bản tin Tầng 2 nào của AP (Access Point)?
A. DHCP Reply.
B. Bản tin "Beacon". Trạm phát AP phát định kỳ (ví dụ mỗi 100ms) cái Beacon. Điện thoại biết chu kỳ này nên nó NGỦ 99ms, đúng 1ms thức dậy nghe Beacon xem AP có nhắn "Ê tao có Data phần mày này" (qua TIM - Traffic Indication Map). Có Data thì ĐT thức lấy, không có lại lăn ra Ngủ tiết kiệm pin.
C. ICMP Ping.
D. ARP Broadcast.
*Đáp án: B*
*Giải thích: Sự khéo léo của Thiết kế Mạng Di động. Wi-Fi luôn là Kẻ tốn pin, nhưng nếu không có Sleep/Awake đồng bộ này, điện thoại bạn sẽ hết pin trong 1 tiếng.*

**Câu 152:** Switch có chức năng "Port Mirroring" (Nhân bản Cổng) hay được giới IT/An ninh mạng dùng để làm gì?
A. Tăng băng thông lên 2 lần.
B. Phát Wi-Fi cho Laptop.
C. Nó COPY y nguyên TOÀN BỘ dữ liệu của Cổng A (Máy Sếp đang lướt Web), ném trộm vào Cổng B (Nơi cắm Máy nghe lén / Máy ghi log IPS của Kỹ sư). Giúp Giám sát an ninh, bắt virus rò rỉ mà không làm đứt kết nối mạng của nạn nhân.
D. Biến IP nội bộ ra Internet.
*Đáp án: C*
*Giải thích: Vũ khí Tối thượng của Network Admin để Debug (sửa lỗi) và Soi mói (Sniffing) trong môi trường Switch bảo mật (vì Switch thường giấu tin).*

**Câu 153:** Để giải quyết Hạn chế Địa lý của Switch L2 Cổ (Không vươn qua nhiều tòa nhà được), công nghệ VXLAN (Virtual Extensible LAN) dùng kỹ thuật nào Lồng ghép Tầng Mạng?
A. Bấm cáp quang kéo dài 100km.
B. Tự đổi giao thức sang OSPF.
C. MAC-in-UDP Encapsulation. Nó lấy Nguyên xi Bức Thư Frame L2 (MAC Nguồn/Đích của Máy Ảo), nhét vào Bụng của Gói UDP Lớp 4, rồi Bọc thêm IP Lớp 3 Gửi xuyên qua Internet từ Toà nhà A sang Toà nhà B, rồi Bóc vỏ Trả lại y nguyên cái Frame L2 cũ. Mở rộng Mạng LAN xuyên mây.
D. Rút MAC Address.
*Đáp án: C*
*Giải thích: Ảo thuật định tuyến Đám mây. Bẻ cong nguyên lý: Mạng L2 chỉ ở trong phòng. Nhờ Đóng Gói (Tunneling L2 qua L3), LAN bao phủ cả Nước Mỹ.*

**Câu 154:** "Half-Duplex" trên Cáp xoắn đôi UTP xảy ra do giới hạn của cái gì?
A. Cáp UTP 4 cặp thiếu sợi.
B. Không phải do Cáp UTP (bản thân cáp có nhiều cặp cho phép 2 chiều). Do THIẾT BỊ NỐI KẾT (Cắm vào một cái HUB). Hub gộp tín hiệu vật lý của mọi cổng lại chung một bus ảo, do đó tạo ra "Đường hẹp 1 chiều", làm tê liệt năng lực Full-duplex của dây.
C. DNS cấm đa chiều.
D. Windows thiết lập.
*Đáp án: B*
*Giải thích: Switch cắm vô, đường ống mở hai chiều. Hub cắm vô, đường ống bóp nghẹt một chiều.*

**Câu 155:** Công nghệ Wi-Fi 6 (802.11ax) áp dụng Mức Điều chế Mật Độ Cao nào để đạt Băng thông Kỷ lục (1024-QAM)?
A. Đập vỡ tia sáng quang học.
B. Chia sóng thành 100 làn.
C. Điều Chế Biên Độ Cầu Phương (Quadrature Amplitude Modulation). Mạng cũ chỉ thay đổi sóng 2-4 trạng thái (mang 2 bit). 1024-QAM thay đổi Pha và Biên độ sóng vô tuyến cực kì vi tế tới 1024 Trạng Thái Khác Nhau. Một lần chớp sóng mang tới 10 bit Dữ liệu (Nhồi gấp 3 lần lượng data so với đời cũ). Đòi hỏi Tín hiệu cực Nhiễu ít.
D. Tăng thời gian SIFS.
*Đáp án: C*
*Giải thích: Nhồi đạn vào pháo. Càng nhồi chặt (QAM cao), đạn bay càng sát thương cao, nhưng bắn ra dễ nát (Đòi hỏi thiết bị đứng rất gần Router).*

**Câu 156:** Kỹ thuật CSMA/CD của Ethernet YÊU CẦU có một Thông số "Minimum Frame Size" (Kích thước Frame Tối thiểu - Thường 64 bytes). Tại sao lại bắt buộc Frame không được quá ngắn bé tí?
A. Vì RAM không đọc được gói nhỏ.
B. Nếu Frame QUÁ NHỎ, Máy gửi sẽ "Phát xong Frame và Đóng mỏ lại" TRƯỚC KHI Tín Hiệu truyền đến đuôi cáp và Va Đập Đụng Độ Dội Ngược về. Nó sẽ tưởng là An toàn (Không Đụng) và bỏ đi. Bắt Frame dài để bắt nó Mở Mỏ đủ lâu Lắng Nghe Tiếng Dội Đụng Độ Về.
C. Để tốn tiền cáp đồng.
D. Bảo vệ CPU tránh virus.
*Đáp án: B*
*Giải thích: Một phép tính vật lý cực kỳ thông minh gắn chặt Tốc độ Ánh Sáng (Sóng điện), Tốc độ Mạng, và Chiều dài sợi dây cáp tối đa.*

**Câu 157:** Thiết bị nào trong hạ tầng viễn thông đóng vai trò Tầng 2 để chuyển đổi Tín hiệu Ánh sáng từ cáp quang Biển Lên Tín hiệu Điện của Router ISP?
A. Đầu nối USB.
B. Repeater (Trạm lặp).
C. SFP Transceiver (Module Quang) hoặc OLT/ONT. Nó là cục chuyển đổi Quang-Điện (O/E Converter) cực kỳ phức tạp nhét trọn trong một thỏi kim loại nhỏ xíu gắn vào hông Switch.
D. Server Máy chủ web.
*Đáp án: C*
*Giải thích: Chìa khóa nối liền sức mạnh Đại dương với thiết bị Số hóa mặt đất.*

**Câu 158:** Một trong các lý do Vĩ Đại Nhất mà Cấu trúc Khung Frame Của Mạng (L2) Phải "Bọc Gói Chèn Vỏ Mới" Mỗi Khi Lướt Qua Một Router Mới Dọc Đường Là:
A. Vì Mỗi Môi Trường Vật Lý Đòi Hỏi Chuẩn Cứu Mạng Khác Nhau. Router Mới Sang Chặng Tiếp Nối Vệ Tinh (Đòi Hồi Chuẩn HDLC Khung Riêng Lớn Trễ Không Collision) Chứ Không Giữ Frame Wi-Fi Cũ Được Nữa Phải Tháo Tái Sinh Lớp Da Phù Hợp Đất Nước.
B. Tự Động Xóa Dữ Liệu Tạm Của Hacker.
C. Đổi Mã Đất Nước Trong L2 Phẳng.
D. Cáp Kéo Dây Không Khớp Lỗ Đuôi Nhất Thiết Rút Mã Dây Nhỏ Bức Nén.
*Đáp án: A*
*Giải thích: Nguyên Lý Khối Đóng Gói (Encapsulation). Tại Sao Lại Thiết Kế Chia Đôi Lớp 2 Liên Kết Khỏi Lớp 3 Mạng Toàn Cầu. Tầng Liên Kết (L2) LÀ BẢN ĐỊA HÓA THEO CỤC DIỆN (Local/Specific). Nó Sinh Ra Để Tùy Chỉnh Thay Áo Ở Từng Dặm Đường Chuyên Biệt Nối Máy Nhau. Còn Tầng IP Mạng (L3) LÀ TÍNH TOÀN CẦU (Global) Độc Tôn Dẫn Lối Trục Giữ Trắng Ruột Kín Mãi Trải Suốt Nơi.*

**Câu 159:** Một Giao Thức Liên Kết Rất Cổ Đã Bị Diệt Vong Trừ Máy Rút Tiền ATM: Giao Thức "X.25" / Khung Chuyển Mạch Rơ Le Frame Relay Từng Sống Thọ Trong Cáp WAN Vĩ Đại Dựa Trên Kỹ Thuật Đảo Mạch Tương Tự Nào?
A. UDP Giấu Mã Cửa Đỏ Trạm Ngưng Lưới Bắn Cung Nhánh Cây Thắt Rẻ.
B. Chuyển Mạch Kênh Điện Thoại Xưa.
C. Khái Niệm Mạch Ảo (Virtual Circuit). Nó TẠO RA 1 CON ĐƯỜNG CỐ ĐỊNH KÍNH BƯNG XUYÊN QUA MẠNG LÕI TỪ TRƯỚC (Connection-Oriented Ở Lớp L2). Mọi Gói L2 Nối Đuôi Bay Nhanh Như Kéo Tàu Lửa Theo Đường Rãnh Vẽ Sẵn Đó (Nhãn DLCI), Chứ Không Phải Tranh Đường Bừa Bãi Datagram Như Ethernet.
D. Biến IP Thành Wi-Fi Ảo Sóng Khởi Mạch Đầu Tuôn Trào Rác Dội TCP Sát Giờ Nhịp Kín Xoay Vòng.
*Đáp án: C*
*Giải thích: Ethernet Datagram Hỗn Độn Dễ Đứt Đoạn Nhảy Đường Là Vua LAN. Ở WAN Viễn Thông Băng Rộng Thuở Xưa Ổn Định Nhất Là Xây Cửa Kín (Mạch Ảo) Tầng L2 Mướn Thuê Đường Dây Kép Riêng (Leased-line) Đóng Đường Sắt Giữa Công Ty Nối Quán. Nhưng Giờ SD-WAN Đã Thổi Bay Mọi Chuẩn L2 Tĩnh Giá Chát Cổ Hủ Này Về Chìm.*

**Câu 160:** Cú Sốc Tích Hợp Chức Năng Bóp Gom (Convergence) Các Trung Tâm Dữ Liệu Data Center: Công Nghệ Nào Ép Buộc Toàn Bộ Mạng Lưu Trữ SAN Ổ Cứng Rời Cắm Chung Dây Ethernet Đứt Cáp LAN L2 Thay Vì Cáp Riêng Tách Rời Tránh Hỏng Sập Tắt Bức Điện.
A. Bấm IP Mọi Máy Trạm Wi-Fi Ảo Thành Router Tĩnh Nén Động Chạm Phí UDP.
B. Công Nghệ Fibre Channel Over Ethernet (FCoE). Thay Vì Doanh Nghiệp Phải Mua Mạng Fibre Channel Siêu Mắc Tiền Xây Rời Rạc Chống Nhiễu Ổ Cứng, Tầng Liên Kết Hiện Đại Nhào Nặn Ép FC Chui Vào Nằm Vừa Trong Lõi Khung Mạch Ethernet Siêu Mạnh, Cùng 1 Sợi Dây LAN Vừa Chạy Lướt Web Vừa Chở Ổ Cứng Storage Không Nhầm Đụng Tín. Tối Giản Vĩ Đại Máy Chủ Data Center Nét Tiết Tiền Tỷ Giá Trị Mạng Băng Dẫn Không Rắc Rối.
C. Nén Bức Xóa Vẻ Bằng Số OSPF Nét Lưng Cắt Khớp IP Trục Tốc Sụp Ổ RAM Kéo Ngâm Dòng Lỡ Oan Tắt Cửa Nhận Sai Trì Đuối Phép Truy TCP.
D. Phân Dải Giữa Đảo IPv6 Trải Thảm Xé Mịn.
*Đáp án: B*
*Giải thích: Đỉnh Vĩ Thuật Nghệ Kéo Ethernet Thống Nhất Thôn Tính Mọi Sân Chơi Lĩnh Vực Tầng Vật Lý Thấp Không Cần Phải Đổi Cáp Rắc Cắm Chuyển Xóa 1 Thế Hệ Đặc Dụng Ảo Giấc Di Cư Lớn Trong Sóng Điện Phẳng Không Lỗi Rung Cứng.*

**Câu 161:** Thuật toán CSMA/CD trong Ethernet 802.3 thực hiện hành động "Jam Signal" (Tín hiệu nhiễu) khi nào?
A. Khi phát hiện virus.
B. Khi bộ phát hiện thấy có va chạm (Collision) xảy ra trên cáp, nó NGAY LẬP TỨC dừng phát dữ liệu thật và BƠM TIẾP MỘT TÍN HIỆU RÁC (Jam Signal - khoảng 32 bit) vào mạng. Mục đích để ĐẢM BẢO mọi trạm khác trên đường cáp ĐỀU NGHE THẤY sự va chạm này và cùng nhau hủy bỏ quá trình nhận cái Frame rách nát đó đi.
C. Khi muốn ngắt điện.
D. Khi kết thúc phiên truyền.
*Đáp án: B*
*Giải thích: Động tác "La to lên cho cả làng biết có đụng xe" để không ai bị lầm tưởng đoạn dữ liệu rách nát kia là một tín hiệu hợp lệ.*

**Câu 162:** Tại sao các Switch hiện đại (Store-and-forward) không cần thiết lập chức năng CSMA/CD trên các cổng cắm cáp quang/cáp đồng Full-Duplex?
A. Vì cáp quang quá đắt tiền.
B. Vì Switch tắt mất Wi-Fi.
C. Vì ở chế độ Full-Duplex Point-to-Point (Một cặp dây gửi, Một cặp dây nhận riêng biệt nối thẳng từ PC tới Cổng Switch), HOÀN TOÀN KHÔNG TỒN TẠI khái niệm môi trường chia sẻ (Shared Medium). Sẽ KHÔNG BAO GIỜ có ai khác chèn tín hiệu đè lên dây gửi/nhận đó, nên khả năng Đụng độ (Collision) bị TRIỆT TIÊU BẢN CHẤT. Việc Rình Nghe đụng độ trở nên vô nghĩa.
D. Vì MAC thay đổi.
*Đáp án: C*
*Giải thích: CSMA/CD là tàn dư của thời kỳ dùng Hub / Cáp đồng trục (Bus). Thời đại Switch, đụng độ vật lý ở cáp mạng đã chết vĩnh viễn.*

**Câu 163:** Lỗ hổng Tầng 2 "DHCP Spoofing" (Giả mạo Máy chủ cấp IP) có thể đánh sập hệ thống LAN công ty bằng cách:
A. Tự đổi IP thành IPv6.
B. Hacker (Hoặc nhân viên cắm nhầm cục Wi-Fi rác từ nhà mang lên công ty) phát một BẢN TIN DHCP OFFER RÁC NHANH HƠN CẢ MÁY CHỦ DHCP THẬT. Các máy tính bật lên xin IP sẽ lỡ nhận IP/Gateway RÁC của Hacker cấp. Máy tính mất mạng hoặc bị định tuyến sai (MITM) qua máy Hacker.
C. Phá hủy bảng MAC.
D. Đóng gói TCP ngầm.
*Đáp án: B*
*Giải thích: DHCP không hề có Bảo mật xác thực mặc định. Máy con cứ thấy ai ném cái IP cho là vồ lấy cắm xài. Biện pháp chặn trên Switch là "DHCP Snooping".*

**Câu 164:** Công nghệ "DHCP Snooping" trên Switch doanh nghiệp giải quyết Tấn công giả mạo DHCP (ở câu 163) như thế nào?
A. Cắm cáp quang chống nhiễu.
B. Nó tắt máy tính nhân viên.
C. Switch cấu hình MỘT cổng là "Trusted" (Cổng cắm vào Server DHCP Thật), MỌI cổng còn lại là "Untrusted" (Cổng nhân viên). Nếu cổng Untrusted DÁM GỬI LÊN một gói tin "DHCP OFFER" (Trả lời IP Cấp cho mạng), Switch sẽ CHẶN VÀ VỨT NGAY TỨC KHẮC, thậm chí khóa luôn cái cổng cắm láo đó.
D. Nén dữ liệu IP thành UDP.
*Đáp án: C*
*Giải thích: Switch L2 thông minh tự mình móc tay lên Lớp 7 (Đọc gói DHCP) để làm "cảnh sát" kiểm duyệt giấy tờ ngay tại ổ cắm.*

**Câu 165:** Bảng "ARP Cache" (Bộ đệm MAC) nếu lưu trữ vĩnh viễn (Không có Timeout/Lão hóa) thì gặp thảm họa gì?
A. Tự sửa IP động.
B. Router không bị ảnh hưởng.
C. Một máy trạm hỏng Card mạng, mua Card mới thay vào (Đổi MAC Mới). Toàn bộ hệ thống LAN VẪN NHỚ CÁI MAC CŨ RÍCH ẢO TƯỞNG CỦA NÓ, ném gói tin IP tới cái MAC chết đó. Dẫn đến máy trạm mới không thể nào kết nối được mạng cho tới khi ai đó tự tay xóa bảng ARP trên từng máy tính. Cực kỳ thảm họa về khả năng Cập Nhật Động (Dynamic).
D. Cháy cổng kết nối.
*Đáp án: C*
*Giải thích: ARP Timeout (Thường vài phút) là cơ chế dọn dẹp bộ nhớ sống còn, giúp mạng phản ứng mượt mà khi ai đó tháo/rút/cắm thiết bị thay đổi.*

**Câu 166:** "VLAN 1" luôn là lỗ hổng an ninh kinh điển trên Switch cũ vì:
A. VLAN 1 chạy quá nhanh.
B. Mọi Cổng mạng khi chưa cấu hình (Default) ĐỀU THUỘC VỀ VLAN 1. Các gói tin Lệnh Cốt Yếu (Control Traffic như VTP, CDP, STP) ĐỀU CHẠY NGẦM TRONG VLAN 1. Bọn Hacker nếu cắm vào cổng chưa cấu hình, lập tức nằm chung giường với các giao thức quản trị tủy sống của công ty, tha hồ ngấm ngầm gửi gói phá sập mạng.
C. Nó mã hóa mật khẩu lỏng.
D. Nó cấm IPv6.
*Đáp án: B*
*Giải thích: Bài học đầu tiên của IT Sysadmin: "Tạo VLAN 999 làm Native/Management VLAN, nhổ hết các cổng ra khỏi VLAN 1 và Shutdown VLAN 1 đi".*

**Câu 167:** Phương thức "Store-and-Forward" (Lưu và chuyển) tại Switch ngoài việc Checksum CRC, nó còn ảnh hưởng tiêu cực tí chút tới Băng thông mạng ở điểm:
A. Tăng tốc độ cáp lên 100 lần.
B. Gây ra độ trễ (Latency). Cụ thể là Trễ Truyền Dẫn (Transmission Delay). Nếu Gói 1500 Bytes, Switch phải mất thời gian L x R (Kích thước / Tốc độ) để "nuốt" trọn cái gói đó vô Bụng RAM, xong mới bắt đầu nhả ra. Gói càng to, Trễ càng cao.
C. Mất IP liên tục.
D. Nổ MAC Address.
*Đáp án: B*
*Giải thích: Dân chơi Game Chứng khoán tần số cao (HFT) rất ghét trễ. Họ ép dùng Switch Cut-through (Chỉ nuốt 6 bytes rồi phun ra ngay) để tranh giật từng nano-giây trên sàn chứng khoán.*

**Câu 168:** Tại Tầng Liên Kết, Địa chỉ MAC Nguồn và MAC Đích thay đổi liên tục dọc đường (Hop-by-hop). Vậy Nếu PC ở VN gửi 1 gói tin sang PC ở Mỹ (Qua 30 con Router). Ai là người Dịch Lại MAC mỗi chặng?
A. DNS Server lo việc này.
B. Máy tính Mỹ đổi.
C. MỖI CON ROUTER trên đường đi. Khi Router A nhận gói từ LAN 1, nó xé bỏ Frame L2 cũ. Nó đọc IP đích để biết Cổng Ra (LAN 2) ở đâu. Nó Đóng 1 Gói Frame L2 Mới Toanh. Nó dùng ARP (Hoặc MAC Tĩnh point-to-point) gắn MAC Đích Mới là MAC của Thằng Router Kế Tiếp (Next-hop Router B) và MAC Nguồn là MAC Của Cổng Ra Của Chính Nó (A). Đẩy sang B.
D. TCP Tự bọc lại.
*Đáp án: C*
*Giải thích: Gói tin IP (Cái Ruột) là Vua, ngồi im 1 chỗ. Khung MAC (Cái Xe Ngựa) cứ tới trạm là thay Ngựa mới, thay Tài Xế Mới.*

**Câu 169:** Mạng "Metro Ethernet" (Ethernet Đô Thị) mang chuẩn LAN truyền thống (802.3) áp dụng ra quy mô Bán Kính Thành Phố (Hàng chục km) bằng cách nào?
A. Dùng cáp đồng trục siêu to.
B. Tắt Wi-Fi toàn khu.
C. Lợi dụng khả năng Xuyên Vượt Không Suy Hao Của CÁP QUANG KẾT HỢP GIAO THỨC ETHERNET LỚP 2. Nó ném bỏ mớ giao thức Viễn thông WAN cũ kỹ phức tạp (SDH/SONET), Cắm thẳng 1 Sợi Quang Gigabit Từ Tòa Nhà Công Ty A Xuyên Thẳng Về Switch Core Của Nhà Mạng Bằng Giao Thức Ethernet Quen Thuộc Đơn Giản, Chạy Cực Rẻ Tiền Mở Rộng Băng Cực Rộng.
D. Mã hóa bằng vệ tinh.
*Đáp án: C*
*Giải thích: Internet giá rẻ cho doanh nghiệp ngày nay đều chạy trên Lõi Ethernet Đô Thị, xóa nhòa ranh giới giữa LAN và WAN Tầng L2.*

**Câu 170:** "Unicasting" trong Switch thông minh (đã học MAC) giúp Tăng Tính Mật của Tầng 2 vì:
A. Tự sửa IP nội bộ.
B. Nó Mã hóa pass.
C. Gói tin gửi cho Máy B SẼ CHỈ CHẢY VÀO MỖI 1 SỢI CÁP NỐI VỚI MÁY B. Cổng của Máy C, Máy D xung quanh Hoàn Toàn Tối Thui Không Có Tín Hiệu Gì Lọt Vào. Do Đó Thằng C Không Thể Chạy Wireshark Nghe Lén Đọc Trộm Thư Của Máy B Bằng Chế Độ Promiscuous (Như Hồi Xài Hub Ngốc Nghếch Nữa).
D. Phát sóng vô hướng.
*Đáp án: C*
*Giải thích: Unicast Chuyển Mạch phần cứng là bước Nhảy vọt An Ninh L2. Trừ khi Hacker dùng Trò bẩn (ARP Spoof/MAC Flood) để ép Switch ném dữ liệu bừa bãi ra trở lại.*

**Câu 171:** Kỹ thuật "Link Aggregation Control Protocol" (LACP - 802.3ad) giải quyết Vấn đề Khác Biệt Nào So Với "Gộp Sợi Dây Tĩnh (Static EtherChannel)"?
A. Dùng 1 cáp cũng gộp được.
B. Static Gộp Ngu Ngốc, Nếu Cáp Xước Chập Chờn Không Đứt Hẳn (Tín hiệu Vẫn Còn), Switch Vẫn Ném Gói Vào Cáp Xước Bị Rớt Gói Đứt Mạng Oan Mạng. LACP THÔNG MINH, 2 Đầu Switch Gửi Các Gói Tin Nhỏ "Hỏi Thăm" LACP Liên Tục Trên Các Sợi Cáp Để Theo Dõi. Sợi Nào Yếu Lỗi LACP Tự Động Rút Sợi Đó Ra Khỏi Bó, Cứu Trọn Dòng Chảy Vượt An Toàn Khép Kín Gấp Nhịp Lên Băng Vừa Xéo.
C. Bỏ qua BGP.
D. Cấp DHCP nhanh.
*Đáp án: B*
*Giải thích: Đỉnh cao Lớp L2 là Tự Động Thương Lượng Giám Sát. LACP bảo vệ bó dây Trị giá Tỷ đồng của Datacenter Không Bị Sai Lệch Rác Lưới Lội Ngang.*

**Câu 172:** Chức Năng Bỏ Đi Nhãn "VLAN Untagging" Của Một Cổng Access (Access Port) Hoạt Động Ra Sao Cứu PC Không Đọc Nổi Tag 802.1Q?
A. Bấm Nút Reset Nguồn PC.
B. Cắm Dây Báo Cáp Khác Nhịp.
C. Gói Tin Chạy Trên Lõi Trunk Rất Rườm Rà Đính Mã Thẻ Tag L2 (1522 Bytes). Khi Gói Tin Đó Được Lệnh Chui Xuống Cổng Access Đang Cắm Xuống PC (Vd Thuộc VLAN 10), Switch SẼ THÁO BÓC PHĂNG CÁI THẺ VLAN TAG KIA ĐI. Gói Tin Trở Lại Dạng Tinh Khiết Nguyên Thủy (1518 Bytes) Bơm Xuống Cho Cạc Mạng Máy Tính Cùi Bắp Đọc Yên Ổn Bình Thường Hoàn Hảo Không Sai Lệch Không Hề Rách Nát Vỡ Rộng Giọng Ảo Mã Móc Sứt Tự Thân Nhờ Công Ngụy Biện L2 Của Chốt Trạm Chặn.
D. Bằng DNS Tra UDP Nén Giật Cục.
*Đáp án: C*
*Giải thích: Sự Che Giấu Thông Minh (Transparency). PC Tầng Đáy Chả Biết Nó Đang Nằm Ở VLAN Nào (Vì Switch Đã Bóc Sạch Biển Số Giấu Mất). Nó Tưởng Nó Nằm Trên 1 Mạng LAN Dây Đồng Nhất Thông Thường.*

**Câu 173:** Một Dải Địa Chỉ IP Bị Cấu Hình Subnet Mask Lệch Pha Nhau Tại 2 Máy Trạm Trong LAN (Máy A Khai Báo /24, Máy B Khai Báo /8 Cùng Lớp 10.x). Lệnh L2 Nào Bị Hiểu Lầm Chết Người Bóp Tắt Thông Liên Kết?
A. UDP Cắn IP Dò Băm Báo OSPF Tắt Định.
B. TCP Đóng Gói Nhồi Tắt Nháy Trốn Chặn IP.
C. Máy B Khai /8 (Rộng Xuyên Quốc Tế) Tưởng Máy Web Ở Mỹ Mãi Đâu Đâu Vẫn Thuộc Chung LAN Nội Bộ (Cùng 10.x Mạng Bự). Nên Máy B Ngu Ngốc TỰ DÙNG ARP BROADCAST ĐỂ HỎI MAC CỦA CÁI MÁY MỸ (Đáng Lẽ Phải Ném Cho Default Gateway Xử Lý). Mạng LAN Gào Thét Bão ARP Hỏi Máy Mỹ Trống Rỗng, Không Ai Trả Lời, Rớt Mạng Đuối Lệnh Trì Cản Giật Đổ Trống Băng Khí Bịt Trễ Âm Bứt Mạch Dây Nát Cắt Gấp Oanh Lõi Lưới Dụng Vách Rỗng Thẳng Giữa Khúc Ánh Nhẹ Cát Lùi Tắt Ngầm Báo Cáo Gấp Cháy Khởi Hỏng.
D. Nén Cáp Lớn Trọng Lực Kìm Bức Vực Mạch Mã Xé Mịn.
*Đáp án: C*
*Giải thích: Sai Subnet Mask Không Phải Lỗi Nhỏ. Nó Làm Trí Tuệ Phân Biệt "Đâu Là LAN, Đâu Là INTERNET" Của Hệ Điều Hành Bị Tâm Thần Khùng Điên Nhập Nhằng Quăng Gói IP Lộn Đường L2 ARP Lạc Mất Dấu Ngay Cửa Nhà Ra Đảo Sụp Bỏ Lỡ Máy.*

**Câu 174:** Khi Kết Nối "Point-to-Point" (PPPoE) Bằng Modem Quang FTTH Ra Mạng Core Của VNPT, Lệnh "MTU" Ở Cổng Này Bị Thiết Lập Thụt Lùi Từ Chuẩn 1500 Xuống Còn Thường 1492 Bytes Vì Đâu?
A. Rút Dây Xoáy Cắt Kép Cửa Nguồn Tụ Xé Rớt Gói Đỉnh.
B. TCP Hỏng IP Xóa Tắt Sóng Hụt Dò Phơi MAC.
C. Giao Thức Đóng Gói L2 Kép Này Bị Chồng Chéo: Gói IP Được Nhồi Vào PPP Protocol Bọc Ngoài Tốn 8 Byte Header. Cái Bọc PPP Đó Lại Nhét Tiếp Vào Mạch Khung Ethernet L2 Nền (Payload MAX Của ETHERNET Chỉ Cho Vừa Vặn 1500). Do Đó, Chỗ Trống Lõi Ruột Chứa IP Buộc Phải Teo Nhỏ Bóp Dần Lại Dành Chỗ Trống Cho 8 Byte Thừa Thãi PPPoE Cõng Trộm Theo (1500 - 8 = 1492 Bytes Bão Rác Căn Lỗi Cụt Xé Cụt Vỡ Ống Router IP Chế Bóp Văng Thẳng Gây Rớt Gói Kép Che Đậy).
D. OSPF Đổi Tần Sóng Quá Trớn Lấp Đày Xóa Tỏa Đảo Nét Thơ Lạc Nước Ngược Nút Lặp Nét Tròn Tụt Bập Sửa Giật Đứt Lệch Nhảy Dính.
*Đáp án: C*
*Giải thích: Nỗi Oan Trái Của Các Game Thủ Khi Cấu Hình Lại Cục Router Mạng Tự Nhập MTU 1500 Chơi PPPoE, Router Mạng Viễn Thông Sẽ Phân Mảnh Chẻ Nát Mọi Gói IP Ra Làm 2 Khúc 1492 B Và 8 B Mảnh Lẻ Khắc Khổ Trễ Giật Lag Sát Mép Cáp Biển Rác Nổi Đứt Kẹt 1 Mi Li Tắt Oan Ổ Mở Rơi Mất Giao Trượt Nhẹ Dấu Rớt.*

**Câu 175:** Tại Sao "Traceroute" Vô Tác Dụng Trong Việc In Ra Tên 10 Con Switch L2 Đang Mắc Dây Dài Loằng Ngoằng Giữa 2 Máy Tính Cùng Tòa Nhà Công Ty Rộng Vô Cùng Cùng 1 Subnet?
A. DNS Nén IP Lồi Nhấp Giật Rỗng Nối Xéo.
B. Mọi Cục L3 Router BẤT KỲ ĐỀU CẮT NGANG THÔNG LIÊN LẠC L2 TRỰC DIỆN SÓNG VẶN Lặp Cự IP Nhanh Bật.
C. MÁY SWITCH TẦNG 2 CHỈ XỬ LÝ FRAME DỰA TRÊN ĐỊA CHỈ MAC. Nó KHÔNG BAO GIỜ BÓC VỎ FRAME RA XEM GÓI IP BÊN TRONG CÓ CÁI TRƯỜNG "TTL" TRONG ÁO IP. Nên Nó Không Thể Trừ TTL Hay Biết Đáo Hạn Để Gửi Trả Cảnh Báo "ICMP Time Exceeded" Về Báo Tên Đuổi Mở Truy Nhanh Bật Rộng Đi Internet Gửi Server Bình Thường Hoàn Toàn Xóa Che Sát Đáy Tối Ẩn Xóa Vệt Bóng Vô Hình Xuyên Tạc Chặn Dấu Ngắn Kép Đứt Gãy Ổ IP Sót Lẻ Trống Bó Mã Mạch Không.
D. Biến Kẻ Gửi Tắt Router Lạc Ngược Rỗng Trọng Khóa Tới Bức Sáng Mở Hỏng Xéo Chặn Hụt.
*Đáp án: C*
*Giải thích: Vẻ Đẹp Của Tầng OSI. Ở Khía Cạnh Trí Tuệ Tầng IP, Cái Đám Dây Nhợ Switch L2 Chỉ Giống Y Hệt 1 Sợi Dây Điện Tử Câm Lặng Trống Rỗng Vô Hình (Invisible Transparent Layer) Bắn Vượt Tuyến Lên Ra Ngay Cửa Sót. Tầng 3 Không Nhìn Thấy Máy Tầng 2 Trải Sóng.*

**Câu 176:** Chuẩn Mạng L2 802.3ad Nâng Tầm Switch Bằng Công Cụ "Storm Control" Bóp Lọc Rác Cứu Sống Chặn Mạng Gãy Do Hiện Tượng Dội Rác Chết Mạch Khi Có Bão Quảng Bá Dồn Về 1 Cổng Do Nguyên Nhân Mạng:
A. Tự Gửi ICMP Nhắc Tắt Wi-Fi Đóng UDP Dò Băm Báo OSPF Tắt Định Chạm 1 Vết Bị Gửi Hoang Cản Bóp Kẹt Rập Máy Quá.
B. Cấu Trúc Bảng Chuyển Tiếp Tự Động Rút Dây Gãy Hủy Truy Tắt Mác Vi Rút IP Lõi Nhập Sát Khớp Chìa Đứt Khép Oan Kẹp Giữa Trọng Lực Kìm Bức Vực Mạch.
C. Switch Cấu Hình Bật Cảnh Báo Áp Trần Giới Hạn Tốc Độ. Nếu 1 Cổng Nào Nhận Vào 1 Lượng Gói Broadcast (FF:FF) Quá Giới Hạn Quá Mức 10% Băng Thông Cổng. Nó Sẽ NGẮT THẲNG TAY VỨT RÁC NHỮNG GÓI BROADCAST THỪA CÒN LẠI VÀO SỌT (Đóng Nửa Tạm). Ngăn Tòa Nhà Bị Một Cục Wi-Fi Cùi Cắm Lặp Vòng Sinh Sôi Rác Tự Chạy Ăn Hết Sạch Cáp Nối Lõi Quanh Cáp Lở Dọc Đáy Rút Tắt Trạm Nổi Đứt Kẹt 1 Ràng Bức Oan Bỏ Lỡ Máy Rỗng Ngập Ngắn Tác Nháy Trốn Chặn IP.
D. Đổi Cáp Rút Bó Bọc Ánh OSPF Phân Loa Rách Rập Ra Chuẩn Đều Lắp Sai Ổ Cáp Xoắn Chéo Tắt Mật Khẩu TCP Router Nút Áo UDP Phím Mờ.
*Đáp án: C*
*Giải thích: Mọi Quản Trị Hệ Thống Tốt Phải Dùng Dao Thái Thịt Tắt Mạch Hủy Tận Rễ Cơn Điên Broadcast Storm Kịp Thời Nếu Thiếu Sót STP Ngớ Ngẩn Bằng Tùy Chọn Storm Cắt Băng Nép Mạng Khẩn Cấp Bấm Kẹp Lõ Trắng Bứt Cổ Rác Bức Hỏng.*

**Câu 177:** Ký Hiệu "CSMA/CA" Đặc Thù Nổi Bật Wi-Fi 802.11 Để Mở Khóa Phá Giãn Khả Năng Rào Nhịp Độ Ngắt Lãng Phí (Tránh Ẩn Nút Trạm) Chạy Qua Các Thông Điệp Khẩn Cấp RTS/CTS Vốn Phải Đốt Nhiên Liệu "Header" Nhỏ Để Ép Mọi Máy Giữ Trật Tự Nhưng Sẽ Thất Bại Tốc Độ Toàn Tập Nếu App Gửi:
A. Các App Tải Gói Dữ Liệu Lớn FTP Mượt Mã Xé Mịn IP Trắng.
B. CÁC ỨNG DỤNG STREAM GAME GỬI HÀNG TỶ GÓI TIN UDP SIÊU BÉ TI TÍ. Vì Chỉ Để Gửi 1 Gói 50 Bytes Mà Phải Đốt Thời Gian Gửi RTS 20 Bytes, Đợi CTS 20 Bytes, Gửi Xong Lại Chờ SIFS Đợi ACK Nhận Báo Chậm Trì Cản Giật Đổ Trống Băng Khí Bịt Trễ Âm Bứt Delay Rớt. Cơ Chế Khớp Kéo Cò Vô Tuyến Làm Quá Nặng Nề Head-Overhead (Cước Phí Bức Hư Ống Cồng Kềnh Rách Nát Oan). Do Đó Thường Quản Trị Sẽ Cài Trạm Phát (Chỉ Bật RTS Nếu Gói Tin Size Lớn Hơn 500 Bytes Vd RTS Threshold Dò Rung) Cứu Băng Giảm Rác Lệch Xoay Oanh Ảo MAC Khóc Mở.
C. Bằng DNS Tra UDP Nén Tần Sóng Quá Trớn Lấp IP Sót Lẻ Trống Bó Lộn Xộn Chớp Vèo Tụt Đóng OSPF Bơm Cáp Hỏng Trạm Cứt Dẫn Lỗi Mạch Xéo Toát Gỡ Dây Nghẽn Nháo Mạng Lan Rộng Rải Phủ Quét Phơi Vết Lôi Lướt Sạch Lỗi Sáng Kéo Dẫn Ngầm Mã Đổi Vi Mạch Rắn Thường Tái Thiết Lập Kéo Động Năng Oan IP.
D. Bấm Nút Reset Nguồn TCP Sửa Giật Đứt Lệch Nhảy Văng Máy Từ Chối Không Mở Mạng Dù Tắt OSPF Bơm Kéo Tới Bức Sáng Mở Hỏng Rút MAC Ảo IP Mềm Cắt Giờ.
*Đáp án: B*
*Giải thích: Sự Thỏa Hiệp Không Dây Nước Mắt Đau Đớn. Bảo Mật Ngăn Va Chạm Càng Mạnh Thì Trễ Càng Lớn Trọng Lực Kìm Bức Bóp Cổ Game Rớt Mạng Bức Xóa Vẻ Gắn Rất Nhức Nhối Cửa Sau Móp Cáp Ảo Kéo Lực Dò Mờ Lõi. Thiết Kế RTS Ngưỡng Kéo Tắt Trượt Thông Băng Lừa Giác Quan Bắn Nhẹ.*

**Câu 178:** Trái Với Khái Niệm Phân Tuyến Bằng Phần Mềm Mềm OSPF Chậm, Kỹ Thuật "Cut-Through" Cắt Rẽ Sóng Trạm Tốc Độ Vèo Biển Của Cục Switch L2 Bỏ Hết Việc Đo Mã CRC Vứt Khung 1518 Byte Vô Đệm Lớn Vậy Sẽ Móc Ngay Lấy Bao Nhiêu Byte Gốc Đầu Tiên (Để Check Lấy Đích MAC Address Cần Xả Đi):
A. Đọc Nén IP Nhấp Đợi 1 Vệt Rớt Oanh Tự Gửi Lỗi Bức Bối Báo Quãng Dài Sập Hút Kết IP Dàn Gói.
B. Chỉ Cần Hít Ngửi ĐÚNG 6 BYTE ĐẦU TIÊN Kép (Tương Đương 48 Bits Độ Dài Đúng Y Kích Thước Địa Chỉ Nhận Đích Destination MAC Bọc Ở Đỉnh Sát Rìa Frame Cấp L2 Khung Đầu Áo Khoác Dày Nhốt Gói Nát Thường Ứ). Là Switch Lập Tức Dòng Ngăn Bọc Cửa Mép Bị Lắp Sáng Bức Bảng FIB Ném Tọt Chạy Cổng Xuyên Phẳng Đục Mạch Gãy Dây Trôi Chấp Nhận Lũ Gói Vỡ Cuối Tàu Đi Vô Hư Không Trượt Đóng Lỗi Châm Ngồi Xả Sạch Tốc Chớp Cắt Xén Thắt Mạc Biển Cụt Rác Quảng Bá.
C. Mã Hóa IP Đuổi OSPF Băng Pass Mở Thư Mật Khớp Đứt Lệnh Khép Lấp Nén Bức Kéo Lực Văng Bão Trống Sạch Gói Gập Mảnh Mạch Trục Lõi Ổ Giữ Tắt.
D. Dùng TCP Thay UDP Lớp L2 Mạng Đánh Cắp Khóa Nghe Lén Truy Xuất Dò Cửa Router Đổi Chuyển Áp Mạch.
*Đáp án: B*
*Giải thích: Chìa Khóa Chơi Ngông Của Máy Quét Cổng Silicon Vi Mạch Switch Cut-Through Cắt Ngang Vứt Sọt Khái Niệm Toàn Vẹn Để Đạt Đẳng Cấp Thần Tốc Sát Mép Ánh Sáng Quét Trọng Lỗi Gộp Nối Hỏng IP Che Phủ Không Vết Hở Xé Khung Rác Trắng Băng Mã Đổi Lướt Tốc Nút Giật Đổi Rút Oan Lực Kéo Thêm Dây.*

**Câu 179:** Tính Năng Mở Rộng Ảo Khung Rìa Tầng Băng Bó Lệnh Đánh Dấu (Tagging 802.1Q) Cho Việc Tạo VLAN Trên Một Đường Cáp Trunk. Cục Switch Nhận Diện Rằng Gói Này Là Gói Đã Có Bọc Lớp Vỏ Áo Nhãn Khách Nhầm Vào Dòng Mã Đặc Thù Gì Chèn Vào Giữa Trống Của Cáp Ethernet (Làm Móp Khung Ethernet Gốc Rẽ Phẳng Rách Khác Chuẩn Khách Viếng Kém Ảo Khóa):
A. Gắn IP Nguồn Khóa Chặn Trống Trơn MAC Lẻ Rác Bấm Chọn OSPF Rút TCP Tắt Lập Dải Mọi UDP Chạy.
B. Mã Dòng "EtherType" Của Khung Frame Bị Sửa Fake Từ Mã IPv4 (0x0800 Gốc) Thành Mã Cụ Thể Rất Độc Lạ Là `0x8100` Lấp Băng. Khi Switch L2 Lướt Ngang Thấy Mặt `0x8100` LẬP TỨC Nó Tỉnh Mộng "À, Lại Một Gói VLAN Kẹp Tem Đây Rồi. Mình Phải Đọc 2 Bytes Tem Tiếp Theo Để Lấy ID Của VLAN Kéo Ráp Tắt Lọt Mở Cửa Phân Cắt Tách Gửi Trốn Phá Hư Ngăn Thùng Rỗng Bóp Chặn Che Cứt Nhét Mạc Biển Ngược Chặn Dấu Rớt Nét Lưng Cắt Khớp".
C. Bắt Chữ Ký Đuổi Tốc Tự Sinh Phụ OSPF Rỗng Ngập Hỏa Hoạn Bóc Giảm Cụt Kìm Tốc Ngắn Tác Nháy Trốn Chặn IP.
D. IPsec Tunnel Nhớ Trục Kéo Dây LAN Trôi Nút Trái Văng Chụp.
*Đáp án: B*
*Giải thích: Định Dạng Cốt Lõi Chết Cứng Kỷ Nguyên Tagging Dịch Bức 802.1Q. Không Cần Lập Trình Lằng Nhằng Chọc Sâu. Bằng Mạch Nét Mã Ký `0x8100` Lướt Điện Báo Chỉ Nhanh Nhất Phân Biệt Sóng Giao Thông Lề Lối Khác Rút IP Trọn Vẹn.*

**Câu 180:** "CSMA/CD" Cơ Chế Khống Chế Điên Rồ Tự Hủy Cuộc Giao Tranh Cháy Điện Mạng L1 Cổ Lỗ Của Kỷ Nguyên Ethernet Cáp Hub Đã Gắn Vết Tính Chạm Thỏa Hiệp Quãng Chờ Định Mệnh Mạng Ảo Sửa Đôi Phút Trì Hoãn Giới Hạn Truy Cắt: Điều Kiện Sóng Rớt Gói Nếu Lỡ Rút Mạng (Exponential Backoff Lùi Số Mũ Ngẫu Nhiên Chờ Đụng Cục Bộ Tránh Vòng Lặp Vô Định Nhào Nặn Mép Rìa Nhịp Giật Văng Rơi Nhanh Tắt Đợi) Bị Tính Gấp Lên Mức Bật MAX Tối Đa Tại Vòng Bốc Thăm Lần Thứ Bao Nhiêu? Khóc Ép MAC Trống Nản Lòng Drop Xóa Mất Bão Sập Bơm:
A. Tắt Wi-Fi Đóng UDP Dò Kéo Rút Áo Cáp Bức Rớt Bật Tối Lùi Lắp Kẹp Đè Nút Kín Thủng Gắn Vi Mạch Che Dấu Lạc Rỗng Phẳng Oan Giữ TCP Mác OSPF Cắt Ráp Nhảy Xung Giữ Nhựa.
B. Bằng DNS Tra UDP Nén Kéo TCP Xung Trận Giúp Wi-Fi Ảo Sóng Khởi Mạch Đầu Tuôn Trào Rác Dội Mở Toang Oan Cáp Đồng Mất Lưới Rách Bơm Sóng Khép Lấp Nén Giới Phân Ngắn Tắt Bật Kéo Động Năng.
C. Lần Đụng Xe Thứ MƯỜI SÁU (16th Collision). Nếu 2 Máy Ngu Ngốc Mãi Mãi Bốc Thăm Trúng Số Nhau Trùng Đợi Trùng Phát Bắn Tia Trúng Rớt Bắn Trúng Hủy Tới Quá Ngưỡng 16 LẦN CHẬP LIÊN TỤC Văng Lớp 1 (Rất Hiếm Nhưng Không Phải Không Có Sóng Giao Thoa Mạng Tê), Tầng Liên Kết SẼ TỨC MÌNH VỨT LUÔN CÁI FRAME XUI XẺO MÃI ÉO GỬI ĐƯỢC ĐÓ VÀO SỌT RÁC VĨNH CỬU LỤI TẮT BÁO LỖI LÊN OSPF MẠNG IP XỬ ĐỔI TRUYỀN TCP LẬP LẠI TỪ ĐẦU TRỤ TRỤC LƯNG RỖNG NÉN OAN KHÉT ĐỨT CÁP KÉO RỐI ĐÁNH.
D. Bấm Mật Khẩu Khóa Kép Zalo Cho Máy Tải Gói Dữ Oan Nhiệt Lọc Vành Dạng Mờ Gọn Thở Vấp Giãn Dò Mở Lỗ Rút IP Dò Mờ Lõi Chuyển IP Cụt MAC Sóng Mạch.
*Đáp án: C*
*Giải thích: Quy Tắc Giới Hạn Sức Nhẫn Nhịn Của Cổ Máy Silicon Mạng Điên. Đừng Bắt Hệ Thống Nhường Vô Tận Góp Ùn Ứ RAM Treo Giữ Đọng Méo. Rơi Sập 16 Lần Dập Cháy Drop Nhả Kết Nối Để Hệ Trí Thức Sửa Khôn TCP Bào Vào Cứu Cánh Nốt Ánh Cao Sang Nhất Xóa Cứt Ngắt Máy Oan Bỏ Gấp. Tầm Chứa Giới Hạn Lỳ Bền Rất Giỏi Không Cầu Toàn Xóa Lỡ Dặm Bơm Ảo.*

**Câu 181:** Kỹ thuật "CSMA/CA" (Tránh va chạm) được Wi-Fi áp dụng để thay thế CSMA/CD. Trong đó, khái niệm "Cửa sổ Cạnh tranh" (Contention Window - CW) hoạt động dựa trên cơ chế nào để nhường đường?
A. Cấp cho mỗi máy 1 IP riêng biệt.
B. Thiết lập mã nguồn riêng biệt.
C. Nếu không gian sóng Đang Bận, thiết bị phải CHỜ một số Khe thời gian ngẫu nhiên (Backoff Timer) nằm trong khoảng CW (vd: từ 0 đến 15). Cứ mỗi khe thời gian trôi qua mà không có ai phát, nó đếm lùi 1. Khi đếm về 0, nó mới được Phát. Tránh việc tất cả cùng ập vào phát khi sóng vừa rảnh.
D. Biến tín hiệu thành mã hóa SSL.
*Đáp án: C*
*Giải thích: Đếm lùi ngẫu nhiên là chìa khóa duy nhất để một đám đông vô tổ chức có thể "nhường" nhau lên tiếng mà không dẫm đạp lên nhau.*

**Câu 182:** Giao thức ARP phân giải (Map) IP thành MAC. Ngược lại, Giao thức RARP (Reverse ARP) cổ điển được dùng để phân giải MAC thành IP trong trường hợp nào?
A. Máy trạm mất Internet.
B. Cấp DHCP nhanh.
C. Rất hay dùng cho các máy Trạm Không Ổ Đĩa (Diskless Workstation) thời xưa. Khi bật máy lên, nó không có HĐH, không có IP. Nó mang cái MAC Card Mạng Gào Lên "Tôi là MAC XYZ, có máy chủ nào cấp IP cho tôi không để tôi tải HĐH về Boot mạng (PXE)?".
D. Xóa dữ liệu ổ cứng.
*Đáp án: C*
*Giải thích: RARP ngày nay đã bị tuyệt chủng và được thay thế hoàn hảo bởi DHCP (có tính năng cấp IP động kèm cả Option Boot File phục vụ PXE).*

**Câu 183:** Khái niệm "VLAN Pruning" (Cắt tỉa VLAN) trên Đường ống Trunking (802.1Q) nhằm tối ưu hệ thống Switch LAN bằng cách:
A. Tự động mã hóa cáp quang.
B. Bơm IP nội bộ cho toàn mạng.
C. Cấm các Gói Broadcast của VLAN X (Vd VLAN Kế toán) lan truyền lãng phí qua Đường Trunk sang các Switch KHÔNG CÓ BẤT KỲ CỔNG NÀO CỦA VLAN X ĐANG CẮM. Tiết kiệm băng thông đáng kể cho xương sống Trunking.
D. Xóa định tuyến BGP.
*Đáp án: C*
*Giải thích: Tránh kiểu rải rác: Phòng kế toán ở lầu 1 gửi Broadcast mà Switch lầu 10 cũng phải nhận trong khi lầu 10 toàn phòng IT.*

**Câu 184:** Tại sao thiết bị Switch L2 (Không hỗ trợ Routing) KHÔNG CẦN CÓ địa chỉ IP để làm chức năng chuyển mạch 24 cổng LAN?
A. Nó dùng mã P2P.
B. Switch L2 thuần túy chỉ "Nhìn" và "Lưu" Địa chỉ MAC để ném Frame. Nó mù lòa hoàn toàn với Tầng 3 (IP). Địa chỉ IP (Nếu được gán VLAN 1 Management) trên Switch chỉ phục vụ duy nhất 1 mục đích: Giúp Quản Trị Viên (Admin) Ping, SSH, Web GUI vào cấu hình thiết bị.
C. Tắt DHCP nội bộ.
D. Vì IP chạy ở Lớp 1.
*Đáp án: B*
*Giải thích: Switch chuyển mạch không dùng IP. Việc gán IP cho Switch chỉ là cái cổng hậu để người quản lý leo vào điều khiển cục Switch đó.*

**Câu 185:** Kỹ thuật Sửa Lỗi Tầng 2 "ARQ" (Automatic Repeat reQuest) được áp dụng MẠNH MẼ trên Môi trường truyền dẫn nào thay vì Ethernet?
A. Cáp đồng xoắn.
B. Wi-Fi (802.11). Môi trường vô tuyến quá độc hại, Lỗi Bit rách nát xảy ra như cơm bữa. Wi-Fi L2 BUỘC PHẢI DÙNG ACK. Nếu truyền xong 1 Frame mà Máy Đích không dội lại 1 Frame ACK Lớp 2 tức thời (SIFS), Máy Phát sẽ LẬP TỨC TRUYỀN LẠI Frame đó Ở TẦNG 2 mà KHÔNG CẦN ĐỢI TCP TẦNG 4 Timeout truyền lại (Cứu nguy độ trễ cực tốt).
C. Sóng Vệ tinh LEO.
D. Mạng dây LAN.
*Đáp án: B*
*Giải thích: Ethernet cáp quang/cáp đồng siêu sạch nên thả luôn không cần truyền lại. Wi-Fi quá dơ nên Lớp 2 phải ôm đồm sửa lỗi để che giấu bớt cái bẩn của Sóng vô tuyến trước mặt anh TCP sạch sẽ khó tính.*

**Câu 186:** Khi thiết lập "MAC Address Filtering" (Lọc MAC) trên Tường lửa, điểm Hạn chế LỚN NHẤT về Phân mảnh Mạng là:
A. MAC không qua được mạng 4G.
B. Nó làm chậm mạng 10 lần.
C. Tường lửa chỉ ĐỌC ĐƯỢC MAC NGUỒN CỦA CÁC MÁY TÍNH NẰM TRONG CÙNG 1 SUBNET L2 VỚI NÓ. Nếu máy tính đi qua 1 cục Router Lớp 3, MAC gốc của máy tính sẽ bị Đè Bỏ (Đổi thành MAC Router). Tường lửa vĩnh viễn không lọc được MAC từ Subnet khác dội tới.
D. Tường lửa bị cháy.
*Đáp án: C*
*Giải thích: Địa chỉ MAC chỉ sống trong cái AO LÀNG của mình. Ra biển lớn (qua Router), MAC bị lột vứt đi thay áo mới. Do đó Lọc MAC xuyên mạng là điều không tưởng.*

**Câu 187:** Giao thức Liên kết Tầng 2 nào dưới đây thường đóng gói IP để cung cấp Đường Truyền Ảo "PPPoE" (PPP over Ethernet) trong truy cập FTTH Internet Băng Rộng Cá Nhân?
A. UDP Header.
B. Một Giao Thức Lai. Bọc Gói PPP (Cung cấp Tính năng Yêu cầu Nhập Tài Khoản Mật Khẩu Tính Cước Nhà Mạng) VÀO TRONG một cái Bụng Frame Ethernet L2 Tiêu chuẩn. Tạo ra một Liên kết Điểm-Điểm Ảo chui qua cáp quang thụ động GPON về Tổng đài.
C. TCP Lớp 2.
D. OSPF Truyền hình cáp.
*Đáp án: B*
*Giải thích: Thủ thuật kết hợp lợi thế Rẻ tiền của Cáp LAN Ethernet (Card LAN) với Khả năng Quản lý Tính Tiền Đăng nhập An Toàn của PPP mạng WAN cũ.*

**Câu 188:** Tốc độ Xử Lý Mạch Nhanh của Cạc Mạng Máy Tính Thường Mất Bao Lâu Để Tính Xong Checksum CRC 32-bit (FCS) Ở Đuôi Gói Ethernet 1500 Byte?
A. Vài giây.
B. Vài chục Mili-giây (Chậm như TCP).
C. Nó được tính TOÁN SONG SONG BẰNG PHẦN CỨNG BẰNG DÒNG BIT TUÔN CHẢY (On-the-fly) khi Frame L2 vừa nhận dở. Thời gian tính toán = ZERO trễ (Hoàn tất gần như Ngay Lập Tức sau khi Bit cuối cùng nhảy vô Cạc Mạng). CPU Máy Tính Hoàn Toàn Rảnh Rang Không Bận Tâm Đến CRC Nhờ Con Chip Gánh Hết.
D. CPU bị đứng hình 1 phút.
*Đáp án: C*
*Giải thích: TCP Checksum phần lớn do CPU phần mềm tính (tốn tài nguyên). CRC L2 là đặc quyền đỉnh cao của Chip Sillicon (Hardware Offload) làm việc hộ Tầng trên.*

**Câu 189:** Thiết Bị "Tap" Mạng Phần Cứng (Network Tap) Phân Biệt Gì Với "Port Mirroring" (SPAN) Trên Switch L2 Khi Triển Khai Nghe Lén Cấp Cao (Network Forensics)?
A. Đổi mật khẩu Switch tự động.
B. Tắt điện cáp quang.
C. Cắm Thẳng Cục "Tap" Bằng Cáp Quang Y Splitter (Chia Chẻ Quang) Cắt Ngang Giữa 2 Thiết Bị. Tín Hiệu Ánh Sáng Chạy Qua Bị Chia Tách Ra 2 Bản Sao Bằng KHÚC XẠ VẬT LÝ, 100% Zero Delay (Không Gây Tải Trễ Cho Switch Như Port Mirror). Cực Kỳ Tuyệt Đối Bắt Sạch Rác Lỗi Layer 1/2 Mắt Trưởng Nhóm Soi Bất Khả Chống.
D. Nén dữ liệu IP thành UDP.
*Đáp án: C*
*Giải thích: Soi Gương Port Mirror bằng Mềm của Switch có thể bị Quá tải Rớt Gói nếu Luồng Đích bị Nghẽn. Cắm Y-Cable Vật Lý Quang (Tap) Là Tuyệt Đỉnh Gián Điệp L1 Bắt Hết Băng Chảy Sáng.*

**Câu 190:** Trong Hệ Thống Wi-Fi Doanh Nghiệp Cấu Hình CAPWAP L2/L3 Nối Từ Cục AP (Bộ Phát) Về WLC (Bộ Điều Khiển Mạng Tập Trung), Vai Trò Chuyển Mạch Data L2 Bị Đảo Lộn Ra Sao?
A. AP Không Cấp Mật Khẩu.
B. Cáp Đồng Tự Bóc IP Sóng Sửa MAC IP Nhập Đứt Báo Gãy Lưới Ác Chặn Tự Di.
C. CHẾ ĐỘ SPLIT MAC. Cục AP (Ngu Đần Hóa) Chỉ Lo Nhận Sóng Vô Tuyến. Bắt Được Gói Nào Là Bọc UDP Chạy Thẳng (Tunnel) Chui Trở Về Cục Não (Controller WLC) Nằm Ở Phòng Kế Toán. Cục WLC KIA MỚI LÀ THẰNG GIẢI MÃ, KIỂM TRA MẬT KHẨU, PHÂN VLAN VÀ ĐẨY RA MẠNG DÂY. AP Khỏi Lo Gì Giảm Kẹt Treo Cháy Tự Cấp Hỏng Chặn Vùng Khẩn Khéo IP.
D. Đổi DNS Trạm Thành IP Lõi Của Router Core Vệ Tinh Kém Khóa Xóa Kín Khớp Oan.
*Đáp án: C*
*Giải thích: Đưa Bộ Não Của Tầng L2 Wi-Fi Vào Trữ Tập Trung (Centralized Data Plane). Chống Hacker Trộm Cục AP Về Bẻ Mã Ổ Cứng, Dễ Cấu Hình Phân Luồng Roaming Mượt Vô Song Ở Chung 1 Cục Bự.*

**Câu 191:** Khi một Switch nhận được một Frame Quảng bá (Broadcast MAC `FF:FF:FF:FF:FF:FF`), nó sẽ KHÔNG làm hành động nào dưới đây?
A. Cập nhật bảng MAC dựa trên Source MAC của Frame.
B. Chuyển tiếp (Forward) Frame ra TẤT CẢ các cổng.
C. Chuyển tiếp Frame ra khỏi cổng mà nó vừa nhận Frame vào.
D. Xử lý phần dữ liệu Payload.
*Đáp án: C*
*Giải thích: Quy tắc chống dội ngược (Split Horizon cơ bản ở L2). Nhận cổng 1 thì phát 23 cổng còn lại, chứ không dội ngược lại cổng 1 làm nhiễu sóng chính cái máy vừa phát.*

**Câu 192:** Chức năng "Port Security" trên Switch sẽ phản ứng thế nào nếu số lượng địa chỉ MAC học được trên một cổng vượt quá giới hạn cấu hình (ví dụ: Limit = 1)?
A. Phát thêm MAC.
B. Cảnh báo lên màn hình.
C. Switch thực hiện Hành động Vi phạm (Violation action). Tùy cấu hình, nó có thể `Protect` (Chỉ thả các frame của MAC lạ, vẫn cho MAC đúng qua), `Restrict` (Như Protect nhưng gửi thêm Cảnh báo SNMP), hoặc nghiêm ngặt nhất là `Shutdown` (ĐÓNG SẬP CỔNG ĐÓ LẠI VÀ CHUYỂN TRẠNG THÁI ERR-DISABLED).
D. Bơm virus.
*Đáp án: C*
*Giải thích: Đây là cách Switch chống lại việc nhân viên lén cắm một cái Hub hay Switch rẻ tiền vào cổng tường để chia mạng cho nhiều máy lạ trong công ty.*

**Câu 193:** Chuẩn 802.1Q chèn một "VLAN Tag" (Nhãn 4 byte) vào Frame. Cấu trúc 4 byte này bao gồm TPID (2 byte) và TCI (2 byte). TPID luôn mang giá trị `0x8100`, vậy TCI chứa những thông tin gì quan trọng nhất?
A. MAC Address.
B. IP Address.
C. Chứa 3 bit Ưu tiên (PCP/CoS) để làm QoS L2, 1 bit CFI (Drop Eligible Indicator), và quan trọng nhất là 12 bit VLAN ID (Chứa số hiệu của VLAN từ 0-4095).
D. Chứa Port Number.
*Đáp án: C*
*Giải thích: Sự chặt chẽ của Header 802.1Q giúp Switch nhận diện chính xác mạng con và độ khẩn cấp của từng Frame đi qua đường Trunk.*

**Câu 194:** Hiện tượng "Asymmetric Routing" (Định tuyến bất đối xứng) có thể gây ra sự cố mất kết nối trong môi trường mạng có Tường lửa Stateful, bởi vì:
A. Cáp mạng bị xoắn lệch.
B. Gói tin đi (Request) qua Firewall A, Firewall A ghi nhận Session. Nhưng Gói tin về (Response) do BGP/OSPF định tuyến lại đi vòng qua Firewall B. Firewall B chưa từng thấy Request đi ra nên COI RESPONSE LÀ GÓI LẠ TRÁI PHÉP VÀ DROP MẤT. Phiên kết nối đứt gãy.
C. Tốc độ cáp chênh lệch 100 lần.
D. Đứt gãy cáp biển ngầm.
*Đáp án: B*
*Giải thích: Định tuyến bất đối xứng là ác mộng của Security. Đường đi và đường về trên Internet thường khác nhau, nhưng bắt buộc phải gặp nhau tại Nút Chặn Trạng Thái nếu không muốn bị khóa.*

**Câu 195:** Trong kiến trúc mạng LAN phân cấp (Hierarchical Network Design) của Cisco, lớp nào (Layer) chịu trách nhiệm chính việc nhóm kết nối các thiết bị người dùng cuối (PC, Điện thoại)?
A. Core Layer (Lớp Lõi).
B. Distribution Layer (Lớp Phân phối).
C. Access Layer (Lớp Truy cập). Gồm các Switch cung cấp trực tiếp các Port cắm dây mạng cho thiết bị đầu cuối, chịu trách nhiệm áp dụng Port Security, phân chia VLAN, PoE.
D. Internet Layer.
*Đáp án: C*
*Giải thích: Lớp Truy cập là "Cửa ngõ" đón khách. Lớp Phân phối là "Nút giao thông". Lớp Lõi là "Đường cao tốc siêu tốc".*

**Câu 196:** "Micro-segmentation" (Vi phân đoạn mạng) trong Data Center hiện đại giúp tăng cường an ninh bằng cách:
A. Rút ngắn độ dài cáp.
B. Giảm kích thước Frame.
C. Áp dụng chính sách Bảo mật L2/L3 (Tường lửa ảo) XUỐNG TẬN MỨC ĐỘ TỪNG CÁI MÁY ẢO (VM) HOẶC TỪNG CỔNG SWITCH (Zero Trust). Dù 2 máy ảo nằm CÙNG MỘT VLAN, nếu máy A nhiễm Virus, nó vẫn bị Tường lửa Tí Hon chặn không cho lây sang máy B kế bên.
D. Biến IPv4 thành IPv6.
*Đáp án: C*
*Giải thích: Đỉnh cao của Security hiện đại (Ví dụ VMware NSX). Xóa bỏ khái niệm "Vào được nhà (LAN) là an toàn", giờ đây từng phòng ngủ trong nhà đều có chốt khóa riêng.*

**Câu 197:** Kỹ thuật nào ở Tầng 2 giúp kết nối nhiều Switch Vật Lý lại với nhau để chúng hoạt động và quản lý NHƯ LÀ MỘT SWITCH ẢO DUY NHẤT (Logical Switch)?
A. VLAN Trunking.
B. Spanning Tree Protocol.
C. Switch Stacking (Ví dụ: Cisco StackWise) hoặc VSS/vPC. Giúp loại bỏ vòng lặp STP vì nhiều Switch được gộp não lại thành 1. Băng thông tăng, dự phòng cao, quản trị siêu nhàn.
D. Hub kết nối.
*Đáp án: C*
*Giải thích: Cắm 4 cục Switch rời rạc thành 1 cỗ máy 192 cổng đồng nhất. Lỗi đứt 1 cục thì 3 cục kia vẫn giữ mạng sống.*

**Câu 198:** Giao thức nào chuyên trách việc tự động dò tìm cấu hình (Auto-Discovery) Tầng 2 chỉ dành RIÊNG cho thiết bị của Hãng Cisco?
A. LLDP (Chuẩn mở).
B. OSPF.
C. CDP (Cisco Discovery Protocol). Giống LLDP, CDP phát đa hướng các gói thông tin cấu hình Switch/Router Cisco cho nhau. Quản trị viên hay Hacker dùng nó để "vẽ bản đồ" mạng nhanh chóng. Do đó thường bị Disable ở các cổng đối diện bên ngoài.
D. BGP.
*Đáp án: C*
*Giải thích: CDP là con dao hai lưỡi. Rất tiện cho Kỹ sư mạng chẩn đoán lỗi, nhưng lại là mỏ vàng cho Hacker trinh sát lấy IP, tên thiết bị, bản iOS.*

**Câu 199:** Tại sao giao thức truyền thông Đồng bộ (Synchronous) ở Lớp Vật Lý (L1/L2) lại cần Clock Signal (Xung nhịp)?
A. Để đếm số máy tính.
B. Để mã hóa mật khẩu.
C. Trong môi trường truyền liên tục không ngắt quãng (như SONET/SDH, Cáp quang lõi), 2 bên Nhận và Phát phải "Nhịp chân" hoàn toàn CÙNG MỘT TẦN SỐ THỜI GIAN CHUẨN XÁC, để máy nhận biết chính xác lúc nào lấy mẫu cắt bit 0/1 trên dòng sóng điện từ trôi tuột, không bị trượt khung lệch chữ.
D. Giảm băng thông Wi-Fi.
*Đáp án: C*
*Giải thích: Đồng bộ hóa Đồng hồ phần cứng là thứ tạo nên sự ổn định viễn thông Lớp Đáy. Lệch 1 nano-giây là sai bét cả đoạn dữ liệu.*

**Câu 200:** "BPDU Guard" (Bảo vệ Gói tin BPDU) được cấu hình trên Switch để cản trở hành động nào?
A. Cản Ping.
B. Chặn gói IP Broadcast.
C. Một Cổng Access nối ra máy trạm bình thường LẼ RA KHÔNG ĐƯỢC PHÉP CHỨA CÁC GÓI BPDU (Vì BPDU là gói báo hiệu STP của Switch với Switch). NẾU Cổng Access Bất Ngờ NHẬN ĐƯỢC 1 GÓI BPDU (Do Hacker cắm Switch rác vào hoặc Loop cáp), Cổng đó sẽ NGAY LẬP TỨC Khóa Sập Lại (Err-Disable) để bảo vệ Cây STP của mạng Lõi không bị bóp méo.
D. Chặn tải Torrent.
*Đáp án: C*
*Giải thích: Tính năng phòng thủ tối thượng chống lại những tay nhân viên táy máy tự đem Switch/Cục phát Wi-Fi rẻ tiền lên công ty cắm nối làm Loop sập toàn mạng LAN.*

**Câu 201:** Trong cấu trúc Ethernet Frame, địa chỉ MAC Đích (Destination MAC) được xếp ĐẦU TIÊN (Trước cả MAC Nguồn). Dụng ý thiết kế của việc này là gì?
A. Do thói quen.
B. Để đổi cáp mạng dễ hơn.
C. Hỗ trợ "Cut-through Switching". Switch Tầng 2 chỉ cần đọc lướt qua 6 Byte đầu tiên (Ngay khi Khung vừa chui vào) là ĐÃ BIẾT NÉM RA CỔNG NÀO, giúp nó Chuyển Mạch ngay lập tức mà không phải chờ Nuốt Hết Khung vào RAM. Tối ưu cực độ Tốc Độ Chuyển Tiếp (Latency).
D. Để che giấu IP.
*Đáp án: C*
*Giải thích: Một sự Sắp Đặt Cấu Trúc Khung Mạng Siêu Thông Minh mang tầm nhìn Xuyên Thế Kỷ của IEEE để tối ưu hóa thời gian thực (Real-time hardware forwarding).*

**Câu 202:** "Dịch Vụ Cố Gắng Hết Sức" (Best-Effort) của Tầng Liên Kết Nghĩa Là Gì Trên Ethernet?
A. Nó dùng TCP để truyền lại.
B. Ethernet (Lớp 2) KHÔNG BAO GIỜ đảm bảo gói tin (Frame) của bạn Sẽ Đến Đích, Không Đảm Bảo Thứ Tự, Không Truyền Lại Nếu Hỏng (CRC Sai Là Vứt). Nó CHỈ CỐ GẮNG Ném Khung Vào Sợi Dây Điện Một Cách Tốt Nhất Có Thể Rồi "Quên Luôn". Trách Nhiệm Đảm Bảo Thuộc Về Tầng Transport Bên Trên.
C. Ethernet mã hóa liên tục.
D. Cung cấp băng thông vô tận.
*Đáp án: B*
*Giải thích: Sự "Vô trách nhiệm" Của Cả Lớp 2 (Ethernet) Và Lớp 3 (IP) Làm Nền Tảng Giúp Phần Cứng Băng Tần Rộng Vận Hành Cực Nhẹ Nhàng Và Nhanh Đỉnh Chóp, Giữ Lại Bộ Não Phức Tạp Rườm Rà Nhất Nằm Trọn Ở Mép Rìa PC Lớp L4.*
