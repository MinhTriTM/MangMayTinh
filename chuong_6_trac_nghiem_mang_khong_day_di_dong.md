# CHƯƠNG 6: TRẮC NGHIỆM MẠNG KHÔNG DÂY VÀ DI ĐỘNG

**Câu 1:** Một trong những khác biệt vật lý lớn nhất làm suy giảm tín hiệu của đường truyền không dây so với cáp quang hoặc cáp đồng là gì?
A. Tín hiệu bị đóng băng do nhiệt độ không gian tự do.
B. Cường độ tín hiệu bị suy giảm rất nhanh theo bình phương khoảng cách (Path loss) và bị hấp thụ/phản xạ bởi các chướng ngại vật trên đường đi.
C. Sóng điện từ không thể mang theo tín hiệu nhị phân.
D. Sóng vô tuyến không thể đi qua vùng có ánh sáng mạnh.
*Đáp án: B*
*Giải thích: Môi trường vô tuyến là không gian mở (unguided media). Sóng lan tỏa mọi hướng làm năng lượng suy hao nhanh, đồng thời tường bê tông, cây cối hấp thụ năng lượng sóng.*

**Câu 2:** Tỉ số SNR (Signal-to-Noise Ratio) trong truyền thông không dây được dùng để đánh giá yếu tố nào?
A. Đo lường kích thước địa chỉ IP.
B. Đo lường tỷ lệ giữa sức mạnh của Tín hiệu thu được so với năng lượng của Nhiễu nền môi trường. SNR càng CAO thì chất lượng tín hiệu càng tốt.
C. Đo tỷ lệ lỗi bit (BER) sinh ra trên cáp.
D. Tính toán tốc độ ánh sáng trong môi trường mạng.
*Đáp án: B*
*Giải thích: Nếu Tín hiệu (Signal) bị Nhiễu (Noise) lấn át (tức SNR thấp), máy nhận sẽ không thể phân biệt nổi số 0 và số 1, dẫn đến Lỗi bit (BER) tăng vọt.*

**Câu 3:** Hiện tượng "Multipath propagation" (Lan truyền đa đường) gây méo tín hiệu vô tuyến xuất phát từ nguyên nhân nào?
A. Do trạm phát phát cùng lúc quá nhiều tần số khác nhau.
B. Do sóng điện từ phản xạ và dội vào các bề mặt (tường, tòa nhà, mặt đất) tạo ra nhiều tia sóng đi theo nhiều quỹ đạo có độ dài khác nhau, và tới ăng-ten nhận ở các thời điểm hơi lệch nhau.
C. Do các thiết bị ở gần nhau phát tín hiệu cùng một lúc.
D. Do nhà mạng đặt các trạm (cell) quá gần nhau.
*Đáp án: B*
*Giải thích: Giống như tiếng vang (echo) trong phòng kín. Tia phản xạ đi xa hơn nên tới muộn hơn tia trực tiếp, chúng dội vào nhau làm nhòe tín hiệu gốc tại bộ thu.*

**Câu 4:** Vấn đề "Hidden Terminal" (Terminal ẩn) trong mạng không dây mô tả nghịch lý nào sau đây?
A. Kẻ tấn công ẩn giấu trong mạng Wi-Fi không hiện tên để nghe lén.
B. Thiết bị di động nằm ở góc chết không tìm thấy điểm phát sóng (AP).
C. Hai máy tính (A và C) không nghe thấy nhau do cách xa nhau hoặc bị cản trở, nhưng chúng cùng nằm trong tầm phủ sóng của một máy chủ AP (B). Cả hai cùng phát sóng tới B vì lầm tưởng kênh đang rảnh, gây ra xung đột tại B.
D. Điểm truy cập tự động ẩn SSID để không ai tìm thấy.
*Đáp án: C*
*Giải thích: A "nghe" kênh rảnh nên A phát cho B. C ở bên kia dãy núi cũng "nghe" kênh rảnh nên C phát cho B. Cả 2 luồng sóng đâm vào nhau tại B khiến B không đọc được khung nào. Ethernet có dây không hề gặp lỗi này.*

**Câu 5:** Vì bài toán Terminal ẩn, chuẩn Wi-Fi (IEEE 802.11) đã thay thế công nghệ CSMA/CD của Ethernet bằng giao thức gì?
A. Token Ring
B. ALOHA
C. TDM
D. CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance)
*Đáp án: D*
*Giải thích: Phần cứng vô tuyến không thể vừa phát mạnh vừa nghe yếu để phát hiện va chạm (CD). Nó phải đổi sang chiến thuật Tránh Va chạm (CA) bằng cách chờ đợi.*

**Câu 6:** Trong CSMA/CA của Wi-Fi, khi thiết bị muốn phát nhưng thấy sóng (kênh) đang BẬN, quá trình đếm ngược thời gian lùi lại ngẫu nhiên (Backoff) có đặc điểm thông minh nào?
A. Đếm ngược liên tục không ngừng cho đến 0.
B. Quá trình đếm ngược sẽ TẠM DỪNG (Freeze) (đóng băng) lại ngay khi nó nghe thấy kênh bị bận bởi một máy khác. Khi kênh rảnh rỗi, nó mới tiếp tục đếm phần còn lại.
C. Tăng gấp đôi bộ đếm thời gian.
D. Xóa bỏ gói tin để truyền gói khác.
*Đáp án: B*
*Giải thích: Đóng băng bộ đếm giúp các máy đã chờ lâu được ưu tiên phát sóng ngay khi mạng rảnh, đảm bảo công bằng (fairness) giữa các máy trạm.*

**Câu 7:** Cơ chế kiểm soát luồng phụ trợ RTS/CTS trong Wi-Fi được sinh ra để triệt tiêu trực tiếp vấn đề gì?
A. Bẻ khóa mật khẩu WEP.
B. Giải quyết bài toán Terminal Ẩn bằng cách gửi các khung điều khiển siêu nhỏ (đặt chỗ) trước khi truyền cục dữ liệu khổng lồ.
C. Mã hóa tín hiệu mạng 4G.
D. Giới hạn dải tần số 5 GHz.
*Đáp án: B*
*Giải thích: RTS (Xin phát) và CTS (Đồng ý phát) đóng vai trò dọn đường. Khung CTS được AP la lớn cho tất cả mọi máy quanh nó (kể cả máy ẩn) nghe thấy và phải câm lặng để nhường đường cho máy xin phát.*

**Câu 8:** Vì sao giao thức Wi-Fi 802.11 lại thiết kế thêm việc gửi gói tin Báo nhận (ACK) ngay tại Tầng Liên kết (Data Link), điều mà Ethernet có dây không hề làm?
A. Vì Wi-Fi không hoạt động cùng với TCP.
B. Để lấy thông tin tính tiền cước dữ liệu cục bộ.
C. Vì tỷ lệ lỗi (BER) và đụng độ trên kênh không dây rất cao. Bằng cách dùng ACK ngay tại phần cứng Wi-Fi, thiết bị có thể chủ động truyền lại tức thì nếu rớt gói, thay vì để Tầng giao vận (TCP) chờ Timeout rất tốn thời gian.
D. Để mã hóa bảo mật chuẩn WPA3.
*Đáp án: C*
*Giải thích: Gửi qua sóng radio thì "rớt gói" là cơm bữa. Việc Sửa Lỗi Cục Bộ tại mức Link layer giúp TCP ở trên vẫn có ảo giác đường truyền ổn định.*

**Câu 9:** Để máy tính/điện thoại quét tìm các điểm phát Wi-Fi (AP) xung quanh để kết nối, nó dựa vào loại khung dữ liệu nào do AP định kỳ phát ra?
A. Data frames
B. RTS frames
C. Beacon frames (Gói đèn biển)
D. ARP Request
*Đáp án: C*
*Giải thích: Passive Scanning (Quét thụ động). Trạm AP cứ mỗi 100ms lại phát tán một Beacon chứa SSID và thông số MAC của nó để "chào hàng" tới các máy tính trong bán kính.*

**Câu 10:** Kiến trúc của Mạng di động 4G LTE khác với các thế hệ viễn thông 2G/3G tiền nhiệm ở điểm đột phá nào?
A. Vẫn duy trì hệ thống chuyển mạch kênh cồng kềnh cho các cuộc gọi thoại thông thường.
B. Thiết lập một kiến trúc All-IP (Packet-switched 100%), mọi luồng dữ liệu kể cả các cuộc gọi thoại (VoLTE) đều được chuyển thành các gói tin IP truyền qua mạng dữ liệu.
C. Sử dụng sóng Wi-Fi thay cho trạm anten.
D. Loại bỏ thẻ SIM ra khỏi điện thoại.
*Đáp án: B*
*Giải thích: Sự thay đổi này thống nhất cấu trúc lõi mạng với Internet, biến nhà mạng viễn thông trở thành những cỗ máy định tuyến IP khổng lồ.*

**Câu 11:** Trạm thu phát sóng trực tiếp kết nối với điện thoại di động trong ô sóng 4G LTE được gọi bằng thuật ngữ kỹ thuật nào?
A. Access Point (AP)
B. BSS
C. eNodeB (Evolved Node B)
D. HSS
*Đáp án: C*
*Giải thích: eNodeB quản lý vùng không gian vô tuyến. Đảm nhận lịch trình truyền cho hàng ngàn điện thoại di động bằng tài nguyên thời gian và tần số.*

**Câu 12:** Trong Mạng lõi di động (EPC - Evolved Packet Core) của 4G, bộ phận nào nắm vai trò Não bộ Điều khiển (Control Plane), quản lý xác thực điện thoại và theo dõi vị trí di chuyển?
A. PGW (Packet Data Network Gateway)
B. SGW (Serving Gateway)
C. MME (Mobility Management Entity)
D. eNodeB
*Đáp án: C*
*Giải thích: MME là một bộ não thuần túy. Nó không vận chuyển dữ liệu video/web của bạn (đó là việc của Data plane SGW/PGW). Nó chỉ lo định vị bạn đang ở trạm nào để điều phối cuộc gọi.*

**Câu 13:** Cổng Gateway giáp ranh kết nối mạng di động của nhà mạng ra Internet toàn cầu (điểm thực hiện gán IP cho điện thoại) gọi là gì?
A. HSS
B. PGW (PDN Gateway)
C. MME
D. Router BGP
*Đáp án: B*
*Giải thích: PGW là cái phễu cuối cùng. Mọi dữ liệu điện thoại đi vào Internet đều phải lọt qua PGW.*

**Câu 14:** Khi bạn mang điện thoại từ mạng Viettel Hà Nội (Home Network) đi du lịch vào Mạng Viettel TP.HCM hoặc sang Mạng Mỹ (Visited Network), Mạng khách sẽ cấp cho bạn một cái địa chỉ IP tạm thời để giao tiếp. Tên của nó là gì?
A. Permanent IP (IP cố định)
B. MAC Address
C. IPv6
D. Care-of Address (COA - Địa chỉ tạm trú)
*Đáp án: D*
*Giải thích: COA là số nhà tạm bợ để mạng khách biết đường giao gói tin tới cho bạn khi bạn đang lang thang trong địa bàn của họ.*

**Câu 15:** Trong cơ chế quản lý Di động, quá trình Định tuyến Gián tiếp (Indirect Routing) giải quyết việc chuyển một tin nhắn từ Internet tới cái điện thoại đang đi du lịch bằng bước nào sau đây?
A. Lên Google tra địa chỉ của mạng khách và gửi thẳng.
B. Phát Broadcast ra toàn cầu chờ điện thoại nhận lấy.
C. Gửi tin nhắn đến cái IP cố định ở Mạng Nhà. Thiết bị Home Agent tại Mạng Nhà sẽ bắt lấy, nén nguyên khối tin nhắn đó vào một Đường hầm IP (Tunneling) và nhắm thẳng địa chỉ tạm trú (COA) ở Mạng Khách để bắn đi.
D. Trả về lỗi không tìm thấy (Destination unreachable).
*Đáp án: C*
*Giải thích: Mạng nhà đóng vai người giao liên. Người gửi ngoài Internet không hề biết điện thoại đang ở Mỹ, họ cứ gửi thư về Hà Nội, Hà Nội sẽ bọc thư lại gửi hỏa tốc sang Mỹ theo địa chỉ COA.*

**Câu 16:** Sự kiện "Handover" (Handoff / Chuyển giao) trong mạng di động xảy ra khi nào?
A. Khi thuê bao trả trước nạp thêm tiền vào tài khoản.
B. Khi thuê bao ngắt chế độ Máy bay.
C. Khi điện thoại di động di chuyển vượt ra ranh giới sóng của trạm eNodeB cũ và đi vào vùng của một trạm eNodeB mới. Hệ thống sẽ tự động hoán đổi luồng kết nối sang trạm mới cực nhanh mà không làm đứt cuộc gọi/video.
D. Khi kết nối Wi-Fi ở nhà bị rớt.
*Đáp án: C*
*Giải thích: Nhờ tính toán cường độ sóng báo cáo từ điện thoại, eNodeB cũ sẽ đàm phán với eNodeB mới trải thảm đỏ mời điện thoại sang, đồng thời forward nốt gói tin thừa sang trạm mới.*

**Câu 17:** Khung dữ liệu (Frame) của chuẩn Wi-Fi 802.11 phức tạp hơn khung của chuẩn Ethernet 802.3 ở điểm nào rõ rệt nhất?
A. Không sử dụng mã kiểm tra lỗi CRC.
B. Có tới tận 4 trường địa chỉ MAC (Address 1, 2, 3, 4) thay vì chỉ có 2 trường (Source/Dest MAC) như Ethernet, nhằm phục vụ việc chuyển giao khung từ điện thoại -> AP không dây -> Router mạng có dây.
C. Có chứa mã hóa RSA.
D. Độ dài phần tải (payload) bắt buộc phải lớn hơn 1500 bytes.
*Đáp án: B*
*Giải thích: Do AP làm cầu nối giữa môi trường vô tuyến và có dây, khung Wi-Fi phải mang địa chỉ đích cuối, địa chỉ gốc, địa chỉ AP thu và địa chỉ AP phát.*

**Câu 18:** Hiện tượng SNR (Signal-to-Noise Ratio) tụt dốc thê thảm sẽ trực tiếp gây ra điều gì?
A. Làm tăng băng thông của kết nối.
B. Làm cho trạm AP bị hỏng.
C. Khiến cho tỷ lệ Lỗi Bit (BER - Bit Error Rate) tăng vọt, vì máy thu không thể phân biệt nổi tín hiệu gốc lẫn trong đám nhiễu ồn ào.
D. Tăng khoảng cách kết nối.
*Đáp án: C*
*Giải thích: SNR thấp tức là "nhiễu" ồn hơn "tín hiệu", giống như cố gắng nghe bạn bè thì thầm giữa sân vận động đang bật nhạc xập xình. Bạn sẽ nghe nhầm chữ (Lỗi Bit).*

**Câu 19:** Để đối phó với hiện tượng tín hiệu sóng (SNR) thay đổi liên tục khi người dùng đi xa hoặc đi gần lại bộ phát Wi-Fi/4G, thiết bị áp dụng kỹ thuật tự động gì?
A. Kỹ thuật thích ứng Tốc độ / Điều chế (Rate/Modulation Adaptation): Khi sóng khỏe, dùng kỹ thuật điều chế bậc cao (ví dụ QAM-64) để truyền rất nhanh. Khi sóng yếu (đi xa), tự động lùi về điều chế cơ bản (ví dụ BPSK) chậm nhưng chống lỗi tốt.
B. Kỹ thuật thay đổi IP liên tục.
C. Kỹ thuật giảm ánh sáng màn hình điện thoại.
D. Kỹ thuật tắt luồng gửi gói tin ACK.
*Đáp án: A*
*Giải thích: Thấy sóng yếu, điện thoại phải nói "chậm rãi, rõ ràng từng chữ" (tốc độ Mbps bị giảm thê thảm). Sóng mạnh, nó sẽ "nói liến thoắng" (tốc độ vọt lên Gigabit).*

**Câu 20:** Active Scanning (Quét chủ động) trong mạng Wi-Fi đòi hỏi máy khách (Client) phải phát đi loại thông điệp nào để dò tìm mạng?
A. Beacon Frame
B. CTS Frame
C. Probe Request Frame (Khung yêu cầu dò tìm) phát quảng bá. Mọi AP nghe thấy sẽ gửi lại Probe Response Frame trả lời.
D. ARP Request
*Đáp án: C*
*Giải thích: Thay vì ngồi thụ động nhặt Beacon từ AP rớt xuống, Active scanning ép điện thoại phải la lên "Có ai ở quanh đây không?" để các AP đồng loạt xưng tên.*

**Câu 21:** Chuẩn mạng không dây nào của cá nhân (Personal Area Network - PAN) có tầm phủ sóng rất ngắn, chủ yếu dùng để kết nối chuột, tai nghe, thiết bị đeo thông minh?
A. Wi-Fi (802.11ax)
B. Bluetooth (IEEE 802.15.1)
C. 4G LTE
D. Fiber-optics
*Đáp án: B*
*Giải thích: Bluetooth hay Zigbee thuộc nhóm mạng tầm ngắn (vài mét) tiêu thụ năng lượng cực thấp dành cho thiết bị cá nhân và IoT.*

**Câu 22:** Ở phía Mạng nhà (Home Network) của một thuê bao di động, thiết bị HSS (Home Subscriber Server) có vai trò tương đương với gì?
A. Tổng đài điện thoại.
B. Một cơ sở dữ liệu (Database) khổng lồ chứa hồ sơ khách hàng, chìa khóa mật mã xác thực (SIM) và thông tin vị trí của toàn bộ thuê bao thuộc nhà mạng đó.
C. Bộ định tuyến quang học.
D. Thiết bị khuếch đại sóng.
*Đáp án: B*
*Giải thích: HSS là hồ sơ lý lịch. Khi bạn đăng nhập vào 4G, MME sẽ lôi hồ sơ của bạn từ HSS ra xem bạn có nợ cước không, khóa bí mật của SIM là gì.*

**Câu 23:** Trạng thái "Sleep" (Ngủ) của các thiết bị Wi-Fi có tác dụng lớn nhất là gì?
A. Tăng băng thông khi thức dậy.
B. Tiết kiệm năng lượng (Pin) cho thiết bị di động bằng cách tắt phần cứng vô tuyến. Thiết bị hẹn giờ thức dậy đúng lúc AP phát Beacon để nghe xem có dữ liệu gửi cho mình hay không.
C. Chống lại cuộc tấn công DoS.
D. Bảo vệ màn hình máy tính.
*Đáp án: B*
*Giải thích: Pin là sinh mệnh của điện thoại. Phần cứng dò sóng ăn điện rất ác. Power management giúp điện thoại ngủ 90% thời gian.*

**Câu 24:** Mạng vô tuyến sử dụng Dải tần số ISM (Industrial, Scientific, Medical) như 2.4 GHz gặp rủi ro gì lớn nhất?
A. Tần số này không thể truyền thông tin.
B. Vì đây là dải tần miễn phí, nó bị sử dụng bởi hàng đống công nghệ tạp nham từ Wi-Fi, Bluetooth, Zigbee cho đến bức xạ của Lò vi sóng, nên MỨC ĐỘ NHIỄU (Interference) rất kinh khủng.
C. Bị nhà mạng tính phí rất cao.
D. Sóng 2.4 GHz không đi xuyên qua được kính cửa sổ.
*Đáp án: B*
*Giải thích: Băng tần 2.4GHz là một "khu chợ chồm hổm" vô tuyến do không cần giấy phép. Đó là lý do chuẩn 5GHz ra đời để có môi trường sạch sẽ hơn (dù xuyên tường kém hơn).*

**Câu 25:** Nhược điểm của cơ chế Direct Routing (Định tuyến trực tiếp) trong việc quản lý thiết bị di động là gì?
A. Người gửi phải đóng gói bằng Tunneling.
B. Nếu thiết bị di động đi ô tô tốc độ cao và thay đổi Mạng khách (Visited Network) liên tục, luồng dữ liệu truyền thẳng từ Người gửi đến COA sẽ bị gãy giữa chừng vì Người gửi gặp khó khăn trong việc cập nhật địa chỉ COA mới liên tục.
C. Quá chậm so với định tuyến gián tiếp.
D. Tốn phí của nhà mạng.
*Đáp án: B*
*Giải thích: Định tuyến trực tiếp tiết kiệm đường đi (không phải vòng về Mạng Nhà). Nhưng bù lại độ trễ chuyển giao handover lớn vì bắt người gửi (đang ở đầu kia Trái đất) phải cập nhật lại luồng tin.*

**Câu 26:** 5G đem lại những cải tiến kỹ thuật nổi trội nào so với 4G?
A. Chuyển trở lại dùng cáp đồng.
B. Loại bỏ giao thức IP.
C. Tốc độ Gigabit ở sóng mmWave, tăng cường mật độ thiết bị khổng lồ cho IoT, và Mạng lõi được Ảo hóa/Phân chia (Network Slicing) tạo ra các mạng riêng biệt tùy theo nhu cầu dịch vụ.
D. Tăng khoảng cách phát sóng của eNodeB lên hàng ngàn kilomet.
*Đáp án: C*
*Giải thích: 5G không chỉ là "Internet nhanh hơn", mà nó được thiết kế cho xe tự lái (trễ siêu thấp) và IoT (hàng triệu cảm biến). Network slicing cắt hạ tầng ảo ra cho từng nhu cầu.*

**Câu 27:** Trong một khung MAC Wi-Fi (802.11), trường "Duration" (Thời lượng) được gài vào để làm gì?
A. Định giờ hẹn tắt máy.
B. Chứa thời lượng của bộ phim đang xem.
C. Để các máy khác "nghe lỏm" được biết là quá trình truyền khung này (cộng thêm khung ACK) sẽ kéo dài trong bao nhiêu micro-giây, từ đó chúng cài đặt bộ đếm NAV (Network Allocation Vector) và im lặng ngủ chờ cho rảnh kênh.
D. Hiển thị độ bền của thiết bị.
*Đáp án: C*
*Giải thích: Khung Wi-Fi la lên: "Tôi cần 50ms để truyền và nhận cục này". Mọi máy nghe thấy liền tự lấy băng dính dán mồm mình lại trong 50ms (NAV).*

**Câu 28:** Đâu KHÔNG phải là một chuẩn do IEEE quy định cho mạng Không dây (Wireless LAN)?
A. 802.11b
B. 802.11g
C. 802.3 Ethernet
D. 802.11ac (Wi-Fi 5)
*Đáp án: C*
*Giải thích: 802.3 là tiêu chuẩn gia đình dành riêng cho Cáp đồng và Cáp quang có dây (Ethernet).*

**Câu 29:** Nếu một thiết bị gửi dữ liệu qua một liên kết vô tuyến mà phát hiện tỷ lệ lỗi quá cao, tầng liên kết của thiết bị đó sẽ dùng công cụ tự động nào thay vì để tầng TCP lo liệu?
A. Chuyển đổi mã hóa RSA.
B. Gửi cờ SYN lên router.
C. Dùng cơ chế ARQ (Automatic Repeat reQuest) ở tầng Liên kết (Data Link Layer) để yêu cầu máy nhận xác nhận ACK cục bộ và tự truyền lại khung bị lỗi ngay trên không trung.
D. Format lại ổ cứng.
*Đáp án: C*
*Giải thích: ARQ tầng Link giúp khắc phục lỗi ngay tại chiến trường vô tuyến đầy nhiễu loạn trước khi rác rến bị đẩy lên các tầng cao hơn.*

**Câu 30:** Thiết kế "Ô hình Lục giác (Tổ ong)" trong mạng Cellular có lợi ích lý thuyết nào?
A. Làm cột sóng dễ xây hơn.
B. Phủ kín hoàn toàn mặt phẳng địa lý không để lại các góc chết, đồng thời cho phép Tái sử dụng Tần số (Frequency Reuse) ở các ô cách xa nhau để tiết kiệm băng tần đắt đỏ.
C. Cho phép sóng truyền qua bê tông 100%.
D. Xóa bỏ hoàn toàn hiện tượng nhiễu.
*Đáp án: B*
*Giải thích: Ô hình lục giác (tổ ong) là mô hình toán học hoàn hảo nhất để tối ưu diện tích phát sóng. Ô số 1 xài băng tần X thì ô số 3 ở xa cũng có thể tái xài băng tần X mà không bị nhiễu.*

**Câu 31:** Trong mạng Wi-Fi (802.11), một "BSS" (Basic Service Set) là gì?
A. Cấu trúc cáp đồng xoắn đôi.
B. Một máy chủ cơ sở dữ liệu.
C. Mạng cơ sở của Wi-Fi, bao gồm một hoặc nhiều Trạm (Wireless Stations - như laptop, điện thoại) kết nối với MỘT Điểm Truy Cập (Access Point - AP) trung tâm. Các thiết bị giao tiếp với nhau PHẢI đi qua AP.
D. Giao thức bảo mật cho cáp quang.
*Đáp án: C*
*Giải thích: BSS là hạ tầng cơ bản nhất (Infrastructure mode) của Wi-Fi tại nhà hay quán cafe. Mọi máy muốn in tài liệu không gửi thẳng Wi-Fi cho máy in được, mà phải ném lên Cục phát AP, rồi AP thả xuống Máy in.*

**Câu 32:** Cấu trúc mạng "Ad-hoc Mode" (IBSS) của Wi-Fi hoạt động như thế nào so với BSS?
A. Không dùng sóng Wi-Fi.
B. IBSS TỪ CHỐI sử dụng Điểm truy cập trung tâm (No Access Point). Các thiết bị (như laptop A và B) liên kết TRỰC TIẾP và phát sóng vô tuyến NGANG HÀNG vào nhau (Ví dụ: Chế độ Wi-Fi Direct hoặc kết nối 2 laptop để share file trong rừng).
C. Bắt buộc dùng cáp mạng Ethernet.
D. Phải có Router mạng lõi.
*Đáp án: B*
*Giải thích: Ad-hoc giống mạng P2P vật lý. Rất khó cấu hình mở rộng nhưng sống sót tốt trong môi trường khẩn cấp (Cứu hộ cứu nạn) khi các cột sóng Wi-Fi đã sập hết.*

**Câu 33:** Mạng "Mesh Wi-Fi" hiện đại khắc phục nhược điểm gì của các bộ kích sóng (Repeater) đời cũ?
A. Khắc phục việc Repeater làm tăng gấp đôi độ trễ và giảm BĂNG THÔNG đi một nửa do bản chất Bán song công (Vừa thu từ AP gốc, vừa phát cho Client trên cùng 1 Ăng-ten). Mesh Wi-Fi sử dụng Băng tần/Ăng-ten riêng biệt (Dedicated Backhaul) để các Cục phát nói chuyện với nhau, giữ nguyên tốc độ cho điện thoại.
B. Tránh hacker đăng nhập.
C. Đổi IP mạng liên tục.
D. Đổi cáp quang.
*Đáp án: A*
*Giải thích: Dùng kích sóng (Repeater) 2.4Ghz rẻ tiền nối tiếp nhà nhiều tầng, đến cục thứ 3 thì tốc độ rớt thê thảm và ping cao vút. Mesh sinh ra để thiết lập cao tốc nội bộ ngầm ở 5GHz giữa các bộ phát.*

**Câu 34:** Sự kiện "Association" (Kết hợp) trong tiến trình kết nối Wi-Fi là bước gì?
A. Cắm cáp điện cho Router.
B. Bật tường lửa Firewall.
C. Quá trình Thiết bị di động (Client) GỬI YÊU CẦU xin phép gia nhập mạng tới một AP cụ thể, kèm theo các thông số năng lực của mình (tốc độ Max, chuẩn mã hóa). AP duyệt và NẠP Địa chỉ MAC của máy đó vào bộ nhớ quản lý.
D. Xin cấp IP DHCP.
*Đáp án: C*
*Giải thích: Cầm điện thoại click vào tên Wi-Fi. Hành động ngầm đầu tiên là Điện thoại xin AP "Ghi danh". Ghi danh (Association/Auth) xong ở Tầng 2 thì mới tính chuyện Xin IP (DHCP Lớp 3).*

**Câu 35:** Cấu trúc Mã hóa WEP (Wired Equivalent Privacy - Đời đầu) thất bại thảm hại về an ninh mạng vì lý do cốt lõi nào?
A. Mật khẩu WEP quá dài.
B. Giao thức không bắt buộc dùng mật khẩu.
C. Hệ thống sử dụng một Vector Khởi tạo (Initialization Vector - IV) quá ngắn (24-bit) và TÁI SỬ DỤNG LIÊN TỤC. Hacker chỉ cần dùng phần mềm bắt gói tin (Sniff) vài chục ngàn Frame rác trong không khí là có thể Dịch ngược (Crack) tóm sống Chìa khóa gốc trong vài phút.
D. Nó chạy trên TCP.
*Đáp án: C*
*Giải thích: Thuật toán mật mã RC4 bản thân nó mạnh, nhưng cách Thiết kế Mạng của WEP quá ngây ngô. Hacker dùng công cụ aircrack-ng có thể bẻ khóa WEP quán cafe nhanh hơn uống 1 ngụm nước.*

**Câu 36:** Để vá lỗi WEP, chuẩn WPA2 hiện tại sử dụng thuật toán mã hóa tối tân nào làm nền tảng?
A. Thuật toán DES.
B. Thuật toán MD5.
C. AES-CCMP (Advanced Encryption Standard). Đây là chuẩn mã hóa Khối do chính phủ Mỹ phê duyệt, cực kỳ kiên cố chống phá mã bằng phương pháp vét cạn (Brute-force) nếu Mật khẩu đủ phức tạp.
D. ROT13.
*Đáp án: C*
*Giải thích: AES 256-bit là bức tường thép vững chắc bảo vệ mạng Wi-Fi, chưa có thuật toán toán học nào trên trái đất có thể giải ngược nó.*

**Câu 37:** Phương thức Tấn công WPA2 phổ biến nhất của Hacker (khi không dò được mật khẩu) là "Deauthentication Attack" (Tấn công Ngắt kết nối). Hacker làm gì?
A. Đánh cắp ổ cứng máy chủ.
B. Hacker "Giả mạo" (Spoof) Địa chỉ MAC của Cục Phát (AP), Gửi 1 Frame Lệnh (Deauth Frame) Không-mã-hóa vào mặt Điện thoại của nạn nhân hét lên: "Tôi là Cục phát, tôi đuổi anh ra khỏi mạng". Nạn nhân ngoan ngoãn ngắt mạng, sập hoàn toàn Wi-Fi.
C. Xóa DNS.
D. Gửi virus vào máy tính.
*Đáp án: B*
*Giải thích: Lỗ hổng ngu ngốc nhất của 802.11 cũ là Các Khung Lệnh (Management Frames) bay trần trụi không mã hóa. WPA3 sau này bổ sung PMF (Protected Management Frames) khóa chặt họng bọn Hacker chơi trò này.*

**Câu 38:** Giao thức MAC của Wi-Fi, CSMA/CA, quy định khoảng thời gian nghỉ ngắt quãng "DIFS" (Distributed Inter-Frame Space) dùng để:
A. Tăng băng thông cáp mạng.
B. Một thiết bị đang chờ để Phát, nếu nó cảm nhận thấy Đường không gian vô tuyến TRỐNG, nó vẫn KHÔNG ĐƯỢC PHÁT NGAY. Nó bắt buộc phải im lặng "Nhẫn nhịn" thêm một khoảng thời gian DIFS. Nếu qua thời gian đó vẫn trống, nó mới dám thả dữ liệu vào không khí.
C. Mã hóa tín hiệu.
D. Xin địa chỉ IP.
*Đáp án: B*
*Giải thích: Khoảng nghỉ này (cùng với SIFS cho các gói ưu tiên như ACK) tạo ra trật tự phân cấp sự nhường nhịn cho một đám đông mù mờ không có cảnh sát giao thông.*

**Câu 39:** Ứng dụng công nghệ "MIMO" (Multiple Input Multiple Output) trên chuẩn Wi-Fi 802.11n/ac có bản chất vật lý là:
A. Đặt thêm nhiều Router.
B. Sử dụng NHIỀU ĂNG-TEN phát và NHIỀU ĂNG-TEN thu trên cùng một Cục phát và Thiết bị (Ví dụ 2x2, 4x4). Truyền ĐỒNG THỜI nhiều luồng Dữ liệu Độc lập qua hiện tượng Đa đường (Multipath), nhân gấp đôi, gấp ba Băng thông cực đại thay vì bị suy hao.
C. Dùng 1 Ăng-ten cực to.
D. Kéo cáp quang vào máy.
*Đáp án: B*
*Giải thích: Trước MIMO, sự phản xạ dội sóng vào tường (Multipath) là kẻ thù gây nhiễu nát bét tín hiệu. MIMO sử dụng thuật toán xử lý không gian ma trận cực đỉnh để "Biến kẻ thù thành sức mạnh", thu thập các tia dội chắp vá lại thành Dữ liệu.*

**Câu 40:** Công nghệ Wi-Fi 6 (802.11ax) khác biệt VƯỢT TRỘI so với Wi-Fi 5 (802.11ac) nhờ áp dụng kiến trúc nào thừa hưởng từ Mạng 4G LTE?
A. Cáp đồng xoắn.
B. MU-MIMO truyền thống.
C. OFDMA (Orthogonal Frequency-Division Multiple Access). AP xẻ vụn Kênh băng tần lớn (vd 80MHz) thành hàng trăm Kênh Nhỏ xíu (Resource Units - RU). Nó TỰ ĐỘNG GIAO TỪNG KÊNH cho từng điện thoại, cho phép ĐỒNG THỜI hàng chục máy chơi Game cùng Truyền/Nhận data chung 1 lúc không phải xếp hàng (Đánh bại CSMA tranh chấp).
D. Phân bổ MAC tự do.
*Đáp án: C*
*Giải thích: Wi-Fi 5 rất nhanh, nhưng 20 người cùng cắm vào tải game thì mạng sẽ sập toàn tập vì ai cũng phải Xếp hàng chờ. Wi-Fi 6 chia vạch phân làn riêng cho mỗi xe tải, dẹp bỏ cảnh sát CSMA/CA lỗi thời.*

**Câu 41:** Hiện tượng "Far-Near Problem" (Gần-Xa) trong mạng vô tuyến (đặc biệt mạng điện thoại) nói lên việc:
A. Cáp dài làm suy yếu sóng.
B. Điện thoại ở GẦN trạm phát sóng sẽ dội tín hiệu quá MẠNH, át hoàn toàn tiếng nói thỏ thẻ của Điện thoại ở XA. Để giải quyết, Trạm phát phải dội lệnh (Power Control) YÊU CẦU CÁC MÁY GẦN giảm mức năng lượng phát sóng của chúng xuống, đảm bảo công bằng.
C. Máy xa tải nhanh hơn máy gần.
D. Không dùng cáp quang được.
*Đáp án: B*
*Giải thích: Giống như trong 1 phòng hội trường, thằng đứng sát mặt bạn nói thì thầm bạn cũng nghe rõ, nhưng thằng đứng xa phải hét to mới tới. Nếu thằng gần cũng hét to (phát Full Power) thì bạn sẽ bị điếc tai, không nghe được thằng ở xa nữa.*

**Câu 42:** Kiến trúc lõi mạng Hệ thống viễn thông 4G (Evolved Packet Core - EPC) có tính năng ĐỘT PHÁ nhất so với kiến trúc của 2G/3G cổ điển là gì?
A. Mạng 4G cấm dùng Internet.
B. 2G/3G phân làm 2 lõi (Lõi Thoại dùng chuyển mạch kênh truyền thống, Lõi Data dùng IP). 4G vứt bỏ Mạng Thoại Cổ Điển, sử dụng Kiến trúc HOÀN TOÀN DỰA TRÊN IP CHUYỂN MẠCH GÓI (All-IP Network). Mọi cuộc gọi thoại giờ đây là Luồng VoIP (VoLTE) ngang hàng với Video Youtube.
C. 4G mã hóa cáp đồng.
D. Dùng vệ tinh truyền tín hiệu.
*Đáp án: B*
*Giải thích: Điện thoại 2G/3G là công cụ nhắn tin sms/gọi điện truyền thống, kẹp thêm Internet. 4G/5G là một cái Máy Tính Internet Toàn diện, Tính năng gọi điện chỉ là 1 App (VoLTE) chạy trên nền IP.*

**Câu 43:** Kỹ thuật "Network Slicing" (Cắt lớp mạng) là tinh hoa của Mạng di động 5G. Mục đích chính của nó là:
A. Cắt cáp quang ra nhiều sợi.
B. Tắt nguồn Router.
C. Ảo hóa và Chia Cắt một Cơ sở hạ tầng 5G Vật lý duy nhất thành NHIỀU MẠNG ẢO LÔGIC ĐỘC LẬP. Lớp A dành riêng cho IoT (Băng thông thấp, Pin trâu), Lớp B cho Xe tự lái (Siêu trễ thấp URLLC), Lớp C cho Tải Video 4K (Băng thông khổng lồ eMBB). Mỗi lớp được tối ưu hóa đặc biệt.
D. Chặn mã độc virus.
*Đáp án: C*
*Giải thích: Một mạng MỘT-KÍCH-CỠ-PHÙ-HỢP-MỌI-NGƯỜI (như 4G) không thể đáp ứng vừa Băng thông 10Gbps, vừa Độ trễ 1ms, vừa Phục vụ hàng triệu Cảm biến nhiệt độ được. Slicing sinh ra để "Tùy biến" mạng theo yêu cầu ứng dụng.*

**Câu 44:** Thuật ngữ "MME" (Mobility Management Entity) trong Lõi mạng 4G EPC làm nhiệm vụ cực kỳ sống còn nào?
A. Phát sóng Wi-Fi.
B. Lưu trữ file phim.
C. Là Não Bộ (Control Plane) của mạng 4G. Xử lý việc Xác thực SIM (Paging), Giám sát Vị trí (Location tracking), Cấp phát IP và ra lệnh Thiết lập Đường Hầm (Tunnels) từ Điện thoại xuyên qua Trạm eNodeB đến Gateway Internet.
D. Mã hóa HTTPS.
*Đáp án: C*
*Giải thích: Khi bạn di chuyển sang Tỉnh khác, cái MME sẽ nhận sóng, tra cứu xem bạn đã đóng tiền cước chưa (HSS/HLR), rồi cấu hình đường dẫn mạng mới đến trạm phát sóng nhà mạng đang cắm (Rerouting).*

**Câu 45:** Sự khác biệt về việc "Cấp phát Kênh" giữa CDMA (Code Division Multiple Access - như mạng 3G/Mỹ) và TDMA (như GSM mạng 2G cũ) là:
A. Không có khác biệt.
B. TDMA chia thời gian (Mỗi người nói 1 giây). CDMA sử dụng MẬT MÃ TOÁN HỌC TRỰC GIAO (Orthogonal Codes). TẤT CẢ mọi người cùng dùng chung MỘT Tần số tại CÙNG MỘT THỜI ĐIỂM 100%. Tín hiệu bị trộn lẫn nát bét. Nhưng nhờ Mã Code duy nhất, Trạm thu có thể Lọc được chính xác tiếng của từng người khỏi cái mớ hỗn độn đó.
C. CDMA dùng cáp quang, TDMA dùng sóng.
D. TDMA nhanh hơn 100 lần.
*Đáp án: B*
*Giải thích: CDMA giống như 100 người ở sảnh chung cùng nói chuyện một lúc. Nhưng 2 người dùng tiếng Anh, 2 người tiếng Việt, 2 người tiếng Nhật. Họ tự tách riêng ngôn ngữ (Code) ra nghe mà không bị lẫn tiếng của nhau.*

**Câu 46:** Mạng di động (như 4G) đóng gói các Datagram IP của Trình duyệt điện thoại vào bên trong một Cấu trúc "Đường hầm GTP" (GPRS Tunneling Protocol) chạy xuyên mạng Lõi đến Cổng P-GW. Mục đích là để?
A. Tải phim nhanh hơn.
B. Giấu địa chỉ IP gốc của người dùng.
C. Hỗ trợ TÍNH LƯU ĐỘNG (Mobility). Gói tin từ bên ngoài Internet luôn nhắm về cái P-GW cố định. P-GW sẽ bọc gói đó trong Tunnel đẩy về Trạm phát sóng (eNodeB) hiện tại mà điện thoại đang cắm. Nếu người dùng di chuyển sang trạm mới, Tunnel được nắn hướng lại, giữ IP điện thoại không thay đổi và luồng TCP luôn bền vững.
D. Bắt sóng Wi-Fi.
*Đáp án: C*
*Giải thích: Đây là giải pháp hoàn hảo cho "Mobile IP". Mạng 4G tạo một Lớp Đóng Gói (Encapsulation L2.5) khổng lồ, luân chuyển ngầm luồng dữ liệu (Tunneling) theo dấu người dùng từ Bắc chí Nam.*

**Câu 47:** Mạng Wi-Fi cá nhân (như ghép Hotspot di động) sử dụng dải IP nội bộ và NAT, thế nhưng Mạng 4G của Nhà cung cấp viễn thông cấp cho điện thoại của bạn cái gì?
A. Cấp cho điện thoại 1 IP Public Mỹ.
B. Thực tế đa số các nhà mạng trên thế giới vẫn cấp IP NỘI BỘ (Ví dụ dải 10.x.x.x) cho điện thoại, và áp dụng hệ thống CGNAT (Carrier-Grade NAT) cấp nhà mạng siêu khổng lồ tại P-GW để dịch hàng triệu điện thoại ra 1 vài IP Public.
C. Cấp MAC động.
D. Cấp IPv4 tĩnh cho từng người.
*Đáp án: B*
*Giải thích: Lý do bạn cắm SIM 4G phát máy chủ Web ở nhà, không ai ngoài Internet có thể truy cập được. Bạn bị kẹt sau tường NAT khổng lồ của Viettel/VNPT.*

**Câu 48:** Yếu tố vật lý nào làm giới hạn KHOẢNG CÁCH của công nghệ sóng Milimet (mmWave) được sử dụng để đạt tốc độ 10Gbps trong Mạng 5G hiện nay?
A. Thiếu nguồn điện.
B. Băng tần Tần số siêu cao (Vd 28 GHz). Tần số càng cao, bước sóng càng cực kỳ nhỏ. Sóng này không có khả năng đi xuyên qua kính, tường, hay lá cây, và bị Suy hao do Oxy trong không khí hấp thụ mạnh. Khoảng cách phát chỉ đạt vài chục đến hàng trăm mét và bắt buộc phải Nhìn Thấy Trực Tiếp (Line of Sight).
C. Không thể giải mã.
D. Tốn gói tin UDP.
*Đáp án: B*
*Giải thích: 5G tốc độ siêu tốc giống như Ánh sáng Đèn pin. Chỉ chiếu được gần và đi thẳng. Để phủ sóng 1 thành phố 5G mmWave cần xây Hàng vạn trạm phát siêu nhỏ (Small Cells) thay vì 1 cái Tháp vô tuyến to của 3G.*

**Câu 49:** Tại sao chuẩn Bảo mật Mạng doanh nghiệp "WPA2-Enterprise (802.1x)" lại an toàn hơn chuẩn gia đình "WPA2-Personal (PSK)"?
A. Mật khẩu gia đình bị chặn.
B. Không an toàn hơn.
C. Cả nhà dùng chung 1 Mật khẩu Wi-Fi (PSK) - Lộ pass là mọi người đều lén vào được mạng. Mạng Doanh nghiệp yêu cầu TỪNG TÀI KHOẢN nhân viên phải nhập Username/Password riêng biệt, gửi về Server RADIUS để check. Khi nghỉ việc, chỉ cần xóa tài khoản người đó mà không phải đổi pass Wi-Fi của công ty.
D. Cáp đồng dài hơn.
*Đáp án: C*
*Giải thích: Trong WPA2-Enterprise, bộ phát (AP) không lưu trữ hay biết Mật khẩu của ai cả. Mọi thứ được mã hóa và chuyển cho Máy chủ Thẩm định tập trung xử lý.*

**Câu 50:** Sự kết hợp giữa Giao thức Điều khiển Kết nối (TCP) và Môi trường Không Dây (Wireless) tạo ra một VẤN ĐỀ LỚN là "TCP over Wireless Problem". Vấn đề đó sinh ra do đâu?
A. TCP đòi hỏi cổng kết nối cắm cáp.
B. Lỗi "Diễn giải sai nguyên nhân mất gói". Sóng vô tuyến cực kỳ chập chờn, dội phản xạ, che khuất, làm Mất 1 gói tin vì lỗi Lớp 1 (Vật lý). Giao thức TCP mù quáng lầm tưởng đó là TẮC NGHẼN ROUTER, lập tức tụt nửa tốc độ và bò lê lết, đánh sập Băng thông thực tế của thiết bị không dây.
C. Không thể phân mảnh IPv6.
D. Giao thức UDP khóa mạng.
*Đáp án: B*
*Giải thích: Đây là tử huyệt của kiến trúc. Lớp 4 (TCP) không có con mắt nhìn xuống Lớp 1 (Sóng). Nó chỉ thấy 1 loại dấu hiệu (Mất gói) và áp dụng duy nhất 1 liều thuốc (Đạp phanh giảm tốc). Thuốc này sai bệnh hoàn toàn với mạng Sóng.*

**Câu 51:** Lựa chọn giải pháp nào thường được Áp dụng (trong các Proxy Không dây hoặc Split TCP) để giải quyết vấn đề "TCP over Wireless"?
A. Tắt Wi-Fi.
B. Cắt đôi kết nối TCP. Từ Trình duyệt đến Trạm phát (AP) dùng giao thức khác chịu lỗi vô tuyến tốt hơn. Từ Trạm phát (AP) về Máy chủ dùng TCP có dây thông thường. Ngăn không cho sự dở tệ của đoạn Wi-Fi lan truyền ảnh hưởng tốc độ của đoạn Mạng cáp quang Lõi.
C. Thay bằng UDP thuần túy.
D. Dùng TCP Tahoe.
*Đáp án: B*
*Giải thích: Nếu 1 chiếc xe tải chạy trên 1 con đường 100km (Trong đó 99km đường nhựa, 1km đường sình lầy), tốc độ cả chuyến sẽ bị kéo lùi thê thảm. Split TCP cắt chiếc xe làm 2, 1 xe siêu nhanh chạy 99km, 1 xe bánh xích chuyên chạy đường bùn.*

**Câu 52:** Thuật toán Handoff (Chuyển giao) của Mạng Viễn Thông 4G sẽ "Cứng" (Hard Handoff) hay "Mềm" (Soft Handoff)?
A. Hoàn toàn cứng (Break-before-Make). Điện thoại PHẢI Ngắt kết nối với Trạm cũ hoàn toàn trước khi Mở kết nối Sóng vô tuyến với Trạm mới. Gây gián đoạn một vài mili-giây nhưng tối giản hóa phần cứng.
B. Hoàn toàn mềm (Make-before-Break).
C. Không hỗ trợ Handoff.
D. Dùng 3G song song.
*Đáp án: A*
*Giải thích: Ở hệ thống 3G (CDMA) người ta dùng Soft Handoff (1 lúc bắt sóng 2 trạm). Lên 4G LTE, để đạt tốc độ Gigabit siêu cao, họ bỏ luôn Soft Handoff vì việc duy trì 2 luồng sóng tốc độ cao song song là quá tốn tần số vô tuyến. Họ chấp nhận "Đứt 1 nhịp chớp mắt" để kết nối.*

**Câu 53:** Lỗi "Roaming" (Chuyển vùng) trong Wi-Fi nội bộ nhà bạn (có 2 cục phát lầu 1 và lầu 2 cùng tên pass) thường là do nguyên nhân Lớp 2 nào?
A. Cáp đồng bị nghẽn.
B. Điện thoại (Client) có Quyền Quyết Định Tuyệt Đối việc "Khi nào thì bứt sóng". Thường thì Client rất "Lì", dù sóng Lầu 1 còn 1 vạch thoi thóp, nó vẫn bám chặt lấy không chịu nhả để bắt sóng Lầu 2 (Sóng đầy), gây rớt mạng giả tạo.
C. Do IP bị tràn.
D. Do Router hỏng ăng-ten.
*Đáp án: B*
*Giải thích: Khác với Mạng di động 4G (Trạm phát đóng vai trò ra lệnh Bắt Điện thoại phải ngắt sóng chuyển trạm). Mạng Wi-Fi dân dụng thì cục Phát là bị động, Mọi quyền lực Roaming nằm trong tay Hệ điều hành Điện thoại (Apple/Android).*

**Câu 54:** Để ép các thiết bị Khách hàng Roaming (Chuyển vùng Wi-Fi) mượt mà hơn, các Hệ thống Wi-Fi Doanh nghiệp (Controller-based) làm thủ thuật gì?
A. Mã hóa cáp mạng.
B. Mở TCP Window size.
C. Sử dụng chuẩn 802.11r/k/v, kết hợp việc AP Gửi tín hiệu Gợi ý chuyển trạm, hoặc Tàn Nhẫn hơn (như RSSI Kick): AP chủ động "Đá" (Ngắt kết nối) thiết bị Khách nếu sóng thu được từ Khách rớt xuống mức quá yếu, ép Khách phải đi tìm AP khác.
D. Xin đổi IPv6.
*Đáp án: C*
*Giải thích: Controller (Não bộ mạng doanh nghiệp) theo dõi vị trí của bạn, nếu bạn đi xa cục AP 1, nó sẽ ra lệnh cục AP 1 đạp bạn văng ra để bạn tự kết nối vào cục AP 2 gần nhất.*

**Câu 55:** Mô hình "Mobile IP" sử dụng "Care-of Address" (COA - Địa chỉ Chăm sóc Tạm thời). COA được lấy từ đâu?
A. Tự bịa ra.
B. Do Router lõi cấp ngẫu nhiên.
C. Do Mạng Khách (Foreign Network) mà thiết bị di động VỪA ĐI VÀO (Ví dụ: Bạn xách máy từ công ty ra quán cafe, thì Quán Cafe cấp cho bạn 1 cái IP mới của quán, đó chính là COA).
D. Do nhà sản xuất cấp.
*Đáp án: C*
*Giải thích: COA là Tọa độ tạm trú của bạn. Máy ở nhà (Home Agent) sẽ bọc thư gửi từ bạn bè vào một đường hầm IPsec/GRE gửi theo cái địa chỉ COA Tạm trú này.*

**Câu 56:** Công nghệ 5G có khái niệm "Beamforming" (Tạo chùm tia). Kỹ thuật này hoạt động ở Tầng Vật Lý như thế nào?
A. Giảm kích thước pin.
B. Thay vì bóng đèn phát sáng tỏa tròn (Đa hướng vô lăng) làm lãng phí năng lượng, Hệ thống ăng-ten Ma trận Khổng lồ (Massive MIMO) dùng Toán học để Hội tụ sóng lại thành một "Tia Laser vô hình", bám theo và Bắn thẳng vào CỤ THỂ một thiết bị người dùng đang di chuyển.
C. Bỏ qua tần số.
D. Phát sóng liên tục.
*Đáp án: B*
*Giải thích: Đỉnh cao công nghệ Vô tuyến điện. Beamforming tăng cường cường độ tín hiệu gấp hàng chục lần, và giúp Trạm phát có thể "bắn" nhiều tia cùng lúc vào nhiều người dùng khác nhau bằng OFDMA.*

**Câu 57:** Chuẩn 802.11ac (Wi-Fi 5) hoạt động CHỦ YẾU trên băng tần nào và mang lại lợi ích gì?
A. Hoạt động trên 2.4 GHz, xuyên tường cực mạnh.
B. Hoạt động trên Băng tần 5 GHz. Băng tần này siêu RỘNG, cho phép ghép nhiều kênh (VD: 80MHz hoặc 160MHz) tạo ra các ống truyền dữ liệu khổng lồ (Lên tới hàng Gbps). Đổi lại, độ xuyên tường rất kém.
C. Hoạt động trên cáp quang.
D. Dùng sóng Bluetooth 10m.
*Đáp án: B*
*Giải thích: Băng tần 2.4 GHz giống đường làng chật chội (chỉ ghép tối đa 40MHz). 5 GHz là Đại lộ siêu cao tốc mênh mông, nhưng lại bị đồi núi/nhà cửa cản trở sóng.*

**Câu 58:** Đâu KHÔNG phải là một mối đe dọa (Threat) phổ biến riêng biệt cho mạng Không dây (Wireless) so với Mạng Có Dây?
A. Nghe lén (Eavesdropping). Bất kỳ ai mang ăng-ten là thu được tín hiệu, không cần đục cáp.
B. Phá sóng, Gây nhiễu (Jamming). Phát một tín hiệu rác công suất lớn trùng tần số để đánh sập mạng.
C. Rút cáp vật lý của Switch phòng máy chủ.
D. Điểm truy cập Giả mạo (Rogue/Evil Twin AP). Kẻ xấu phát một Wi-Fi Tên y hệt Wi-Fi quán cafe để lừa người dùng kết nối vào ăn trộm mật khẩu.
*Đáp án: C*
*Giải thích: Mạng không dây chịu 100% rủi ro của mạng dây, cộng thêm một đống rủi ro vật lý vô tuyến do "Không khí" là một Môi trường chia sẻ, mở tâng hoác cho toàn thế giới.*

**Câu 59:** Tầng Liên kết dữ liệu của mạng Vệ Tinh, do Đặc thù Lớp 1 (Vật lý trễ siêu lớn 250ms), phải thay đổi thông số Lớp 2 nào để không làm sập TCP?
A. Tắt CRC.
B. Sử dụng "Window Scaling" cho TCP. Và Ở Lớp 2, phải dùng Kích thước Khung (Frame) Siêu To hoặc Kéo dài Bộ Định Thời (Timer) của Lớp 2 ARQ (Automatic Repeat reQuest) để không truyền lại mù quáng.
C. Nén IP bằng thuật toán zip.
D. Giao thức UDP.
*Đáp án: B*
*Giải thích: Thiết kế mạng bao giờ cũng là bài toán dây chuyền. Lớp 1 chậm -> Lớp 2 phải thay đổi kích thước gói/timer -> Lớp 4 (TCP) phải giãn cửa sổ.*

**Câu 60:** Việc xác định Mật khẩu Bảo mật trên thiết bị IoT (Internet of Things) sử dụng giao thức mạng vô tuyến (như ZigBee, Z-Wave) có một thách thức CỰC LỚN là:
A. IoT không dùng IP.
B. Thiết bị IoT không có màn hình hoặc bàn phím để gõ Mật khẩu Wi-Fi. (Ví dụ: Bóng đèn thông minh). Việc khởi tạo xác thực an toàn lần đầu (Provisioning/Onboarding) luôn bị hacker rình rập bằng Sniffer.
C. IoT luôn dùng cáp LAN.
D. Tốn điện năng quá cao.
*Đáp án: B*
*Giải thích: Bạn mua bóng đèn Xiaomi về, muốn bóng kết nối Wi-Fi nhà bạn thì phải dùng App trên điện thoại truyền Pass sang bóng đèn. Bước truyền Pass này (nếu làm qua sóng Bluetooth/Wi-Fi Direct rác) là lỗ hổng to đùng.*

**Câu 61:** Mạng di động 5G sử dụng dải tần số nào để đạt được tốc độ tải dữ liệu lên tới hàng Gigabit/giây (vượt trội hoàn toàn 4G)?
A. Dải tần số cực thấp dưới 100 MHz.
B. Băng tần vệ tinh C-Band.
C. Sóng Milimet (mmWave - ví dụ từ 24 GHz đến 100 GHz) kết hợp với các băng tần Trung (Sub-6 GHz) và Thấp để đảm bảo phủ sóng. Băng tần mmWave cực rộng cho phép truyền lượng dữ liệu khổng lồ nhưng phạm vi rất ngắn.
D. Ánh sáng hồng ngoại.
*Đáp án: C*
*Giải thích: Băng tần càng cao, khả năng chuyên chở data càng khủng, nhưng điểm yếu chết người là sóng dễ bị chặn bởi tờ giấy hoặc giọt mưa.*

**Câu 62:** Cơ chế "Carrier Sense" (Lắng nghe đường truyền) trong Wi-Fi CSMA/CA thực hiện việc cảm nhận không gian vô tuyến thông qua yếu tố nào?
A. Cảm nhận ánh sáng.
B. Cảm nhận Năng lượng (Energy Detection) và Nhận dạng Tín hiệu (Preamble Detect). Trạm phát sẽ đo mức năng lượng vô tuyến hiện tại trong không khí, nếu vượt ngưỡng (có người đang phát), nó sẽ lùi lại.
C. Hỏi xin phép Server.
D. Dùng vệ tinh đo.
*Đáp án: B*
*Giải thích: Đơn giản là việc "Áp tai vào tường" xem có tiếng ồn không. Nếu không khí có điện áp sóng RF cao, máy tính sẽ khóa mỏ không phát.*

**Câu 63:** Lỗ hổng WPA2 "KRACK" (Key Reinstallation Attack) kinh điển do chuyên gia bảo mật phát hiện năm 2017 đánh vào giai đoạn nào của Wi-Fi?
A. Giải mã cáp mạng.
B. Tấn công DNS.
C. Quá trình Bắt tay 4 bước (4-Way Handshake) khi thiết lập kết nối mã hóa. Hacker ép thiết bị nạn nhân "Cài đặt lại" một chìa khóa cũ có bộ đếm đã bị reset, từ đó Hacker có thể giải mã 100% dữ liệu truyền qua Wi-Fi WPA2 dù không biết Pass.
D. Xóa mật khẩu bằng USB.
*Đáp án: C*
*Giải thích: Sự kiện chấn động toàn cầu khiến mọi máy tính, điện thoại, router phải tung bản vá khẩn cấp. Lỗ hổng nằm ở cấp độ Thiết kế Chuẩn Giao thức của IEEE chứ không phải do người dùng đặt pass yếu.*

**Câu 64:** Thiết bị nào là ranh giới "Chuyển tiếp" giữa mạng lõi Viễn thông 4G IP (EPC) và mạng Internet Công cộng toàn cầu?
A. eNodeB (Trạm phát sóng).
B. MME (Bộ quản lý di động).
C. S-GW (Serving Gateway).
D. P-GW (PDN Gateway - Packet Data Network Gateway). Nó đóng vai trò là Tường lửa, NAT, Ghi cước (Billing), và Cửa ngõ tống dữ liệu IP từ điện thoại ra Internet.
*Đáp án: D*
*Giải thích: P-GW là "Hải quan cửa khẩu". Mọi luồng Data của bạn đều phải chui qua đây để nhà mạng tính tiền Data 4G trước khi thả bạn ra Internet.*

**Câu 65:** "Wi-Fi Direct" có tính năng khác biệt nào so với Bluetooth trong việc chia sẻ File giữa 2 điện thoại (như AirDrop/ShareMe)?
A. Wi-Fi Direct dùng cáp.
B. Tầm hoạt động của Wi-Fi Direct hẹp hơn Bluetooth.
C. Wi-Fi Direct tạo ra một kết nối ngang hàng (Ad-hoc P2P) TRỰC TIẾP giữa 2 thiết bị mà KHÔNG CẦN CỤC PHÁT (AP) TRUNG GIAN, cung cấp tốc độ chuyển file băng thông siêu rộng (Gigabit) của Wi-Fi, ăn đứt Bluetooth chậm chạp.
D. Không cần dùng mật khẩu.
*Đáp án: C*
*Giải thích: Bluetooth sinh ra cho bàn phím/chuột (tốc độ thấp, tốn ít pin). Chuyển 1 video 4K bằng Bluetooth mất cả ngày, nhưng Wi-Fi Direct chỉ mất vài giây.*

**Câu 66:** Trong công nghệ Wi-Fi 6 (802.11ax), màu BSS (BSS Coloring) được sinh ra để khắc phục nhược điểm gì ở khu chung cư đông đúc?
A. Cấp IP chậm.
B. Giảm nhiễu trùng kênh (Co-channel Interference). Khi cục phát nhà bạn và nhà hàng xóm xuyên tường đều dùng Kênh 6. Thiết bị sẽ bị "Điếc" nhầm, phải đợi hàng xóm phát xong mới dám phát. BSS Coloring tô thêm 1 con số (Màu) vào Frame, điện thoại thấy Frame Kênh 6 nhưng "Khác Màu" nhà mình, nó tự tin coi đó là rác, BỎ QUA và PHÁT ĐÈ LÊN LUÔN mà không thèm chờ.
C. Đổi pass liên tục.
D. Nén video HD.
*Đáp án: B*
*Giải thích: Tính năng tái sử dụng không gian mạng (Spatial Reuse) đỉnh cao giúp Wi-Fi 6 duy trì sức mạnh tuyệt đối ở chung cư dày đặc.*

**Câu 67:** Khi di chuyển từ Mạng 3G lên Mạng 4G LTE, khái niệm "Độ Trễ" (Latency) được cải thiện đột phá (Giảm từ 100ms xuống còn ~20ms) là nhờ việc gì ở Kiến trúc Mạng Truy cập (RAN)?
A. Đẩy nhanh cáp đồng.
B. Rút ngắn Cấu trúc Rườm rà. Mạng 3G có một thiết bị quản lý trung gian RNC đứng giữa Cột phát và Mạng lõi. 4G LTE LOẠI BỎ RNC, cho Cột phát (eNodeB) THÔNG TRỰC TIẾP vào Mạng lõi IP (EPC), cắt giảm đi một trạm dừng chân gây trễ khổng lồ.
C. Đổi IP liên tục.
D. Tắt mã hóa.
*Đáp án: B*
*Giải thích: "Bẹt hóa" mạng (Flat Network Architecture) là bí quyết cốt lõi để mạng di động đuổi kịp tốc độ phản hồi của cáp quang cá nhân.*

**Câu 68:** Chuẩn 802.11w ra đời tích hợp "Protected Management Frames" (PMF) để ngăn chặn kiểu tấn công nào?
A. DDoS bằng ICMP.
B. SQL Injection.
C. Tấn công Hủy Xác Thực (Deauthentication Attack). PMF mã hóa và xác thực các Khung Lệnh Điều Khiển (Management Frames), nên Kẻ xấu KHÔNG THỂ giả danh cục phát (AP) để dội lệnh "Đá văng" (Kick) thiết bị nạn nhân ra khỏi Wi-Fi được nữa.
D. Rút cáp LAN.
*Đáp án: C*
*Giải thích: Từ WPA3, tính năng PMF này chuyển thành BẮT BUỘC, đóng sầm cánh cửa dễ dãi nhất của tin tặc.*

**Câu 69:** Hệ thống Cáp Biển quang học quốc tế đóng vai trò thế nào đối với Mạng 4G/5G Di Động?
A. Không liên quan.
B. Mạng di động chỉ không dây ở "Đoạn Không Khí Cuối Cùng" (Last Mile) từ Cột phát đến Điện thoại. Từ Cột phát trở đi về Mạng Lõi và Xuyên Quốc Tế VẪN CHẠY 100% TRÊN CÁP QUANG NGẦM. Đứt cáp biển thì 5G vẫn nghẽn mạng lướt web quốc tế y hệt Wi-Fi.
C. 5G chạy hoàn toàn bằng vệ tinh.
D. Tự phát IP nội bộ.
*Đáp án: B*
*Giải thích: Ảo tưởng "Không dây hoàn toàn" là sai lầm. Di động chỉ giải quyết rào cản kết nối cục bộ của thiết bị di chuyển.*

**Câu 70:** Khi điện thoại của bạn đang dùng Data 4G tải 1 file, sau đó bạn bước vào nhà, Hệ điều hành kết nối vào Wi-Fi. Phiên tải file (TCP Session) có thể tiếp tục diễn ra bình thường hay không?
A. Chạy tiếp ngay lập tức.
B. TCP Session bị NGẮT ĐỨT HOÀN TOÀN. Nguyên nhân là Mạng Wi-Fi và Mạng 4G thuộc HAI NHÀ CUNG CẤP CẤP 2 IP KHÁC NHAU. Bộ 4 Thông số TCP (Source IP) bị thay đổi cái rụp, Máy chủ Web sẽ không chấp nhận phiên TCP với IP lạ, File tải bị lỗi (trừ khi dùng Tool hỗ trợ tải lại từ vị trí đứt - Resumable HTTP GET).
C. Tốc độ tăng gấp đôi.
D. Tự đổi IP thành IPv6.
*Đáp án: B*
*Giải thích: Sự thay đổi IP Tầng 3 phá vỡ hoàn toàn định dạng Tầng 4. MPTCP và QUIC đang khắc phục điểm yếu lịch sử này trên di động.*

**Câu 71:** Ứng dụng "Viber" hay "Zalo" thực hiện gọi điện thoại (VoIP) bằng sóng 3G/4G, giao thức Giao vận nào được dùng làm xương sống để nhồi tiếng nói?
A. HTTP
B. RTP (Real-time Transport Protocol) chạy trên nền UDP.
C. TCP
D. BGP
*Đáp án: B*
*Giải thích: Giao thức ứng dụng đóng gói Time-stamp, Sequence để App xếp khung hình. Nằm trên UDP nhẹ, trượt đi cực mượt không bị khựng hình.*

**Câu 72:** Cấu trúc mạng Cell (Tế bào) trong hệ thống Di động 2G/3G sử dụng khái niệm "MSC" (Mobile Switching Center). MSC giống với thiết bị nào ở mạng dây?
A. Router Core Lớp 3. Tổng đài MSC quản lý việc Chuyển mạch cuộc gọi, Ghi cước, Điều phối Handoff diện rộng.
B. Cáp đồng.
C. Màn hình điện thoại.
D. Modem Wi-Fi.
*Đáp án: A*
*Giải thích: MSC là trái tim định tuyến của Mạng Thoại Cổ Điển (Circuit Switching), trước khi bị thay thế bằng Kiến trúc All-IP ở thế hệ 4G.*

**Câu 73:** Công nghệ MU-MIMO (Multi-User MIMO) ở Wi-Fi 5 (802.11ac) hỗ trợ hướng giao tiếp nào ưu việt hơn SU-MIMO cũ?
A. Tắt Wi-Fi ban đêm.
B. Đổi mật khẩu.
C. Cho phép Router PHÁT DỮ LIỆU ĐỒNG THỜI (Downlink) ĐẾN NHIỀU ĐIỆN THOẠI KHÁC NHAU CÙNG MỘT LÚC trên cùng một tần số, bằng cách lợi dụng các Ăng-ten và điều hướng sóng (Beamforming) tránh đâm vào nhau. Thay vì phải "Xếp hàng phát từng máy một".
D. Nhắn tin qua lại.
*Đáp án: C*
*Giải thích: Bước tiến vĩ đại dập bỏ sự tù túng của mạng Share Broadcast. Router giờ đây như ông thầy giáo có nhiều miệng, đọc cho 4 trò chép bài cùng lúc.*

**Câu 74:** Đặc tính kỹ thuật cốt lõi làm nên tiêu chuẩn Mạng 5G là "URLLC" (Ultra-Reliable Low-Latency Communication - Giao tiếp siêu tin cậy trễ siêu thấp). Mục tiêu của URLLC là gì?
A. Tải phim nhanh.
B. Lướt web mượt.
C. Phục vụ các ứng dụng RỦI RO SINH MẠNG đòi hỏi ĐỘ TRỄ GẦN NHƯ BẰNG 0 (1 mili-giây) và TIN CẬY 99.999% (Ví dụ: Xe tự lái tránh chướng ngại vật, Robot Phẫu thuật nội tạng từ xa).
D. Gửi Email.
*Đáp án: C*
*Giải thích: 5G không sinh ra để tải Youtube (4G thừa sức). 5G nhắm vào "Cách mạng Công nghiệp" (M2M) để máy móc tự động hóa thay thế con người xử lý Real-time.*

**Câu 75:** Trong môi trường mạng Không Dây, vì sao Kích thước Frame L2 bị giới hạn nhỏ hơn (Ví dụ Tối đa 2304 Bytes trên 802.11) thay vì truyền khung Jumbo 9000 Bytes như cáp quang?
A. Vì ăng-ten quá bé.
B. Vì Sóng rất dễ bị nhiễu. Frame càng To -> Xác suất đang truyền giữa chừng bị tia chớp/sóng tạp đập vào làm Xước Méo Lỗi (Lỗi FCS) Càng Cao. Nếu Frame bự bị hỏng, phải Truyền Lại nguyên cục to đùng cực tốn băng thông. Frame nhỏ chia rủi ro ra, Hỏng cục nhỏ truyền lại rẹt cái là xong.
C. Vì thiếu điện năng.
D. Mã hóa WPA bị chặn.
*Đáp án: B*
*Giải thích: Nguyên lý thiết kế: Môi trường dơ bẩn (nhiễu cao) thì chở hàng bằng thùng nhỏ. Môi trường siêu sạch (cáp quang 0 nhiễu) thì chở hàng bằng Container bự.*

**Câu 76:** Công cụ "WPS" (Wi-Fi Protected Setup) trên các Router Wi-Fi thường hay bị tắt đi bởi dân Kỹ thuật chuyên nghiệp vì lý do bảo mật gì?
A. Vì nó tốn RAM.
B. Lỗ hổng Mã PIN. Mã PIN của WPS chia làm 2 nửa độc lập, Hacker dùng Tool (như Reaver) vét cạn từng nửa một, tốn khoảng vài chục ngàn phép thử (Vài giờ đồng hồ) là Dò Ra Mã PIN. Từ mã PIN này, Router ngoan ngoãn NỘP LUÔN CÁI MẬT KHẨU WPA2 CHÍNH CHO HACKER dù mật khẩu dài tới 20 ký tự phức tạp.
C. Không hỗ trợ IPv6.
D. Máy tính nóng.
*Đáp án: B*
*Giải thích: Sự Thỏa Hiệp giữa Tiện Dụng và Bảo Mật. Tiện dụng bấm nút (hoặc gõ PIN 8 số) đổi lấy việc vứt bỏ toàn bộ nỗ lực Cài Pass Dày 20 Ký Tự.*

**Câu 77:** Để quản lý lưu lượng truyền dẫn khổng lồ của Mạng 5G, nhà mạng sử dụng công nghệ "SFC" (Service Function Chaining) ở Tầng Lõi Mạng (SDN/NFV) với bản chất:
A. Cắt cáp mạng.
B. Khởi động lại Server.
C. Ghép xâu chuỗi (Chaining) các "Hộp Chức Năng Ảo Hóa" (Firewall Ảo, NAT Ảo, Bộ Lọc Rác Ảo) chạy hoàn toàn bằng Phần mềm (VMs) trên máy chủ Cloud. Gói tin IP tự động lướt qua xâu chuỗi này để được xử lý linh hoạt, chấm dứt việc phải mua các cục phần cứng Firewall, NAT Cisco đắt tiền cắm vật lý.
D. Biến IP thành MAC.
*Đáp án: C*
*Giải thích: Đỉnh cao NFV (Network Functions Virtualization). Viễn thông biến toàn bộ trạm phần cứng thành các Tòa nhà Cloud Server phần mềm.*

**Câu 78:** Mạng vệ tinh LEO (Low Earth Orbit - Quỹ đạo Thấp) như Starlink của Elon Musk khắc phục nhược điểm chí tử nào của Vệ tinh GEO (Địa tĩnh) đời cũ?
A. Vệ tinh to quá.
B. Tắt mạng nhanh.
C. Giảm Độ Trễ (Latency) Rất Sâu. GEO ở tít 36.000km, dội xuống mất 250ms+ gây giật lag Game/Gọi thoại thê thảm. LEO chỉ ở độ cao 500km, Ping RTT dội xuống trái đất chỉ khoảng 30-40ms, ngang ngửa cáp quang trên đất liền, giúp TCP hoạt động hoàn hảo.
D. Không dùng điện.
*Đáp án: C*
*Giải thích: Vệ tinh LEO là cuộc cách mạng mang Internet băng rộng thực sự (Có thể Call, Chơi game Real-time) phủ sóng toàn bộ rừng núi, hải đảo.*

**Câu 79:** Kỹ thuật Bluetooth Low Energy (BLE) hy sinh Đặc tính Gì để đánh đổi lấy khả năng Chạy viên pin đồng hồ được tới 2 năm?
A. Bỏ mã hóa.
B. Thay đổi băng tần.
C. Hy sinh BĂNG THÔNG và THỜI GIAN NGỦ. Máy phát BLE ngủ (Sleep) liên miên 99% thời gian, nó chỉ Thức Dậy nháy 1 xung tín hiệu Siêu Nhỏ Siêu Chậm (Vài Kbps) rồi lập tức Tắt Điện ngủ tiếp.
D. Ngắt địa chỉ IP.
*Đáp án: C*
*Giải thích: Hoàn hảo cho Thiết bị định vị (Airtag, Đồng hồ điện nước). Băng thông không phải là tất cả.*

**Câu 80:** Mạng di động (Mobility) khi thiết bị đi từ Tầng 1 Lên Tầng 5 trong công ty, Thiết Bị Client làm nhiệm vụ gì để Sóng không rớt?
A. Lập mạng VPN.
B. Liên tục rà quét (Scanning) âm thầm các kênh (Channels) khác để ĐO ĐẠC Cường độ Tín hiệu của các Access Point (AP) lân cận. Khi AP hiện tại yếu đi, Hệ điều hành lập tức ra Quyết định Bứt Rễ (Roam) sang ôm cục AP mới mạnh hơn. Mọi sự đều Lặng Lẽ dưới nền, người dùng không hề hay biết.
C. Đổi Subnet Mask.
D. Kéo lại TCP.
*Đáp án: B*
*Giải thích: Client Wi-Fi giống con Nhện đu tơ. Nó luôn văng tơ đi thăm dò những cột chắc chắn hơn để nhảy sang trước khi cột cũ bị gãy.*

**Câu 81:** Trong cấu trúc Tầng Liên kết của Wi-Fi, "Mac Address" thứ 3 (Address 3) trong Frame (khung) làm nhiệm vụ gì đối với Cấu trúc BSS Hạ tầng (có AP)?
A. Đánh dấu địa chỉ vệ tinh.
B. Chỉ ra địa chỉ MAC của Trạm Nguồn (Laptop).
C. Để chỉ đích danh Địa chỉ MAC của BỘ ĐỊNH TUYẾN (Router Interface) nối với AP (Nếu gói tin gửi ra Internet). Hoặc MAC Đích của Máy Tính B (Nếu gói gửi nội bộ mạng LAN). AP căn cứ vào MAC này để đẩy gói vào đường cáp LAN.
D. Làm mã bảo mật.
*Đáp án: C*
*Giải thích: Wi-Fi rắc rối vì AP là một Trạm Giao Vận L2. Nó cần 3 MAC: MAC điện thoại, MAC của cục AP (BSSID), và MAC của Cục Router phía sau Tường để nó biết ném rác ra cửa nào.*

**Câu 82:** Lỗ hổng KRACK (Key Reinstallation Attack) năm 2017 trên WPA2 KHÔNG đánh cấp được gì?
A. Mật khẩu thật (Passphrase) của Wi-Fi. Hacker giải mã được dữ liệu truyền (Packet Decryption) nhưng Lỗ hổng Toán học KRACK hoàn toàn không làm rò rỉ cái Mật khẩu Gốc của bạn. Do đó Cập nhật bản Vá là xong, KHÔNG CẦN phải đi Đổi Pass Wi-Fi.
B. Địa chỉ IP.
C. Mã MAC.
D. Tần số vô tuyến.
*Đáp án: A*
*Giải thích: Một sự hiểu lầm phổ biến của dân IT thời điểm đó là ùa đi đổi pass. Thực tế KRACK chỉ "bắt chước chìa khóa phụ", không ăn cắp được "phôi chìa khóa chính".*

**Câu 83:** Giao thức Mobile IP (IPv4) khắc phục vấn đề đứt kết nối TCP do Di chuyển bằng cách duy trì HAI ĐỊA CHỈ IP cho một thiết bị di động. Địa chỉ nào ĐƯỢC GIỮ CỐ ĐỊNH để định danh phiên TCP?
A. Địa chỉ MAC.
B. Địa chỉ Chăm sóc Tạm thời (Care-of Address).
C. Địa chỉ Thường trú (Home Address). Địa chỉ này do Mạng Gốc (Home Network) cấp vĩnh viễn, được dùng làm Source IP/Dest IP gốc bám chặt vào Kết nối TCP, giúp Máy Chủ Web không bao giờ biết bạn đang di chuyển.
D. Cổng Port.
*Đáp án: C*
*Giải thích: Home Address là CMTND. Còn Care-of Address là Khai báo tạm vắng tạm trú. Server Web luôn gửi thư về CMTND. Trưởng công an phường (Home Agent) sẽ bọc thư đó gửi tiếp vào địa chỉ Khách sạn bạn đang tạm trú.*

**Câu 84:** "Chặn lọc MAC" (MAC Filtering) cấu hình trên Router Wi-Fi Gia đình để cấm hàng xóm dùng ké mạng CÓ HIỆU QUẢ CAO KHÔNG trước Hacker?
A. Vô cùng hiệu quả.
B. HIỆU QUẢ CỰC THẤP (Vô Tác Dụng Mức Cơ Bản). Hacker chỉ cần bật Kali Linux, bật Monitor Mode bắt sóng bừa trong 1 phút, sẽ THẤY LỘ RÕ TẤT CẢ Địa Chỉ MAC Hợp Lệ của các máy tính nhà bạn đang dùng. Hacker Đổi (Spoof) MAC Của Mình thành MAC của bạn là Vượt Màn Lọc Cái Rụp.
C. Cháy cục Wi-Fi.
D. Router chặn ngay.
*Đáp án: B*
*Giải thích: MAC bay khỏa thân trên Lớp 2 không mã hóa. Bộ Lọc MAC chỉ là rào chắn mỏng lừa trẻ con, tuyệt đối không dùng làm biện pháp an ninh duy nhất.*

**Câu 85:** Mạng 5G phân loại 3 Kịch bản ứng dụng cốt lõi (Use Cases) được định nghĩa bởi ITU là gì?
A. eMBB (Băng thông siêu rộng), URLLC (Trễ siêu thấp siêu tin cậy), mMTC (Kết nối hàng triệu Thiết bị IoT mật độ dày đặc).
B. Tốc độ, Ổn định, Rẻ tiền.
C. IPv4, IPv6, MAC.
D. Web, Email, Chat.
*Đáp án: A*
*Giải thích: Ba trụ cột Thiết kế thay đổi Thế giới của 5G. Nhấn mạnh việc Mạng 5G không phải sinh ra chỉ để Lướt Web Nhanh (eMBB), mà sứ mệnh cao cả là Robot/Xe Tự Lái (URLLC) và Thành phố Thông minh (mMTC).*

**Câu 86:** Hiện tượng "Hidden Node" (Nút ẩn) trong không gian Wi-Fi có thể được giảm thiểu/giải quyết Triệt Để Nhất bằng cách:
A. Tăng băng thông Cáp quang.
B. Thiết lập Wi-Fi Pass mạnh.
C. Giao thức RTS/CTS (Request To Send / Clear To Send). Nút A hỏi Cục Phát "Cho em nói nhé (RTS)". Cục Phát Gào To Cả Làng "Thằng A Sắp Nói, Bọn Khác Im Ngay (CTS)". Nút C ở xa tít mù không thấy A, nhưng Lại Nghe Thấy Lệnh CTS của Cục Phát, C liền ngoan ngoãn Khóa Mõm Đứng Im Chờ, không đâm sóng vào A.
D. Đổi cáp mạng.
*Đáp án: C*
*Giải thích: Cách mạng Kỹ thuật giải bài toán Vô tuyến Cực hay. Dùng Chính Cái Loa Phường (Access Point) để Đảm bảo Trật Tự.*

**Câu 87:** Tín hiệu Bluetooth (PAN) làm sao sống sót chung trong môi trường 2.4 GHz đông đúc ngập tràn Sóng Wi-Fi và Lò Vi Sóng mà không bị nhiễu sập?
A. Vì Bluetooth sóng quá yếu.
B. Mã hóa cao siêu.
C. Công nghệ Nhảy Tần Thích Ứng (Adaptive Frequency Hopping - AFH). Bluetooth liên tục "nhảy cóc" đổi kênh sóng qua lại 1600 lần/giây giữa 79 kênh hẹp. Nếu nhảy trúng Kênh đang bị Wi-Fi lấn át, nó chỉ xịt rớt 1 tí Data rồi Vọt Sang Kênh Sạch Kế Tiếp Ngay Tức Khắc. Tránh bị kẹt chết ở một Lỗ Đen Tần Số.
D. Đặt gần máy vi tính.
*Đáp án: C*
*Giải thích: Chiến thuật "Bắn và Chạy" cực dị. Chấp nhận nhường kênh to cho Wi-Fi, tao chỉ lách vào khe hẹp lấy mẩu nhỏ rồi nhảy đi chỗ khác kiếm ăn.*

**Câu 88:** "WPA3" Mới Nhất Mang Lại Sự Bảo Mật Cách Mạng Nào Trong Cấu Hình "Mạng Khách Công Cộng Mở" (Open Wi-Fi Mật Khẩu OWE)?
A. Đóng Tường Lửa Ngay.
B. OWE (Opportunistic Wireless Encryption). Dù Bạn Ra Sân Bay Bấm Kết Nối Wi-Fi "Free_SBAy" KHÔNG CÓ PASSSWORD BẢO VỆ NÀO (Open), Thiết Bị Của Bạn Và Cục Phát AP VẪN NGẦM TỰ ĐỘNG THƯƠNG LƯỢNG SINH RA MỘT CHÌA KHÓA MÃ HÓA RIÊNG MÀ KHÔNG AI BIẾT. Hacker Bàn Bên Bắt Sóng Bạn Cũng KHÔNG ĐỌC ĐƯỢC CHỮ NÀO.
C. Chạy VPN Ẩn.
D. Phân Dải Tần Số 6GHz.
*Đáp án: B*
*Giải thích: Đỉnh Cao Của Tự Động Hóa An Ninh Khách Sạn/Sân Bay Tương Lai. Xóa Bỏ Vĩnh Viễn Thời Đại Dò Trộm Phiên Cookie Bằng Cục Phát Mở Rông.*

**Câu 89:** Tại Sao Vệ Tinh "VSAT" Băng Thông Rộng 50Mbps Lại Không Thể Dùng Làm Backhaul (Đường Truyền Lõi Cốt) Cho Trạm 4G Đặt Trên Đảo Xa Gọi Điện Thoại Di Động Tốt Được?
A. Vì VSAT Có Giá Thành Đắt.
B. DO ĐỘ TRỄ (LATENCY). Vệ Tinh Địa Tĩnh (GEO) Ở Độ Cao 36.000Km Dội Sóng Gây Trễ Ping Lên Tới 600ms (1 Chiều). Hệ Thống Viễn Thông Mạng Lõi 4G (EPC) Thường Set Timeout Cực Ngắn Cho Các Gói Báo Hiệu (Signaling). Trễ 600ms Làm Giao Thức Lõi 4G Bị Timeout Gãy Đổ Liên Tục, Rớt Cuộc Gọi Nhịp Cầu Đồng Bộ Liên Thông Thảm Hại.
C. Tín Hiệu Yếu Nhỏ.
D. Vệ Tinh Không Dùng IP.
*Đáp án: B*
*Giải thích: Bài Toán Xương Máu Thi Công Trạm Di Động Vùng Sâu. Các Lập Trình Viên Ericsson/Huawei Phải Viết Lại Thuật Toán Nới Lỏng TCP Timer Mới Ép Sống Được Con 4G Trạm Vệ Tinh GEO.*

**Câu 90:** Lớp "GTP" (GPRS Tunneling Protocol) Của Mạng Lõi IP Di Động (3G/4G) Chứa Thông Tin Gì Ở Lớp Ứng Dụng (Payload) Của Nó?
A. File Excel.
B. Virus Độc Hại.
C. NÓ CHỨA CHÍNH CÁI GÓI TIN IP CỦA ĐIỆN THOẠI NGƯỜI DÙNG (Kèm TCP/HTTP). Mạng Lõi Nhà Mạng (Viettel/Mobi) BỌC Gói IP Của Nạn Nhân Vào Trong Một Gói IP Của Trạm Phóng (eNodeB) Với Giao Thức Đệm Là UDP Cổng 2152 Của GTP. Giấu Mọi Hành Vi Duyệt Web Của Khách Vào Bụng Mạch Ống Đường Hầm Gửi Về Khách Sạn Cửa Khẩu Trung Tâm P-GW Tính Tiền Cước Data Vượt Trạm Chậm Trễ Mềm Dẻo Đổ Bịch Trắng Khống Rỗng Tức Rò IP Lướt Nhanh Bật.
D. Mật Mã Mã PIN Trạm Phóng.
*Đáp án: C*
*Giải thích: Sự Vận Dụng Huyền Diệu Của Khái Niệm Đóng Gói Lồng Nhau (Tunneling). Bạn Đang Xem Youtube TCP. Còn Mạng Lõi Vận Chuyển Gói Của Bạn Bằng UDP Tunnel Lên Xuống Vòng Qua Cột.*

**Câu 91:** Hệ thống "Handoff" trong mạng Di động xảy ra tình trạng "Ping-Pong Effect" (Chuyển vùng liên tục qua lại) do nguyên nhân Lớp Vô Tuyến nào?
A. Do IPsec chặn mã hóa.
B. Cáp đứt do sét.
C. Người dùng đứng đúng ở "Ranh giới" giao thoa sóng giữa 2 cột thu phát. Gió thổi lá cây hoặc bước đi 1 mét làm sóng Cột A mạnh hơn B, 1 giây sau B mạnh hơn A. Thiết bị liên tục Handoff qua lại giữa A và B mỗi giây gây kiệt quệ mạng lõi (Signaling Storm) và đứt sóng, tốn pin sập thiết bị rỗng mạch chuyển TCP hoảng loạn xả gói rớt thê thảm.
D. Do Tường lửa chặn Cổng.
*Đáp án: C*
*Giải thích: Để tránh hiệu ứng Ping-Pong, nhà mạng dùng chỉ số "Hysteresis Margin" (Biên độ trễ trớn). Cột B phải MẠNH HƠN HẲN cột A ít nhất 3dB trong thời gian 5 giây thì HĐH mới cho phép Rời cột A sang B.*

**Câu 92:** Tại sao kết nối Vệ tinh (Satellite Internet) thường sử dụng Tần số Siêu Cao (Ku, Ka band - Tức là trên 12 GHz)?
A. Vì Tần số cao đi trong nước dễ hơn.
B. Vì Cáp đồng không chịu được.
C. Tần số càng cao, Bước Sóng (Wavelength) càng NHỎ. Sóng ngắn dễ dàng đâm xuyên thẳng tắp qua Thượng tầng Khí quyển (Tầng Điện Ly) lướt vào vũ trụ mà không bị phản xạ dội ngược lại mặt đất như Tần số sóng Radio FM cũ kỹ. Đồng thời cung cấp Băng Thông Data cực rộng để nuôi hàng ngàn User tải phim cùng lúc dưới mặt đất bốc luồng lớn.
D. Biến TCP thành UDP ngay lập tức.
*Đáp án: C*
*Giải thích: Tần số là chìa khóa mở cánh cửa không gian. Sóng dài trượt bò trên cong trái đất, Sóng siêu ngắn đi thẳng tắp xuyên thủng bầu trời.*

**Câu 93:** Mạng "Bluetooth" sử dụng kiến trúc Mạng Lưới gì để kết nối nhiều hơn 2 thiết bị?
A. Cáp vòng Token.
B. Piconet và Scatternet. Trong Piconet, 1 thiết bị làm Master (Chủ) điều khiển tới 7 thiết bị Active Slaves (Tớ). Nó có thể nối nhiều Piconet lại (1 con Slave nhóm này làm Master nhóm kia) tạo thành lưới Scatternet rải rác. Vận hành cực kỳ tiết kiệm điện theo chu trình gác cổng thời gian chặt chẽ (Master nói thì Slave mới được nói).
C. Trạm Base Station.
D. Giao thức OSPF Nội bộ.
*Đáp án: B*
*Giải thích: Mô hình Chủ-Tớ (Master/Slave) của Bluetooth triệt tiêu hoàn toàn vụ đụng độ sóng (Collision) rác nhảm nhí của Wi-Fi, đổi lại sự phản hồi cực chậm không dùng cho lướt Web được.*

**Câu 94:** Cơ Chế Phân Bổ Kênh "Dynamic Frequency Selection" (DFS) Trong Băng Tần 5 GHz Của Wi-Fi 5/6 Có Chức Năng Bắt Buộc Gì Do Luật Pháp Quốc Tế Quy Định Ngặt Nghèo Gây Rớt Mạng Đột Ngột?
A. Quét Mã Thẻ Từ Ảo Tấn Công DNS Thủng Khớp Cứng Phụ Mạch Trắng TCP Khóc Ép Nâng Nhịp Phân Rã OSPF Rút.
B. Giải Nén IP Báo Chặn Mở MAC Giữ Sóng Đóng Bóp Hút Thảm Giảm.
C. Router Wi-Fi Đang Phát Sóng Ở Kênh Đẹp Tốc Độ Cao. ĐỘT NHIÊN NÓ PHÁT HIỆN "CÓ SÓNG RADAR CỦA QUÂN ĐỘI HOẶC SÂN BAY" XUẤT HIỆN Ở GẦN ĐÓ TRÊN CÙNG TẦN SỐ NÀY. Router BẮT BUỘC PHẢI LẬP TỨC TẮT KÊNH NÀY NGAY TRONG VÀI MILI GIÂY Và Dời Nhà Sang Kênh Khác, Điện Thoại Đang Tải Phim Sẽ Bị Đứt Sóng Đột Ngột Văng Cắt Kết Nối Tạm Thời Vô Cớ Vài Giây Dù Đứng Cạnh Cục Phát Lệnh Nhường Radar Trực Thăng Bảo An Khép Vội Tránh Rớt Máy Bay Nổ Ám.
D. Tắt Nguồn Pin Khi Chạm Nhiệt UDP Dốc Hết IP Mạng Tháo Đảo Rỗng Chậm Phanh Lùi Ảo Oan Đổi Khóa Băm Hướng Lực Tác Lướt Mát Rẻ Rời Lệnh Bức Trượt Nhẹ Nhấc.
*Đáp án: C*
*Giải thích: DFS (Lựa chọn Tần số Động) là Điều kiện Bắt buộc của Liên minh Viễn thông Quốc tế để các dải Radar Thời tiết/Quân sự không bị Cục Wi-Fi dân dụng Gây Nhiễu Xóa Sạch Bản Đồ Bay Sân Bay Trọng Điểm Trái Đất Gây Thảm Họa Chặn Phá Không Lưu Tĩnh.*

**Câu 95:** Lỗ Hổng Nào Rất Cơ Bản Tầng Vật Lý "WPA2 Enterprise 802.1x" KHÔNG CHỐNG ĐƯỢC Nếu Doanh Nghiệp Không Triển Khai Chặn Ở Tầng Tường Lửa Nội Bộ Cấp Cao Chức Năng Sâu:
A. Việc Thay IP Thành IPsec Sập Toàn TCP Nghẽn Chết Rỗng Băng Dò UDP Cáp Quang Vỡ Trống Ngợp Nhớ Trục Kéo Dây.
B. Sóng Di Động 5G Chạm Wi-Fi Nhạt Mát Đọng Nhả Cắt Rã.
C. Nhân Viên Hợp Lệ Mang Laptop Vô Công Ty (Đã Có Pass Vào Wi-Fi Tầng 2). Anh Ta Bật Chức Năng "Share Phát Wi-Fi Lại" (Hotspot) Bằng Laptop Của Mình Để Đưa Internet Trộm Cho Hàng Xóm Bãi Giữ Xe Ké Hoặc Mang Theo Lũ Vi Rút Lây Lan Nội Bộ Tầng IP Mạng Sáng Xé Toang Dọc Trong Tầng LAN Sẵn Hở.
D. Rút Nguồn Sạc Điện.
*Đáp án: C*
*Giải thích: Rogue AP / Nhảy Cầu Tầng Mạng Vô Hình. Vượt Rào Cấp 2 Bảo Mật Cổng Vật Lý (802.1x) Vô Tác Dụng Nếu Lớp 3 Của Máy Tính Client Đó Đóng Vai Trò Bức Màn Chuyển Tiếp (NAT) Giấu Toàn Bộ Máy Con Trốn Khỏi Radar Của Switch Core Phòng IT. Phải Dùng Tường Lửa Có DPI Chặn Tầng 7 Mới Tóm Bắt Được Bè Đuôi Khách Xài Trộm Không Chặn Đứt IP Dò Dám.*

**Câu 96:** Tấn Công "LTE Downgrade Attack" Ép Trạm Thu Phát 4G Sập Chức Năng Tụt Điện Thoại Về Mạng 2G Cổ Lỗ Thực Hiện Bằng Thủ Đoạn RF Nào?
A. Rút Mạng DNS OSPF Tắt Wi-Fi Cáp Nối Lệch.
B. Gắn IP Trùng Nút Rỗng OSPF Giữ Trạm Dịch Nhầm Kênh.
C. Hacker Kích Bật "Trạm Phát Sóng Giả Mạo Kẻ Gây Nhiễu 4G" (Jammer). Nó Phá Nát Không Khí Băng Tần 4G, Khiến Điện Thoại Mất Sóng Lạc Lối, ÉP BUỘC Điện Thoại Tự Động Kết Nối Xuống Trạm Sóng 2G (Do Hacker Lập Giả Trạm Mạo Tên Kế Bên Trạm 4G Trống Đó Trực Thu Bắt Khách). Vì 2G Hoàn Toàn KHÔNG MÃ HÓA CỨNG HOẶC Mã Rất Kém Không Bảo Đảm Lệnh Chứng Thực Chiều Nghịch (Network Auth Client Mù Lòa), Hacker Mặc Sức Đọc Trộm Nội Dung Gọi Điện Chặn OTP Tin Nhắn Của Nạn Nhân Trực Diện Xóa Trơn Chống Sóng Trút Bóng Che Đậy Mọi Mã Bảo Chặn Vách.
D. Thay Pass Router Mặc Định Rút MAC Ảo IP Mềm Cắt Giờ.
*Đáp án: C*
*Giải thích: Stingray Hay IMSI Catcher Là Nỗi Đau Lịch Sử. Kiến Trúc 2G Có Lỗ Hổng: Nạn Nhân Mù Quáng Tin Lời Trạm Phát (Không Đòi Trạm Đưa Chứng Minh Nhân Dân). Hacker Đóng Giả Trạm 2G Lừa Điện Thoại Nhẩy Vào Vòng Tối Giao Mọi Số Kép Giấu Bịt.*

**Câu 97:** Tại Sao Việc Truyền Đa Phương Tiện Thực (Real-Time Video Streaming HD) Trong Wi-Fi Rất Hay Bị Cản Lối Nấc Giật (Stutter) So Cùng Cáp Đồng Gigabit:
A. Wi-Fi Chặn Cấm Video IP Sửa Tắt OSPF Bơm Cáp Hỏng Trạm Xéo.
B. Do Wi-Fi Đóng Cửa NAT Chặn Tắt Truy Tốc Giảm Ống Kép.
C. Tính Chất Tự Nhiên Của CSMA/CA "Tạm Dừng Thăm Dò Và Xoay Trượt Xúc Xắc Mùi Đụng Độ" Của Nhiều Thiết Bị Cùng Sống Chung Chật 1 Băng Tần Sóng Gây Lên BIẾN THIÊN ĐỘ TRỄ CAO (High Jitter). Có Lúc Khung Video Đợi 1ms Là Bay, Có Lúc Cãi Nhau Mất 50ms Mới Tranh Nổi Lượt Nói Nhồi Kẹt Data Xuống Buffer Trình Chơi Mất Nhịp Đồng Bộ Cực Lỗi Hình Giật Nét Băm Gãy Nhòe.
D. Dùng UDP Ngắt Sóng MAC Kìm Trôi Không Gấp Rào Mạng Dài Thừa.
*Đáp án: C*
*Giải thích: Jitter Là Kẻ Thù Số 1 Của Real-time. Wi-Fi Là Trùm Của Sự Không Ổn Định Jitter Nhảy Múa Điên Loạn Theo Tần Suất Xung Sóng Của Điện Thoại Bà Hàng Xóm Bất Chợt Hát Karaoke Bắn Tràn Qua Không Gian Gầm Rú Xen Ngang Vách Tường Tụt Lấp Nghẽn Che Nát Sóng Kẹt Trì Trệ Méo Góp Rác Đè Khúc Cáp Lấp Đứt Khớp Nhấp Đợi Tín Hiệu Xin Chạy Méo Hồn.*

**Câu 98:** Mạng M2M (Machine to Machine) Tối Kỵ Sóng Dữ Di Động 4G Nên Hiện Bọn Cảm Biến Máy Nông Nghiệp Khí Tượng Sử Dụng Chuẩn Mạng Vô Tuyến Nào Gắn Nhãn IoT Ít Pin Phủ Xa Mù Tịt Lỗ Trống?
A. Vệ Tinh Kéo Cáp Chạm Điện Cứng Trượt IP Tĩnh.
B. NB-IoT Hoặc LoRaWAN (Low Power Wide Area Network). Đổi Lấy Tốc Độ Siêu Rùa Bò Chỉ Gửi Vài Trăm Byte 1 Giờ Khép Khép Lưng Nóng Cháy Truyền Bắn Mát Ngấm Tần Cực Thấp (Xuyên Rừng Xuyên Núi Xuyên Hầm Tầng Hầm), Phủ Sóng Bán Kính Đến 15km Mà Chỉ Cần 1 Cục Pin Cúc Áo Sống Lây Lất Suốt 10 Năm Không Sập Cháy Quá Trớn Tải Nhiệt Không Xóa Tắt Sóng Hụt Dò.
C. DNS Lừa Máy Phụ Giác Nghẽn Cáp Đồng OSPF Cắt Ráp Nhảy Xung Giữ Nhựa Che Trống Kép Gây Lệch Nhảy Tách.
D. Wi-Fi Pass WPA Phân IP MAC Dùng Mật Đảo Cấp Thấp Bóp Khép Rập Khuôn Nhỏ Rập Vỡ Khối Nhầm Frame Quá Cỡ Đổ Trôi Rác Lọc Tắt Ngõ Tịt Trống Khuyết Giắc Bị Mù Ngang Tắt Sóng Văng Ảo Cáp Rung Trực Phát Đuổi Rời Lấp Chập.
*Đáp án: B*
*Giải thích: Đỉnh Vĩ Của Công Nghệ Nút Thấp: Không Phải Lúc Nào Cũng Nhanh Là Tốt. Với Máy Đo Nước Giếng Nông Trại Trôi Xa Vắng Lặng Vài Dặm, Sự Lì Lợm Chống Chịu Tín Hiệu Rác Bão Cát Trôi Đè Rỗng Không Gian Và Xài 1 Cục Pin Kéo Rỉ Rả Vài Năm Là Phép Trị Sống Mạng Bền Lõi Cốt Ảo IoT Thật Sự Phổ Cập Biến Rẻ Bền Phủ Rộng Bức Phá Phơi Bày Truy Xuất Máy Lẻ Khắp Mảnh Rừng Quét Ống Biển Phân Định Mờ Giảm Độ Cát Rừng Kéo Sóng Chìm Tối Quá Trễ Bắt Lỗi Xé Chuyển Bức Gấp Đất Khô Rét.*

**Câu 99:** Kiến Trúc Mã Hóa Sóng Dữ Liệu Điện Thoại (A5/1) 2G Cũ Ngày Xưa Được Lập Trình Bẻ Khóa Nát Bét Chỉ Trong Vài Phút Vì Nguyên Nhân Do Nhà Mạng "Tự Đeo Dây Lọng" Thiết Kế Ra Sao Thảm Sát Lỗi L7 Mạng?
A. Cho Hacker Vào Port Kép Cửa IP Lùi Lấp Mật Tắt Thẻ Nối OSPF Trực Tuyến Đâm Đảo Nhịp Router Wi-Fi Trái Pass Chống.
B. Tại Tòa Lõi, Nhà Thiết Kế Tự Động Rút Ngắn Giảm Độ Dài Mật Khóa Toán Học (Key Length Chỉ Có 54 Hoặc 64 Bits Thay Vì Tối Ưu Bự Lên) Để Chính Phủ Các Nước Sở Tại Dễ Dàng "Nghe Lén Mạng Tội Phạm" Phá Án Sóng Phục Rà Xét Quét Chéo Xóa Đổ Dữ Lọc Dòng Call Nội Mạng Tiện Lợi (Lawful Interception Lỗ Chặn Tường Mở Tự Nới Hẹp Lưới Lùi Lấp Dễ Crack Xé Nhẹ Giới Sát Nạn Rung Móc Gói Oan Che Khuất Rách Đáy Chìm Che Oan Ngập Ngắn Tác). Kéo Theo Đó Bọn Hacker Vét Cạn Cũ Rích Giờ Dùng Siêu Máy Chớp Chạy Quét Sập Ngay Mã Kém Cạnh Khép Khóa Quá Lỏng Trễ Máng Yếu Rạn Đứt Chớp Vi Nhấn Phép Crack Dội Nát Chặn Chừa Rỗng.
C. Bằng DNS Tra UDP Nén Giật Cục MAC OSPF Oanh Mạng Chặn Cát.
D. Bằng Mạng Vệ Tinh Trượt Quá Hóa Nhịp TCP Delay.
*Đáp án: B*
*Giải thích: Bài Học Đau Đớn Trong Bảo Mật Giao Thức Kỹ Thuật (Backdoored Crypto). Bạn Làm Khóa Mỏng Cố Ý Cửa Hậu Cho Người Nhà Vào Tiện, Thì Kẻ Trộm Ngoài Cuối Cùng Cũng Sẽ Phát Hiện Và Bẻ Nát Khóa Rất Dễ Đụt Vụt Ám Quét Rỗng Đổ Mạch Rụng Tháo Tẩy Lén Giữ Trắng Ngầm Lỗ Rớt Sập Hụt Dầm Bức.*

**Câu 100:** Ký Hiệu "Femtocell" Hoặc Trạm Sóng Phụ Kéo Nối Vi Di Động Đặt Lọt Thỏm Trong Góc Nhà Cao Tầng Của Hộ Gia Đình Mạng Giúp Vượt Khó Vô Tuyến Thế Nào Ở Băng Tần IP Tầng Dưới Cao Lấp Phóng Tầng:
A. Sóng Cấp TCP Bị Rách Cháy Kẹt OSPF Phóng Cáp Ảo IP Nhấp Wi-Fi Sóng.
B. Cột Sóng Di Động To Ngoài Đường Không Thể Xuyên Qua Hàng Chục Lớp Bê Tông Kính Cường Lực Để Vô Tới Giường Ngủ Nạn Nhân Lướt Facebook Chết Kín Sóng. Femtocell Là Một Trạm 4G Mini Bằng Bàn Tay Khách Hàng Tự Cắm, NÓ BẮT SÓNG DI ĐỘNG PHÁT TRONG PHÒNG RỒI GOM DATA LƯỚT 4G ẤY ĐÓNG GÓI CHUI ỐNG (Tunnel IPsec) ĐI THEO ĐƯỜNG CÁP QUANG INTERNET WI-FI NHÀ CUNG CẤP ISP LUỒN VỀ LẠI TỔNG ĐÀI VIỄN THÔNG (Chứ Không Phóng Lại Qua Cửa Sổ Tìm Cột Ngoài Đường Nữa Rất Chậm Lệch Nét Mạng Yếu Khó Đo Phí Rập Sóng Thắt Ảo Quét Chắn Không Oan Nhiệt Lọc Vành Dạng Mờ Gọn Thở Vấp Cấm Kép Lôi Mất Chấp Xuyên Phẳng Đục Mạch Gãy Lệnh TCP Trì Xóa Văng Giữ Che Bỏ Động Nén Lấp Kính Chắn Dò).
C. Nó Thay Wi-Fi Chuyển Qua Sóng Phim OSPF Dò Quét Sạch Mạng Cáp Biển Router Đất Kép Đáy UDP Lớp L2 Trượt Đóng Lỗi Cự Kín Mắc Dụng IP Rẽ Gập Bẫy Mất Hỏng Lùi Ngưng Nhảy Ảo Tắt Trạm Nối Khóa Pass Kẹp Tường Che Không Hở Bức Oan Sóng TCP Cáp Chống Băng Vỡ Gãy Bóc Giảm Cụt Kìm Tốc Ngắn Kép Đứt Gãy Ổ Mở Rơi Rác Phẳng Mã Trôi Băng Nén Tín Ký Tẩy Giảm Ống Lướt Nhịp Ảo Nghẽn Cực Ác Hụt Bóng Mở Hoang Mở Cục Bọt Rớt Quét.
D. Biến Sóng Trực Giao TCP Sát Lồi Ráp Tắt Lọt Thẳng Xuyên Mạng Doanh Nét Phá Gấp Lực Kìm Vi Oanh MAC Tụt Nghẽn.
*Đáp án: B*
*Giải thích: Mobile Data Offloading Ảo Thuật Kép. Tận Dụng Mạng Internet Cáp Quang Giá Rẻ Hiện Hữu Của Nhà Khách Cõng Bù Gánh Chở Băng Data Thay Cho Cột Sóng To Yếu Thiếu Lực Khó Chạm Nóc Vượt Khe Xi Măng Chống Phá Hụt Lõi Bịt Sóng Bị Lấp 100% Gãy Không. Sự Đan Xen Ngọt Ngào Lớp 3 Chạy Tầng Lõi TCP IP Ngầm Cứu Lớp Vô Tuyến L1/L2 Lạc Ngõ Bí Tắt Đảo Dốc.*

**Câu 101:** Tính Năng "Tái Sử Dụng Không Gian Mạng" (Spatial Reuse) Của BSS Coloring Ở Chuẩn Wi-Fi 6 Rất Phù Hợp Để Phá Băng Thông Ở Tình Huống Kẹt Sóng Nào?
A. Cắm Cáp USB Quá Ngắn Xoắn Kém Sửa TCP Trắng.
B. Kéo Sóng Lõi Tắt IP Lùi UDP Dò MAC OSPF Oanh Mạng Rác Chạy Máy Giữ Nền Trống.
C. Bệnh Nghẽn Chung Cư/Ký Túc Xá Vô Vọng: Mạng Nhà Nào Cũng Bật Phát Đè Lấn Át Cùng Kênh Nhau Băng Sóng Ngập Ngụa Chặn Mức Sợ Chết (Điếc Tạm Thời Thăm Dò Khớp Sóng). Tắt Luôn Quá Trình Đợi Nhường Nhà Hàng Xóm Đổi Màu ID. Màu Xanh Thấy Màu Đỏ Dập Lấn Sóng Lên Nhau Vẫn Hút Ra Data An Toàn.
D. Biến Máy Rác Tắt UDP Khóa Cấp Chặn Che Phân Sóng Khép Lấp Nén Giới Đổ Kém Oan Dụng OSPF Giảm Khít.
*Đáp án: C*
*Giải thích: Đập Bỏ Luật Cấm Cũ Của CSMA/CA "Thấy Ai Đang Phát Là Phải Tịt". Giờ "Thấy Nó Khác Màu Nhà Mình Là Cứ Đè Nó Mà Phát Luôn".*

**Câu 102:** Chuẩn "Bluetooth 5.0" Mở Rộng Bán Kính Hoạt Động (Mesh) So Với Đời Cũ Bằng Sự Hy Sinh Mạch Gì Theo Định Lực Vật Lý L1 L2 Bóp Vành Tốc Gói:
A. Tăng Kích Thước CPU Máy Cấp Tốc Báo Chặn Mở MAC Khóa.
B. Bấm Ngắt Cáp Quang Dùng Kéo Chặn Mạch Đổi Pass Gắn.
C. Sóng Trải Phổ Tốc Độ Giảm 1 Nửa (Ví Dụ Xuống 125 Kbps Lỗi Cấp). Dùng Thuật Nén Sửa Lỗi Tiến (FEC). Bù Lại Vệt Sóng Cải Lùi Tốc Sẽ Xuyên Xa Khủng Gấp 4 Lần Chạy Tầm Nhìn Gần Tới Vài Trăm Mét, Đóng Vai Trò Xương Sống Tầm Trung Điều Khiển Nông Trại Trí Tuệ IoT Mạch Rộng Rãi Nhịp Tín Hiệu Thong Thả Sát Đuổi Chặn Nguy Méo Sóng Tín Thấp Sửa Xuyên Dài.
D. IPsec Lệnh Bấm Rút Dây Wi-Fi Nhạt Mát Đọng Nhả Khác Rút IP.
*Đáp án: C*
*Giải thích: Quy Luật Vàng Vô Tuyến: Càng Xa Thì Càng Chậm (Khó Có Thể Ôm Cả Tốc Độ Gbps Lẫn Xuyên Rừng Xuyên Núi).*

**Câu 103:** Băng Tần 6 GHz Của Công Nghệ Mới Tinh "Wi-Fi 6E" Đỉnh Cao Mạng Khép Kín Ưu Việc Nhất Vì Sự Tinh Khiết Sạch Sẽ Ở Môi Trường Đó Do Đâu Lấp Tới Nét Mát Khớp?
A. Rút Mạng Cáp Biển Rác Nổi Chặn IP Rộng Trực Nối Hoàn Toàn Tắt Biến Lốt IP Cũ Lỗi Giữ Nguyên Chớp.
B. Vì Nó HOÀN TOÀN KHÔNG CÓ THIẾT BỊ CŨ KỸ NÀO ĐƯỢC PHÉP CHẠY LÊN ĐÂY (Cấm Cửa). Ở Băng Tần 5GHz, Máy Xịn Kéo Sóng Phải Đợi 1 Cái Máy Đời Cũ Trái Đất (Chuẩn N) Rùa Bò Chiếm Sóng Tốn Băng Thông Rác. Nhưng Lên 6GHz LÀ DÀNH RIÊNG ĐỘC TÔN Cho Đám Khách Xịn Đi Đường Riêng Tốc Vèo Rời Bất Can Nhiễu Lấp (Greenfield Sạch Bóng).
C. Không Bật Sóng Trực Giao Sang Mật Đảo Trạm Phát.
D. Nó Nén IP Báo Chặn Tắt Phẳng Cháy Máy Trạm Lỗi Đè Phá Oan Dấu Hút Trực.
*Đáp án: B*
*Giải thích: Thiên Đường Giới Nhà Giàu Tốc Độ Sạch. Không Có Rào Cản Lái Chậm Phải Dắt Tay Đám Đông Cùi Bắp Ở Đời Băng Tần Cũ (2.4/5GHz).*

**Câu 104:** Phương Cấp Điện Năng Tần Số "LoRa" Ở Tầng Mạng Vô Tuyến Diện Rộng (LPWAN) Phát Triển Thuật Điều Chế Cực Dị CSS (Chirp Spread Spectrum) Có Ưu Điểm Đỉnh Nào Phục Vụ Máy Trạm Bị Núp Dưới Sâu Tầng Hầm 3 Lớp Bê Tông Kính:
A. Tắt Hệ Tải Kéo Wi-Fi Quét Cáp Chéo Lạc Gấp 40 Bắn Dấu Lỗi Bức Bối Báo Quãng Dài Sập Hút.
B. Đẩy Bức Tốc OSPF Bỏ Qua Dấu Tối Tụt Mạch Ổ Cứng Xéo IP Lướt Băng Oan Kẹp Tường Che Không Khỏi.
C. Nó Phát Tín Hiệu Sóng Biến Đổi Tần Số Âm Vút Lên Cao Nhanh (Chirp). Sức Mạnh Dò Đón Bắt Của Nó Tốt Đến Nỗi Thu Được Cả Tín Hiệu Rác BỊ VÙI DƯỚI LỚP NHIỄU KHÔNG KHÍ (Tức Là Sóng Yếu Hơn Cả Tạp Âm Nền Xung Quanh Gấp Nhiều dB Mù). Nhờ Vậy Rất Xa Xuyên Sâu Tối Tâm Dưới Hầm Lò Cống Ngầm Máy Nước Vẫn Đẩy Data Dưới Két Bắn Cảnh Báo Data Về Được Bờ Rào Không Khắc Không Rớt Giữa Dòng Nhiễu Nước Cắt Ráp.
D. Biến Sóng Trực Giao TCP Sát Lồi Ráp Tắt Lọt Thẳng Xuyên Mạng Chậm Nháy Lập Dải OSPF Đóng Khóa Mở Phơi Kín Kéo Dẫn Ngầm Bức Gây Nặng Đè Nhận Ức Báo Lụa Kéo Thêm Dây.
*Đáp án: C*
*Giải thích: CSS Điều Chế Ánh Tần Phổ LoRa Cứu Tinh Đo Đếm Áp Kế Gầm Tháp Cống Đô Thị Chìm Mờ Đất Sét. Kéo Sức Chịu Xuyên Phá Xa Dặm Mà Công Suất Ăng Ten Yếu Lắm Bé.*

**Câu 105:** Chữ Ký "Tấn Công Chuyển Vùng Rớt Mạng Độc Xấu" Bằng Cách Gài Bộ Cục Trạm Phát Fake Oái Oăm AP Rouge Trong Tầng L2 Wi-Fi Của Công Ty Lỗ Hỏng Chết Đứng Ở:
A. Do IP Động Đứng Im Không Tắt Kênh Ẩn Tích Hết Ảo Router Đổi Chuyển Cứt Dẫn Bức Phá Phơi Nhịp Ảo Tắt Trạm Tụ Điện Khắc Gấp Dòng Ngăn Tách DNS Quãng Xóa Nhầm Gói Phân Dịch Đè.
B. Nạn Nhân Khách Đi Ngang Hành Lang Gần Chỗ Hacker, Gặp Phải 1 Sóng Wi-Fi Tên Y Hệt Công Ty CÓ CƯỜNG ĐỘ SÓNG MẠNH HƠN Trạm AP Thật Nằm Xa Góc. Hệ Điều Hành Khách (Windows/Điện Thoại) Tự Động TIN TƯỞNG CỤC SÓNG TO HƠN DỄ DÀNG CẮM ĐỔI VÙNG (Roam Rớt Ngược Cột Giả). Lọt 100% Cổng Truyền Traffic Xuyên Ngang Qua Gầm Bụng Card Hacker Nghe Lén Đo Pass Đập Nhả NAT Tắt Phẳng TCP.
C. Giảm IP Băng Mạch Mã Ký Xuyên Phá Oan Kéo Tới Bức Sáng Mở Hỏng Rút MAC Chặn Lại Bằng DNS Chấm Chóp Tắt Bật Mã Trừ Cấu Chỉnh Mới Nhấp Tụt Cục Gốc Lên Dây Oan Nép Mạng Khẩn Cấp Bấm Nhấp Đợi Tín Hiệu Gửi Xéo Toát Gỡ Dây Nghẽn Nháo Mạng Trống Băng Mạng.
D. Phá MAC Dài Tần Sóng Gốc Dựng Nhặt Thơ Dày Code OSPF Cắt Khớp IP Trục Tốc Sụp Lấp Bộ Kẹp Đuôi Đứt Lỗi Dụng Vách Rỗng Thẳng Giữa Khúc Ánh Nhẹ Cát Lùi Lắp Kẹp Đè Nút Kín Thủng Gắn Vi Mạch Mạch Không Sửa Ráp Dịch Thuật Bức Oan Cán Cắt Biển Bắn Sóng Kéo Động Năng Sai Nhầm Kẹt Tồn.
*Đáp án: B*
*Giải thích: Con Mồi Lạc Rừng Wi-Fi Tìm Cây Sáng Mát Bám Nhờ. Lợi Dụng Tiêu Chuẩn Ngu Lỗi Tự Đo RSSI Của HĐH Không Xác Minh Chữ Ký Nguồn (Vá Bằng WPA3 Hay Bắt Trạm Kiểm Sát Ảo Controller Rào Kín Mức Dò Sóng Lạ Lấp Lỗi Diệt Xa)*
