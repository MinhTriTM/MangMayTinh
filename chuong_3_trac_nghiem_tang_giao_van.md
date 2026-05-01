# CHƯƠNG 3: TRẮC NGHIỆM TẦNG GIAO VẬN (TRANSPORT LAYER)

**Câu 1:** Trong kiến trúc mạng TCP/IP, Tầng Giao vận (Transport Layer) có nhiệm vụ chính là gì?
A. Tìm đường đi ngắn nhất giữa hai router.
B. Cung cấp liên kết truyền thông logic trực tiếp giữa các TIẾN TRÌNH ỨNG DỤNG (Process-to-Process) chạy trên các máy khác nhau.
C. Mã hóa tín hiệu nhị phân thành sóng ánh sáng.
D. Sửa lỗi vật lý của cáp đồng.
*Đáp án: B*
*Giải thích: Nếu Tầng Mạng cung cấp giao tiếp Host-to-Host (nhà với nhà), thì Tầng Giao vận đi sâu hơn, chuyển thư tới tận tay từng người trong nhà (Process).*

**Câu 2:** Thuật ngữ "Multiplexing" (Ghép kênh) tại máy phát (Sender) ở Tầng Giao vận có nghĩa là gì?
A. Giải nén dữ liệu video trước khi phát.
B. Lấy các gói tin từ tầng Mạng, kiểm tra lỗi và đẩy lên đúng socket của phần mềm.
C. Thu thập các thông điệp từ nhiều Socket khác nhau, bọc chúng bằng Transport Header (để đánh dấu Port) rồi tạo thành các Segment đẩy xuống tầng mạng.
D. Tăng gấp đôi tốc độ đồng hồ của máy tính.
*Đáp án: C*
*Giải thích: Gom nhiều luồng dữ liệu từ các ứng dụng khác nhau thành một luồng xuống cáp mạng là quá trình ghép kênh.*

**Câu 3:** Giao thức nào ở Tầng Giao vận cung cấp dịch vụ Truyền dữ liệu KHÔNG ĐÁNG TIN CẬY (Unreliable) và PHI KẾT NỐI (Connectionless)?
A. HTTP
B. TCP
C. ICMP
D. UDP
*Đáp án: D*
*Giải thích: UDP gửi dữ liệu mà không cần thiết lập kết nối trước, không bận tâm dữ liệu có tới nơi hay có bị lỗi hay không.*

**Câu 4:** Socket của kết nối UDP được định danh bởi bao nhiêu tham số?
A. 2 tham số: Địa chỉ IP đích và Số hiệu cổng đích.
B. 4 tham số: IP nguồn, Cổng nguồn, IP đích, Cổng đích.
C. 1 tham số: Cổng đích.
D. 6 tham số.
*Đáp án: A*
*Giải thích: Do tính phi kết nối, hệ điều hành chỉ dùng 2 tuple (IP Đích, Port Đích) để nhét chung mọi thông điệp UDP vào cùng 1 socket.*

**Câu 5:** Máy chủ Web (Apache/Nginx) sử dụng TCP. Khi có 100 máy khách (Client) cùng kết nối đến Port 80 của máy chủ này, điều gì sẽ xảy ra ở tầng Giao vận của Server?
A. Server chỉ tạo 1 Socket TCP duy nhất để nhận 100 kết nối.
B. Xảy ra xung đột mạng do trùng Port.
C. Server sẽ sinh ra 100 Socket TCP khác nhau, mỗi Socket quản lý một phiên làm việc độc lập vì TCP dùng cơ chế 4-tuple (IP nguồn, Port nguồn, IP đích, Port đích) để phân kênh.
D. Server chuyển 99 kết nối sang UDP.
*Đáp án: C*
*Giải thích: Sức mạnh của TCP demultiplexing. IP nguồn và Cổng nguồn của mỗi client là khác nhau nên tạo ra bộ tứ (4-tuple) khác nhau.*

**Câu 6:** Trong UDP Header (dài 8 byte), trường Checksum có mục đích gì?
A. Đếm số lượng gói tin bị mất trên mạng.
B. Kiểm tra xem các bit trong đoạn tin (Segment) có bị lỗi (lật bit) do nhiễu vật lý trên đường truyền hay không.
C. Mã hóa mật khẩu người dùng.
D. Giới hạn băng thông của ứng dụng.
*Đáp án: B*
*Giải thích: Checksum sử dụng bù 1 để bắt lỗi. Mặc dù UDP không đảm bảo tin cậy, nó vẫn check lỗi cơ bản, nếu lỗi nó sẽ vứt gói tin đó đi.*

**Câu 7:** Để xây dựng một Giao thức truyền tin cậy (RDT) trên một đường truyền hay mất gói, phía gửi (Sender) BẮT BUỘC phải dùng công cụ nào để tự động gửi lại gói bị mất?
A. Bộ đếm thời gian (Timeout Timer).
B. Tín hiệu CTS/RTS.
C. Hàm băm SHA-256.
D. Bộ định tuyến không dây.
*Đáp án: A*
*Giải thích: Khi ném gói tin vào "hố đen" mạng mà không thấy ACK báo về, Sender sẽ bị kẹt mãi mãi nếu không có đồng hồ Timer để kích hoạt truyền lại.*

**Câu 8:** Số thứ tự (Sequence Number) được sinh ra để khắc phục vấn đề gì của đường truyền mạng?
A. Tăng kích thước bộ đệm.
B. Giúp bộ định tuyến chạy nhanh hơn.
C. Giúp phía nhận (Receiver) phân biệt được một gói tin gửi đến là dữ liệu MỚI hay chỉ là Bản sao gửi lặp lại (Duplicate) do phía gửi bị Timeout.
D. Giúp phân mảnh gói tin IP.
*Đáp án: C*
*Giải thích: ACK của Receiver có thể bị mất trên đường về. Sender tưởng mất gói nên gửi lại. Receiver phải xem số thứ tự để biết "À gói này mình nhận rồi, vứt đi, gửi lại cái ACK".*

**Câu 9:** Kỹ thuật Pipelining (Đường ống) trong truyền dữ liệu mạng có nghĩa là gì?
A. Nén dữ liệu xuống mức thấp nhất.
B. Nối nhiều đoạn cáp với nhau.
C. Phía gửi được phép gửi nhiều gói tin liên tiếp vào đường truyền mà KHÔNG CẦN phải chờ nhận được ACK của gói tin trước đó.
D. Chỉ cho phép gửi từng byte một.
*Đáp án: C*
*Giải thích: Trái ngược với Stop-and-wait, Pipelining giúp liên kết truyền dẫn luôn "đầy ắp" dữ liệu, tăng hiệu suất tận dụng băng thông (Utilization).*

**Câu 10:** Giao thức Go-Back-N (GBN) quản lý các báo nhận (ACK) theo cơ chế nào?
A. Báo nhận độc lập từng gói (Individual ACK).
B. Không sử dụng báo nhận.
C. Báo nhận lũy kế (Cumulative ACK) - Khi gửi ACK(n), có nghĩa là đã nhận thành công TẤT CẢ các gói từ n trở xuống.
D. Gửi ACK chung cho cả file.
*Đáp án: C*
*Giải thích: GBN có tính chất dồn cục. Nếu mất gói số 3, nhận được gói 4, 5, 6, nó sẽ bỏ qua và chỉ gào thét ACK(2) (Tới gói 2 là hết rồi). Timeout, gửi lại cả chùm từ 3.*

**Câu 11:** Khác biệt giữa Selective Repeat (SR) và Go-Back-N (GBN) khi xảy ra mất một gói tin là gì?
A. GBN gửi lại tất cả từ gói bị lỗi trở về sau; SR chỉ gửi lại ĐÚNG DUY NHẤT gói tin bị lỗi đó.
B. GBN gửi qua TCP, SR gửi qua UDP.
C. SR không dùng Timer.
D. SR không dùng bộ đệm ở máy nhận.
*Đáp án: A*
*Giải thích: Tên gọi "Phát lại có chọn lọc" (Selective Repeat) nói lên tất cả. Đổi lại, máy nhận phải có bộ đệm phức tạp để giữ các gói "vượt rào" chờ gói bị rớt tới.*

**Câu 12:** Trong TCP, quá trình thiết lập kết nối (3-way handshake) gồm các bước nào?
A. SYN -> SYN/ACK -> ACK
B. FIN -> ACK -> FIN -> ACK
C. RTS -> CTS -> DATA
D. GET -> POST -> OK
*Đáp án: A*
*Giải thích: Máy khách gửi SYN. Máy chủ đáp bằng SYN/ACK. Máy khách xác nhận lại bằng ACK. Hoàn tất quá trình tạo đường ống 2 chiều.*

**Câu 13:** Trường Acknowledgment Number (Số báo nhận) trong header của một TCP Segment từ máy B gửi cho máy A có giá trị là 1000. Nó mang thông điệp gì?
A. B đã gửi cho A 1000 byte.
B. B vừa nhận được byte số 1000 từ A.
C. B mong chờ nhận được byte tiếp theo từ A có số thứ tự (Sequence Number) bắt đầu từ 1000.
D. Kích thước cửa sổ của B là 1000 byte.
*Đáp án: C*
*Giải thích: TCP sử dụng số ACK lũy kế dự kiến. ACK=1000 ngầm hiểu "Tôi đã ôm trọn đến byte 999. Hãy ném cho tôi cục data bắt đầu bằng byte 1000".*

**Câu 14:** Sự kiện "Truyền lại nhanh" (Fast Retransmit) của TCP xảy ra khi nào?
A. Khi TCP đếm ngược Timer về 0.
B. Khi bộ đệm máy nhận báo đầy.
C. Khi phía gửi nhận được 3 gói ACK lặp lại (3 Duplicate ACKs) của cùng một số liệu.
D. Khi kết nối Wi-Fi bị yếu.
*Đáp án: C*
*Giải thích: Thay vì mỏi mòn chờ Timeout, nếu thấy Receiver liên tục hét "Gửi tôi gói 100" tới 3 lần, Sender tự hiểu gói 100 đã bốc hơi và truyền lại ngay.*

**Câu 15:** Kiểm soát luồng (Flow Control) trong TCP được sinh ra để bảo vệ đối tượng nào?
A. Bảo vệ cáp quang dưới biển.
B. Bảo vệ toàn bộ mạng lưới Router khỏi bị quá tải.
C. Bảo vệ Máy nhận (Receiver) khỏi việc bị tràn bộ đệm do Máy gửi bơm dữ liệu quá nhanh.
D. Bảo vệ Máy gửi khỏi bị nóng CPU.
*Đáp án: C*
*Giải thích: Cứ mỗi gói ACK, Receiver sẽ đính kèm thông số Receive Window (rwnd) báo cho Sender biết "Tao chỉ còn trống 5MB RAM thôi nhé, liệu mà gửi".*

**Câu 16:** Kiểm soát tắc nghẽn (Congestion Control) bảo vệ ai?
A. Bảo vệ Máy gửi.
B. Bảo vệ Máy nhận.
C. Bảo vệ sự ổn định của TOÀN MẠNG INTERNET bằng cách điều tiết lượng truy cập bơm vào hệ thống để các Router không bị sập.
D. Chống lại Hacker.
*Đáp án: C*
*Giải thích: Khác Flow control (1 đấu 1), Congestion control là trách nhiệm xã hội. Nếu mạng bị kẹt (thấy qua việc rớt gói tin), mọi TCP phải đồng loạt giảm ga.*

**Câu 17:** Pha Khởi động chậm (Slow Start) của thuật toán TCP Congestion Control tăng kích thước cửa sổ tắc nghẽn (cwnd) theo hình thức nào?
A. Tăng tuyến tính (Cộng thêm 1 mỗi lần).
B. Tăng theo cấp số nhân (Nhân đôi sau mỗi RTT) cho đến khi gặp ngưỡng ssthresh hoặc xảy ra mất gói.
C. Không tăng, giữ nguyên 1 MSS.
D. Tăng ngẫu nhiên.
*Đáp án: B*
*Giải thích: Cái tên "Chậm" chỉ đúng ở vạch xuất phát (cwnd=1). Nhưng nó tăng trưởng theo hàm mũ ($2^n$) nên thực chất vận tốc bứt tốc cực kỳ gắt.*

**Câu 18:** Khi TCP nhận thấy có mất gói do Timeout, nó phạt biến cwnd như thế nào?
A. Chỉ giảm đi một nửa.
B. Giảm đi 10%.
C. Hạ ssthresh xuống một nửa, và bóp nghẹt cwnd về vạch xuất phát 1 MSS (Quay lại Slow Start).
D. Không làm gì cả.
*Đáp án: C*
*Giải thích: Timeout là báo hiệu một vụ tắc đường thảm khốc, chả có gói nào về được. TCP bóp phanh lút cán về 1 MSS.*

**Câu 19:** Hành vi đồ thị của TCP Congestion Control được gọi là AIMD (Additive Increase, Multiplicative Decrease). Điều này tạo ra hình dạng đồ thị gì cho Thông lượng (Throughput)?
A. Đường thẳng đi lên mãi mãi.
B. Hình răng cưa (Saw-tooth).
C. Hình Sin tròn.
D. Đường cong parabol.
*Đáp án: B*
*Giải thích: TCP từ từ tăng ga (Tuyến tính - Additive), đến lúc đụng trần gây mất gói, nó bóp phanh cắt nửa (Multiplicative), rồi lại rà ga lên từ từ. Đồ thị y như cái răng cưa.*

**Câu 20:** Nếu máy A gửi cho máy B một Segment chứa 100 bytes dữ liệu, có Sequence Number = 300. Dữ liệu đến an toàn. Vậy máy B sẽ gửi gói ACK có số hiệu là bao nhiêu?
A. 300
B. 100
C. 400
D. 401
*Đáp án: C*
*Giải thích: Segment A mang các byte từ 300 đến 399. Byte tiếp theo mà B cần là 400. Do đó Acknowledgment Number = 400.*

**Câu 21:** Cơ chế thiết lập kết nối của TCP rất dễ bị lợi dụng để thực hiện cuộc tấn công Từ chối dịch vụ (DoS) kiểu nào sau đây?
A. UDP Flooding
B. SYN Flooding
C. Ping of Death
D. MAC Spoofing
*Đáp án: B*
*Giải thích: Hacker gửi hàng vạn gói SYN nhưng dùng IP giả. Máy chủ trả lời SYN-ACK và cấp phát sẵn tài nguyên (buffer/RAM) để chờ ACK cuối cùng. Khách không bao giờ gửi ACK, làm máy chủ cạn kiệt bộ nhớ.*

**Câu 22:** Giai đoạn "Tránh tắc nghẽn" (Congestion Avoidance) của TCP hoạt động như thế nào?
A. Tăng kích thước cửa sổ cwnd lên gấp đôi sau mỗi RTT.
B. Tăng kích thước cwnd một cách tuyến tính, thêm 1 MSS cho mỗi RTT trôi qua.
C. Giảm cửa sổ cwnd đi 1 MSS mỗi khi nhận được ACK.
D. Khóa chặn ứng dụng để không cho tải thêm dữ liệu.
*Đáp án: B*
*Giải thích: Sau khi cwnd vượt qua ngưỡng ssthresh (Slow Start Threshold), TCP chuyển từ tăng mũ sang tăng tuyến tính rà dậm chân để thăm dò giới hạn cuối cùng.*

**Câu 23:** Quá trình giải phóng kết nối (Ngắt kết nối) của TCP diễn ra như thế nào?
A. Gửi 1 gói tin EXIT và ngắt ngay lập tức.
B. Diễn ra theo quy trình 4 bước (4-way handshake) trao đổi cờ FIN và ACK. Cả hai phía đều phải báo gửi FIN để chấm dứt phiên truyền dữ liệu.
C. Máy chủ cắt điện mạng.
D. Rút dây mạng.
*Đáp án: B*
*Giải thích: Kết nối TCP là Full-duplex (2 chiều). A gửi FIN để báo A xong rồi. Nhưng B vẫn có thể tiếp tục gửi nốt dữ liệu cho A cho đến khi B cũng gửi FIN.*

**Câu 24:** Biến cwnd (Congestion Window) và rwnd (Receive Window) có mối liên hệ như thế nào trong việc quyết định lượng dữ liệu tối đa (Unacknowledged data) mà Máy gửi được phép bơm ra mạng?
A. Dữ liệu tối đa = cwnd + rwnd.
B. Dữ liệu tối đa = Min (cwnd, rwnd).
C. Dữ liệu tối đa = Max (cwnd, rwnd).
D. Dữ liệu tối đa = rwnd / cwnd.
*Đáp án: B*
*Giải thích: TCP phải tuân thủ nghiêm ngặt theo kẻ yếu nhất. Nếu mạng báo chỉ cho đi 10MB (cwnd), nhưng máy nhận báo RAM chỉ còn 2MB (rwnd), thì Máy gửi chỉ được xuất xưởng 2MB.*

**Câu 25:** Ưu điểm của kiến trúc UDP so với TCP là gì?
A. Đảm bảo dữ liệu đến đúng thứ tự.
B. Kích thước Header nhỏ bé (8 byte) giúp tiết kiệm băng thông và không mất thời gian thiết lập kết nối (RTT ban đầu = 0).
C. Có chức năng mã hóa dữ liệu mặc định.
D. Chống lại cuộc tấn công DDoS.
*Đáp án: B*
*Giải thích: Sự gọn nhẹ của UDP là lý tưởng cho các luồng dữ liệu liên tục như video streaming hoặc truy vấn DNS siêu tốc.*

**Câu 26:** Trong giao thức TCP, để tính toán thời gian Timeout (Hẹn giờ hết hạn), máy tính phải dựa trên thông số nào?
A. Tốc độ quay của quạt tản nhiệt.
B. Thời gian RTT (Round Trip Time) đo lường được trên mạng (EstimatedRTT) cộng với sai số biên độ biến thiên (DevRTT).
C. Khoảng cách địa lý bằng km đo bằng GPS.
D. Dung lượng RAM của thiết bị.
*Đáp án: B*
*Giải thích: Mạng có lúc nhanh lúc chậm, TCP không thể set cứng Timeout = 1 giây. Nó liên tục đo RTT để tính ra Timeout Interval tối ưu, đảm bảo không bắt chờ quá lâu cũng không quá vội vã.*

**Câu 27:** Một ứng dụng tải phim từ Server qua HTTP (dùng TCP). Đột nhiên có một người tải file cực kỳ lớn qua đường liên kết bên cạnh dùng UDP khiến tắc nghẽn cục bộ. Điều gì sẽ xảy ra?
A. TCP sẽ tự động nâng băng thông lên để đè UDP.
B. Kênh TCP sẽ ngoan ngoãn tự bóp băng thông (giảm cwnd) do có rơi vãi gói tin, trong khi UDP vẫn xả láng với tốc độ ứng dụng. Kết quả UDP sẽ bóp nghẹt TCP.
C. UDP tự động nhường đường cho TCP.
D. Cả hai cùng bị rớt mạng hoàn toàn.
*Đáp án: B*
*Giải thích: Đây là một vấn đề bất công (fairness) nổi tiếng. UDP không có cơ chế Congestion Control, nó giống xe biển xanh ưu tiên, cứ thế lao vào điểm nghẽn, ép các ứng dụng TCP phải tự phanh lại.*

**Câu 28:** Giao thức nào hoạt động ở cả Mạng máy tính có dây và Mạng di động không dây (4G/Wi-Fi)?
A. CSMA/CD
B. ARP
C. TCP và UDP
D. OSPF
*Đáp án: C*
*Giải thích: TCP và UDP chạy ở tầng Transport (cấp ứng dụng), chúng không hề quan tâm thiết bị dưới dây cáp là đồng, quang hay vô tuyến.*

**Câu 29:** Để một máy khách biết được một cổng (Port) của máy chủ có đang sẵn sàng phục vụ dịch vụ hay không, thao tác kỹ thuật thường dùng là gì?
A. Ping IP
B. Port Scanning (Quét cổng)
C. Phân giải DNS
D. Gửi gói ICMP
*Đáp án: B*
*Giải thích: Hacker hoặc quản trị viên dùng nmap (Port scanner) gửi các gói SYN tới từng port từ 1 đến 65535. Nếu Port nào có trả về SYN-ACK nghĩa là cửa đó đang mở.*

**Câu 30:** Trạng thái TIME_WAIT cuối quá trình ngắt kết nối TCP của máy chủ chủ động ngắt có ý nghĩa gì?
A. Chờ người dùng thanh toán tiền mạng.
B. Bắt máy chủ nhận nốt dữ liệu còn thiếu.
C. Đợi 1 khoảng thời gian (thường là 2 lần MSL) để đảm bảo các gói tin cũ bị lạc (delayed segments) có thời gian bốc hơi khỏi mạng hoàn toàn, tránh ảnh hưởng tới phiên làm việc mới nếu xài lại port đó.
D. Cập nhật bảng định tuyến nội bộ.
*Đáp án: C*
*Giải thích: Trên Internet hay có những gói tin bị kẹt trong router 1 thời gian dài rồi mới tới. TIME_WAIT giúp cái ống nước thật sự sạch sẽ trước khi đóng cửa.*

**Câu 31:** Chức năng cơ bản nhất mà MỌI giao thức Tầng giao vận (như UDP và TCP) đều MẶC ĐỊNH phải cung cấp cho hệ thống là gì?
A. Kiểm soát tắc nghẽn mạng lõi.
B. Truyền tải tin cậy 100%.
C. Ghép kênh (Multiplexing) và Phân kênh (Demultiplexing) dữ liệu dựa trên số hiệu Cổng (Port number).
D. Định tuyến gói tin qua các quốc gia.
*Đáp án: C*
*Giải thích: IP chỉ mang gói tin tới đúng Máy tính (Host). Tầng giao vận dùng Port để phân kênh, đẩy dữ liệu đó vào đúng Ứng dụng (Process) nào đang đợi (VD: vào Chrome hay vào Zalo).*

**Câu 32:** Kỹ thuật "Multiplexing" (Ghép kênh) tại máy gửi (Sender) trong Tầng giao vận có nghĩa là gì?
A. Nén nhiều file lại thành 1 file ZIP.
B. Thu thập các thông điệp từ nhiều Socket (từ nhiều ứng dụng khác nhau đang chạy), thêm Transport Header (chứa Source Port, Dest Port) vào từng thông điệp, rồi đẩy tất cả xuống Tầng mạng.
C. Mở nhiều tab trình duyệt cùng lúc.
D. Trộn lẫn tín hiệu điện trên cùng một sợi cáp.
*Đáp án: B*
*Giải thích: Giống như bưu điện gom thư từ nhiều hòm thư khác nhau trong thành phố, dán tem (Header) rồi bỏ chung vào một chiếc xe tải (Tầng mạng) để chở đi.*

**Câu 33:** Trong cấu trúc Header của một Segment UDP, tổng kích thước của Header là bao nhiêu byte?
A. 4 bytes
B. 8 bytes
C. 20 bytes
D. Không cố định
*Đáp án: B*
*Giải thích: UDP Header cực kỳ nhỏ gọn, chỉ có đúng 8 byte (gồm 4 trường, mỗi trường 2 byte: Source Port, Destination Port, Length, Checksum).*

**Câu 34:** Giao thức UDP được mô tả là "Connectionless" (Phi kết nối). Điều này có nghĩa là gì?
A. Nó không dùng dây cáp.
B. Nó không cần địa chỉ IP.
C. Không có quá trình thiết lập trạng thái hoặc "Bắt tay" (Handshake) giữa bên gửi và bên nhận trước khi dữ liệu thực sự được truyền đi.
D. Máy tính không cần kết nối mạng.
*Đáp án: C*
*Giải thích: UDP cứ có dữ liệu là ném thẳng vào mạng, không cần hỏi "Bên kia đã sẵn sàng chưa?" (Trái ngược với TCP dùng 3-way handshake).*

**Câu 35:** Trường "Checksum" trong UDP Header thực hiện chức năng gì?
A. Đảm bảo dữ liệu không bị ai nghe lén.
B. Cung cấp cơ chế phát hiện lỗi cơ bản (Error Detection) để xem gói tin có bị thay đổi/hỏng bit trong quá trình truyền qua mạng hay không.
C. Giới hạn số lượng gói tin được gửi.
D. Đếm số lượng router đã đi qua.
*Đáp án: B*
*Giải thích: Máy nhận tính lại Checksum dựa trên Payload nhận được và so sánh với Checksum trong Header. Nếu khác nhau, UDP biết gói tin đã bị rác/hỏng và thường sẽ thả (Drop) nó đi một cách thầm lặng.*

**Câu 36:** Đặc tính nào của UDP khiến nó RẤT ĐƯỢC ƯA CHUỘNG trong các cuộc tấn công từ chối dịch vụ (DDoS Amplification)?
A. Nó mã hóa dữ liệu.
B. UDP dễ dàng giả mạo IP nguồn (IP Spoofing) vì nó không yêu cầu quá trình "Bắt tay" xác nhận 2 chiều như TCP.
C. UDP không dùng Port.
D. UDP làm cháy Router.
*Đáp án: B*
*Giải thích: Vì không có handshake, Hacker gõ lệnh "Gửi 1 gói UDP đến máy chủ DNS, nhưng ghi địa chỉ Nguồn là IP của Nạn nhân". DNS Server nhận được, không chút nghi ngờ, gửi gói trả lời khổng lồ đập vào mặt nạn nhân.*

**Câu 37:** Nguyên lý RDT (Reliable Data Transfer - Truyền dữ liệu tin cậy) giải quyết hai vấn đề cốt lõi của một môi trường mạng vật lý không hoàn hảo là gì?
A. Tốc độ chậm và cáp đồng bị đứt.
B. Lỗi bit (Bit errors) và Mất gói tin (Packet loss).
C. Không có điện và hỏng phần mềm.
D. Tắc nghẽn mạng và định tuyến sai.
*Đáp án: B*
*Giải thích: Tầng liên kết bên dưới có thể làm hỏng bit, Router có thể vứt bỏ gói tin khi tràn hàng đợi. RDT sinh ra để sửa 2 lỗi này.*

**Câu 38:** Để giải quyết vấn đề "Lỗi Bit" (Bit errors), RDT sử dụng các cơ chế nào?
A. Stop-and-Wait.
B. Checksum (Phát hiện lỗi), ACK/NAK (Phản hồi trạng thái) và Retransmission (Truyền lại).
C. Tăng băng thông.
D. Đóng gói lại thành UDP.
*Đáp án: B*
*Giải thích: Nhận thấy gói hỏng (qua Checksum), máy nhận sẽ báo NAK (hoặc không báo ACK). Máy gửi nghe vậy sẽ gửi lại gói đó.*

**Câu 39:** Để giải quyết vấn đề "Mất gói" (Packet loss) - khi gói tin hoặc ACK biến mất hoàn toàn, RDT sử dụng thêm cơ chế nào?
A. Mã hoá.
B. Chạy đa luồng.
C. Bộ định thời (Timer/Timeout). Nếu sau một khoảng thời gian chờ mà không nhận được ACK, máy gửi tự động cho rằng gói tin đã mất và Truyền lại.
D. Tự sinh ra gói mới.
*Đáp án: C*
*Giải thích: Timer là công cụ bắt buộc. Nếu không có Timer, máy gửi sẽ ngồi chờ ACK mãi mãi (Deadlock) nếu gói tin bị rơi mất trên đường.*

**Câu 40:** "Sequence Number" (Số thứ tự) được sinh ra trong các giao thức RDT (và TCP) để giải quyết lỗ hổng logic nào?
A. Tăng kích thước gói tin.
B. Giải quyết việc Máy nhận không thể phân biệt được gói tin mới và Gói tin truyền lại (Duplicate packet) nếu ACK trước đó bị trễ hoặc mất.
C. Để nén dữ liệu.
D. Thay thế địa chỉ Port.
*Đáp án: B*
*Giải thích: Máy gửi gửi Gói X. Máy nhận gửi ACK X. Nhưng ACK X bị trễ. Máy gửi Timer timeout, tưởng mất nên gửi lại Gói X. Nếu không có Sequence Number để đánh dấu, máy nhận sẽ tưởng đây là Gói Y mới.*

**Câu 41:** Thuật toán RDT dạng "Stop-and-Wait" (Dừng và Đợi) có nhược điểm lớn nhất là gì?
A. Không phát hiện được lỗi bit.
B. Không giải quyết được mất gói.
C. Hiệu suất (Utilization) cực kỳ thảm hại trên các đường truyền có khoảng cách xa (Độ trễ truyền lan lớn), vì Máy gửi phải ngồi chơi chờ ACK sau mỗi một gói tin nhỏ.
D. Yêu cầu cáp quang.
*Đáp án: C*
*Giải thích: Nếu RTT là 30ms, gửi 1 gói 1KB mất 1ms. Stop-and-Wait sẽ lãng phí 30ms ngồi chờ rỗng, làm giảm tốc độ thực tế từ 1Gbps xuống còn chưa tới 1Mbps.*

**Câu 42:** Để khắc phục nhược điểm của "Stop-and-Wait", RDT hiện đại (và TCP) sử dụng kỹ thuật nào?
A. Đổi cáp mạng.
B. Pipeline (Đường ống) - Cho phép Máy gửi được phép gửi nhiều gói tin liên tiếp vào mạng mà KHÔNG CẦN CHỜ các gói trước đó được ACK ngay lập tức.
C. Gom 100 gói thành 1 gói.
D. Chuyển sang UDP.
*Đáp án: B*
*Giải thích: Pipeline tận dụng việc "nhồi" đầy gói tin vào không gian RTT, giúp đường truyền luôn bận rộn và đạt tối đa băng thông.*

**Câu 43:** Trong kỹ thuật Pipeline, phương pháp "Go-Back-N" (GBN) phản ứng thế nào khi Máy nhận phát hiện bị mất Gói tin số 3 (nhưng đã nhận được gói 4, 5)?
A. Nó lưu gói 4, 5 vào buffer, chỉ yêu cầu gửi lại gói 3.
B. Nó vứt bỏ gói 4, 5 (vì sai thứ tự). Máy gửi khi Timeout gói 3 sẽ tự động Truyền Lại TOÀN BỘ cửa sổ từ gói 3 trở đi (3, 4, 5...).
C. Nó bỏ qua gói 3 luôn.
D. Báo lỗi sập mạng.
*Đáp án: B*
*Giải thích: GBN (Trở lại N) rất đơn giản phía nhận: "Sai thứ tự là vứt". Nhưng nhược điểm là Máy gửi phải truyền lại một lượng lớn dữ liệu dù chúng đã đến đích an toàn.*

**Câu 44:** Phương pháp "Selective Repeat" (SR - Lặp lại có chọn lọc) khác với Go-Back-N ở điểm nào?
A. SR kém hiệu quả hơn GBN.
B. SR Máy nhận sẽ Ghi đệm (Buffer) các gói tin đến không đúng thứ tự. Máy gửi CHỈ truyền lại đúng NHỮNG GÓI TIN bị mất hoặc lỗi, không truyền lại cả loạt.
C. SR không dùng Sequence Number.
D. Không có khác biệt.
*Đáp án: B*
*Giải thích: SR thông minh hơn, tiết kiệm băng thông hơn GBN vì tránh việc truyền lại thừa thãi, bù lại SR đòi hỏi bộ nhớ đệm (Buffer) và độ phức tạp cao hơn ở Máy nhận.*

**Câu 45:** Cấu trúc TCP Segment Header tối thiểu (không có phần Options) có kích thước là bao nhiêu?
A. 8 bytes
B. 16 bytes
C. 20 bytes
D. 32 bytes
*Đáp án: C*
*Giải thích: Tương đương IPv4 Header. 20 Bytes này chứa rất nhiều thông tin: Port, Seq#, Ack#, Window Size, Checksum, Flags (SYN, ACK, FIN...)*

**Câu 46:** TCP cung cấp dịch vụ "Full-Duplex" (Song công toàn phần). Tính chất này cho phép:
A. Thiết bị chỉ gửi được vào ban ngày.
B. TCP chia đôi dữ liệu để gửi 2 đường.
C. Dữ liệu từ Process A đến Process B và dữ liệu từ Process B đến Process A có thể chảy song song và đồng thời trên cùng một kết nối duy nhất.
D. TCP chạy trên cả IPv4 và IPv6.
*Đáp án: C*
*Giải thích: Kết nối TCP là một ống nước có 2 ngăn, cho phép 2 bên thoải mái gửi data qua lại bất cứ lúc nào.*

**Câu 47:** Trong quá trình "Thiết lập kết nối TCP" (3-way Handshake), bước đầu tiên Máy khách (Client) gửi cho Máy chủ (Server) một gói tin có đặc điểm gì?
A. Chứa mật khẩu.
B. Chứa thẻ HTML.
C. Là một Segment không có dữ liệu (Payload = 0) và Cờ SYN (Synchronize) được bật lên mức 1. Nó cũng chọn ngẫu nhiên một Số thứ tự ban đầu (ISN).
D. Gói tin UDP.
*Đáp án: C*
*Giải thích: SYN là lời chào "Tôi muốn thiết lập kết nối, tôi sẽ bắt đầu đếm số thứ tự từ X nhé".*

**Câu 48:** Bước thứ 2 trong quá trình Bắt tay 3 bước của TCP diễn ra như thế nào?
A. Server gửi file index.html.
B. Server gửi gói SYN/ACK (Bật cả cờ SYN và cờ ACK). Server xác nhận số X của Client (ACK = X+1) và đồng thời chọn Số thứ tự ban đầu của mình là Y (SYN = Y).
C. Server đóng cổng.
D. Client tự gửi bước 2.
*Đáp án: B*
*Giải thích: Server vừa gật đầu chào lại (ACK), vừa thông báo "Tôi đồng ý, tôi sẽ đếm số thứ tự từ Y nhé" (SYN).*

**Câu 49:** Tại sao TCP cần đến BƯỚC THỨ 3 (Máy khách gửi lại gói ACK) trong quá trình thiết lập kết nối?
A. Để làm màu.
B. Để máy khách xác nhận lại cho Máy chủ biết rằng "Tôi đã nghe thấy Số thứ tự Y của bạn rồi". Hoàn tất việc đồng bộ thông số 2 chiều một cách chắc chắn trước khi truyền Dữ liệu.
C. Để Server gửi mật khẩu.
D. Để chuyển sang giao thức UDP.
*Đáp án: B*
*Giải thích: Nếu không có bước 3, Server sẽ không chắc Client có bị rớt mạng hay không sau khi Server gửi gói 2. Ở bước 3, Client cũng có thể bắt đầu nhét luôn HTTP GET vào Body.*

**Câu 50:** Quá trình "Đóng kết nối" (Teardown) của TCP thường diễn ra bao nhiêu bước (tin nhắn) hoàn chỉnh để đóng cả 2 chiều một cách an toàn?
A. 2 bước
B. 3 bước
C. 4 bước
D. 1 bước
*Đáp án: C*
*Giải thích: Khi A muốn nghỉ: A gửi FIN -> B xác nhận ACK (A hết nói, nhưng B vẫn được nói). Khi B cũng muốn nghỉ: B gửi FIN -> A xác nhận ACK. TCP gọi là 4-way teardown.*

**Câu 51:** "Kiểm soát luồng" (Flow Control) trong TCP nhằm bảo vệ hệ thống nào?
A. Router ở giữa mạng.
B. Đường cáp quang dưới biển.
C. Bảo vệ Máy nhận (Receiver) không bị ngập lụt dữ liệu, làm tràn Bộ nhớ đệm (Receive Buffer) khi Máy gửi (Sender) truyền quá nhanh mà Ứng dụng Máy nhận chưa kịp đọc/xử lý.
D. Trình duyệt Chrome.
*Đáp án: C*
*Giải thích: Nếu PC 1Gbps gửi sang Điện thoại 10Mbps, điện thoại sẽ bị nghẹn. Flow Control là máy nhận dơ bảng báo "Tôi chỉ còn 5MB trống" để máy gửi biết đường hãm phanh.*

**Câu 52:** TCP thực hiện Flow Control bằng cách sử dụng thông số nào trong TCP Header?
A. Cờ SYN.
B. Receive Window (rwnd - Cửa sổ nhận).
C. Checksum.
D. Cờ PSH.
*Đáp án: B*
*Giải thích: Mỗi gói ACK gửi về, máy nhận đính kèm thông số Receive Window (không gian trống còn lại trong Buffer). Máy gửi luôn đảm bảo Số lượng Byte đang gửi (chưa được ACK) không bao giờ vượt quá rwnd.*

**Câu 53:** Khác với "Kiểm soát luồng" (Bảo vệ máy nhận), chức năng "Kiểm soát tắc nghẽn" (Congestion Control) của TCP nhằm mục đích bảo vệ cái gì?
A. Bảo vệ ổ cứng máy gửi.
B. Bảo vệ phần mềm diệt virus.
C. Bảo vệ toàn bộ Cơ sở hạ tầng mạng (Network Core - Các Router, Link) không bị quá tải (dẫn đến sụp đổ mạng - Congestion Collapse) do có quá nhiều máy tính cùng bơm dữ liệu vào mạng lúc.
D. Ngăn bị tấn công DDOS.
*Đáp án: C*
*Giải thích: Router không có cách nào yêu cầu Máy tính "Đừng gửi nữa". Máy tính phải TỰ Ý THỨC phát hiện mạng đang tắc nghẽn để TỰ ĐỘNG giảm tốc độ gửi lại.*

**Câu 54:** Máy gửi TCP làm thế nào để TỰ NHẬN BIẾT được rằng Mạng Lõi đang bị tắc nghẽn (Congestion)?
A. Router gửi email báo cho máy gửi.
B. Dựa vào Cờ FIN.
C. Thông qua hiện tượng Mất gói (Packet Loss) do tràn bộ đệm tại Router. Máy gửi thấy Hết giờ (Timeout) hoặc nhận 3 ACK lặp (Duplicate ACKs) thì suy ra mạng đang kẹt.
D. Máy gửi gọi điện hỏi ISP.
*Đáp án: C*
*Giải thích: IP là mạng câm (không phản hồi). TCP phải phán đoán: "Nếu tôi gửi mà mãi không thấy ACK về, chắc chắn Router ở đâu đó đã vứt gói của tôi vì nó quá tải rồi".*

**Câu 55:** Thuật toán Kiểm soát tắc nghẽn của TCP điều chỉnh một biến trạng thái có tên là gì để giới hạn số gói tin được phép gửi vào mạng?
A. Receive Window (rwnd)
B. Congestion Window (cwnd)
C. MSS
D. TTL
*Đáp án: B*
*Giải thích: Máy gửi bị giới hạn bởi cả rwnd (do máy nhận quy định) và cwnd (do thuật toán của chính máy gửi tính toán dựa trên tình trạng mạng). Tốc độ gửi tỉ lệ thuận với cwnd.*

**Câu 56:** Giai đoạn "Khởi động chậm" (Slow Start) trong thuật toán kiểm soát tắc nghẽn TCP diễn ra như thế nào?
A. Gửi cực kỳ chậm và giữ nguyên tốc độ đó.
B. Bắt đầu với cwnd rất nhỏ (1 MSS), nhưng TĂNG THEO CẤP SỐ NHÂN (Gấp đôi cwnd) sau mỗi RTT (bằng cách cộng thêm 1 MSS cho mỗi ACK nhận được) để dò tìm giới hạn băng thông cực kỳ nhanh.
C. Bắt đầu gửi 1000 gói tin cùng lúc.
D. Gửi gói tin rỗng.
*Đáp án: B*
*Giải thích: Tên là "Slow Start" nhưng thực chất nó tăng tốc độ theo cấp số nhân (1, 2, 4, 8, 16...). Đây là giai đoạn thăm dò xem ống nước to cỡ nào khi vừa mới mở kết nối.*

**Câu 57:** Khi biến Congestion Window (cwnd) chạm đến ngưỡng `ssthresh` (Slow Start Threshold), thuật toán TCP chuyển sang giai đoạn nào?
A. Dừng gửi dữ liệu.
B. Giai đoạn Tránh tắc nghẽn (Congestion Avoidance). Lúc này cwnd chuyển sang TĂNG THEO CẤP SỐ CỘNG (Tuyến tính) mỗi RTT để dò dẫm giới hạn một cách an toàn hơn.
C. Tăng gấp 4 lần cwnd.
D. Đóng kết nối.
*Đáp án: B*
*Giải thích: Khi đã tăng theo cấp số nhân (rất bạo lực) đến một mốc an toàn nhất định, TCP chuyển sang tăng rón rén (+1 mỗi vòng) để tránh đâm sầm vào vách đá (vượt ngưỡng chịu đựng của Router).*

**Câu 58:** Cấu trúc TCP Segment không quy định rõ "ranh giới" thông điệp cho Tầng ứng dụng (như HTTP). Tính chất này gọi là gì?
A. Đa phân mảnh.
B. Stateless.
C. Luồng byte liên tục (Byte-stream). TCP nhìn dữ liệu như một dòng sông byte tuôn chảy, không quan tâm nội dung, ứng dụng đọc phải tự tự cắt xén dựa vào nội dung (như ký tự \r\n).
D. Block-chain.
*Đáp án: C*
*Giải thích: UDP gửi 1 gói 100 byte, máy nhận nhận đúng 1 khối 100 byte. TCP có thể gom nhiều `send()` nhỏ của App vào 1 Segment, hoặc chặt 1 `send()` to thành nhiều Segment.*

**Câu 59:** Tấn công "SYN Flood" lợi dụng bước nào trong giao thức TCP?
A. Quá trình truyền dữ liệu Data.
B. Bước 1 của Handshake: Kẻ tấn công gửi hàng triệu gói SYN rác nhưng KHÔNG BAO GIỜ hoàn thành bước 3 (ACK). Máy chủ web cấp phát RAM/Tài nguyên để chờ đợi đến khi cạn kiệt, không thể đón khách thật.
C. Quá trình đóng kết nối FIN.
D. Gửi ACK giả mạo.
*Đáp án: B*
*Giải thích: Đây là kiểu tấn công DoS kinh điển vào Tầng Giao vận. Server nhận SYN, cấp phát Half-open connection (treo đó chờ). Nếu quá nhiều, Server hết bộ nhớ.*

**Câu 60:** Cơ chế "SYN Cookies" được sinh ra để khắc phục vấn đề gì?
A. Chống bị đọc trộm Web Cookie.
B. Chống lại tấn công SYN Flood. Khi Server nhận SYN, nó không cấp phát RAM ngay, mà tính toán một con số mã hóa (Cookie) nhét vào gói SYN/ACK trả về, chỉ khi Client gửi đúng số đó ở bước 3, Server mới cấp phát bộ nhớ.
C. Chống dội bom email.
D. Nén gói SYN.
*Đáp án: B*
*Giải thích: Tính năng phòng thủ rất thông minh của TCP ở các hệ điều hành hiện đại để vượt qua bão SYN Flood.*

**Câu 61:** Lựa chọn giao thức Giao vận nào cho ứng dụng "Phát sóng Trực tiếp" (Live Streaming) nếu bạn ưu tiên việc Mọi khán giả đều xem được hình ảnh MƯỢT MÀ, không quan tâm việc chất lượng có thể bị nhoè đôi chút?
A. TCP vì nó đảm bảo không sai màu.
B. ICMP.
C. UDP. Vì TCP sẽ làm luồng live bị đứng hình (buffering) nếu đường truyền chập chờn do cơ chế truyền lại và congestion control giảm tốc.
D. HTTP/2.
*Đáp án: C*
*Giải thích: Live stream (nhất là tương tác thấp như Twitch, bóng đá) dùng TCP qua HTTP vẫn phổ biến (DASH), nhưng ở các kênh ưu tiên thời gian thực (như Discord, WebRTC), UDP luôn là chân ái.*

**Câu 62:** Lệnh `netstat -n` trên Windows dùng để kiểm tra điều gì liên quan đến Tầng giao vận?
A. Kiểm tra card mạng hỏng chưa.
B. Liệt kê TẤT CẢ các Socket (Cổng) TCP/UDP đang mở, đang Lắng nghe (LISTENING) hoặc Đã thiết lập kết nối (ESTABLISHED) trên máy tính.
C. Quét virus TCP.
D. Xoá bộ nhớ đệm.
*Đáp án: B*
*Giải thích: Công cụ kinh điển để IT kiểm tra xem có phần mềm nào đang lén lút mở Port kết nối ra ngoài (Trojan) hay Web server đã chạy lên Port 80 chưa.*

**Câu 63:** Khái niệm "Demultiplexing" (Phân kênh) ở máy nhận TCP hoạt động dựa trên thông số nào?
A. Chỉ dựa vào Port đích (Destination Port).
B. Dựa vào IP nguồn, IP đích, Port nguồn và Port đích (Bộ 4 tham số - 4 tuple).
C. Dựa vào Địa chỉ MAC.
D. Dựa vào URL.
*Đáp án: B*
*Giải thích: UDP Socket chỉ cần (IP đích, Port đích) để ném vào App. TCP Socket Cần cả 4 để phân biệt các Client khác nhau đang cùng truy cập vào 1 Port Server.*

**Câu 64:** Số liệu thống kê chỉ ra rằng phần lớn giao thông (Traffic) trên Internet hiện nay chạy trên nền tảng giao thức giao vận nào?
A. TCP. (Nhờ Web HTTP/HTTPS, Video Streaming DASH, File, Email).
B. UDP.
C. SCTP.
D. IPsec.
*Đáp án: A*
*Giải thích: Dù UDP tốt cho Real-time, nhưng Video Streaming hiện đại (Youtube/Netflix) dùng HTTP (DASH) chạy trên TCP, chiếm phần lớn dung lượng Internet.*

**Câu 65:** Số cổng (Port Number) 22 được mặc định dành cho dịch vụ nào?
A. DNS
B. FTP
C. HTTP
D. SSH (Secure Shell)
*Đáp án: D*
*Giải thích: Các port Well-known rất quan trọng: 21 (FTP), 22 (SSH), 25 (SMTP), 53 (DNS), 80 (HTTP), 443 (HTTPS).*

**Câu 66:** Quá trình "Fast Retransmit" (Truyền lại nhanh) của TCP xảy ra khi nào thay vì đợi Timeout?
A. Ngay khi gửi xong gói tin.
B. Khi nhận được một gói tin sai địa chỉ MAC.
C. Khi Máy gửi nhận được 3 ACK lặp lại (Triple Duplicate ACKs) cho cùng một số thứ tự. Điều này báo hiệu gói tin tiếp theo chắc chắn đã mất, Máy gửi lập tức truyền lại mà không chờ đếm ngược Timeout.
D. Khi rút cáp.
*Đáp án: C*
*Giải thích: Timeout thường mất rất lâu (vài giây). 3 ACK lặp là tín hiệu cảnh báo sớm: "Tôi đã nhận được 3 gói mới nhất, nhưng gói ở giữa vẫn chưa thấy". TCP lập tức gửi lại gói giữa đó.*

**Câu 67:** Timeout (Thời gian chờ để truyền lại) trong TCP được thiết lập như thế nào?
A. Cố định ở mức 5 giây.
B. Cố định ở mức 1 mili-giây.
C. TCP liên tục đo đạc và tính toán thời gian Round Trip Time (RTT) trung bình của mạng (SampleRTT) và thiết lập Timeout nhỉnh hơn RTT trung bình một chút.
D. Bằng kích thước gói tin.
*Đáp án: C*
*Giải thích: Mạng biến động liên tục, nếu đặt Timeout tĩnh quá dài sẽ chờ lâu, quá ngắn sẽ bị truyền lại rác (do gói chưa kịp về).*

**Câu 68:** Thuật toán Nagle được tích hợp trong TCP dùng để giải quyết vấn đề gì liên quan đến ứng dụng Telnet/SSH?
A. Chống Virus Keylogger.
B. Tránh việc gửi quá nhiều gói tin siêu nhỏ (Mỗi gói chỉ chứa 1 byte phím gõ nhưng cõng thêm 40 byte Header) lên mạng. Thuật toán sẽ đệm (gom) các phím gõ lại và gửi trong một gói lớn hơn.
C. Tăng độ trễ để chơi game mượt hơn.
D. Giới hạn số lượng user truy cập.
*Đáp án: B*
*Giải thích: Nagle tối ưu băng thông (tránh Hội chứng cửa sổ ngu ngốc - Silly window syndrome). Tuy nhiên, trong Game Online, Lập trình viên phải TẮT thuật toán Nagle (`TCP_NODELAY`) để phím bấm ăn ngay lập tức.*

**Câu 69:** TCP tính toán Checksum bao gồm phần Header TCP, Dữ liệu và một cấu trúc "Header Giả" (Pseudo-Header). Pseudo-Header này chứa thông tin gì?
A. Mật khẩu Wi-Fi.
B. IP Nguồn và IP Đích lấy từ Tầng Mạng (IP).
C. Địa chỉ MAC.
D. Ngày giờ hệ thống.
*Đáp án: B*
*Giải thích: Dù TCP nằm ở Tầng Giao vận, nó lấy lén 2 IP từ Tầng Mạng đưa vào tính Checksum để đảm bảo gói TCP này thực sự được giao cho ĐÚNG MÁY TÍNH (sai IP đích thì Checksum sẽ sai).*

**Câu 70:** Trạng thái TIME_WAIT trong chu trình đóng kết nối TCP có ý nghĩa gì đối với máy tính chủ động đóng (Active close)?
A. Đợi nạp tiền cước.
B. Đợi để đóng cáp mạng.
C. Máy tính phải chờ một khoảng thời gian (thường là 2*MSL, khoảng 1-2 phút) sau khi gửi ACK cuối cùng để đề phòng ACK này bị mất, và để các gói tin lạc lõng cũ chết hẳn trên mạng trước khi tái sử dụng Cổng (Port) đó.
D. Tắt nguồn ngay lập tức.
*Đáp án: C*
*Giải thích: Nếu vừa đóng xong đã mở Port đó cho App khác, các gói tin cũ đến muộn (do tắc đường) có thể lọt vào App mới gây lỗi.*

**Câu 71:** Khi TCP gặp hiện tượng Mất gói (Packet Loss) do Hết giờ (Timeout), cwnd (Cửa sổ tắc nghẽn) sẽ phản ứng như thế nào (theo phiên bản TCP Reno)?
A. Giảm cwnd đi một nửa.
B. Giữ nguyên cwnd.
C. Reset cwnd về lại mức khởi điểm là 1 MSS, và bắt đầu lại quá trình Slow Start.
D. Tăng cwnd gấp đôi.
*Đáp án: C*
*Giải thích: Timeout là mức độ nghiêm trọng nhất của tắc nghẽn (Mạng kẹt cứng không có 1 cái ACK nào về). TCP phản ứng bằng cách "đạp phanh gấp", giảm tốc độ về con số 0.*

**Câu 72:** Nếu TCP gặp hiện tượng Mất gói nhưng thông qua cơ chế 3 ACK lặp (Fast Retransmit), cwnd sẽ phản ứng như thế nào (TCP Reno)?
A. Reset về 1 MSS.
B. Giảm cwnd ĐI MỘT NỬA (Cắt đôi) và bước vào giai đoạn Phục hồi nhanh (Fast Recovery).
C. Tăng lên mức tối đa.
D. Đóng kết nối.
*Đáp án: B*
*Giải thích: 3 ACK lặp chứng tỏ mạng vẫn còn lưu thông (có gói tin khác lọt qua được để tạo ra ACK). Nên TCP chỉ "rảo phanh", giảm một nửa tốc độ để giảm tải cho Router.*

**Câu 73:** Lợi thế của giao thức QUIC (Quick UDP Internet Connections) đang được Google thúc đẩy mạnh mẽ thay thế TCP cho HTTP/3 là gì?
A. QUIC không cần cáp mạng.
B. QUIC hoạt động trên UDP, gộp quá trình Bắt tay TCP và Bắt tay Mã hóa (TLS) làm một, giảm RTT xuống mức 0 (với client cũ). Đồng thời giải quyết hoàn toàn lỗi Head-of-line blocking của TCP.
C. QUIC bỏ qua mọi kiểm tra lỗi.
D. QUIC chỉ chạy trên 5G.
*Đáp án: B*
*Giải thích: TCP nằm sâu trong Nhân Hệ điều hành (Kernel) nên rất khó sửa đổi chuẩn. QUIC khéo léo dùng UDP (cho qua các Firewall) và tự thân tích hợp TCP-logic vào Application space (dễ cập nhật).*

**Câu 74:** Đặc điểm của cơ chế "Cumulative ACK" (ACK tích lũy) trong TCP là gì?
A. Chỉ ACK từng gói lẻ tẻ.
B. Nếu nhận được gói 1, 2, 3 liên tục, Máy nhận chỉ cần gửi 1 gói `ACK 4` để ngụ ý "Tôi đã nhận đủ TẤT CẢ các gói từ 3 trở xuống, xin hãy gửi gói từ Byte số 4".
C. Gom 10 gói tin vào 1 ACK.
D. Cộng dồn dung lượng gói.
*Đáp án: B*
*Giải thích: Cumulative ACK giúp giảm đáng kể lượng rác ACK trên mạng. Nếu gói `ACK 2` bị rớt, nhưng `ACK 4` về đích, Máy gửi vẫn biết gói 2 đã thành công vì `ACK 4` bao trùm lên nó.*

**Câu 75:** Trong lập trình mạng bằng C/Python, hàm `socket(AF_INET, SOCK_STREAM)` dùng để tạo ra một đối tượng kết nối thuộc giao thức nào?
A. ICMP
B. UDP
C. TCP
D. IGMP
*Đáp án: C*
*Giải thích: `SOCK_STREAM` ám chỉ luồng dữ liệu liên tục có thứ tự và tin cậy (TCP). Nếu dùng `SOCK_DGRAM` (Datagram) thì sẽ sinh ra Socket UDP.*

**Câu 76:** Chỉ số "Fairness" (Tính công bằng) của thuật toán Congestion Control TCP (TCP Reno) được thể hiện như thế nào khi có K kết nối TCP chia sẻ chung một liên kết nút cổ chai (Bottleneck) có băng thông R?
A. Không công bằng, ai đến trước lấy hết.
B. Không công bằng, chia theo cấp bậc IP.
C. Theo thời gian, thuật toán TCP sẽ tự động điều tiết khiến cho mỗi kết nối nhận được một phần băng thông xấp xỉ R/K, chia đều tài nguyên mạng một cách tự nhiên.
D. ISP phải chia bằng tay.
*Đáp án: C*
*Giải thích: Do tính chất "Tăng cộng (khi rảnh) - Giảm nhân (khi kẹt)" (AIMD), các luồng TCP ép nhau cho đến khi mọi luồng đều có băng thông gần bằng nhau.*

**Câu 77:** Hai máy tính A và B cùng kết nối vào một Router nhà. Máy A mở 1 Session tải file (TCP), Máy B mở 9 Session tải file (TCP). Theo tính công bằng của TCP, máy nào sẽ lấy nhiều băng thông hơn?
A. Máy A.
B. Máy B (Lấy 9/10 tổng băng thông).
C. Bằng nhau.
D. Tuỳ thuộc Router.
*Đáp án: B*
*Giải thích: TCP chia đều băng thông cho CÁC KẾT NỐI (Sessions), không phải cho Máy tính (Hosts). Đó là lý do phần mềm tải file (IDM) thường chẻ 1 file thành 8-16 Session TCP nhỏ để "hút máu" đường truyền mạnh hơn.*

**Câu 78:** Mạng UDP có tính công bằng (Fairness) với TCP không nếu chúng chạy chung trên một đường cáp?
A. Có, chia đều.
B. Không. Do UDP không có cơ chế "Đạp phanh" (Kiểm soát tắc nghẽn). Khi mạng nghẽn, TCP tự động giảm tốc độ, nhưng UDP vẫn bơm ồ ạt, dẫn đến UDP lấn át và cướp hết băng thông của TCP.
C. TCP lấn át UDP.
D. UDP tự đóng khi thấy TCP.
*Đáp án: B*
*Giải thích: Đây là lý do các nhà mạng rất ghét lưu lượng UDP tốc độ cao (như từ các tool DDoS), nó không có "ý thức" nhường đường và sẽ làm sập các ứng dụng TCP chuẩn mực.*

**Câu 79:** Kích thước Cửa sổ nhận (Receive Window - rwnd) trong TCP Header do bên nào quyết định và với mục đích gì?
A. Bên Gửi quyết định để đo tốc độ mạng.
B. Bên Nhận quyết định, dùng để thông báo cho bên Gửi biết mình còn bao nhiêu dung lượng trống trong Buffer, nhằm ngăn bên Gửi gửi quá nhanh làm tràn Buffer (Kiểm soát luồng).
C. Router quyết định để chia sẻ băng thông.
D. ISP quyết định để tính cước.
*Đáp án: B*
*Giải thích: Đây là giao tiếp "End-to-End". Máy yếu (RAM ít) sẽ gửi rwnd nhỏ, máy mạnh (RAM nhiều) gửi rwnd lớn.*

**Câu 80:** "Cổng" (Port) trong TCP/UDP không phải là cổng vật lý trên switch. Vậy nó là gì?
A. Mã số MAC.
B. Ổ cắm điện.
C. Một định danh Logic (Số nguyên 16-bit) do Hệ điều hành tạo ra nhằm phân biệt và ánh xạ dữ liệu mạng tới các Tiến trình (Process) ứng dụng khác nhau đang chạy trên cùng một máy.
D. Tên miền.
*Đáp án: C*
*Giải thích: Nếu không có Port, gói tin từ Zalo và gói tin từ Chrome về máy bạn, hệ điều hành sẽ không biết ném gói nào vào màn hình Zalo, ném gói nào vào màn hình Chrome.*

**Câu 81:** Ứng dụng P2P sử dụng thuật toán "Lỗ thủng NAT" (NAT Traversal / UDP Hole Punching) nhằm mục đích gì ở Tầng giao vận?
A. Sửa lỗi phần cứng.
B. Giúp hai Máy khách (Client) đều đang nằm ẩn sau các Tường lửa / NAT có thể thiết lập được một kết nối UDP trực tiếp với nhau (như trong cuộc gọi Skype/Zalo) mà không bị NAT chặn lại.
C. Bắt luồng TCP.
D. Nén dữ liệu.
*Đáp án: B*
*Giải thích: Vì 2 NAT đều chặn luồng lạ đi vào. Chúng phải nhờ 1 Server trung gian (STUN Server) "dắt mối", khiến 2 NAT tưởng lầm và mở một lỗ thủng cho nhau chui qua.*

**Câu 82:** "Cờ FIN" trong Header của TCP biểu thị điều gì?
A. Báo hiệu bị lỗi Checksum.
B. Báo hiệu muốn mở kết nối.
C. Báo hiệu rằng Máy gửi đã "Kết thúc" (Finish), không còn dữ liệu nào cần gửi vào đường ống nữa và muốn khởi xướng quá trình Đóng kết nối.
D. Yêu cầu truyền lại gói tin.
*Đáp án: C*
*Giải thích: Đóng bằng FIN là đóng "Lịch sự". Dữ liệu cũ vẫn được phép gửi cho đến khi hết. Trái ngược với Cờ RST (Reset) là đóng bạo lực, cắt ngang lập tức.*

**Câu 83:** Trong một Tấn công Từ chối Dịch vụ (DoS) sử dụng UDP Flood, hacker thường nã hàng triệu gói UDP rác vào một cổng Port ngẫu nhiên trên máy chủ. Máy chủ thông thường sẽ phản ứng (theo giao thức) như thế nào ở Tầng mạng/Giao vận?
A. Cháy CPU lập tức.
B. Gửi lại ICMP "Destination Unreachable" (Port Unreachable) vì không có ứng dụng nào mở ở cổng ngẫu nhiên đó. Hành động dội ngược này làm kiệt quệ tài nguyên máy chủ.
C. Mã hóa gói tin rác.
D. Đóng nguồn điện.
*Đáp án: B*
*Giải thích: Phản ứng báo lỗi của HĐH chính là điểm yếu chí mạng khiến CPU máy chủ phải làm việc liên tục để trả lời thư rác.*

**Câu 84:** Nếu Giao thức tầng Ứng dụng cần Bảo mật (Mã hóa SSL/TLS), thì TLS được cấy ghép vào đâu trong mô hình TCP/IP?
A. Bên dưới Tầng mạng.
B. Gắn vào Router.
C. Nằm "bánh mì kẹp thịt" giữa Tầng Ứng dụng (vd: HTTP) và Tầng Giao vận (TCP Socket).
D. Ở bên trong cáp quang.
*Đáp án: C*
*Giải thích: HTTP không còn gọi trực tiếp TCP Socket nữa. Nó gọi thư viện TLS. TLS mã hóa đoạn Text thành mã rác, rồi TLS mới gọi TCP Socket để đẩy đi.*

**Câu 85:** Đối với một gói tin TCP, quá trình Đóng gói (Encapsulation) diễn ra theo thứ tự nào?
A. Application Data -> Thêm TCP Header -> Thêm IP Header -> Thêm Frame Header (MAC).
B. MAC Header -> IP Header -> TCP Header -> Data.
C. TCP -> UDP -> IP -> MAC.
D. Data -> HTTP -> TCP -> Frame.
*Đáp án: A*
*Giải thích: Tưởng tượng như củ hành. Lớp Data trong cùng, mỗi tầng mạng đi xuống sẽ khoác thêm một lớp vỏ bảo vệ.*

**Câu 86:** Chỉ số "Payload" (Tải trọng) trong một TCP Segment được tính bằng công thức nào (Nếu biết tổng chiều dài gói IP)?
A. Bằng Tổng chiều dài IP.
B. Kích thước Payload TCP = (Tổng chiều dài gói IP) trừ đi (Kích thước IP Header) trừ đi (Kích thước TCP Header).
C. Luôn cố định 1500 bytes.
D. Bằng kích thước MAC.
*Đáp án: B*
*Giải thích: Payload là phần lõi thực sự do Ứng dụng gửi xuống. Phải bóc hết các lớp vỏ IP (20 byte) và TCP (20 byte) mới ra Payload.*

**Câu 87:** Khái niệm "RDT" (Reliable Data Transfer) được nhắc nhiều trong giáo trình mạng đại diện cho điều gì?
A. Tên một giao thức thực tế của Microsoft.
B. Một khái niệm lý thuyết trừu tượng mô hình hóa các cơ chế (như ACK, Sequence, Timer) cần thiết để xây dựng sự tin cậy trên một kênh không tin cậy. TCP là một bản hiện thực hóa của RDT.
C. Tên phần cứng của Switch.
D. Ứng dụng chống Spam.
*Đáp án: B*
*Giải thích: Trong sách Kurose/Ross, RDT 1.0 đến 3.0 là các bước lập luận lý thuyết giúp sinh viên hiểu tại sao TCP phải phức tạp như hiện nay.*

**Câu 88:** Trường "Window Size" (16-bit) trong TCP Header có giới hạn tối đa theo lý thuyết cổ điển là 65.535 byte (64KB). Trên các đường truyền Cáp quang quang xuyên lục địa (Băng thông cực cao, Trễ cực lớn - LFN), giới hạn này gây ra điều gì?
A. Không ảnh hưởng gì.
B. Máy gửi chỉ có thể nhồi tối đa 64KB dữ liệu vào "đường ống" trước khi phải chờ ACK. Nếu đường ống rất to (Băng thông x Trễ lớn), 64KB không đủ "lấp đầy" ống, làm lãng phí băng thông thê thảm.
C. Gây đứt cáp quang.
D. Biến TCP thành UDP.
*Đáp án: B*
*Giải thích: Giải pháp là TCP Window Scaling (RFC 1323) được thêm vào Option Header, cho phép nhân bản (shift left) kích thước Window lên hàng Gigabytes.*

**Câu 89:** Một Segment TCP có trường `ACK Number = 5000`. Con số 5000 này nói lên ý nghĩa gì với máy nhận?
A. Cổng 5000 đang mở.
B. Máy nhận đã gửi 5000 byte.
C. "Tôi đã nhận hoàn hảo tất cả các byte dữ liệu đến byte thứ 4999. Tôi đang mong chờ byte dữ liệu tiếp theo bắt đầu từ vị trí 5000".
D. Gói tin nặng 5000 byte.
*Đáp án: C*
*Giải thích: ACK trong TCP luôn mang ý nghĩa là "SỐ BYTE MONG ĐỢI TIẾP THEO" (Next Expected Byte), chứ không phải số hiệu của gói tin.*

**Câu 90:** Hiện tượng "Silly Window Syndrome" (Hội chứng cửa sổ ngu ngốc) trong TCP xảy ra khi:
A. Mở quá nhiều tab Chrome.
B. Máy nhận đọc dữ liệu quá chậm (1 byte mỗi lần), liên tục gửi báo cáo Window Size = 1. Máy gửi nhận được lệnh, liền ngoan ngoãn gửi các gói TCP siêu nhỏ (cõng 40 byte Header chỉ để chở 1 byte Data), làm tắc nghẽn mạng nghiêm trọng.
C. Trình duyệt bị lỗi hiển thị.
D. Máy tính nhiễm Virus.
*Đáp án: B*
*Giải thích: Giải pháp cho phía Nhận là Thuật toán Clark (Không báo cáo Window nếu trống quá ít). Giải pháp phía Gửi là Thuật toán Nagle (Không gửi gói lắt nhắt).*

**Câu 91:** Khi ứng dụng thực hiện lời gọi `send()` trên một Socket TCP, dữ liệu ngay lập tức đi đâu?
A. Phóng thẳng ra đường dây mạng vật lý.
B. Đi vào không trung bằng sóng Wi-Fi.
C. Được chép từ bộ nhớ Ứng dụng (User space) vào Bộ đệm Gửi (Send Buffer) của TCP nằm trong Nhân Hệ điều hành (Kernel). Giao thức TCP sẽ tự quyết định KHI NÀO đóng gói và truyền đi.
D. Xóa khỏi RAM.
*Đáp án: C*
*Giải thích: Ứng dụng không thể ra lệnh trực tiếp cho Card mạng. Nó chỉ "khoán" data cho TCP. TCP có thể gộp nhiều data lại (Nagle) rồi mới đẩy đi.*

**Câu 92:** TCP sử dụng giao thức nào của Tầng Mạng để truyền tải (bọc Segment) qua Internet?
A. MAC
B. UDP
C. ICMP
D. IPv4 hoặc IPv6
*Đáp án: D*
*Giải thích: Mọi Segment của tầng Transport cuối cùng đều phải được bọc trong một gói tin Datagram của Tầng Mạng (Internet Protocol - IP) để định tuyến toàn cầu.*

**Câu 93:** Tại sao các truy vấn DNS thông thường hiếm khi bị lỗi dù sử dụng UDP (vốn không đáng tin cậy)?
A. Vì UDP trên thực tế có truyền lại.
B. Vì các hệ thống DNS thường đặt gần người dùng (Local DNS do ISP cấp) và tin nhắn DNS rất nhỏ (dễ lọt qua router), nên Tỷ lệ mất gói tự nhiên là cực kỳ thấp. Đồng thời, Ứng dụng DNS (Client) tự cài đặt Timeout truyền lại nội bộ của mình.
C. Vì DNS chạy cáp xịn.
D. Vì DNS được Chính phủ bảo vệ.
*Đáp án: B*
*Giải thích: UDP không có Timer, nhưng bản thân phần mềm DNS Client trên máy bạn có vòng lặp While chờ. Nếu 2 giây không thấy phản hồi UDP, phần mềm sẽ gọi gửi lại lệnh UDP khác.*

**Câu 94:** Khái niệm "Connection-oriented" (Hướng kết nối) của TCP nghĩa là gì?
A. Cắm dây mạng vào máy.
B. Cắm sạc pin.
C. Một phiên làm việc Lôgic (Virtual/Logic) được thiết lập, trong đó cả 2 máy tính dành ra một phần Bộ nhớ (RAM) để ghi nhớ Trạng thái của nhau (Sequence, Window, Buffers) trước khi trao đổi dữ liệu.
D. Dùng chung một Router.
*Đáp án: C*
*Giải thích: Khác với mạng chuyển mạch kênh (Circuit Switching - nối mạch điện thật), "Kết nối" của TCP chỉ là sự ghi nhớ bằng phần mềm (State) trong RAM của 2 Máy tính đầu cuối. Các Router ở giữa KHÔNG biết TCP đang kết nối.*

**Câu 95:** Trong đồ thị biểu diễn AIMD (Additive Increase, Multiplicative Decrease) của TCP, đường biểu diễn Tốc độ gửi (cwnd) thường có hình dạng gì?
A. Đường thẳng đứng.
B. Hình parabol.
C. Hình răng cưa (Sawtooth). Cứ tăng dần lên (Cộng) cho đến khi đụng trần gây mất gói, rồi tụt thẳng đứng xuống một nửa (Nhân/Chia 2), rồi lại bò từ từ lên.
D. Hình tròn khép kín.
*Đáp án: C*
*Giải thích: Đặc tính "Răng cưa" này là bản sắc kinh điển của TCP Reno, phản ánh quá trình liên tục "thăm dò" giới hạn mạng của máy tính.*

**Câu 96:** Lệnh TCP `RST` (Reset) gửi đi khi nào?
A. Khi vừa bắt đầu mở máy.
B. Máy nhận nhận được một Segment TCP đến một Cổng (Port) KHÔNG CÓ ứng dụng nào đang lắng nghe. Nó trả về RST để báo "Cổng này đóng, bỏ cuộc đi".
C. Báo hiệu thành công.
D. Xin cấp thêm IP.
*Đáp án: B*
*Giải thích: Đây là phản hồi cự tuyệt của TCP. Port Scanner của Hacker thường dò các Port, nếu nhận được RST, hacker biết cổng đó bị khóa.*

**Câu 97:** Thuật toán TCP "Cubic" (mặc định trên Linux hiện đại) cải tiến đường Răng cưa của TCP Reno như thế nào trên mạng tốc độ siêu cao?
A. Tăng băng thông mạng.
B. Không dùng răng cưa nữa mà đường cwnd tăng theo hàm Bậc 3 (Cubic). Khi bị tụt tốc độ, nó phình to CỰC KỲ NHANH về lại mốc cũ, rồi nằm "lì" (phẳng) lại ngay tại mốc đó để ổn định mạng, tránh rớt gói liên tục.
C. Biến thành TCP UDP.
D. Cấm TCP hoạt động.
*Đáp án: B*
*Giải thích: Trên đường truyền 10Gbps, nếu sập 1 nửa (5Gbps), TCP Reno tăng tuyến tính (+1) sẽ mất vài tiếng mới lấy lại được mốc 10Gbps. Cubic dùng hàm mũ 3 vọt lên lại trong nháy mắt.*

**Câu 98:** Đặc điểm nào của giao thức SCTP (Stream Control Transmission Protocol) mang tính lai tạp giữa UDP và TCP?
A. SCTP chạy bằng cáp đồng.
B. Cung cấp tính năng truyền đa luồng (Multi-streaming - tránh Head-of-line blocking giống HTTP/2) và Đa điểm (Multi-homing - một phiên có thể dùng nhiều IP) nhưng vẫn đảm bảo tính tin cậy như TCP, và theo định hướng gói tin (Message-oriented) như UDP.
C. SCTP biến hình thành IP.
D. Không dùng bảo mật.
*Đáp án: B*
*Giải thích: SCTP được thiết kế chủ yếu cho mạng Viễn thông di động (báo hiệu SS7 over IP), hiện nay được tái sử dụng trong WebRTC Data Channel.*

**Câu 99:** Chỉ báo "ECN" (Explicit Congestion Notification) là gì?
A. Tắt điện Router.
B. Gắn còi báo động vào cáp mạng.
C. Thay vì Máy gửi phải "Đoán" nghẽn mạng qua việc rớt gói tin (rất tốn kém). Các Router nếu thấy sắp tràn bộ đệm, sẽ đánh dấu một bit (CE) vào IP Header. Máy nhận thấy bit này sẽ báo cho Máy gửi giảm tốc ĐỂ KHÔNG BỊ RỚT gói nào.
D. Biển báo giao thông.
*Đáp án: C*
*Giải thích: ECN là sự kết hợp hiếm hoi giữa Tầng Mạng (Router) và Tầng Giao Vận (TCP). Router TỰ NÓI CHO PC biết "Tôi sắp nghẽn rồi, chậm lại đi" thay vì lẳng lặng vứt gói tin.*

**Câu 100:** Bạn đang lướt Web trên điện thoại di động (Wi-Fi), nhưng mạng của bạn rất yếu (chập chờn, lúc bắt được lúc không). Hiện tượng "TCP Timeout" diễn ra do Wi-Fi kém sẽ gây ảnh hưởng gì tới Tốc độ lướt web?
A. Làm tốc độ lướt web tăng lên.
B. Hệ thống coi Mất gói = Nghẽn mạng. Do đó TCP TỰ ĐỘNG bóp nghẹt tốc độ (cwnd) của bạn xuống cực thấp, khiến cho tốc độ đã yếu lại càng chậm thêm một cách thảm hại (dù Internet nhà bạn không hề bị ai dùng tranh).
C. Tự đổi sang 4G.
D. Điện thoại khởi động lại.
*Đáp án: B*
*Giải thích: Đây là nhược điểm chí mạng của TCP truyền thống trên môi trường Không dây (Wireless). Mất gói do "nhiễu sóng" bị hiểu nhầm là "Tắc nghẽn", làm thuật toán xử lý sai lầm (TCP BBR của Google ra đời sau này giúp khắc phục lỗi này).*

**Câu 101:** Đối với giao thức UDP, hệ điều hành (như Windows/Linux) phân bổ bao nhiêu Bộ đệm Gửi (Send Buffer) cho nó?
A. 10 GB.
B. Không có bộ đệm gửi thực sự (hoặc rất mỏng). Ứng dụng ném cục data xuống, UDP dán Header xong là đẩy thẳng xuống IP luôn, không cần giữ lại (vì không có cơ chế truyền lại).
C. Bộ đệm vô cực.
D. Bộ đệm lưu trên đám mây.
*Đáp án: B*
*Giải thích: Khác với TCP phải giữ lại bản sao của gói tin trong Send Buffer đợi cho đến khi có ACK. UDP đẩy xong là quên ngay.*

**Câu 102:** "Khóa phiên" (Session Hijacking) tấn công vào TCP bằng cách nào?
A. Rút cáp mạng máy chủ.
B. Kẻ tấn công đoán (hoặc sniff) được Số thứ tự (Sequence Number) và Số ACK hiện tại của một phiên kết nối đã xác thực, từ đó giả mạo gói tin IP nguồn và chèn lệnh điều khiển độc hại vào luồng TCP mà Server tưởng là Client thật gửi.
C. Tắt màn hình nạn nhân.
D. Gửi virus qua email.
*Đáp án: B*
*Giải thích: Việc HĐH sinh ra Số ISN (Initial Sequence Number) ban đầu phải thực sự ngẫu nhiên. Nếu ISN dễ đoán, hacker dễ dàng cướp phiên mà không cần mật khẩu.*

**Câu 103:** Thuật ngữ "DCC" trong mạng ngang hàng (Ví dụ BitTorrent) nghĩa là gì?
A. Mã hóa chuỗi khối.
B. Đầu nối cáp đồng.
C. Choke / Unchoke Algorithm (Thuật toán nghẽn). Cơ chế đánh giá xem peer nào tải lên cho mình tốt nhất để mở khóa (Unchoke) băng thông cho họ, phần thưởng cho sự đóng góp.
D. Màn hình điều khiển.
*Đáp án: C*
*Giải thích: Game Theory (Lý thuyết trò chơi) trong mạng P2P để loại bỏ những người ích kỷ.*

**Câu 104:** Lệnh Port Scanning có tên "TCP SYN Stealth Scan" (Quét ẩn danh nửa chừng) của công cụ Nmap hoạt động ra sao?
A. Gửi 1 gói Ping.
B. Hacker gửi gói SYN. Nếu Server trả SYN/ACK (nghĩa là Port mở), Hacker LẬP TỨC gửi gói RST để cắt đứt. Do không hoàn thành bước 3, Server sẽ không ghi Log sự kiện truy cập, giúp Hacker quét mà không bị lộ.
C. Nhắn tin qua Zalo.
D. Gửi email ẩn danh.
*Đáp án: B*
*Giải thích: Kỹ thuật trinh sát mạng kinh điển. Lợi dụng việc Hệ điều hành chỉ báo cáo lên Ứng dụng/File Log sau khi phiên TCP ESTABLISHED (Handshake 3 bước hoàn tất).*

**Câu 105:** Chức năng "Urgent Pointer" (Cờ URG) trong TCP Header có tác dụng gì?
A. Tăng băng thông cáp.
B. Đánh dấu một phần dữ liệu trong luồng byte là "Khẩn cấp" (Ví dụ tín hiệu Ctrl+C để ngắt lệnh Telnet), yêu cầu Máy nhận phải xử lý dữ liệu này ĐẦU TIÊN bỏ qua hàng đợi thông thường.
C. Nén hình ảnh khẩn cấp.
D. Mở máy tính từ xa.
*Đáp án: B*
*Giải thích: Dù có chức năng này, trong thực tiễn lập trình hiện đại Cờ URG rất ít khi được các HĐH và Ứng dụng thực hiện chuẩn xác, nên hiếm khi được sử dụng.*

**Câu 106:** Tại sao Header của UDP có trường "Length" (Độ dài) nhưng TCP Header thì không có trường chỉ thị độ dài tổng của Segment?
A. TCP dùng IP Length. TCP Header có trường "Header Length" để biết phần đầu dài bao nhiêu, còn phần cuối của Segment được Tự tính toán suy ra từ Độ dài của gói IP bọc ngoài nó. UDP có để thừa.
B. TCP gói tin luôn bằng nhau.
C. TCP không dùng kích thước.
D. Cáp quang tự đo chiều dài.
*Đáp án: A*
*Giải thích: Trong TCP: Payload Length = IP_Total_Length - IP_Header_Length - TCP_Header_Length. Dữ liệu Length của UDP thực ra dư thừa (RFC 768).*

**Câu 107:** Việc thiết lập giá trị MSS (Maximum Segment Size) trong lúc Handshake TCP có ý nghĩa gì?
A. Mật khẩu kết nối.
B. Máy A nói cho Máy B biết: "Khi anh gửi dữ liệu cho tôi, anh ĐỪNG nhét quá X bytes vào một gói TCP, vì Card mạng/Bộ đệm của tôi chỉ nuốt được ngần ấy thôi".
C. Đo tốc độ cáp.
D. Thay thế địa chỉ MAC.
*Đáp án: B*
*Giải thích: MSS thường được tính = MTU của mạng LAN đó - 40 bytes (IP+TCP). Đảm bảo gói TCP đi qua cáp LAN nhà mình không bị chia vụn (Phân mảnh IP).*

**Câu 108:** Tại sao ứng dụng Email (SMTP) không bao giờ sử dụng UDP?
A. UDP đòi hỏi cáp đồng.
B. Vì Email là dữ liệu văn bản/tệp đính kèm. Một ký tự bị mất hoặc lỗi có thể làm hỏng toàn bộ nội dung Hợp đồng, UDP không có cơ chế truyền lại sẽ làm mất thư.
C. SMTP bảo mật hơn UDP.
D. Tốc độ UDP chậm.
*Đáp án: B*
*Giải thích: Các ứng dụng truyền "Dữ liệu dạng Tệp" (File Transfer, Email, Web) đều xem "Sự toàn vẹn" là yếu tố số 1. Mất 1s hay 10s không quan trọng bằng Mất 1 chữ.*

**Câu 109:** Trong khái niệm Mạng, "Độ tin cậy" (Reliability) khác "Bảo mật" (Security) như thế nào?
A. Tin cậy là máy không virus.
B. Tin cậy (TCP) là đảm bảo mọi mảnh dữ liệu tới đích đủ, đúng thứ tự, không hỏng rác do lỗi đường truyền vật lý. Bảo mật (TLS/IPsec) là ngăn chặn con người nghe lén, sửa đổi ác ý dữ liệu.
C. Cả 2 là một.
D. Bảo mật dùng phần cứng, tin cậy dùng phần mềm.
*Đáp án: B*
*Giải thích: Giao thức TCP siêu đáng "tin cậy", nhưng nó truyền mật khẩu dạng Text "lộ thiên", không hề có một chút "bảo mật" nào.*

**Câu 110:** Giao thức Giao vận nào hỗ trợ chức năng "Phân mảnh và Lắp ráp" (Segmentation & Reassembly)?
A. UDP
B. ARP
C. TCP (Chia nhỏ dòng byte khổng lồ thành các Segment kích thước MSS và gửi đi, đầu kia ghép lại đúng thứ tự).
D. HTTP
*Đáp án: C*
*Giải thích: Ứng dụng gọi `send(10_Megabytes)`. Nó không thể nhét cái cục 10MB đó vào sợi cáp. TCP phải "băm" cái cục đó thành hàng ngàn gói 1460 Bytes để gửi.*

**Câu 111:** Thuật toán TCP BBR (Bottleneck Bandwidth and Round-trip propagation time) của Google khác biệt cơ bản nhất với TCP Reno/Cubic ở điểm nào?
A. TCP BBR dùng UDP.
B. TCP BBR không dùng Packet Loss (Mất gói) làm dấu hiệu nghẽn. Thay vào đó, nó liên tục đo đạc Băng thông thực tế và RTT. Khi thấy RTT bắt đầu tăng lên (Gói tin bắt đầu phải xếp hàng ở Router), nó chủ động giảm tốc độ gửi trước khi Router kịp vứt bỏ gói tin.
C. TCP BBR mã hoá cao hơn.
D. TCP BBR chạy trên cáp quang riêng.
*Đáp án: B*
*Giải thích: BBR cực kỳ hiệu quả trên đường truyền Mạng Di Động (Wi-Fi, 4G). Mất gói do sóng yếu không làm nó hiểu nhầm là kẹt xe, giúp tốc độ Youtube/Youtube trên điện thoại mượt mà hơn hẳn.*

**Câu 112:** TCP Tahoe (phiên bản cổ xưa) xử lý 3 ACK lặp (Triple Duplicate ACK) như thế nào?
A. Cắt đôi cwnd.
B. Tahoe cực kỳ bảo thủ, dù là Hết giờ (Timeout) hay 3 ACK lặp, nó đều coi là lỗi nghiêm trọng, đạp phanh (cwnd = 1) và bắt đầu lại Slow Start.
C. Tăng tốc độ gấp đôi.
D. Đóng kết nối lập tức.
*Đáp án: B*
*Giải thích: TCP Reno thông minh hơn Tahoe khi phân biệt được 2 loại lỗi. Reno thấy 3 ACK lặp thì chỉ áp dụng Fast Recovery (chia đôi cửa sổ) thay vì reset về 1.*

**Câu 113:** Khi bạn "Ping" 1 địa chỉ IP, nó hoạt động ở Tầng nào và sử dụng Cổng (Port) nào?
A. Tầng Ứng dụng, Port 80.
B. Tầng Giao vận, Port UDP 7.
C. Nằm gọn trong Tầng Mạng (Network Layer) sử dụng ICMP. ICMP không có khái niệm Số Cổng (Port) như TCP/UDP.
D. Tầng Vật lý.
*Đáp án: C*
*Giải thích: Packet ICMP Echo Request không chui vào Tầng Giao vận, nó nằm ngay trên lõi IP. Do đó câu hỏi "Mở port mấy để ping" là sai cơ bản.*

**Câu 114:** Ứng dụng DNS có thể dùng TCP không?
A. Cấm tuyệt đối.
B. Có, DNS thường dùng TCP (Port 53) cho các tác vụ cần truyền dữ liệu lớn (như Zone Transfer giữa các máy chủ DNS với nhau) hoặc khi Response UDP vượt quá 512 bytes và bị cắt xén (Truncated).
C. Chỉ dùng khi có cáp quang.
D. Chỉ dùng ở Mỹ.
*Đáp án: B*
*Giải thích: DNSSEC ra đời làm chìa khóa mã hóa rất lớn, Response hay bị phình to. Khi Client thấy cờ báo "Dữ liệu đã bị cắt xén do quá to" trong gói UDP, nó sẽ chủ động mở lại kết nối TCP để xin tải bản đầy đủ.*

**Câu 115:** Trong mạng nội bộ, Giao thức Tầng Giao vận có quan tâm đến Địa chỉ MAC không?
A. Không. Tầng Giao vận (TCP/UDP) chỉ tư duy ở mức Tiến trình-tới-Tiến trình (IP:Port), nó hoàn toàn mù tịt và không biết MAC là gì (Tầng Liên kết lo việc đó).
B. TCP lưu MAC vào Header.
C. UDP chạy dựa trên MAC.
D. Port và MAC là một.
*Đáp án: A*
*Giải thích: Sự đóng gói trừu tượng (Abstraction). Lập trình viên C# viết code Socket không bao giờ phải gõ địa chỉ MAC.*

**Câu 116:** Trong một kết nối TCP, "Cửa sổ gửi" (Send Window) thực tế được xác định như thế nào?
A. Do người dùng nhập tay.
B. Được lấy giá trị NHỎ HƠN giữa `rwnd` (Cửa sổ nhận báo về - Khả năng của Máy tính) và `cwnd` (Cửa sổ tắc nghẽn - Khả năng của Mạng).
C. Do ISP quyết định.
D. Do Router quy định.
*Đáp án: B*
*Giải thích: Cực kỳ logic. Nếu Máy mạnh (rwnd to) nhưng Mạng yếu (cwnd nhỏ) -> Gửi chậm theo Mạng. Nếu Mạng mạnh (cwnd to) nhưng Máy yếu (rwnd nhỏ) -> Gửi chậm theo Máy.*

**Câu 117:** Khái niệm "Delayed ACK" (ACK bị hoãn lại) trong TCP được thực hiện vì lợi ích gì?
A. Tăng bảo mật.
B. Máy nhận khi nhận 1 gói tin, sẽ KHÔNG GỬI ACK NGAY LẬP TỨC. Nó chờ khoảng 500ms, xem Ứng dụng có xuất dữ liệu phản hồi nào không, để "Cõng" (Piggyback) ACK đó vào gói Dữ liệu phản hồi luôn, giúp giảm số lượng gói tin độc lập (ACK rỗng) bay trên mạng.
C. Tránh bị hack.
D. Tránh hư card mạng.
*Đáp án: B*
*Giải thích: 1 gói ACK rỗng cõng 40 byte rác. 1 triệu gói ACK rỗng là 40MB rác. Delayed ACK giúp gom nhiều hành động vào 1 gói.*

**Câu 118:** Cờ "PSH" (Push) trong TCP Header có chức năng báo hiệu điều gì cho Hệ điều hành ở đầu nhận?
A. Mở máy tính (Wake-on-LAN).
B. Khi TCP thu thập được một lượng dữ liệu và đóng gói gửi đi với cờ PSH, Máy nhận khi thấy cờ này PHẢI LẬP TỨC đẩy đống dữ liệu này lên cho Ứng dụng (Trình duyệt) đọc, chứ không được giữ lại (Buffer) để chờ thêm dữ liệu.
C. Xóa dữ liệu.
D. Ngắt kết nối.
*Đáp án: B*
*Giải thích: Ứng dụng Chat (Zalo) gửi 1 chữ "A". Rất nhỏ. TCP muốn tiết kiệm băng thông thì nên đợi 1 phút có nhiều chữ rồi gửi. Nhưng App ra lệnh cờ PSH: "Đừng đợi, gửi ngay và báo bên kia đọc ngay cho tôi".*

**Câu 119:** Việc thiết kế thuật toán RDT 3.0 (Kênh truyền có Lỗi bit VÀ Mất gói) yêu cầu Sender phải gắn thêm thông tin gì cực kỳ cơ bản vào mỗi gói tin để Receiver phân biệt gói trùng lặp?
A. Kích thước gói.
B. Chữ ký số.
C. Một Số thứ tự luân phiên (Alternating Sequence Number, ví dụ gói 0, rồi gói 1, rồi lại gói 0).
D. Ngày giờ.
*Đáp án: C*
*Giải thích: Stop-and-wait RDT 3.0 (Giao thức Bit luân phiên) chỉ cần 1 bit làm Sequence (0 hoặc 1). Gửi 0 -> Chờ ACK 0. Gửi 1 -> Chờ ACK 1. Rất đơn giản nhưng giải quyết triệt để gói trùng lặp.*

**Câu 120:** Giao thức tầng Ứng dụng (như Web, Mail) dùng UDP hay TCP là do ai quyết định?
A. Hệ điều hành Windows/Linux.
B. Router mạng lõi.
C. Lập trình viên viết ra ứng dụng đó thiết kế (Code quyết định mở Socket loại nào).
D. ISP (VNPT/Viettel).
*Đáp án: C*
*Giải thích: Người xây App phải tự chọn. Nếu viết App Game cần nhanh -> Dùng UDP. Viết App Ngân hàng cần chuẩn -> Dùng TCP.*

**Câu 121:** Quá trình "Khởi động lại kết nối nhanh" (Fast Open) của TCP (TFO) hướng tới việc giảm thiểu thời gian gì?
A. Tắt máy tính.
B. Rút ngắn quá trình Handshake 3 bước cho các Kết nối ĐÃ TỪNG được thiết lập thành công trước đó giữa Client và Server (dùng một đoạn mã TFO Cookie), cho phép gửi Dữ liệu Web ngay ở bước SYN (tiết kiệm 1 RTT).
C. Tắt mở Router.
D. Reset Wi-Fi.
*Đáp án: B*
*Giải thích: Dành cho các trang web bạn vào liên tục mỗi ngày (như Facebook). Việc bắt tay 3 bước ở những lần sau được rút ngắn tối đa nhờ Server đã cấp cho bạn "Thẻ vào cửa quen" (Cookie) từ hôm qua.*

**Câu 122:** Lệnh `traceroute` sử dụng cơ chế nào để in ra tên/IP của các Router trung gian trên đường?
A. Ping thẳng vào Server.
B. Hacker khai thác cổng.
C. Gửi các gói UDP (hoặc ICMP) với TTL (Time-to-Live) tăng dần: 1, 2, 3... Khi Router thứ X nhận gói có TTL=1 (trừ đi thành 0), nó vứt bỏ và gửi ngược lại thông báo lỗi ICMP (Time Exceeded), từ đó máy gửi biết được IP của Router X.
D. Tra cứu bảng DNS nội bộ.
*Đáp án: C*
*Giải thích: Cách làm cực kỳ thông minh lợi dụng cơ chế báo lỗi có sẵn của IP để vẽ bản đồ đường đi.*

**Câu 123:** Khái niệm Tầng (Layer) sinh ra để giải quyết sự phức tạp. Ở Tầng Giao vận (Transport), "Sự phức tạp" nào của mạng đã bị CHE GIẤU đi?
A. Mã nguồn App bị che.
B. Máy khách và Máy chủ giao tiếp với nhau qua Socket như thể họ đang "nói chuyện trực tiếp trên một sợi cáp vô hình", không cần biết thông điệp phải chui qua cáp quang, vệ tinh, hay bị băm nhỏ qua 30 cái Router.
C. Lỗi màn hình.
D. Thiết bị hư hỏng.
*Đáp án: B*
*Giải thích: Logical Communication (Kết nối lô-gic). Lập trình viên tâng 7 chỉ biết gọi hàm Send(), mọi sự vất vả, dơ bẩn của bùn đất vật lý, định tuyến đều do các Tầng dưới lo liệu.*

**Câu 124:** Một gói tin TCP bị trùng lặp (Duplicate) có thể sinh ra trên mạng do nguyên nhân nào?
A. Do người dùng copy file.
B. Do lỗi sao chép của Router hoặc Máy gửi Timeout sớm hơn bình thường (trong khi gói thực tế không mất mà chỉ bị trễ), dẫn đến gửi thêm một bản sao giống hệt gói cũ.
C. Do dùng mạng 4G.
D. Do CPU quá nhanh.
*Đáp án: B*
*Giải thích: Sequence Number ở máy nhận sẽ loại bỏ được các bản sao rác này, tránh việc nội dung tải về bị nhân đôi lên.*

**Câu 125:** "Piggybacking" (Cõng) bị ảnh hưởng xấu bởi việc gì nếu ứng dụng máy nhận không có dữ liệu phản hồi ngay?
A. Cháy ổ cứng.
B. Lãng phí thời gian. Delay ACK bắt TCP phải chờ 500ms, nếu sau 500ms App vẫn im lặng, TCP buộc phải gửi đi một gói ACK "rỗng" tốn kém.
C. Sinh ra virus.
D. Mất kết nối Wi-Fi.
*Đáp án: B*
*Giải thích: Delay ACK chỉ tốt nếu 2 bên "Chat" qua lại liên tục. Nếu một bên chỉ Tải (Tải file từ Web), thì chờ 500ms chả có ý nghĩa gì vì máy tải đâu có định gửi lại Web Dữ liệu gì (chỉ gửi ACK).*

**Câu 126:** Kỹ thuật "Port Address Translation" (PAT / NAT Overload) trên Router nhà phân biệt các luồng dữ liệu của nhiều máy tính trong nhà (cùng truy cập Internet) dựa vào đâu?
A. Địa chỉ MAC.
B. Kích thước màn hình.
C. Nó gán cho mỗi luồng kết nối của từng máy tính một Cổng nguồn (Source Port) khác nhau trên IP Public duy nhất của Router. Khi Web trả về cái Port đó, Router dò bảng NAT và trả lại đúng IP máy tính nội bộ.
D. Tên miền.
*Đáp án: C*
*Giải thích: PC1 vào web (Router gán Port 5001). PC2 vào web (Router gán Port 5002). Gói trả về vào cổng 5001 thì Router đẩy thẳng vào PC1.*

**Câu 127:** Trong hệ thống thông tin di động, nếu 1 người dùng chuyển từ trạm phát (Cell) 3G này sang 4G khác, làm thay đổi địa chỉ IP. Kết nối TCP đang tải dở file của họ có bị đứt không?
A. TCP sẽ tự động chạy tiếp.
B. Có, TCP định danh bằng 4-tuple (trong đó có IP Nguồn). Nếu IP Nguồn thay đổi giữa chừng, Máy chủ Web sẽ không nhận ra phiên cũ, kết nối TCP BỊ ĐỨT (Phải lập kết nối TCP mới).
C. Không đứt vì dùng MAC.
D. Chuyển sang FTP.
*Đáp án: B*
*Giải thích: Đây là một vấn đề với TCP trên thiết bị di động (Mobility). QUIC khắc phục điều này bằng Connection ID riêng (không phụ thuộc IP), bạn từ Wi-Fi sang 4G tải Youtube vẫn mượt.*

**Câu 128:** Trong đồ thị AIMD, quá trình "Giảm nhân" (Multiplicative Decrease) chứng tỏ đặc tính nhường nhịn (Altruism) của TCP. Ý nghĩa là gì?
A. TCP không bao giờ nhường nhịn.
B. Khi một gói mất -> Báo hiệu mạng đang bắt đầu kẹt. TCP cắt phăng 1/2 tốc độ để lập tức xả xú-páp cho các Router, nhường không gian cho các người dùng khác cùng sống sót.
C. Chỉ giảm tốc độ khi hết tiền mạng.
D. Giảm tốc độ để tải video HD.
*Đáp án: B*
*Giải thích: Nếu TCP tham lam không chịu giảm, mạng sẽ sập toàn tập (Congestion Collapse) như những năm 1980.*

**Câu 129:** Đơn vị PDU (Protocol Data Unit) nào là chính xác cho các Tầng TCP/IP theo thứ tự: Application -> Transport (TCP) -> Network -> Link?
A. Message -> Datagram -> Frame -> Segment
B. Message -> Segment -> Datagram/Packet -> Frame
C. Frame -> Packet -> Segment -> Bits
D. Data -> Bits -> Packet -> Frame
*Đáp án: B*
*Giải thích: Đây là thứ tự chuẩn danh pháp phải thuộc lòng trong kiến trúc mạng.*

**Câu 130:** Trong thuật toán RDT 2.2, trạng thái (State) của Sender có thêm phần "Chờ đợi ACK 0" hoặc "Chờ đợi ACK 1". Tại sao Receiver phải dán số 0/1 vào ACK?
A. Để trang trí.
B. Sender phải biết cái ACK vừa đến (có thể là ACK rác đến trễ từ lượt cũ) là để Xác nhận cho CÁI GÓI TIN 0 hiện tại hay gói tin 1 trước đó.
C. Để tính cước mạng.
D. Dùng làm ID cho gói IP.
*Đáp án: B*
*Giải thích: RDT phải được thiết kế đối phó với những gói tin lặp hoặc ACK đến muộn một cách vô lý trên mạng. Sequence trên ACK giúp đồng bộ tuyệt đối.*

**Câu 131:** Trong kiểm soát tắc nghẽn TCP (ví dụ TCP Tahoe), khi xảy ra "Timeout" (hết hạn thời gian chờ ACK), biến trạng thái ssthresh (Slow Start Threshold) sẽ được cập nhật như thế nào?
A. Tăng lên gấp đôi.
B. ssthresh = cwnd / 2 (Một nửa kích thước cửa sổ hiện tại ngay trước khi rớt mạng).
C. Không thay đổi.
D. Giảm về 1 MSS.
*Đáp án: B*
*Giải thích: ssthresh lưu lại mốc "an toàn" của mạng. Nếu đang chạy 100 gói mà rớt mạng, ssthresh sẽ đặt lại là 50. Ở vòng lặp sau, TCP sẽ chạy đua (nhân đôi) lên tới 50 là dừng, bắt đầu dò dẫm từng gói một.*

**Câu 132:** UDP Header không có số tuần tự (Sequence Number). Vậy ứng dụng Video Streaming (dùng UDP) giải quyết việc các khung hình video đến sai thứ tự (Frame 3 đến trước Frame 2) như thế nào?
A. Không làm gì cả, video sẽ bị ngược hình.
B. Đẩy việc này lên Tầng Ứng dụng. Giao thức ứng dụng (ví dụ RTP - Real-time Transport Protocol) sẽ tự chèn Sequence Number và Timestamp (Nhãn thời gian) vào Payload gửi đi, để Trình phát Video tự sắp xếp lại.
C. UDP tự xin thêm Sequence Number từ TCP.
D. Chạy qua thuật toán Router nội bộ.
*Đáp án: B*
*Giải thích: UDP giống phong bì trống. RTP bỏ đồ vào phong bì và tự viết số thứ tự ngoài phong bì. Transport Layer (UDP) mù không biết, nhưng Application Layer (Video Player) sẽ đọc được số thứ tự đó.*

**Câu 133:** TCP Reno khác với TCP Tahoe chủ yếu ở cơ chế nào?
A. TCP Reno không dùng Checksum.
B. Cơ chế Fast Recovery (Phục hồi nhanh). Reno không bao giờ đạp thắng về 0 khi có 3 ACK trùng lặp, nó chỉ chia đôi cửa sổ rồi chạy tiếp.
C. Cả 2 đều dùng UDP ẩn.
D. TCP Reno không có Slow Start.
*Đáp án: B*
*Giải thích: TCP Reno là chuẩn chung của mạng rất nhiều năm. Tahoe bị thay thế vì đạp thắng quá sâu về số 0 làm rớt băng thông quá lâu.*

**Câu 134:** Cấu trúc cửa sổ trượt (Sliding Window) được thiết kế nhằm mục đích gì cho cả Máy gửi và Máy nhận?
A. Tăng kích thước bộ nhớ ổ cứng.
B. Nó là danh sách đánh dấu liên tục các gói đã gửi chưa được ACK, các gói được phép gửi, nhằm giới hạn số gói tin bay trên mạng và kiểm soát luồng đồng bộ.
C. Thay thế màn hình hiển thị.
D. Sắp xếp cáp theo thứ tự.
*Đáp án: B*
*Giải thích: Cửa sổ trượt giống như khung ngắm, Máy gửi chỉ được gửi các gói nằm trong khung ngắm đó. Khi gói cũ nhất được ACK, khung sẽ trượt về bên phải để ăn gói mới.*

**Câu 135:** Bảng định tuyến (Forwarding table) của Router mạng lõi KHÔNG CÓ cột thông tin nào dưới đây?
A. IP Subnet Đích.
B. Cổng ra (Outgoing Interface).
C. Cổng TCP/UDP Đích (Destination Port).
D. Giao thức định tuyến (OSPF/BGP).
*Đáp án: C*
*Giải thích: Router lõi thuần tuý (Layer 3) CHỈ quan tâm đến IP để dẫn đường. Chỉ Tường lửa (Firewall) hoặc NAT Router ở Biên mới mở sâu gói tin ra để đọc Port (Layer 4).*

**Câu 136:** Tấn công "UDP Flood" nguy hiểm vì nó lợi dụng đặc điểm gì của UDP?
A. Cấu trúc quá phức tạp.
B. Tính phi kết nối. Máy gửi có thể sinh ra hàng triệu gói UDP giả IP nguồn với tốc độ tối đa của chip mạng mà không cần chờ Server gật đầu xác nhận kết nối, làm ngập lụt băng thông đích ngay lập tức.
C. Giao thức này bắt buộc phải giải mã SSL.
D. Nó tự nhân bản mã độc.
*Đáp án: B*
*Giải thích: Khác với TCP yêu cầu Handshake (Hacker phải dùng IP thật mới nhận được ACK để tấn công), UDP cho phép "Ném đá giấu tay" không tốn thời gian chờ.*

**Câu 137:** Chức năng "Congestion Avoidance" (Tránh tắc nghẽn) trong TCP hoạt động bằng cách:
A. Tắt card Wi-Fi.
B. Tăng cwnd lên 1 MSS mỗi khi TẤT CẢ các gói tin trong một Cửa sổ (Window/1 RTT) được ACK thành công, tăng tốc độ một cách từ từ tuyến tính.
C. Phóng đại gói TCP.
D. Nén Header IP.
*Đáp án: B*
*Giải thích: Đây là quá trình dò tìm sườn dốc một cách cẩn thận. Thay vì nhảy vọt x2 như Slow Start, nó chỉ thêm +1 gói vào mỗi chuyến xe tải gửi đi.*

**Câu 138:** TCP thiết lập một kết nối 3 bước, vì vậy Máy chủ Web (Server) phải duy trì trạng thái của bao nhiêu Kết nối TCP (Session)?
A. Chỉ 1 cho mọi người dùng.
B. Tương ứng đúng bằng số lượng Client đang kết nối tới (Mỗi phiên là một bộ Buffer và Biến trạng thái riêng trong RAM máy chủ).
C. Chỉ lưu trữ trong 5 phút đầu.
D. Luôn là 65535 phiên.
*Đáp án: B*
*Giải thích: 10,000 người vào Web = 10,000 cái Sockets (TCP Sessions) mở trong RAM Server. Đây gọi là "Trạng thái nặng" (Heavy State), dễ dẫn đến cạn kiệt RAM (Lỗi C10K).*

**Câu 139:** Giá trị Timeout của giao thức TCP được tính toán qua công thức hàm lấy mẫu theo hàm mũ (Exponential Weighted Moving Average - EWMA) nhằm mục đích gì?
A. Thay thế cho Checksum.
B. Làm "Mịn" (Smooth) độ dao động RTT của mạng. Các độ trễ RTT thất thường (Spike) do nghẽn đột xuất sẽ ít làm sai lệch giá trị Timeout trung bình ổn định của hệ thống.
C. Đảm bảo tốc độ CPU ổn định.
D. Nén ảnh chất lượng cao.
*Đáp án: B*
*Giải thích: Mạng giật 1 phát vọt ping lên 500ms, nếu TCP tin ngay lập tức thì Timeout sẽ rất to. Hàm EWMA lấy trung bình có trọng số (ưu tiên lịch sử) giúp Timeout ổn định hơn.*

**Câu 140:** Khi Máy gửi đang chờ phản hồi, nó nhận được các thông báo: ACK 10, ACK 10, ACK 10 (Fast Retransmit). Điều gì đang xảy ra bên phía Máy nhận?
A. Máy nhận bị sập nguồn.
B. Máy nhận đã nhận được đầy đủ dữ liệu đến Byte số 9. Nhưng nó đang nhận được các gói từ số 11 trở đi (Bị nhót mất đoạn 10). Mỗi lần nhận gói lệch thứ tự (11, 12, 13), nó đều gào lên (ACK 10) để đòi Máy gửi gửi lại gói 10.
C. Gói 10 đã thành công tuyệt đối.
D. Máy gửi đóng kết nối.
*Đáp án: B*
*Giải thích: Máy nhận có thái độ "Trẻ con đòi quà": Nếu chưa cho tôi kẹo số 10, anh có đưa kẹo 11, 12 tôi vẫn chỉ khóc đòi "Tôi muốn số 10". Tiếng khóc đó chính là Duplicate ACKs.*

**Câu 141:** Trong thiết kế RDT 2.0, tín hiệu "NAK" (Negative Acknowledgment - Phủ nhận) có chức năng gì?
A. Cấp lại IP động.
B. Báo cho Máy gửi biết gói tin vừa đến BỊ HỎNG DỮ LIỆU (sai Checksum), yêu cầu gửi lại.
C. Chuyển tiền từ thẻ tín dụng.
D. Hủy bỏ truyền file.
*Đáp án: B*
*Giải thích: TCP thực tế không dùng NAK. TCP chỉ dùng ACK (Nếu hỏng nó im lặng không gửi ACK, hoặc gửi lại ACK cũ). RDT 2.0 sinh ra NAK để xây dựng mô hình lý thuyết máy tính.*

**Câu 142:** "Maximum Transmission Unit" (MTU) phụ thuộc vào công nghệ truyền tải của Tầng nào?
A. Tầng Ứng dụng.
B. Tầng Giao vận.
C. Tầng Liên kết dữ liệu (Data Link Layer - ví dụ chuẩn Ethernet LAN hoặc Wi-Fi).
D. Tầng Trình diễn.
*Đáp án: C*
*Giải thích: MTU là "Kích cỡ thùng xe tải" của thiết bị phần cứng Ethernet. Tầng Giao vận (TCP) phải ngoan ngoãn chia nhỏ hàng hoá (MSS) theo cái thùng xe này.*

**Câu 143:** Cờ "SYN" chiếm một Số thứ tự ảo (Sequence number) trong chuỗi dòng Byte. Lệnh đóng kết nối "FIN" có chiếm không?
A. Có, FIN cũng chiếm một số thứ tự trong không gian dòng Byte để Máy nhận có thể Xác nhận (ACK) việc đóng mạch một cách tin cậy.
B. Không, FIN không chiếm Byte nào.
C. Tùy thuộc vào tốc độ mạng.
D. UDP tự cung cấp số này.
*Đáp án: A*
*Giải thích: SYN và FIN tuy không có Dữ liệu thực, nhưng TCP tính chúng bằng 1 Byte "Ảo" để có số đếm mà gửi ACK về. Việc này đảm bảo Lệnh mở/đóng không bao giờ bị mất trên mạng.*

**Câu 144:** Cổng mặc định của giao thức HTTPS bảo mật là:
A. 80 TCP
B. 443 TCP
C. 443 UDP
D. 21 TCP
*Đáp án: B*
*Giải thích: Mọi kết nối đến Web có ổ khóa (SSL/TLS) đều mặc định cắm vào cổng số 443 của Web Server.*

**Câu 145:** Hiện tượng "Silly Window Syndrome" xuất phát từ ĐẦU GỬI (Sender) có thể do Ứng dụng sinh ra từng Byte dữ liệu một. Giải pháp Thuật toán Nagle khắc phục bằng cách nào?
A. Từ chối ứng dụng.
B. Nếu lượng dữ liệu trong Buffer gửi nhỏ hơn MSS và vẫn chưa nhận được ACK của gói gửi trước đó, TCP sẽ TẠM GIỮ dữ liệu đó lại trong Buffer (đợi gom thêm) thay vì gửi ngay gói tin nhỏ xíu lên mạng.
C. Sinh thêm gói rác cho to.
D. Phóng to cửa sổ nhận.
*Đáp án: B*
*Giải thích: Nagle ép dòng nước nhỏ giọt thành một gáo nước đầy rồi mới hất đi, làm giảm 99% lượng gói rác trên mạng.*

**Câu 146:** Phương pháp "Selective Repeat" (SR) trong RDT sử dụng cơ chế đếm ngược (Timer) như thế nào?
A. MỘT Timer duy nhất cho toàn bộ cửa sổ (GBN).
B. MỖI GÓI TIN ĐƯỢC GỬI ĐI đều có một Timer RIÊNG BIỆT độc lập. Gói nào quá hạn thì truyền lại đúng gói đó.
C. Timer đồng bộ với đồng hồ thế giới.
D. Chạy Timer bằng ICMP.
*Đáp án: B*
*Giải thích: SR cực kỳ tối ưu nhưng tốn bộ nhớ vì phải quản lý hàng trăm cái Timer đếm ngược chạy song song trên RAM máy phát.*

**Câu 147:** Ứng dụng VPN (Ví dụ OpenVPN) thường cung cấp tùy chọn chạy qua UDP hoặc TCP. Chạy qua TCP gặp một rào cản kỹ thuật chết người nào khiến người ta hay ưu tiên UDP cho VPN?
A. TCP không bảo mật.
B. Lỗi "TCP Meltdown" (TCP qua TCP). Nếu kết nối VPN (TCP ngoài) bị rớt mạng làm tăng Timeout, TCP của Trình duyệt bên trong cũng tăng Timeout và truyền lại, tạo ra vòng lặp tắc nghẽn, triệt tiêu tốc độ.
C. Trình duyệt không chạy trên TCP.
D. UDP đổi được MAC.
*Đáp án: B*
*Giải thích: Đóng gói 1 xe tải chở hàng (TCP trong) lên 1 xe chở container (TCP ngoài) là thảm họa vì 2 thằng tài xế đều đạp phanh ngẫu nhiên.*

**Câu 148:** Số cổng ngẫu nhiên (Ephemeral Ports) do Hệ điều hành cấp phát cho Client thường nằm trong khoảng dải số nào theo tiêu chuẩn của IANA?
A. Từ 0 đến 1023
B. Từ 1024 đến 49151 (Registered Ports)
C. Từ 49152 đến 65535 (Dynamic/Private Ports)
D. Hàng triệu số không đếm được.
*Đáp án: C*
*Giải thích: Máy cá nhân bạn vào lướt Facebook thì Windows sẽ bốc ngẫu nhiên số kiểu `60124` làm cổng nguồn của Trình duyệt Chrome.*

**Câu 149:** Trong môi trường Data Center (Mạng nội bộ 100Gbps, trễ cực thấp dưới 1ms), người ta đôi khi ưu tiên sử dụng giao thức UDP cho các dịch vụ lưu trữ (ví dụ NFS over UDP, Memcached) vì sao?
A. Dễ lập trình hơn.
B. TCP mang lại sự nặng nề không cần thiết (Overhead bắt tay, Slow Start, cửa sổ trượt). Trong môi trường mạng siêu sạch, kín, không rớt gói, UDP (bắn thẳng dữ liệu) mang lại hiệu năng cao nhất, ít tiêu tốn CPU Server nhất.
C. Tăng bảo mật mạng.
D. Không dùng cáp quang.
*Đáp án: B*
*Giải thích: Ở nơi "nhà giàu" (mạng kín 100Gbps, không đụng độ), đồ bảo hộ (TCP) đôi khi làm chậm tiến độ thi công. UDP thô và trần trụi được tận dụng tối đa.*

**Câu 150:** Đặc tính "Kết nối hướng điểm-điểm" (Point-to-Point) của TCP có nghĩa là:
A. Thiết bị bắt buộc cắm cáp chéo.
B. TCP CHỈ hỗ trợ kết nối Unicast giữa chính xác 2 Máy tính (1 Gửi - 1 Nhận). TCP KHÔNG THỂ cung cấp dịch vụ Broadcast hoặc Multicast (1 Gửi - Nhiều Nhận) giống như UDP.
C. TCP gửi song song đa điểm.
D. Nó là cáp đồng trục.
*Đáp án: B*
*Giải thích: TCP phải đảm bảo trạng thái State của máy đối diện (Bắt tay 3 bước). Một cái máy chủ không thể "bắt tay" cùng lúc 1 cú sinh ra phiên kết nối cho 1000 người (mỗi người 1 Window/Seq riêng).*

**Câu 151:** Trong kiến trúc Client-Server, một máy chủ Web (Server) đang Lắng nghe (Listen) ở cổng 80. Khi 100 máy khách (Client) kết nối tới, Máy chủ web này sử dụng bao nhiêu Cổng (Port) vật lý để giao tiếp với 100 khách?
A. Phải mở 100 cổng ngẫu nhiên khác nhau.
B. Chỉ dùng DUY NHẤT một Cổng TCP số 80. Hệ điều hành máy chủ phân biệt 100 kết nối độc lập đó dựa trên 100 cặp (IP Nguồn, Port Nguồn) khác nhau của các khách hàng.
C. Bắt buộc dùng 100 card mạng.
D. Dùng cổng 443.
*Đáp án: B*
*Giải thích: Port 80 là cái Biển Hiệu. Còn phía sau là 100 đường ống luồng dữ liệu độc lập (Sockets).*

**Câu 152:** Thuật toán TCP Tahoe và Reno đều sử dụng biến số `ssthresh` (Slow Start Threshold). Ý nghĩa của `ssthresh` là:
A. Là kích thước cửa sổ nhận `rwnd`.
B. Là ngưỡng giới hạn của băng thông cáp vật lý.
C. Là một mốc "Kinh nghiệm". Dưới mốc này, TCP tăng tốc MẠNH (Cấp số nhân - Slow Start). Trên mốc này, TCP tăng tốc CHẬM (Tuyến tính - Congestion Avoidance) vì đoán là sắp đụng trần nghẽn.
D. Cờ đánh dấu mở kết nối.
*Đáp án: C*
*Giải thích: TCP ghi nhớ lại điểm nó vừa vấp ngã (bằng nửa tốc độ cũ), và chọn điểm đó làm mốc thay đổi chiến thuật thăm dò.*

**Câu 153:** Khi máy tính gửi 1 gói TCP Segment, nếu sau một thời gian Timer chưa kịp đếm xong mà gói đó ĐÃ VỀ đích và được ACK, Timer sẽ:
A. Ngưng và đặt lại (Reset) để bắt đầu đếm cho gói gửi tiếp theo.
B. Tiếp tục đếm đến 0 rồi báo lỗi.
C. Gửi NAK.
D. Trở thành RTT.
*Đáp án: A*
*Giải thích: Máy gửi liên tục thiết lập/Reset Timer mỗi khi có gói mới đi hoặc ACK về để theo dõi luồng lưu thông nhịp nhàng.*

**Câu 154:** Tại tầng Giao vận (Transport Layer), yếu tố nào dưới đây KHÔNG NẰM trong phạm vi hoạt động của giao thức này?
A. Cổng (Port).
B. Định tuyến (Routing - quyết định gói tin đi rẽ trái hay rẽ phải ở một nút giữa mạng).
C. Số thứ tự (Sequence Number).
D. Cửa sổ trượt (Sliding Window).
*Đáp án: B*
*Giải thích: Định tuyến (Routing) hoàn toàn là trách nhiệm của Tầng Mạng (Network Layer - IP).*

**Câu 155:** Mã lệnh `recv()` hoặc `read()` trong lập trình Socket của ứng dụng dùng để làm gì?
A. Gửi dữ liệu ra cáp quang.
B. Yêu cầu Hệ điều hành khởi động máy tính từ xa.
C. Yêu cầu Tầng Giao vận (Hệ điều hành) Bốc dữ liệu (đã đến và được xác nhận xong) từ Bộ nhớ đệm Nhận (Receive Buffer) đưa lên cho Ứng dụng xử lý.
D. Đóng cổng Port.
*Đáp án: C*
*Giải thích: Nếu App của bạn lười gọi `recv()` (Máy đơ/CPU kẹt), Buffer sẽ đầy, lúc đó rwnd của TCP sẽ giảm về 0 báo hiệu "Khách nhà tôi ngập việc rồi, đừng gửi nữa".*

**Câu 156:** Tính năng TCP BBR (Bottleneck Bandwidth and RTT) cố gắng giữ cho "Hàng đợi" (Queue) tại Router ở trạng thái nào?
A. Luôn chứa 1 triệu gói tin.
B. Rỗng (Hoặc tối thiểu nhất có thể). BBR chỉ bơm vào mạng một tốc độ BẰNG ĐÚNG với Tốc độ Nút thắt (Bottleneck Bandwidth), giữ mạng ở điểm cân bằng, không làm phình to bộ đệm Router (Giảm thiểu Bufferbloat).
C. Tràn bộ đệm liên tục.
D. Xóa toàn bộ hàng đợi.
*Đáp án: B*
*Giải thích: Các bản TCP cũ (Reno/Cubic) nhồi data để "Lấp đầy" hàng đợi cho tới khi đứt. BBR nhồi data để "Lấp đầy" ống cáp quang, nhưng không nhét thêm vào Router, giúp duy trì RTT tối thiểu.*

**Câu 157:** Hiện tượng Bufferbloat (Phình to bộ đệm) ở Router gia đình do dùng TCP cũ gây ra tác hại gì cho bạn khi đang chơi Game (ví dụ: Liên minh huyền thoại)?
A. Game chạy mượt hơn.
B. Băng thông tăng gấp 10.
C. Nếu ai đó trong nhà tải file IDM, TCP tải file sẽ nhét đầy cứng cái Bộ đệm siêu to của Router. Gói UDP của Game sẽ phải XẾP HÀNG chờ cả giây trong Router mới được đẩy đi, làm Ping trong game vọt lên 1000ms.
D. Sập mạng Wi-Fi ngay lập tức.
*Đáp án: C*
*Giải thích: Buffer to không phải là tốt. Nó triệt tiêu Packet Loss nhưng đánh đổi bằng việc tăng Độ trễ cực cao (High Jitter/Ping spikes).*

**Câu 158:** Một TCP Segment có cờ SYN = 1, ACK = 1 (Bước 2 của Handshake). Nó thực hiện nhiệm vụ gì?
A. Yêu cầu máy chủ tắt.
B. Báo lỗi mật khẩu web.
C. Máy chủ (Server) vừa xác nhận lại tín hiệu mở kết nối của Client (ACK), vừa đưa ra đề nghị Số thứ tự đồng bộ từ phía Server (SYN) để thiết lập luồng ngược lại.
D. Chấm dứt TCP.
*Đáp án: C*
*Giải thích: Do tính Song công toàn phần (Full-duplex), TCP thực chất là 2 đường ống độc lập. Client báo mở ống 1 (SYN 1). Server đồng ý ống 1 (ACK 1), báo mở ống 2 (SYN 2).*

**Câu 159:** Một Socket UDP nhận một Datagram đến. Nó dựa vào thông tin gì duy nhất để đưa cho Ứng dụng?
A. Cổng Nguồn (Source Port).
B. Cổng Đích (Destination Port).
C. Tên File.
D. Địa chỉ MAC đích.
*Đáp án: B*
*Giải thích: Khác với TCP phải nhìn đủ 4 tham số. UDP ngốc nghếch hơn, hễ gói tin có Đích là Cổng 53 (DNS) thì nó ném thẳng vào Ứng dụng DNS đang mở, không cần biết gói đó từ IP nào đến.*

**Câu 160:** Cấu trúc TCP Checksum có khả năng phát hiện độ dài lỗi (Error detection) ở mức độ nào?
A. Đảm bảo an toàn mật mã học chống Hacker sửa đổi (Như SHA-256).
B. Nó chỉ là phép Cộng Bù 1 (1's complement sum) khá thô sơ. Giúp phát hiện các nhiễu điện từ, lật bit ngẫu nhiên tự nhiên (Noise), nhưng không thể chống lại tin tặc cố tình làm giả Checksum hợp lệ.
C. Phát hiện sai đường link URL.
D. Tránh Virus lây lan.
*Đáp án: B*
*Giải thích: Đừng nhầm lẫn Error Detection (Sửa lỗi Vật lý) với Cryptographic Hash (Bảo mật Tầng Ứng dụng). Hacker giỏi thừa sức sửa nội dung gói TCP và sửa lại Checksum cho khớp.*

**Câu 161:** Điều kiện nào khiến Tầng Ứng dụng TỰ XÂY DỰNG cơ chế Truyền lại trên nền UDP thay vì dùng luôn TCP?
A. Lập trình viên thích phức tạp.
B. Không hỗ trợ Win XP.
C. Khi ứng dụng (như HTTP/3 QUIC) muốn loại bỏ độ trễ Handshake của TCP, nhưng VẪN MUỐN TÍNH TIN CẬY; hoặc khi nó muốn kiểm soát tuyệt đối thời gian truyền mà không bị Hệ điều hành can thiệp (TCP).
D. Vì cáp đồng trục rẻ hơn cáp quang.
*Đáp án: C*
*Giải thích: Lập trình TCP giống như bạn thuê Taxi tự động hoàn toàn, rất nhàn nhưng không can thiệp được phanh/ga. Nếu bạn tự xây RDT trên nền UDP, bạn có chiếc xe Số Sàn, khó lái nhưng chủ động tối đa.*

**Câu 162:** Giao thức Giao vận nào hỗ trợ truyền dữ liệu theo Đa đường (Multipath) ở cùng một thời điểm để tăng băng thông (Ví dụ: dùng cả Wi-Fi và 4G đồng thời trên điện thoại)?
A. UDP chuẩn.
B. MPTCP (Multipath TCP) - bản mở rộng hiện đại của TCP.
C. ICMP.
D. DNS.
*Đáp án: B*
*Giải thích: Apple Siri (Siri của iOS) tiên phong dùng MPTCP. Dù bạn đi từ nhà (Wi-Fi) ra đường (4G), kết nối không đứt mà được ghép luồng liền mạch.*

**Câu 163:** Kỹ thuật "Hole Punching" (UDP) dựa vào hành vi nào của thiết bị NAT/Tường lửa gia đình?
A. Xóa ổ cứng NAT.
B. Khi một máy tính trong nhà (A) chủ động gửi một gói tin UDP ra ngoài (cho B), NAT sẽ ghi nhớ và TẠO MỘT LỖ MỞ trên Firewall (ánh xạ Cổng). Nếu B gửi ngược gói tin vào ĐÚNG CÁI LỖ CỔNG đó trong một thời gian ngắn, NAT sẽ cho đi qua.
C. Dịch tên miền thành IP.
D. Đổi MAC nội bộ.
*Đáp án: B*
*Giải thích: Đây là cách P2P "Lách luật" NAT để kết nối máy nhà với máy nhà, không cần qua Server tốn tiền băng thông.*

**Câu 164:** Các dịch vụ Streaming Video sử dụng TCP thì bị mắc một lỗi khó chịu gì nếu mạng có hiện tượng mất gói ngẫu nhiên nhưng rất ít (1%)?
A. Rớt mạng.
B. Chặn địa chỉ MAC.
C. Hiện tượng Jitter giả (Head-of-Line blocking). Mất 1 gói tin TCP làm TẤT CẢ các khung hình video đằng sau gói đó bị HĐH giữ lại trong Buffer (để chờ truyền lại) dù chúng đã đến đích. Ứng dụng Video không có hình để vẽ, gây ra vòng xoay Buffering.
D. Nén nhầm video thành mp3.
*Đáp án: C*
*Giải thích: Đây là cái "Máy móc" của TCP. HĐH luôn bắt Trình duyệt đợi "phải đủ tuần tự tôi mới giao". Dù Trình duyệt muốn nói "Kệ cái khung hình lỗi đó, đưa khúc sau đây để chiếu đi" thì TCP cũng không cho.*

**Câu 165:** Giao thức tầng Ứng dụng "WebRTC" (dùng cho Video call thẳng trên Trình duyệt) sử dụng tập giao thức Giao vận nào?
A. Chạy trên cáp quang riêng.
B. Chủ đạo là UDP (kết hợp với SCTP/DTLS/SRTP) để đảm bảo độ trễ thấp tối đa.
C. Chỉ dùng TCP cổng 80.
D. Không dùng giao thức nào.
*Đáp án: B*
*Giải thích: Gọi Google Meet (WebRTC) cực kỳ mượt và trễ thấp (Low latency) là nhờ sức mạnh của UDP, bỏ qua TCP hoàn toàn để giải quyết lỗi của Câu 164.*

**Câu 166:** "Maximum Segment Lifetime" (MSL) trong trạng thái TIME_WAIT của TCP là gì?
A. Thời gian sống của con người.
B. Là thời gian ước tính Tối đa mà một gói tin IP (cùng các bản sao trễ nải của nó) có thể tồn tại lang thang trên mạng lưới Internet trước khi bị các Router tiêu hủy (TTL = 0).
C. Chiều dài dây mạng.
D. Dung lượng RAM lớn nhất.
*Đáp án: B*
*Giải thích: TIME_WAIT yêu cầu Port phải chờ xấp xỉ 2 lần thời gian MSL này để đảm bảo toàn mạng Internet đã sạch bóng rác cũ của phiên đó.*

**Câu 167:** Phương thức truyền TCP "Half-Close" xảy ra khi:
A. Mở máy tính một nửa.
B. Rút cáp mạng.
C. Một bên (Ví dụ Client) gửi cờ FIN báo hiệu "Tôi không GỬI dữ liệu nữa", nhưng nó VẪN MỞ để tiếp tục NHẬN dữ liệu do Server chưa gửi xong.
D. Tắt Router đột ngột.
*Đáp án: C*
*Giải thích: Sự linh hoạt của Full-duplex. Một đường ống xả cạn và khoá lại, nhưng đường ống kia vẫn bơm.*

**Câu 168:** TCP "Keep-Alive" (Probe packets) có giống HTTP "Keep-Alive" không?
A. Là một.
B. Hoàn toàn khác. TCP Keep-Alive là những gói tin dò xét rất nhỏ, gửi theo chu kỳ dài (VD 2 tiếng/lần) khi kết nối đang Im lặng (Idle) để báo cho NAT/Firewall rằng "Chúng tôi vẫn còn sống, đừng đóng cửa cổng NAT nhé".
C. Đều dùng để nén trang web.
D. Đều thuộc tầng Ứng dụng.
*Đáp án: B*
*Giải thích: HTTP Keep-Alive để tải nhiều file trên 1 TCP. TCP Keep-Alive để "Thở" duy trì cái lỗ thủng NAT không bị hết hạn (Timeout Timeout).*

**Câu 169:** Thuật toán Nagle và Cờ PSH giải quyết vấn đề gì ngược nhau?
A. Chống lại các phần mềm virus.
B. Nagle cố gắng Tích trữ/Gom dữ liệu để Gửi thành cụm lớn (Tối ưu Băng thông nhưng tăng Trễ). Cờ PSH ép TCP gửi ngay lập tức dù rất nhỏ (Tối ưu Độ trễ nhưng tốn Băng thông đầu cước Header).
C. Nén RAM và giải phóng CPU.
D. Thay đổi cáp mạng tự động.
*Đáp án: B*
*Giải thích: Một sự cân bằng vĩnh cửu trong Mạng: Băng thông (Throughput) vs Độ trễ (Latency). Cần một, hy sinh một.*

**Câu 170:** Để thiết lập mức cửa sổ tắc nghẽn (cwnd) lý tưởng nhất cho TCP trên mạng cáp quang, chỉ số quan trọng nào được đo lường?
A. Tốc độ ánh sáng chân không.
B. BDP (Bandwidth-Delay Product - Tích số Băng thông x Độ trễ). Xác định Lượng dữ liệu chính xác có thể nhồi đầy toàn bộ cái ống cáp quang khổng lồ mà không rớt một giọt nào ra ngoài hàng đợi.
C. Kích thước màn hình.
D. Dung lượng Ổ cứng SSD.
*Đáp án: B*
*Giải thích: Ống nước to (Bandwidth Gbps), và rất Dài (Delay sang Mỹ 200ms). Thể tích ống (BDP) chứa được hàng chục Megabyte dữ liệu đang bay lơ lửng trong không khí. TCP vĩ đại ở chỗ tìm ra thông số này.*

**Câu 171:** Khi Máy gửi TCP gửi một loạt dữ liệu lớn hơn kích thước MSS, điều gì xảy ra ở Tầng Mạng (Network Layer)?
A. Máy tính tự động đổi IP.
B. TCP đã chủ động chia nhỏ (Segmentation) dữ liệu thành nhiều mảnh (mỗi mảnh <= MSS). Do đó, IP Layer chỉ nhận các mảnh nhỏ vừa vặn và không bao giờ phải thực hiện việc "Phân mảnh IP" (IP Fragmentation) ở trên cáp LAN, giảm tải CPU.
C. Thay cáp mạng.
D. Dữ liệu nén lại thành 1 gói.
*Đáp án: B*
*Giải thích: Một thiết kế tối ưu cực hay của Giao thức TCP là "Làm hộ" việc cắt bánh trước khi đẩy xuống Tầng dưới, để router Tầng dưới đẩy mượt mà.*

**Câu 172:** Chức năng "Tự động khôi phục" (Auto-recovery) khi Đứt cáp quang dưới biển, khiến đường truyền Internet chuyển hướng sang cáp dự phòng. TCP phản ứng như thế nào?
A. Không biết gì cả. Miễn là Đường truyền IP (Network Layer) tìm được đường mới trước khi TCP bị Timeout và ngắt kết nối (thường mất 1 thời gian dài), TCP sẽ vẫn kiên nhẫn Gửi lại và tiếp tục Tải file bình thường (với tốc độ chậm hơn).
B. Tắt màn hình xanh.
C. Sập TCP.
D. Xóa tệp tin đang tải.
*Đáp án: A*
*Giải thích: TCP cung cấp sự bền bỉ. Mọi biến động vật lý dưới biển đều "trong suốt" với TCP. Tuy nhiên RTT lúc này tăng cao khiến tốc độ bị giảm sút.*

**Câu 173:** Các ứng dụng mạng dựa trên UDP cần tự xử lý vấn đề Mật mã hóa. Giao thức bảo mật Tầng Ứng dụng/Giao vận nào được tạo ra song song với TLS để chạy riêng cho UDP?
A. HTTPS
B. SSL
C. DTLS (Datagram Transport Layer Security).
D. WPA3
*Đáp án: C*
*Giải thích: TLS truyền thống cần TCP để đảm bảo không mất byte nào mới giải mã được. DTLS sửa đổi thuật toán mật mã để dù mất gói (đặc điểm của UDP) vẫn có thể duy trì luồng giải mã Video Call.*

**Câu 174:** Socket TCP ở Cổng 80 của Máy chủ Web (Server) sử dụng hàm `accept()` để:
A. Sinh ra một virus mới.
B. "Chốt đơn". Khi một Client mới gõ cửa `connect()`, Server chốt một "Kết nối Mới" (Tạo ra một file descriptor/socket MỚI TRONG RAM dành riêng cho vị khách này), trong khi Cổng 80 cũ VẪN mở để đón khách tiếp theo.
C. Bỏ qua mọi gói tin.
D. Tắt hệ điều hành.
*Đáp án: B*
*Giải thích: Nếu Server chỉ có 1 cổng 80, mà 1 cổng chỉ làm việc với 1 khách thì sập tiệm. `accept()` nhân bản (fork/thread) quy trình xử lý, đẩy khách vào "phòng riêng", giữ "cửa chính" cổng 80 luôn thông thoáng.*

**Câu 175:** Quá trình "Tăng tuyến tính" (Additive Increase) trong thuật toán Tắc nghẽn xảy ra MỖI RTT. Nếu cwnd = 10 (MSS), sau bao nhiêu cái ACK nhận về thành công thì cwnd tăng thành 11?
A. Ngay sau 1 cái ACK.
B. Cứ đếm đủ số ACK tương đương 10 gói tin đó (Hoàn tất 1 Window/RTT), thì cửa sổ mới + 1. Tính trung bình, mỗi ACK chỉ cộng thêm 1/10 MSS vào cửa sổ hiện hành.
C. Mất 1 phút.
D. Trình duyệt mở tab mới.
*Đáp án: B*
*Giải thích: Sự gia tăng tuyến tính là +1 MSS mỗi "Vòng" (RTT). Chứ không phải nhận 1 gói + 1 MSS (đó là hành vi của Slow Start).*

**Câu 176:** Tại sao DNS (Port 53) có thể vừa chạy trên TCP vừa chạy trên UDP?
A. Do ISP cài đặt sai.
B. Do cấu hình kỹ thuật của hệ điều hành. DNS mặc định dùng UDP cho các truy vấn đơn lẻ để SIÊU NHANH. Nhưng nếu kết quả trả về của một truy vấn (Vd vùng zone khổng lồ) lớn hơn 512 bytes, nó bị cắt xén, Trình duyệt tự gọi TCP để đảm bảo Tải trọn vẹn kết quả.
C. Không bao giờ chạy được TCP.
D. UDP lỗi thì cắm TCP.
*Đáp án: B*
*Giải thích: Một ví dụ điển hình về Lập trình viên Tầng ứng dụng linh hoạt sử dụng cả 2 giao thức Giao vận tuỳ theo khối lượng công việc.*

**Câu 177:** Sự xuất hiện của Cơ chế "Quản lý luồng" (Flow Control) chứng minh điều gì về Năng lực phần cứng của các hệ thống đầu cuối trên mạng Internet?
A. Tất cả PC đều có CPU siêu mạnh.
B. Internet là một mạng lưới cực kỳ Không đồng nhất (Heterogeneous). Máy chủ 100 Tỷ VNĐ và Điện thoại cùi bắp 1 Tỷ VNĐ giao tiếp với nhau. Cần có Flow Control để chiếc xe lu (Server) không tông chết chiếc xe đạp (Điện thoại) bằng cách dội quá nhiều dữ liệu.
C. RAM là vô tận.
D. IP không ổn định.
*Đáp án: B*
*Giải thích: Nếu mọi máy có sức mạnh bằng nhau, Flow Control là không cần thiết. Internet là thế giới mà Kẻ mạnh phải tự động giảm tốc độ khi phục vụ Kẻ yếu.*

**Câu 178:** Trạng thái "Half-Open" (Mở một nửa) trên TCP sinh ra lỗ hổng tấn công SYN Flood vì:
A. Tốn quá nhiều điện.
B. Kẻ tấn công gửi SYN nhưng từ chối gửi ACK cuối. Tài nguyên (TCB - Transmission Control Block) và Bộ nhớ được Máy chủ DÀNH ĐẶT TRƯỚC ngay từ bước thứ 2 (SYN-ACK) chứ không phải đợi xong hoàn toàn mới cấp.
C. Hỏng cáp vật lý.
D. Thay đổi tên miền.
*Đáp án: B*
*Giải thích: SYN Cookie (đã giải thích ở câu trên) dời việc "Cấp RAM" này sang tận sau Bước 3 để vá lỗ hổng này.*

**Câu 179:** Giao thức Giao vận TCP (Transmission Control Protocol) hoạt động chủ yếu ở môi trường nào?
A. Tầng vật lý.
B. Bên trong lõi Router mạng.
C. Giao thức "End-to-End" (Đầu cuối đến Đầu cuối), mã nguồn của TCP chỉ được cài đặt và thực thi (chạy) TẠI CÁC THIẾT BỊ NGƯỜI DÙNG CỐI (Hệ điều hành Windows, Linux, Mac), hầu như không chạy trên các Router lõi thuần túy.
D. Trong card đồ hoạ.
*Đáp án: C*
*Giải thích: Đây là tư duy cốt lõi của Kiến trúc Internet. Internet là những sợi dây ngốc nghếch (IP routers) nối 2 cỗ máy thông minh (PC chạy TCP).*

**Câu 180:** "Phân kênh" (Demultiplexing) tại Tầng giao vận tương tự với hành động nào trong đời sống?
A. Đổ nước xuống cống.
B. Bưu tá của toà nhà chung cư gom tất cả thư (Packet) nhận từ xe tải bưu điện vào sảnh, rồi căn cứ vào Tên/Số Phòng (Port Number) để chia các phong bì vào từng khe hòm thư riêng của mỗi cư dân (Process).
C. Sửa xe.
D. Lắp bóng đèn.
*Đáp án: B*
*Giải thích: Số IP là Địa chỉ của Toà chung cư. Số Port là Số phòng 101, 102. Tầng mạng giao thư đến Sảnh. Tầng Giao vận phát thư lên từng phòng.*

**Câu 181:** Tại sao nói UDP là "Best-Effort" (Cố gắng tốt nhất)?
A. UDP cung cấp tốc độ vô hạn.
B. UDP KHÔNG CÓ sự đảm bảo. Nó cũng giống như Tầng Mạng IP, chỉ có nhiệm vụ bọc Port rồi ném gói tin đi. "Đến thì đến, không đến thì thôi, tôi đã cố gắng hết sức gửi đi rồi".
C. UDP làm router chạy nhanh hơn.
D. Không dùng cáp quang.
*Đáp án: B*
*Giải thích: "Best-effort" là một thuật ngữ kỹ thuật mang tính châm biếm, thực chất nghĩa là "Không cam kết chất lượng dịch vụ nào cả".*

**Câu 182:** Lựa chọn nào sau đây giải thích tốt nhất tại sao Giao thức "Stop-and-wait" lại không được TCP sử dụng trên thực tế?
A. Vì nó truyền quá nhanh.
B. Tỷ lệ Lợi dụng đường truyền (Utilization) quá thấp. Trong phần lớn thời gian (RTT), đường truyền trống rỗng, không truyền dữ liệu gì, chờ đợi phản hồi một cách lãng phí.
C. Quá tốn tài nguyên.
D. Rất dễ bị hack.
*Đáp án: B*
*Giải thích: Khái niệm "Pipe" (Ống nước). Gửi 1 gói giống như bơm 1 giọt nước vào ống rồi đứng nhìn nó chảy sang Mỹ, rất lãng phí cái ống to.*

**Câu 183:** Nếu mạng cực kỳ hoàn hảo, không bao giờ lỗi, không bao giờ mất gói tin, thì giao thức RDT chỉ cần xây dựng với cơ chế nào?
A. TCP Tahoe.
B. Đơn giản hóa về "RDT 1.0", không cần Checksum, không cần Sequence, không cần ACK, không cần Timer. Cứ gửi mù quáng như UDP là xong.
C. Thuật toán Cubic.
D. IPsec.
*Đáp án: B*
*Giải thích: TCP tồn tại trên đời vì một lý do duy nhất: Thế giới Vật lý đầy rẫy lỗi (Nhiễu điện từ, Cáp đứt, Bộ nhớ quá tải). Nếu không có lỗi, TCP hoàn toàn vô giá trị.*

**Câu 184:** Trong thuật toán TCP Reno, hiện tượng "3 ACK trùng lặp" (Triple duplicate ACKs) báo hiệu điều gì cho bộ máy TCP?
A. Cáp mạng bị tháo.
B. Báo hiệu Mất duy nhất một gói lẻ tẻ. Vì Gói 1, Gói 2 tới nơi, Gói 3 Mất, nhưng Gói 4, Gói 5 VẪN ĐẾN ĐÍCH (kích hoạt ACK trùng lặp), chứng tỏ MẠNG KHÔNG BỊ TẮC NGHẼN NGHIÊM TRỌNG, chỉ suy hao nhẹ. Cần truyền lại gói 3 nhanh chóng.
C. Tắt kết nối ngay.
D. Virus lây lan mạng.
*Đáp án: B*
*Giải thích: Sự khác biệt vĩ đại giữa Hết giờ (Tắc nghẽn đường toàn tập) và Rớt nhẹ 1 gói do ổ gà. Fast Retransmit cứu được tốc độ rất nhiều.*

**Câu 185:** Kích thước của Cửa sổ trượt (Sliding Window) được cấu hình dựa trên đơn vị tính toán nào trong TCP chuẩn?
A. Bằng số km.
B. Bằng số MegaHertz.
C. Byte.
D. Số lượng tập tin (Files).
*Đáp án: C*
*Giải thích: TCP quản lý luồng dữ liệu theo dạng Dòng Byte liên tục (Byte-stream). Số thứ tự Seq và kích thước Cửa sổ đều được đếm bằng "Byte" chứ không phải đếm số lượng Gói tin (Packets).*

**Câu 186:** Khi Máy gửi A đang trong trạng thái gửi dữ liệu liên tục cho Máy nhận B (TCP Connection). Điều gì sẽ xảy ra nếu Dây cáp mạng của B bị RÚT RA ĐỘT NGỘT (Làm chết kết nối vật lý tức thì)?
A. A ngay lập tức nhận được thông báo đứt cáp và dừng gửi lập tức.
B. A không có thần giao cách cảm. A tiếp tục gửi các Byte trong Cửa sổ của nó, sau đó chờ ACK. Không thấy ACK, A bắt đầu đếm ngược Timeout, truyền lại gói, lại đếm ngược... sau nhiều lần thất bại, A mới kết luận "Liên kết đã chết" (Timeout toàn cục).
C. B tự động gửi lệnh FIN qua sóng điện từ.
D. Card màn hình bị lỗi.
*Đáp án: B*
*Giải thích: Mạng gói (IP) không có đường dây "báo hiệu sập mạng" liên thông như mạng điện thoại. Mọi thứ chỉ được phát hiện thông qua sự "Im lặng đáng sợ" (Timeout).*

**Câu 187:** Khi Trình duyệt Web yêu cầu Tải 1 file hình ảnh 500KB bằng HTTP/1.1 (TCP). Trình duyệt có quan tâm việc cái ảnh đó bị cắt làm bao nhiêu gói tin nhỏ (Segment) không?
A. Có, trình duyệt phải tự tính toán.
B. Có, trình duyệt hiển thị từng gói lên màn hình dạng text.
C. Hoàn toàn Không. Ứng dụng (Trình duyệt) chỉ lấy "Dữ liệu dạng luồng" (Stream) ra từ Socket API giống như mở Vòi Nước ở bồn rửa. Tầng TCP bên dưới HĐH đã làm mọi việc ghép nối ảnh, sửa lỗi trước khi bơm nước vào vòi cho App.
D. Tùy thuộc vào Router.
*Đáp án: C*
*Giải thích: Sự che giấu phức tạp. Trình duyệt chỉ cần gọi hàm `socket.read(500KB)`. Chuyện bên dưới TCP xử lý ngầm trong Nhân (Kernel).*

**Câu 188:** Việc giao thức UDP có "Checksum" nhưng KHÔNG có cơ chế Sửa lỗi hay Truyền lại, ngụ ý điều gì?
A. Tự sửa bằng siêu âm.
B. UDP cho phép Ứng dụng tùy ý quyết định: "Nếu anh phát hiện sai (Checksum rớt), anh có thể vứt bỏ khung hình Video lỗi đó đi, KHÔNG CẦN BẮT TÔI TRUYỀN LẠI để giữ độ mượt mà của Clip đang chiếu".
C. UDP làm tăng nhiễu.
D. UDP không quan tâm mạng.
*Đáp án: B*
*Giải thích: Phát hiện lỗi (Error Detection) khác Sửa lỗi (Error Recovery). UDP phát hiện nhưng không sửa, dành cho Real-Time (Thà mất hình xíu còn hơn đứng máy).*

**Câu 189:** Thiết bị "Firewall" (Tường lửa) ở mức trạng thái (Stateful Firewall) có thể sử dụng thông tin của Tầng Giao vận để làm gì?
A. Cấp lại IP cho Router.
B. Đóng/Mở cáp tự động.
C. Nhớ trạng thái kết nối TCP (SYN, ACK). Nếu một gói tin lạ lọt vào từ ngoài Internet mà không thuộc về bất kỳ phiên TCP (Socket) nào đã được Lập trong mạng nội bộ, Tường lửa lập tức hủy gói tin đó (Drop) để chặn Hacker quét (Scan).
D. Truyền tải điện năng.
*Đáp án: C*
*Giải thích: Tường lửa không chỉ chặn Port, nó còn có Trí nhớ (Stateful). Chỉ cho phép "Đứa nào đi ra cửa thì mới được về", còn đứa lạ tự dưng lọt từ ngoài vào thì chặn ngay.*

**Câu 190:** Để triển khai ứng dụng "Chuyển tiền Ngân hàng" an toàn, các lập trình viên bắt buộc phải cấu hình Socket sử dụng giao thức nào ở Tầng Giao vận (trước khi bọc TLS)?
A. UDP
B. ICMP
C. TCP (Vì tính Toàn vẹn, Đảm bảo thứ tự, Không để xảy ra Mất mát Dữ liệu là sống còn).
D. ARP
*Đáp án: C*
*Giải thích: Giao dịch tiền tệ mất 1 chữ số 0 (100k thành 10k) là thảm họa tài chính. TCP cung cấp lớp khiên kiên cố nhất của hệ điều hành chống lại sự khắc nghiệt của mạng vật lý.*

**Câu 191:** Thuật ngữ "Socket" được dịch nôm na là "Ổ cắm". Hãy hình dung nó giống như ổ cắm điện. Tầng ứng dụng và Tầng giao vận tương tác với cái ổ cắm này ra sao?
A. Tầng ứng dụng là ổ cắm, tầng giao vận là phích cắm điện.
B. Ứng dụng "cắm phích" đẩy dữ liệu vào lỗ cắm trên tường (Socket). Hệ điều hành (Tầng Giao Vận) đóng vai trò là "Đường dây điện ngầm trong tường" sẽ bí mật truyền tải dữ liệu đó đến ổ cắm của nhà người khác trên Internet.
C. Socket là thiết bị phát sóng Wi-Fi.
D. Socket là màn hình máy tính.
*Đáp án: B*
*Giải thích: Lập trình viên không quan tâm hệ điều hành nhào nặn gói tin (TCP hay IP) như thế nào. Lập trình viên chỉ cần biết gọi hàm ném vào Socket (Cái lỗ trên tường).*

**Câu 192:** Việc giao thức TCP phải sử dụng một bộ Định thời (Timer) duy nhất để quản lý việc truyền lại cho rất nhiều gói tin (để tối ưu tài nguyên CPU và RAM) gây ra một giới hạn nào so với việc quản lý hàng ngàn Timer độc lập?
A. Không có giới hạn.
B. Máy tính quá tải.
C. TCP không thể quản lý "Selective Repeat" (Lặp có chọn lọc) một cách hoàn hảo ban đầu (như lý thuyết). Nó mang đặc tính kết hợp của cả Go-Back-N. Sau này, tính năng SACK (Selective ACKs) mới được đưa vào dưới dạng Option để sửa khuyết điểm này.
D. Trình duyệt đóng đột ngột.
*Đáp án: C*
*Giải thích: Việc chỉ dùng 1 Đồng hồ đếm ngược (đặt cho gói cũ nhất) khiến TCP Reno/Tahoe đôi khi phải truyền lại cả những gói không bị mất do tính chất Cumulative ACK che khuất lỗ hổng. Cờ SACK vá lỗ hổng này.*

**Câu 193:** Khi Tốc độ gửi (cwnd) của máy A được kiểm soát bởi TCP, nếu số lượng gói tin A gửi vào mạng bị lặp lại quá nhiều do 3-Duplicate ACK, đường truyền của Máy A bị ảnh hưởng tích cực hay tiêu cực?
A. Tích cực, vì làm tốc độ đường truyền tăng lên.
B. Tiêu cực, vì A đang "đốt" băng thông một cách lãng phí (Gửi những thứ đã tồn tại trên mạng hoặc gửi lại thừa). Băng thông thực tế (Goodput) sẽ thụt giảm nhiều hơn so với Tốc độ gửi thô.
C. Trình duyệt báo lỗi 404.
D. IP tự thay đổi.
*Đáp án: B*
*Giải thích: Throughput (Thông lượng gửi) đo số gói bơm vào cáp. Goodput (Băng thông hữu ích) chỉ đo số gói Dữ liệu mới cập bến an toàn. Truyền lại quá nhiều làm chênh lệch giữa hai số này rất lớn.*

**Câu 194:** Trong kiến trúc TCP, Máy gửi (Sender) sẽ luôn tính toán biến `LastByteSent - LastByteAcked` (Số byte đã gửi nhưng chưa được xác nhận) để đảm bảo điều kiện gì?
A. Bằng kích thước file Video.
B. Không bao giờ bằng 0.
C. Đảm bảo lượng dữ liệu chưa được xác nhận không bao giờ vượt qua biến Cửa sổ trượt tối thiểu là `min(cwnd, rwnd)`.
D. Biến bằng địa chỉ MAC.
*Đáp án: C*
*Giải thích: Đây là cái "Chốt cửa" để giới hạn việc Bơm dữ liệu liên tục. Nếu tính toán ra số lượng đang bay trên mạng (Flight size) đụng trần, Sender phải ngồi im chờ ACK.*

**Câu 195:** Trong biểu đồ TCP Congestion Window (cwnd), điều gì tạo nên cái dốc TĂNG CỰC KỲ DỐC lúc mới khởi tạo (Slow Start)?
A. Máy tính dùng lệnh Ping.
B. Khởi tạo cwnd = 1 MSS. Lần RTT số 1: Nhận 1 ACK, cwnd = 2. Lần RTT số 2: Gửi 2 gói, nhận 2 ACK, cwnd = 2+2=4. Lần RTT 3: Nhận 4 ACK, cwnd = 4+4=8. Do đó tốc độ vọt lên theo cấp số nhân (hàm Mũ 2^n).
C. Hệ điều hành được cấp quyền Root.
D. Cắm cáp quang tốc độ cao.
*Đáp án: B*
*Giải thích: Slow start là cái tên đánh lừa. Thực ra nó là giai đoạn Tăng Tốc độ Nhanh nhất (Exponential growth) để mò mẫm độ rộng của đường mạng ngay khi mở Web.*

**Câu 196:** Khái niệm "Connection-oriented" (Hướng kết nối) của TCP khác với Giao thức của Tầng Mạng IP như thế nào?
A. IP là "Kết nối cố định", TCP là "Không kết nối".
B. IP là "Không kết nối" (Connectionless), mỗi Datagram định vị đường đi độc lập và bơ vơ. TCP TẠO RA ẢO GIÁC "Hướng kết nối" trên nền cái mớ hỗn độn đó bằng việc thiết lập Trạng thái Phần mềm ở 2 đầu thiết bị cuối.
C. Không khác nhau.
D. IP dùng cổng Port, TCP dùng IP.
*Đáp án: B*
*Giải thích: Cáp vật lý và Router IP không hề biết bạn đang "Kết nối TCP". Chúng chỉ xử lý từng cục hàng (Packet) một cách mù quáng.*

**Câu 197:** Nếu bạn làm System Admin cho một máy chủ Game, làm sao để giới hạn lưu lượng rác UDP Flood (Tấn công DoS) dội vào máy chủ của bạn?
A. Đóng cổng 80 lại.
B. Tắt màn hình Server.
C. Viết các quy tắc (Rules) trên Firewall để Giới hạn tốc độ gói tin UDP (Rate-limiting) đi qua IP Server xuống mức X gói/giây, vì UDP Flood thường sử dụng băng thông cực đoan.
D. Thay đổi tên miền Game.
*Đáp án: C*
*Giải thích: Firewall (Iptables/UFW) có tính năng đếm và giới hạn tốc độ. Nếu nó thấy IP A bắn 10,000 UDP/s, nó sẽ rớt (drop) tự động 9900 gói để cứu mạng Server.*

**Câu 198:** Giao thức nào dưới đây KHÔNG có tính năng phân chia/cắt nhỏ dữ liệu (Segmentation)?
A. UDP
B. TCP
C. SCTP
D. QUIC
*Đáp án: A*
*Giải thích: UDP không biết cắt dữ liệu. Nếu bạn gọi hàm UDP `send()` truyền 1 file 5MB, nó sẽ nguyên khối xuống Tầng Mạng (IP). Sau đó Router IP sẽ khóc thét và băm gói 5MB đó thành hàng ngàn mảnh nhỏ (IP Fragmentation).*

**Câu 199:** Tại sao "IP Fragmentation" (Phân mảnh IP do xài UDP cho gói to) lại bị coi là tồi tệ hơn nhiều so với "TCP Segmentation" (Phân mảnh TCP)?
A. Đổi IP sang MAC.
B. Trong IP Fragmentation, nếu chỉ mất 1 mảnh IP nhỏ lẻ trên đường, Hệ điều hành đích SẼ HỦY TOÀN BỘ gói 5MB vì không ghép lại được. UDP không có cơ chế truyền lại. Do đó tỷ lệ thất bại cực cao. (Trong khi TCP chỉ mất mảnh nào gửi lại mảnh đó).
C. Tốn RAM router.
D. Phân mảnh IP có virus.
*Đáp án: B*
*Giải thích: Đó là lý do lập trình viên DNS (UDP) luôn cố gắng giữ gói tin dưới 512 bytes (Dưới giới hạn MTU) để tuyệt đối không xảy ra Phân mảnh IP trên đường bay.*

**Câu 200:** Giao thức TCP hỗ trợ gửi nhận "Out-of-band data" (Dữ liệu ngoại băng) bằng cờ/pointer nào?
A. ACK
B. SYN
C. URG (Urgent Pointer)
D. FIN
*Đáp án: C*
*Giải thích: Như đã phân tích, URG là cách ép Máy nhận đọc tức thì một nhóm Byte khẩn cấp, bất chấp thứ tự hàng đợi luồng dữ liệu thông thường.*

**Câu 201:** Hệ điều hành sử dụng công cụ gì để nhận dạng và gắn một tiến trình (ví dụ Chrome) vào một Cổng Socket TCP?
A. PID (Process ID)
B. Tên miền.
C. Địa chỉ MAC tĩnh.
D. Đèn LED.
*Đáp án: A*
*Giải thích: Cổng 80 đang Lắng nghe thực ra là được "Bind" (Trói chặt) vào một phần mềm có mã số nhận diện nội bộ trên Windows (như Nginx có PID=1023).*

**Câu 202:** "Dịch vụ Nền" (Daemon) trên Linux liên quan đến Tầng Giao vận như thế nào?
A. Làm hỏng cáp mạng.
B. Nó là các phần mềm chạy ngầm 24/7 (như `sshd`, `httpd`) sử dụng các Hàm API Socket để mở Cổng Lắng Nghe (Listening Ports: 22, 80) sẵn sàng chờ Client yêu cầu kết nối TCP/UDP.
C. Không dùng cổng.
D. Xóa bộ nhớ RAM.
*Đáp án: B*
*Giải thích: Mọi máy chủ đều phải chạy các Daemon. Nếu tắt Daemon Web (như Nginx), Cổng 80 sẽ bị đóng trên Tầng giao vận.*

**Câu 203:** Tại sao "Congestion Window" (cwnd) của TCP lại không được chèn vào TCP Header truyền qua mạng?
A. Để che giấu mật khẩu.
B. Để giảm băng thông.
C. Cửa sổ Tắc nghẽn `cwnd` là một biến số được Máy tính Gửi TỰ TÍNH TOÁN và TỰ ÁP DỤNG TRONG RAM cục bộ của nó, không liên quan đến cấu trúc gói tin mà Máy nhận cần phải biết.
D. Nó là của UDP.
*Đáp án: C*
*Giải thích: TCP Header chỉ mang `rwnd` (Receive Window - Báo cho đối phương biết "Tôi chứa được ngần này"). Còn `cwnd` (Đoán xem Mạng tải được ngần nào) là việc nhà ai nấy giữ.*

**Câu 204:** Kỹ thuật nào giúp tăng tốc độ HTTPS lên đáng kể, giải quyết vấn đề của việc thiết lập phiên SSL/TLS sau khi bắt tay TCP?
A. TCP SYN Flood.
B. Cài đặt lại Router.
C. TLS Session Resumption (Khôi phục phiên). Server lưu lại ID/Key của một lần bắt tay mã hoá trước đó. Khi mở TCP lần sau, chỉ tốn 1 RTT (hoặc 0 RTT với TLS 1.3) thay vì 2-3 RTT như bắt tay mới hoàn toàn.
D. Bật lại Wi-Fi.
*Đáp án: C*
*Giải thích: Trong thời đại HTTPS phổ cập 100%, việc giảm bớt những thủ tục "Trình giấy tờ" (Handshake) tốn kém RTT được ưu tiên số một trong Giao vận Web.*

**Câu 205:** "Trượt" (Slide) của một Sliding Window diễn ra tại thời điểm nào trong hệ thống RDT?
A. Rút phích cắm.
B. Máy gửi chỉ Trượt "Khung ngắm" về phía trước (bên phải) khi và chỉ khi nhận được ACK báo CÁC GÓI CŨ NHẤT nằm ở rìa trái của khung ngắm đã được giao hàng thành công.
C. Đổi chuẩn Wi-Fi.
D. Khi ấn F5.
*Đáp án: B*
*Giải thích: Hình dung khung cửa sổ gồm các ô [Gói 1, 2, 3, 4]. Chờ nhận được ACK số 1, thì Khung mới trượt thành [Gói 2, 3, 4, 5].*

**Câu 206:** Bạn có 1 file mã nguồn Code (1KB) và 1 video 4K (1GB) gửi qua TCP. TCP đối xử với 2 thứ này có gì khác nhau không ở tầng Giao vận?
A. Mã hóa Code tốt hơn.
B. TCP thiên vị Video.
C. TCP mù tịt (Agnostic) về nội dung ứng dụng. Nó coi cả 2 như một dải "Byte Stream" vô tri, chặt ra thành các block 1500 byte và đóng gói Header để ném đi, cơ chế bảo vệ là y hệt nhau.
D. TCP cấm truyền Video.
*Đáp án: C*
*Giải thích: Sự Trong suốt (Transparency). Giao thức dưới không cần biết Giao thức trên nó là cái gì. Nhờ vậy TCP có thể tải Web, Tải Game, Tải Code mà không phải cấu hình lại cho từng loại tệp.*

**Câu 207:** Trong mô hình Client-Server, đặc thù sử dụng Port là gì?
A. Không cần Port.
B. Client dùng Cổng chuẩn, Server dùng cổng động.
C. Server bắt buộc phải Lắng nghe ở một Cổng đã được Biết trước (Well-known Port, VD: 80). Client thì được Hệ điều hành cấp phát ngẫu nhiên Cổng Động (Ephemeral Port) bất kỳ chưa ai dùng (VD: 55231) để giao tiếp.
D. Tên miền.
*Đáp án: C*
*Giải thích: Nếu Server Web không nằm yên ở Cổng 80, mà cứ mỗi phút lại nhảy sang Cổng 50, Cổng 90, thì trình duyệt của hàng tỷ người trên thế giới sẽ không biết cắm phích vào lỗ nào.*

**Câu 208:** Giao thức TCP/IP có thuộc Bản quyền độc quyền của một Công ty nào không (như Microsoft, Apple)?
A. Của Microsoft.
B. Của CISCO.
C. Hoàn toàn Không. Nó là một Tiêu chuẩn Mở (Open Standard) miễn phí, được công bố dưới dạng các RFC, bất kỳ sinh viên hay công ty nào cũng có thể tự viết code lập trình bộ TCP/IP riêng cho mình.
D. Của IBM.
*Đáp án: C*
*Giải thích: Sự mở cửa và tự do của giao thức là nền tảng tối thượng tạo ra một mạng Internet không biên giới kết nối mọi thiết bị của hàng ngàn hãng phần cứng/phần mềm khác nhau.*

**Câu 209:** Gói tin ở tầng Giao vận (Transport) được gọi tên tiêu chuẩn (PDU - Protocol Data Unit) là gì?
A. Packet
B. Datagram (Nếu là UDP) / Segment (Nếu là TCP). Mặc dù một số sách cũng gọi chung là Segment cho cả 2.
C. Frame
D. Message
*Đáp án: B*
*Giải thích: Để giao tiếp chuyên nghiệp, nói "Tôi đang phân tích TCP Segment" sẽ chính xác và học thuật hơn là nói "Gói tin mạng TCP".*

**Câu 210:** Cụm từ "Lỗ hổng TCP" (TCP Vulnerability) kinh điển nhất liên quan đến việc dễ bị ngập lụt kết nối (DoS) tên là gì?
A. ICMP Ping of Death.
B. SYN Flooding.
C. SQL Injection.
D. Buffer Overflow.
*Đáp án: B*
*Giải thích: Như phân tích, điểm chết của Tầng Giao vận là bắt các máy chủ phải Ghi nhớ (Lưu trạng thái trên RAM). Việc sinh ra hàng triệu trạng thái giả (SYN Flood) đánh gục máy chủ trong tích tắc.*

**Câu 211:** "Fast Recovery" (Phục hồi nhanh) của thuật toán TCP Reno có chức năng:
A. Gọi cấp cứu mạng.
B. Nó bỏ qua quá trình bắt đầu chậm chạp (Slow Start về cwnd=1) sau khi phát hiện nghẽn nhẹ (3 ACK trùng). Thay vào đó, nó chia nửa Cửa sổ và khôi phục tốc độ nhanh hơn bằng cách tăng tuyến tính (Congestion Avoidance) ngay lập tức.
C. Tắt nguồn điện.
D. Reboot máy.
*Đáp án: B*
*Giải thích: Nếu cứ mỗi lần vấp ổ gà lại phải tắt máy khởi động xe lại từ đầu thì sẽ rất bực mình. Reno thông minh gạt số về nửa ga để chạy tiếp luôn qua ổ gà.*

**Câu 212:** Việc kết hợp Địa chỉ IP và Số Cổng (IP + Port) được các kỹ sư mạng gọi là gì?
A. Định danh Socket (Socket Address).
B. Tên miền.
C. Địa chỉ MAC vật lý.
D. Giao thức HTTP.
*Đáp án: A*
*Giải thích: Socket = IP:Port (VD: 192.168.1.1:8080). Đây là chìa khóa duy nhất để định danh một Endpoint ảo trong liên lạc Mạng tầng 4.*

**Câu 213:** Dữ liệu Video trong cuộc gọi Messenger (Facebook) nên được gửi qua giao thức nào để duy trì tính thời gian thực tốt nhất?
A. ICMP.
B. FTP.
C. UDP. (Không yêu cầu truyền lại, không bị "khựng" hình khi mất gói).
D. TCP.
*Đáp án: C*
*Giải thích: Đa phần Voice/Video Call ngày nay dùng RTP/UDP làm gốc.*

**Câu 214:** Cơ chế MPTCP (Multi-path TCP) cho phép gì đối với các kết nối tải xuống của thiết bị cầm tay hiện đại?
A. Cấm 4G.
B. Cho phép Trình duyệt (Tầng ứng dụng) chia đều việc tải 1 File qua ĐỒNG THỜI cả ăng-ten Wi-Fi lẫn ăng-ten 4G LTE, gộp 2 băng thông lại và tăng độ tin cậy tuyệt đối khi chuyển mạng (Handover).
C. Tự tạo mã nguồn mới.
D. Biến điện thoại thành Router.
*Đáp án: B*
*Giải thích: Nhược điểm chí mạng của TCP cổ điển là khóa chặt vào 1 IP tĩnh. MPTCP giải cứu giới hạn này trong thế giới vạn vật di động.*

**Câu 215:** Trong mạng TCP/IP, lệnh Command Prompt `ping 8.8.8.8` dùng Giao thức TCP cổng số mấy?
A. Cổng 80
B. Cổng 53
C. Cổng 443
D. CÂU HỎI SAI BẢN CHẤT. Ping dùng ICMP (Internet Control Message Protocol), hoạt động sát trên nền IPv4, KHÔNG CÓ KHÁI NIỆM SỐ CỔNG TCP hay UDP.
*Đáp án: D*
*Giải thích: Ping thuộc bộ gõ lỗi Lớp 3 (Network Layer). Các kỳ thi kỹ thuật rất hay gài bẫy hỏi "Ping dùng Port mấy" để kiểm tra người học có vững kiến trúc mô hình không.*

**Câu 216:** Một hệ thống tường lửa (Firewall) được thiết lập để "Cho phép mọi kết nối TCP ra ngoài, nhưng Chặn tất cả các kết nối TCP cố gắng khởi tạo từ ngoài vào trong". Tính năng này bảo vệ mạng LAN như thế nào?
A. Cấm dùng DNS.
B. Cho phép nhân viên trong công ty lướt Web thoải mái (Khởi tạo kết nối SYN từ trong ra ngoài), nhưng ngăn chặn Hacker ngoài Internet cố gắng Quét cổng hoặc Truy cập vào máy chủ (SYN từ ngoài vào bị DROP).
C. Tăng giá cước mạng.
D. Ngắt mạng Wi-Fi.
*Đáp án: B*
*Giải thích: Tường lửa trạng thái (Stateful) chỉ mở cửa ngược lại nếu nó thấy trong RAM rằng Gói tin vào là Gói phản hồi (ACK) của Phiên mà Nhân viên vừa chủ động mở (SYN) trước đó.*

**Câu 217:** Trong sơ đồ RDT (Truyền tin cậy), trường hợp "ACK bị mất hoàn toàn" (ACK Loss) sẽ gây ra tình trạng gì cho Máy gửi (Sender) nếu dùng RDT 2.0 (Chưa có Sequence Number)?
A. Đứng máy vĩnh viễn.
B. Sender sau một khoảng Timer Timeout sẽ tự Gửi Lại gói dữ liệu cũ. Máy nhận (Receiver) đã có gói này rồi, khi nhận thêm gói trùng lặp này, do KHÔNG CÓ Sequence Number, nó tưởng là GÓI DỮ LIỆU MỚI và nạp lỗi vào ứng dụng.
C. Bắt tay lại từ đầu.
D. Tăng tốc gửi.
*Đáp án: B*
*Giải thích: Gói dữ liệu trùng lặp (Duplicate Data) là lý do Mấu chốt mà Mạng tin cậy bắt buộc phải đánh Số thứ tự (0, 1, 2) cho Data để tránh bị nhầm lẫn giữa Gói cũ và Gói mới.*

**Câu 218:** Tín hiệu (Flag) "SYN" (Synchronize) và "FIN" (Finish) được thiết lập ở Byte nào trong Header TCP?
A. Byte đầu tiên.
B. Nằm ở Trường Flags (Control bits / 6 bits) nằm ở vị trí các byte 13-14 trong Header chuẩn. Bật cờ nghĩa là chuyển Bit đó lên giá trị 1.
C. Chứa trong phần Data.
D. Không nằm trong TCP.
*Đáp án: B*
*Giải thích: Control bits (URG, ACK, PSH, RST, SYN, FIN) như là Hệ thống còi đèn xi-nhan trên xe tải (TCP Header) để báo hiệu rẽ trái/phải cho cảnh sát giao thông (OS Receiver).*

**Câu 119 (Đổi thành 219):** TCP Segment có trường Header Length (Độ dài Header) dài 4 bit. Kích thước TCP Header lớn nhất có thể đạt được là bao nhiêu bytes?
A. 1500 bytes.
B. 60 bytes (Với tuỳ chọn Options tối đa). Do giá trị Max của 4 bit là 1111 (Hệ 10 = 15). Header tính bằng đơn vị 32-bit (4 bytes). Nên Max = 15 * 4 = 60 bytes. (Trừ 20 byte tĩnh thì có tới 40 byte dùng cho Options).
C. 20 bytes cố định.
D. Không giới hạn.
*Đáp án: B*
*Giải thích: Trường Options (Tùy chọn) trong TCP cực kỳ quan trọng để thêm các tính năng nâng cao (SACK, Window Scaling, MSS) mà không phá vỡ cấu trúc cũ.*

**Câu 220:** UDP là giao thức cốt lõi cho các thiết bị IoT cực kỳ đơn giản (như cảm biến nhiệt độ nhà thông minh gán nhúng C code). Ưu điểm tại sao?
A. Có độ trễ tính bằng giờ.
B. Mã code lập trình Stack UDP cực kỳ nhỏ nhẹ gọn (tốn vài trăm byte RAM), hoàn toàn thích hợp chạy trên các vi mạch vi điều khiển (MCU) siêu bé không có hệ điều hành (Bare-metal) mà TCP quá đồ sộ không nhét vừa.
C. UDP làm mát CPU máy lạnh.
D. Khóa chặn virus.
*Đáp án: B*
*Giải thích: TCP đòi hỏi cấu trúc lưu trữ Trạng thái phức tạp, Timer, Bộ đệm... Quá đắt đỏ với một con chip cảm biến giá 1$ chỉ dùng pin nút áo.*

**Câu 221:** Một đặc tính quan trọng của hệ thống Giao vận "Best-effort" (Cố gắng tối đa - như IP/UDP) là gì trong vấn đề Phân bổ Tài nguyên?
A. Cấp trước toàn bộ băng thông.
B. Không có sự Đặt chỗ trước (No Reservation). Các gói tin cạnh tranh tự do trên từng mili-giây ở Router. Có lúc được băng thông tối đa, có lúc mất sạch nếu tắc đường.
C. Mã hoá bằng cáp quang.
D. Yêu cầu nhập mật khẩu.
*Đáp án: B*
*Giải thích: Mạng điện thoại bàn truyền thống luôn cấp riêng 1 mạch thoại. Mạng Internet là mạng "Cạnh tranh sinh tồn", rất rẻ nhưng tốc độ không ai bảo lãnh.*

**Câu 222:** Trong Mạng phân tán P2P, làm sao UDP có lợi thế hơn TCP khi các Nút (Peers) muốn "Đánh hơi/Khám phá" (Discovery) xem có bao nhiêu người dùng ở gần mình?
A. UDP gửi lệnh Ping.
B. UDP hỗ trợ gửi gói tin Quảng bá mạng nội bộ (LAN Broadcast / Multicast) đến tất cả mọi người cùng lúc (Cổng cố định) bằng 1 gói duy nhất. TCP không có tính năng Broadcast nên phải đi Mở hàng trăm kết nối để hỏi từng người rất rườm rà.
C. TCP không dùng Port.
D. Không khác biệt.
*Đáp án: B*
*Giải thích: Game LAN như Counter-Strike dùng UDP Broadcast để máy của bạn có thể "Nhìn thấy" phòng chờ Game của máy thằng bạn ở kế bên phòng ngay tức thì.*

**Câu 223:** Quá trình "Tăng tuyến tính" (Congestion Avoidance) của TCP phản ứng với Băng thông (Capacity) bằng hình học như thế nào?
A. Cực nhanh.
B. Dò dẫm từ từ. Khi cwnd tăng 1 gói / 1 RTT, TCP chỉ nhẹ nhàng đặt thêm một hạt cát lên chiếc cân. Nếu hệ thống (Router) chưa sập, nó tự tin đặt thêm 1 hạt cát nữa ở vòng sau, cho đến khi đứt gãy.
C. Đạp ga mạnh.
D. Tắt mạng để thử.
*Đáp án: B*
*Giải thích: Triết lý của TCP Reno là luôn chạy nhanh hơn mức mạng cho phép 1 tí xíu, rồi rớt gói, rồi lùi lại, rồi lại chạy lên. Do đó nó dùng hiệu quả 90-95% đường cáp.*

**Câu 224:** "Mức sử dụng kênh truyền" (Link Utilization) của TCP ở mô hình "Dừng và Đợi" (Stop-and-wait) với tốc độ đường truyền 1 Gbps và khoảng cách RTT 30ms là khoảng bao nhiêu?
A. 100%.
B. 90%.
C. Cực kỳ nhỏ (Ví dụ < 0.03%). Vì Máy gửi gửi 1 gói 8000 bits (mất 8 micro-giây), sau đó nó NGHỈ CHƠI, ngồi chờ vô ích 30 mili-giây (30.000 micro-giây) để đợi cái ACK. Tỉ lệ làm việc = 8/30000 quá thấp.
D. Máy tính hư.
*Đáp án: C*
*Giải thích: Pipeline ra đời để nhét 10.000 gói tin vào cái thời gian trống 30.000 micro-giây kia, đẩy Utilization lên 100%.*

**Câu 225:** Khi TCP gửi một Segment 100 bytes, có cờ PSH (Push), nhưng lại nhận về ACK của gói MỚI HƠN do Cumulative ACK trùm lên, TCP sẽ hiểu gì?
A. Báo lỗi mạng ngay.
B. Segment 100 bytes đó ĐÃ THÀNH CÔNG VÀ AN TOÀN ĐẾN ĐÍCH. Hệ thống Gửi (Send Buffer) tự động xóa sạch 100 bytes đó khỏi bộ nhớ RAM để giải phóng dung lượng.
C. Trùng gói, xóa kết nối.
D. Hệ thống nhiễm Virus.
*Đáp án: B*
*Giải thích: Sứ mệnh tối cao của ACK là Lệnh Xóa Bộ Nhớ Tạm (Buffer). Chưa có ACK thì dữ liệu vẫn nằm rác trong RAM máy gửi.*

**Câu 226:** Khái niệm "Silly Window Syndrome" (Hội chứng Cửa sổ nhỏ) từ PHÍA NHẬN (Receiver) diễn ra khi Ứng dụng đọc dữ liệu quá chậm. Nếu Hệ điều hành không dùng Thuật toán Clark, nó sẽ phản hồi như thế nào?
A. Đập vỡ ổ cứng.
B. Trả về Window size siêu bé (vd rwnd = 1, 2 bytes) liên tục. Báo hại Máy gửi phải gửi các TCP Segment 40-byte-header chỉ chở được 1-2 bytes Data, tắc nghẽn mạng do rác Header quá nhiều.
C. Máy gửi ngắt cáp.
D. Đóng cổng Port.
*Đáp án: B*
*Giải thích: Thuật toán Clark bảo Máy nhận rằng "Nếu trống < 1 MSS, cứ giả vờ báo rwnd = 0 cho đối phương chờ luôn đi, khi nào tôi xả xong ổ cứng tôi báo rwnd bự rồi anh hẵng gửi".*

**Câu 227:** Việc Tầng Giao vận phân nhỏ Data thành Segment giải quyết hạn chế gì của Mạng Vật Lý ở Tầng Dưới?
A. Mạng vật lý cấm dữ liệu lớn.
B. Tránh lỗi MTU (Maximum Transmission Unit). Tầng 2 Liên kết Dữ liệu (Ethernet) vật lý chỉ có thể tải khung Frame dài tối đa 1518 byte. Nếu TCP gửi cục Data 1MB mà không Segment, Frame mạng sẽ nổ bùm (hoặc bắt Tầng IP phải băm nát bét rủi ro cao).
C. Tránh nhiễm Virus băng thông.
D. Mã hóa nhanh hơn.
*Đáp án: B*
*Giải thích: Segment MSS chính là cách Lớp 4 (TCP) nhường nhịn sự yếu kém của phần cứng Lớp 2 (Card mạng).*

**Câu 228:** Tính "Công bằng" (Fairness) trong một nút thắt cổ chai bị chia sẻ (Bottleneck Share) KHÔNG bảo đảm tuyệt đối do đặc tính nào của TCP?
A. TCP không bao giờ nhường.
B. RTT (Round Trip Time) khác nhau. TCP nào có RTT ngắn (Khoảng cách gần hơn) sẽ nhận ACK về nhanh hơn, do đó bơm tốc độ cwnd nhanh hơn, LẤY MẤT NHIỀU BĂNG THÔNG HƠN TCP có RTT dài (Khoảng cách xa).
C. Tên miền đẹp hơn.
D. IP máy chủ mạnh hơn.
*Đáp án: B*
*Giải thích: Hai người cùng download từ 1 server. Người ở Mỹ (ping 20ms) sẽ tải xong sớm gấp 10 lần người ở VN (ping 200ms) không chỉ vì độ trễ, mà vì TCP Mỹ mở Window nhanh như chớp cướp hết cáp mạng.*

**Câu 229:** TCP Header Option "Window Scale" ra đời để khắc phục giới hạn 16-bit nguyên thủy của trường Window Size (Max 64KB). Cấu trúc của Window Scale hoạt động như thế nào?
A. Dịch trái Bit (Shift Left). Nếu Window Scale = 2, giá trị Window thực tế = Giá trị 16 bit ban đầu x 2^2 (Nhân 4 lần). Mở rộng khả năng cấp Window lên đến hàng Gigabytes, giải quyết bài toán tải dữ liệu lớn trên vệ tinh/cáp quang xuyên lục địa.
B. Gắn Window vào Port.
C. Thay cáp mới 10Gbps.
D. Xóa bỏ TCP Window.
*Đáp án: A*
*Giải thích: Một thủ thuật xuất sắc để nâng cấp dung lượng lưu trữ của Protocol đã 40 năm tuổi mà không phải thay đổi lõi Header cũ.*

**Câu 230:** Bạn đang Download file, tốc độ trên Cửa sổ (Browser) báo là `1 MB/s`. Đường mạng nhà bạn là `10 Mbps`. Tại sao 1 MB/s không phải là 10 Mbps?
A. Browser báo sai.
B. 1 Byte (B) = 8 bits (b). Tốc độ 1 MB/s là tải trọng hữu ích của Tầng Ứng dụng. Nó xấp xỉ 8 Mbps. Phải cộng thêm 2 Mbps "Cước phí Header" (TCP Header 20B + IP Header 20B + Ethernet Header 18B + PPPoE 8B) mới ăn đủ 10 Mbps băng thông cáp vật lý Tầng 1.
C. Virus ăn bớt băng thông.
D. Router nhà mạng bị hỏng.
*Đáp án: B*
*Giải thích: Đừng bao giờ nhầm lẫn Bandwidth vật lý (L1) và Goodput ứng dụng (L7). Mọi lớp bọc Header bảo vệ đều tiêu tốn thêm băng thông truyền trên cáp.*

**Câu 231:** Giao thức DCCP (Datagram Congestion Control Protocol) nhằm mục đích kết hợp yếu tố nào?
A. Mã hóa DNS.
B. Cung cấp Kiểm soát tắc nghẽn (Congestion Control như TCP) nhưng lại truyền tin theo dạng Hướng gói (Datagram / Message-oriented như UDP) và cho phép truyền KHÔNG TIN CẬY (Có mất gói). Phù hợp cho Streaming Media muốn mượt nhưng vẫn không làm nghẽn mạng.
C. Bỏ qua tầng Mạng.
D. Biến đổi cáp đồng.
*Đáp án: B*
*Giải thích: UDP thuần là quá hung hăng. DCCP sinh ra để Streaming Video có "đạo đức mạng" hơn, tránh vắt kiệt băng thông của người khác.*

**Câu 232:** Nếu bạn tạo một ứng dụng truyền nhận "Nhắn tin nội bộ", bước đầu tiên ứng dụng phải Lắng nghe ở Server, lệnh `bind()` trong Socket API có nhiệm vụ:
A. Tải video.
B. Gắn chặt cái Lỗ cắm (Socket) ảo ở trong RAM vào một IP và một Số Cổng vật lý cụ thể của Máy tính (Ví dụ cổng 8888). Kể từ đây, mọi gói tin đến Cổng 8888 đều chui vào cái Lỗ cắm này.
C. Mở trình duyệt Web.
D. Ngắt mạng để cập nhật.
*Đáp án: B*
*Giải thích: Nếu không `bind()`, HĐH không biết gói tin lạ kia là rác hay là thư để giao vào nhà bạn.*

**Câu 233:** Trong biểu đồ hoạt động RDT, "Timer" của gói tin bị "Timeout" thì Máy gửi sẽ:
A. Tự động đổi Port kết nối.
B. Gửi lại đúng gói tin đang nằm chờ đó (Retransmission) và Thiết lập/Reset lại đồng hồ đếm ngược (Timer mới) ngay từ đầu.
C. Gửi file khác luôn.
D. Gửi gói NAK báo lỗi cho Mạng.
*Đáp án: B*
*Giải thích: Timer luôn được lên dây cót lại mỗi khi hành động gửi diễn ra để đảm bảo nó kiên trì chờ đến khi có hồi âm.*

**Câu 234:** Tại sao tấn công UDP Port Scan thường khó chính xác hơn TCP Port Scan?
A. Do UDP chạy nhanh quá.
B. Quét UDP thường gửi gói rỗng. Nếu Server Không phản hồi (Im lặng), Kẻ tấn công không thể kết luận chắc chắn Cổng đó MỞ hay là gói UDP đã bị Tường lửa (Firewall) VỨT MẤT DỌC ĐƯỜNG (Do UDP không có ACK).
C. Trình duyệt không mở được UDP.
D. IP nội bộ luôn chối từ UDP.
*Đáp án: B*
*Giải thích: TCP Scan (SYN scan) rõ ràng: Mở (nhận SYN/ACK), Đóng (nhận RST), Lọc/Block (Im lặng). UDP Scan rất tù mù vì thiếu tính phản hồi kết nối.*

**Câu 235:** Cờ RST (Reset) trong TCP Header do một Máy tính gửi đi khi nào?
A. Khi Máy tính muốn nâng tốc độ truyền.
B. Khi Máy tính muốn huỷ bỏ bạo lực lập tức phiên kết nối. Thường do nó nhận được gói tin của một kết nối mà nó KHÔNG HỀ BIẾT (không có state trong RAM), hoặc khi Port đó không có App nào chạy.
C. Báo hiệu thành công gửi tệp tin.
D. Yêu cầu Router cấp lại địa chỉ IP.
*Đáp án: B*
*Giải thích: RST = "Tôi không biết anh là ai, biến ngay đi". Nếu Ứng dụng Server bị Crash đột ngột, HĐH sẽ gửi RST cho các gói tin khách hàng gửi tới để dập kết nối rác.*

**Câu 236:** Trong lập trình Socket, một Máy khách (Client) muốn gửi HTTP Request đến một Máy chủ thì quy trình API đúng là:
A. `bind()` -> `listen()` -> `accept()` -> `send()`.
B. `socket()` -> `connect()` (Đợi bắt tay 3 bước TCP xong) -> `send()` -> `recv()`.
C. `recv()` ngay lập tức.
D. Tắt mạng rồi `send()`.
*Đáp án: B*
*Giải thích: Client đóng vai trò "Kẻ chủ động đi gọi điện thoại". Gọi số (connect) thành công thì mới nói chuyện (send) được.*

**Câu 237:** Sự phân biệt rõ nhất giữa Kênh (Channel) Tầng Mạng IP và Kênh Tầng Giao vận là gì?
A. IP có dây, Giao vận không dây.
B. Kênh IP là liên kết giữa CÁC HỆ THỐNG MÁY TÍNH (Host-to-Host). Kênh Giao vận (Transport) là liên kết Ảo giữa CÁC TIẾN TRÌNH PHẦN MỀM (Process-to-Process) chạy trên máy tính đó.
C. Tốc độ Giao vận gấp đôi Tốc độ IP.
D. Giao vận mã hóa, IP để Text.
*Đáp án: B*
*Giải thích: Đích đến cuối cùng của Dữ liệu mạng không phải là cái CPU, mà là cái màn hình Trình duyệt (Process). Transport sinh ra để giải nốt mẩu cuối đó.*

**Câu 238:** Biến `rwnd` (Cửa sổ nhận) của TCP được dùng trong Kiểm soát Luồng (Flow Control) phụ thuộc vào yếu tố tài nguyên nào của Máy tính nhận?
A. Tốc độ ánh sáng cáp.
B. Mức độ tắc nghẽn của Router.
C. Sự chênh lệch giữa Tốc độ Dữ liệu vào (Receive Buffer) và Tốc độ Ứng dụng Đọc/Lấy dữ liệu ra khỏi Buffer đó (Năng lực CPU xử lý ứng dụng của thiết bị).
D. Chiều dài gói IP.
*Đáp án: C*
*Giải thích: RAM có 100MB. Dữ liệu vào 10MB/s, App đọc ra 1MB/s. Rõ ràng rác ứ đọng lại. `rwnd` tụt dần cho đến khi = 0 (Báo nghẹn) để PC Gửi ngưng phát.*

**Câu 239:** Cấu trúc Header TCP có kích thước linh hoạt, làm sao Tầng giao vận Máy nhận biết được đâu là điểm BẮT ĐẦU CỦA DỮ LIỆU (Payload)?
A. Đọc từ byte số 1.
B. Dựa vào trường "Data Offset" (Header Length) 4 bit trong TCP Header. Nó cho biết Header dài bao nhiêu (số hàng 32-bit), suy ra vị trí bắt đầu của Data thực sự.
C. Dữ liệu luôn bắt đầu từ số 0.
D. Nhờ ICMP báo.
*Đáp án: B*
*Giải thích: Options Header có thể làm Header dãn ra (từ 20 đến 60 byte). Data Offset như một cây thước chỉ báo "Cắt ở đây để lấy lõi ăn".*

**Câu 240:** Thuật ngữ "BDP" (Tích số Băng thông-Trễ) liên quan mật thiết đến cấu hình Window TCP. Nếu đường cáp xuyên biển có Băng thông 1Gbps, và RTT là 100ms. Thể tích đường ống (BDP) chứa được bao nhiêu Byte lơ lửng?
A. BDP = 100 Bytes.
B. BDP = 1 Gigabit/s * 0.1 s = 100 Megabits (Khoảng 12.5 Megabytes). Nếu Window Size (TCP rwnd/cwnd) cấu hình nhỏ hơn 12.5 MB, liên kết cáp quang này sẽ luôn trong tình trạng KHÔNG THỂ KHAI THÁC ĐƯỢC ĐẦY ĐỦ BĂNG THÔNG, gây lãng phí đầu tư 1Gbps.
C. BDP không tồn tại.
D. TCP tự đóng mở cáp quang.
*Đáp án: B*
*Giải thích: Kiến thức kinh điển thiết kế Server. TCP cổ 64KB không thể tải nổi đường mạng này (Chỉ lấp được 0.5% cáp). Window Scaling ra đời cứu rỗi tốc độ Internet liên lục địa.*

**Câu 241:** Ứng dụng P2P sử dụng DHT (Distributed Hash Table), khi 1 Node rời đi, dữ liệu DHT bị xử lý thế nào?
A. Mạng bị sập.
B. DHT sử dụng cơ chế Sao chép dự phòng (Replication) lên nhiều Node liền kề (Successor/Predecessor). Khi 1 Node tắt máy, các Node kia đã có bản sao nên mạng không mất dữ liệu định tuyến.
C. Máy chủ trung tâm bù vào.
D. Bắt buộc kết nối lại Wi-Fi.
*Đáp án: B*
*Giải thích: P2P sống nhờ sự thừa mứa và "dự phòng". Bất kỳ ai cũng có thể là cái gai tắt nguồn, nhưng hệ thống luôn có kế hoạch backup phi tập trung.*

**Câu 242:** Kỹ thuật "Checksum" trong TCP/UDP giúp phát hiện được dạng lỗi nào trên mạng vật lý?
A. Hacker hack tài khoản.
B. Chỉ phát hiện lật bit (0 thành 1) ngẫu nhiên do nhiễu vật lý của cáp từ/vô tuyến. Không thể phát hiện nếu toàn bộ khung Frame bị vứt bỏ mất tích (Packet loss) tại Router.
C. Phục hồi dữ liệu xóa ổ cứng.
D. Sửa tên miền lỗi.
*Đáp án: B*
*Giải thích: Mất Packet (Drop) không làm sai Checksum, vì Packet đó có đến được đích đâu mà Checksum. Checksum chỉ dành cho gói CÒN SỐNG sót bò được về đích nhưng bị xước xát dọc đường.*

**Câu 243:** Tại sao QUIC (HTTP/3) phải sử dụng Mã hóa Mặc định và Độc quyền, KHÔNG cho phép chạy Không-Mã-hóa (Clear-text)?
A. Để thu phí bản quyền.
B. Vì nó chạy trên UDP (Không ổn định). Để xây dựng TCP Header giả ngay trong User-space, Google mã hoá toàn bộ Header này. Các Router/Firewall giữa mạng không thể đọc/sửa Header ảo (Middlebox ossification), giúp Google dễ dàng tự nâng cấp QUIC sau này mà không bị thiết bị phần cứng cũ chặn lại.
C. UDP bị cấm mã hóa.
D. Cho chạy nhanh trên CPU.
*Đáp án: B*
*Giải thích: Các Firewall đời cũ trên thế giới "dị ứng" với chuẩn lạ, nó thấy TCP Header sai khác là thả (Drop). QUIC mã hóa hết, Router chỉ thấy 1 luồng UDP vô nghĩa, cho qua tuốt tuột.*

**Câu 244:** Phương pháp định tuyến "Multicast" có lợi ích chính gì cho Tầng Ứng dụng Video Streaming?
A. Rẻ tiền cáp.
B. Chỉ phải GỬI 1 Bản sao duy nhất của Luồng Video từ Server xuống mạng Lõi. Các Router mạng Lõi tự nhân bản (Replicate) nó ở các nhánh cây cần thiết. Tránh việc Server phải Gửi HÀNG TRIỆU bản copy cho Hàng triệu thiết bị xem Live.
C. Chạy trên cáp xoắn đôi siêu âm.
D. Chặn mã độc tự lây.
*Đáp án: B*
*Giải thích: Xem chung kết Bóng đá. Thay vì 1 Server Youtube gánh 1 tỷ người (Unicast sập lập tức). 1 Server chỉ đẩy 1 Stream xuống lõi ISP, Router ISP tự vắt Stream đó ra 1 tỷ sợi cho người dùng (Multicast/IPTV).*

**Câu 245:** "Connection Refused" (Từ chối kết nối) là một lỗi thường gặp khi dùng ứng dụng. Dưới góc độ TCP, điều gì gây ra lỗi này?
A. Cáp mạng bị đứt ngầm.
B. DNS bị mất tín hiệu.
C. Máy khách gửi SYN, nhưng Địa chỉ IP Máy chủ thì ĐÚNG, còn Số Port thì KHÔNG có phần mềm nào trên Máy chủ đang Lắng nghe (Listen). HĐH Máy chủ gửi về RST (Reset).
D. Lỗi hết RAM.
*Đáp án: C*
*Giải thích: "Bấm chuông đúng số nhà, nhưng chủ nhà không có nhà hoặc phòng đó không mở cửa". Chứ mạng thì vẫn sống hoàn toàn (Bằng chứng là trả về RST rất nhanh).*

**Câu 246:** Kỹ thuật NAT (Network Address Translation) giải quyết thiếu hụt IP bằng cách hi sinh tài nguyên nào của TCP/UDP?
A. Hi sinh địa chỉ MAC.
B. Nó "Cướp" (Chiếm dụng) hàng chục ngàn Số Cổng (Port Number) ở mức Giao vận của IP Public để phân biệt các máy nội bộ. Biến Thiết bị Mạng (Router) thành một thiết bị vi phạm nguyên tắc Phân lớp (Router L3 lại đi đọc và sửa Port L4).
C. Hi sinh tốc độ Wi-Fi.
D. Xóa dữ liệu web.
*Đáp án: B*
*Giải thích: NAT là một cú tát vào mô hình OSI lý thuyết (Router chỉ là L3). Router NAT sửa IP (L3), sửa cả Port (L4), tính lại Checksum TCP. Mặc dù "sai chuẩn", nhưng NAT đã cứu rỗi Internet khỏi thảm hoạ hết IP.*

**Câu 247:** Trong quá trình "Đóng kết nối" TCP (4-way Teardown), sau khi Máy A nhận được FIN từ B và A gửi ACK xác nhận, máy A lập tức đi vào trạng thái nào?
A. CLOSE_WAIT. Máy A phải chờ để đảm bảo máy B đã nhận được ACK trước khi đóng mạch vật lý và thu hồi ổ cứng.
B. TIME_WAIT. Phải chờ 2 MSL (Khoảng thời gian tối đa gói tin tồn tại trên mạng) để đảm bảo không còn tàn dư của phiên kết nối cũ nào bay lạc vào Mạng gây lỗi cho ứng dụng mới.
C. Xóa tài khoản cục bộ.
D. Restart máy chủ.
*Đáp án: B*
*Giải thích: TIME_WAIT là biện pháp giữ an toàn cực kì quan trọng (dù nó gây tốn Socket trên Server nếu đóng mở quá nhiều).*

**Câu 248:** Khi Máy khách tải xuống từ Máy chủ, nếu "Cửa sổ Tắc nghẽn" (cwnd) của Server là 10.000 Bytes, và "Cửa sổ Nhận" (rwnd) của Client báo về là 2.000 Bytes. Server chỉ được phép gửi lượng dữ liệu chưa được xác nhận (UnACKed) là bao nhiêu?
A. 10.000 Bytes (vì Mạng mạnh).
B. 12.000 Bytes (Tổng).
C. 2.000 Bytes. Server phải Tôn trọng Khả năng của Máy Khách (Flow Control), lấy giá trị MIN(cwnd, rwnd) để đảm bảo không làm tràn bộ nhớ của Client yếu ớt.
D. Gửi vô hạn.
*Đáp án: C*
*Giải thích: "Min(Mạng, RAM)" luôn là công thức điều tiết tốc độ tối thượng của TCP.*

**Câu 249:** Trong sơ đồ RDT (Truyền tin cậy), chức năng "Kiểm tra tính toàn vẹn" (Error Detection) luôn yêu cầu Tầng Ứng dụng phải làm gì?
A. Nén dữ liệu MP4.
B. Hoàn toàn Không làm gì cả. Tầng Ứng dụng không cần biết Checksum tính ra sao, Mọi công việc Băm mã, Tính Checksum, Thêm Checksum vào Header là do Tầng Giao vận (TCP/UDP) thực hiện âm thầm trong Hệ điều hành (Kernel space).
C. Phải tự tính bằng Javascript.
D. Mua phần mềm chặn Virus.
*Đáp án: B*
*Giải thích: Nếu lập trình viên App chat (C#/Java) phải tự code hàm Kiểm tra lỗi bit cho mỗi tin nhắn thì thảm hoạ. HĐH bao trọn gói món này qua Socket.*

**Câu 250:** Cuối cùng, chức năng vĩ đại nhất của Tầng Giao vận (Transport Layer) so với các Tầng khác trong Kiến trúc Internet là gì?
A. Cung cấp Dây mạng không bao giờ đứt.
B. Biến môi trường Vô Tuyến (Wi-Fi) thành Hữu tuyến.
C. Tạo ra môi trường Kết nối Logic Trừu tượng (Logical Communication) Bền vững, Tin cậy, Đảm bảo từ Điểm-đến-Điểm (End-to-End) trên nền tảng của một mớ hỗn độn các Đường dây Vật lý và Bộ định tuyến rời rạc, rủi ro, rẻ tiền và thường xuyên đánh mất gói tin của Tầng Mạng IP.
D. Sinh ra trí tuệ nhân tạo.
*Đáp án: C*
*Giải thích: IP (Network) cung cấp "Sự kết nối" (Kết nối mọi thứ trên đời lại với nhau). TCP (Transport) cung cấp "Sự văn minh" (Duy trì Trật tự, Độ tin cậy, Phân kênh ứng dụng) để con người sử dụng.*
