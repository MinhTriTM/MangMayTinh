# CHƯƠNG 4: TRẮC NGHIỆM TẦNG MẠNG (NETWORK LAYER)

**Câu 1:** Trong khái niệm mạng hiện đại, Data Plane (Mặt phẳng Dữ liệu) chịu trách nhiệm cho chức năng cơ bản nào của Router?
A. Định tuyến (Routing) tính toán toàn bộ bản đồ.
B. Chuyển tiếp gói tin (Forwarding) cục bộ từ cổng vào sang cổng ra của chính bộ định tuyến đó.
C. Cấp phát địa chỉ IP cho máy chủ.
D. Mã hóa luồng truyền thông.
*Đáp án: B*
*Giải thích: Data plane chỉ làm công việc "cơ bắp": nhặt gói tin ở ngõ vào, nhìn IP đích, tra Forwarding table và đẩy ra ngõ ra tương ứng (diễn ra trong vài nanosecond).*

**Câu 2:** Tầng Mạng (Network Layer) sử dụng đơn vị dữ liệu (PDU) được gọi là gì?
A. Segment
B. Frame
C. Datagram (Gói tin)
D. Message
*Đáp án: C*
*Giải thích: Tại Tầng mạng, Segment từ trên chuyển xuống được đóng gói IP Header tạo thành Datagram.*

**Câu 3:** Theo kiến trúc truyền thống, Bảng chuyển tiếp (Forwarding Table) của một Router được xây dựng từ đâu?
A. Do người dùng tự lập trình bằng tay.
B. Router ngẫu nhiên đoán đường.
C. Từ việc bộ định tuyến chạy các thuật toán định tuyến (Routing Algorithms) trong Mặt phẳng điều khiển (Control Plane).
D. Do nhà mạng gọi điện báo.
*Đáp án: C*
*Giải thích: Data Plane và Control Plane dù nằm chung trong con Router truyền thống, nhưng quá trình Control plane chạy các thuật toán (như OSPF, BGP) mới tính ra được bảng Forwarding table.*

**Câu 4:** Kiến trúc SDN (Software-Defined Networking) tách rời bộ phận nào ra khỏi Router vật lý?
A. Tách Data Plane ra khỏi Router, đặt trên mây.
B. Tách Control Plane (Não bộ định tuyến) ra khỏi Router vật lý và đem nó gộp lên các Máy chủ Điều khiển (Remote Controller) trung tâm bằng phần mềm.
C. Tách ăng ten thu phát Wi-Fi.
D. Tách RAM của Router.
*Đáp án: B*
*Giải thích: Trong SDN, Router trở thành các thiết bị đơn giản "dumb switches", chỉ biết tuân lệnh (OpenFlow) đẩy gói tin, còn phần thuật toán khổng lồ nằm ở Server tập trung.*

**Câu 5:** Thông số TTL (Time To Live) trong Header của IPv4 có công dụng lớn nhất là gì?
A. Chỉ định ngày giờ sản xuất gói tin.
B. Chống sự tồn tại lặp đi lặp lại vô hạn (Routing Loops) của một Datagram trên mạng do lỗi định tuyến sai bằng cách trừ 1 giá trị mỗi khi đi qua một Router.
C. Cảnh báo quá tải RAM cho máy chủ.
D. Tăng thời gian lưu trữ ở Router.
*Đáp án: B*
*Giải thích: Giả sử Router A định tuyến đến Router B, B lại bị lỗi chỉ ngược lại A. Gói tin sẽ chạy A-B-A-B mãi mãi. TTL = 64, mỗi lần qua router trừ 1, đến 0 thì gói tin bị tiêu diệt, trả lại băng thông cho Internet.*

**Câu 6:** Địa chỉ IPv4 có tổng độ dài bao nhiêu bits?
A. 16 bits
B. 32 bits
C. 64 bits
D. 128 bits
*Đáp án: B*
*Giải thích: IPv4 có 32 bit, thể hiện dưới dạng 4 con số từ 0-255 cách nhau bởi dấu chấm (ví dụ 192.168.1.1).*

**Câu 7:** Một mạng cục bộ có ký hiệu địa chỉ là `192.168.10.0/24`. Nếu mạng này không dùng Subnet nào khác, có tối đa bao nhiêu địa chỉ IP khả dụng có thể gán cho các thiết bị (Hosts)?
A. 256
B. 255
C. 254
D. 24
*Đáp án: C*
*Giải thích: Mạng /24 có 8 bit phần Host (32-24=8). Tổng IP là 2^8 = 256. Bỏ địa chỉ đầu (Network Address 192.168.10.0) và địa chỉ cuối (Broadcast 192.168.10.255), còn 254 IP khả dụng.*

**Câu 8:** Bạn vừa cắm cáp mạng vào máy tính mới. Máy tính sẽ dùng giao thức Tầng Ứng dụng nào để xin tự động một địa chỉ IP nội bộ, Subnet mask, Default Gateway từ mạng đó?
A. NAT
B. ARP
C. DHCP (Dynamic Host Configuration Protocol)
D. ICMP
*Đáp án: C*
*Giải thích: DHCP là giao thức cấp phát địa chỉ IP động cho mạng nội bộ hoạt động theo nguyên tắc DORA (Discover, Offer, Request, ACK).*

**Câu 9:** Chức năng NAT (Network Address Translation) giải quyết khủng hoảng thiếu địa chỉ IPv4 toàn cầu thông qua cách nào?
A. Tự động chuyển đổi máy tính dùng IPv4 sang IPv6.
B. Nén nội dung gói tin lại.
C. Cho phép toàn bộ mạng LAN nội bộ phía sau Router (dùng Private IP 192.168.x.x) ẩn đi, chỉ đại diện duy nhất bởi 1 IP Public của Router khi giao tiếp với Internet. Router ánh xạ các máy nội bộ này bằng Số hiệu Cổng (Port).
D. Chặn các quảng cáo để giảm lưu lượng.
*Đáp án: C*
*Giải thích: Nhờ NAT, hàng triệu nhà mạng, công ty chỉ cần tốn 1 vài IP Public, còn hàng tỷ thiết bị bên trong dùng IP Private không đụng hàng với ai ngoài Internet.*

**Câu 10:** Quá trình "IP Fragmentation" (Phân mảnh IP) diễn ra khi nào?
A. Khi gói tin muốn mã hóa làm nhiều mảnh.
B. Khi kích thước Datagram quá lớn, vượt qua mức giới hạn truyền tải tối đa (MTU) của liên kết phía trước, bắt buộc Router phải băm Datagram gốc thành nhiều phần nhỏ hơn.
C. Khi đường cáp bị đứt làm đứt gói tin.
D. Khi tín hiệu Wi-Fi yếu đi.
*Đáp án: B*
*Giải thích: Ethernet thường có MTU = 1500 bytes. Nếu Datagram 4000 bytes lao tới, Router phải dùng cờ Fragmentation Offset băm nhỏ Datagram ra mới đẩy lọt đường ống đó.*

**Câu 11:** Trong quy trình Phân mảnh IP (IP Fragmentation), các mảnh vỡ của gói tin sẽ được ráp nối lại (Reassembly) nguyên vẹn tại đâu?
A. Tại Router trạm kế tiếp.
B. Tại Mọi Router trên đường dẫn.
C. Tại Thiết bị nhận cuối cùng (Destination Host).
D. Tại Switch.
*Đáp án: C*
*Giải thích: Để các Router lõi hoạt động cực nhanh, nhà thiết kế mạng đẩy gánh nặng ráp mảnh vỡ (Reassembly) về phía thiết bị nhận (End-system) cuối cùng, dựa theo ID của gói tin.*

**Câu 12:** So với IPv4, giao thức IPv6 có thay đổi mang tính cách mạng nào dưới đây?
A. IPv6 hỗ trợ phân mảnh ở Router linh hoạt hơn IPv4.
B. Địa chỉ IP mở rộng từ 32 bit lên 128 bit, Header cố định 40 byte và LOẠI BỎ hoàn toàn trường Header Checksum lẫn việc Phân mảnh ở Router nhằm tăng tốc độ xử lý.
C. IPv6 không dùng được cho các thiết bị di động.
D. IPv6 ghép MAC và IP làm một.
*Đáp án: B*
*Giải thích: IPv6 tối giản để xử lý siêu tốc, không cần Checksum (do Tầng 2, 4 làm rồi). Cấm phân mảnh: Gói quá to thì drop, gửi lỗi ICMP về bắt thằng gửi tự chia nhỏ.*

**Câu 13:** "Đường hầm" (Tunneling) là một chiến lược phổ biến trong mạng tầng 3 để giải quyết vấn đề gì?
A. Cho phép kết nối 2 thiết bị không dùng chung dải IP.
B. Truyền gói tin IPv6 vượt qua các khu vực toàn là Router thế hệ cũ chỉ hiểu IPv4 bằng cách đóng gói nguyên con Datagram IPv6 nhét vào trong Payload của Datagram IPv4.
C. Mã hóa kết nối TCP cục bộ.
D. Bảo vệ đường cáp vật lý.
*Đáp án: B*
*Giải thích: Tunneling lừa các router IPv4 cũ bằng cách ngụy trang IPv6 thành tải trọng (Payload) mang bởi xe tải IPv4.*

**Câu 14:** Giao thức định tuyến nội vùng (Intra-AS) "OSPF" sử dụng dạng thuật toán định tuyến nào làm nền tảng?
A. Distance Vector (Ví dụ: phương trình Bellman-Ford).
B. Link State (Trạng thái liên kết - Sử dụng thuật toán tìm đường ngắn nhất Dijkstra trên biểu đồ có sẵn).
C. BGP Policy Routing.
D. K-Nearest Neighbor.
*Đáp án: B*
*Giải thích: OSPF bắt mọi Router phát tán bản tin Broadcast toàn mạng (LSA). Cuối cùng, mọi Router nắm trong tay bản đồ chi tiết của toàn mạng rồi tự chạy thuật toán Dijkstra để vẽ đường ngắn nhất.*

**Câu 15:** Trái ngược với Link State, thuật toán định tuyến Distance Vector (như RIP) có đặc điểm gì?
A. Router phải tải toàn bộ bản đồ Internet.
B. Router không có tầm nhìn toàn cục. Nó chỉ biết thông tin từ các router láng giềng kề sát vách, chia sẻ qua lại các bảng ước tính khoảng cách, và dùng phương trình quy hoạch động Bellman-Ford để cập nhật đường đi.
C. Có tốc độ chạy nhanh hơn Dijkstra hàng trăm lần.
D. Tuyệt đối không bao giờ bị lỗi lặp vòng định tuyến (Routing loop).
*Đáp án: B*
*Giải thích: Distance Vector giống như việc hỏi đường người dân dọc đường, không ai có bản đồ cả nhưng truyền miệng nhau sẽ tính ra khoảng cách. Tuy nhiên nó dễ bị hiện tượng "Tin dữ truyền chậm" (Count to infinity).*

**Câu 16:** Hiện tượng "Đếm đến vô cực" (Count-to-infinity) trong mạng máy tính là gì?
A. Vòng lặp đếm địa chỉ MAC không dừng.
B. Là lỗi của thuật toán Link State khi dùng thuật toán Dijkstra sai lệch trọng số.
C. Lỗi kinh điển của thuật toán Distance Vector, khi một liên kết bị đứt (chi phí tăng vọt), các router lân cận trao đổi các ước lượng sai lạc vòng quanh nhau, khiến khoảng cách đường đi tăng từ từ đến vô cực.
D. Bộ nhớ của router đếm số IP hết giới hạn.
*Đáp án: C*
*Giải thích: Khi cáp đứt, A không báo "Đường hỏng rồi", B tưởng đường cũ qua A vẫn ngon, A lại tưởng B còn đường khác. Cả hai cứ cộng dồn chi phí mãi.*

**Câu 17:** Giao thức nào là "Chất keo dính" duy nhất định tuyến các mạng liên vùng (Inter-AS Routing), kết nối các mạng của các ISP trên toàn thế giới với nhau?
A. OSPF
B. RIP
C. BGP (Border Gateway Protocol)
D. SDN
*Đáp án: C*
*Giải thích: BGP chịu trách nhiệm định tuyến giữa Hệ thống tự trị Viettel với Hệ thống tự trị AT&T Mỹ, quy mô toàn cầu.*

**Câu 18:** Khác với OSPF chỉ quan tâm đến tốc độ/chi phí đường truyền, giao thức BGP định tuyến dựa trên yếu tố trọng yếu nào?
A. Chiều dài cáp quang là duy nhất.
B. Khoảng cách địa lý vật lý (GPS).
C. Các chính sách về mặt chính trị và kinh tế (Policy Routing), ví dụ: AS không muốn làm phương tiện trung chuyển miễn phí cho AS đối thủ.
D. Thuật toán Dijkstra.
*Đáp án: C*
*Giải thích: BGP mang bản chất của kinh doanh. Đường ngắn nhất chưa chắc được chọn nếu đi đường đó tốn nhiều tiền cước thuê nhà mạng đối thủ.*

**Câu 19:** Các bản ghi quảng bá (BGP Advertisements) truyền thông điệp cốt lõi gì cho các Router BGP khác?
A. Báo hiệu bị tấn công DDoS.
B. Chia sẻ băng thông cục bộ.
C. "Reachability" (Khả năng tiếp cận): Tôi có thể dẫn gói tin đi đến Dải mạng Subnet X thông qua danh sách các AS-PATH này.
D. Truyền lại khóa mật mã.
*Đáp án: C*
*Giải thích: BGP quảng bá tuyến đường: "Đường tới mạng của Đại học Bách Khoa có thể đi qua tôi (AS1) rồi đến AS2, AS3".*

**Câu 20:** Khi một Router BGP biên (Gateway) học được đường đi tới một mạng ngoài từ BGP, nó dùng giao thức nội bộ nào để thông báo cho các Router bên TRONG tổ chức của nó biết lối ra?
A. eBGP (External BGP)
B. iBGP (Internal BGP)
C. SNMP
D. ICMP
*Đáp án: B*
*Giải thích: Sau khi Router biên đứng ngoài cổng nhận tin từ eBGP, nó rải tin đó cho anh em trong nhà thông qua các session iBGP.*

**Câu 21:** Ping và Traceroute là hai công cụ chuẩn đoán mạng vô cùng phổ biến. Cả hai hoạt động dựa trên cơ chế của giao thức nào?
A. ARP
B. TCP
C. UDP
D. ICMP (Internet Control Message Protocol)
*Đáp án: D*
*Giải thích: ICMP là "công cụ gỡ rối" của IP. Ping gửi các gói Echo Request để chờ ICMP Echo Reply báo mạng đang sống.*

**Câu 22:** Công cụ Traceroute thực hiện vẽ bản đồ đường đi của gói tin tới đích bằng một "mẹo" thông minh nào?
A. Dùng GPS của máy gửi.
B. Cố tình gửi các gói tin có giá trị TTL (Time-To-Live) lần lượt tăng dần: 1, 2, 3... Khi mỗi gói tin chết ở một Router nào đó, Router đó sẽ gửi thông điệp báo lỗi ICMP (Time Exceeded) về, nhờ vậy lộ diện địa chỉ IP của Router đó.
C. Mã hóa toàn bộ đường truyền.
D. Yêu cầu từng Router chụp ảnh cấu hình gửi về.
*Đáp án: B*
*Giải thích: Lần đầu gửi TTL=1, tới trạm đầu tiên chết, trạm báo về. Lần 2 gửi TTL=2, tới trạm 2 chết, trạm 2 báo về. Cứ thế, Traceroute lần ra toàn bộ các chặng.*

**Câu 23:** Sự phân biệt rõ nhất giữa eNodeB (Mạng 4G) và Router BGP (Internet Core) là gì?
A. Cả hai đều thuộc về Control Plane.
B. BGP là mạng có dây, eNodeB là không dây.
C. eNodeB quản lý Mạng Truyền dẫn Vô tuyến, cung cấp truy cập vật lý cho thiết bị di động, còn BGP định tuyến logic cho toàn bộ gói tin đi trên lõi cáp quang toàn cầu.
D. Không có khác biệt vì chúng dùng chung một dải băng tần.
*Đáp án: C*
*Giải thích: Vị trí của eNodeB là ở Access Network (Rìa), trong khi BGP cấu trúc mạng Network Core (Lõi).*

**Câu 24:** Nếu Data Plane được thực thi bằng phần cứng tốc độ rất cao (như FPGA/ASIC), thì Control Plane trong các Router truyền thống được chạy ở đâu?
A. Trong dây cáp mạng.
B. Bằng phần mềm trên bộ vi xử lý (CPU) đa dụng tích hợp bên trong bộ định tuyến đó, tốc độ có thể chậm hơn phần cứng.
C. Trên máy chủ Google.
D. Không cần thiết phải có.
*Đáp án: B*
*Giải thích: Control plane yêu cầu giải các bài toán quy hoạch động, thuật toán đồ thị rất phức tạp. Nó cần CPU chạy hệ điều hành (như Cisco IOS) thay vì phần cứng cứng.*

**Câu 25:** Vì sao NAT lại bị coi là vi phạm nghiêm trọng tính kiến trúc phân tầng gốc của Internet?
A. Vì nó gây ô nhiễm sóng vô tuyến.
B. Vì router (thiết bị Tầng 3 - Tầng Mạng) lại xâm phạm vào việc lấy thông tin và thay đổi cả Số hiệu Cổng (Port Number - vốn thuộc độc quyền Tầng 4 - Tầng Giao Vận) của gói tin.
C. Vì nó quá đắt tiền.
D. Vì không dùng được IPv6.
*Đáp án: B*
*Giải thích: Nguyên lý thiết kế ban đầu là Tầng nào xử lý Tầng đó. Router chỉ được bóc tới lớp IP, cấm sờ vào Port của TCP/UDP. Nhưng NAT vì lý do sinh tồn phải sửa Port.*

**Câu 26:** Mạng nào dưới đây thuộc địa chỉ Private IP do IANA quy định, không thể định tuyến tự do ngoài Internet toàn cầu?
A. 8.8.8.8
B. 10.0.0.0/8
C. 142.250.0.0/16
D. 210.245.0.0/24
*Đáp án: B*
*Giải thích: Các dải IP Private thông dụng gồm 10.0.0.0/8, 172.16.0.0/12, và 192.168.0.0/16. Chúng được dùng ở mạng LAN đằng sau cục NAT router.*

**Câu 27:** Các thiết bị phần cứng thực thi Tường lửa Lọc gói tin (Packet Filter Firewall) cần can thiệp kiểm tra đến tầng nào trong mô hình mạng?
A. Chỉ kiểm tra tầng vật lý (Physical).
B. Kiểm tra tầng Liên kết (Data Link).
C. Kiểm tra tầng Mạng (Network) và tầng Giao vận (Transport) để xem xét các quy tắc IP Nguồn/Đích và Cổng Nguồn/Đích.
D. Kiểm tra sâu vào tầng Ứng dụng (Application).
*Đáp án: C*
*Giải thích: Tường lửa lọc thông thường phải bóc đến lớp IP (Tầng 3) và TCP/UDP (Tầng 4) để thực thi nguyên tắc Allow/Drop (VD: Cấm IP 10.0.0.5 truy cập Port 80).*

**Câu 28:** Trong Bảng Định Tuyến OSPF, "Cost" (Chi phí) của một liên kết thường được quản trị viên đặt tỷ lệ nghịch với thông số nào?
A. Độ dài vật lý của cáp.
B. Tốc độ/Băng thông của liên kết đó.
C. Địa chỉ IP của cáp.
D. Phiên bản của hệ điều hành.
*Đáp án: B*
*Giải thích: Liên kết có băng thông càng cao (như cáp quang 10Gbps) thì chi phí (Cost) càng thấp, OSPF sẽ ưu tiên chọn những liên kết này làm đường đi.*

**Câu 29:** Điều gì làm cho IPv6 không hoàn toàn tương thích ngược với IPv4, dẫn đến quá trình chuyển đổi gian nan?
A. IPv6 viết địa chỉ bằng chữ cái.
B. Độ dài Header của IPv6 (40 bytes cố định) và cấu trúc các trường hoàn toàn khác với Header của IPv4 (20 bytes biến đổi). Router IPv4 thuần túy nhìn gói IPv6 sẽ không hiểu gì.
C. IPv6 không hoạt động trên cáp quang.
D. IPv6 yêu cầu dùng trình duyệt mới.
*Đáp án: B*
*Giải thích: Sự thay đổi cốt lõi trong phần móng của giao thức khiến các thiết bị phần cứng cũ bị mù màu khi gặp IPv6, phải dùng đường hầm (Tunneling).*

**Câu 30:** Một Router OSPF trong tổ chức bỗng nhiên bị hỏng dây mạng. Nó sẽ xử lý theo cơ chế gì?
A. OSPF tự động sửa dây.
B. Không làm gì, để mặc gói tin thất lạc.
C. Gửi bản tin trạng thái liên kết (Link State Update) phát tán Broadcast tới toàn bộ mạng nội bộ, báo tin xấu để các Router khác cập nhật lại cơ sở dữ liệu và chạy lại thuật toán Dijkstra tìm đường tránh khúc hỏng.
D. Tự động chuyển sang BGP.
*Đáp án: C*
*Giải thích: OSPF rất nhạy cảm với thay đổi cấu trúc mạng lưới (topology). Bản tin báo cáo sẽ làm mạng hội tụ (converge) lại đường đi mới khá nhanh.*

**Câu 31:** Tầng mạng (Network Layer) phân thành 2 mặt phẳng riêng biệt. Chức năng chính của Mặt phẳng dữ liệu (Data plane) là gì?
A. Phân giải tên miền thành địa chỉ IP.
B. Tính toán và xác định đường đi tốt nhất (định tuyến) từ nguồn đến đích thông qua các thuật toán OSPF, BGP.
C. Nhận một gói tin (datagram) đang đến trên một liên kết đầu vào của router và chuyển tiếp (forward) nó đến liên kết đầu ra phù hợp.
D. Sửa lỗi bit trên cáp mạng.
*Đáp án: C*
*Giải thích: Data plane lo việc chuyển tiếp (forwarding) cục bộ tại TỪNG BỘ ĐỊNH TUYẾN. Control plane (mặt phẳng điều khiển) lo việc định tuyến (routing) trên TOÀN LƯỚI MẠNG.*

**Câu 32:** Nếu Mặt phẳng dữ liệu (Data plane) được thực hiện bằng phần cứng (chip chuyên dụng trong Router), thì Mặt phẳng điều khiển (Control plane) thường được thực hiện ở đâu trong mô hình truyền thống?
A. Trong tầng Liên kết dữ liệu.
B. Bằng phần mềm (software) chạy trên bộ vi xử lý (CPU) bên trong chính các bộ định tuyến (Router) đó.
C. Tại một máy chủ đám mây của Google.
D. Bằng các giao thức vật lý.
*Đáp án: B*
*Giải thích: Theo truyền thống (Per-router control), mỗi router tự thân vận động tính toán đường đi. Các bộ não (CPU) của router nói chuyện với nhau qua giao thức OSPF/BGP để tự xây dựng bảng định tuyến.*

**Câu 33:** Mô hình SDN (Software-Defined Networking) tạo ra một cuộc cách mạng ở Tầng Mạng bằng cách:
A. Tích hợp chặt chẽ Control plane và Data plane vào một con chip duy nhất.
B. Chuyển toàn bộ dữ liệu qua không dây.
C. Bóc tách mặt phẳng điều khiển (Control plane) ra khỏi Router vật lý và đưa lên một Máy chủ Điều khiển Tập trung (Logically Centralized Controller).
D. Bỏ sử dụng địa chỉ IP.
*Đáp án: C*
*Giải thích: SDN biến Router thành một "thiết bị ngốc nghếch" chỉ biết chuyển tiếp dữ liệu nhanh nhất có thể. Mọi quyền tính toán, ra quyết định đều nằm ở bộ não Controller tập trung từ xa.*

**Câu 34:** Sự khác biệt cốt lõi giữa IP Datagram của Tầng mạng và TCP Segment của Tầng giao vận là:
A. Datagram lớn hơn Segment.
B. Datagram chứa địa chỉ IP Nguồn & Đích, Segment chứa Port Nguồn & Đích.
C. Datagram được bảo mật, Segment không bảo mật.
D. Không có khác biệt.
*Đáp án: B*
*Giải thích: Segment giải quyết bài toán Process-to-Process (Port). Datagram bọc cái Segment đó lại để giải bài toán Host-to-Host (IP).*

**Câu 35:** Tại sao nói Tầng mạng của Internet (Giao thức IP) cung cấp dịch vụ "Cố gắng hết sức" (Best-effort)?
A. IP cung cấp chất lượng mạng tốt nhất thế giới.
B. Tốc độ ánh sáng là cố gắng lớn nhất của IP.
C. IP KHÔNG ĐẢM BẢO gói tin sẽ đến đích, không đảm bảo đến đúng thứ tự, cũng không đảm bảo băng thông tối thiểu hay độ trễ.
D. IP luôn truyền lại gói tin khi bị mất.
*Đáp án: C*
*Giải thích: IP rất đơn giản và "vô trách nhiệm", chỉ làm việc duy nhất là vận chuyển theo bảng chỉ đường. Sự đơn giản này giúp mạng Internet có thể mở rộng khổng lồ với chi phí thấp (sự tin cậy đẩy lên cho TCP).*

**Câu 36:** Để Router thực hiện chức năng Chuyển tiếp (Forwarding), nó tra cứu Bảng nào bên trong bộ nhớ?
A. Bảng ARP (ARP Table).
B. Bảng DNS.
C. Bảng Chuyển tiếp (Forwarding Table / FIB - Forwarding Information Base).
D. Bảng Kết nối TCP.
*Đáp án: C*
*Giải thích: Router đối chiếu địa chỉ IP đích của Datagram vào Bảng chuyển tiếp để tìm ra Cổng giao diện (Interface) cần đẩy gói tin ra.*

**Câu 37:** Khi một Router có 4 cổng (interfaces). Nếu một gói tin đi vào cổng 1, quá trình Router đẩy nó ra cổng 2, cổng 3 hay cổng 4 được gọi là:
A. Routing (Định tuyến).
B. Switching / Forwarding (Chuyển mạch / Chuyển tiếp).
C. Subnetting (Chia mạng con).
D. Congestion Control (Kiểm soát tắc nghẽn).
*Đáp án: B*
*Giải thích: Forwarding là hành động "bốc vác" cục bộ tại 1 nút (Kéo dài vài nanosecond bằng phần cứng). Routing là hành động "vẽ bản đồ" toàn cục (Kéo dài vài giây bằng phần mềm).*

**Câu 38:** Nguyên tắc đối chiếu "Longest Prefix Match" (Khớp tiền tố dài nhất) của Router khi tra Bảng Chuyển tiếp có nghĩa là gì?
A. Chọn đường đi có số lượng gói tin lớn nhất.
B. Router sẽ so sánh IP đích của gói tin với các dải mạng trong Bảng, nếu IP đích khớp (match) với nhiều dải mạng, nó sẽ ưu tiên chuyển tiếp gói tin theo dòng (entry) có MẶT NẠ MẠNG (Subnet Mask) DÀI NHẤT (cụ thể nhất).
C. Ưu tiên địa chỉ IP có số lớn nhất.
D. Ưu tiên cáp quang dài nhất.
*Đáp án: B*
*Giải thích: Ví dụ: Gói tin đích 200.23.16.5. Bảng có 2 dòng: `200.23.0.0/16` (đi cổng 1) và `200.23.16.0/21` (đi cổng 2). IP trên đều thuộc 2 dải này. Nhưng Router chọn đi cổng 2 vì độ dài Prefix /21 > /16 (Càng dài càng chi tiết).*

**Câu 39:** Trong kiến trúc bên trong của một Router vật lý (như thiết bị Cisco/Juniper), thành phần "Switching Fabric" (Mạng lưới chuyển mạch) đóng vai trò:
A. Cắm dây cáp.
B. Xử lý thuật toán OSPF/BGP.
C. Là một "siêu xa lộ" mạch tích hợp bên trong nằm giữa các cổng Input và các cổng Output, với nhiệm vụ vận chuyển gói tin từ cổng vào sang đúng cổng ra ở tốc độ cực cao.
D. Ngăn cản tấn công Hacker.
*Đáp án: C*
*Giải thích: Các Router lớn không dùng CPU để chuyển gói tin từ cổng này sang cổng kia (quá chậm). Chúng dùng phần cứng Switching Fabric (dạng Bus, Memory, hoặc Crossbar) có thể đạt tốc độ hàng Terabits/s.*

**Câu 40:** Khi cổng vào (Input port) của một Router nhận gói tin đến NHANH HƠN tốc độ mà Switching Fabric có thể vận chuyển nó sang cổng ra, hiện tượng gì sẽ xảy ra?
A. Tự đổi định tuyến.
B. Gói tin bị đẩy thẳng ra mạng.
C. Các gói tin phải xếp hàng đọng lại tại Bộ đệm (Queue) của Cổng vào (Input Queue). Nếu tràn, sẽ xảy ra rớt gói (Packet Loss).
D. Gói tin được nén tự động.
*Đáp án: C*
*Giải thích: Bộ đệm có mặt ở cả cổng vào và cổng ra của Router để hấp thụ các "cú sốc" do tốc độ luồng dữ liệu đến/đi không đồng đều.*

**Câu 41:** Hiện tượng Head-of-Line (HOL) Blocking thường xảy ra ở bộ đệm nào của Router có kiến trúc chuyển mạch kiểu cũ?
A. Bộ đệm cổng ra (Output Queue).
B. Bộ đệm cổng vào (Input Queue).
C. Bộ đệm CPU.
D. Bộ đệm hệ điều hành.
*Đáp án: B*
*Giải thích: Khi 2 gói tin ở đầu 2 hàng đợi (Input Queue 1 và 2) cùng muốn ra Output Queue A. Fabric chuyển mạch chỉ cho 1 gói đi, gói kia bị chặn. Gói phía sau gói bị chặn (dù muốn đi ra Output Queue B đang trống) cũng đành nằm chờ vô ích (HOL).*

**Câu 42:** "Active Queue Management" (AQM) là một thuật toán của Router để cải thiện TCP. AQM thực hiện chiến thuật nào dưới đây?
A. Tắt Router lúc ban đêm.
B. Tăng bộ nhớ RAM router lên vô cực.
C. Chủ động loại bỏ (Drop) sớm một số gói tin ngay cả khi Hàng đợi CHƯA ĐẦY, nhằm "báo hiệu khéo" cho máy gửi TCP biết mạng đang hơi kẹt, TCP tự giảm tốc trước khi Hàng đợi thực sự bị ngập lụt.
D. Xóa định dạng IPv4.
*Đáp án: C*
*Giải thích: Ví dụ kinh điển của AQM là thuật toán RED (Random Early Detection). Nhờ Drop ngẫu nhiên sớm, TCP phản ứng phanh sớm, giúp hàng đợi luôn ở mức thấp, giảm Độ trễ (Ping) đáng kể.*

**Câu 43:** Kích thước tiêu chuẩn của Header IPv4 (khi không có các Options) là:
A. 8 bytes
B. 16 bytes
C. 20 bytes
D. 40 bytes
*Đáp án: C*
*Giải thích: Bằng đúng kích thước chuẩn của Header TCP. Một TCP Segment trần trụi bọc trong IP thì đầu cước luôn là 40 Bytes.*

**Câu 44:** Trong IP Header, trường "TOS" (Type of Service) hay còn gọi là Differentiated Services (DiffServ) dùng để:
A. Đếm số lần đi qua Router.
B. Đánh dấu độ ưu tiên của Datagram (Vd: Đây là Voice Call ưu tiên Cao, đây là File Tải ưu tiên Thấp) để Router quyết định gói nào đi trước, gói nào chờ.
C. Khai báo mật khẩu mạng.
D. Đổi MAC sang IP.
*Đáp án: B*
*Giải thích: Trong thời đại IoT và Video Call, QoS (Chất lượng dịch vụ) cực kỳ quan trọng. Các gói Real-time sẽ được gán Differentiated Services Code Point (DSCP) ưu tiên cao nhất.*

**Câu 45:** Để đảm bảo một gói tin IP bị định tuyến sai (bị lặp vòng tròn giữa 2 Router A-B-A-B-A) không lởn vởn mãi mãi trên mạng, giao thức IPv4 thiết kế trường nào?
A. Protocol
B. Fragment Offset
C. Time to Live (TTL)
D. Header Checksum
*Đáp án: C*
*Giải thích: Nguồn khởi tạo TTL = 64 (hoặc 128/255). Qua mỗi Router, TTL trừ đi 1. Vòng lặp A-B 64 lần thì TTL = 0, Router tàn nhẫn kết liễu gói tin để dọn rác mạng.*

**Câu 46:** Giao thức mạng IPv4 có độ dài địa chỉ là 32-bit. Có khoảng bao nhiêu địa chỉ IP được tạo ra trên lý thuyết?
A. Hơn 4 Tỷ (2^32).
B. Hơn 10 Tỷ.
C. Khoảng 4 Triệu.
D. 340 Tỷ Tỷ Tỷ.
*Đáp án: A*
*Giải thích: 4.3 tỷ IP không đủ cho 8 tỷ dân số thế giới (chưa tính vạn vật IoT), do đó NAT và IPv6 phải ra đời.*

**Câu 47:** Một địa chỉ IP được chia làm hai phần chính (Hierarchy) nhờ vào Subnet Mask (Mặt nạ mạng) là những phần nào?
A. Phần Quốc gia và Phần Tỉnh thành.
B. Phần MAC và Phần Cổng.
C. Phần Network (Mạng) và Phần Host (Máy chủ/Đầu cuối).
D. Phần TCP và Phần UDP.
*Đáp án: C*
*Giải thích: IP giống như địa chỉ nhà. Phần Network là "Tên Đường/Phường" (Ví dụ 192.168.1), Phần Host là "Số nhà" (Ví dụ .100) trên con đường đó.*

**Câu 48:** Ký hiệu Subnet Mask chuẩn CIDR dạng "192.168.1.0/24" có ý nghĩa gì?
A. Có 24 máy tính trong mạng.
B. Băng thông tối đa 24 Mbps.
C. 24 bit đầu tiên tính từ trái sang phải của địa chỉ IP được cố định làm phần Mạng (Network ID), 8 bit còn lại dành cho phần Host.
D. Mạng này dùng cổng số 24.
*Đáp án: C*
*Giải thích: CIDR (Classless Inter-Domain Routing) đã chấm dứt kỷ nguyên chia lớp IP (Class A,B,C) cứng nhắc. 24 bit mạng nghĩa là Subnet Mask ở dạng thập phân là 255.255.255.0.*

**Câu 49:** Với dải mạng 192.168.1.0/24, số lượng Địa chỉ IP có thể GÁN (Usable) cho các máy tính là bao nhiêu?
A. 256
B. 254
C. 255
D. 128
*Đáp án: B*
*Giải thích: 8 bit Host cho 2^8 = 256 địa chỉ (Từ 0 đến 255). Trừ đi 2 địa chỉ đặc biệt: .0 (Địa chỉ đại diện cho Mạng - Network Address) và .255 (Địa chỉ Quảng bá Broadcast - ai cũng nghe), còn lại 254 thiết bị dùng được.*

**Câu 50:** Tổ chức máy chủ doanh nghiệp xin cấp được khối địa chỉ 200.23.16.0/20. ISP có thể cấp bao nhiêu IP hợp lệ cho doanh nghiệp này?
A. 4094
B. 1022
C. 2046
D. 254
*Đáp án: A*
*Giải thích: Phần host còn 32 - 20 = 12 bits. Tổng số IP = 2^12 = 4096. Trừ đi địa chỉ Mạng và Broadcast => 4094 IP khả dụng.*

**Câu 51:** Tính chất "IP Fragmentation" (Phân mảnh IP) xảy ra do:
A. Lỗi cáp quang.
B. Router nhận một gói IP có kích thước LỚN HƠN giới hạn Truyền tải tối đa (MTU) của đoạn đường cáp (Link) tiếp theo. Router cắt gói đó ra thành nhiều Gói IP nhỏ lẻ (Fragments).
C. Để chống vi rút.
D. Thay đổi DNS.
*Đáp án: B*
*Giải thích: Ví dụ gói 4000 Bytes đi qua cáp MTU 1500 Bytes. Router phải chẻ thành 3 gói nhỏ. Việc chẻ này cực kỳ tốn CPU của Router.*

**Câu 52:** Sau khi Phân mảnh IP (Fragmentation) bị chẻ nhỏ dọc đường ở Router trung gian, việc "Lắp ráp lại" (Reassembly) chúng thành gói ban đầu diễn ra ở đâu?
A. Ở Router kế tiếp.
B. Ở Máy chủ DNS.
C. Ở Tường lửa.
D. CHỈ ĐƯỢC THỰC HIỆN TẠI HỆ THỐNG ĐÍCH CUỐI CÙNG (Destination Host).
*Đáp án: D*
*Giải thích: Mạng giữ nguyên tắc "Nhanh gọn" cho Router. Đã băm ra là ném đi luôn, không có Router nào rảnh đi chờ ghép lại. Chỉ cái máy tính người dùng ở cuối cùng mới có RAM để chờ gom đủ các mảnh xếp lại hình.*

**Câu 53:** Để Máy nhận có thể lắp ráp các mảnh (Fragments) IP lại với nhau chính xác, nó dựa vào 3 trường thông tin nào trong Header IP của các mảnh nhỏ đó?
A. Port, MAC, Length.
B. ID định danh gốc, Cờ (Flags), và Độ lệch (Offset).
C. IP Nguồn, TTL, Checksum.
D. Password, Protocol, TOS.
*Đáp án: B*
*Giải thích: ID để biết "Mảnh này thuộc về Gói IP gốc nào". Offset chỉ ra vị trí (Mảnh số 1, Mảnh số 2...). Cờ MF (More Fragments) bật 1 nghĩa là "Sau mảnh này còn mảnh khác", MF=0 nghĩa là "Đây là cái chót đuôi rồi".*

**Câu 54:** Dải địa chỉ IP `127.0.0.1` được dùng cho mục đích gì?
A. Giao tiếp với vệ tinh.
B. Loopback (Vòng lặp ngược). Máy tính tự gửi dữ liệu nội bộ (Localhost) cho chính các ứng dụng đang chạy trên nó mà không cần phát tín hiệu ra card mạng vật lý.
C. Liên lạc P2P.
D. Địa chỉ Gateway của Internet.
*Đáp án: B*
*Giải thích: Rất phổ biến cho lập trình viên lập trình Web. Bật server lên rồi vào Browser gõ localhost hoặc 127.0.0.1 để xem web do chính máy mình đang code.*

**Câu 55:** Giao thức IPv6 ra đời chủ yếu để giải quyết bài toán nào của IPv4?
A. Tăng cường khả năng truyền Analog.
B. IPv4 sử dụng hệ nhị phân, IPv6 dùng hệ thập phân.
C. Khan hiếm địa chỉ. IPv6 mở rộng độ dài địa chỉ từ 32 bit lên 128 bit, tạo ra không gian địa chỉ khổng lồ ($3.4 \times 10^{38}$) đủ cấp cho từng hạt cát trên Trái Đất.
D. Tăng tốc độ cáp mạng lên 100 Gbps.
*Đáp án: C*
*Giải thích: IoT (Internet Vạn vật) ra đời, ô tô, bóng đèn, tủ lạnh đều cần IP. Không gian IPv4 (4 tỷ) là con kiến so với đại dương thiết bị hiện nay.*

**Câu 56:** Thiết kế Header của IPv6 mang tính "Đột phá" nhằm TĂNG TỐC CHO ROUTER so với IPv4 ở điểm nào?
A. Loại bỏ hoàn toàn Địa chỉ Nguồn.
B. Tăng kích thước Header tùy ý.
C. IPv6 sử dụng một Base Header CỐ ĐỊNH cực gọn nhẹ (Đúng 40 Bytes). Đã LOẠI BỎ hoàn toàn quá trình Phân mảnh (Fragmentation) và Checksum tại Router.
D. IPv6 yêu cầu Checksum phức tạp gấp đôi.
*Đáp án: C*
*Giải thích: IPv6 bắt Máy tính (Host) phải tự tính MTU để cắt gói trước, Router IPv6 thấy gói to là Thả (Drop) kèm báo lỗi ICMP, chứ tuyệt đối không rảnh CPU đi phân mảnh hộ như IPv4.*

**Câu 57:** Nếu gói tin IPv4 có trường Header Checksum, tại sao IPv6 lại loại bỏ đi việc tính Checksum ở Tầng Mạng?
A. Vì cáp quang bây giờ 100% không bao giờ lỗi bit.
B. Vì Checksum đã được tính toán cực kì chắc chắn bởi Tầng Giao Vận (TCP/UDP) và cả Tầng Liên kết (Ethernet FCS). Việc bắt Router tính lại Checksum (IP) qua mỗi trạm gây lãng phí tài nguyên CPU mà không mang lại nhiều lợi ích.
C. Vì IPv6 là mạng không dây.
D. Để Hacker không kiểm tra được.
*Đáp án: B*
*Giải thích: Mọi thay đổi của IPv6 đều xoay quanh triết lý "Fast Forwarding" - Đóng gói nhanh, xử lý ít, truyền đi ngay.*

**Câu 58:** Cấu trúc địa chỉ IPv6 được biểu diễn bằng hệ cơ số nào và có mấy nhóm?
A. Hệ thập phân, 4 nhóm.
B. Hệ bát phân, 6 nhóm.
C. Hệ Thập lục phân (Hexadecimal), 8 nhóm cách nhau bằng dấu hai chấm (:).
D. Nhị phân toàn bộ.
*Đáp án: C*
*Giải thích: Ví dụ: `2001:0db8:85a3:0000:0000:8a2e:0370:7334`. Gọn gàng hơn có thể viết tắt các số 0 liên tiếp thành `::`.*

**Câu 59:** Một vấn đề lớn là không thể đổi tất cả Router thế giới sang IPv6 trong một đêm. "Dual-Stack" (Ngăn xếp kép) là chiến lược phổ biến nhất, hoạt động ra sao?
A. Chập 2 đường cáp mạng lại.
B. Thiết bị (như Router, Điện thoại, Máy tính) được cấu hình chạy đồng thời CẢ HAI GIAO THỨC IPv4 và IPv6 song song. Nếu gặp Web v4 thì nói chuyện v4, gặp Web v6 thì gọi v6.
C. Đổi luân phiên v4 và v6 theo giờ.
D. IPv6 bị nén thành IPv4.
*Đáp án: B*
*Giải thích: Đây là lý do bạn vào Windows/Mac sẽ luôn thấy phần cấu hình TCP/IPv4 và TCP/IPv6 đi cùng nhau.*

**Câu 60:** Bên cạnh Dual-Stack, kỹ thuật "Tunneling" (Đường hầm) được dùng để kết nối hai đảo (hòn đảo mạng) IPv6 cô lập phải đi xuyên qua đại dương mạng lõi chỉ có Router chạy IPv4 bằng cách nào?
A. IPv6 bị xóa, Router đổi thành IPv4.
B. Router biên của đảo IPv6 sẽ LẤY TOÀN BỘ gói Datagram IPv6, đóng gói trọn vẹn (như một kiện hàng Payload) NHÉT VÀO BÊN TRONG thân của một gói tin IPv4 bình thường, gửi qua đại dương v4, rồi Router bờ bên kia bóc dỡ ra lại thành IPv6.
C. Đặt cáp ngầm riêng nối 2 đảo.
D. Dùng TCP thay vì IP.
*Đáp án: B*
*Giải thích: Các Router IPv4 ở giữa không hề hay biết đang chở kiện hàng gì, nó chỉ thấy một gói IPv4 (Protocol = 41) bình thường đang gửi đi.*

**Câu 61:** Giao thức nào hoạt động cùng Tầng Mạng, được thiết kế để "Trợ lý" cho giao thức IP, giúp các Máy tính và Router trao đổi các bản tin Lỗi (Error) hoặc báo trạng thái hoạt động?
A. UDP
B. IGMP
C. OSPF
D. ICMP (Internet Control Message Protocol)
*Đáp án: D*
*Giải thích: Khi cáp đứt, Router dùng ICMP nhắn về Host: "Network Unreachable". Khi TTL=0, Router nhắn "Time Exceeded". ICMP là cái loa thông báo của Tầng Mạng.*

**Câu 62:** Lệnh `ping` sử dụng cặp bản tin ICMP cụ thể nào?
A. Type 3 (Destination Unreachable)
B. Type 11 (Time Exceeded)
C. Type 8 (Echo Request - Hỏi) và Type 0 (Echo Reply - Đáp)
D. Source Quench
*Đáp án: C*
*Giải thích: Khi gõ `ping google.com`, máy tính phát đi tiếng kêu Type 8. Máy chủ Google nghe thấy phải lịch sự gửi lại tiếng vọng Type 0.*

**Câu 63:** Chức năng chính của giao thức IPsec, vốn có thể tích hợp trong Tầng Mạng IP, là gì?
A. Nén video truyền thông.
B. Cung cấp một bộ khung bảo mật (Mã hóa Payload, Xác thực điểm nguồn) để bảo vệ toàn bộ các gói tin IP (Datagrams) trên đường bay, thường dùng xây dựng mạng riêng ảo VPN doanh nghiệp ở Lớp 3.
C. Cấp IPv6 cho toàn mạng.
D. Tăng cường tốc độ sóng Wi-Fi.
*Đáp án: B*
*Giải thích: TLS/SSL bảo mật Tầng Ứng dụng (L7), chỉ mã hóa từng ứng dụng Web cụ thể. IPsec bảo mật Tầng Mạng (L3), mã hóa MỌI THỨ từ máy này đến máy kia (Web, Game, Ping, Truyền file).*

**Câu 64:** Thiết bị nào sau đây cấu hình cơ chế NAT (Network Address Translation) để biến Dải địa chỉ Nội bộ (như 192.168.1.0/24) thành 1 Địa chỉ IP công cộng (VD: 14.15.16.17)?
A. Switch
B. Hub
C. Gateway Router Biên (Router gia đình / Firewall Cổng ngõ doanh nghiệp).
D. Laptop cá nhân.
*Đáp án: C*
*Giải thích: Việc dịch chuyển thế giới Ảo/Nội bộ ra thế giới Thực/Internet được giao trọng trách cho cánh cửa sát mép tường nhất của nhà bạn (Modem/Router nhà mạng cấp).*

**Câu 65:** "Bảng Dịch NAT" (NAT Translation Table) chứa các cột thông số thiết yếu nào để biến đổi gói tin hai chiều?
A. MAC đích và MAC nguồn.
B. Tên miền Web và IP đích.
C. (IP riêng + Cổng riêng của mạng LAN) <--> (IP Công cộng NAT + Cổng NAT).
D. Chuẩn cáp và Giao thức.
*Đáp án: C*
*Giải thích: Nhờ sự map (ánh xạ) này, gói tin ra mạng đổi từ `192.168.1.10:3345` thành `14.15.16.17:5001`. Khi gói web trả về IP `14.15.16.17:5001`, Router nhìn bảng dò ngược lại để giao hàng đúng phòng 192.168.1.10.*

**Câu 66:** Nhược điểm LỚN NHẤT về thiết kế triết lý mạng của thiết bị NAT là gì?
A. Làm tốn IP Public hơn.
B. Tăng bảo mật do giấu IP nội bộ.
C. Phá vỡ nguyên lý "End-to-End" (Tương tác Đầu-Cuối) của Internet. Một Server Web bên ngoài không thể chủ động gửi kết nối TCP mới Xuyên thủng thẳng vào một Máy tính nằm giấu mặt phía sau tường NAT nếu không có các cài đặt lách luật phức tạp (Port Forwarding, UPnP, Hole Punching).
D. Không hỗ trợ mạng không dây.
*Đáp án: C*
*Giải thích: NAT được ca tụng vì cứu IP, nhưng nó là rào cản chết chóc làm vô hiệu hoá lý tưởng "Mạng ngang hàng" vĩ đại. Bất kỳ kỹ sư lập trình Voice Call, Game nào cũng ghét Cay ghét đắng NAT.*

**Câu 67:** Khi bạn đăng ký gói cước Internet, nhà cung cấp ISP thường sử dụng công nghệ cấp IP bằng cơ chế DHCP. Dịch vụ DHCP hoạt động như thế nào với Tầng Mạng?
A. Thay thế hoàn toàn Giao thức IP.
B. DHCP là một giao thức ở Tầng Ứng dụng (Port 67/68 UDP), nhưng nó tham gia CẤU HÌNH tự động các thông số của Tầng Mạng (Địa chỉ IP, Mặt nạ mạng Subnet Mask, Gateway) cho thiết bị vừa tham gia mạng.
C. Mã hóa hoàn toàn dữ liệu.
D. Biến Router thành Switch.
*Đáp án: B*
*Giải thích: DHCP là một quá trình "Cắm và Chạy" (Plug and Play). Không có nó, bạn phải điền tay (Static IP) hàng chục con số mới vào được mạng.*

**Câu 68:** Thuật ngữ "Default Gateway" (Cổng mặc định) cấu hình trên máy tính có nghĩa là:
A. Cổng vật lý cắm dây màn hình.
B. Địa chỉ IP của Server DNS Google (8.8.8.8).
C. Địa chỉ IP của Router trực tiếp (Next-hop Router) trên CÙNG mạng cục bộ (Subnet). Bất cứ khi nào Máy tính gửi 1 gói tin có IP Đích nằm NGOÀI mạng cục bộ, nó sẽ tự động tống toàn bộ gói tin đó cho Default Gateway xử lý đường đi tiếp theo.
D. IP của Máy in.
*Đáp án: C*
*Giải thích: Giống như Tủ bảo vệ cửa chung cư. Nếu bạn gửi thư cho nhà hàng xóm, bạn đi bộ sang đưa thẳng. Nếu gửi thư sang Mỹ, bạn không biết đường, bạn cứ ném ra Tủ bảo vệ, bảo vệ (Gateway) tự biết gửi thư ra bưu điện.*

**Câu 69:** Một hệ thống mạng (Subnet) `10.0.0.0/8` là dải mạng IP đặc biệt thuộc về lớp (Class) mạng nào (theo truyền thống)?
A. Dải Public quốc tế.
B. Dải IP riêng (Private Network) cỡ khổng lồ (Thường gọi là Class A Private), thường dành riêng cho các mạng Nội bộ Doanh nghiệp/Tập đoàn lớn sử dụng để không trùng lặp với Internet bên ngoài.
C. IPv6
D. Dải Loopback.
*Đáp án: B*
*Giải thích: Internet Assigned Numbers Authority (IANA) đã cắt riêng 3 dải làm IP Nội bộ cấm lưu thông quốc tế: 10.x.x.x, 172.16.x.x đến 172.31.x.x, và dải quen thuộc nhà nhà đều dùng 192.168.x.x.*

**Câu 70:** Để một gói tin di chuyển đúng đường trên Mạng Internet toàn cầu, các Bảng định tuyến (Forwarding Table) trong TẤT CẢ hàng vạn Router phải được thiết lập. Ai/Cái gì tạo ra các Bảng định tuyến đó?
A. Một kỹ sư dùng lệnh cấu hình bằng tay trên tất cả Router mỗi sáng.
B. Chính phủ các nước chỉ định.
C. Quá trình Tương tác tự động của "Mặt phẳng điều khiển" (Control Plane) thông qua các Thuật toán Định tuyến (Routing Algorithms / Protocols) chạy ở Dạng phần mềm ngầm trên Router hoặc ở Controller trung tâm (SDN).
D. Giao thức UDP.
*Đáp án: C*
*Giải thích: Định tuyến là cái Não của Internet. Router tự nói chuyện với nhau, tự tính "Đường tới Google mất 5 trạm, nếu đi đường này mất 10 trạm". Mọi thứ là tự động hoàn toàn.*

**Câu 71:** Khi Máy gửi (Host) chia nhỏ gói dữ liệu bằng cơ chế "Phân mảnh IP" (Fragmentation), các thiết bị Định tuyến (Router) dọc đường sẽ phải làm gì với những Mảnh vỡ này?
A. Cố gắng dán các mảnh vỡ lại (Reassembly) rồi mới đẩy đi tiếp.
B. Router coi mỗi mảnh vỡ (Fragment) như MỘT GÓI IP ĐỘC LẬP HOÀN TOÀN, tra bảng định tuyến và vứt chúng ra ngoài cổng một cách độc lập (Thậm chí 2 mảnh có thể chạy 2 đường khác nhau nếu bảng định tuyến biến động).
C. Trả mảnh vỡ lại cho máy gửi.
D. Sửa lỗi Checksum liên tục.
*Đáp án: B*
*Giải thích: Router Tầng Mạng vốn "mù quáng". Nó không có bộ đệm lưu trữ trạng thái chờ ghép gói. Nó thấy IP Đích là nó tống đi. Mọi việc ghép xếp hình là việc của cái PC ở cuối đường.*

**Câu 72:** IPv6 sử dụng không gian địa chỉ khổng lồ 128 bit. Tại sao IPv6 không sử dụng cơ chế NAT (Dịch địa chỉ mạng) như IPv4?
A. Vì NAT quá bảo mật.
B. Vì thiết bị IPv6 không có port.
C. IPv6 có quá nhiều địa chỉ public, đủ để cấp cho MỌI THIẾT BỊ TỒN TẠI (Tủ lạnh, Máy ảnh, Bóng đèn...) một IP thực tế trên Internet, qua đó khôi phục lại lý tưởng "Kết nối Trực tiếp Đầu-cuối" (End-to-end) thuần khiết mà NAT đã phá vỡ ở IPv4.
D. Vì IPv6 rất yếu.
*Đáp án: C*
*Giải thích: NAT là liều thuốc chữa cháy tạm thời. Khi có IPv6, căn bệnh thiếu IP đã khỏi, thuốc NAT không còn cần thiết, giúp P2P (BitTorrent, Game, Call) hoạt động cực mượt.*

**Câu 73:** Trong kiến trúc mạng SDN (Software-Defined Networking), Giao thức nào thường được sử dụng để Máy chủ Điều khiển Tập trung (Controller) giao tiếp với phần cứng Router/Switch bên dưới nhằm nạp Bảng chuyển tiếp (Flow table) vào chúng?
A. Giao thức OSPF.
B. Giao thức HTTP.
C. Giao thức OpenFlow. Đây là một chuẩn mở tiên phong giúp tách rời phần Cứng và phần Mềm của thiết bị Mạng.
D. Giao thức ARP.
*Đáp án: C*
*Giải thích: OpenFlow là cái cáp cắm từ Bộ Não (Controller) xuống Cơ Bắp (Switch). Nhờ nó mà Google quản lý hàng chục vạn Switch trong Data Center cực kỳ rẻ tiền và thông minh.*

**Câu 74:** Dải địa chỉ IP `169.254.x.x` thường xuất hiện trên máy tính Windows/Mac khi nào?
A. Khi mạng chạy bình thường nhanh nhất.
B. Khi hệ thống đang dùng IPv6.
C. Khi máy tính được thiết lập tự động lấy IP (DHCP), nhưng KHÔNG THỂ tìm thấy hoặc kết nối tới Máy chủ DHCP nào (Do rớt cáp, Router hỏng). HĐH tự động gán dải địa chỉ riêng APIPA này để tạm thời gọi nhau trong LAN hẹp.
D. IP cố định của Google.
*Đáp án: C*
*Giải thích: Nếu cắm dây mạng mà thấy dải này (APIPA - Automatic Private IP Addressing), 99% mạng nhà bạn đang đứt kết nối vào Cổng Router hoặc Router treo chức năng cấp IP.*

**Câu 75:** Trong môi trường mạng lớn, thuật toán kiểm soát Tắc nghẽn mạng (Congestion Control) nào được sử dụng tích hợp "Báo hiệu ngầm" (Implicit signaling) từ Tầng Mạng để báo nghẽn lên Tầng Giao vận?
A. Thuật toán AES.
B. Công nghệ ECN (Explicit Congestion Notification). Router đánh dấu (đổi bit) vào gói IP khi hàng đợi gần đầy, Máy nhận thấy thế sẽ báo ngược lại cho Máy phát để Máy phát hạ tốc độ trước khi rớt gói.
C. Giao thức FTP.
D. Chạy mạng 5G.
*Đáp án: B*
*Giải thích: Đây là sự hợp tác đỉnh cao. Thay vì im lặng vứt cục hàng (TCP phải tự đoán). Tầng Mạng (Router) "nói" cho Tầng Giao vận (TCP) biết: "Tao mệt rồi, gửi chậm lại đi bạn".*

**Câu 76:** Trường thông tin "Fragment Offset" (Độ lệch mảnh) trong IPv4 Header dùng để làm gì?
A. Cho biết Gói tin có bị virus không.
B. Cho biết Máy nhận cần lắp ghép Mảnh vỡ này VÀO VỊ TRÍ NÀO (Byte thứ mấy) trong gói Datagram gốc siêu lớn để khôi phục chính xác Dữ liệu.
C. Mã hóa Mật khẩu.
D. Định tuyến đường bay.
*Đáp án: B*
*Giải thích: Giống như cắt quyển sách làm 3 tập để gửi đi. Tập 1 (Offset 0), Tập 2 (Offset 1500), Tập 3 (Offset 3000). Đầu kia nhận 3 cuốn lấy Offset ráp lại thành sách nguyên vẹn.*

**Câu 77:** "Anycast" trong IPv6 được sử dụng cho kịch bản nào hợp lý nhất?
A. Gửi email cho một người duy nhất.
B. Livestream cho hàng triệu người xem trên toàn thế giới.
C. Truy vấn dịch vụ máy chủ phân tán (VD: DNS Root/CDN). Bạn gửi vào một IP Anycast chung, mạng sẽ tự động tìm và định tuyến gói tin đó TỚI MÁY CHỦ CÓ CÙNG IP NÀY NHƯNG GẦN BẠN NHẤT về mặt cấu trúc mạng.
D. Cấp phát IP động.
*Đáp án: C*
*Giải thích: Đỉnh cao của tối ưu tốc độ. Hàng chục máy chủ DNS 8.8.8.8 của Google phân bố rải rác trên toàn cầu. Nhờ Anycast, bạn ở VN hỏi 8.8.8.8, mạng sẽ tự dẫn bạn đến con máy chủ đặt ở VN.*

**Câu 78:** Giao thức nào hoạt động bằng cách quảng bá địa chỉ IP trên mạng cục bộ (LAN) để truy vấn lấy Địa chỉ MAC của máy đích tương ứng?
A. DHCP
B. ARP (Address Resolution Protocol)
C. ICMP
D. HTTP
*Đáp án: B*
*Giải thích: Mặc dù ARP phục vụ Tầng Mạng, hành vi của nó là gửi Frame Quảng bá (Broadcast MAC FF:FF:FF:FF:FF:FF) ở Tầng Liên kết để hét lên: "Ê, thằng nào mang IP 192.168.1.15 trả lời tao cái MAC của mày coi".*

**Câu 79:** Bảng chuyển tiếp (FIB) trong một Router có thể hỗ trợ hàng triệu dòng (Entries) IP đích khác nhau. Router sử dụng phần cứng nào để "Tìm kiếm" siêu nhanh (Lookup) ra dòng phù hợp trong khoảng vài nano-giây (ns) cho mỗi gói tin?
A. CPU Intel Core i9.
B. RAM máy tính thông thường (DDR4).
C. Bộ nhớ phần cứng chuyên dụng TCAM (Ternary Content-Addressable Memory). Cho phép tìm kiếm toàn bộ bảng MỘT LẦN DUY NHẤT (O(1)) bằng song song mạch điện thay vì duyệt từng dòng bằng phần mềm.
D. Ổ cứng SSD.
*Đáp án: C*
*Giải thích: Tốc độ Gigabit/Terabit bắt buộc phải dùng chip Silicon thiết kế riêng. TCAM là linh kiện đắt tiền nhất trong lõi Router mạng doanh nghiệp.*

**Câu 80:** "IP Spoofing" (Giả mạo IP) khó có thể bị ngăn chặn hoàn toàn ở Tầng Mạng vì lý do thiết kế gì?
A. Tầng mạng bắt buộc dùng Windows.
B. Tầng mạng IPv4/IPv6 nguyên thủy KHÔNG HỀ ĐÒI HỎI XÁC THỰC DANH TÍNH (Authentication). Bất kỳ máy nào cũng có thể tự do điền một chuỗi 32-bit tùy ý vào ô IP Source của Header trước khi đẩy ra mạng.
C. Router không biết đọc IP.
D. TCP mã hóa IP Nguồn.
*Đáp án: B*
*Giải thích: Giống như bạn ra bưu điện gửi thư, bạn có quyền ghi "Người gửi: Tổng thống Mỹ" ngoài bì thư, bưu điện vẫn nhận và chuyển thư bình thường. Chỉ có cài thêm IPSec hoặc Tường lửa lọc biên (Ingress filtering) mới ngăn chặn được.*

**Câu 81:** Để hỗ trợ kết nối mạng cho Hệ thống Thông tin Di động (Mobility), Mobile IP sử dụng công nghệ "Đường hầm" (Tunneling) với mục đích gì?
A. Chặn điện thoại chơi game.
B. Đóng gói Datagram chứa "IP Cố định" (Home Address) của máy di động vào bên trong một Datagram mới có "IP Tạm thời" (Care-of Address) nơi máy đang lưu trú. Giúp máy di chuyển qua mạng khác mà phiên TCP cũ đang kết nối không bị sập.
C. Tắt kết nối 4G.
D. Mã hóa nội dung video.
*Đáp án: B*
*Giải thích: Bình thường mang laptop sang nhà hàng xóm, đổi IP là Zalo/Download đứt hết kết nối. Mobile IP tạo "Home Agent" chuyển tiếp mọi thư từ nhà cũ (Home IP) qua đường hầm sang nhà mới (Foreign IP) cho bạn.*

**Câu 82:** Giao thức IPsec chạy ở chế độ "Transport Mode" (Chế độ giao vận) bảo vệ phần nào của gói tin?
A. Mã hóa và xác thực TẤT CẢ các thành phần, kể cả IP Header cũ (Gói tin thành vô hình).
B. Chỉ mã hóa phần Payload (Segment của Tầng Giao vận trở lên), giữ nguyên IP Header gốc để các Router dễ định tuyến trên mạng công cộng. Phù hợp kết nối Host-to-Host (PC với Server).
C. Không mã hóa gì cả.
D. Chỉ mã hóa phần Header MAC.
*Đáp án: B*
*Giải thích: Tunnel Mode thì giấu tiệt cả IP Header gốc (dành cho kết nối Site-to-Site giữa 2 công ty vpn). Transport Mode thì để lộ IP Header (kết nối trực tiếp từ laptop nhân viên về công ty).*

**Câu 83:** Trong mô hình Tầng mạng SDN, thuật ngữ "Northbound API" (Giao diện Bắc) dùng để chỉ kết nối giữa ai với ai?
A. Giao tiếp giữa 2 Controller.
B. Giao tiếp giữa Controller (Bộ điều khiển trung tâm) và các Ứng dụng Mạng cấp cao (Network Applications như Quản lý Load Balancing, Firewall, QoS) nằm phía trên nó.
C. Giao tiếp giữa Controller và Switch mạng bên dưới.
D. Giao tiếp giữa người dùng và trình duyệt web.
*Đáp án: B*
*Giải thích: "Southbound API" (Giao diện Nam, ví dụ OpenFlow) cắm xuống phần cứng mồ hôi bùn lầy (Switch). "Northbound API" (REST API) ngửa lên trời để Lập trình viên Python trên Server gọi lệnh cấu hình ảo hoá mạng.*

**Câu 84:** Thuật ngữ "Middlebox" (Hộp trung gian) trên nền kiến trúc mạng IP ám chỉ loại thiết bị nào?
A. Dây cáp mạng quang.
B. Các bộ định tuyến thuần túy (Router gốc) chỉ tra bảng FIB.
C. Các hộp phần cứng nằm giữa đường đi của gói tin, CÓ CAN THIỆP và XỬ LÝ SÂU gói tin ngoài việc chuyển tiếp đơn thuần (Ví dụ: NAT, Firewall, IPS/IDS, Web Caches, Load Balancers).
D. Đầu phát Wi-Fi.
*Đáp án: C*
*Giải thích: Bức tranh mạng hiện đại không chỉ có Router ngoan hiền. Trên đường đi còn đầy rẫy các "Chú bảo vệ, máy soi chiếu an ninh" (Middlebox) chọc phá gói tin, làm vi phạm nguyên lý thiết kế End-to-End cổ điển.*

**Câu 85:** Giao thức OSPF (Open Shortest Path First) là giao thức định tuyến hoạt động bên trong Nội bộ Mạng một Tổ chức (IGP). Nó dựa vào thuật toán cốt lõi nào?
A. Thuật toán Chuỗi khối (Blockchain).
B. Thuật toán Trạng thái liên kết (Link-State), sử dụng thuật toán Dijkstra để vẽ toàn bộ Bản đồ mạng cấu trúc hình cây đường đi ngắn nhất (Shortest-path Tree) tại mỗi Router.
C. Thuật toán Vector khoảng cách (Distance-Vector) Bellman-Ford.
D. Thuật toán Đoán ngẫu nhiên.
*Đáp án: B*
*Giải thích: Trong OSPF, mỗi Router phải liên tục dội Broadcast để nắm bản đồ ĐẦY ĐỦ của cả công ty. Khi mạng thay đổi (đứt cáp), nó tính toán lại (Converge) rất nhanh.*

**Câu 86:** Trái ngược với OSPF, giao thức định tuyến RIP (Routing Information Protocol) đời cũ dùng thuật toán "Vector Khoảng cách" (Distance-Vector) hoạt động như thế nào?
A. Router chỉ cần biết IP đích.
B. Router không biết tổng thể mạng hình thù ra sao. Nó chỉ nghe lời "rỉ tai" từ Router hàng xóm kề bên (Neighbors) về khoảng cách đến đích và tin tưởng tuyệt đối, cộng thêm 1 khoảng cách (hop) của mình để cập nhật bảng định tuyến.
C. Router tải bản đồ từ máy chủ Google.
D. Định tuyến dựa vào cáp quang.
*Đáp án: B*
*Giải thích: Thuật toán Bellman-Ford ("Nhờ bạn báo hộ"). Mạng lớn dùng RIP sẽ hội tụ (converge) rất chậm, và dễ sinh ra hiện tượng Lặp định tuyến (Routing Loop / Count to Infinity) nếu có cáp đứt.*

**Câu 87:** Điểm mạnh lớn nhất giúp giao thức BGP (Border Gateway Protocol) trở thành "Ông hoàng định tuyến" nối các Quốc gia và các ISP (EGP - Exterior Gateway Protocol) trên toàn bộ Internet là gì?
A. BGP tìm đường siêu nhanh.
B. BGP hỗ trợ mạnh mẽ việc KHAI BÁO CÁC CHÍNH SÁCH ĐỊNH TUYẾN (Policy-based routing). Nó không màng tới "đường ngắn nhất", mà quan trọng là "Quy định làm ăn kinh tế/chính trị" (VD: Không cho gói tin Mỹ đi qua mạng Trung Quốc).
C. BGP không tốn RAM.
D. BGP sử dụng UDP.
*Đáp án: B*
*Giải thích: Giữa các mạng tập đoàn viễn thông (Autonomous System - AS), bài toán không còn là nhanh hay chậm (như OSPF nội bộ), mà là "Tao không ưa mày, tao không cho mày đi ké cáp của tao". BGP sinh ra vì nhu cầu Thương mại đó.*

**Câu 88:** "Subnetting" (Chia mạng con) tại Tầng Mạng đem lại lợi ích quản lý nào cho Quản trị viên hệ thống (IT Admin) của Công ty?
A. Ngăn chặn DDoS vào Router ngoài biên.
B. Nâng cấp tốc độ máy tính cũ.
C. Cắt nhỏ một Dải mạng lớn (Ví dụ /16) thành nhiều Dải nhỏ hơn (Ví dụ /24) và gắn vào các Tầng lầu/Phòng ban. Giúp cô lập lỗi mạng (Broadcast Domain), dễ áp dụng quy tắc Firewall (Phòng IT cấm thông mạng với Phòng Kế toán) và giảm thiểu các bản tin Rác nội bộ.
D. Tạo mật khẩu cho Windows.
*Đáp án: C*
*Giải thích: Nếu 5000 nhân viên cắm chung 1 cái Mạng /16 khổng lồ, một virus lan truyền (hay ARP Broadcast) sẽ làm 5000 máy sập cùng lúc.*

**Câu 89:** Tại sao khi cấu hình Máy tính trong mạng IPv4 nội bộ tĩnh (Static IP), bạn thường phải gõ thủ công "Subnet Mask" (Ví dụ `255.255.255.0`)? Hệ điều hành dùng nó để làm gì?
A. Để che giấu mật khẩu.
B. HĐH lấy IP Đích đem phép toán logic AND (Nhân bit) với Subnet Mask để quyết định xem Máy đích đang ở CÙNG MẠNG (nội bộ - gọi thẳng qua MAC) hay ở KHÁC MẠNG (phải tống cho Default Gateway).
C. Dùng làm IP ảo.
D. Mở cổng kết nối.
*Đáp án: B*
*Giải thích: IP bạn 192.168.1.5 (Mask 255.255.255.0). Bạn vào 192.168.1.10. Phép AND thấy phần Mạng (192.168.1) trùng nhau -> Máy tính gọi thẳng MAC bằng ARP trong phòng. Bạn vào 8.8.8.8, AND thấy lệch -> Máy tính đưa cho cửa Gateway giải quyết.*

**Câu 90:** Giao thức nào hoạt động bằng cách "Gắn nhãn" (Label/Tag) nhỏ vào Gói tin IP (nằm giữa L2 và L3) để Router lõi chỉ cần đọc NHÃN NÀY và phần cứng mạch chuyển mạch cực nhanh (Fast Switching) mà không cần bóc sâu vào tra Bảng IP dài thòng?
A. VLAN 802.1Q
B. MPLS (Multiprotocol Label Switching)
C. SD-WAN
D. ATM
*Đáp án: B*
*Giải thích: MPLS (Layer 2.5) được dùng rầm rộ ở lõi mạng của nhà mạng Viễn thông. Nó gắn cho gói tin cái tem giống mã vạch siêu thị, chít vèo cái là đi ngay, đỡ tốn CPU tra bảng IP khổng lồ.*

**Câu 91:** "IPv6 Auto-configuration" (SLAAC) cho phép máy tính khi bật lên sẽ tự động có một IP Public hoàn chỉnh (128 bit) MÀ KHÔNG CẦN CÓ MÁY CHỦ DHCP bằng cách nào?
A. Gõ phím tùy ý.
B. Nó tự lắng nghe (Router Advertisement) dải Mạng 64-bit từ Router phát xuống. Sau đó lấy 64-bit đó ghép với 64-bit Mở rộng (EUI-64) được chế biến từ chính Địa chỉ MAC của máy tính để thành IP 128-bit duy nhất trên toàn cầu.
C. Lên Internet xin IP.
D. Xin cấp IP từ DNS.
*Đáp án: B*
*Giải thích: Một tính năng cắm-và-chạy (Plug & Play) đỉnh cao của IPv6, thiết bị IoT cứ cắm mạng là tự mọc ra IP dùng ngay, không cần cấu hình Router phức tạp.*

**Câu 92:** Tính năng "IP Anycast" thực tế KHÔNG GỬI GÓI TIN ĐẾN ĐÂU?
A. Không gửi đến nhiều nơi cùng lúc (Multicast). Nó chỉ gửi đến đúng MỘT MÁY CHỦ DUY NHẤT (Unicast) trong nhóm các máy dùng chung 1 IP, dựa trên cự ly định tuyến là Rẻ nhất/Gần nhất do BGP phân bổ.
B. Không gửi đến vệ tinh.
C. Không gửi đến Firewall.
D. Không dùng cáp quang.
*Đáp án: A*
*Giải thích: Nhắc lại: Multicast là gửi 1 tivi, phát 100 tivi xem chung. Anycast là 100 Server chung 1 tên (IP), nhưng 1 khách hàng chỉ gửi lệnh đến và làm việc với 1 Server duy nhất (Server nào gần mình nhất).*

**Câu 93:** Hệ thống số AS (Autonomous System Number) trong giao thức BGP được hiểu như thế nào?
A. Mã định danh của từng cái máy tính trong mạng.
B. Một mã số duy nhất cấp cho các tổ chức khổng lồ (VD: Google, Viettel, VNPT) để định danh toàn bộ khối mạng của họ trên bản đồ định tuyến Internet thế giới (Ví dụ VNPT là AS45899). BGP không định tuyến theo từng IP nhỏ, mà định tuyến nhảy từ AS này sang AS khác.
C. Số lượng Router tối đa trong 1 mạng.
D. Mã số của cáp quang.
*Đáp án: B*
*Giải thích: Internet không phải mạng của các Router nhỏ lẻ. Internet là một Lưới của các Siêu Tập đoàn khổng lồ (Các tổ chức Tự trị - AS) nối tay với nhau bằng BGP.*

**Câu 94:** Kỹ thuật "Route Aggregation" (Gom tuyến đường / Route Summarization) tại các Router biên (Border) giải quyết bài toán gì cho các Router lõi Internet toàn cầu?
A. Bẻ khóa mật khẩu mạng.
B. Tránh việc Bảng định tuyến BGP toàn cầu bị quá tải RAM (Bùng nổ hàng triệu dòng IP lẻ tẻ). Bằng cách Gộp các dải mạng nhỏ (VD: bốn dải /24 của công ty con) thành MỘT DẢI MẠNG LỚN DUY NHẤT (/22) để quảng bá ra thế giới.
C. Mở rộng kích thước gói tin.
D. Gộp cáp đồng và Wi-Fi.
*Đáp án: B*
*Giải thích: Nếu không gom lại (Summarize), Bảng FIB trên các máy chủ Tier-1 ISP sẽ phình lên hàng tỷ dòng, vượt quá dung lượng bộ nhớ TCAM cực kỳ đắt đỏ của chúng.*

**Câu 95:** Trong kiến trúc OpenFlow (SDN), Bảng Flow Table có một hành động (Action) nổi bật nào mà Router truyền thống không có (ngoài việc chuyển tiếp - Forward)?
A. Thắt cáp mạng lại.
B. Có thể dễ dàng ra lệnh Drop (Chặn Firewall), Sửa đổi Header IP/MAC/Port (Làm chức năng NAT), hoặc Nhân bản gói tin gửi sang nhiều cổng. Biến phần cứng Switch trở thành Firewall hoặc Load Balancer tùy ý phần mềm Controller lập trình.
C. Khởi động lại Windows.
D. Sinh thêm virus.
*Đáp án: B*
*Giải thích: Router cũ chỉ biết Forward theo IP đích. SDN Switch cho phép "Chọc phá" đủ mọi tầng (từ Tầng 2 đến Tầng 4), linh hoạt như một con dao Thụy Sĩ mềm dẻo.*

**Câu 96:** Nếu bạn sử dụng trình duyệt Web vào mạng công ty và truy cập một trang web độc hại, Tường lửa IPS/IDS của công ty CẢNH BÁO bạn ở mức Cảnh báo Cáo cấp. Thiết bị bảo mật này đang hoạt động theo cơ chế nào?
A. Tra bảng ARP.
B. Signature-based (Dựa trên chữ ký - Nó có 1 Database khổng lồ chứa Mẫu/Chuỗi Bytes của các cuộc tấn công/Virus mạng đã biết. Khi kiểm tra nội dung (DPI) gói tin IP thấy chuỗi Byte này, nó báo động đỏ).
C. Tắt cổng nguồn 80.
D. Sửa IP mạng.
*Đáp án: B*
*Giải thích: IPS (Intrusion Prevention System) giống hệt phần mềm quét Virus (quét mẫu chữ ký), nhưng thay vì quét File ổ cứng, nó quét từng gói tin (Packet) đang chạy bay bay trên cáp LAN thời gian thực.*

**Câu 97:** Công nghệ "SD-WAN" (Software-Defined WAN) đang nổi lên mạnh mẽ thay thế cho cáp thuê bao (Leased Line / MPLS) vì lý do nào ở Tầng Mạng?
A. Vì nó truyền qua Bluetooth.
B. Nó cung cấp sự Độc lập về đường truyền vật lý. Công ty có thể dùng hỗn hợp Cáp quang rẻ tiền (FTTH), 4G và Leased Line để chạy SDN. Controller sẽ linh hoạt tự đẩy gói Voice (quan trọng) chạy qua đường MPLS xịn, còn gói Download (ít quan trọng) tống ra đường FTTH rác rẻ tiền để tiết kiệm chi phí.
C. SD-WAN cấm IPv6.
D. Nó tạo ra điện.
*Đáp án: B*
*Giải thích: Ảo hóa đám mây trong kết nối chi nhánh công ty. SD-WAN tạo ra nhiều đường hầm (Tunnels) ảo bọc trên nền cáp vật lý và định tuyến gói tin cực kỳ thông minh theo Application (DPI) thay vì IP thô cứng.*

**Câu 98:** Một hiện tượng "Blackhole" (Hố đen) ở Tầng Mạng xảy ra do sự cố Cấu hình Định tuyến (BGP Misconfiguration). Hậu quả đối với người dùng là:
A. Tốc độ cao lên.
B. Gói tin IP được một Router A chuyển đến Router B, nhưng Router B lại TỰ Ý thả (Drop) gói tin mất tích không lý do hoặc chuyển vào hư không, không báo ICMP lỗi, khiến Máy gửi không hiểu vì sao mình bị đứt mạng.
C. Mất điện toàn nhà máy.
D. MAC address bị ẩn.
*Đáp án: B*
*Giải thích: Vụ việc nổi tiếng Youtube bị sập toàn cầu vài chục phút do Pakistan Telecom định tuyến nhầm (BGP hijacking), hút mọi băng thông thế giới (đang vào Youtube) vào mạng của Pakistan rồi drop sạch xuống cống (Blackhole).*

**Câu 99:** Giao thức IP có "Tùy chọn" (Options Header) để hỗ trợ "Source Routing" (Định tuyến do Nguồn quy định - Source dictating the path). Tại sao ngày nay tính năng này CỰC KỲ HIẾM KHI được ISP hỗ trợ và thường bị Tường lửa Block?
A. Nó chậm chạp.
B. Vấn đề bảo mật vô cùng nghiêm trọng. Source Routing cho phép Hacker viết sẵn "Bản đồ đường đi" vào gói tin để Vượt tường lửa, ép gói tin đi vào những mạng nội bộ nhạy cảm và đi ra ngoài hòng ẩn danh (Spoofing).
C. Vì nó tốn bộ nhớ đệm.
D. Vì không tương thích cáp đồng.
*Đáp án: B*
*Giải thích: Trái ngược với Default Routing (Router toàn quyền quyết định), Source routing (Bạn tự quyết định) là cửa hậu cho kẻ phá hoại vượt mặt bảo mật công ty.*

**Câu 100:** Cuối cùng, Tầng Mạng (Network Layer) là tầng phức tạp và khó thay đổi nâng cấp (Ossification) nhất mạng Internet vì:
A. Nó miễn phí nên không ai thèm bảo trì.
B. Lớp Application sửa phần mềm là xong, Lớp Transport (như QUIC) có thể chạy trên trình duyệt. Nhưng Lớp Network bám rễ sâu vào Phần cứng (Hardware/Chip ASICS) của hàng chục tỷ bộ định tuyến Rải rác Khắp toàn cầu, không thể cắm USB hay chạy Lệnh Cập nhật qua đêm toàn thế giới.
C. Tầng mạng bắt buộc mua bản quyền.
D. Cáp quang phải kéo dưới biển.
*Đáp án: B*
*Giải thích: Đó là bi kịch của việc chuyển từ IPv4 sang IPv6 (Kéo dài hơn 30 năm). Sự "cốt hóa" (Ossification) của Tầng Mạng khiến sự đổi mới hạ tầng lõi Internet diễn ra cực kỳ rùa bò.*

**Câu 101:** Bảng định tuyến (Routing Table) và Bảng chuyển tiếp (Forwarding Table / FIB) khác nhau cơ bản ở điểm nào trong Router cổ điển?
A. Không có khác biệt.
B. Routing Table được xây dựng (Build) chậm chạp bằng phần mềm (OSPF/BGP) chứa đủ các loại đường đi tốt/xấu dự phòng. FIB được Cắt tỉa tinh gọn từ Routing Table để bốc xuống cấy thẳng vào Phần cứng tĩnh (ASIC), chứa DUY NHẤT một đường đi ngắn nhất để Xử lý siêu nhanh (Fast path).
C. Routing chứa MAC, FIB chứa IP.
D. Routing chạy cáp, FIB chạy Wi-Fi.
*Đáp án: B*
*Giải thích: Logic "Bộ Não" tính toán cẩn thận (Routing) - "Cơ Bắp" cứ thế mà nhắm mắt làm theo chớp nhoáng (FIB/CEF).*

**Câu 102:** "IP Anycast" khác "IP Broadcast" như thế nào trong hành vi truyền gói tin?
A. Không khác biệt.
B. Anycast là gửi từ 1 người cho nhiều người.
C. Broadcast gửi gói tin ĐẾN TOÀN BỘ các máy trong miền cục bộ (Ai cũng phải nhận). Anycast chỉ chuyển gói tin ĐẾN ĐÚNG MỘT MÁY CHỦ (Gần nhất về mặt chi phí) trong một NHÓM các máy chủ cùng chung 1 IP Anycast trên thế giới.
D. Anycast không dùng địa chỉ đích.
*Đáp án: C*
*Giải thích: Anycast là "Thuật phân thân". Bạn gọi "Alo Cảnh sát (số 113)". Cuộc gọi đó KHÔNG phát loa cho toàn bộ cảnh sát trong nước nghe (Broadcast), mạng viễn thông chỉ nối máy bạn cho Đồn Cảnh Sát ở gần nhà bạn nhất (Anycast).*

**Câu 103:** Tính năng "Policy-based Routing" (Định tuyến dựa trên chính sách - PBR) cho phép Quản trị mạng cấu hình Router bẻ lái gói tin dựa trên tiêu chí nào khác ngoài IP Đích?
A. Không được phép bẻ lái.
B. Router có quyền bỏ qua Bảng FIB thông thường. Nó đọc IP Nguồn, Loại Dịch vụ (Web hay Ping), Port, hoặc Kích thước gói (Cấu hình bằng Access Control List - ACL) để Đẩy gói tin sang một đường cáp hoàn toàn khác theo Ý ĐỒ RIÊNG của người quản trị.
C. Router bẻ lái theo nhiệt độ CPU.
D. Định tuyến theo tên nhà sản xuất.
*Đáp án: B*
*Giải thích: Bình thường Router chỉ nhìn (IP Đích). PBR là "đặc quyền chọc gậy bánh xe": "Nếu giám đốc lướt Web thì cho đi cáp quang A nhanh, nếu sinh viên tải Torrent thì vứt qua cáp đồng B chậm rì".*

**Câu 104:** Giao thức định tuyến "IS-IS" (Intermediate System to Intermediate System) thuộc loại thuật toán định tuyến nào và thường dùng ở đâu?
A. Thuật toán Distance-Vector dùng cho Wi-Fi cá nhân.
B. Thuật toán Link-State (giống OSPF) thường được các Nhà cung cấp dịch vụ Viễn thông (ISP/Telecom) cực kỳ ưa chuộng để định tuyến Mạng Lõi cỡ lớn nội bộ thay vì OSPF do tính linh hoạt với các Tầng khác.
C. Thuật toán Broadcast.
D. Dùng cho kết nối cáp USB.
*Đáp án: B*
*Giải thích: IS-IS là một giao thức cực kỳ mạnh mẽ, vốn thiết kế cho chuẩn ISO OSI cũ, nhưng được tái sử dụng chạy song song hoàn hảo cho cả IPv4 và IPv6 (Integrated IS-IS).*

**Câu 105:** Giao thức "ARP" (Address Resolution Protocol) phục vụ mục đích "Chuyển tiếp qua mỗi chặng" (Hop-by-hop forwarding) như thế nào?
A. Đổi mật khẩu.
B. Khi Router quyết định phải đưa gói tin IP cho Router Kế tiếp (Next-hop) có IP 192.168.1.1, nó BẮT BUỘC phải dùng ARP để hỏi xem cái địa chỉ MAC vật lý của Card mạng con Router kia là gì, mới đóng khung Frame ném qua dây cáp chéo được.
C. Bỏ qua Lớp IP.
D. Nó tìm Cổng Port.
*Đáp án: B*
*Giải thích: Tầng 3 (IP) chỉ ra đường dẫn logic trên bản đồ giấy. ARP là chìa khoá để lắp lốp xe vào trục bánh để chạy trên con đường nhựa vật lý Tầng 2.*

**Câu 106:** Cơ chế "Reverse Path Forwarding" (RPF - Chuyển tiếp Đường dẫn Ngược) thường xuyên được sử dụng kết hợp với Multicast routing nhằm mục đích gì?
A. Tăng băng thông lên mức tối đa.
B. Kiểm tra xem Gói tin Quảng bá (Multicast/Broadcast) có đi vào Router bằng cái CỔNG MÀ NẾU TRUYỀN NGƯỢC LẠI SẼ VỀ TỚI NGUỒN (Đường đi ngắn nhất về Nguồn) hay không. Nếu đi cổng khác (đường vòng rác), Router SẼ DROP gói đó để triệt tiêu các Vòng Lặp Vô Tận (Routing Loops).
C. Thay đổi mật khẩu người dùng.
D. Định tuyến vệ tinh.
*Đáp án: B*
*Giải thích: RPF là cách thông minh để Router phát hiện ra: "Gói rác này đang đi lòng vòng qua mạng và quay lại mặt tao, không được phép Forward tiếp". Rất hiệu quả chống Multicast Storm.*

**Câu 107:** Trong IP Header, trường Protocol = 1 báo hiệu cho Hệ điều hành rằng Payload của gói IP này chứa Giao thức gì?
A. TCP (Protocol = 6)
B. UDP (Protocol = 17)
C. ICMP
D. HTTP
*Đáp án: C*
*Giải thích: Khi mở phong bì IP, Hệ điều hành nhìn số Protocol để biết nên ném cái lõi (Payload) này vào tay Phần mềm TCP, UDP hay ICMP để xử lý tiếp.*

**Câu 108:** Gói ICMP "Time Exceeded" sẽ ĐƯỢC GỬI CHO AI khi một Router trừ TTL xuống 0 và vứt bỏ gói Datagram?
A. Gửi cho Máy nhận đích (Destination Host).
B. Gửi cho tất cả các máy trên mạng (Broadcast).
C. Gửi ngầm cho DNS Server.
D. Gửi trả ngược về chính MÁY GỬI GỐC (Source IP Address) đã sinh ra gói Datagram đó.
*Đáp án: D*
*Giải thích: "Có làm có chịu". Máy nào gửi gói lỗi làm rác đường truyền, Router sẽ gửi trát phạt (ICMP Error) thẳng về nhà máy đó dựa trên Source IP lấy từ gói bị vứt.*

**Câu 109:** Nếu Router lõi đang bận xử lý Bảng chuyển tiếp TCAM (Fast path), liệu nó có khả năng bị quá tải CPU (Control plane) vì nguyên nhân nào khác không?
A. Không bao giờ quá tải vì TCAM siêu nhanh.
B. Có, nếu bị Tấn công DoS bằng ICMP (Ping Flood), hoặc bão thay đổi bảng định tuyến (BGP Flapping), hoặc hàng triệu Gói Phân mảnh IP cần CPU "Mềm" (Process switching/Punt path) nhúng tay xử lý. Cạn CPU -> Router treo.
C. Bị quá tải do đầy ổ cứng lưu trữ.
D. Do quá trình mã hóa cáp quang.
*Đáp án: B*
*Giải thích: Đừng tưởng Router là bất khả chiến bại. Các gói tin Lạ, gói Phân mảnh, gói Báo lỗi, gói Định tuyến... KHÔNG ĐI QUA mạch điện nhanh (ASIC) mà bị "đá lên" CPU mềm để não xử lý. Nếu số lượng này (Control/Management traffic) dồn vào nhiều, Não của Router cũng sẽ treo máy (Crash).*

**Câu 110:** Địa chỉ IP "Dạng Loopback" (127.0.0.1 ở v4, hoặc `::1` ở v6) có đặc tính vật lý nào khi truyền dẫn dữ liệu?
A. Gói tin đi thẳng ra cáp quang nhưng vòng trở lại ở Router.
B. Gói tin KHÔNG BAO GIỜ chạm tới Card mạng Vật lý (NIC). Nó đi vòng ngược trở lại lên Hệ điều hành ngay TẠI BÊN TRONG Cấu trúc Phần mềm Mạng của Máy tính (Loopback interface).
C. Gói tin tự biến đổi thành Analog.
D. Buộc phải có Wi-Fi mới vòng lại được.
*Đáp án: B*
*Giải thích: Dành cho lập trình viên Tự Test phần mềm của mình trên cùng một máy, không tốn bất kỳ tài nguyên mạng LAN hay Internet nào (Thậm chí ngắt mạng vẫn test Localhost bình thường).*

**Câu 111:** IPv6 loại bỏ tính năng Broadcast truyền thống của IPv4 (VD: `255.255.255.255`). Nó thay thế tính năng này bằng cơ chế nào ưu việt hơn?
A. Unicast liên tục.
B. BGP Routing.
C. IPv6 Multicast (với các nhóm xác định cụ thể như "Tất cả các node trong mạng LAN" - `ff02::1`). Điều này giúp Máy tính/Router KHÔNG PHẢI XỬ LÝ (bị làm phiền bởi) các thông báo Quảng bá rác nếu nó không đăng ký tham gia nhóm Multicast đó.
D. Anycast vệ tinh.
*Đáp án: C*
*Giải thích: Broadcast IPv4 là "hét lên cho cả làng nghe", máy không liên quan cũng phải tốn CPU bật tai lên nghe. IPv6 chỉ "hét lên ở cái tần số đặc biệt", ai có tần số đó mới bật máy lên nghe (Tiết kiệm Pin cho thiết bị mạng).*

**Câu 112:** Khái niệm BGP (Border Gateway Protocol) hoạt động dựa trên "Path Vector" (Vector đường dẫn) khác với "Distance Vector" (RIP) ở điểm nào quan trọng nhất?
A. RIP nhanh hơn BGP 10 lần.
B. BGP không chỉ đếm số chặng (Hops/Cost), mà nó GỬI KÈM MỘT DANH SÁCH HOÀN CHỈNH TÊN CÁC TỔ CHỨC (AS Path - Ví dụ: Đi qua FPT, rồi sang VNPT, rồi tới Google) để kiểm soát các Quy định Cấm/Mở kết nối chính trị/thương mại và chống lặp vòng.
C. RIP lưu lại tên quốc gia.
D. Không có khác biệt.
*Đáp án: B*
*Giải thích: Do quy mô toàn cầu, BGP phải biết rõ "Mình đang giao du với ai" chứ không chỉ là "Đi đường nào ngắn". Nếu công ty bạn cấm làm ăn với ISP XYZ, BGP thấy tên XYZ trong AS Path sẽ drop lập tức.*

**Câu 113:** Khi nói về IPv4 Subnetting, ký hiệu `/29` nghĩa là dải mạng này cho phép MỖI MẠNG CON (Subnet) chứa được tối đa bao nhiêu IP có thể Gán (Usable) cho Host?
A. 8
B. 14
C. 6
D. 62
*Đáp án: C*
*Giải thích: /29 tức là Phần Network chiếm 29 bit. Phần Host còn 32 - 29 = 3 bits. Số IP sinh ra = $2^3 = 8$. Trừ IP Mạng (.0) và IP Broadcast (.7) -> Còn 6 IP gắn được.*

**Câu 114:** Địa chỉ MAC hoạt động ở Tầng 2, Địa chỉ IP hoạt động ở Tầng 3. Tại sao mạng lại cần CẢ HAI loại địa chỉ này, thay vì chỉ cần một mã số phần cứng duy nhất?
A. Do chuẩn cũ chưa loại bỏ được.
B. Địa chỉ MAC là phẳng, cố định và đi theo cái thẻ nhựa máy tính đi khắp nơi. Địa chỉ IP là HÀNG LỐI, CÓ TÍNH ĐỊA LÝ/PHÂN CẤP (như số nhà đường phố). Router Tầng 3 dùng IP để "Chỉ đường" liên quốc gia. Switch Tầng 2 dùng MAC để ném đồ trong cự ly hẹp.
C. MAC dùng cho chữ, IP dùng cho số.
D. IP bảo mật hơn MAC.
*Đáp án: B*
*Giải thích: Nếu chỉ dùng MAC (Không có dải khu vực, ai thích đi đâu mang theo MAC đó), Bảng Định tuyến sẽ phải học lòng 8 Tỷ cái MAC loạn xạ trên thế giới -> Bất khả thi.*

**Câu 115:** Kỹ thuật "Network Address Translation" (NAT) phá vỡ nguyên lý End-to-End vì nó làm điều gì với Dữ liệu Giao vận (Transport Layer)?
A. Đổi mật khẩu TCP.
B. NAT không chỉ sửa IP Nguồn/Đích (Layer 3), mà còn sửa lại CẢ Cổng Port (Layer 4) trong TCP/UDP Header, và tính toán lại trường Checksum ở Lớp 4 (và đôi khi là Lớp 7 như FTP) làm chậm quá trình Forwarding.
C. Xóa luôn phần TCP.
D. Biến Router thành Switch.
*Đáp án: B*
*Giải thích: NAT giống như người đưa thư phải bóc bì thư IP, mở tiếp phong bì nhỏ bên trong (TCP) lấy bút xóa cái Số điện thoại liên lạc, viết đè số khác lên, dán lại rồi mới đi giao.*

**Câu 116:** Giao thức mạng "IPsec" có hai giao thức con chính đảm nhiệm mã hóa và xác thực. "ESP" (Encapsulating Security Payload) dùng để làm gì?
A. Tính cước mạng.
B. Nó là bộ phận chính thực hiện việc Mã hóa toàn bộ dữ liệu bí mật (Cung cấp tính Bảo mật) và Đảm bảo Tính toàn vẹn/Xác thực gốc (Data integrity & origin authentication).
C. Nó chỉ trao đổi Key.
D. Đặt tên người gửi.
*Đáp án: B*
*Giải thích: Trong cấu trúc IPsec (ví dụ VPN của cơ quan), ESP là thằng đóng vai trò lấy Data cho vào két sắt khóa lại. Giao thức con còn lại (AH) chỉ kiểm tra tem niêm phong chứ không mã hóa.*

**Câu 117:** Mạng IPv6 sử dụng khái niệm "Prefix Delegation" (Ủy quyền tiền tố) để tự động hóa chức năng nào cho các Bộ định tuyến gia đình (Home Routers)?
A. Cấp mã MAC động.
B. Nhà mạng (ISP) thay vì cấp cho Router nhà bạn 1 cái IP như IPv4, ISP sẽ đẩy hẳn cho Router nhà bạn một MẢNG MẠNG KHỔNG LỒ (Ví dụ khối `/56`). Router nhà bạn tự động băm cái khối đó thành nhiều Subnet (/64) để xài cho Wi-Fi, LAN tự động.
C. Dịch tên miền DNS.
D. Ngắt kết nối từ xa.
*Đáp án: B*
*Giải thích: Đây là sự xa xỉ của IPv6. ISP chia sỉ một mảng (1 triệu tỷ IP) thẳng xuống nhà bạn. Cái Router quèn ở nhà bạn bỗng trở thành 1 đại gia quản lý IP chia lẻ lại cho tủ lạnh, tivi...*

**Câu 118:** Cấu trúc Router hiện đại (Ví dụ Juniper, Cisco cao cấp) thực hiện Tách biệt Mặt phẳng Điều khiển (Control) và Chuyển tiếp (Forwarding). Thành phần Phần cứng nào làm nhiệm vụ Chuyển tiếp?
A. Intel CPU Core i9.
B. Line Cards (Các card Giao diện chứa cổng quang) kết nối trực tiếp với Switching Fabric bằng chip phần cứng ASIC để tra bản FIB ở tốc độ ánh sáng mà không cần báo cáo lên não.
C. RAM DDR4.
D. Ổ đĩa cứng HDD.
*Đáp án: B*
*Giải thích: "Não" (CPU) nằm ở trên cao (Routing Engine). Khi có Bảng Chỉ đường, nó cấy bảng đó xuống Từng cái Chân (Line Card). Các Chân tự đá gói tin đi mà không cần hỏi Não.*

**Câu 119:** Nếu một Router không hỗ trợ Multicast, nó sẽ làm gì khi nhận được một gói tin IP Multicast (Ví dụ Đích là 224.x.x.x)?
A. Broadcast bừa đi mọi cổng.
B. Tự động nâng cấp phần mềm.
C. Vứt bỏ (Drop) gói tin đó ngay lập tức, vì nó KHÔNG THỂ KHỚP cái IP Đích lạ lẫm đó vào bất kỳ Dòng Chỉ đường Thông thường (Unicast FIB) nào của nó.
D. Chặn mọi truy cập sau đó.
*Đáp án: C*
*Giải thích: Để 1 tivi xem được luồng Multicast, BẮT BUỘC 100% các Router từ Nhà Đài tới nhà bạn phải bật (Enable) giao thức Multicast Routing (như PIM). Chỉ 1 mắt xích ngu ngơ, luồng Video sẽ gãy.*

**Câu 120:** Trong Tầng Mạng, giao thức ICMP có thể được kẻ xấu lợi dụng làm Tấn công TỪ CHỐI DỊCH VỤ (Ping of Death) bằng thủ thuật nào?
A. Ping đúng chuẩn 64 byte.
B. Phá hủy cáp mạng.
C. Gửi một gói ICMP Echo Request khổng lồ vượt quá giới hạn lý thuyết tối đa của IP (65535 bytes) bằng cách lách luật chỉnh sửa thông số "Phân mảnh Offset". Máy nhận khi Lắp ráp lại sẽ bị Tràn Bộ Nhớ Đệm và Crash Hệ điều hành.
D. Tự làm cháy máy tính kẻ gửi.
*Đáp án: C*
*Giải thích: Đây là lỗi bảo mật kinh điển thời Win 95/98 (Ping of Death). HĐH mù quáng dán các mảnh vỡ lại, khi ráp thành cục to hơn RAM cho phép, màn hình xanh lè.*

**Câu 121:** Quá trình "Decapsulation" (Bóc vỏ/Giải đóng gói) tại Router đối với một Datagram đi ngang qua nó diễn ra như thế nào?
A. Router tháo toàn bộ IP, TCP, HTTP.
B. Router nhận một Frame từ cáp (L2), Bóc bỏ vỏ Frame (Header/Trailer L2) để moi ra gói IP Datagram (L3). Router Đọc IP Đích, tính lại TTL. Xong nó lại lấy gói IP đó ĐÓNG LẠI thành một cái Frame L2 MỚI TOANH để tống ra cáp mạng khác.
C. Router sửa đổi nội dung TCP.
D. Không cần tháo gì cả.
*Đáp án: B*
*Giải thích: Ở mỗi nấc (Hop), Gói tin thay đổi áo khoác MAC ngoài cùng (Tầng 2), nhưng Ruột IP (Tầng 3) và TCP (Tầng 4) vẫn bất di bất dịch.*

**Câu 122:** Chức năng "Flow Table" trong mạng SDN (như giao thức OpenFlow) dựa vào tiêu chí nào để đưa ra Quyết định (Action)?
A. Chỉ dựa vào IP Đích.
B. Dựa vào sự Match (So khớp) với nhiều trường cùng lúc nằm rải rác trên L2, L3, L4 (Ví dụ: MAC nguồn là A, IP Đích là B, Port UDP là C). Nếu Khớp, nó thực hiện Hành động (như Forward ra cổng 5, hoặc Drop chặn virus).
C. Dựa vào tốc độ mạng cáp.
D. Theo nhiệt độ RAM.
*Đáp án: B*
*Giải thích: Sức mạnh của OpenFlow nằm ở khả năng "So khớp Đa chiều" (Multi-dimensional matching) biến Switch cùi bắp thành con quái vật thông minh đa dụng.*

**Câu 123:** Tại sao BGP lại được gọi là giao thức định tuyến "Vector Đường Dẫn" (Path Vector)?
A. BGP sử dụng hệ thống vector 3D.
B. Vì để thông báo sự tồn tại của 1 dải mạng, Router BGP không ném con số khoảng cách vô hồn (Cost=5). Nó NÉM NGUYÊN MỘT CHUỖI TÊN (Ví dụ: Qua mạng Viettel, qua mạng FPT, qua Singtel). Bất cứ ai thấy tên mình trong chuỗi đó sẽ DROP lập tức để CHỐNG LẶP VÒNG (Routing Loop).
C. Vì BGP dùng vector quang học.
D. Thay đổi đường dẫn vật lý.
*Đáp án: B*
*Giải thích: "AS-PATH" là linh hồn của BGP giúp nó tránh thảm họa Loop trên mạng Internet toàn cầu (vấn đề mà RIP gặp rất nhiều).*

**Câu 124:** Một khối địa chỉ IP là `10.0.0.0/16`. Subnet mask của nó khi viết ở định dạng hệ 10 sẽ là:
A. 255.0.0.0
B. 255.255.0.0
C. 255.255.255.0
D. 255.255.255.255
*Đáp án: B*
*Giải thích: /16 nghĩa là 16 bit 1 liên tục (11111111.11111111.00000000.00000000), quy đổi thành hệ 10 là 255.255.0.0.*

**Câu 125:** Dải địa chỉ IP nội bộ loại C (Class C Private IP) mà các bộ Router Wi-Fi gia đình rất hay dùng mặc định là:
A. 10.0.0.0 đến 10.255.255.255
B. 172.16.0.0 đến 172.31.255.255
C. 192.168.0.0 đến 192.168.255.255
D. 8.8.8.0 đến 8.8.8.255
*Đáp án: C*
*Giải thích: Đây là dải địa chỉ quen thuộc nhất hành tinh, 192.168.1.1 thường là IP để truy cập trang quản trị Router.*

**Câu 126:** Kỹ thuật nào giúp các công ty tiết kiệm CỰC KỲ NHIỀU địa chỉ IP Public đắt đỏ, nhưng bù lại gặp khó khăn rất lớn khi triển khai ứng dụng VoIP (Gọi thoại SIP/RTP)?
A. Cắm cáp quang.
B. DNS Server.
C. NAT (Network Address Translation). NAT thay đổi port và IP của các luồng SIP/RTP, làm cho Máy chủ Tổng đài (SIP Server) bên ngoài Internet không thể nhận diện được địa chỉ thực của máy khách và không thể báo máy khác gọi lại được (Âm thanh đi 1 chiều).
D. IPv6 SLAAC.
*Đáp án: C*
*Giải thích: Lập trình Voice/Video Call là cực hình vì phải lách qua con NAT cùi bắp chặn đường. Phải dùng đủ mẹo (STUN, TURN, ICE) tốn kém băng thông để vượt ngục.*

**Câu 127:** Trong thuật toán Dijkstra (Dùng trong OSPF), một Router phải biết được thông tin gì để chạy tính toán?
A. Không cần biết gì cả.
B. Chỉ cần biết thằng hàng xóm kế bên.
C. Router cần một cơ sở dữ liệu Toàn cảnh Lưới mạng (Link-State Database), tức là Nắm Rõ TẤT CẢ các liên kết, khoảng cách giữa MỌI con Router trong công ty (Global view). Từ bản đồ đó nó mới chạy toán học tìm đường ngắn nhất.
D. Biết cấu hình phần cứng của switch.
*Đáp án: C*
*Giải thích: Trái ngược với Distance-Vector (mù mờ), Link-State (OSPF) yêu cầu "Sự hiểu biết tường tận". Bù lại tốn rất nhiều RAM của Router để chứa cái Bản đồ (Database) này.*

**Câu 128:** "Broadcast Storm" (Cơn bão quảng bá) sẽ ĐÁNH SẬP một mạng LAN nhanh chóng nếu:
A. Thiết kế mạng có "Vòng lặp" vật lý (Loop) bằng cách cắm 2 sợi cáp chéo giữa 2 cái Switch không hỗ trợ giao thức chặn vòng (Spanning Tree Protocol). Các gói Broadcast (có Đích FF:FF) cứ thế chạy lòng vòng nhân bản lên tỷ lần làm cháy đèn Switch.
B. Đăng nhập sai mật khẩu.
C. Vào web phim HD quá nhiều.
D. Cáp đồng xoắn bị đứt lõi.
*Đáp án: A*
*Giải thích: Đừng bao giờ lấy 1 sợi dây mạng, cắm cả 2 đầu vào 2 lỗ trên cùng 1 Switch rẻ tiền. Toàn mạng của cơ quan sẽ rớt mạng do bão sấm chớp Lớp 2.*

**Câu 129:** Sự khác biệt của kiến trúc SD-WAN so với MPLS WAN cổ điển của Viễn thông?
A. SD-WAN đắt gấp 10 lần.
B. MPLS dựa vào cấu hình cực cứng nhắc, đắt đỏ của Phần cứng Nhà mạng lõi. SD-WAN xây dựng một "Đám mây Phần mềm" ở trên (Overlay), cho phép công ty cắm MỌI LOẠI ĐƯỜNG TRUYỀN RẺ TIỀN (3G, Cáp gia đình) vào Thiết bị biên, Thiết bị biên tự động bọc mã hóa gửi qua Internet, điều khiển bằng Web Controller.
C. SD-WAN tắt định tuyến.
D. MPLS chặn IPv6.
*Đáp án: B*
*Giải thích: Làn sóng SD-WAN bùng nổ vì nó giúp Doanh nghiệp cắt được chi phí khổng lồ phải trả cho các đường truyền riêng (Leased-line) đắt đỏ, trong khi vẫn đạt được tốc độ và bảo mật y hệt.*

**Câu 130:** Trong bảng IPv4, một Datagram mang Cờ "DF" (Don't Fragment - Không được phân mảnh) bằng 1. Nếu Router không thể đẩy nó qua liên kết có MTU nhỏ hơn, Router bắt buộc phải:
A. Tự sửa Cờ thành 0.
B. Chém gói tin ra thành 2.
C. Bỏ qua luật cấm, cứ phân mảnh.
D. Drop gói tin đó, và gửi ngược 1 gói ICMP "Fragmentation Needed but DF Set" (Cần chia nhỏ nhưng cấm cắt) về cho Máy gửi. Máy gửi thấy báo lỗi sẽ tự động tìm MTU thấp hơn (Path MTU Discovery).
*Đáp án: D*
*Giải thích: TCP sử dụng triệt để thủ thuật này (Path MTU Discovery) để tự động đo xem kích thước Ống nhỏ nhất trên toàn chặng đường là bao nhiêu, giúp nó chọn MSS tối ưu, KHÔNG BAO GIỜ bị Router băm gói.*

**Câu 131:** Trong thiết kế ICMPv6 (Dùng cho IPv6), chức năng nào đã được sáp nhập MẠNH MẼ vào giao thức này (mà ở IPv4 nó là giao thức rời)?
A. HTTP
B. ARP. IPv6 loại bỏ ARP (dùng Broadcast) và thay bằng "Neighbor Discovery Protocol" (NDP) chạy TRÊN NỀN TẢNG ICMPv6 và sử dụng Multicast an toàn hơn.
C. DNS
D. FTP
*Đáp án: B*
*Giải thích: IPv6 ghét cay ghét đắng Broadcast. Do đó ARP (kẻ chuyên làm ồn mạng bằng Broadcast) bị vứt bỏ, thay bằng người anh em NDP êm ái hơn.*

**Câu 132:** Ký hiệu "Hop Limit" trong IPv6 Header thực chất đóng vai trò gì (tương đương trong IPv4)?
A. MAC Address
B. Subnet Mask
C. Time-to-Live (TTL). Khi bằng 0 thì gói tin bị vứt bỏ.
D. TOS / DSCP
*Đáp án: C*
*Giải thích: IPv6 đổi tên cho đúng bản chất. TTL cũ tính bằng thời gian (Giây) dù thực tế đếm bằng số Trạm (Hops). IPv6 đổi thẳng tên thành Hop Limit cho rõ nghĩa.*

**Câu 133:** Cơ chế "VRF" (Virtual Routing and Forwarding) trên các Router có tác dụng gì?
A. Tách 1 Router vật lý thành nhiều Router ảo độc lập Lôgic. Mỗi Router ảo có một Bảng Định tuyến riêng rẽ 100%. Cho phép nhiều dải IP TRÙNG LẶP của nhiều công ty khách hàng cùng tồn tại trên 1 cục sắt Router của ISP.
B. Tạo mạng Wi-Fi mạnh hơn.
C. Nén video 4K.
D. Gửi mật khẩu dạng MD5.
*Đáp án: A*
*Giải thích: Giống như VLAN chia nhỏ Switch, VRF chia nhỏ Router (chia não). Cục Router của Viettel có thể chạy VRF cho Ngân hàng A (có IP 10.0.0.0) và VRF cho Ngân hàng B (CŨNG CÓ IP 10.0.0.0) mà gói tin không bị đi lộn phòng.*

**Câu 134:** Cổng kết nối (Interface) mặc định để Tầng mạng của một máy tính kết nối và định tuyến tới phần cứng Card Mạng nội bộ Tự thân là cổng nào?
A. Cổng WAN
B. Cổng LAN 1
C. Cổng Loopback `lo0` (hoặc Loopback Interface).
D. Cổng HDMI
*Đáp án: C*
*Giải thích: Giao diện `lo0` là cái cầu nối mềm (Software-only) giúp các ứng dụng trên cùng một máy gọi thẳng cho nhau mà không phải chui qua dây nhợ hỏng hóc.*

**Câu 135:** Một gói tin IP có Dải đích là `10.10.10.0/24`. Trong bảng định tuyến có 2 quy tắc: `10.10.0.0/16` đẩy ra cổng 1, và `0.0.0.0/0` (Default Route) đẩy ra cổng 2. Router sẽ đẩy gói tin này ra cổng nào?
A. Cổng 2.
B. Cổng 1. (Do nguyên tắc Longest Prefix Match, /16 bao trùm và dài hơn /0 nên nó sẽ trúng quy tắc cụ thể hơn).
C. Cả cổng 1 và 2.
D. Vứt bỏ.
*Đáp án: B*
*Giải thích: Bạn ghi thư gửi "Quận 1, HCM". Luật 1: "Đi miền Nam" cổng 1. Luật 2: "Mọi nơi khác" cổng 2. Do "Quận 1" nằm trong miền Nam, và chữ miền Nam CỤ THỂ HƠN mọi nơi khác, thư đi cổng 1.*

**Câu 136:** Trong định tuyến IP, "Default Route" (Tuyến mặc định) được biểu diễn bằng ký hiệu mạng nào?
A. 255.255.255.255/32
B. 127.0.0.1/8
C. 0.0.0.0/0
D. 192.168.1.1/24
*Đáp án: C*
*Giải thích: 0.0.0.0/0 bao trùm TOÀN BỘ không gian địa chỉ IPv4. Nó là giải pháp "Cửa thoái lui" cuối cùng khi Router tra bảng không khớp với bất kỳ dòng dải mạng cụ thể nào.*

**Câu 137:** Một gói tin IP có giá trị TTL (Time To Live) khởi tạo là 64. Sau khi đi qua 4 bộ định tuyến (router), giá trị TTL còn lại bao nhiêu?
A. 64
B. 60
C. 68
D. 0
*Đáp án: B*
*Giải thích: Mỗi khi gói IP đi qua MỘT Router (ở Lớp 3), Router bắt buộc phải trừ đi 1 đơn vị TTL trước khi chuyển tiếp.*

**Câu 138:** Giao thức NAT (Network Address Translation) sửa đổi thông tin gì trong gói tin TCP/IPv4 đi ra ngoài Internet?
A. Chỉ sửa Source MAC.
B. Chỉ sửa Source IP.
C. Sửa Source IP (thành IP Public của Router) và sửa Source Port TCP/UDP, cập nhật Checksum.
D. Sửa Destination IP.
*Đáp án: C*
*Giải thích: Do NAT Overload (PAT) chia sẻ 1 IP Public cho nhiều máy nội bộ, nó phải gán cho mỗi luồng 1 Port ngẫu nhiên mới để phân biệt.*

**Câu 139:** Kỹ thuật nào giúp giảm bớt gánh nặng bảng định tuyến BGP toàn cầu bằng cách gom nhiều dải mạng con liên tiếp thành một dải lớn?
A. OSPF Area
B. VLSM (Variable Length Subnet Masking)
C. Route Summarization (Route Aggregation / CIDR)
D. Anycast
*Đáp án: C*
*Giải thích: Thay vì quảng bá 4 dòng /24, Router gộp lại thành 1 dòng /22 duy nhất.*

**Câu 140:** Máy A và Máy B nằm trên hai Subnet (VLAN) khác nhau. Để A ping được B, gói tin bắt buộc phải đi qua thiết bị nào?
A. Một Switch Layer 2 thuần túy.
B. Hub.
C. Router (Hoặc Switch Layer 3) đóng vai trò Gateway.
D. Access Point Wi-Fi.
*Đáp án: C*
*Giải thích: Giao tiếp liên mạng (Inter-VLAN routing) bắt buộc phải có can thiệp của Lớp 3 để bóc IP ra xem hướng định tuyến.*

**Câu 141:** Phương thức định tuyến nào sau đây TỰ ĐỘNG CẬP NHẬT đường đi khi một tuyến cáp quang bị đứt?
A. Static Routing (Định tuyến tĩnh do Admin gõ tay).
B. Dynamic Routing (Định tuyến động - OSPF, BGP, EIGRP).
C. Default Routing.
D. MAC Flooding.
*Đáp án: B*
*Giải thích: Định tuyến động giúp mạng có khả năng "Chống chịu lỗi" (Fault tolerance) tự nhiên.*

**Câu 142:** Trong header IPv4, trường Header Checksum CHỈ BẢO VỆ phần nào?
A. Chỉ bảo vệ phần Payload (Data TCP/UDP).
B. Bảo vệ toàn bộ gói tin (Header + Payload).
C. Chỉ bảo vệ riêng phần IPv4 Header. Nếu bit trong Header bị lỗi, Router sẽ drop gói tin.
D. Không bảo vệ gì.
*Đáp án: C*
*Giải thích: Tầng IP không quan tâm Payload hỏng hay không (đó là việc của Checksum L4 TCP/UDP).*

**Câu 143:** Lệnh PING sử dụng thông điệp ICMP Echo Request. Nếu bị Tường lửa (Firewall) chặn PING, Tường lửa đã chặn chính xác thông tin gì?
A. Chặn Port TCP 80.
B. Chặn Port UDP 53.
C. Chặn ICMP Type 8 (Echo Request) hoặc Type 0 (Echo Reply).
D. Chặn MAC Broadcast.
*Đáp án: C*
*Giải thích: Nhiều quản trị viên tắt Ping từ bên ngoài vào Server để tránh lộ IP Server cho hacker dòm ngó.*

**Câu 144:** IPv6 hỗ trợ loại địa chỉ "Link-Local" (fe80::/10). Đặc tính của địa chỉ này là:
A. Tương đương IP Public, định tuyến được toàn cầu.
B. Chỉ có giá trị sử dụng giao tiếp TRONG PHẠM VI 1 ĐƯỜNG LINK (1 subnet L2). Router tuyệt đối KHÔNG chuyển tiếp các gói tin mang địa chỉ Link-Local sang mạng khác.
C. Dùng làm IP Loopback.
D. Dành riêng cho Multicast.
*Đáp án: B*
*Giải thích: Trong IPv6, dù bạn chưa cấu hình DHCPv6 hay SLAAC, máy tính vẫn TỰ ĐỘNG sinh ra 1 IP Link-Local để chat với các máy trong cùng phòng.*

**Câu 145:** Một tổ chức xin được dải IP `172.16.0.0/16`. Họ chia nhỏ ra bằng Subnet Mask `/24`. Tổ chức này có thể tạo ra bao nhiêu Subnet?
A. 24
B. 16
C. 256 (Tương đương mượn 8 bit: $2^8$)
D. 65536
*Đáp án: C*
*Giải thích: Mượn phần Host 8 bit (Từ /16 lên /24). 8 bit mượn này tạo ra $2^8 = 256$ mạng con độc lập.*

**Câu 146:** Địa chỉ MAC đích của một gói tin Broadcast IP (`255.255.255.255`) ở mạng LAN sẽ được hệ điều hành đóng gói thành MAC nào?
A. 00:00:00:00:00:00
B. FF:FF:FF:FF:FF:FF
C. Phải gọi ARP để tìm.
D. Dùng MAC của Gateway.
*Đáp án: B*
*Giải thích: IP Broadcast luôn đi cặp với MAC Broadcast để tát cả Switch và Máy tính trong LAN đều phải mở ra nghe.*

**Câu 147:** BGP chọn đường đi (Best Path Selection) khác với OSPF ở chỗ:
A. OSPF dựa trên số lượng Router (Hop count).
B. OSPF dựa trên Băng thông (Cost) để tính đường Nhanh/Ngắn nhất. BGP chọn đường theo các Thuộc tính (Attributes) và Chính sách (Policy) đã được cấu hình tay (Local Preference, AS Path ngắn nhất, MED).
C. Cả 2 đều dùng chung thuật toán Dijkstra.
D. BGP tự động ping thử đường truyền.
*Đáp án: B*
*Giải thích: BGP linh hoạt cực độ để phục vụ Thương mại. Tôi có đường cáp 10Gbps sang FPT, nhưng tôi cấu hình BGP bắt chạy qua đường 1Gbps của Viettel vì tôi đang nợ tiền FPT.*

**Câu 148:** Lệnh `arp -d *` trên hệ điều hành Windows dùng để làm gì?
A. Ping toàn mạng.
B. Xóa (Flush) toàn bộ bộ nhớ đệm ARP Cache của máy tính, ép máy tính phải hỏi lại MAC từ đầu nếu muốn giao tiếp.
C. Hiển thị ARP.
D. Tắt card mạng.
*Đáp án: B*
*Giải thích: Rất hữu ích khi mạng LAN vừa bị thay đổi Switch/Router làm sai MAC, máy tính vẫn lưu MAC cũ dẫn đến mất mạng.*

**Câu 149:** Trong SDN (Software-Defined Networking), ưu điểm của việc "Tập trung hóa" (Centralized) Control Plane là:
A. Tăng băng thông cáp quang.
B. Các Router L2/L3 phần cứng rẻ tiền hơn.
C. Controller có "Cái nhìn Toàn cục" (Global View) của Toàn bộ sơ đồ mạng (Topology) theo thời gian thực. Nó có thể tính toán định tuyến cực kỳ tối ưu, điều phối Load Balancing mà không bị "mù mờ cục bộ" như OSPF chạy trên từng router lẻ tẻ.
D. Bỏ được TCP/IP.
*Đáp án: C*
*Giải thích: Giống như bạn chơi Game chiến thuật nhìn từ trên cao, bạn điều khiển lính đi đường nào tốt nhất, thay vì để lính tự tìm đường.*

**Câu 150:** Tại sao Giao thức ICMP lại bị chặn (Block) trên một số Tường lửa Internet?
A. Vì nó gây tốn tiền.
B. Lợi dụng ICMP có thể thực hiện DDoS (Ping Flood), quét mạng (Reconnaissance) hoặc lợi dụng ICMP Tunnels để tuồn dữ liệu mật ra ngoài một cách lén lút xuyên qua tường lửa lỏng lẻo.
C. Vì nó quá chậm.
D. Vì nó dùng quá nhiều cổng Port.
*Đáp án: B*
*Giải thích: Do tính chất "Vô thưởng vô phạt", Firewall đôi khi bỏ qua ICMP. Hacker chế tạo mã độc giấu dữ liệu ăn cắp vào thân gói Ping để tuồn ra ngoài Internet.*

**Câu 151:** Trong Bảng định tuyến (Routing table), thông số "Metric" (hoặc Cost) có ý nghĩa gì?
A. Cước phí trả cho ISP.
B. Là giá trị độ ưu tiên của một Tuyến đường. Nếu có 2 đường đi đến cùng 1 Đích, Router sẽ chọn Tuyến đường có Metric THẤP NHẤT (Đường đi tốn ít chi phí/băng thông nhất).
C. Là độ dài gói tin.
D. Là thời gian Ping RTT.
*Đáp án: B*
*Giải thích: Metric OSPF tính bằng Công thức `100 Mbps / Bandwidth`. Đường 1Gbps có Cost nhỏ hơn đường 100Mbps.*

**Câu 152:** "Administrative Distance" (AD) của một tuyến đường mang ý nghĩa:
A. Khoảng cách địa lý tính bằng dặm.
B. Độ tin cậy (Ưu tiên) CỦA GIAO THỨC ĐỊNH TUYẾN sinh ra tuyến đường đó. (VD: Tuyến đường gõ tĩnh (Static) có AD=1, OSPF có AD=110. Nếu Cùng chỉ đường tới 1 Đích, Router tin Đường Static hơn Đường OSPF).
C. Số lượng Router phải đi qua.
D. Trọng lượng gói tin.
*Đáp án: B*
*Giải thích: Nếu 2 "Ông chỉ đường" cãi nhau. Tôi tin ông nào uy tín hơn (AD nhỏ hơn).*

**Câu 153:** Thuật toán Routing "Distance-Vector" bị vướng phải vấn đề kinh điển nào khi mạng có sự cố?
A. Tràn RAM ngay lập tức.
B. Vấn đề "Đếm đến vô cùng" (Count-to-Infinity). Do Router B nghe tin từ Router A, Router C nghe từ B. Khi A sập, B không biết lại đi nghe C nói "Tao có đường tới A này", thế là 2 thằng C và B cứ đẩy gói tin qua lại vô tận đếm số Hop lên mãi.
C. Máy tính sập nguồn.
D. Tự động đổi IP MAC.
*Đáp án: B*
*Giải thích: RIP giải quyết bằng cách chặn Mốc Infinity ở số Hop = 16 (Gói đi quá 15 hop là drop).*

**Câu 154:** Địa chỉ IPv6 `::1/128` tương đương với địa chỉ nào ở IPv4?
A. 0.0.0.0
B. 192.168.1.1
C. 127.0.0.1 (Localhost / Loopback)
D. 255.255.255.255
*Đáp án: C*
*Giải thích: Viết tắt của `0000:0000:0000:0000:0000:0000:0000:0001`.*

**Câu 155:** Công nghệ NAT traversal (Vượt NAT) nào cho phép các thiết bị phía sau Tường lửa GIAO TIẾP VỚI NHAU một cách gián tiếp thông qua một máy chủ công cộng trung gian, làm chuyển tiếp TOÀN BỘ gói tin của 2 bên?
A. STUN.
B. TURN (Traversal Using Relays around NAT). Vì 2 cái NAT quá cứng đầu không cho đục lỗ chéo (Symmetric NAT), 2 máy tính đành phải nhờ 1 cái Máy Chủ TURN ở giữa làm "Trạm trung chuyển" toàn bộ băng thông. Rất tốn kém cho Server.
C. ICE.
D. DNS.
*Đáp án: B*
*Giải thích: Giải pháp cuối cùng (Fallback) của Discord/Skype khi tính năng đục lỗ P2P thất bại.*

**Câu 156:** Kỹ thuật chia mạng VLSM (Variable Length Subnet Mask) là gì?
A. Đổi IP liên tục.
B. Chia một mạng lớn thành các Mạng con CÓ KÍCH THƯỚC (Subnet Mask) KHÁC NHAU tùy theo nhu cầu thực tế, nhằm tiết kiệm tối đa Không gian IP. (VD: Chia mạng /24 ra thành mạng /25, /26, /30 chứ không chia đều rập khuôn).
C. Chuyển IPv4 thành IPv6.
D. Thay cáp đồng trục.
*Đáp án: B*
*Giải thích: Phân bổ IP kiểu Cổ điển cắt bánh quá lãng phí (Mạng nối 2 router chỉ cần 2 IP, nhưng bị cắt nguyên miếng 256 IP). VLSM cấp đúng cái mạng /30 (4 IP) cho 2 router đó.*

**Câu 157:** Thiết bị nào được gọi là "Layer 3 Switch" (Switch Lớp 3)?
A. Hub chia mạng.
B. Switch Tầng 2 được nhồi thêm chức năng Phần Mềm (HĐH) và Phần Cứng Định Tuyến (Routing Lớp 3). Nó có thể làm Gateway, chạy OSPF, chuyển tiếp gói tin giữa các VLAN y hệt một Router thực thụ, nhưng Nhanh Hơn bằng ASIC.
C. Switch phát Wi-Fi.
D. Tường lửa mềm.
*Đáp án: B*
*Giải thích: Cisco Catalyst 3560/3850 là L3 Switch. Thường dùng trong mạng Lõi Tòa nhà (Core/Distribution) vì nó chuyển mạch IP nhanh hơn Router biên truyền thống.*

**Câu 158:** Một gói Datagram IPv4 có cờ `MF` (More Fragment) = 0 và `Fragment Offset` = 0. Điều này ngụ ý gì?
A. Nó là mảnh vỡ cuối cùng.
B. Nó là một gói tin Hoàn Chỉnh, KHÔNG BỊ PHÂN MẢNH (Nguyên vẹn từ đầu đến cuối).
C. Nó bị lỗi cấu trúc.
D. Nó là mảnh đầu tiên của gói bị phân mảnh.
*Đáp án: B*
*Giải thích: Offset = 0 (bắt đầu từ đầu). MF = 0 (phía sau không còn mảnh nào). Kết luận: Gói nguyên khối.*

**Câu 159:** Một tổ chức sử dụng công cụ BGP để "Multi-homing" (Nối 2 nhà mạng ISP). Để kiểm soát gói tin RA KHỎI mạng của mình, họ dùng thuộc tính BGP nào?
A. AS-Path Prepending.
B. Local Preference (Sự ưa thích Cục bộ). Định tuyến nội bộ để ép các Router của tổ chức ƯU TIÊN xuất dữ liệu qua đường ISP A (Local Pref cao) thay vì đường ISP B (Dùng làm Backup).
C. MED.
D. OSPF Cost.
*Đáp án: B*
*Giải thích: Local Pref là công cụ cực mạnh của BGP để "Điều tiết giao thông Lối Ra" (Outbound Traffic Engineering).*

**Câu 160:** Cấu trúc IPv6 cung cấp trường "Flow Label" (20-bit). Mục đích thiết kế của nó là:
A. Cấm tải video.
B. Cho phép Router nhận diện nhanh NHỮNG GÓI TIN THUỘC CÙNG MỘT LUỒNG (Ví dụ 1 cuộc gọi Video) để Cung cấp Chất lượng dịch vụ (QoS) Mượt Mà, đi chung một đường nhất quán, mà KHÔNG CẦN Router phải mở sâu gói tin ra xem TCP Port/TOS.
C. Chứa Mật khẩu.
D. Lưu tên người dùng.
*Đáp án: B*
*Giải thích: IPv6 sinh ra ở thời đại Media bùng nổ, Flow Label là tầm nhìn xa để tối ưu hóa thiết bị chuyển mạch video.*

**Câu 161:** Giao thức định tuyến "OSPF" sử dụng khái niệm "Area" (Khu vực) để làm gì trong các Mạng Doanh Nghiệp Cỡ Lớn (Enterprise)?
A. Đổi mật khẩu khu vực.
B. Tránh việc MỘT Bảng Định Tuyến (Link-State Database) phình to khủng khiếp chứa cả vạn Router. Bằng cách chia làm nhiều Area (Area 0 là xương sống Backbone), Router ở Area 1 chỉ cần biết Chi Tiết bản đồ Area 1, và Đẩy mọi thứ ngoài biên cho Area 0. Giảm tải RAM và CPU cực lớn.
C. Phân chia phòng ban vật lý.
D. Không cho các khu vực gửi email cho nhau.
*Đáp án: B*
*Giải thích: OSPF là thuật toán ngốn RAM (vì mỗi con Router chứa nguyên cái bản đồ toàn công ty). Phân chia Area là bắt buộc khi công ty có quá đông Router.*

**Câu 162:** Gói tin ICMP "Redirect" (Đổi hướng) được Router sử dụng với mục đích tốt gì?
A. Làm sập máy trạm.
B. Khi Máy trạm A có 2 Router (R1 và R2) chung LAN. A ngớ ngẩn gửi gói tin cho R1 (Gateway mặc định) để ra Internet. R1 thấy "Quái, đường này R2 đi nhanh hơn", R1 sẽ tống gói tin sang R2, ĐỒNG THỜI gửi 1 gói ICMP Redirect về báo cho A: "Lần sau mày gửi thẳng cho R2 cho lẹ, đừng gửi qua tao nữa".
C. Dịch tên miền thành IP.
D. Xin cấp IP động.
*Đáp án: B*
*Giải thích: Tính năng tối ưu mạng nội bộ rất thông minh, giúp máy tính tự động học được Gateway tốt hơn mà không cần Admin chỉnh tay.*

**Câu 163:** Kỹ thuật "Route Poisoning" (Đầu độc Tuyến đường) trong các thuật toán định tuyến Distance-Vector (RIP) là hành động:
A. Phát tán virus độc hại.
B. Khi một Router phát hiện cáp tới Mạng A bị Đứt. Nó KHÔNG XÓA dòng đó, mà TỐI ĐA HÓA CỐT (Đặt Metric của Mạng A = Infinity/16). Rồi Báo Cáo ngay cho láng giềng: "Đường tới Mạng A là XA VÔ TẬN". Láng giềng nghe thấy lập tức tin ngay và xóa bỏ đường đó. Giúp tránh Lặp vòng (Count-to-Infinity).
C. Tăng tốc độ mạng.
D. Mở port cho Firewall.
*Đáp án: B*
*Giải thích: Một trong những phương pháp "Truyền tin xấu nhanh nhất có thể" để dọn dẹp các đường cáp đứt.*

**Câu 164:** Giao thức MPLS (Multiprotocol Label Switching) chèn thêm một cái "Label" (Nhãn) vào giữa gói tin. Nhãn này (Thường gọi là Layer 2.5) mang lợi ích Cốt Lõi gì?
A. Nó biến dữ liệu thành Text.
B. Router MPLS (LSR) không cần đọc cái IP Header dài dòng 20 Byte nữa. Nó CHỈ ĐỌC MỖI CÁI NHÃN 4 BYTE (cực ngắn) và Tra bảng Nhãn Tốc độ Chớp Mắt (Dùng phần cứng), rồi Tráo Nhãn (Swap Label) ném ra cổng đi tiếp.
C. Bỏ qua TCP Checksum.
D. Truyền mã hóa 2 lớp.
*Đáp án: B*
*Giải thích: Công nghệ giúp Mạng Viễn Thông xử lý hàng Terabit/s luồng dữ liệu 4G, FTTH mượt mà không bị nghẽn CPU Core Router.*

**Câu 165:** Tại Tầng 3 Mạng IP, nếu một Datagram lớn bị phân mảnh làm 3 (Fragment 1, 2, 3) trên đường đi. Tuy nhiên mảnh số 2 BỊ RỚT trên mạng. Kết quả ở Máy Nhận là gì?
A. Máy nhận tự lắp ráp mảnh 1 và 3 thành gói thiếu data.
B. Máy nhận xin IP Router lại mảnh 2.
C. Máy nhận chờ hết thời gian Timeout (Reassembly Timeout), sau đó VỨT BỎ CẢ 3 MẢNH (Vứt Mảnh 1 và 3 đã nhận được). Phải đợi TCP ở trên gửi lại Toàn bộ cục Data Gốc lớn ban đầu. Sự lãng phí khủng khiếp.
D. Mạng bị cháy nổ.
*Đáp án: C*
*Giải thích: Tầng Mạng IP không có "Truyền lại một phần nhỏ". Do đó Phân mảnh (IP Fragmentation) là Kẻ thù số 1 của Băng Thông Mạng thực tế.*

**Câu 166:** "Traceroute" có thể hoạt động nhưng KHÔNG ĐẢM BẢO 100% Vẽ Ra Tuyến Đường CHÍNH XÁC bởi vì:
A. Tên miền thay đổi.
B. Cáp đứt thường xuyên.
C. Hiện tượng Định Tuyến Không Đối Xứng (Asymmetric Routing) hoặc Cân Bằng Tải (Load Balancing). Gói TTL=1 đi đường A, gói TTL=2 có thể bị Router tống đi Đường B (do cân bằng tải), gói TTL=3 đi Đường C. Traceroute in ra một Bản đồ "Lai tạp" không có thực.
D. UDP không hỗ trợ TTL.
*Đáp án: C*
*Giải thích: Trên Internet khổng lồ, luồng gói tin hiếm khi đi một mạch 1 con đường độc đạo. Traceroute chỉ là công cụ tham khảo tương đối.*

**Câu 167:** "Broadcast IP" `255.255.255.255` được gọi là "Limited Broadcast" (Quảng bá Hạn chế) vì:
A. Bị giới hạn tốc độ.
B. Nó CHỈ CÓ TÁC DỤNG TRONG PHẠM VI MẠNG LAN CỤC BỘ (Subnet). Bộ Định Tuyến (Router) NGHIÊM CẤM 100% Việc CHUYỂN TIẾP (Forward) Gói Tin Này Xuyên Qua Biên Giới Ra Ngoài Subnet Khác, tránh Bão Broadcast Toàn Cầu.
C. Không cho phép IPv6 chạy.
D. Phải nén dung lượng.
*Đáp án: B*
*Giải thích: Nếu Router cho phép chuyển tiếp cục 255.255.255.255. Một hacker có thể đút 1 gói tin mà đánh sập Internet toàn trái đất.*

**Câu 168:** Thiết bị "NAT Router" gia đình thực hiện việc "Port Address Translation" (PAT). Trong bảng NAT, Dòng dữ liệu sau được lưu trữ `[192.168.1.10 : 3456] <--> [14.15.16.17 : 5001]`. IP `14.15.16.17` là gì?
A. IP Máy tính.
B. IP Public Công cộng (Mặt ngoài của Router hướng ra Internet do ISP cấp).
C. IP của Máy Chủ Google.
D. Tên miền.
*Đáp án: B*
*Giải thích: Cả nhà bạn (dù 100 cái điện thoại) khi ra lướt Web thì Google cũng CHỈ NHÌN THẤY đúng 1 cái IP Public là 14.15.16.17 này đập vào mặt Google.*

**Câu 169:** Mạng "Overlay Network" (Mạng phủ) là thuật ngữ kiến trúc chỉ loại mạng nào?
A. Mạng chạy dưới đất.
B. Một Hệ thống Mạng Ảo (Logical Network) được xây dựng đè lên trên một Hạ Tầng Mạng Có Sẵn. Ví dụ: VPN, P2P BitTorrent, CDN, SD-WAN. Chúng sử dụng Mạng IP vật lý làm "Ống dẫn" (Underlay) nhưng tự tạo Bản đồ Định tuyến Logic riêng cho mình.
C. Mạng bị treo đứng.
D. Mạng cấm mã hóa.
*Đáp án: B*
*Giải thích: Overlay là cách Người ta lách qua sự Cứng ngắc của Tầng Mạng IP vật lý. Tự vẽ ra một chân trời mới Ảo hóa mềm dẻo hơn.*

**Câu 170:** IP Protocol quy định rằng Giao tiếp Mạng là "Vô hướng / Phi kết nối" (Connectionless). Trái lại, Mạng điện thoại cũ dùng Mạch (Circuit Switching) hoặc mạng ATM là "Hướng kết nối" (Connection-oriented). Tại sao Internet IPv4/v6 lại chọn mô hình Connectionless?
A. Rẻ tiền hơn, vì nó ĐẨY SỰ PHỨC TẠP CỦA VIỆC ĐẢM BẢO TIN CẬY ra phía Hai ĐẦU MÁY TÍNH CÁ NHÂN (TCP/Edge). Router Mạng Lõi được giải phóng RAM, trở nên cực kỳ Ngu ngốc nhưng SIÊU NHANH, RẺ và Khả năng chịu sự cố Đứt Cáp Rất Cao (Tự động đổi đường không cần thiết lập lại mạch).
B. Tốn nhiều điện năng.
C. Bắt buộc dùng Wi-Fi.
D. Đắt đỏ nhưng bảo mật.
*Đáp án: A*
*Giải thích: Triết lý thiết kế (Design Philosophy) quan trọng nhất của Internet. "Dumb Network - Smart Edge" (Mạng ngu ngốc - Đầu cuối Thông minh).*

**Câu 171:** Một Gói IP đi qua Tường Lửa (Firewall), Tường Lửa KHÔNG cấu hình NAT, chỉ Drop/Accept. Địa chỉ MAC Nguồn (Source MAC) và MAC Đích (Dest MAC) của Gói IP đó có bị thay đổi sau khi xuyên qua Tường lửa không (Nếu Tường Lửa cấu hình chế độ Mạng Xuyên Thấu - Transparent L2 Bridge)?
A. Đổi toàn bộ MAC.
B. KHÔNG ĐỔI BẤT KỲ CÁI GÌ. Tường lửa Chế Độ Mạch Cầu L2 (Transparent/Bump-in-the-wire) ẩn mình hoàn toàn về mặt Lớp 2. Gói tin đi qua như đi qua một sợi dây cáp vô hình.
C. Đổi IP đích.
D. Xóa Checksum.
*Đáp án: B*
*Giải thích: Đây là cách triển khai IPS/Firewall đỉnh cao ở Doanh nghiệp. Cắm Firewall vào giữa mạng mà không cần đổi Cấu hình IP/Routing của bất kỳ máy tính nào trong phòng.*

**Câu 172:** Chức năng "ARP Proxy" (Proxy ARP) trên Router có tác dụng gì?
A. Làm Router bốc cháy.
B. Cho phép Router "Đứng ra nhận hộ" (Trả lời giả mạo ARP Reply bằng MAC của chính Router) khi một Máy tính gào lên Broadcast hỏi MAC của một IP NẰM KHÁC MẠNG LAN. Giúp Máy tính ngốc nghếch (cấu hình nhầm Subnet Mask) vẫn có thể vứt gói tin ra Internet thông qua Router.
C. Giảm băng thông Wi-Fi.
D. Cấm TCP chạy.
*Đáp án: B*
*Giải thích: Proxy ARP là cái Mẹo Sửa sai hệ thống. Cực kỳ tiện lợi nhưng cũng tạo ra Bão Lội ARP nếu dùng sai cách.*

**Câu 173:** Các giao thức như DHCP, ARP, ICMP là những giao thức "Đóng Đinh" (Crucial) cho Mạng Cục bộ (LAN) hoạt động. Giao thức nào tương đương với cả 3 thằng này Gộp Lại ở môi trường mạng IPv6?
A. NAT64.
B. ND (Neighbor Discovery Protocol - Giao thức Khám phá Láng giềng). Chạy bằng ICMPv6, nó làm MỌI THỨ: Thay ARP để dò MAC, Thay DHCP để Cấp IP (SLAAC), Làm nhiệm vụ tìm Default Gateway (Router Solicitation).
C. EIGRP v6.
D. OSPF v3.
*Đáp án: B*
*Giải thích: IPv6 gộp mọi sự lộn xộn của IPv4 lại vào một Bộ Giao Thức Khám Phá gọn gàng, an toàn (bằng Multicast thay vì Broadcast).*

**Câu 174:** Giao thức định tuyến "BGP" của Internet Toàn cầu dễ bị sụp đổ bởi yếu tố nào nhất?
A. Yếu tố Phần Cứng của Card Mạng.
B. Sự Tin Cậy Mù Quáng. BGP truyền thống Không Có Xác Thực Mã Hóa (No Authentication). Một Lỗi Cấu Hình Nhầm Của Kỹ sư mạng (Bấm lộn số AS) có thể làm Đảo Lộn Định Tuyến của Hàng Loạt Quốc Gia (BGP Route Leak/Hijacking).
C. Sóng Tần Số Radio.
D. Đổi cáp quang sang cáp đồng.
*Đáp án: B*
*Giải thích: Lỗ hổng khổng lồ của Internet. Hiện nay đang cố gắng vá bằng cách triển khai RPKI (Ký số BGP) để xác thực các dải mạng quảng bá.*

**Câu 175:** Tại sao Địa chỉ IPv4 `169.254.x.x` (APIPA) lại KHÔNG THỂ LƯỚT WEB Internet được (Dù bạn ping máy bên cạnh chung phòng thì được)?
A. Vì APIPA bị cài Virus.
B. IP này thuộc dải "Link-Local" (Chỉ dùng riêng trong cự ly 1 Cáp LAN). CÁC ROUTER BIÊN VÀ ISP SẼ LẬP TỨC DROP (VỨT BỎ) BẤT KỲ GÓI TIN NÀO CÓ IP ĐÍCH HOẶC NGUỒN thuôc DẢI 169.254.x.x này, nên nó không bao giờ chui ra Khỏi Cửa Nhà Bạn được.
C. IP APIPA bị mã hóa.
D. Do lỗi Trình duyệt.
*Đáp án: B*
*Giải thích: Bản chất của Link-Local là "Tự kỉ cục bộ".*

**Câu 176:** Trong Tầng Mạng IP, khái niệm "Control Plane" Tập Trung Của SDN (Controller) Sử Dụng Các Thiết Kế Toán Học Tương Tự Như:
A. Tự sửa ổ cứng.
B. Hệ thống Điều hành Tập Trung. Nó Gom Tất Cả Bản Đồ Mạng Của Toàn Bộ Switch Vào MỘT MÁY CHỦ, Áp dụng Thuật toán Dijkstra trên Máy chủ đó, rồi Đổ (Push) Bảng Chuyển Tiếp Trực Tiếp (Flow Table) Dạng Tĩnh Xuống Mọi Switch. Switch không còn phải Vất Vả Chạy Toán học gì nữa.
C. Cài mật khẩu BIOS.
D. Chạy Cáp quang siêu nhanh.
*Đáp án: B*
*Giải thích: SDN là cuộc Cướp Quyền Não Bộ. Switch L3/Router đắt tiền bị Cướp não, Trở thành cái Switch ngu ngốc L2 giá rẻ mạt, Mọi trí thông minh chuyển lên Controller trung tâm trên Đám Mây.*

**Câu 177:** Ký hiệu IPv6 `::` (Hai dấu hai chấm) có luật sử dụng khắt khe nào?
A. Dùng ở đâu cũng được, vô số lần.
B. CHỈ ĐƯỢC PHÉP XUẤT HIỆN DUY NHẤT 1 LẦN TRONG MỘT ĐỊA CHỈ IPV6. Nó dùng để viết tắt CÁC CỤM SỐ 0 (Ví dụ: `0000:0000:0000`) LIÊN TIẾP NHAU. Nếu dùng 2 lần, Máy tính sẽ không biết mỗi `::` đại diện cho bao nhiêu số 0 để giãn ngược lại thành 128 bit.
C. Cấm dùng trong Wi-Fi.
D. Thay thế dấu Chấm v4.
*Đáp án: B*
*Giải thích: Viết `2001::1::2` là Sai Cú Pháp Nghiêm trọng, vì máy tính không biết cái `::` đầu là mấy con 0, cái `::` sau là mấy con 0.*

**Câu 178:** Phân mảnh Gói IP (Fragmentation) chỉ áp dụng cho Giao thức Tầng Giao vận nào DỄ DÀNG nhất?
A. TCP
B. UDP. Vì UDP vứt nguyên 1 Cục Dữ liệu Lớn thẳng xuống IP. Cục dữ liệu đó bị cắt làm 3 Gói IP Mảnh (Fragment 1, 2, 3).
C. ICMP
D. IGMP
*Đáp án: B*
*Giải thích: TCP đã chủ động chặt Data ra thành Các Cục MSS Siêu Nhỏ (1460 Byte) từ trong Tầng 4, Nên Khi rớt xuống Tầng 3 (IP), Gói IP nó bọc cũng Chỉ to 1500 Byte, Nhỏ hơn hoặc Bằng MTU Chuẩn, Không Cần Phân Mảnh.*

**Câu 179:** Giao thức định tuyến Nội bộ Mạng (IGP) phổ biến "EIGRP" (Enhanced Interior Gateway Routing Protocol) là sản phẩm Độc quyền của hãng thiết bị Mạng nào trước khi mở chuẩn?
A. Microsoft
B. Google
C. Cisco Systems. Nó lai tạo Sự Nhanh Nhạy của Distance Vector với Sự Nhận Thức Toàn Cục Của Link-State, tạo ra Thuật toán DUAL siêu hội tụ độc quyền trên các thiết bị Cisco.
D. IBM
*Đáp án: C*
*Giải thích: Ngày xưa Mua Router Cisco đắt gấp 3 hãng khác vì cái phần mềm "Ma Thuật" (EIGRP) này. Giờ Cisco đã Mở Mã Nguồn EIGRP cho các hãng khác dùng.*

**Câu 180:** "Multicast IP" khác "Broadcast IP" ở điểm:
A. Multicast chặn Virus, Broadcast lan truyền Virus.
B. Broadcast bắt BUỘC TẤT CẢ mọi thiết bị trong LAN phải Nhận và Xử lý Gói. Multicast CHỈ YÊU CẦU Các thiết bị ĐÃ CHỦ ĐỘNG ĐĂNG KÝ (Bằng giao thức IGMP) gia nhập Nhóm Multicast đó mới phải Xử lý, Giảm Rác CPU Cực Kỳ Lớn Cho Mạng LAN.
C. Multicast dùng cáp đồng, Broadcast cáp quang.
D. Đổi định dạng thành IPv6.
*Đáp án: B*
*Giải thích: Đăng ký Multicast Giống như Bấm Nút Subcribe Youtube. Ai Subcribe thì mới Nhận Thông báo (Notification). Kẻ lướt rác ngoài đường sẽ không Bị Ting Ting Phiền Hà.*

**Câu 181:** Khái niệm "Data Plane" trong Tầng Mạng chịu trách nhiệm xử lý tác vụ gì TRÊN MỖI mili-giây (Per-Packet)?
A. Gọi điện thoại báo hỏng cáp.
B. CHỈ việc Chuyển tiếp (Forwarding). Nó phải hoạt động 100% bằng Silicon Mạch Cứng (Phần cứng ASICs) cực rẻ, cực nhanh để Đọc IP Đích -> Tra Bảng FIB -> Ném ra Cổng. Không có tư duy, không có tính toán đường.
C. Bỏ qua Tầng Vật Lý.
D. Mã hóa Gói tin BGP.
*Đáp án: B*
*Giải thích: Nếu nhúng não vào từng mili-giây, Router sẽ sụp đổ. Các hãng như Cisco/Juniper bán Router đắt tiền không phải vì Phần mềm, mà vì Các Mạch Silicon chuyên dụng chớp nhoáng (Switching Fabric).*

**Câu 182:** "Quá trình Hội tụ" (Convergence Time) của Mạng OSPF là gì?
A. Tải phim 4K.
B. Thời gian từ lúc MỘT CÁP MẠNG BỊ ĐỨT (Gây thay đổi Sơ đồ) cho đến khi TẤT CẢ CÁC ROUTER TRONG CÔNG TY nhận được Bản tin Cập nhật, Tính toán Lại Toàn Bộ Đường Đi Mới, và Nạp Xong Bảng Định Tuyến Mới. Trong lúc Hội tụ, Mạng có thể Bị Đi Lạc (Routing Loop) tạm thời.
C. Nén Dữ Liệu IP.
D. Sạc pin cho Router.
*Đáp án: B*
*Giải thích: Rớt mạng 5 Giây Nghĩa là Mạng OSPF cần 5 giây để Hội tụ (Convergence) chuyển đường. Mạng càng Xịn thì Thời gian Hội tụ Càng Siêu Tốc (Dưới 50 mili-giây).*

**Câu 183:** Nếu gói tin IPv4 có Cờ "Don't Fragment" (DF=1) Bật Cứng, và Router gặp đường Cáp Có MTU cực bé (Vd: Cáp Đồng Cũ 500 Bytes). Router Xử lý sao?
A. Cố nhét Gói 1500 Bytes vô Cáp 500 Bytes.
B. Vứt Gói Tin Đó Vào Hư Không Và Lặng Im.
C. CHẶN Vứt Bỏ Gói Tin (Drop), VÀ QUAN TRỌNG NHẤT: Trả Về MỘT GÓI ICMP BÁO LỖI (Fragmentation Needed) Về Cho Trạm Nguồn, Khai Báo Luôn MTU Của Đường Cáp Yếu Đó. Máy Nguồn Biết Lỗi Tự Giảm Kích Thước Gói Xả Lại Từ Đầu.
D. Hack Đổi IP Trạm Nhận.
*Đáp án: C*
*Giải thích: Tính Năng Sống Còn Giúp Tầng Mạng Vận Hành (Path MTU Discovery). TCP Dựa Hẳn Vào Cơ Chế Này Của Tầng 3 Để Chọn Cỡ Gói Tin Gửi.*

**Câu 184:** Bảng MAC Table Của Switch Tầng 2 Lưu Trữ Trong RAM Bao Lâu?
A. Vĩnh Viễn.
B. Đóng Lưu Ổ Cứng SSD Của Máy Chủ.
C. Thời Gian Lão Hóa (Aging Time - Thường Là 300 Giây / 5 Phút). Nếu Máy Tính Rút Cáp Hoặc Không Gửi Gói Tin Nào Trong 5 Phút, Cổng MAC Đó Sẽ Bị Xóa Trắng Khỏi RAM Để Giải Phóng Bộ Nhớ Tránh Lỗi.
D. Lưu Trên Đám Mây Mạng.
*Đáp án: C*
*Giải thích: Mọi Cấu Trúc Bảng Chuyển Tiếp Tự Động Học Đều Phải Có "Aging" (Lão Hóa) Để Tránh Rác Làm Đầy Trí Nhớ.*

**Câu 185:** Kỹ Thuật "Port Address Translation" (PAT) Hay Còn Gọi Là "NAT Overload" Xử Lý Vấn Đề Thiếu IPv4 Ra Sao Cực Đoan Nhất?
A. Bán Thêm IP Bằng Tiền Tỷ.
B. Nó Ánh Xạ Đến 65.535 KẾT NỐI (Socket LAN Khác Nhau Của Cả Công Ty) Chui Chung Qua ĐÚNG MỘT (1) ĐỊA CHỈ IP PUBLIC DUY NHẤT Do ISP Cấp. Nó Lấy Sạch Quỹ Số Port 16-Bit Của TCP/UDP Ra Làm Số Định Danh Cứu Mạng Chống Trùng.
C. Đổi MAC Của Điện Thoại Thành Router IP.
D. Biến Mọi File Thành Văn Bản Gzip Cỡ Nhỏ.
*Đáp án: B*
*Giải thích: Điểm Thiên Tài Nhất Cứu Internet IPv4 Sống Thêm 30 Năm (Thay Vì Chết Yểu Năm 1995). Nhưng Phá Hủy Tự Do P2P Của Mạng Mẽo Đầu Cuối.*

**Câu 186:** Khi Dùng VPN (Mạng Riêng Ảo Lớp 3 - IPsec Tunnel), Gói Tin Bạn Bị Xử Lý Đặc Thù Ra Sao?
A. Tắt Wi-Fi Thay Bằng Dây.
B. Gói Tin Có IP Đích Nằm TRONG LAN Công Ty Bạn (Vd: 192.168.10.x). Phần Mềm VPN Bọc Gói Đó Kín Lại (Mã Hóa). Dán Ngoài Vỏ IP Nguồn (Của Bạn) Và IP Đích (Của Cổng Cty Ngoài Internet - 14.x.x.x). Ném Gói Tin Ra Internet. Gói Xuyên Internet Về Công Ty Bị Bóc Vỏ Mở Ra IP Mật Vứt Lại Vô Tường Lửa Nội Bộ Chạy Bình Thường.
C. Không Cho Phép Truyền Packet Khác Subnet.
D. Đổi Giao Thức UDP Quá Giới Hạn Cáp Quang Thành USB Cáp Ngầm.
*Đáp án: B*
*Giải thích: Ảo Thuật Lớp 3 Kinh Điển Nhất (Overlay Encapsulation). Tạo Cho Con Người Cảm Giác Như Đang Cắm Dây Trực Tiếp Tại Bàn Làm Việc Văn Phòng Mặc Dù Đang Nằm Ở Biển Đảo Cách Nửa Bờ Trái Đất.*

**Câu 187:** Địa Chỉ IP Lớp 4 (Transport) Là Khái Niệm Đúng Hay Sai?
A. Cực Kỳ Đúng Vì IP Của TCP Tốt Hơn UDP Đỉnh Điểm.
B. Rất Đúng Do Switch Hỗ Trợ Port Đầu Cuối Mạnh Hơn Router.
C. HOÀN TOÀN SAI. IP (Internet Protocol) Là Giao Thức Lớp 3 (Network Layer). Lớp 4 (Transport Layer) KHÔNG CÓ Khái Niệm ĐỊA CHỈ IP, Lớp 4 Chỉ Có "Số Hiệu Cổng - Port Number" (VD: 80, 443).
D. Lớp 4 Sinh Ra Lớp IP.
*Đáp án: C*
*Giải thích: Đề Thi Luôn Đánh Lừa Tư Duy Cơ Bản Của Dân Ngoại Đạo. Nếu Không Nắm Chắc Các Lớp Layer OSI Bóc Tách Khái Niệm Sẽ Đi Sai Hướng Hoàn Toàn 100%.*

**Câu 188:** Trong Kỹ Thuật "Longest Prefix Match", Router Sẽ Chọn Dòng Nào Sau Đây Nếu IP Đích Của Gói Tin Là `192.168.1.150`?
Dòng 1: `192.168.1.0/24` Hướng Cổng A.
Dòng 2: `192.168.1.128/25` Hướng Cổng B.
Dòng 3: `0.0.0.0/0` Hướng Cổng C.
A. Cổng A Vì Nó Rộng.
B. Cổng C Vì Mặc Định Là Rộng Vô Tận.
C. CỔNG B. Vì /25 Cụ Thể, Dài Hơn Và Bọc Gọn Rút Sát Cấu Trúc Nhất (Khớp 25 Bit Khít Hoàn Hảo So Với /24 Chỉ Khớp 24 Bit).
D. Lỗi Bị Vứt Sọt Rác.
*Đáp án: C*
*Giải thích: IP .150 Nằm Gọn Lỏn Nửa Mạng Sau Của Mạng /24 (Là Mạng .128 Lên .255). Do Đó Thằng /25 Bắt Trúng Tình Huống Chi Tiết Hơn Rất Nhiều Rất Chuẩn Xát.*

**Câu 189:** Giao Thức "BGP" Của Mạng Liên Quốc Gia Tránh Vòng Lặp Bằng Đặc Điểm Nào Thay Vì Dùng "Đếm Hop = 16" Cổ Của RIP?
A. Nó Nén Gói Dữ Liệu Rác.
B. Thay Đổi Cáp Quang Bằng Ăng Ten Sóng Ngắn.
C. Router BGP TRƯỚC KHI THÊM 1 Dải Mạng Vào Sổ, Nó NHÌN CHUỖI DANH SÁCH (AS_PATH) Các Mạng Nó Vừa Đi Qua. Nếu NÓ THẤY SỐ AS (TÊN NÓ) ĐÃ NẰM SẴN TRONG CÁI CHUỖI ĐÓ -> CHỨNG TỎ GÓI TIN ĐANG ĐI LÒNG VÒNG TRỞ LẠI -> NÓ LẬP TỨC DROP DÒNG ĐỊNH TUYẾN ĐÓ ĐI.
D. Biến UDP Thành IPv6 Tự Dưỡng.
*Đáp án: C*
*Giải thích: Triết Lý Mềm Mỏng Của Việc Đánh Nhãn. Nếu Tôi Đã Ở Trong Căn Phòng ĐÓ Rồi, Tại Sao Cảnh Sát Lại Hướng Dẫn Tôi Đi Vô Lại Căn Phòng Đó? Vòng Lặp Vô Định (Loop).*

**Câu 190:** Giao Thức "NDP" (Neighbor Discovery Protocol) Thay Thế ARP Trong IPv6 Sử Dụng Cơ Chế Phát Sóng Nào?
A. Broadcast Vung Vãi Ra Toàn Không Khí Vô Hướng (FF:FF...).
B. Mở IPsec Toàn Bộ Máy Chủ Khác Biệt Băng Tần Sóng Gốc.
C. ICMPv6 MULTICAST (Solicited-Node Multicast). Một Dạng Broadcast Có Giới Hạn Siêu Nhỏ. Máy Hỏi Sẽ Ghép Mã Cầu Nối IPv6 Sang Một Dải Multicast Đích Chuyên Dụng Tương Ứng Với Vài Con Máy Cuối. Chỉ Những Con Máy Đang Cùng Dải Multicast Cuối Đó Mới Bật Bộ Nhớ Lên Xử Lý Để Trả Lời MAC Về, Giảm Ô Nhiễm Bão Rác CPU Hoàn Toàn 100%.
D. Cấm TCP Chạy Qua Lớp Router Lõi BGP.
*Đáp án: C*
*Giải thích: Đỉnh Cao Tối Ưu Năng Lượng Cho Tivi Và Bóng Đèn Gắn Tường. Chúng Không Rảnh Để Giải Quyết Những Tiếng Gào Thét Tìm Nhau Của Máy Tính Kế Bên, Chúng Đang Ngủ Pin (Sleep).*

**Câu 191:** Thuật Lập Trình Lõi Của IPv6 (Header Cơ Bản 40 Bytes) Hoàn Toàn Gạt Bỏ Việc Gắn Thêm Lựa Chọn (Options). Vậy Nếu Muốn Thêm Tùy Biến Định Tuyến Vào IPv6 Thì Gắn Nơi Đâu?
A. Nén Thành Frame L2 Dư Thừa Bị Cắt Tỉa.
B. SỬ DỤNG MỘT CHUỖI CÁC "HEADER MỞ RỘNG" (Extension Headers) NHÉT CHÚI VÀO PHÍA SAU LƯNG HEADER GỐC. Header Gốc Nối Vào Header Mở Rộng 1, Header 1 Trỏ Tiếp Tới Header Nối 2 Móc Xích Thành Tàu Lửa... Nhờ Vậy Khung Mạch Nhanh (ASIC Router Lõi) Cứ Việc Lờ Đi Tàu Lửa Nối Chạy Thẳng Đi Miễn Khớp Header 40B Cứng Nhanh Siêu Tốc Xử Lý Nhảy Tuyến Hoàn Mỹ.
C. Chèn Mật Khẩu FTP.
D. Đưa Vô Transport Lớp 4 TCP Giữ.
*Đáp án: B*
*Giải thích: Mọi Tinh Hoa Kỹ Thuật Tập Trung Vào Bài Toán "Nhanh Lẹ Nhất Dành Cho Cỗ Máy So Khớp Silicon".*

**Câu 192:** Chức Năng ICMP (Ping, Traceroute) Có Thể Gây Nguy Hiểm Rò Rỉ Thông Tin Nội Bộ Mạng Nhà Ra Sao?
A. Nó Khóa Password Mạng Trạm Cáp.
B. Kẻ Xấu Có Thể (Scan Ping Sweep) Phóng 1 Vạn Gói ICMP Vào 1 Vạn IP Nội Bộ Để Dò Xét Vẽ Ra Chính Xác Sơ Đồ Có Bao Nhiêu Máy Chạy IP Nào, Hệ Điều Hành Nào Đang Sống Xung Quanh Trong Công Ty Vừa Để Xâm Nhập Đánh Cắp (Reconnaissance) Và Để Đoán Bảng Định Tuyến.
C. Gây Tụt Áp Điện Thoại Nổ Pin Hư Mạch Trong Mainboard.
D. Bắt Tường Lửa Ngắt RAM.
*Đáp án: B*
*Giải thích: Dấu Hiệu Quét ICMP Dò Dẫm Liên Tục Là Giai Đoạn Đếm Ngày Đếm Phút Bọn Đột Nhập Trinh Sát Căn Nhà Chờ Mở Cửa Sổ Hỏng Mà Lẻn Vào Nửa Đêm Đục Đẽo Két Sắt Nằm Bên Trong Server Core Kế Toán.*

**Câu 193:** Một Router Gặp Phải 1 Cú Nghẽn Mạng Cực Lớn Tạm Thời Khác Biệt Rất Ít CPU Băng Thông Ra. Hàng Đợi (Queue) Của Nó Gắn Thêm Bộ Đệm 5GB To Khủng Tràn RAM Trải Dài. Hậu Quả Ác Mộng Của "Bufferbloat" Là Gì?
A. Rớt Mạng Đứt Ngay Đứt Luôn Chuyển Ngành Rời Sóng Biển Lẻ Lõi Vứt.
B. GÓI TIN KHÔNG BAO GIỜ BỊ RỚT (Bị vứt bỏ) VÌ BỘ ĐỆM QUÁ TO. Nhưng 1 Gói Tới Đuôi Bị Tắc Xếp Hàng Mãi Mãi HÀNG GIÂY (Chờ Lâu Hơn Mạng Vệ Tinh Trễ). TCP Đo RTT Cực Lớn Vỡ Trận. Cảnh Báo "Khủng Cực Về Độ Trễ" Sinh Ra Độ Chênh Giật Hình Jitter Thê Thảm Game Online Nhảy Trễ Ping Khóc Liệt Tận Cùng Nhức Đầu.
C. Mất Dữ Liệu Tải Chữ Méo Mó Dữ Dội Không Phục Hồi Code 404 Nát.
D. Chạy 1 Tốc Độ Vèo Biển Lặng Y Hệt Thường.
*Đáp án: B*
*Giải thích: Càng "Ôm Hàng Khư Khư Sợ Mất", Hệ Thống Router Càng Trở Nên Lệch Lạc Rề Rà Tái Phạm Năng Lực Trì Chệ Của Chuẩn Mực Dòng Chảy Stream Trơn Tru Tức Thì Không Độ Trễ Low Latency Ngày Nay.*

**Câu 194:** Tại Sao BGP Có Thể Quyết Định Nắn Một Lô Gói Tin (Destination VN) Chạy Vòng Nửa Vòng Trái Đất Qua Mỹ Rồi Mới Quành Lại VN (Thay Vì Đi Thẳng Đường Biển AAG VN - VN Cực Nhanh 2ms Trực Tiếp Bóp Méo Hiệu Năng)?
A. BGP Bị Virus Router Đánh Sập RAM Bỏ Rơi Mật Mã.
B. Định Tuyến BGP (BGP Routing) KHÔNG CHĂM CHĂM Chọn Đường NGẮN NHẤT. Nó Tuân Theo SỰ LỰA CHỌN KINH TẾ/THƯƠNG MẠI (Economic Policies). Ví Dụ Cáp Vòng Sang Mỹ Lại Là Cáp Của Hãng A Cấp "Miễn Phí Rẻ Tiền", Còn Cáp Nối Nhanh VN Lại Chậm Nhỏ Của Hãng B Đòi Cước Cắt Cổ. Admin Quyết Định Ưu Tiên Đường Rẻ Nhất Để Cứu Lợi Nhuận, Dù Cho Trễ 200ms Đi Xa.
C. Do DNS Lỗi Rớt Máy Đổ Sập Bản Mạng Cache Lõi Rút.
D. Cáp Cắm Lệch Dây Ngược Mặt Biển Khơi Rắn.
*Đáp án: B*
*Giải thích: Chào Mừng Đến Thế Giới Thực Tại Lọc Lừa Thương Trường Viễn Thông Xứ Khổng Lồ Nơi Đồng Tiền Đo Bằng Dây Cáp (Peering/Transit).*

**Câu 195:** Lệnh Nào Có Thể Bị Lạm Dụng Biến Giao Thức RIP Bỗng Chốc Bóp Méo Sai Đường Đứt Đoạn Nạp Đè Hệ Điều Hành Cả Tòa Nhà Trong Vòng 2 Phút Chơi Xấu?
A. Route Poisoning Báo Cáp Chết Thật 16 Hop Vứt Đi Chạy Nơi Khác.
B. HACKER cắm LAPTOP Cài Giao Thức RIP Rác Nhái Làm "Router Đểu" Vào Trong Mạng Công Ty Rống To Lên Bằng Broadcast: "Đường Đi Tới Máy Chủ Server Công Ty Chỉ Cách Tôi 0 Hop Dài Thôi (Tức Là Tôi Đang Giữ Két Sắt Nè), Hãy Đẩy Data Tới Phía Cổng Của Tôi Đi". Các Switch Vội Vã Tin Cập Nhật RIP Thảy Data Vô Hết Cáp Của Kẻ Gian Đội Lốt Mù Mờ (RIP Spoofing Lừa).
C. Tắt DHCP Khép Cửa Xin IP Lại Từ Đầu Đòi Thường Sóng Wi-Fi Thụ Thủng.
D. Xóa OSPF Vùng 0 Khóa Hủy Giao Thức Gốc Băng Sóng Không Nghe Gọi Lỗi UDP Bứt Cứng Đứt Lại Sợi Quang Đen Dẫn Điện Chạy Thẳng Ngang.
*Đáp án: B*
*Giải thích: Các Giao Thức Định Tuyến Nội Bộ Thường Tin Tưởng Đồng Nghiệp Tới Mức Ngu Ngốc Thiếu Sự Xác Minh Thẻ Bài Ký Chữ (Auth OSPF Route) Dẫn Tới Tổn Thất Trầm Trọng Nhức Nhối Cửa Sau Xuyên Qua Sóng Gầm Nhà Dưới Vực.*

**Câu 196:** "SDN Controller" Đóng Vai Trò Gì Trong Mạng Ảo Hóa "Kiến Trúc Lập Trình Linh Hoạt Phần Mềm Hóa"?
A. Làm Chỗ Lưu Mạng Trữ Phim Bãi Rác Cho Mạng Máy Chủ Cháy Ổ HDD Chập Lệch Cứu Phục.
B. Nó Là Bộ Não Toàn Tri. Nó Không Xử Lý 1 Khung L2 Nào Hết, Nhưng Nó Ra Lệnh Cho 1 Triệu Cái Công Tắc (Switch Vô Tri Giác Phần Cứng Dưới Lầu Đất) Bằng 1 Dòng Cập Nhật Bảng API. Đẩy Code Cấu Hình Giảm Đứt Từ Tay Xong Tức Tối Hàng Tỷ Băng Băng Cả Thành Phố Nối Nhau Tuân Lệnh Đồng Loạt Tích Tắc Siêu Phàm Bắt Data Bay Lượn Bẻ Cong Hoàn Hảo Theo Phần Mềm C# Khóa Nhanh Chóng Cắt Rẻ Gọn Trơn Lỗi Ngập Dọn Nhanh Chóng Mạng Trung Tâm Dữ Liệu Cloud.
C. Bóc Vỏ TCP Gỡ Header Gửi Pass Báo Hacker Xin Đổi Bán Hàng Trái Phép Mã Code UDP Tẩy Đi Lậu Sửa Đổi Trích Cáp Cho To Tường Chắn Sóng Tần OSPF Rỗng Ruột Rỗng Không IP Lõ Lõi Biển Cát Mù.
D. Thay IP Bằng IPv4 Chặn Truy Cập Wi-Fi Xoáy Sâu Vô Vạch Đen Điện Năng Biển Nước Ngọt Quý.
*Đáp án: B*
*Giải thích: Đưa Nền Công Nghệ Khép Kín Cứng Đầu CISCO Vào Việc Thiết Kế Lại Toàn Bộ Internet Từ Ban Đầu "Ngu Si Mềm Dẻo" Lập Trình Được Như Một Cái Bảng Tính Điện Tử Phần Mềm Sống Mềm Viết Code Chứ Không Cần Sờ Cáp Cài Config Cli Dòng Lệnh Text Quá Lỗi Thời Cực Nhọc Tốn Thời Gian Đội IT Nghìn Người Giới Mạng Gánh.*

**Câu 197:** Vì Sao IP Lại Không Được Trang Bị Tính Năng Truyền Lại Cục Bộ Ở Tầng 3 Nối 2 Trạm Với Nhau (Hop-by-Hop Reliability)?
A. Do IP Đắt Quá Nên Cáp Viễn Thông Nối Nhau Mù Cho Nhanh.
B. Vì Sự Tin Cậy (Reliability) Nên Được Đẩy Lên Trên Tầng TCP (End-to-End). Nếu Router Giữa Đường Mà Cũng Tự Dừng Lại Hàng Giây Tính Toán Kiểm Lỗi Rót Mất Trả Về Thì "Bão Thời Gian RTT" Gấp Lên Tiền Tỷ Lần Phá Tan Việc Duy Trì Liên Tục Vượt Tuyến Lõi Của Cao Tốc Rộng Đáy Bể Bơi Rách Router Quá Tải Hút Cạn Không Giữ Góp RAM Bỏ Kẹt Nửa Bước 1 Bị Tắc Thẻ.
C. Sóng Đẩy IP Bị Phân Hủy Ngược Bằng Tia Laze Vệ Tinh Trái Tim Nhiễu Sóng Điện Áp Từ Khác Thường Không Có Thời Khắc Chuẩn Giai Điệu Khối 1400 Byte Cho Phù Hợp Hoàn Hảo Xứng Tầng Khung.
D. IPv6 Lên Ngôi Nên IPv4 Giữ Cho Bằng MAC Gốc Rập Sống.
*Đáp án: B*
*Giải thích: Tư Duy Tối Thượng Thiết Kế Xương Sống: Chạy Thật Nhanh, Không Quay Đầu Lại Nhìn 1 Mi-li-Mét Sự Việc Sửa Đổi Nào. Lỗi Để Đầu Nhận Tự Kêu Báo TCP Cứu. Mạng Ở Giữa Làm Cái Dây Rỗng Tuếch To Mượt Là Chóp Cấp Nhất Quán Lý Tưởng Cao Xa Mạng Kết Nối Ảo Chạy Trốn Trơn Vèo Trở Mặt Trái Trí Tuệ Cốt Lõi Tốc Độ Nhồi Ép Silicon Phần Cứng Nhào Nặn Ngay Sửa Check Ngăn Đọng Máy Hư Hỏng Chặn Ngừng Tắt Đóng Đường Chết Chóc Ảo IP Toàn Vẹn Đạt Không Lỗi.*

**Câu 198:** Khi Đọc "Mặt Nạ Mạng" (Subnet Mask) Bằng Chữ Số 255.255.255.192. Con Số "/?" Tương Đương CIDR Ngắn Gọn Sẽ Là Gì Toán Học Bấm Ngón Tay:
A. /28
B. /24
C. /26. Vì `255.255.255` = 24 Bit Chắc Chắn. Cục `.192` Cuối Cùng Ở Binary Bằng `11000000` (Thêm 2 Bit Đầu). Tổng Cộng Lấy 24 + 2 = 26 Bit Phần Mạng Phủ Khóa Chặn Trống (Phần Host Còn Thở Dài Chút Xíu 6 Bit Nghĩa Là Chứa Đc Max Khoảng 62 Khách Xài Trọ Kéo Trống Máy Trong Tầng Phòng Chia Lẻ Đơn Vị Tách Ngắn).
D. /30
*Đáp án: C*
*Giải thích: Toán Học Nhị Phân Lớp Mạng Trái Tim Kỹ Sư Thiết Kế Xây Cơ Quan Bàn Ghế Chống Giật Mạng Kéo Bừa Chơi Xài Ngập Dư Phí Hoang Tàn Địa Chỉ Tốn Tiền Tỷ Thẻ.*

**Câu 199:** Mô Hình Cấu Trúc Khép Kín "VRRP" Hoặc "HSRP" (Cổng Trực Phòng Hờ Dự Chữ) (Virtual Router Redundancy Protocol) Sinh Ra Để:
A. Router Có Sẵn Cổng Tắm Điện Nước Cao Tràn Thắt.
B. Cấp 2 Cục Router Tầng Nhất Mạng Nhưng Nối Cùng LAN Công Ty Để Nhận Diện MỘT (1) ĐỊA CHỈ IP ẢO GATEWAY DUY NHẤT. Nếu Một Con Router (Cắm Điện Tắt Nguồn) Cháy Tắt Bất Thình Lình. Cục Còn Lại Đứng Yên Bỗng Tự Khởi Chạy Sống Lên Thừa Kế Ngay Kéo Địa Chỉ IP Ảo Đó Về Mình Ẵm Trọn Trong Chớp Mắt Giúp Máy Trạm Lướt Web Thả Cửa Chẳng Cảm Thấy Khập Khựng Bứt Rứt Mạng Đứt Hoang Lạc Bóng Lăn Giây Đảo Hồi Quá Ảo Sống Đi Cùng Năm Tháng Cao Xa Chống Lạc Kháng Trễ Hoàn Toàn Tối Cao (High Availability Nhức Nối Lỗi Bỏ Qua Xử Bóc Giảm Chiều Sâu Ẩn Tích Hết Ảo Không).
C. Biến Mất Của Mạng Máy Nâng Cấp RAM OSPF Định Hình Oanh Liệt Giọng Gõ Sửa Tự Tháo Quạt Mát Lẻ.
D. Biến Trạm Vệ Tinh Sang Khúc Đồi Viễn Khơi Cao Tần Sóng Xung Rung IP Chạy TCP UDP Cũ Trừ.
*Đáp án: B*
*Giải thích: Doanh Nghiệp Không Thể Rớt 1 Cục Sắt Trọng Lõi Nối Biển Mất Hoàn Toàn Giao Dịch, Backup Chống Chịu Lỗi Bằng Con Tường Vách Ảo Móc Khớp MAC Bay IP Di Trú Vô Hình Góp Mặt Chở Che Xoay Trục Gãy Nhanh Lập Tức.*

**Câu 200:** Chốt Vấn Đề Hiểu Cơ Cấu Nền Trục IP Tầng 3 Của "Dịch Vụ Cố Gắng Hết Sức" Đáng Kính Giao Thức (Best-Effort IP Network) Là Gì Theo Sâu Thẳm Xa Lắc Của Công Trình Cha Đẻ Vinton Cerf Và Bob Kahn:
A. Hủy Toàn Mọi Hệ Điều Hành Tắt UDP Trừ Mã Xóa P2P Kẹt Ổ.
B. Internet CHỈ CẦN NÓI CHO CÁP ĐỒNG RÚT TIN CHẠY 1 MẠCH QUYẾT TỬ NHANH RẺ ĐƠN GIẢN RỘNG LỚN BỨC BÁCH. KHÔNG CẦN BẢO MẬT GẮN TRONG. KHÔNG CẦN CHUẨN XÁC HOÀN CHỈNH KÈM CHÈN KHÓA THEO THEO DÕI NỐI KẾT LIỀN THEO BẮT TRÓT ĐONG ĐIẾM CHẶT CHẼ HẾT CHẶNG Ở GIỮA ĐƯỜNG MẠCH... IP Giống Một Thùng Carton Gói Rỗng Mọi Đồ Lỗ Hỏng Chứa Bay Loạn Trôi Ngang Trôi Chéo Dòng Sông Mịt Mù Khắp Điểm Nhưng Là Chân Đế Rộng Hoàn Hảo Cho Việc Dựng Mọi Lâu Đài Sắt Thép Bảo Vệ TCP / HTTP Xa Hoa Tuyệt Mỹ Lớp Trên Dựa Nhờ Tồn Sống Kéo To Rực Rỡ Đầy Kiêu Hãnh Lan Dài Bức Nền Hạ Đáy Bển.
C. Nén Bức Xóa Vẻ Định Hình Khúc Bằng Số OSPF Nét Lưng Vô Hạn Không Có Độ Bằng Giá Hồi Chuyển IP Cột Cước.
D. Chia Thể Tần Sóng Quá Trớn Lấp Đày Xóa Tỏa Ngập Kín Giác Tắt MAC.
*Đáp án: B*
*Giải thích: Đỉnh Cao Nhất Triết Học Mạng (Philosophy of the Internet). Đơn Giản Dưới Thấp Mức Ngu Nhất Lõi Thô Nhanh Giảm Trí Càng Sống Lâu Sâu Da Cực Thịnh Phủ Ngập Ngàn Nơi Lấp Đáy. Mọi Sự Nặng Rườm Thông Tuệ Bọc Đè Gỡ Chắp Sửa Cắt Cứ Kéo Vứt Gán Áp Che Trên Chóp Máy Chủ Edge Đầu Đôi Chót Vót.*

**Câu 201:** Trong định tuyến BGP, thuộc tính (Attribute) nào là bắt buộc và vô cùng quan trọng để chống lặp vòng toàn cầu?
A. OSPF Router ID.
B. Weight (Trọng số).
C. AS-PATH (Danh sách các Hệ thống tự trị đã đi qua). Bất kỳ Router BGP nào khi nhận được bản tin quảng bá, nếu thấy mã AS của CHÍNH MÌNH đã nằm lù lù trong danh sách AS-PATH đó, nó SẼ VỨT NGAY TỨC KHẮC để không đâm đầu vào vòng luẩn quẩn.
D. IP Multicast.
*Đáp án: C*
*Giải thích: AS-PATH là cột sống của BGP. Một sợi dây liên kết mạch lạc chứng minh nguồn gốc xuất xứ của lộ trình.*

**Câu 202:** Khi sử dụng công cụ "Traceroute" trên Windows (hoặc Tracert), công cụ này thường dựa vào thông điệp ICMP nào của Router gửi về để vẽ bản đồ?
A. Destination Unreachable (Đích không thể tới).
B. Redirect (Chuyển hướng).
C. Time Exceeded (Quá hạn thời gian sống - TTL = 0). Mỗi lần gói tin dò đường đi chết yểu ở một trạm do hết TTL, trạm đó sẽ ném cái thẻ phạt ICMP này về, giúp máy gửi chép lại địa chỉ IP của trạm đó vào danh sách lộ trình.
D. Echo Request.
*Đáp án: C*
*Giải thích: Việc cố tình thả những con cờ bay có giới hạn độ cao (TTL tăng dần 1,2,3) để chúng rụng xuống ở từng cột mốc là cách thăm dò thông minh nhất của mạng.*

**Câu 203:** IPv6 Header có trường "Traffic Class" (Lớp lưu lượng - 8 bit) đóng vai trò tương tự như trường nào bên IPv4?
A. Header Checksum.
B. TOS (Type of Service - Differentiated Services Code Point). Dùng để gắn nhãn phân mức Ưu tiên (Ví dụ: QoS cho gói tin Voice/Video đi trước, gói Web rác xếp hàng sau).
C. Fragment Offset.
D. Version.
*Đáp án: B*
*Giải thích: Đổi tên gọi nhưng bản chất việc đánh dấu phân luồng băng thông vẫn được kế thừa hoàn hảo.*

**Câu 204:** Điểm hạn chế chí mạng của "Hub" ở tầng L1, dẫn đến việc Tầng Mạng (L3) bị liên đới sụt giảm tốc độ là gì?
A. Dùng cáp quang đắt đỏ.
B. Hub tạo ra một Broadcast Domain và một Collision Domain KẾT HỢP khổng lồ. Mọi gói tin IP/ARP bay qua nó đều phải chịu rủi ro Đụng độ dội ngược rác rưởi. Làm suy giảm 80% Băng thông khả dụng thực tế truyền tải.
C. Hub không chạy điện.
D. Không dùng được chuẩn IPv6.
*Đáp án: B*
*Giải thích: Sự thay thế Hub bằng Switch (L2) là cuộc đại tu cơ bản cứu rỗi Internet khỏi bờ vực tắc nghẽn vật lý những năm 90.*

**Câu 205:** "Static Routing" (Định tuyến tĩnh) ưu việt hơn Dynamic Routing (Định tuyến động) ở một khía cạnh ngách nào?
A. Tự đổi đường khi cáp đứt 5 giây.
B. Quét được MAC ảo.
C. Tính Bảo mật và Tiết kiệm Tài nguyên tuyệt đối. Không có việc các Router "Trò chuyện" (Gửi bản tin Broadcast cập nhật) làm rác băng thông LAN hay nguy cơ bị Hacker chèn Route giả. CPU Router không tốn 1% nào để tính toán thuật toán, vì mọi đường đi đã được Đóng Đinh do Quản trị viên gõ tay.
D. Phân bổ BGP.
*Đáp án: C*
*Giải thích: Trong mạng quá nhỏ hoặc nối thẳng ISP, gõ 1 lệnh Route tĩnh vừa an toàn vừa khỏe máy.*

**Câu 206:** Chức năng "Proxy ARP" có thể giúp máy trạm bị Lỗi gì vẫn ra được Internet?
A. Tắt Wi-Fi.
B. Máy trạm Cấu hình SAI Subnet Mask (Ví dụ tưởng IP 8.8.8.8 là chung mạng cục bộ LAN với nó) nên Máy Trạm Ngu Ngốc gào lên Broadcast hỏi MAC của 8.8.8.8. Router biên (có bật Proxy ARP) nghe thấy, thương tình ĐÓNG GIẢ LÀM 8.8.8.8, Gửi MAC của Router cho Máy trạm để Máy trạm ném gói tin vào mồm Router.
C. Hỏng RAM.
D. Cấm TCP.
*Đáp án: B*
*Giải thích: Một tính năng "Bảo mẫu" siêu hay của Cisco Router dùng để cứu vớt các máy tính cấu hình lỗi không biết đường Gateway.*

**Câu 207:** Dải IP "Multicast" của IPv4 trải dài từ địa chỉ nào đến địa chỉ nào (Lớp D cũ)?
A. 10.0.0.0 đến 10.255.255.255.
B. 192.168.x.x.
C. 224.0.0.0 đến 239.255.255.255. Đây là vùng đất cấm không được gán cho một cái máy tính cụ thể nào, mà dùng làm ĐỊA CHỈ NHÓM (Group Address) cho các dịch vụ Video IPTV, Routing OSPF/RIP nói chuyện chung với nhau.
D. 255.255.255.255 duy nhất.
*Đáp án: C*
*Giải thích: Mọi máy tính lắng nghe Multicast giống như gia nhập một Câu lạc bộ kín, chỉ cần mở tai nghe đúng tần số nhóm đó.*

**Câu 208:** Một bộ chuyển đổi NAT không chỉ giữ Nhiệm vụ Tầng Mạng, mà nó đóng vai trò "Man in the middle" hiền lành cho Tầng Giao vận (Transport) vì:
A. Tải phim nhanh.
B. Nó theo dõi (Track) và SỬA TRỰC TIẾP từng cái Cổng Port Nguồn/Đích của mọi TCP/UDP Segment đi xuyên qua bụng nó, và PHẢI TÍNH LẠI CẢ CHECKSUM TCP MỚI để máy tính kia không tưởng là gói rác. Công việc cực nhọc và lén lút.
C. Bỏ qua DHCP.
D. Xóa dữ liệu web ẩn.
*Đáp án: B*
*Giải thích: NAT bẻ gãy mọi quy tắc trong sạch của Lớp IP. Nó bẩn thỉu nhưng lại là phao cứu sinh của Internet hiện tại.*

**Câu 209:** Giao thức IGMP (Internet Group Management Protocol) liên kết chặt chẽ với chức năng nào của Tầng mạng?
A. Báo lỗi ping mạng.
B. Dò mật khẩu Wi-Fi.
C. Đăng ký tham gia Nhóm Đa hướng (Multicast). Máy tính của bạn dùng IGMP báo với Router gần nhất: "Em muốn nhận Luồng Video của Kênh VTV3 có IP Nhóm là 224.1.2.3". Router sẽ nhớ và kéo Luồng đó về tivi nhà bạn.
D. Truyền tải TCP chậm.
*Đáp án: C*
*Giải thích: IGMP là người kiểm duyệt sổ điểm danh. Nếu không có máy nào trong mạng đăng ký xem tivi, Router sẽ từ chối tải luồng tivi đó về cho tốn cáp mạng.*

**Câu 210:** Router OSPF (Link-State) xây dựng một cơ sở dữ liệu LSDB giống hệt nhau trên MỌI Router trong cùng 1 Area. Lợi ích là:
A. Tốn ít RAM.
B. Không cần dùng IP.
C. Bất kỳ Router nào cũng Nắm rõ Bản Đồ Mạng Tuyệt Đối của toàn khu vực, tự mình vẽ đường đi bằng thuật toán Dijkstra độc lập, DO ĐÓ KHÔNG THỂ BỊ LỪA DỐI bởi 1 thông tin định tuyến sai lệch lặp vòng như thuật toán Giao phó Niềm tin mù quáng (RIP).
D. Gửi thông tin không mã hóa.
*Đáp án: C*
*Giải thích: OSPF là sự Thấu hiểu Tường tận. Nắm bản đồ trong tay thì không thể bị lạc.*

**Câu 211:** Một trong những lợi thế bảo mật lớn nhất (By-design) của IPv6 khi được phát triển là:
A. Mã hóa MAC.
B. Yêu cầu tích hợp CỨNG (Bắt buộc) kiến trúc IPsec vào Mọi hệ thống IPv6. Khác với IPv4 (IPsec là gói cài thêm tuỳ chọn). Nhờ đó mọi giao tiếp IPv6 Đều Được hỗ trợ Mã hóa và Xác Thực Chống giả mạo Tận Rễ ở Tầng Mạng nếu kích hoạt.
C. Bỏ qua UDP.
D. Vô hiệu DNS độc hại.
*Đáp án: B*
*Giải thích: IPv6 không chỉ tăng số lượng IP. Nó mang khao khát xây dựng một Không gian Mạng sạch sẽ, không có giả mạo (Spoofing) bằng mã hóa từ trong lõi lõi mạng.*

**Câu 212:** "Network Slicing" (Cắt lát mạng) trong 5G Mobile Network ảnh hưởng gì đến Tầng Mạng?
A. Tắt sóng vô tuyến 5G đi ngủ.
B. Tách 1 cơ sở hạ tầng Mạng Vật lý Khổng lồ thành các Lát Cắt (Slices) Mạng Ảo Lô-gic Độc lập Hoàn Toàn (Chạy IP ảo, Định tuyến ảo riêng biệt). Tránh việc Luồng Video Tiktok xem mạng chậm chèn ép tranh giành Băng thông IP với Hệ thống Cấp cứu Y Tế Phẫu Thuật Từ Xa đòi hỏi trễ 1ms.
C. Đổi chuẩn Wi-Fi cũ lên cao.
D. Ngắt toàn bộ IPsec ngầm.
*Đáp án: B*
*Giải thích: Đây là sự Ảo Hóa Vĩ Đại. Chia chẻ đường truyền phục vụ đa mục đích.*

**Câu 213:** Trong Bảng BGP, thuộc tính "MED" (Multi-Exit Discriminator) dùng để:
A. Đánh dấu Router hỏng.
B. Khi hai Tổ Chức (AS 1 và AS 2) nối tay với nhau bằng nhiều sợi cáp ở nhiều Bang khác nhau. AS 1 dùng MED để "Nói khéo" với AS 2 rằng: "Hãy đẩy Traffic của bạn qua sợi cáp ở Bang California này nhé, sợi cáp ở Bang Texas yếu lắm tôi không thích". Một sự Gợi ý lịch sự cho Lối vào (Inbound traffic).
C. Tắt cổng quang.
D. Biến Router thành Switch.
*Đáp án: B*
*Giải thích: MED là một trong những thông số tinh vi nhất để Kỹ sư mạng điều khiển Giao thông Thương mại Quốc tế.*

**Câu 214:** Lỗi Mạng Nội Bộ (LAN) do Tội phạm (ARP Spoofing) gây ra sẽ Gây gián đoạn Mạng ra Internet như thế nào?
A. Tự sửa IP thành v6.
B. Kẻ gian "Bơm rác ARP" báo rằng "TÔI CHÍNH LÀ ĐỊA CHỈ IP CỦA ROUTER GATEWAY ĐÂY". Cả văn phòng mù lòa ném gói tin đi Mỹ vào máy tính của Hacker. Hacker không buồn chuyển tiếp mà Vứt Sạch. Mọi người đứt mạng dù Wi-Fi vẫn đầy sóng.
C. Cáp đồng bị nổ do chập điện.
D. Mất điện.
*Đáp án: B*
*Giải thích: Sóng đầy, Ping nội bộ sống, Nhưng Mù đường ra cổng (Gateway) là đặc trưng của vụ hack ARP. Cách trị là Dynamic ARP Inspection (DAI) trên Switch cao cấp.*

**Câu 215:** Sự Khác Biệt Giữa Địa Chỉ MAC Bị Gắn Cứng (Burned-in) So Với Khả Năng Giả Mạo MAC (MAC Spoofing) Bằng Phần Mềm Là Gì?
A. Không Thể Giả Mạo.
B. Phần Cứng Chứa Số Tĩnh. Nhưng Khi Khởi Động HĐH Lên (Windows/Linux), HĐH Mới Là Người Đóng Gói Khung Lớp 2. Nếu Admin Dùng Lệnh Chỉnh Trình Điều Khiển (Driver) Để Đè Một Dãy Chữ Số Lạ Làm MAC Source TRƯỚC Khi Phát Khung Ra Cáp, Card Mạng Vẫn Phục Tùng Mù Quáng Ném Ra Y Trang Chữ Ký Fake Đó Ra Ngoài Phố.
C. Sóng Không Gian Bị Tắc.
D. Hỏng Router.
*Đáp án: B*
*Giải thích: MAC là cố định ở Phần cứng, Nhưng Dữ liệu Frame L2 lại được Đắp Nặn ở Phần mềm RAM. Hacker sửa ở Phần Mềm.*

**Câu 216:** Cơ Chế BGP (Border Gateway Protocol) Lại Dùng TCP Để Chạy Truyền Tải Bảng Định Tuyến Giữa Các Router Vì:
A. Nó Nhanh Hơn.
B. Bảng BGP Của Internet Quá Cỡ (Hàng Triệu Dòng). BGP KHÔNG TỰ VIẾT LẠI CƠ CHẾ SỬA LỖI TRUYỀN LẠI VẤT VẢ NHƯ OSPF, Mà Nó "Ở Đậu" Lên Cổng TCP 179 Của Tầng Giao Vận. Để TCP Lo Hết Việc Đảm Bảo Chuyển 100MB Dữ Liệu Bảng Mà Không Mất Dòng IP Nào (Nếu Mất Chút Xíu Là Đứt Nối Nguyên Quốc Gia Lạc Trôi Định Tuyến Lỗi Bừa).
C. Không Có Giao Thức Nào Rảnh Bằng.
D. Chống Lại Virus Botnet Ping.
*Đáp án: B*
*Giải thích: Một Ví Dụ Rất Điển Hình Về Việc Giao Thức Lớp 3 Rất Thông Minh, Biết Lợi Dụng Ngược Sự Đảm Bảo Khổng Lồ Của Lớp 4 (TCP).*

**Câu 217:** Giao Thức "MPLS" Khi Nối 2 Mạng Có Bất Cập (Discontiguous Networks) Giải Quyết Việc Đọc Header Như Thế Nào Lẹ Nhất?
A. Đọc Đổi Lại IP Trăm Lần.
B. Tắt Màn Hình.
C. Kỹ Thuật "Label Swapping" Tráo Đổi Thẻ Nhãn Lớp 2.5 Ở Giữa. Kế Kịp Cạnh Lõi Lưới, Các Con Label Switch Router (LSR) CHỈ Tra Đúng Cột Nhãn "Số 15 Vào -> Số 30 Ra Đẩy Cổng 2". Tuyệt Đối Không Chạm Đến Lớp TCP IP Ẩn Bọc Kín Ở Bên Trong, Biến Thời Gian Định Tuyến Của Nó Ngang Với Việc Quẹt Mã Vạch Băng Chuyền Siêu Thị Rất Trơn Tru Rẻ Đồ Máy Phụ Mạch Thấp.
D. Nén Cáp Lớn.
*Đáp án: C*
*Giải thích: MPLS Định Hình Lại Kỷ Nguyên Băng Rộng Giữa Cáp Quang ISP Toàn Cầu, Loại Bỏ "Xử Lý Não Bộ Chậm Của IP".*

**Câu 218:** Tường Lửa Thế Hệ Mới Khác (Next-Gen Firewall - NGFW) Trộn Lẫn Tính Năng IP L3 Với IDS/IPS Tầng 7 Nhằm Mục Đích Gì?
A. Cho Gọn Chỗ Đặt Server.
B. Thay IP Bằng IPv6 Tự Dưỡng.
C. Có Thể Ngăn Chặn Các Mối Đe Dọa Ẩn Kín Mà Tường Lửa Truyền Thống IP L3 Bị "Mù" Mắt Do Gói Đóng HTTP SSL Không Thấy Cổng Dịch. Ngăn Đứng Nguy Cơ Xuyên Lủng Tràn Màng Lấy IP Thường Tố Tấn Công Sâu Lõi L7 Vỡ Máy Chủ Nhanh Mất Thẻ Chống Dính Mã Độc Hại Che Kín Tinh Xảo Lừa Cửa L4 Nét Nát Ngay Mép Rìa Firewall Chặng Mới Tốn Giữ Bảo Mật Tốt.
D. Nén IP Bị Chặn.
*Đáp án: C*
*Giải thích: Sự Hợp Nhất Chức Năng Bóp Gom Mọi Công Cụ Thành Đa Tầng Bức Tường Lưới Mềm Dẻo NGFW (Palo Alto, Fortinet).*

**Câu 219:** Hiện Tượng Đổi Vùng Sóng "Roaming" Wi-Fi Chuyển AP (Access Point) Ở Nhà Hàng, Nhưng IP Điện Thoại Bạn VẪN GIỮ NGUYÊN Không Phải Nạp Lại DHCP Giúp Tránh Bị Rớt Gọi Zalo Liên Tục, Làm Sao Được?
A. Do IP Động Đứng Im Không Tắt Phép.
B. Cả Quán Ăn Rộng Lớn Được Bố Trí MỘT MẠNG LƯỚI LAN LỚP L2 VẬT LÝ DUY NHẤT (Chung 1 Subnet Bự, Các Cục AP Nối Bằng Cáp Chung 1 Switch Chẳng Hạn). Cục Phát 1 Và Cục Phát 2 Giao Data Ở Lớp 2 Bằng Địa Chỉ MAC Tầng Dưới. Lớp IP Tầng 3 Bên Trên Chả Hệ Thấy Suy Chuyển Sai Khác Gì, Yên Ổn Hoạt Động Tiếp TCP Tải Zalo Đang Ẵm Sóng Vượt Khắp Phòng Méo Mó Mát Rẻ Rành Ràng Mượt Lỗ Kín Hồn Lối Tốt IP Rộng Tương Lập Liên Nét Cục Bộ Ranh Biên Không Nét Không Chịu Kéo Cáp Mới Lệ.
C. Zalo Tự Đổi Sóng Lệnh OSPF Dịch Tạm Tốc Cước Thẻ Xa Băm.
D. Vệ Tinh Thu Tự Sửa Đổi Dấu Chặn.
*Đáp án: B*
*Giải thích: Nếu Roaming MÀ XUYÊN QUA 2 SUBNET L3 KHÁC NHAU, Bắt Buộc Đứt Mạng Đóng Kịch IP DHCP Cấp IP Mới Ngắt Kết Nối Ngập Phim.*

**Câu 220:** Cốt Lõi Giá Trị Định Tuyến Mạng L3 Cho Việc Phát Hiện Sự Cố Đứt Ngầm Giữa 2 Router Vắng Lặng "Im Lìm" Không Cáp Không Rơi Là Nhờ Giao Thức Trao Đổi Gì Cực Rõ Giữ Sóng Xuyên Tuyến Cứ Mỗi 10s:
A. OSPF Có Các Bản Tin KEEPALIVE / HELLO PACKET Liên Tục Trò Chuyện Báo Sống Tĩnh Giờ Gió Đều Nhau Qua Mặt Mạng Nhận Biết Nhịp Tim Vắng Mất (Dead Interval Thường Trễ Bằng X3 Gấp 3 Hay X4) Thì Tuyên Cáo Mất Nước Phân Lẻ Ngay Định Trí Bỏ Hẳn Bảng Map Xóa Xẻ Vượt Chấn Sóng Nhớ Mạng Cũ Tìm Mới Cực Mịn Đi Thẳng Chớp Tránh Nén Ác Liệt Treo Ping Chết Báo Dữ Dội Chỗ Cáp Đục Khoét Ngầm Xóa Mạch Mò Rờ Cảm Mạch Vô Giác Im Câm Gãy.
B. Mã Lệnh Xóa Băng.
C. UDP Check Nhịp Thường Xuyên Lấp Bộ.
D. Vứt Thử Ping Mạng Giả.
*Đáp án: A*
*Giải thích: HELLO là Nhịp Đập Trái Tim Mạng Định Tuyến Động Tầng L3 Vạch Kế Hoạch Sống Còn Không Gãy Treo Mù Tối.*

**Câu 221:** Địa Chỉ IPv6 `fe80::1` Là Thuộc Loại Dải Nào?
A. Anycast Công Cọng BGP Rỗng.
B. Địa Chỉ Mạng Loopback Máy Tĩnh IP Chủ Hẹp Tự Đo Tự Check Kéo Nóng.
C. Địa Chỉ "Link-Local" Ảo Cục Bộ Tự Sinh Phụ Kiện Rẻ Tại Mỗi Cổng LAN Máy Tính Chỉ Để Xưng Hô Chào Nhau Quanh Hàng Xóm Chút Xíu Mạng Phòng Dẹp Mở Gateway Rót Lệnh Thêm Chút Đợi Router Khảo Mở IP Ngoài Rào Chạy Internet Khơi Sau Vút Trống Hoang Dài Tần Sóng Gốc Dựng Nhặt Thơ Dày Code DHCP Mất Giọng.
D. Tên Miền Gốc Của Google.
*Đáp án: C*
*Giải thích: Điểm Sáng Tạo Hạt Giống Gắn Liên IPv6 Từ Lúc Chào Đời Rất Linh Động Hoàn Thiện Sự Sống Còn Mạng Chập Chững Dù Lạc Vùng Cáp Biển Đứt Băng Vẫn Chạy Mạng Nội Làng Yên Vui Kẹt Nhịp Gắn Lô Đọng Tràn Cáp Xoắn Chéo Oan Nghiệt Gắn Chắc Cấp Nhuần Cứu Máy Phóng Dữ Gói Dòng Tự Động Phân Bố Sống Hấp Lan Màng Tinh Lệnh Kéo Đi Nhặt Ráp Cũ Mức 0.5 Tỉ Tự Phân Lắp Dọn Đi Mới.*

**Câu 222:** Một Tấn Công Bơm ARP Nhồi Độc Cửa Ngõ "Trạm Trung Gian MITM" Phá Mạng Wi-Fi Sẽ Bị Máy Nạn Nhân NGĂN CẢN Đánh Bật Chống Mất Trí Nhớ Rác Dữ Liệu Tầng L2 Mạng Nhờ Chặn Khóa Phủ Kín Biện Pháp Kỹ Thuật Này Do Trạm Switch Gánh Đỡ:
A. Cắm Cáp Quang Ngay Không Dùng Khí Dữ Liệu Sóng Bể Gầm Mất Giọng.
B. Bấm Mật Khẩu Khóa Kép Zalo Cho Router Trạm Kéo Chắn Đè UDP Cáp Bức Không.
C. Dynamic ARP Inspection (DAI) - Kiểm Tra Kép Xác Thực ARP Động Cài Trên Lớp Switch Chuyên Nghiệp Ở Văn Phòng Lớn Để So Khớp Gói Nhận Fake ARP Có Trùng Với Bảng Cấp Trộm IP Khống Bị Ép Giả Chó Đội Lốt MAC Cửa Router Ngăn Cổng Cứu Lẽ Đụng Nhau Thấy Mùi Khét Khép Chặn Cửa Rơi Gói Ngập Lụt Ăn Cắp Khóa Pass Nét Của Kẻ Giữa Rình Trộm Lấy Phiên Session Mã Cướp Phanh.
D. Khóa Máy Rút Nhảy Xoay DHCP Kéo OSPF.
*Đáp án: C*
*Giải thích: DAI Ngăn Thảm Họa Độc Mạng Mùi ARP Thối Sinh Ra Mạng Lan Trống Vắng Lời Trối Thâm Gói Bọc Mù Không Che Nhận Bẩn Đè Khóa Pass Ổ Khóa Của Dân Dò Mật Ngầm Trạm Giả 192.168.1.1 Trói Xác Đích Nháy Trốn Chặn IP Phạt Góc Khóa Dây Vững Vi Mạch Ngừa Lỗ Tổ Đứng Phía Ngầm Bọc Bảng.*

**Câu 223:** Quản Lý Giao Thức RIP Ngăn Việc Nhận Sai Đường Dài Hoặc Vòng Lặp Vô Định Lặp Gói "Đếm Đến Vô Cùng 16 Hop" Bằng Các Cơ Chế Bảo Hiểm Phân Phát Route Bổ Sung Ngắn Nào Hợp Lại Tối Ưu Lưới Trượt Lỗ Hỏng:
A. Dịch Ngôn Ngữ IP Qua Cổng USB Nhờ Dấu Chấm Hỏi Đuôi Khép Pass Chữa Vỡ Bằng MAC Kéo Dây.
B. Route Poisoning, Split Horizon, Hold-Down Timers... (Các Thủ Thuật Rào Chắn Không Cho Phép Một Trạm Đi Kể Ngược Lại Gói Tin Cũ Rích Xấu Xa Về Chính Đường Nó Vừa Nhận Ra Kéo Lỗi Lắp Bảng Ngốc Sai Hiệu Nhầm Sai Chiều Lặp Cho Thằng Láng Giềng Thưa Kiện Nhầm Gói Nguy Kịch Chạy Cạn Đứt Oanh Liệt Dây Sập Nhũn Mạch Héo Lấp Bóng Ngầm Báo Cáo Không Chắc Rắn Ổn Lên Tiếng Mở Tái Thiết Lập Kéo Động Năng Sai Nhầm Kẹt Tồn Kho Không Hở Oan Trái Gói Nứt Sóng Loa Trễ Ping Bắn Hoang Đồ Tối Đường Sập Tịt Khốn Cùng Tải Xa Bỏ Sóng Rớt Trở Tay Không).
C. Tắt Màn Hình RAM Máy Tải Game Nhấn Dính Phím Esc Mất Ngay Giữ.
D. Truyền Lên UDP Xóa Bóp.
*Đáp án: B*
*Giải thích: Bài Toán Xử Lý Khủng Hoảng Định Tuyến Distance-Vector Gây Kinh Sợ Nhất Ngành Viễn Thông (Split Horizon Là "Đừng Múa Rìu Qua Mắt Thợ", Không Được Dạy Cho Thằng Láng Giềng Cái Đường Đi Mà Chính Nó Vừa Chỉ Cho Mày Ngay Lúc Sáng Ngược Phạt Đi). Dẹp Ngăn Chặn Vòng Đua Chuột Lẩn Quẩn Định Dạng Thất Thường Chạm Ngõ Cuối Rất Ác Lũ Phá Mạng Xéo Toát Gỡ Dây Nghẽn Nháo Mạng Lan Rộng Rải Phủ Quét Phơi Lỗi Bắt Vết Ngăn Ác Diệt Cùng Chặn Lún Giữ Ánh Lên Dò Ngờ Bẻ Cong Vực Đường IP Cụt.*

**Câu 224:** "NAT Overload" Trở Thành Phương Thuốc Bóp Cứu Thế Giới Khỏi Sập Hết Lượng IPv4 Trong 3 Thập Kỷ Qua Đã Vi Phạm Nguyên Tắc Nào Tối Kỵ Sạch Sẽ Bị Xóa Bỏ Hoàn Toàn Xuyên Mạch End-To-End Ở Định Dạng TCP/IP?
A. Rút Mạng Không Cho Mở UDP Rời Ràng Thay Dòng Quét Chấm.
B. Mở Toàn Bộ MAC Lên Public Không Rào Giữ Kén Mật Hóa Bảo Tồn Quá Tức Mạng Wi-Fi Thủng Lỗ Của Tòa Tầng Máy Mốc Máy Rỗng Máy Bóp Trụ Trục Lưng Tắt Bật Tốc Máy Cháy 1 1 Lẩn Khuất Sâu Hư Nguồn Kéo Dây LAN Trôi Nút Trái Văng Chụp.
C. Gây Cắt Đứt Tương Tác Sạch Không Thể Từ Máy Ngoài Chủ Động Yêu Cầu Kết Nối Tự Vào Máy Bên Trong Giấu Mặt Sau NAT Nếu NAT Không Mở Xăm Thủ Lỗ Trước Hoặc Tạo Cơ Chế Port Forward Móc Ngoặc Cực Kì Chắp Vá Méo Mó Khủng Hoảng Các App Voice P2P Kẹt Ứ Giữa Khung Bóp Nhồi Nhẹt Giữa Chặng Mới Tồn Lên Tức Nhức Chóng Mặt Nhất Bị Vi Phạm Mạch Thẳng Tư Duy Rất Trơn Tru Hoàn Thiện Kế Hoạch 1 Chiều Bóp Chắn Cổ Cửa Tường Thành Sụp Xó Mạch Bầm Chặn Bít Ngõ Khép Khít Đâm Xuyên Lỗ Cổng Trong Giấu Nhẹm Cứng Nhắc Sửa Lớp.
D. Sửa Lại Tên Domain Tự Phát Chậm Băng Pass HTTP Thẳng Quanh.
*Đáp án: C*
*Giải thích: Lập Trình Viên Khóc Tiếng Mán Vì NAT. Bạn Viết 1 Trò Chơi Muốn Hai Thằng Khách Ở 2 Nước Kết Nối Đánh Nhau Trực Tiếp, Cả Hai Cùng Đều Kẹt Sau Đít NAT Của Modem Nhà Chúng Nó... Không Thể Nào Liên Lạc Bằng Cổng Trực Tiếp Nhau Dù Có Biết IP. Phải Đi Rẽ Lối Nhờ Cái Server Nằm Cố Định Mỹ Trích Điện Cầu Nối Chuyển Dữ Liệu Tốn Băng Thông Rề Rà Ping Cao Rất Ngộp Bứt Ách Kháng Cực Ngầm Không Cấp Cứu Nối Trực Lộ Cửa Khó Gánh Mất 1 Chạm Nhay Chớp Lướt Thả Ảo Bọt Bèo Lộ Kín Vút Trở Ngoại Vây.*

**Câu 225:** Khi IPv6 Bắt Máy Chủ Phải Bỏ Ngay Việc Phân Mảnh Dữ Liệu IP Cỡ Gói Bự Thường Ngày Của Phế Tích Chặt Chia Cáp Lắp Ráp Khó Khăn Dọc Đường... Biện Pháp Giao Tầng Lớp IP Path MTU Discovery Kéo TCP Xung Trận Giúp Việc Này Mịn Mượt Chống Rớt Lặng Mất Bằng Động Tác Đỡ Trục Trặc Bóp Gói Thế Nào Kì Ảo Tốt Nhất Nhanh Xử Gọn:
A. Tự Gửi ICMP Nhắc Mở File Tắt Dây OSPF Thay Pass Dữ Lực Oanh Cáp Ảo Kéo Lực Hết.
B. Router Khi Gặp Gói To Tắt Rẽ Đè Khúc Cáp Hẹp Giảm Phí Không Có Trách Nhiệm Phân Rã, LẬP TỨC THẢ ĐÁP TÓM BỤP GÓI ĐÓ VÀ BÁO GÓI ICMPV6 (PACKET TOO BIG) QUĂNG VỀ LẠI NGƯỜI GỬI: "CÁI LỖ NÀY CỠ 1400 B THÔI CHÚ EM ƠI MÀ CHÚ NÉM 1500 VÔ KẸT RỒI". Người Gửi Bị Nhắc Báo Lập Tức Dọn TCP Kéo MSS Giảm Gọn Khúc Vừa Vặn Đút Băng Phóng 1 Lèo Sạch Xuyên Lủng Không Đụng Trạm Cắt Chẻ Nào Bị Xé Áo Cản Gấp Lộ Nguy Quá Nhiệt Nút Trạm Vi Xử Chặn Đứng.
C. Mã Hóa IP Đuổi Bắt Mở Thư Mật Khớp 1 Tỷ MAC L2 Không Sửa Xóa Cân Mạng Y Hệt Lệnh Gõ Rác Truy Tốc Gắn Đuôi Header Biển Cát Trôi.
D. Nâng RTT Lên Mức Trễ Kéo IP Chết Phanh Bất Tỉnh Gãy Sóng Giữ Dây Vệ Tinh Kìm Phát Đuổi Cản Ngăn Lấy Lưng Hẹp Khít Nút Gài IPsec Rỗng Kín Vi Mạch.
*Đáp án: B*
*Giải thích: Vẻ Đẹp Của Kiến Trúc Thay Thế IPv6 Bỏ Lại Sự Nặng Nề Oằn Mình Của Vi Bộ Chip Chuyển Nhỏ Gói Khóc Hận Chẻ Lỗi Đè Lưng Máy Gửi Tư Duy Rỗng Làm Việc Tự Quản Bọc Dữ Gói Kích Cỡ Xuyên Phá Ống Nhỏ Chuẩn Cản Ngăn Hỏng Mịn Đuổi Cáp Bức Gập Chạy Xỏ Bóp Nhanh Lập Vừa Ngang Bằng Nét.*

**Câu 226:** Một Ứng Dụng Streaming "IPTV Truyền Hình Đa Hướng Cáp Quang Kéo Đến Từng Phòng Khách" Bắt Phải Phụ Thuộc Vào Giao Thức Liên Lạc Bầu Phân Tuyến Bọn Đầu Thu Của Khán Giả Xem Tivi Bật Chuyển Kênh Mới Sẽ Nhờ Đến Kẻ Quản Lý Đăng Ký Chuyển Kênh Dẫn Lối Thâu Luồng Data Tách Mạng IP Tới Hút Thẳng Tivi Nhà Này (Mà Không Hút Tràn Vô Nhà Kế Bên Không Bật Kênh Đó):
A. Giao Thức TCP HTTPS Mã Ảo Trượt Nét FTP Trữ Lỗi UDP Trục Rối Văng Mạng Gặp Vỡ Nén Giật Văng Code Rào Kín Hẻm Báo Đóng Bức Phá Phơi Bày Truy Xuất Máy Lẻ Trơn Giữa Router Dòng Ngăn Bọc MAC Che.
B. OSPF Routing Chạy Giao Giữa Mạng LAN Cá Nhân Với Phim 4K Đánh Ngập 1 Máy Đổi Luồng IP Gắn Mác Rỗng Vết Bị Gửi Hoang Cản Bóp.
C. Giao Thức IGMP (Internet Group Management Protocol) Mở Máy Bật Truyền: "Cho Khách Trạm Đăng Ký / Rút Bỏ Xem Luồng Kênh 224.2.2.2 Của Đám Đông Dịch Vụ Cáp Tivi". Báo Lên Cấp Cục Router Tầng Gần Phát Kéo Cáp Vuốt Thẳng Xuống Phủ Mạng Đánh Dấu Đầu Thu Khớp Nhóm Video Bưng Trả Mở Mắt Rút Dữ Vận Chuyển Multicast Thu Nhỏ Đậm Nét Mềm Rải Quét Vừa Nhịp Phim Chuẩn Lướt Nhóm Dành Cục Bộ LAN Mảnh Liệt Ngăn Phí Bão Kéo Tái Ngộp Kẹt Màn IP.
D. Kéo DNS Tra Tên Phim UDP.
*Đáp án: C*
*Giải thích: Router Chỉ Bơm Nước (Kênh VTV1) Xuống Cho Nhà Bạn NẾU CHÍNH XÁC Nó Thấy Đầu Thu Của Bạn Phát Lên Lời Xin Phép Đăng Ký (IGMP Join) Đòi Xem Kênh Đó, Tránh Gây Đổ Rác Mạng Vào Ngôi Nhà Sát Vách Không Bật Tivi Cùng Giây Phút Chống Cự Băng Cụt Rác Quảng Bá Chói.*

**Câu 227:** Khái Niệm Phân Khúc Băng Thông Bảo An QoS "Differentiated Services Code Point" (DSCP) Giấu Kín Cấu Hình 6 Bit Ở Lớp IP TOS Gắn Đánh Dấu Các Gói Xóa Trơn Độ Trễ Lớn Cuộc Điện Call: Chức Năng Này Do Bộ Nào Phải Thực Hiện Soi Cụ Thể Ưu Ái:
A. Tự Điện Thoại Tự Định Đường Dẫn Wi-Fi Ảo Sửa Code Kéo Đóng Nhịp UDP.
B. Chỉ Do ICMP Tự Chém Mã Nguồn Kéo Dây.
C. MỌI BỘ ĐỊNH TUYẾN ROUTER DỌC ĐƯỜNG Internet Phải Soi Cái Cờ Nhãn Gói DSCP. Nếu Gặp Mã Báo Khẩn "Voice Lớp 1" Thì Nó Vứt Các Gói Email Rác Khác Bắt Đứng Đợi Ở Bụng Hàng Đợi (Queue), Cho Ưu Tiên Thủng Lốp Gói Thoại Bốc Đầu Xếp Hàng Vọt Bắn Vượt Tuyến Lên Ra Ngay Cổng Tránh Khỏi Nhảy Jitter Phá Thoại Tiếng Gãy Nát Chữ Tiếng Chó Khóc Chết Trì Cản Giật Đổ Trống Băng Khí Bịt Trễ Âm Bứt Delay Kinh Điển Ngầm Nhồi Ngăn Nén Mịn Khít.
D. Đặt ARP Proxy Chạy IP Mạng Không Hút IPsec.
*Đáp án: C*
*Giải thích: Traffic Shaping (Xếp Hạng Phân Loại Đẳng Cấp Thượng Lưu / Dân Thường) Của Mọi Kiểu Router Mạng Doanh Nghiệp Cần Có Sự Chung Tay Ở Mặt Bằng Phần Cứng Ưu Tiên Ưu Đãi Gói Đặc Cấp Thời Gian Thực Giành Điểm Dành Riêng Rắn Lót Mượt Luồng Ống Rớt. QoS Bậc Thầy Trải Đều Lõi Dẫn Lỗ Vượt Khung Trạm Lệch Băng Thoại Quá Đẹp Ngắt Hình Nối.*

**Câu 228:** Công Nghệ "Carrier-Grade NAT" (CGNAT) Ứng Dụng Giữa Nền Lõ Mạng Thiết Kế Vĩ Đại ISP Có Đặc Tính Vét Cạn Nào Áp Chế Quyền Người Dùng Bán Mạng Nét IP Rẽ Trực Kín Tàn Lụi Bủa Cửa Tường Rác Lướt Sóng Chậm?
A. Mã Trạm Đóng Kín Vệt Phóng Tuyến Sóng Quá Lặng Phát TCP 40 Mảnh Hủy IP Xoáy Xé Cắt Biển Bắn Văng Không Cục NAT Cổng Phụ Ảo Thả Trống.
B. Mở Toàn Bộ Port LAN Phơi Mặt Rớt Nhịp Trạm Phát Máy Cháy Tự Kích Lấy Bỏ Sóng Hoang Cập Rải Điện Khắp Chỗ Bứt Vỏ Mở Đầu Kết Nối Kéo Dây Dẫn Ra Ngoài Mát.
C. NGƯỜI DÙNG Ở NHÀ KHÔNG CÒN ĐƯỢC CẤP MỘT CÁI IP PUBLIC TỰ DO ĐỘC LẬP NỮA Dù Đã Kéo Tường NAT Ở Gia Đình. HỌ BỊ NHỐT TIẾP VÀO 1 CÁI NAT KHỔNG LỒ THỨ 2 CỦA TỔNG ĐÀI NHÀ MẠNG VIỄN THÔNG (NAT LỒNG NAT ĐA TẦNG CẤP KÉP). Hàng Nghìn Căn Hộ Dùng Chung Chui Lại Qua Chỉ Vài Trăm Cái IP Public Của Tổng Đài, Phá Hủy Mất Dấu Sự Chạy Camera Camera Của Các Gia Đình Không Port Forward Đục Ra Nước Ngoài Gọi Về 1 Mạch IP. Thất Thủ IP.
D. Không Sửa MAC Băng Mạng. Trộn IPv4 Lên TCP Lệch Đẩy Gói Nát Thường Ứ.
*Đáp án: C*
*Giải thích: Đỉnh Của Đói Khát Cạn Kiệt Nguồn Lương Thực Của IP Nguồn Gốc. Việc Viettel VNPT Phải Dùng Khối Trạm Giấu Kính Khách Hàng (100.x.x.x CGNAT) Sau Bóng Tối Gây Ứ Đọng Tụt Đường Luồn Mở Game Khó Ping Màn Cấm Kết Nối Đội Game Đấu P2P Trục Xóa Nước Ngoài Bi Thảm Liên Lạc Bóp Méo Chống Ảo Giải Lỗi Bức Bối Báo Quãng Dài Sập Hút Kết IP Dàn Gói.*

**Câu 229:** Mô Phỏng Chức Năng Bơm Giao Ước Đường "VPN Site-to-Site" Giữa Hai Chỗ Vùng Công Ty (Công Ty Cha Và Công Ty Con Mỹ Và VN) Áp Tầng Mã Hóa IPsec Tunnel Bảo Đảm Đặt Trong Quỹ Đạo Đường Cáp Ngầm Công Cộng Lõ Tầng Nước Ngoài Hoạt Động Do Lõi Đầu Kéo Ẩn Danh Mạng Ngụy Nào Khởi Làm:
A. Từng Cặp Máy Lẻ Lẻ Trong Phòng Nhân Viên Chạy Phần Mềm Cấp IP Cho Nhanh.
B. Mã Hóa IPsec Tại Tường Lửa Tắt Ngay ARP Nhớ Địa MAC Ngôn BGP Sóng Rã Trạm Ngầm Dựng Sóng Bức Dấu Trạm Ảo Lắp Giấu Bóp Đẩy Nước Giữ IP Chạy Tách Nhập Ngu Ngốc Gỡ Tường OSPF Tầng Mạng Vặn Cước Nối Không Định Hình Tới Dễ Phục Khẩu Mạng Lụa UDP.
C. Bằng Cơ Chế Ở ĐÚNG 2 ĐẦU CỔNG TƯỜNG LỬA CHÍNH (Gateway Firewalls) Của 2 Vùng Công Ty Này Lên Cấu Hình Móc Sợi Cáp Mật Khấu Lưới Chặn Băng Cứng Cáp Đóng Vai Kẻ Vận Chuyển Bao Bọc IPsec Áo Khoác Dày Nhốt Cả Lũ IP Riêng Phía Sau Đi Cầu Thủng Lưới Internet Của Người Lạ Thấy Lỗ Giấu Đi Vào An Toàn Ra Cửa Lấy Ráp Ném Chỗ Bến Cũ Hoàn Diện Yên Bình Bảo Mật Cặp Rắn Nối Lõi Quanh Cáp Lở Dọc Ngoài Ngầm Toạt Thẳng Đâm Cứu Ngụy Lòng Mắt Trộm Bẻ Nén.
D. DNS Nhớ Dài Vệt Router Không Che Chống Phủ Bóng Che Hút TCP Tắt Lập Dải Mọi OSPF Đóng.
*Đáp án: C*
*Giải thích: VPN Điểm - Nối - Điểm Là Phép Giải Hoàn Hảo Cho Không Gian Riêng Nội Bộ Tồn Tại Ảo Diệu Song Song Trên Cùng Không Gian Public Công Cộng Sầm Uất Hỗn Độn Kẻ Nghe Lén Giăng Mạng Không Chạm Trích Cướp Bọn Quanh Internet Lõi (Bằng Sự Hy Sinh 2 Router Phía Cổng Mã Hóa Tối Lực Khủng Khiếp Trạm Tranh Hàng Động Chữ).*

**Câu 230:** Chốt Một Khái Niệm Quan Trọng Tột Đỉnh Giao Thức Mạng Thiết Kế Xương Tủy IP "Dumb Network - Cổ Thẳng Mạng Ngu, Thông Minh Đầu Cuối - Smart Edge" Phác Họa Đặc Thù Tốt Nhất Nào Giúp Mạng IP Phát Triển Bùng Nổ Chết Cắt Rễ Hoàn Toàn Bất Diệt Thế Giới Suốt Bán Kỷ Không Phai Bỏ:
A. Rằng Router Phải Khóa Chặt Tất Cả Wi-Fi Mật Mã Lọc Gói Nhận Virus Sửa Xóa Bắt Đề Diệt Thẳng Gói. Phải Thông Minh Đỉnh Giữ CPU Mã Cứng Không Gian Sửa Sai Đảo Cấp Lỗi Trống Giật Gói Tháo Dữ Dò Tìm Xong Sạch Đẩy Cắt Trơn TCP Cùng Pass MAC.
B. Router Mạng Lõi (Core Network) PHẢI CỰC KỲ NGU NGỐC, CHỈ BIẾT LÀM 1 CHỨC NĂNG DUY NHẤT LÀ ĐỌC IP ĐÍCH RỒI ĐÁ GÓI TIN ĐI CÀNG NHANH CÀNG TỐT (Không Hề Ghi Nhớ Của Ai, Không Cần Sửa Lỗi Giật Mất Phân Rã, Trống Cục Bộ Rỗng RAM Chống Chứa Bệnh Ghi Vết Chết Không Giữ Kết Nối Kéo Giữ Thời Gian). MỌI TRÍ THÔNG MINH, SỬA LỖI, BẢO MẬT TCP TLS ĐỀU ĐẨY HẾT VỀ PHẦN MỀM CHO LAPTOP SMARTPHONE Ở RÌA NGOÀI CÙNG TỰ XỬ LÝ NHAU. Mạng Ở Giữa Nhẹ Bệnh Rẻ Tiền Mới Xây Bọc Trùm Trái Đất Không Giới Hạn Cứu Sống Giá Trị.
C. Bắt Buộc Cáp Quang Không Bao Giờ Trễ Không Bao Giờ Mất Nén Không Đứt Gãy 1 Xíu Lật UDP Kẻ Định Hình Trượt Giao Bóp Cửa Rút Ống To Máy Trở Cực Ngốc Vỡ Tuyến Phép Xé Giọt Tốc Nhanh Kín Bó Lên Xé Bật Mạch Quá Trễ Bắt.
D. Biến Router Thành PC Bán Hàng Trữ Phim Bãi Điện UDP Khóa TCP Trữ Trễ TCP Mã Cứng Biển Không Trống Bức Đâm IPv6 Chạm Cáp Kẹp Router Che Khất Giữ Data.
*Đáp án: B*
*Giải thích: Đỉnh Cao Của Vẻ Đẹp Khoa Học. Lấy Sự Rỗng Tuếch Ở Tâm Mạng Điểm Yếu Biến Thành Sức Mạnh Đi Xuyên Phá Xây Dựng 1 Hạ Tầng Rẻ Trâu Lỳ Lợm Bao Dung Đủ Mọi Ứng Dụng Đỉnh Cấp Không Mất Sức Tiện Nghi.*

**Câu 231:** Trong giao thức OSPF, để tránh việc trao đổi thông tin định tuyến (LSA) quá tải khi có quá nhiều Router trong cùng một khu vực (Area), mạng OSPF chia các Router theo vai trò nào?
A. Router BGP và Router Tĩnh.
B. Chia thành Designated Router (DR - Router Chỉ định) và Backup Designated Router (BDR). Các Router khác chỉ cần gửi thông tin cập nhật cho DR và BDR thay vì gửi cho tất cả mọi người, giảm thiểu bão Broadcast trong mạng đa truy cập (như Ethernet).
C. Không chia vai trò.
D. Biến Router thành Switch.
*Đáp án: B*
*Giải thích: Nếu 10 người cùng nói chuyện với nhau, sẽ có 45 đường dây chéo (Công thức n*(n-1)/2). Nếu cử 1 lớp trưởng (DR) đứng giữa, 10 người chỉ cần nói với lớp trưởng (10 đường dây). DR sẽ thông báo lại cho cả lớp. Rất tiết kiệm băng thông.*

**Câu 232:** Lỗ hổng "IP Fragmentation Attack" (Tấn công phân mảnh IP) lợi dụng đặc điểm nào của quá trình lắp ráp (Reassembly) tại Hệ điều hành đích?
A. Router không đọc được IP đích.
B. Cáp mạng bị đứt ngầm.
C. Hacker tạo ra các mảnh vỡ IP (Fragments) có kích thước giả mạo, CỐ TÌNH ĐÈ CHỒNG LÊN NHAU (Overlapping offsets) hoặc thiết kế các mảnh không bao giờ hoàn chỉnh. Trình quản lý bộ nhớ của Máy đích khi cố gắng ghép lại sẽ bị kiệt quệ tài nguyên, tràn bộ đệm hoặc bỏ qua tường lửa do tường lửa không thấy được các Payload hoàn chỉnh ở Lớp 4 (TCP/UDP).
D. Đổi tên miền liên tục.
*Đáp án: C*
*Giải thích: Các Tường lửa đời cũ thường chờ nhận đủ mảnh mới đọc (tốn RAM) hoặc đọc mảnh 1 chứa Header TCP rồi thả các mảnh sau (bị lách luật).*

**Câu 233:** Một trong những lợi ích lớn nhất của IPv6 là tính năng "SLAAC" (Stateless Address Autoconfiguration). Chữ "Stateless" (Vô trạng thái) ở đây có nghĩa là gì?
A. Không dùng địa chỉ MAC.
B. Không có Máy Chủ Trung Tâm (như DHCP Server) nào LƯU TRỮ VÀ NHỚ TRẠNG THÁI (danh sách) IP nào đã cấp cho máy nào. Mọi máy tự sinh IP, tự hoạt động mà không bị phụ thuộc vào sự phân phối tĩnh cồng kềnh.
C. Đổi IP liên tục ngẫu nhiên.
D. Cấm TCP chạy trên đó.
*Đáp án: B*
*Giải thích: Đơn giản hóa việc vận hành mạng. Nó giúp quản lý Mạng IPv6 khổng lồ không cần các CSDL DHCP nặng nề lưu trữ log cho cả ngàn máy tính thay đổi.*

**Câu 234:** Một Dải Địa chỉ IP đặc biệt dùng cho "Tự kiểm tra mạng nội bộ" của chính máy tính (Loopback) trong IPv4 là gì?
A. 10.x.x.x
B. 192.168.x.x
C. 127.0.0.0/8 (Phổ biến nhất là 127.0.0.1). Gói tin gửi vào dải này sẽ quay đầu trở lại máy tính chứ không thoát ra Card mạng thật.
D. 255.255.255.255
*Đáp án: C*
*Giải thích: Gắn chặt vào Hệ điều hành, giúp Developer test Server Web ngay trên máy mình không tốn mạng LAN.*

**Câu 235:** Tại sao BGP Protocol (Định tuyến quốc tế) lại chọn TCP để truyền dữ liệu Cập nhật định tuyến thay vì tự viết giao thức UDP riêng như OSPF?
A. Vì BGP nghèo nàn code.
B. Vì CSDL Định tuyến toàn cầu BGP cực lớn (Triệu dòng chữ), việc chạy trên TCP giúp BGP "Miễn phí" tận dụng được khả năng tự chia nhỏ (Segmentation), tự truyền lại (Reliability) của TCP mà không phải thiết kế thuật toán chống mất gói phức tạp như các hệ thống IGP phải tự làm.
C. Vì BGP dùng HTTPS.
D. UDP cấm BGP.
*Đáp án: B*
*Giải thích: 1 bảng BGP cập nhật có thể băm thành vạn mảnh. Nếu không có TCP gom lại và sửa lỗi thì Router sẽ bị khập khiễng lộ trình thường xuyên do Mất tín hiệu ngẫu nhiên.*

**Câu 236:** Công nghệ định tuyến nào sau đây giúp "Chọc thủng" giới hạn của IPv4 để 1 mạng công ty có thể Xài Chồng Lên Nhau các dải mạng 10.0.0.0 nội bộ (mà không đụng vào IP Công cộng NAT) trên mạng Ảo?
A. Switch Port.
B. OSPF Area.
C. Virtual Routing and Forwarding (VRF - Định tuyến và chuyển tiếp ảo). Tạo ra các "Bảng định tuyến ảo" biệt lập trên một Router thật.
D. Dùng IPsec.
*Đáp án: C*
*Giải thích: VRF giống như 1 tòa nhà 10 tầng, mỗi tầng đều có Phòng số 1. Nhưng Phòng 1 Tầng 2 thì không nhầm với Phòng 1 Tầng 3 vì thuộc VRF Tầng khác nhau.*

**Câu 237:** Sự phân biệt rõ nhất giữa "Routing" và "Forwarding" là gì?
A. Không khác biệt.
B. Routing (Lập bản đồ/Tìm đường) diễn ra CHẬM, bằng CPU Phần Mềm, liên quan toàn mạng. Forwarding (Chuyển tiếp/Đẩy gói) diễn ra CỰC NHANH (Mili-giây), bằng Phần cứng Mạch in (ASIC) tại 1 Nút độc lập, chỉ Đọc Tra Bảng Ném ra cổng.
C. Forwarding đổi IP, Routing đổi MAC.
D. Cả 2 cùng dùng ARP.
*Đáp án: B*
*Giải thích: Nền tảng cốt lõi của SDN là đập vỡ 2 khái niệm này ra 2 cái máy vật lý khác nhau.*

**Câu 238:** Giao thức MPLS sử dụng "Nhãn" (Label) để chuyển mạch. Cái Nhãn 4 Byte này được chèn vào đâu trong gói tin?
A. Đính trước TCP.
B. Gắn vào Payload.
C. Nằm lơ lửng GIỮA Lớp 2 (Header MAC/Frame) và Lớp 3 (Header IP Datagram). Được coi là Lớp 2.5 (Shim Header).
D. Gắn vào cuối Trailer.
*Đáp án: C*
*Giải thích: Do nằm trước Lớp 3, con Chip xử lý không cần bóc lớp vỏ 3 ra đọc làm chậm việc, nó chỉ đọc Lớp 2.5 là đã biết hướng đi, đẩy nhanh gói tin lên tốc độ ánh sáng.*

**Câu 239:** Trong OSPF, "Link-State Advertisement" (LSA - Thông báo trạng thái liên kết) được các Router phát ra khi nào?
A. Khi Mạng gặp Lỗi (Ví dụ cáp đứt, thay đổi trạng thái Link), hoặc định kỳ sau một thời gian dài để đảm bảo bộ nhớ Đồ thị (Topology) của mọi người không bị lệch.
B. Mỗi 1 giây 1 lần liên tục.
C. Khi Ping rớt.
D. Chỉ phát 1 lần lúc bật máy.
*Đáp án: A*
*Giải thích: OSPF rất "im lặng" khi mạng ổn định. Nó không gào thét báo cáo toàn bộ bảng mỗi 30s như thuật toán RIP. LSA chỉ gửi các biến động (Delta changes), cực kỳ tiết kiệm băng thông.*

**Câu 240:** IP Subnet Mask `/23` ở dạng số thập phân được viết là:
A. 255.255.255.240
B. 255.255.255.0
C. 255.255.254.0 (Vì octet thứ ba là `11111110` nhị phân, tương đương 254).
D. 255.255.255.255
*Đáp án: C*
*Giải thích: /24 là 255. Lùi 1 bit xuống /23 là lấy 255 trừ đi 1 bit cuối ($2^0 = 1$) còn 254. Phép toán ngẩm nhanh chia mạng của Kỹ sư mạng.*

**Câu 241:** Kỹ thuật "Route Redistribution" (Tái phân phối Tuyến đường) trên Router biên mạng của Công ty dùng để làm gì?
A. Nén dữ liệu đi qua BGP.
B. Dịch và Đổ thông tin bảng định tuyến TỪ MỘT GIAO THỨC NÀY (VD: RIP chạy trong Phòng Kế toán) SANG GIAO THỨC KHÁC (VD: OSPF chạy ở Phòng Kỹ thuật). Giúp các mạng không đồng nhất ngôn ngữ nói chuyện được với nhau.
C. Cấp đổi MAC Address.
D. Đặt mật khẩu IP.
*Đáp án: B*
*Giải thích: Router biên làm "Phiên dịch viên". Lấy đường ngắn nhất của ông A, đổi hệ quy chiếu, báo cho ông B biết bằng ngôn ngữ của ông B.*

**Câu 242:** Ký hiệu "TTL" trong lệnh Ping trả về mang ý nghĩa dự đoán hệ điều hành như thế nào?
A. Đo được CPU mạnh hay yếu.
B. Các Hệ điều hành khác nhau CÓ MỨC TTL BẮT ĐẦU KHÁC NHAU. Windows thường dùng 128, Linux/Android là 64. Nếu bạn Ping thấy TTL=50, bạn đoán máy đích chạy Linux (bắt đầu từ 64 trừ đi 14 trạm Router dọc đường).
C. Không liên quan gì.
D. Lấy tốc độ mạng nhân đôi.
*Đáp án: B*
*Giải thích: Mẹo nhỏ của giới Hacker trinh sát mạng. Nhìn TTL đoán hệ điều hành đang dùng.*

**Câu 243:** Tại sao Mạng Lõi Internet (Core Network) luôn ưu tiên cấu trúc liên kết dạng Lưới Lớn (Full-Mesh / Partial Mesh) thay vì cấu trúc Hình Sao (Star)?
A. Đẹp mắt.
B. Để đảm bảo Tính Dự Phòng Cao Độ (High Redundancy / Fault Tolerance). Nếu một con Router Xương sống chết cháy, hay một tuyến Cáp quang biển bị cá mập cắn đứt, Lưới mạng LẬP TỨC tìm ra hàng chục lộ trình đường vòng khác để gói tin IP không bao giờ bị nghẽn ngưng hoàn toàn.
C. Tiết kiệm cáp.
D. Tránh Hacker vào cổng.
*Đáp án: B*
*Giải thích: Internet sinh ra dưới mục đích Quân sự (ARPANET) chống đứt gãy kết nối thông tin khi chiến tranh vũ khí nổ.*

**Câu 244:** BGP (Border Gateway Protocol) sử dụng Port TCP bao nhiêu để kết nối các Peer (Nhà mạng)?
A. 21
B. 80
C. 179. BGP không gửi Broadcast như OSPF, nó chạy kết nối TCP Unicast cứng trên Cổng 179 giữa 2 IP hàng xóm cụ thể đã được khai báo tay.
D. 443
*Đáp án: C*
*Giải thích: Nếu Tường lửa mạng lõi vô tình chặn Cổng TCP 179. Cả Quốc gia có thể bị đứt kết nối quốc tế vì mất Bảng định tuyến BGP.*

**Câu 245:** Địa chỉ IPv6 có cấu trúc Rất Thân Thiện Với Định Tuyến (Routing-Friendly) là do đâu?
A. Nó dùng mật khẩu Wi-Fi.
B. Nó không phân mảnh.
C. Phân bổ Bằng Cấu trúc Phân Cấp Khắt khe (Hierarchical Addressing). Gồm Prefix của Nhà Cung Cấp, Prefix Khu Vực, và Subnet Công Ty nối đuôi nhau. Giúp các Router Lõi Gom Mạng (Route Aggregation) Cực Kỳ Dễ Dàng Thành Đúng 1 Dòng, Thu Gọn Bảng FIB khổng lồ.
D. Dùng TCP.
*Đáp án: C*
*Giải thích: IPv4 băm nát bét hỗn loạn. IPv6 từ khi sinh ra đã được phân bổ quy củ địa lý, giống như mã bưu chính Zip Code rất gọn gàng cho việc Chuyển Thư.*

**Câu 246:** Kỹ thuật "NAT Hairpinning" (NAT Loopback) dùng để giải quyết Vấn Đề Oái Oăm nào của mạng LAN gia đình?
A. Lỗi rút nguồn.
B. Bạn ở ngoài quán Cafe gõ Web `camera.nhatoi.com` (IP Public của bạn) -> Camera lên hình. BẠN VỀ NHÀ, Ngồi Dùng Wi-Fi Ở Nhà, Gõ Lại Link Web Đó SẼ BỊ CHẶN LỖI (Vòng lặp ngược IP Public vào IP LAN). Tính năng NAT Loopback Trên Cục Router Giúp NẮN DÒNG GÓI TIN ĐÓ QUAY TRỞ VÀO LẠI PHÒNG LAN, để bạn vẫn xem được Camera nội bộ bằng Link ở Cả Ngoài Lẫn Trong Nhà.
C. Tắt cổng ICMP.
D. Sửa MAC.
*Đáp án: B*
*Giải thích: Tình trạng "Người trong nhà mượn cổng chính để vào lại cửa nhà" thường làm các Router cổ lúng túng Drop gói.*

**Câu 247:** Trong Tầng Mạng, IPSec (VPN) nếu được mã hóa (ESP), thì Thiết Bị Ở Giữa (Router/NAT) có thể đọc được Header TCP/UDP bên trong Gói không?
A. Đọc dễ dàng.
B. Hoàn toàn Không. Lớp ESP Của IPSec BỌC KHÓA HOÀN TOÀN từ Tầng 4 (Transport) trở Lên. Các Middlebox Chỉ Nhìn Thấy IP Header Dẫn Đường (Lớp 3) Bên Ngoài Cùng.
C. TCP chặn mã.
D. Đọc được do cáp sáng.
*Đáp án: B*
*Giải thích: Tuyệt Mật. Một con mắt ở giữa đường không thể biết bạn đang lướt Web TCP 80 hay xem Video UDP, hay nội dung gì trong đó. Tất cả chỉ là khối Dữ liệu mờ đục.*

**Câu 248:** Dải địa chỉ IP `0.0.0.0` được Máy Tính dùng với Vai Trò Nguồn (Source IP) Cụ Thể khi nào?
A. Khi Ping Google.
B. Khi Máy Tính Vừa Bật Nguồn, CHƯA ĐƯỢC CẤP MỘT IP NÀO. Nó Phải Lấy Tạm IP `0.0.0.0` (Của Không Ai Cả) Để Gửi Vào Gói Xin Cấp IP Broadcast (DHCP Discover). Đợi Mạng Cấp IP Xong Mới Có Danh Phận Rõ Ràng.
C. Khi Dùng Wi-Fi Tốc Độ Cao.
D. Bị Lỗi Mạng IPv6.
*Đáp án: B*
*Giải thích: `0.0.0.0` là "Sự Vô Danh". Cấm Tuyệt Đối dùng nó làm Đích (Destination).*

**Câu 249:** Giao thức "IGMP Snooping" Của Tầng L2 Switch Giúp Sửa Lỗi Ngốc Nghếch Nào Của Tầng Mạng IP Multicast?
A. Tắt Wi-Fi Rác.
B. Khi Multicast Về Tới Switch L2, Switch Thấy Cờ Đích Multicast Liền ĐỐI XỬ NHƯ BROADCAST (Bơm Nước Ra Cả 24 Cổng). Gây Nóng Cháy Tivi Người Khác Không Xem Kênh Đó. IGMP Snooping Là Việc Switch "Nghe Lén" Tin Nhắn Lớp 3 IGMP, Biết Chỉ Có Port 5 Xin Kênh Đó, Bơm ĐÚNG Luồng Nước Multicast XUỐNG CỔNG 5, Khóa 23 Cổng Kia Cứu Mạng LAN Khỏi Tràn Ngập Lụt Video.
C. Đổi MAC Bằng UDP.
D. Giảm Băng Thông ISP.
*Đáp án: B*
*Giải thích: Việc Tối Ưu Hóa Giao Thức Lai Giữa Lớp 2 Và Lớp 3. Switch Nhúng Tay Vô Lớp 3 Để Thông Minh Hơn Khác Thường.*

**Câu 250:** Đặc Tính "Store-and-Forward" (Lưu Và Chuyển Tiếp) Ở Router Mạng Ảnh Hưởng Rõ Rệt Nhất Lên Đặc Điểm Lưu Lượng Nào Của Gói IP?
A. Không Có Lỗi.
B. Nó Là Nguyên Nhân Sinh Ra "Trễ Truyền Dẫn Và Trễ Xử Lý" (Nodal Processing Delay). Gói Tin Lớn Sẽ Bắt Router Tốn Thời Gian Đọc, Chép Hết Toàn Bộ Vô RAM Xong Mới Cho Sút Đi Khỏi. Cộng Dồn Lại Qua 30 Trạm Router Sẽ Sinh Ra Trễ Ping Hàng Trăm Mili-Giây Trên Trái Đất.
C. Xóa Hết Lịch Sử Web.
D. Đổi Định Tuyến Sang OSPF Lỏng.
*Đáp án: B*
*Giải thích: Đây Là Giới Hạn Của Kỷ Nguyên Chuyển Mạch Gói Vốn Đã Chấp Nhận Để Đổi Lấy Khả Năng Ghép Kênh Tuyệt Vời Rẻ Tiền Mở Rộng Linh Hoạt Ngập Cáp Băng.*
