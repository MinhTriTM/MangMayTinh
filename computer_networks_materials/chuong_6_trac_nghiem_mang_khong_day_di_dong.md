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

**Câu 106:** Để giải quyết vấn đề trạm ẩn (hidden terminal) trong mạng không dây IEEE 802.11, người ta có thể sử dụng cơ chế nào sau đây?
A. Gửi gói tin RTS (Request to Send) và CTS (Clear to Send)
B. Tăng công suất phát của tất cả các trạm
C. Sử dụng CSMA/CD thay vì CSMA/CA
D. Giảm kích thước gói tin dữ liệu xuống mức tối thiểu
*Đáp án: A*
*Giải thích: Cơ chế RTS/CTS được thiết kế đặc biệt để giải quyết bài toán trạm ẩn. Trạm gửi sẽ phát RTS, Access Point (AP) trả lời bằng CTS, thông báo cho tất cả các trạm trong vùng phủ sóng của AP biết kênh truyền đã được đặt trước, giúp các trạm ẩn tránh gửi dữ liệu và gây đụng độ.*

**Câu 107:** Trong mạng 802.11, thời gian chờ nào là ngắn nhất để ưu tiên việc truyền các khung tin điều khiển (ví dụ: ACK, CTS)?
A. DIFS (Distributed Inter-Frame Space)
B. SIFS (Short Inter-Frame Space)
C. PIFS (PCF Inter-Frame Space)
D. EIFS (Extended Inter-Frame Space)
*Đáp án: B*
*Giải thích: SIFS là khoảng thời gian ngắn nhất giữa các khung tin, được sử dụng cho các khung tin phản hồi có mức độ ưu tiên cao như ACK, CTS, hoặc các khung dữ liệu trong một chuỗi truyền, nhằm tránh bị các trạm khác tranh chấp kênh truyền.*

**Câu 108:** Kỹ thuật trải phổ (Spread Spectrum) nào được sử dụng trong chuẩn 802.11b để mở rộng băng thông tín hiệu và chống nhiễu?
A. OFDM (Orthogonal Frequency-Division Multiplexing)
B. DSSS (Direct-Sequence Spread Spectrum)
C. FHSS (Frequency-Hopping Spread Spectrum)
D. MIMO (Multiple-Input Multiple-Output)
*Đáp án: B*
*Giải thích: 802.11b sử dụng kỹ thuật trải phổ chuỗi trực tiếp (DSSS - Direct-Sequence Spread Spectrum), mã hóa mỗi bit dữ liệu bằng một chuỗi chip (ví dụ: mã Barker) để tăng khả năng chống nhiễu.*

**Câu 109:** Tốc độ truyền dữ liệu tối đa lý thuyết của chuẩn IEEE 802.11g là bao nhiêu?
A. 11 Mbps
B. 54 Mbps
C. 150 Mbps
D. 600 Mbps
*Đáp án: B*
*Giải thích: Chuẩn 802.11g (và 802.11a) sử dụng kỹ thuật điều chế OFDM, hỗ trợ tốc độ truyền dữ liệu tối đa trên lý thuyết là 54 Mbps.*

**Câu 110:** Giao thức nào cung cấp cơ chế bảo mật cải tiến trong chuẩn WPA2 so với WEP và WPA ban đầu?
A. TKIP (Temporal Key Integrity Protocol)
B. CCMP (Counter Mode CBC-MAC Protocol) sử dụng thuật toán AES
C. RC4 (Rivest Cipher 4)
D. EAP (Extensible Authentication Protocol)
*Đáp án: B*
*Giải thích: WPA2 bắt buộc sử dụng CCMP, một giao thức mã hóa dựa trên thuật toán AES mạnh mẽ, cung cấp mức độ bảo mật cao hơn nhiều so với TKIP (dùng trong WPA) và RC4 (dùng trong WEP).*

**Câu 111:** Trong mạng di động tế bào, khi một thiết bị di động (Mobile Station) di chuyển từ một ô (cell) này sang một ô khác trong khi đang thực hiện cuộc gọi, quá trình chuyển giao kết nối được gọi là gì?
A. Roaming
B. Hand-off (hoặc Handover)
C. Paging
D. Multiplexing
*Đáp án: B*
*Giải thích: Hand-off (chuyển giao) là cơ chế chuyển đổi kênh tần số, trạm gốc (Base Station) hoặc luồng dữ liệu cho một kết nối di động đang diễn ra khi người dùng di chuyển giữa các vùng phủ sóng của các cell.*

**Câu 112:** Kiến trúc Mobile IP sử dụng khái niệm nào để đại diện cho địa chỉ IP thường trú cố định của một thiết bị di động?
A. Care-of Address (CoA)
B. Home Address
C. Foreign Address
D. Gateway Address
*Đáp án: B*
*Giải thích: Trong Mobile IP, Home Address là địa chỉ IP cố định được cấp cho thiết bị di động (Mobile Node), không thay đổi bất kể thiết bị di chuyển đến mạng nào. Các gói tin luôn được gửi đến địa chỉ này.*

**Câu 113:** Trong Mobile IP, địa chỉ nào được sử dụng để định tuyến gói tin đến vị trí hiện tại của thiết bị di động khi nó đang ở một mạng khách (foreign network)?
A. Home Address
B. Care-of Address (CoA)
C. MAC Address
D. Loopback Address
*Đáp án: B*
*Giải thích: Khi thiết bị di chuyển sang một mạng khác (foreign network), nó nhận được một Care-of Address (CoA). Home Agent sẽ đóng gói (tunnel) các gói tin gửi đến Home Address và chuyển tiếp chúng đến CoA hiện tại.*

**Câu 114:** Khái niệm "Tam giác định tuyến" (Triangle Routing) trong Mobile IP mô tả vấn đề gì?
A. Gói tin từ thiết bị gửi (Correspondent Node) đi thẳng đến thiết bị nhận (Mobile Node)
B. Gói tin từ mạng gửi đi qua 3 router khác nhau trước khi đến đích
C. Gói tin từ Correspondent Node phải đi qua Home Agent trước khi đến Mobile Node ở mạng khách, tạo thành đường đi vòng
D. Gói tin bị lặp vô hạn giữa 3 trạm phát sóng
*Đáp án: C*
*Giải thích: Định tuyến tam giác là tình trạng gói tin từ máy gửi (CN) không đi trực tiếp đến máy nhận di động (MN) đang ở mạng khách, mà phải đi đường vòng đến Home Agent rồi mới được tunnel đến MN.*

**Câu 115:** Công nghệ 4G LTE (Long-Term Evolution) chủ yếu sử dụng kiến trúc chuyển mạch nào để truyền tải dữ liệu, bao gồm cả cuộc gọi thoại (VoLTE)?
A. Chuyển mạch kênh (Circuit Switching) toàn bộ
B. Chuyển mạch gói (Packet Switching) toàn bộ (All-IP Network)
C. Kết hợp cả chuyển mạch kênh và chuyển mạch gói
D. Chuyển mạch bản tin (Message Switching)
*Đáp án: B*
*Giải thích: Kiến trúc cốt lõi của LTE là EPC (Evolved Packet Core), là một mạng "All-IP" chỉ sử dụng chuyển mạch gói cho mọi loại dịch vụ, kể cả thoại (Voice over LTE - VoLTE).*

**Câu 116:** Trong mạng 802.11, Access Point (AP) định kỳ phát đi một loại khung quản lý (Management Frame) để quảng bá sự hiện diện của mạng (SSID) và các thông số đồng bộ. Khung đó gọi là gì?
A. Probe Request
B. Association Request
C. Beacon Frame
D. Authentication Frame
*Đáp án: C*
*Giải thích: Beacon frame được AP phát định kỳ (thường là mỗi 100ms) chứa thông tin về SSID, tốc độ hỗ trợ, phương thức bảo mật, giúp các thiết bị (client) phát hiện và quét (passive scanning) mạng.*

**Câu 117:** Khi một thiết bị Wi-Fi chủ động tìm kiếm các Access Point xung quanh bằng cách gửi gói tin yêu cầu trên nhiều kênh tần số, thiết bị đang thực hiện quá trình gì?
A. Passive Scanning (Quét thụ động)
B. Active Scanning (Quét chủ động)
C. Roaming (Chuyển vùng)
D. Beaconing (Phát báo hiệu)
*Đáp án: B*
*Giải thích: Active scanning là khi trạm khách (client) gửi các gói tin Probe Request trên từng kênh, và các AP sẽ phản hồi lại bằng gói Probe Response.*

**Câu 118:** Công nghệ ăng-ten MIMO (Multiple-Input Multiple-Output) trong chuẩn 802.11n và 802.11ac giúp tăng tốc độ truyền tải chủ yếu bằng cách nào?
A. Giảm nhiễu băng tần hẹp
B. Gửi cùng một tín hiệu lặp lại nhiều lần
C. Truyền nhiều luồng dữ liệu song song (Spatial Multiplexing) qua nhiều ăng-ten
D. Tăng công suất phát tín hiệu RF
*Đáp án: C*
*Giải thích: MIMO tận dụng hiện tượng đa đường (multipath) truyền độc lập nhiều luồng dữ liệu (spatial streams) qua các cặp ăng-ten phát-nhận khác nhau, nhân lên băng thông tổng thể.*

**Câu 119:** Dải tần số nào ít bị nhiễu bởi các thiết bị gia dụng (như lò vi sóng, điện thoại không dây) hơn, và cung cấp nhiều kênh không chồng chéo hơn trong mạng Wi-Fi?
A. 900 MHz
B. 2.4 GHz
C. 5 GHz
D. 60 GHz
*Đáp án: C*
*Giải thích: Dải tần 5 GHz rộng hơn, có nhiều kênh không bị chồng lấn (non-overlapping channels) và ít bị nhiễu bởi các thiết bị tiêu chuẩn sử dụng chung băng tần công nghiệp (ISM) ở mức 2.4 GHz.*

**Câu 120:** Chuẩn 802.11 nào hỗ trợ tốc độ cao nhất (Gigabit Wi-Fi) và hoạt động độc quyền trên băng tần 5GHz?
A. 802.11a
B. 802.11n
C. 802.11g
D. 802.11ac
*Đáp án: D*
*Giải thích: 802.11ac (Wi-Fi 5) hỗ trợ tốc độ lên đến hàng Gigabit, sử dụng các kênh rộng (lên đến 160MHz) và hoạt động hoàn toàn trên băng tần 5GHz.*

**Câu 121:** Trong mạng di động GSM (2G), kỹ thuật đa truy nhập nào được sử dụng để chia một kênh tần số vô tuyến thành các khe thời gian (time slots) cho nhiều người dùng?
A. CDMA (Code Division Multiple Access)
B. TDMA (Time Division Multiple Access) kết hợp với FDMA
C. OFDM (Orthogonal Frequency-Division Multiplexing)
D. CSMA/CA
*Đáp án: B*
*Giải thích: GSM sử dụng sự kết hợp của FDMA (chia dải tần số) và TDMA (chia kênh thành các khe thời gian) để phục vụ nhiều người dùng đồng thời.*

**Câu 122:** Kỹ thuật đa truy nhập nào, được sử dụng trong mạng 3G (UMTS/WCDMA), gán cho mỗi người dùng một mã giả ngẫu nhiên duy nhất để mã hóa tín hiệu, cho phép nhiều người dùng truyền đồng thời trên cùng một dải tần số rộng?
A. TDMA
B. FDMA
C. CDMA
D. SDMA
*Đáp án: C*
*Giải thích: CDMA (Code Division Multiple Access) cho phép mọi cell và mọi người dùng hoạt động trên cùng một dải tần số (phổ rộng), phân tách các luồng dữ liệu bằng mã toán học.*

**Câu 123:** Thuật ngữ "Near-Far Problem" (Vấn đề Gần-Xa) đặc biệt quan trọng và cần phải kiểm soát công suất chặt chẽ trong hệ thống mạng di động nào?
A. TDMA (2G GSM)
B. FDMA (1G AMPS)
C. CDMA (3G WCDMA)
D. Wi-Fi (802.11)
*Đáp án: C*
*Giải thích: Trong CDMA, nếu một máy gần trạm gốc phát cùng công suất với máy ở xa, tín hiệu từ máy gần sẽ làm chìm tín hiệu của máy ở xa (nhiễu đa người dùng). Do đó, CDMA yêu cầu cơ chế kiểm soát công suất (Power Control) cực kỳ nhanh và chính xác.*

**Câu 124:** Trong kiến trúc LTE (4G), thiết bị nào đóng vai trò là điểm kết nối trực tiếp (trạm gốc) với các thiết bị di động (User Equipment - UE) qua giao diện vô tuyến?
A. BSC (Base Station Controller)
B. eNodeB (evolved Node B)
C. MSC (Mobile Switching Center)
D. MME (Mobility Management Entity)
*Đáp án: B*
*Giải thích: Trong cấu trúc E-UTRAN của mạng LTE, eNodeB (hoặc eNB) là trạm gốc chịu trách nhiệm xử lý toàn bộ giao thức sóng vô tuyến và quản lý tài nguyên vô tuyến.*

**Câu 125:** Nút mạng nào trong kiến trúc lõi EPC (Evolved Packet Core) của LTE chịu trách nhiệm xác thực người dùng và quản lý tính di động (Mobility Management)?
A. SGW (Serving Gateway)
B. PGW (Packet Data Network Gateway)
C. MME (Mobility Management Entity)
D. HSS (Home Subscriber Server)
*Đáp án: C*
*Giải thích: MME là thành phần điều khiển (control-plane) chính, xử lý tín hiệu giữa UE và mạng lõi, chịu trách nhiệm xác thực (cùng với HSS), thiết lập kết nối mang (bearer) và theo dõi vị trí của UE.*

**Câu 126:** Kỹ thuật điều chế nào được ứng dụng mạnh mẽ trong đường xuống (downlink) của mạng 4G LTE và chuẩn Wi-Fi 802.11n/ac để chịu đựng tốt nhiễu đa đường và suy hao chọn lọc tần số?
A. QPSK
B. DSSS
C. OFDM (Orthogonal Frequency Division Multiplexing)
D. CDMA
*Đáp án: C*
*Giải thích: OFDM chia dòng dữ liệu tốc độ cao thành nhiều luồng tốc độ thấp (các sóng mang phụ trực giao), giúp tín hiệu bền vững hơn trước sự biến dạng kênh truyền và nhiễu.*

**Câu 127:** Trong cơ chế truy cập CSMA/CA của Wi-Fi, nếu kênh truyền đang bận, trạm phát sẽ làm gì sau khi chờ hết thời gian DIFS?
A. Phát ngay lập tức
B. Trở lại trạng thái nghỉ và không truyền
C. Bắt đầu đếm ngược thời gian Backoff ngẫu nhiên
D. Gửi gói tin Jam Signal
*Đáp án: C*
*Giải thích: Theo CSMA/CA, nếu kênh bận, trạm sẽ hoãn việc truyền, chờ DIFS khi kênh rảnh, sau đó chọn một giá trị lùi thời gian (random backoff) trong một "cửa sổ tranh chấp" (Contention Window) trước khi thử phát.*

**Câu 128:** Vấn đề "Exposed Terminal" (Trạm phơi bày) trong mạng không dây dẫn đến hệ quả gì?
A. Làm tăng tỷ lệ đụng độ (collision) gói tin
B. Gây lãng phí băng thông do một trạm nhầm tưởng kênh truyền bị bận nên không dám phát dữ liệu
C. Làm giảm tầm phủ sóng của Access Point
D. Buộc các thiết bị phải ngắt kết nối
*Đáp án: B*
*Giải thích: Trạm phơi bày (Exposed terminal) là hiện tượng một trạm (A) nghe thấy trạm khác (B) đang phát (cho trạm C không liên quan), A tưởng kênh bận nên hoãn việc phát dữ liệu cho trạm D, dù thực tế việc A phát cho D sẽ không gây nhiễu cho việc B phát cho C. Điều này làm giảm hiệu suất mạng.*

**Câu 129:** Trong giao thức Mobile IP, khi Mobile Node ở xa mạng nhà, thông báo đăng ký (Registration Request) được gửi từ Foreign Agent đến thành phần nào?
A. MME (Mobility Management Entity)
B. Correspondent Node
C. Home Agent
D. DNS Server
*Đáp án: C*
*Giải thích: Foreign Agent (hoặc trực tiếp Mobile Node nếu sử dụng Co-located CoA) gửi thông báo đăng ký tới Home Agent để cập nhật vị trí Care-of Address (CoA) hiện tại.*

**Câu 130:** Trong cấu trúc liên kết Wi-Fi (Architecture), tập hợp các thiết bị khách (Station) kết nối với một Access Point duy nhất tạo thành một mạng con cơ bản gọi là gì?
A. BSS (Basic Service Set)
B. ESS (Extended Service Set)
C. IBSS (Independent Basic Service Set)
D. DS (Distribution System)
*Đáp án: A*
*Giải thích: BSS (Basic Service Set) là khối xây dựng cơ bản của mạng 802.11 (Infrastructure mode), bao gồm một AP trung tâm và các trạm (STA) liên kết với nó.*

**Câu 131:** Khi nhiều BSS (các mạng con với các AP) được kết nối với nhau thông qua một mạng phân phối (Distribution System) (ví dụ: mạng LAN có dây) để tạo ra một vùng phủ sóng rộng lớn hơn, cấu trúc này gọi là gì?
A. Ad-hoc Network
B. ESS (Extended Service Set)
C. WPAN
D. VLAN
*Đáp án: B*
*Giải thích: ESS (Extended Service Set) bao gồm nhiều BSS được liên kết qua một Hệ thống phân phối (DS), cho phép người dùng chuyển vùng (roam) từ AP này sang AP khác trong cùng một mạng ảo (thường dùng chung một SSID).*

**Câu 132:** Chế độ mạng Wi-Fi nào cho phép các thiết bị (Stations) giao tiếp trực tiếp với nhau (peer-to-peer) mà không cần thông qua Access Point trung tâm?
A. Infrastructure Mode
B. Ad-hoc Mode (IBSS)
C. ESS Mode
D. Bridging Mode
*Đáp án: B*
*Giải thích: Chế độ Ad-hoc (Independent BSS - IBSS) cho phép các thiết bị không dây tạo thành một mạng tạm thời và gửi gói tin trực tiếp cho nhau không cần hạ tầng AP.*

**Câu 133:** Tầng giao thức nào trong mô hình OSI xử lý trực tiếp các thuật toán CSMA/CA và cấu trúc khung tin (MAC frame) trong chuẩn IEEE 802.11?
A. Tầng vật lý (Physical Layer)
B. Tầng liên kết dữ liệu (Data Link Layer - MAC sublayer)
C. Tầng mạng (Network Layer)
D. Tầng giao vận (Transport Layer)
*Đáp án: B*
*Giải thích: Cơ chế CSMA/CA và việc đóng gói/kiểm soát truy cập môi trường (MAC - Medium Access Control) thuộc phân tầng MAC của tầng liên kết dữ liệu (Layer 2).*

**Câu 134:** Khung dữ liệu MAC của chuẩn 802.11 có một đặc điểm độc đáo là nó thường chứa tối đa bao nhiêu trường địa chỉ MAC (Address fields)?
A. 2 trường (Source, Destination)
B. 3 trường (Source, Destination, Router)
C. 4 trường (RA, TA, DA, SA - Receiver, Transmitter, Destination, Source)
D. 6 trường
*Đáp án: C*
*Giải thích: Khung MAC 802.11 có thể chứa đến 4 địa chỉ MAC (Address 1 đến Address 4) để chỉ định rõ nguồn gốc, đích đến cuối cùng, thiết bị phát vô tuyến trực tiếp (ví dụ AP) và thiết bị nhận vô tuyến trực tiếp (ví dụ Client), đặc biệt quan trọng khi truyền qua DS (Distribution System).*

**Câu 135:** Thành phần nào trong một khung MAC 802.11 chỉ định khoảng thời gian mà kênh truyền được "đặt chỗ" (reserve) cho việc trao đổi các khung tin tiếp theo (như ACK)?
A. Trường Sequence Control
B. Trường Duration/ID
C. Trường Frame Control
D. Trường Frame Check Sequence (FCS)
*Đáp án: B*
*Giải thích: Trường Duration/ID được sử dụng để cập nhật Vector cấp phát mạng (Network Allocation Vector - NAV) tại các trạm khác, cho biết kênh sẽ bị chiếm dụng trong bao lâu.*

**Câu 136:** Tính năng nào của Mobile IP cho phép bỏ qua (bypass) Home Agent bằng cách thiết lập đường hầm (tunnel) trực tiếp từ Correspondent Node (CN) đến thiết bị di động (MN)?
A. Route Optimization (Tối ưu hóa định tuyến)
B. Reverse Tunneling
C. Foreign Agent Paging
D. Triangular Routing
*Đáp án: A*
*Giải thích: Tối ưu hóa định tuyến (Route Optimization) là quá trình trong đó CN học được Care-of Address (CoA) của MN, từ đó gửi gói tin trực tiếp đến MN, khắc phục vấn đề định tuyến tam giác.*

**Câu 137:** 5G NR (New Radio) mang lại cải tiến lớn nhất ở đặc điểm nào so với 4G LTE cho các ứng dụng thực tế ảo (VR) hoặc điều khiển tự động hóa công nghiệp?
A. Băng thông thoại (Voice quality) tốt hơn
B. Độ trễ (Latency) siêu thấp (Ultra-Reliable Low Latency Communications - URLLC)
C. Hỗ trợ nhiều địa chỉ IPv6 hơn
D. Thay thế hoàn toàn cáp quang dưới biển
*Đáp án: B*
*Giải thích: 5G NR hỗ trợ tính năng URLLC, giảm độ trễ trên không (air-interface latency) xuống mức dưới 1ms, cần thiết cho các ứng dụng thời gian thực khắt khe.*

**Câu 138:** Kỹ thuật nào trong mạng di động 5G cho phép chia sẻ hạ tầng vật lý mạng lõi thành nhiều mạng logic riêng biệt, mỗi mạng tối ưu cho một loại dịch vụ (ví dụ: IoT, băng thông rộng, độ trễ thấp)?
A. Network Slicing (Cắt lớp mạng)
B. Beamforming
C. Massive MIMO
D. Carrier Aggregation
*Đáp án: A*
*Giải thích: Network Slicing là khái niệm mạng ảo hóa, cho phép tạo ra nhiều lát cắt (slice) logic từ một mạng vật lý duy nhất, cung cấp các đặc tả SLA (Service Level Agreement) khác nhau.*

**Câu 139:** Kỹ thuật truyền dẫn tín hiệu không dây nào sử dụng mảng ăng-ten để định hướng năng lượng sóng radio (tập trung chùm tia) trực tiếp đến thiết bị người dùng cụ thể, thay vì phát đẳng hướng (tỏa tròn)?
A. CSMA/CD
B. Spread Spectrum
C. Beamforming
D. Multiplexing
*Đáp án: C*
*Giải thích: Beamforming điều chỉnh pha và biên độ của tín hiệu trên nhiều ăng-ten để tạo ra giao thoa tăng cường tại vị trí thiết bị nhận, tăng cường cường độ tín hiệu và giảm nhiễu.*

**Câu 140:** Mã hóa WEP (Wired Equivalent Privacy) dễ bị bẻ khóa (crack) chủ yếu do nguyên nhân nào?
A. Sử dụng thuật toán AES quá chậm
B. Khóa bí mật (Pre-Shared Key) được truyền dưới dạng bản rõ (plaintext)
C. Vector khởi tạo (Initialization Vector - IV) quá ngắn (24-bit) và bị tái sử dụng (IV reuse)
D. Không hỗ trợ xác thực MAC
*Đáp án: C*
*Giải thích: WEP dùng luồng mã hóa RC4 với IV chỉ có 24-bit. Do IV ngắn, nó nhanh chóng bị lặp lại. Kẻ tấn công có thể thu thập đủ số lượng gói tin IV trùng lặp để phân tích và tìm ra khóa bí mật gốc.*

**Câu 141:** Trong chuẩn 802.11, việc phân mảnh (Fragmentation) các gói tin dữ liệu lớn thành nhiều khung nhỏ hơn có mục đích gì?
A. Tăng băng thông tối đa của mạng
B. Tiết kiệm năng lượng cho thiết bị phát
C. Giảm xác suất phải truyền lại toàn bộ gói dữ liệu lớn nếu có lỗi do kênh vô tuyến kém (tăng độ tin cậy)
D. Cho phép nén dữ liệu tốt hơn
*Đáp án: C*
*Giải thích: Trong môi trường vô tuyến nhiều lỗi (BER cao), khung càng lớn càng dễ bị hỏng do nhiễu. Phân mảnh giúp nếu một mảnh nhỏ bị lỗi, chỉ cần truyền lại mảnh đó thay vì toàn bộ khung lớn.*

**Câu 142:** Tính di động mạng (Network Mobility) khác với tính di động máy tính (Host Mobility) ở điểm nào?
A. Network Mobility dùng IPv4, Host Mobility dùng IPv6
B. Network Mobility liên quan đến việc di chuyển của toàn bộ một mạng con (sub-network, ví dụ router trên xe lửa) kết nối với mạng lõi, thay vì chỉ một thiết bị đơn lẻ.
C. Network Mobility là tên gọi khác của việc Hand-off giữa các cell
D. Host Mobility sử dụng chuyển mạch kênh
*Đáp án: B*
*Giải thích: Network Mobility (NEMO) quản lý sự di chuyển của một nhóm các thiết bị đằng sau một Mobile Router, giúp che giấu sự thay đổi mạng đối với các thiết bị bên trong mạng con đó.*

**Câu 143:** Cấu hình "Hard Hand-off" trong mạng di động (như LTE) có nghĩa là gì?
A. Thiết bị duy trì kết nối với cả trạm gốc cũ và mới cùng lúc (Make-before-break)
B. Thiết bị ngắt kết nối với trạm gốc cũ hoàn toàn trước khi thiết lập kết nối với trạm gốc mới (Break-before-make)
C. Thiết bị kết nối qua cáp mạng khi chuyển trạm
D. Việc chuyển vùng mất hơn 10 giây
*Đáp án: B*
*Giải thích: Hard Hand-off (chuyển giao cứng) là ngắt kết nối vô tuyến hiện tại trước khi thiết lập kết nối mới. Soft hand-off (chuyển giao mềm - dùng trong CDMA 3G) mới có tính chất "Make-before-break" (Kết nối trước khi ngắt).*

**Câu 144:** Trong mạng 802.11, cơ chế xác thực nào yêu cầu người dùng phải cung cấp tài khoản/mật khẩu hoặc chứng chỉ số qua máy chủ RADIUS?
A. WPA-Personal (WPA-PSK)
B. Open System Authentication
C. Shared Key Authentication (WEP)
D. WPA-Enterprise (802.1X/EAP)
*Đáp án: D*
*Giải thích: Chế độ Doanh nghiệp (Enterprise mode) của WPA/WPA2/WPA3 dựa trên tiêu chuẩn IEEE 802.1X. Nó sử dụng EAP (Extensible Authentication Protocol) để giao tiếp với máy chủ xác thực trung tâm như RADIUS hoặc TACACS+.*

**Câu 145:** "Carrier Aggregation" (Gộp sóng mang) trong LTE-Advanced (4G+) có mục đích chính là gì?
A. Ghép nhiều ăng-ten để thu phát xa hơn
B. Gộp nhiều dải tần số vô tuyến (component carriers) rời rạc lại với nhau để tăng băng thông tổng thể cho một người dùng
C. Kết nối đồng thời Wi-Fi và mạng di động
D. Chia sẻ một kênh tần số cho nhiều người dùng bằng TDMA
*Đáp án: B*
*Giải thích: Gộp sóng mang cho phép thiết bị sử dụng cùng lúc nhiều băng tần (ví dụ băng tần 1800MHz và 2600MHz) gộp lại thành một "ống" dữ liệu lớn hơn, tăng đáng kể tốc độ mạng.*

**Câu 146:** Khi một gói tin IP được gửi từ thiết bị A qua một kết nối Wi-Fi đến Access Point, sau đó ra Internet, quá trình chuyển đổi (translation) loại khung nào diễn ra tại Access Point?
A. Từ khung TCP sang khung UDP
B. Từ khung IPv4 sang khung IPv6
C. Từ khung MAC 802.11 sang khung MAC 802.3 (Ethernet)
D. Từ khung Token Ring sang khung FDDI
*Đáp án: C*
*Giải thích: Access Point hoạt động như một Bridge ở lớp 2. Khi gói tin di chuyển từ môi trường vô tuyến (802.11) sang mạng có dây (thường là 802.3 Ethernet), AP sẽ gỡ bỏ header 802.11 và gắn header 802.3 vào tải trọng IP.*

**Câu 147:** Wi-Fi Direct là công nghệ cho phép các thiết bị thực hiện điều gì?
A. Kết nối thẳng vào hệ thống mạng lõi của nhà mạng di động
B. Kết nối peer-to-peer với nhau mà không cần thông qua một Access Point truyền thống
C. Truyền điện năng không dây
D. Định tuyến lại các gói tin Internet
*Đáp án: B*
*Giải thích: Wi-Fi Direct cho phép hai hoặc nhiều thiết bị Wi-Fi kết nối trực tiếp với nhau (như in ấn từ điện thoại sang máy in) với tốc độ của Wi-Fi thông thường, bằng cách một trong các thiết bị tạm thời đóng vai trò "Soft AP".*

**Câu 148:** Kỹ thuật điều khiển truy cập MAC nào yêu cầu các trạm phải "lắng nghe" môi trường truyền dẫn để chắc chắn rằng không có tín hiệu RF nào đang được phát trước khi bắt đầu truyền dữ liệu?
A. Time Division Multiplexing
B. Token Passing
C. Carrier Sense Multiple Access (CSMA)
D. Code Division Multiple Access
*Đáp án: C*
*Giải thích: Cảm nhận sóng mang (Carrier Sense - CS) là bước đầu tiên trong các giao thức họ CSMA (cả CSMA/CD và CSMA/CA), nơi thiết bị lắng nghe (cảm nhận mức năng lượng vật lý) trên kênh truyền.*

**Câu 149:** Trong mạng Cellular, quá trình mà mạng di động cố gắng tìm vị trí hiện tại (cell nào) của một thiết bị đang ở trạng thái nhàn rỗi (idle) để chuyển một cuộc gọi đến gọi là gì?
A. Hand-off
B. Paging
C. Roaming
D. Authenticating
*Đáp án: B*
*Giải thích: Paging (nhắn gọi) là quá trình mạng phát ra một bản tin quảng bá qua nhiều trạm gốc (trong vùng Location Area) để "đánh thức" và định vị chính xác cell mà thiết bị di động đang kết nối nhằm thiết lập luồng gọi đến.*

**Câu 150:** Tại sao CSMA/CD (Phát hiện đụng độ) không được sử dụng trong mạng không dây (như Wi-Fi) thay cho CSMA/CA?
A. Vì mạng không dây không thể có đụng độ
B. Vì các phần cứng vô tuyến thường là bán song công (half-duplex) và tín hiệu thu rất yếu so với tín hiệu phát, thiết bị không thể vừa phát vừa nghe tín hiệu của người khác để phát hiện đụng độ ngay lập tức
C. Vì việc phát hiện đụng độ vi phạm tiêu chuẩn bảo mật
D. Vì Wi-Fi sử dụng cáp đồng trục nên không cần thiết
*Đáp án: B*
*Giải thích: Ở mạng không dây, sự suy hao năng lượng tín hiệu là rất lớn (theo quy luật bình phương khoảng cách). Khi một thiết bị đang phát tín hiệu công suất cao, nó sẽ "làm điếc" mạch thu của chính nó, khiến việc phát hiện tín hiệu yếu từ một máy khác (dấu hiệu đụng độ) là bất khả thi.*

**Câu 151:** Trong kỹ thuật OFDM (Orthogonal Frequency Division Multiplexing), tại sao các sóng mang phụ (subcarriers) lại được gọi là "trực giao" (Orthogonal)?
A. Vì chúng truyền trên các môi trường vật lý khác nhau
B. Vì đỉnh sóng (peak) của một sóng mang phụ trùng với điểm không (null) của các sóng mang phụ lân cận, giúp triệt tiêu nhiễu xuyên kênh (ICI)
C. Vì chúng luôn vuông góc với nhau trong không gian 3 chiều
D. Vì chúng sử dụng các thuật toán mã hóa khóa công khai
*Đáp án: B*
*Giải thích: Tính trực giao về mặt toán học đảm bảo rằng mặc dù phổ tần số của các sóng mang phụ xếp chồng lên nhau rất sít sao, nhưng chúng không gây nhiễu lẫn nhau khi được giải mã bằng biến đổi Fourier nhanh (FFT).*

**Câu 152:** Chức năng chính của "Guard Interval" (Khoảng thời gian bảo vệ) hoặc Cyclic Prefix trong tín hiệu OFDM là gì?
A. Tăng tốc độ dữ liệu
B. Giảm nhiễu đa đường (Inter-Symbol Interference - ISI) do sự trễ pha của các tia phản xạ
C. Cung cấp mã hóa dữ liệu
D. Tăng khoảng cách truyền sóng
*Đáp án: B*
*Giải thích: Guard Interval sao chép một phần đuôi của biểu tượng (symbol) OFDM và chèn lên phía trước. Điều này tạo ra một vùng đệm hấp thụ các tín hiệu phản xạ (echoes) từ biểu tượng trước đó, ngăn chặn nhiễu liên biểu tượng (ISI).*

**Câu 153:** Thuật ngữ "QoS" (Quality of Service) trong mạng không dây đặc biệt quan trọng để hỗ trợ loại lưu lượng nào?
A. Tải tập tin đính kèm email (SMTP)
B. Duyệt web (HTTP)
C. Thoại qua IP (VoIP) và Video Streaming thời gian thực
D. Truyền tệp tin nền (FTP)
*Đáp án: C*
*Giải thích: Lưu lượng thời gian thực như VoIP và Video rất nhạy cảm với độ trễ (latency) và biến động trễ (jitter), do đó cần các cơ chế QoS để ưu tiên băng thông và đảm bảo chất lượng.*

**Câu 154:** Chuẩn IEEE 802.11e bổ sung tính năng nào quan trọng nhất cho mạng Wi-Fi?
A. Tăng băng thông lên Gigabit
B. Cung cấp cơ chế Quality of Service (QoS) thông qua WMM (Wi-Fi Multimedia)
C. Thay thế hoàn toàn mã hóa WPA2
D. Chuyển sang sử dụng hoàn toàn băng tần 6GHz
*Đáp án: B*
*Giải thích: 802.11e định nghĩa cơ chế MAC cải tiến (EDCA) để phân loại lưu lượng thành 4 danh mục truy cập (Voice, Video, Best Effort, Background) với các mức độ ưu tiên khác nhau.*

**Câu 155:** Trong cơ chế QoS WMM (Wi-Fi Multimedia), lưu lượng nào sau đây được gán mức độ ưu tiên tranh chấp kênh truyền cao nhất (thời gian chờ ngắn nhất)?
A. Background (BK)
B. Best Effort (BE)
C. Video (VI)
D. Voice (VO)
*Đáp án: D*
*Giải thích: Lưu lượng thoại (Voice) yêu cầu độ trễ thấp nhất, do đó WMM gán cho nó các tham số tranh chấp kênh (như AIFS nhỏ nhất và Cwmin nhỏ nhất) để ưu tiên phát trước.*

**Câu 156:** Chế độ tiết kiệm năng lượng (Power Save Mode) tiêu chuẩn của 802.11 hoạt động bằng cách nào?
A. Giảm tốc độ CPU của thiết bị xuống mức tối thiểu
B. Client tắt mạch thu phát vô tuyến (vào chế độ sleep) và định kỳ thức dậy để nghe Beacon xem AP có giữ gói tin (buffered) nào cho nó hay không (thông qua TIM/DTIM)
C. Giảm công suất ăng-ten của Access Point
D. Ngắt kết nối TCP và thiết lập lại sau mỗi phút
*Đáp án: B*
*Giải thích: Thiết bị (Client) báo cho AP biết nó sẽ đi vào chế độ ngủ. AP sẽ lưu trữ các gói tin đến client đó. Client định kỳ thức dậy, nghe khung Beacon (chứa bản đồ TIM/DTIM) để biết có gói tin nào đang đợi mình không, nếu có nó sẽ gửi khung PS-Poll để xin lấy gói tin.*

**Câu 157:** Bản đồ chỉ thị lưu lượng (Traffic Indication Map - TIM) trong khung Beacon của Wi-Fi dùng để làm gì?
A. Định tuyến gói tin IP
B. Báo cho các client đang ở chế độ tiết kiệm năng lượng biết rằng Access Point đang lưu trữ các khung dữ liệu Unicast dành riêng cho chúng
C. Đoạn mã để mã hóa WEP
D. Cấp phát địa chỉ IP động (DHCP)
*Đáp án: B*
*Giải thích: TIM là một danh sách ảo được AP phát trong Beacon, liệt kê ID của các client (Association ID - AID) đang có gói tin bị giữ lại (buffered) tại AP.*

**Câu 158:** Bluetooth (IEEE 802.15.1) thuộc loại mạng không dây nào sau đây?
A. WLAN (Wireless Local Area Network)
B. WMAN (Wireless Metropolitan Area Network)
C. WPAN (Wireless Personal Area Network)
D. WWAN (Wireless Wide Area Network)
*Đáp án: C*
*Giải thích: Bluetooth được thiết kế để kết nối các thiết bị cá nhân (chuột, bàn phím, tai nghe, điện thoại) trong cự ly rất ngắn (vài mét đến khoảng 10 mét), tạo thành một WPAN.*

**Câu 159:** Mạng piconet trong kiến trúc Bluetooth bao gồm tối đa bao nhiêu thiết bị đang hoạt động (active) đồng thời?
A. 1 Master và 3 Slaves
B. 1 Master và 7 Slaves
C. 1 Master và 255 Slaves
D. Không giới hạn
*Đáp án: B*
*Giải thích: Một piconet Bluetooth cho phép một thiết bị đóng vai trò Master điều khiển tối đa 7 thiết bị Slave đang ở trạng thái hoạt động (active) cùng lúc.*

**Câu 160:** Trong Bluetooth, khi nhiều piconet có vùng phủ sóng chồng lấn lên nhau và có một thiết bị tham gia vào nhiều piconet (làm bridge), cấu trúc đó được gọi là gì?
A. Scatternet
B. ESS (Extended Service Set)
C. Mesh Network
D. Ad-hoc
*Đáp án: A*
*Giải thích: Scatternet là một nhóm các piconet được liên kết với nhau bằng cách chia sẻ chung một hoặc nhiều thiết bị. Một thiết bị có thể làm Master ở piconet này và làm Slave ở piconet khác, hoặc làm Slave ở cả hai.*

**Câu 161:** Chuẩn mạng không dây nào được thiết kế đặc biệt cho các ứng dụng cảm biến và tự động hóa nhà thông minh với đặc tính tiêu thụ điện năng cực thấp và chi phí thấp?
A. IEEE 802.11ac (Wi-Fi)
B. IEEE 802.15.4 (Zigbee)
C. 4G LTE
D. IEEE 802.16 (WiMAX)
*Đáp án: B*
*Giải thích: Zigbee (dựa trên chuẩn IEEE 802.15.4) tối ưu hóa cho mạng cảm biến không dây (WSN), truyền dữ liệu tốc độ thấp (250 kbps) nhưng pin có thể duy trì hàng năm.*

**Câu 162:** Kiến trúc mạng điển hình của Zigbee là gì, giúp nó mở rộng vùng phủ sóng và độ tin cậy tự phục hồi (self-healing)?
A. Point-to-Point (Điểm-Điểm)
B. Star (Hình Sao)
C. Mesh (Lưới)
D. Ring (Vòng)
*Đáp án: C*
*Giải thích: Zigbee hỗ trợ mạnh mẽ kiến trúc mạng Lưới (Mesh topology). Các nút mạng (Routers) có thể chuyển tiếp gói tin cho nhau, giúp tự động tìm đường đi thay thế nếu một nút bị hỏng.*

**Câu 163:** Trong Zigbee, thiết bị nào có nhiệm vụ duy nhất là gửi/nhận dữ liệu của chính nó, ngủ hầu hết thời gian để tiết kiệm pin và không thể định tuyến gói tin cho thiết bị khác?
A. Zigbee Coordinator (ZC)
B. Zigbee Router (ZR)
C. Zigbee End Device (ZED)
D. Access Point
*Đáp án: C*
*Giải thích: End Device (Thiết bị đầu cuối) trong mạng Zigbee được tối giản phần cứng, không tham gia vào việc định tuyến (chuyển tiếp gói tin mạng lưới), giúp nó có thể ngủ sâu để tiết kiệm năng lượng tối đa.*

**Câu 164:** Công nghệ RFID (Radio Frequency Identification) thụ động (Passive RFID) hoạt động dựa trên nguyên lý nào?
A. Thẻ RFID có pin nội bộ dùng để phát tín hiệu định kỳ
B. Thẻ RFID thu năng lượng từ sóng điện từ do đầu đọc (Reader) phát ra để bật chip và phản xạ lại tín hiệu mang thông tin ID
C. Sử dụng vệ tinh GPS để định vị thẻ
D. Giao tiếp qua mạng 3G/4G
*Đáp án: B*
*Giải thích: Thẻ RFID thụ động không có pin (no internal power source). Nó hoàn toàn phụ thuộc vào năng lượng điện từ trường cảm ứng do thiết bị đọc (Reader) tạo ra để cấp nguồn cho vi mạch và gửi phản hồi.*

**Câu 165:** Giao thức Mobile IPv6 khác với Mobile IPv4 ở điểm thiết kế cơ bản nào liên quan đến Foreign Agent?
A. Mobile IPv6 yêu cầu nhiều Foreign Agent hơn
B. Mobile IPv6 KHÔNG CẦN Foreign Agent; nó sử dụng các tính năng tự động cấu hình IPv6 (như Stateless Address Autoconfiguration) để tự thiết lập Care-of Address (CoA) tại mạng khách
C. Mobile IPv6 kết hợp Foreign Agent vào trong Home Agent
D. Mobile IPv6 không hỗ trợ Care-of Address
*Đáp án: B*
*Giải thích: Một trong những cải tiến lớn của MIPv6 so với MIPv4 là loại bỏ hoàn toàn thực thể Foreign Agent. Thiết bị di động tự cấu hình Co-located CoA bằng cơ chế SLAAC hoặc DHCPv6 khi chuyển mạng.*

**Câu 166:** Hiện tượng "Phai nhạt đa đường" (Multipath Fading) trong truyền dẫn vô tuyến xảy ra do đâu?
A. Do sự cản trở hoàn toàn của một tòa nhà bằng bê tông cốt thép
B. Do tín hiệu truyền đi từ trạm phát đập vào nhiều vật cản (tòa nhà, cây cối, xe cộ), tạo ra nhiều tia sóng đến trạm nhận ở các thời điểm và pha khác nhau, gây giao thoa triệt tiêu lẫn nhau
C. Do mưa lớn làm suy hao tín hiệu băng tần 2.4GHz
D. Do thiết bị hết pin
*Đáp án: B*
*Giải thích: Phai nhạt đa đường là sự biến động cường độ tín hiệu rất nhanh do sự giao thoa (có thể là tăng cường hoặc triệt tiêu) giữa tia sóng trực tiếp và các tia sóng phản xạ, khúc xạ từ môi trường xung quanh.*

**Câu 167:** Hiện tượng "Trải trễ" (Delay Spread) trong môi trường truyền đa đường dẫn đến hậu quả nghiêm trọng gì trong truyền thông số tốc độ cao?
A. Làm tăng công suất tiêu thụ của thiết bị
B. Gây nhiễu liên biểu tượng (ISI - Inter-Symbol Interference), nơi phần đuôi của biểu tượng trước chồng lấn lên biểu tượng sau do đến muộn
C. Làm tín hiệu bị mã hóa sai
D. Thay đổi địa chỉ MAC của gói tin
*Đáp án: B*
*Giải thích: Vì các tia đa đường di chuyển qua các quãng đường dài ngắn khác nhau, chúng đến máy thu vào các thời điểm khác nhau. Sự chênh lệch thời gian này (trải trễ) khiến các bit/symbol đi liền kề nhau bị nhòe và trộn lẫn vào nhau, gây nhiễu ISI.*

**Câu 168:** Công nghệ di động nào lần đầu tiên hiện thực hóa tầm nhìn về một mạng viễn thông toàn cầu duy nhất, dựa trên IP (All-IP), loại bỏ hoàn toàn mạng chuyển mạch kênh truyền thống cho thoại?
A. 2G (GSM)
B. 3G (UMTS)
C. 4G (LTE)
D. 1G (AMPS)
*Đáp án: C*
*Giải thích: 4G LTE/EPC được thiết kế ngay từ đầu như một kiến trúc dựa trên gói (packet-switched), nơi tất cả dữ liệu, bao gồm cả dịch vụ thoại thời gian thực (VoLTE), đều chạy trên nền tảng IP.*

**Câu 169:** Trong mạng di động, "Vị trí khu vực" (Location Area - LA) hoặc "Vùng theo dõi" (Tracking Area - TA trong LTE) là gì?
A. Tọa độ GPS chính xác của người dùng
B. Một nhóm các ô (cells) kế cận nhau; mạng sẽ chỉ gửi bản tin Paging tới các ô trong vùng này khi cần tìm một thiết bị đang ở trạng thái Idle
C. Khoảng cách vật lý tối đa từ trạm gốc đến thiết bị
D. Tên gọi khác của Home Network
*Đáp án: B*
*Giải thích: Để tránh phải Paging toàn bộ mạng lưới (rất tốn tài nguyên vô tuyến), mạng chia thành các vùng Tracking Area (gồm nhiều cell). Trạng thái Idle của UE chỉ được mạng theo dõi ở mức độ Tracking Area. Khi có cuộc gọi đến, mạng chỉ phát Paging trong các cell thuộc Tracking Area mà UE đã đăng ký gần nhất.*

**Câu 170:** Tính năng nào của Bluetooth cho phép thiết bị chỉ cần "chạm" hoặc đặt sát nhau là có thể ghép nối (pairing) nhanh chóng một cách an toàn mà không cần nhập mã PIN?
A. OFDM
B. NFC (Near Field Communication) OOB (Out-of-Band) pairing
C. Zigbee Routing
D. WPA3 SAE
*Đáp án: B*
*Giải thích: Các thiết bị có thể sử dụng kết nối trường gần (NFC) như một kênh Out-of-Band bảo mật phụ trợ để trao đổi nhanh khóa thiết lập kết nối Bluetooth (pairing) chỉ bằng thao tác chạm.*

**Câu 171:** Sự suy hao tín hiệu theo khoảng cách trong không gian tự do (Free Space Path Loss) tuân theo quy luật nào đối với khoảng cách (d)?
A. Suy hao tỉ lệ thuận với d
B. Suy hao tỉ lệ nghịch với d
C. Suy hao tỉ lệ thuận với bình phương khoảng cách ($d^2$)
D. Suy hao không phụ thuộc vào khoảng cách
*Đáp án: C*
*Giải thích: Theo định luật bình phương nghịch đảo, mật độ năng lượng của sóng vô tuyến bức xạ ra mọi hướng (đẳng hướng) giảm tỉ lệ thuận với bình phương khoảng cách từ nguồn phát.*

**Câu 172:** Trong mô hình TCP/IP, khi chuyển từ kết nối có dây (như Ethernet) sang kết nối không dây (như Wi-Fi 802.11) có BER (Tỉ lệ lỗi bit) cao hơn nhiều, giao thức TCP thường gặp vấn đề gì?
A. TCP tự động chuyển sang UDP
B. TCP không thể hoạt động trên môi trường vô tuyến
C. TCP hiểu nhầm các gói tin bị mất do lỗi sóng vô tuyến là hiện tượng nghẽn mạng (Congestion), từ đó kích hoạt cơ chế giảm tốc độ truyền (Slow Start/Congestion Avoidance) một cách không cần thiết, làm giảm nghiêm trọng thông lượng
D. TCP bị tấn công Man-in-the-Middle dễ dàng hơn
*Đáp án: C*
*Giải thích: Cốt lõi của TCP là thuật toán kiểm soát tắc nghẽn dựa trên giả định rằng gói tin bị mất chủ yếu do router bị tràn bộ đệm. Tuy nhiên, trong mạng không dây, gói tin bị mất thường do nhiễu vật lý. Việc TCP cắt giảm tốc độ truyền (CWnd) khi có nhiễu sóng là hành vi sai lầm, làm suy giảm hiệu suất đáng kể.*

**Câu 173:** Cơ chế SACK (Selective Acknowledgment) trong TCP giúp giải quyết vấn đề gì, đặc biệt hữu ích trong môi trường mạng không dây có tỷ lệ mất gói tin (packet loss) rải rác?
A. Cho phép bên nhận báo cáo chính xác các khối dữ liệu (blocks) rời rạc đã nhận được thành công, giúp bên gửi chỉ cần truyền lại chính xác những gói bị thiếu (thay vì truyền lại toàn bộ từ điểm bị lỗi như cơ chế Go-Back-N truyền thống)
B. Bỏ qua các gói tin bị mất để giữ nguyên tốc độ
C. Ưu tiên gửi các gói tin có kích thước nhỏ
D. Mã hóa các gói tin phản hồi
*Đáp án: A*
*Giải thích: Với tỷ lệ mất gói ngẫu nhiên cao trong mạng không dây, SACK giúp tối ưu hóa băng thông truyền lại bằng cách chỉ định chính xác các khoảng (ranges) dữ liệu bị rớt, hạn chế việc truyền lại thừa thãi dữ liệu đã đến đích an toàn.*

**Câu 174:** Trong mạng Cellular, thuật ngữ "Frequency Reuse" (Tái sử dụng tần số) đề cập đến khái niệm nào?
A. Sử dụng cùng một tần số cho Wi-Fi và mạng di động
B. Tái sử dụng một tập hợp các kênh tần số ở các ô (cells) cách xa nhau về mặt địa lý đủ để nhiễu đồng kênh (co-channel interference) nằm ở mức chấp nhận được, giúp tăng tổng dung lượng của hệ thống
C. Chuyển đổi tần số liên tục trong một cuộc gọi
D. Thu hồi dải tần của đài phát thanh để dùng cho di động
*Đáp án: B*
*Giải thích: Tái sử dụng tần số là nền tảng của mạng tế bào (cellular network). Vì dải phổ vô tuyến là hữu hạn, một tập các dải tần số phải được lặp lại ở các cụm (cluster) cell khác nhau, miễn là khoảng cách tái sử dụng (D) đủ lớn để giảm thiểu nhiễu Co-channel.*

**Câu 175:** Trong lập kế hoạch mạng di động, "Kích thước cụm" (Cluster Size - K) biểu thị điều gì?
A. Số lượng người dùng trong một ô
B. Số lượng ăng-ten trên một cột thu phát sóng
C. Số lượng các ô kế cận nhau chia sẻ toàn bộ phổ tần số khả dụng của hệ thống (mỗi ô dùng một dải tần số khác nhau, K thường là 1, 3, 4, 7, 12,...)
D. Kích thước vật lý của thiết bị trạm gốc
*Đáp án: C*
*Giải thích: Nếu tổng số kênh là S và kích thước cụm là K, thì số kênh mỗi ô được cấp là S/K. Các ô trong cùng một cụm sẽ không dùng chung bất kỳ tần số nào để tránh nhiễu. Cụm đó sẽ được nhân bản (tái sử dụng) trên toàn mạng lưới.*

**Câu 176:** Trong hệ thống CDMA (Code Division Multiple Access), làm thế nào bộ thu nhận (receiver) có thể tách được tín hiệu của một người dùng cụ thể ra khỏi tín hiệu nhiễu hỗn hợp của tất cả những người dùng khác đang phát trên cùng một dải tần số?
A. Dựa vào thời gian phát sóng (Timeslot)
B. Bằng cách thực hiện phép tương quan (Correlation) giữa tín hiệu thu được với một mã giả ngẫu nhiên (Pseudorandom Noise - PN Code) đặc trưng, khớp chính xác với mã của người dùng đó
C. Dựa vào địa chỉ IP của thiết bị
D. Sử dụng bộ lọc dải thông tần số cực hẹp
*Đáp án: B*
*Giải thích: Các mã trong CDMA được thiết kế trực giao (orthogonal) với nhau. Khi tính tích phân chập (correlation), tín hiệu của mã đúng sẽ hội tụ thành đỉnh (khôi phục dữ liệu), trong khi các tín hiệu của mã khác sẽ triệt tiêu hoặc biến thành nhiễu nền cường độ thấp.*

**Câu 177:** Kỹ thuật nào trong mạng WCDMA (3G) cho phép thiết bị di động (UE) giữ liên kết với nhiều trạm gốc (NodeB) đồng thời trong quá trình chuyển giao, đảm bảo không bao giờ bị rớt cuộc gọi giữa chừng?
A. Hard Hand-off
B. Soft Hand-off (Chuyển giao mềm)
C. Inter-system Hand-off
D. Ping-pong Hand-off
*Đáp án: B*
*Giải thích: Trong Soft Hand-off, do tất cả các cell 3G dùng chung một dải tần số, thiết bị có thể thu/phát dữ liệu đồng thời với trạm cũ và trạm mới. Mạng (RNC) sẽ kết hợp (combine) tín hiệu tốt nhất từ cả hai phía trước khi cắt hẳn kết nối với trạm cũ khi tín hiệu của nó quá yếu.*

**Câu 178:** Chức năng của RNC (Radio Network Controller) trong kiến trúc mạng 3G (UMTS) là gì?
A. Quản lý việc định tuyến gói tin IP ra Internet
B. Quản lý tài nguyên vô tuyến (như cấp mã CDMA, kiểm soát công suất) và điều khiển nhiều trạm gốc NodeB
C. Đóng vai trò làm tường lửa bảo mật
D. Lưu trữ cơ sở dữ liệu người dùng (Billing/SIM)
*Đáp án: B*
*Giải thích: RNC chịu trách nhiệm phần "trí tuệ" của mạng truy nhập vô tuyến, bao gồm phân bổ kênh, xử lý Soft Hand-off, kiểm soát công suất vòng ngoài (outer-loop power control) đối với các NodeB thuộc quyền.*

**Câu 179:** Tại sao trong kiến trúc 4G LTE, thực thể RNC (Radio Network Controller) của 3G lại bị loại bỏ?
A. Vì 4G không cần quản lý tài nguyên vô tuyến
B. Để đơn giản hóa kiến trúc mạng (Flat Architecture), giảm độ trễ bằng cách tích hợp trực tiếp các chức năng của RNC vào các trạm gốc thông minh eNodeB
C. Vì 4G chỉ sử dụng Wi-Fi
D. Vì SGW (Serving Gateway) đã đảm nhiệm vai trò này
*Đáp án: B*
*Giải thích: Việc loại bỏ nút mạng trung gian RNC tạo ra một mạng lưới "phẳng" (Flat IP network). eNodeB trong LTE tự xử lý toàn bộ các giao thức quản lý vô tuyến, giúp dữ liệu từ thiết bị đến mạng lõi nhanh hơn nhiều (độ trễ siêu thấp).*

**Câu 180:** "Cơ chế kiểm soát lỗi vòng tự động kết hợp" (Hybrid ARQ - HARQ) được sử dụng phổ biến trong mạng 4G/5G có điểm gì khác biệt so với ARQ tiêu chuẩn (như trong TCP)?
A. HARQ không bao giờ yêu cầu gửi lại gói tin
B. HARQ kết hợp mã sửa lỗi tới (FEC) vào gói tin. Khi nhận gói tin bị lỗi, thay vì vứt bỏ hoàn toàn như ARQ, bộ thu sẽ giữ lại dữ liệu hỏng đó (Soft-combining) và gộp với bản sao được truyền lại để tăng xác suất giải mã thành công
C. HARQ chỉ áp dụng cho dữ liệu thoại
D. HARQ dựa vào checksum IP
*Đáp án: B*
*Giải thích: Việc kết hợp (combining) các bản sao bị lỗi yếu giúp tăng tỷ lệ tín hiệu trên nhiễu (SNR/SINR), cho phép giải mã dữ liệu trong môi trường vô tuyến khắc nghiệt mà nếu chỉ dùng ARQ thuần túy thì sẽ phải truyền lại vô số lần.*

**Câu 181:** Một cuộc tấn công "Rogue Access Point" (AP giả mạo) nhắm vào mục tiêu gì?
A. Làm hỏng phần cứng của AP thật bằng điện áp cao
B. Lừa các thiết bị người dùng (client) tự nguyện kết nối vào một Access Point do kẻ tấn công kiểm soát, từ đó có thể nghe lén, chặn bắt (sniff) hoặc thao túng (Man-in-the-Middle) dữ liệu chưa mã hóa
C. Gây nhiễu tần số (Jamming) để chặn liên lạc
D. Thay đổi mã PIN của router
*Đáp án: B*
*Giải thích: Hacker thiết lập một AP với SSID giống hệt (hoặc hấp dẫn như "Free Wi-Fi") và tín hiệu mạnh hơn AP thật. Các thiết bị tự động chọn AP mạnh nhất, vô tình gửi mọi traffic qua máy của hacker.*

**Câu 182:** Kỹ thuật "Evil Twin" (Anh em sinh đôi độc ác) là một dạng cụ thể của loại tấn công mạng không dây nào?
A. Tấn công DDoS
B. Rogue Access Point
C. ARP Spoofing
D. MAC Flooding
*Đáp án: B*
*Giải thích: Evil Twin là thuật ngữ chỉ một Rogue AP giả mạo chính xác địa chỉ MAC (BSSID) và SSID của mạng hợp pháp, đánh lừa các cơ chế bảo mật tinh vi hơn để ép người dùng kết nối (thường thông qua việc kích hoạt tấn công giải xác thực - Deauth attack vào AP thật).*

**Câu 183:** Mục đích của cuộc tấn công Giải xác thực (Deauthentication Attack) trong mạng Wi-Fi 802.11 là gì?
A. Đánh cắp gói tin dữ liệu
B. Giải mã khóa WPA2
C. Gửi các khung quản lý (Deauth frames) mạo danh địa chỉ MAC của AP hoặc Client để buộc client ngắt kết nối, nhằm gây từ chối dịch vụ (DoS) hoặc ép client phải kết nối lại (ví dụ để bắt gói tin Handshake WPA2)
D. Thay đổi mật khẩu Wi-Fi
*Đáp án: C*
*Giải thích: Do các khung quản lý (management frames) trong 802.11 nguyên bản không được mã hóa và xác thực, kẻ tấn công có thể giả mạo địa chỉ MAC gửi lệnh "ngắt kết nối" giả đến máy nạn nhân. Nạn nhân sẽ tuân theo và rớt mạng.*

**Câu 184:** Tiêu chuẩn nào được IEEE ban hành để khắc phục các lỗ hổng như Deauth Attack bằng cách áp dụng mã hóa bảo vệ cho các khung tin quản lý (Management Frame Protection - MFP)?
A. IEEE 802.11a
B. IEEE 802.11w
C. IEEE 802.1X
D. IEEE 802.11n
*Đáp án: B*
*Giải thích: Chuẩn 802.11w (sau này được gộp vào 802.11 tiêu chuẩn và bắt buộc trong WPA3) ngăn chặn giả mạo khung quản lý (như Deauthentication và Disassociation) bằng cách yêu cầu xác thực bằng khóa mật mã trước khi thiết bị chấp nhận các lệnh này.*

**Câu 185:** Mã hóa WPA3 Personal nâng cấp giao thức bảo mật cốt lõi nào để chống lại các cuộc tấn công Brute-force/Dictionary (đoán mật khẩu) Offline, ngay cả khi người dùng đặt mật khẩu yếu?
A. 4-Way Handshake
B. SAE (Simultaneous Authentication of Equals) thay thế cho PSK (Pre-Shared Key)
C. TKIP
D. MD5
*Đáp án: B*
*Giải thích: Giao thức SAE (dựa trên thuật toán trao đổi khóa Dragonfly) đảm bảo Forward Secrecy. Nó giới hạn kẻ tấn công chỉ có thể thử một mật khẩu cho mỗi lần tương tác trực tiếp với AP, làm vô hiệu hóa hoàn toàn việc bắt gói tin rồi mang về chạy phần mềm crack offline hàng triệu mật khẩu mỗi giây.*

**Câu 186:** Mạng Sensor Network (WSN - Mạng cảm biến không dây) thường có đặc điểm vật lý nào khác biệt rõ rệt so với mạng Wi-Fi thông thường?
A. Tốc độ truyền tải Gigabits mỗi giây
B. Sử dụng cáp quang để kết nối các node
C. Số lượng node (cảm biến) rất lớn, rải rác trên diện rộng, tự tổ chức (ad-hoc), có tài nguyên tính toán và pin cực kỳ hạn chế
D. Sử dụng giao thức TCP/IP truyền thống trên toàn bộ mạng lưới
*Đáp án: C*
*Giải thích: WSN bao gồm hàng trăm hoặc hàng ngàn nút nhỏ gọn (motes). Yêu cầu quan trọng nhất của WSN là thuật toán định tuyến và MAC phải cực kỳ tiết kiệm năng lượng (Energy-efficient) để duy trì tuổi thọ pin lâu dài.*

**Câu 187:** Trong hệ thống RFID, dải tần số vô tuyến siêu cao (UHF) thường cung cấp đặc tính nào sau đây cho hệ thống đọc thẻ?
A. Chỉ đọc được ở khoảng cách dưới 1 cm (như NFC)
B. Bị vô hiệu hóa hoàn toàn bởi gỗ và nhựa
C. Khoảng cách đọc xa (đến vài mét) và có thể quét được hàng loạt (bulk reading) hàng trăm thẻ cùng lúc (ứng dụng kho bãi, logistics)
D. Hỗ trợ băng thông 54 Mbps
*Đáp án: C*
*Giải thích: RFID UHF (phổ biến ở băng tần 860-960 MHz) được ứng dụng mạnh mẽ trong quản lý chuỗi cung ứng vì Reader có thể bắt sóng phản xạ của các thẻ (tags) dán trên các thùng hàng từ khoảng cách khá xa.*

**Câu 188:** Công nghệ di động V2X (Vehicle-to-Everything) trong hạ tầng giao thông thông minh sử dụng nền tảng mạng nào để các xe ô tô tự động giao tiếp với nhau (V2V) và với hạ tầng (V2I)?
A. DSRC (Dedicated Short-Range Communications dựa trên 802.11p) và C-V2X (Cellular V2X dựa trên LTE/5G)
B. WPAN (Bluetooth Low Energy)
C. Ethernet cáp đồng
D. Vệ tinh quỹ đạo địa tĩnh (GEO)
*Đáp án: A*
*Giải thích: V2X được chuẩn hóa dựa trên hai nhánh công nghệ chính: DSRC (một biến thể của Wi-Fi tối ưu cho độ trễ thấp ở môi trường di chuyển nhanh) và Cellular-V2X (sử dụng phổ của nhà mạng, tận dụng hạ tầng 4G/5G URLLC).*

**Câu 189:** Giao thức định tuyến AODV (Ad-hoc On-Demand Distance Vector) được sử dụng phổ biến trong mạng MANET (Mạng Ad-hoc không dây di động) hoạt động theo nguyên tắc nào?
A. Định kỳ gửi bảng định tuyến đến toàn bộ mạng (Proactive)
B. Chỉ tìm kiếm và thiết lập tuyến đường (Route Discovery) bằng cách broadcast gói yêu cầu (RREQ) KHI VÀ CHỈ KHI có dữ liệu cần gửi đi (Reactive / On-Demand)
C. Tính toán đường đi tập trung tại một máy chủ SDN
D. Luôn định tuyến gói tin theo hình vòng tròn
*Đáp án: B*
*Giải thích: Do tính chất topo mạng liên tục thay đổi trong MANET, các thuật toán Reactive như AODV chỉ tiêu tốn băng thông và năng lượng để tìm đường khi có nhu cầu thực tế, phù hợp với môi trường động hơn là duy trì liên tục bảng định tuyến toàn cục.*

**Câu 190:** "Mạng Lưới Không Dây" (Wireless Mesh Network - WMN) ở quy mô thành phố thường sử dụng cấu trúc gồm các thành phần nào?
A. Chỉ toàn các End User Devices kết nối với nhau
B. Các Router Mesh cấu thành một bộ khung hạ tầng tĩnh (Backbone), định tuyến dữ liệu không dây cho nhau và cuối cùng chuyển tới một hoặc nhiều Gateway ra Internet
C. Một AP trung tâm duy nhất phát sóng cho toàn thành phố
D. Vệ tinh thu phát trực tiếp tới điện thoại
*Đáp án: B*
*Giải thích: Hạ tầng Mesh gồm nhiều điểm phát sóng (Mesh Node) liên kết vô tuyến với nhau để truyền tải (backhaul) lưu lượng từ các Client về các điểm có cáp quang ra Internet (Gateway), loại bỏ việc phải kéo cáp đến từng điểm phát.*

**Câu 191:** Trong mạng 5G, công nghệ "Massive MIMO" khác với MIMO thông thường của Wi-Fi ở điểm cốt lõi nào?
A. Sử dụng dải tần AM/FM
B. Tích hợp số lượng ăng-ten cực lớn (có thể lên tới 64, 128 hoặc nhiều hơn) trên một trạm gốc duy nhất, tạo ra các chùm sóng (beams) siêu nhỏ, không gian hóa (spatial resolution) cho hàng chục người dùng đồng thời trên cùng một tài nguyên thời gian/tần số
C. Chỉ có 1 ăng-ten phát và nhiều ăng-ten nhận
D. Tăng khoảng cách phát sóng lên gấp 100 lần
*Đáp án: B*
*Giải thích: Massive MIMO là công nghệ đột phá của 5G (tập trung chủ yếu ở băng tần C-band), kết hợp Beamforming tiên tiến (3D Beamforming) để phục vụ đồng thời nhiều UE bằng cách "đẩy" luồng tín hiệu theo các hướng không gian khác nhau.*

**Câu 192:** Băng tần sóng Milimet (mmWave) trong mạng 5G (FR2 - dải tần trên 24GHz) mang lại đặc tính gì nổi bật?
A. Băng thông cực kỳ lớn (Gigabits) nhưng khả năng đâm xuyên vật cản (tường, kính) cực kỳ kém và khoảng cách phủ sóng rất ngắn
B. Xuyên qua các tòa nhà dễ dàng nhưng băng thông thấp
C. Có thể truyền tín hiệu đi xa hàng trăm km
D. Không bị ảnh hưởng bởi nhiễu môi trường như mưa
*Đáp án: A*
*Giải thích: Tần số càng cao, bước sóng càng ngắn (tới mức milimet). Sóng mmWave cung cấp "ống nước" khổng lồ cho tốc độ truyền tải cực khủng, nhưng năng lượng nhanh chóng bị suy hao trong không khí và gần như bị chặn đứng bởi cây cối, con người hoặc tường bê tông. Cần sử dụng các trạm phát sóng siêu nhỏ (Small Cells) rải rác dày đặc.*

**Câu 193:** Chuẩn Wi-Fi 6 (IEEE 802.11ax) giải quyết bài toán môi trường mật độ cao (sân vận động, hội trường, văn phòng đông đúc) bằng cách vay mượn công nghệ cốt lõi nào từ mạng di động 4G LTE?
A. DSSS (Direct-Sequence Spread Spectrum)
B. OFDMA (Orthogonal Frequency-Division Multiple Access)
C. CSMA/CD
D. Token Ring
*Đáp án: B*
*Giải thích: OFDMA (chữ A - Access) cho phép AP chia kênh tần số vô tuyến thành các khối tài nguyên nhỏ (Resource Units - RU). Một khung truyền duy nhất của AP có thể giao tiếp đồng thời (cả nhận và gửi) với nhiều thiết bị Client khác nhau bằng cách phân bổ các RU khác nhau cho chúng, giảm thiểu hoàn toàn sự tranh chấp vô ích.*

**Câu 194:** Tính năng "Target Wake Time" (TWT) trong Wi-Fi 6 (802.11ax) mang lại lợi ích đặc biệt nào cho các thiết bị IoT (Internet of Things)?
A. Tăng tốc độ tính toán cho chip
B. Cho phép AP và Client thương lượng trước các lịch trình thời gian cụ thể (còn gọi là target wake time) để thức dậy và truyền dữ liệu, thay vì phải kiểm tra Beacon thường xuyên, giúp kéo dài thời lượng pin lên đáng kể
C. Cho phép đánh thức thiết bị bằng tin nhắn SMS
D. Cải thiện khả năng mã hóa dữ liệu
*Đáp án: B*
*Giải thích: Với TWT, các thiết bị (ví dụ cảm biến nông nghiệp) có thể thương lượng để đi vào trạng thái ngủ sâu (deep sleep) trong vài ngày, vài tuần và chỉ thức dậy vào những giây phút cực kỳ chính xác để truyền, tối ưu hóa năng lượng.*

**Câu 195:** Trong kiến trúc Wi-Fi doanh nghiệp có sử dụng Wireless LAN Controller (WLC) tập trung, Access Point hoạt động ở chế độ nào sau đây để chia sẻ tải xử lý với Controller?
A. Standalone Mode (Autonomous AP)
B. Lightweight Mode (CAPWAP/LWAPP)
C. Ad-hoc Mode
D. Bridge Mode
*Đáp án: B*
*Giải thích: Các "Lightweight Access Points" (LAP) không xử lý toàn bộ stack mạng (Split-MAC architecture). Chúng gửi toàn bộ các gói tin quản lý và dữ liệu qua đường hầm CAPWAP về Controller trung tâm để xác thực, cấu hình mạng và áp dụng chính sách bảo mật.*

**Câu 196:** Ưu điểm chính của kiến trúc Controller-based WLAN (Sử dụng WLC tập trung) so với Autonomous WLAN (Các AP hoạt động độc lập) là gì?
A. Chi phí thiết bị rẻ hơn
B. Khả năng tự động điều chỉnh kênh RF, công suất phát, xử lý chuyển vùng (Roaming) mượt mà cho hàng ngàn Client và quản lý chính sách bảo mật từ một điểm duy nhất
C. Cho phép sử dụng chuẩn 802.11 b cũ
D. AP không cần kết nối với cáp mạng
*Đáp án: B*
*Giải thích: Khi có một "bộ não" trung tâm (WLC) nhìn thấy toàn bộ bản đồ sóng vô tuyến, nó có thể tối ưu hóa phổ tần số (Radio Resource Management - RRM), tránh nhiễu và cung cấp trải nghiệm seamless roaming nhanh (Fast Roaming 802.11r) khi thiết bị người dùng di chuyển khắp tòa nhà.*

**Câu 197:** Chức năng "Fast BSS Transition" (IEEE 802.11r) trong mạng Wi-Fi doanh nghiệp có vai trò gì quan trọng đối với các cuộc gọi VoWLAN (Voice over WLAN)?
A. Tăng băng thông âm thanh lên chuẩn HD
B. Cho phép trao đổi trước các khóa bảo mật (802.1X/EAP) giữa các AP thông qua mạng lõi, giảm thời gian xác thực khi thiết bị di chuyển từ AP này sang AP khác xuống dưới 50ms, tránh hiện tượng đứt quãng cuộc gọi thoại
C. Tự động ngắt kết nối các thiết bị chiếm quá nhiều băng thông
D. Mở rộng dải tần số âm thanh
*Đáp án: B*
*Giải thích: Mọi dịch vụ thoại (VoIP) sẽ bị ngắt tiếng nếu độ trễ vượt quá 150ms. Việc thực hiện lại Handshake 802.1X toàn phần mất tới vài trăm mili-giây. 802.11r giảm thiểu quá trình này bằng cách tối ưu hóa việc phân phối khóa.*

**Câu 198:** Trong mạng cảm biến không dây, thuật toán MAC S-MAC (Sensor-MAC) sử dụng cơ chế nào để giảm tiêu thụ điện năng (giảm hiện tượng nghe trộm - idle listening)?
A. Truyền dữ liệu liên tục 24/7
B. Đồng bộ chu kỳ Ngủ/Thức (Sleep/Listen schedules) định kỳ giữa các node lân cận, sao cho chúng cùng thức giấc để trao đổi dữ liệu và cùng đi vào trạng thái ngủ sâu để tiết kiệm năng lượng
C. Tăng công suất phát
D. Sử dụng cáp quang
*Đáp án: B*
*Giải thích: S-MAC giải quyết vấn đề "Idle Listening" (nút mạng thức và nghe dù kênh rỗng, tiêu thụ pin gần bằng lúc thu dữ liệu). Bằng cách nhóm các nút thành các virtual cluster có chung lịch Sleep/Wake, hệ thống giảm tối đa thời gian bật module vô tuyến.*

**Câu 199:** Một "Trạm Không Gian Di Động" (High Altitude Platform Station - HAPS) sử dụng khinh khí cầu hoặc máy bay không người lái để cung cấp Internet băng thông rộng thuộc loại mạng không dây nào?
A. WPAN
B. Cellular Networks
C. Dịch vụ vệ tinh quỹ đạo thấp (LEO)
D. Hạ tầng mạng Stratospheric (Tầng bình lưu)
*Đáp án: D*
*Giải thích: HAPS là các trạm phát sóng được neo đậu hoặc bay ở tầng bình lưu (khoảng 20km). Chúng có lợi thế là bao phủ vùng rộng lớn (hơn tháp di động mặt đất) nhưng không xa như vệ tinh, đem lại độ trễ thấp hơn nhiều so với vệ tinh.*

**Câu 200:** Trong công nghệ truyền thông khoảng cách siêu ngắn, kỹ thuật Ultra-Wideband (UWB - IEEE 802.15.4z) có ứng dụng chủ chốt nào nhờ khả năng đo thời gian bay của tín hiệu (Time-of-Flight) với độ chính xác cao?
A. Xem video 8K trên TV
B. Cung cấp kết nối Internet tốc độ cao cho toàn thành phố
C. Định vị chính xác vị trí trong nhà (Indoor Positioning) ở mức độ centimet (cm) và tính năng chìa khóa xe hơi kỹ thuật số an toàn
D. Thay thế mạng cáp quang liên lục địa
*Đáp án: C*
*Giải thích: UWB sử dụng các xung tín hiệu cực ngắn (nano giây) trải trên băng thông rất rộng (trên 500 MHz). Đặc điểm xung ngắn cho phép đo khoảng cách giữa các thiết bị thông qua thời gian truyền (Time-of-Flight) chính xác đến từng centimet, dùng trong tìm kiếm đồ vật (ví dụ AirTag) hoặc định vị bảo mật.*

**Câu 201:** Trong kiến trúc mạng di động, giao diện vô tuyến (Air Interface) kết nối giữa thiết bị người dùng (UE) và trạm gốc (eNodeB trong LTE) được gọi là gì?
A. S1-MME
B. LTE-Uu
C. X2
D. S1-U
*Đáp án: B*
*Giải thích: LTE-Uu là tên gọi kỹ thuật của giao diện không dây vô tuyến giữa User Equipment (UE) và E-UTRAN Node B (eNodeB), đây là giao diện quan trọng nhất quyết định tốc độ và chất lượng sóng.*

**Câu 202:** Giao diện nào trong kiến trúc LTE được sử dụng để kết nối trực tiếp các trạm gốc (eNodeB) với nhau, phục vụ chủ yếu cho việc chuyển giao (Handover) nhanh mà không cần đi qua mạng lõi?
A. Giao diện S1
B. Giao diện Uu
C. Giao diện X2
D. Giao diện S5/S8
*Đáp án: C*
*Giải thích: Giao diện X2 cho phép các eNodeB giao tiếp trực tiếp (peer-to-peer), trao đổi thông tin tải (load) và quản lý quá trình X2-Handover, giúp giảm độ trễ khi người dùng chuyển vùng.*

**Câu 203:** Thành phần nào trong Mạng Lõi Gói Tiến Hóa (EPC - Evolved Packet Core) đóng vai trò là điểm neo (mobility anchor) cho dữ liệu người dùng khi họ di chuyển giữa các eNodeB?
A. MME (Mobility Management Entity)
B. SGW (Serving Gateway)
C. PGW (Packet Data Network Gateway)
D. HSS (Home Subscriber Server)
*Đáp án: B*
*Giải thích: SGW xử lý mặt phẳng người dùng (user plane), định tuyến và chuyển tiếp các gói dữ liệu. Nó hoạt động như một điểm neo di động cục bộ; khi UE chuyển từ eNodeB này sang eNodeB khác, kết nối từ SGW đến mạng lõi vẫn được giữ nguyên.*

**Câu 204:** Nút mạng nào trong EPC (4G) là cổng giao tiếp ra các mạng dữ liệu gói bên ngoài (như Internet, mạng doanh nghiệp riêng) và thực hiện cấp phát địa chỉ IP cho thiết bị di động?
A. MME
B. SGW
C. PGW (Packet Data Network Gateway)
D. PCRF
*Đáp án: C*
*Giải thích: PGW là điểm thoát/vào (exit/entry point) cho luồng dữ liệu của UE. Nó gán địa chỉ IP cho UE, thực hiện lọc gói (packet filtering), áp dụng chính sách cước phí (charging) và là điểm neo (anchor) di động giữa hệ thống 3GPP và non-3GPP.*

**Câu 205:** Cơ sở dữ liệu trung tâm trong mạng 4G LTE chứa toàn bộ thông tin về hồ sơ thuê bao, khóa xác thực và trạng thái vị trí của người dùng được gọi là gì?
A. VLR (Visitor Location Register)
B. HLR (Home Location Register)
C. HSS (Home Subscriber Server)
D. EIR (Equipment Identity Register)
*Đáp án: C*
*Giải thích: HSS là bản nâng cấp kết hợp của HLR và AuC trong các thế hệ mạng trước. Nó là siêu cơ sở dữ liệu lưu trữ thông tin nhận dạng (IMSI), khóa bí mật (K) dùng cho xác thực và thông tin về dịch vụ mà thuê bao được phép dùng.*

**Câu 206:** Giao thức nào được sử dụng phổ biến trong mạng lõi 4G/5G (ở mặt phẳng điều khiển - Control Plane) để truyền tải các bản tin báo hiệu như đường hầm GTP (GTP-C) thay thế cho UDP/TCP truyền thống nhằm đảm bảo độ tin cậy cao mà không bị chặn đầu dòng (Head-of-Line Blocking)?
A. SCTP (Stream Control Transmission Protocol)
B. ICMP
C. RTP (Real-time Transport Protocol)
D. IPSec
*Đáp án: A*
*Giải thích: SCTP được thiết kế cho báo hiệu viễn thông (SIGTRAN). Nó cung cấp tính năng đa luồng (multi-streaming) để tránh Head-of-Line Blocking và đa kết nối (multi-homing) để tăng khả năng dự phòng (redundancy) mạng.*

**Câu 207:** Tính năng "Carrier Sense" trong CSMA có nghĩa là gì?
A. Thiết bị tự động cảm biến công suất phát của AP
B. Lắng nghe sóng vô tuyến để xem có năng lượng RF (tín hiệu của một trạm khác) đang truyền trên kênh hiện tại hay không trước khi phát dữ liệu
C. Phát hiện sóng điện từ của các thiết bị gia dụng
D. Cảm biến sự thay đổi của tầng điện ly
*Đáp án: B*
*Giải thích: "Carrier" ở đây chỉ sóng mang. "Sense" là lắng nghe. Trạm sẽ đo mức năng lượng vô tuyến hiện tại. Nếu vượt quá ngưỡng (CCA threshold), nó coi kênh là đang bận.*

**Câu 208:** Phương thức xác thực nào của chuẩn 802.11 nguyên thủy (Legacy) là cực kỳ không an toàn vì nó gửi chuỗi thử thách (challenge text) dưới dạng bản rõ và mã hóa RC4, dễ dàng bị kẻ tấn công dịch ngược khóa (Keystream)?
A. Open System Authentication
B. Shared Key Authentication (WEP)
C. EAP-TLS
D. PEAP
*Đáp án: B*
*Giải thích: Trong Shared Key Authentication của WEP, AP gửi một chuỗi rõ ngẫu nhiên, Client mã hóa bằng WEP key rồi gửi lại. Hacker bắt được cả bản rõ và bản mã, từ đó dễ dàng tính ra Keystream (dòng khóa) do tính chất của thuật toán XOR.*

**Câu 209:** Giao thức mạng ảo riêng (VPN) nào thường được triển khai tích hợp trên các thiết bị di động (như smartphone) để bảo vệ dữ liệu khi kết nối vào các điểm Wi-Fi công cộng không an toàn?
A. WEP
B. IPSec / IKEv2
C. HTTP
D. FTP
*Đáp án: B*
*Giải thích: IKEv2/IPSec đặc biệt phù hợp cho thiết bị di động (giao thức MOBIKE) vì nó có khả năng duy trì đường hầm VPN ngay cả khi thiết bị chuyển đổi kết nối liên tục (ví dụ từ Wi-Fi sang 4G).*

**Câu 210:** Đặc điểm cốt lõi nào của chuẩn Wi-Fi 802.11ad (WiGig) khiến nó khác biệt hoàn toàn với 802.11n/ac?
A. Hoạt động trên băng tần sóng milimet 60 GHz thay vì 2.4/5 GHz
B. Chỉ sử dụng cáp đồng trục
C. Tầm phủ sóng xa hơn 10km
D. Tốc độ tối đa chỉ đạt 11 Mbps
*Đáp án: A*
*Giải thích: 802.11ad sử dụng băng tần 60GHz. Sóng 60GHz cung cấp băng thông khổng lồ (lên tới 7Gbps) nhưng không thể xuyên tường và bị suy hao mạnh bởi khí oxy trong không khí, nên chỉ dùng cho truyền dữ liệu tốc độ cực cao trong cùng một căn phòng (như truyền video 4K không dây).*

**Câu 211:** Thuật ngữ "Hidden Node" (Nút ẩn) trong mạng không dây dùng để chỉ tình huống nào?
A. Một nút mạng bị hỏng ăng-ten không thể phát sóng
B. Nút mạng ẩn danh (ẩn địa chỉ MAC)
C. Hai máy trạm (Client) có thể giao tiếp với cùng một Access Point nhưng nằm ngoài tầm phủ sóng (hoặc bị vật cản) của nhau, dẫn đến chúng không nghe thấy nhau và có thể phát dữ liệu cùng lúc, gây đụng độ tại AP
D. Access Point thiết lập SSID bị ẩn (Hidden SSID)
*Đáp án: C*
*Giải thích: Trạm A và C đều "nhìn thấy" AP B ở giữa, nhưng A và C không "nhìn thấy" nhau. A đang phát cho B, C muốn phát cũng lắng nghe kênh, thấy trống (vì không nghe được A), C phát theo. Tại B, hai tín hiệu chồng lên nhau gây hỏng gói tin.*

**Câu 212:** Khi triển khai nhiều Access Point (AP) trong cùng một khu vực (như tầng văn phòng), nguyên tắc cấp phát kênh (Channel Allocation) cơ bản nhất đối với băng tần 2.4GHz để tránh nhiễu đồng kênh và nhiễu kênh lân cận là gì?
A. Gán cùng một kênh cho tất cả các AP để tăng tốc độ
B. Đặt các AP gần nhau sử dụng các kênh không chồng lấn (ví dụ: 1, 6, 11)
C. Đặt tất cả AP ở kênh 14
D. Chỉ sử dụng kênh 1
*Đáp án: B*
*Giải thích: Băng tần 2.4GHz có băng thông hẹp, các kênh (ví dụ kênh 1 và 2) bị chồng mép lên nhau (overlapping). Chỉ có các nhóm kênh như {1, 6, 11} là tách biệt hoàn toàn về tần số, không gây nhiễu cho nhau.*

**Câu 213:** Trong chuẩn bảo mật WPA2-Enterprise, ba thành phần chính tham gia vào quá trình xác thực (theo mô hình 802.1X) là những thành phần nào?
A. Supplicant (Client), Authenticator (AP/Switch), và Authentication Server (RADIUS)
B. Router, Firewall, và Switch
C. Master, Slave, và Piconet
D. Home Agent, Foreign Agent, và Mobile Node
*Đáp án: A*
*Giải thích: IEEE 802.1X phân định rõ 3 vai trò: Máy khách muốn kết nối (Supplicant), thiết bị kiểm soát truy cập như AP (Authenticator), và máy chủ chứa cơ sở dữ liệu xác thực (Authentication Server, thường là RADIUS).*

**Câu 214:** Công nghệ nào trong mạng cảm biến không dây cho phép các cảm biến (nodes) thu thập năng lượng trực tiếp từ môi trường xung quanh (như ánh sáng mặt trời, rung động cơ học, sóng vô tuyến nền) để tự cấp nguồn, loại bỏ nhu cầu thay pin?
A. Power over Ethernet (PoE)
B. Energy Harvesting (Thu hoạch năng lượng)
C. Wireless Power Transfer
D. Battery Management System
*Đáp án: B*
*Giải thích: Energy Harvesting (hay Energy Scavenging) là mảng nghiên cứu rất quan trọng cho IoT/WSN, giúp các cảm biến đặt ở những nơi khó tiếp cận có thể tự duy trì hoạt động vĩnh viễn nhờ năng lượng từ môi trường.*

**Câu 215:** Một hệ thống RFID hoạt động ở dải tần số thấp (LF - Low Frequency, 125-134 kHz) thường có nhược điểm gì khi so sánh với dải UHF (Ultra High Frequency)?
A. Khoảng cách đọc rất ngắn (vài cm) và tốc độ truyền dữ liệu rất chậm
B. Bị nhiễu mạnh bởi nước và cơ thể người
C. Tiêu thụ năng lượng quá lớn
D. Gây nhiễu sóng Wi-Fi 2.4GHz
*Đáp án: A*
*Giải thích: Thẻ LF hoạt động dựa trên cảm ứng từ trường gần (near-field magnetic coupling). Do tần số thấp, tốc độ dữ liệu chậm và chỉ đọc được khi đặt sát đầu đọc (như thẻ giữ xe, thẻ từ mở cửa).*

**Câu 216:** Kỹ thuật "Rate Adaptation" (Thích ứng tốc độ) trong thiết bị Wi-Fi hoạt động dựa trên nguyên lý nào?
A. Luôn ép thiết bị phát ở tốc độ cao nhất (ví dụ 54 Mbps) dù tín hiệu yếu
B. Tự động giảm tốc độ truyền (chuyển sang kiểu điều chế cơ bản hơn, ví dụ từ 64-QAM xuống QPSK hoặc BPSK) khi cường độ tín hiệu (SNR) giảm hoặc tỷ lệ lỗi khung (PER) tăng lên, để đảm bảo tính ổn định của kết nối
C. Tăng công suất phát RF lên mức tối đa khi mạng bị nghẽn
D. Tự động chuyển qua dùng 4G khi Wi-Fi chậm
*Đáp án: B*
*Giải thích: Khi thiết bị di chuyển xa khỏi AP, SNR giảm. Nếu vẫn giữ tốc độ cao (điều chế phức tạp), dữ liệu sẽ hỏng hết. Thích ứng tốc độ sẽ hạ số bit truyền trên mỗi symbol (dùng điều chế đơn giản nhưng bền bỉ hơn) để giữ được kết nối, dù tốc độ tải xuống sẽ chậm đi.*

**Câu 217:** Giao thức EAP-TLS (Extensible Authentication Protocol - Transport Layer Security) cung cấp mức độ bảo mật cao nhất cho Wi-Fi doanh nghiệp nhờ cơ chế nào?
A. Sử dụng mật khẩu 128 ký tự
B. Sử dụng khóa WEP kết hợp với mã hóa phần cứng
C. Yêu cầu xác thực hai chiều (Mutual Authentication) bằng Chứng chỉ số (Digital Certificates) được cài đặt trên cả Máy chủ RADIUS và Máy khách (Client)
D. Xác thực bằng địa chỉ MAC
*Đáp án: C*
*Giải thích: EAP-TLS là chuẩn vàng về bảo mật không dây. Việc yêu cầu client cũng phải có chứng chỉ số do PKI cấp khiến hacker không thể thực hiện tấn công Brute-force mật khẩu hay giả mạo client hợp pháp.*

**Câu 218:** PEAP (Protected EAP) là một biến thể của EAP phổ biến trong doanh nghiệp. Tại sao nó được ưa chuộng hơn EAP-TLS?
A. Vì nó không có mã hóa, kết nối nhanh hơn
B. Vì PEAP chỉ yêu cầu Chứng chỉ số trên Máy chủ (Server Certificate) để thiết lập một đường hầm TLS bảo mật. Sau đó, Client chỉ cần nhập Username/Password truyền qua đường hầm đó, không cần cài đặt chứng chỉ phức tạp cho từng thiết bị cá nhân (BYOD)
C. Vì nó sử dụng chung cơ sở dữ liệu với WEP
D. Vì PEAP do mã nguồn mở phát triển
*Đáp án: B*
*Giải thích: Việc quản lý chứng chỉ (Certificate) cho hàng ngàn điện thoại/laptop của nhân viên là cơn ác mộng IT. PEAP (hoặc EAP-TTLS) tạo một hầm mã hóa trước, sau đó xác thực bằng MSCHAPv2 bên trong hầm, kết hợp tính bảo mật cao và sự tiện lợi.*

**Câu 219:** Vấn đề suy hao tín hiệu do "Vùng Fresnel" (Fresnel Zone) trong thiết lập liên kết không dây điểm-điểm (Point-to-Point) ngoài trời là gì?
A. Sóng không dây không thể đi qua không gian hẹp
B. Ngay cả khi hai ăng-ten có tầm nhìn thẳng (Line of Sight - LoS), nếu có vật cản (cây cối, mái nhà) lọt vào không gian hình elip (Vùng Fresnel) xung quanh đường thẳng đó, sóng vô tuyến sẽ bị nhiễu do hiện tượng nhiễu xạ và phản xạ
C. Từ trường trái đất bẻ cong tín hiệu vô tuyến
D. Nhiệt độ cao làm giảm tốc độ sóng
*Đáp án: B*
*Giải thích: Sóng vô tuyến không đi theo một đường thẳng mỏng như tia laser mà lan truyền trong một vùng không gian hình bầu dục. Để liên kết vi ba đạt hiệu suất tối đa, ít nhất 60% vùng Fresnel (đặc biệt là vùng số 1) phải quang đãng hoàn toàn.*

**Câu 220:** Trong 802.11, trường hợp nào một thiết bị Client sẽ gửi khung "Probe Request" chứa tên SSID trống (Null SSID / Broadcast SSID)?
A. Khi muốn ngắt kết nối khỏi AP hiện tại
B. Khi muốn biết có những AP nào đang phát SSID ẩn (Hidden Network) gần đó
C. Khi thực hiện Quét chủ động (Active Scanning) để yêu cầu TẤT CẢ các Access Point trong phạm vi nghe được phải phản hồi bằng Probe Response chứa thông tin mạng của chúng
D. Khi nó đang bị tấn công Deauth
*Đáp án: C*
*Giải thích: Gửi Null SSID là cách thiết bị (như điện thoại) "hỏi thăm" toàn bộ môi trường xung quanh xem có những mạng Wi-Fi nào đang hiện hữu để hiển thị lên danh sách Wi-Fi cho người dùng chọn.*

**Câu 221:** Tính năng "Band Steering" (Điều hướng băng tần) trên các router Wi-Fi hiện đại (Dual-band/Tri-band AP) có tác dụng gì?
A. Chuyển đổi giữa Wi-Fi và 4G
B. Khuyến khích hoặc ép buộc các thiết bị Client có hỗ trợ 5GHz/6GHz kết nối vào các băng tần cao này (rộng rãi và ít nhiễu hơn), giải phóng băng tần 2.4GHz chật chội cho các thiết bị đời cũ (chỉ có 2.4GHz)
C. Giảm công suất phát của băng tần 5GHz
D. Gộp băng thông của cả 2.4GHz và 5GHz cho một thiết bị
*Đáp án: B*
*Giải thích: Khi một thiết bị gửi Probe Request trên cả băng tần 2.4GHz và 5GHz, AP dùng tính năng Band Steering sẽ chủ động phớt lờ yêu cầu ở 2.4GHz hoặc phản hồi chậm, ép thiết bị kết nối vào SSID ở dải 5GHz tốt hơn.*

**Câu 222:** Kỹ thuật "Spatial Multiplexing" (Ghép kênh không gian) trong MIMO yêu cầu điều kiện môi trường vô tuyến nào để hoạt động hiệu quả nhất?
A. Môi trường chân không hoàn toàn không có vật cản
B. Môi trường có hiện tượng "Đa đường" (Multipath) mạnh mẽ (nhiều vật cản, phản xạ), giúp tạo ra các kênh truyền không gian độc lập cho mỗi luồng dữ liệu
C. Hai ăng-ten phải cách nhau ít nhất 1 kilomet
D. Môi trường chỉ có Line-of-Sight (tầm nhìn thẳng) tuyệt đối
*Đáp án: B*
*Giải thích: Khác với các hệ thống vi ba cũ coi Multipath là kẻ thù, MIMO tận dụng Multipath. Các tia phản xạ khác nhau tạo ra "chữ ký không gian" (spatial signatures) khác biệt, giúp máy thu với nhiều ăng-ten (nhờ thuật toán ma trận) tách biệt được nhiều luồng dữ liệu phát đi cùng lúc trên cùng tần số.*

**Câu 223:** Thuật ngữ "WPS" (Wi-Fi Protected Setup) gây ra rủi ro an ninh mạng nghiêm trọng nào?
A. WPS không mã hóa dữ liệu truyền tải
B. WPS sử dụng mã PIN 8 chữ số dễ bị tấn công Brute-force (chạy thử mật khẩu) bằng công cụ như Reaver trong vòng vài giờ, từ đó hacker lấy được mật khẩu WPA/WPA2 thực sự
C. WPS làm hỏng firmware của router
D. WPS yêu cầu quyền root của điện thoại
*Đáp án: B*
*Giải thích: Do lỗi thiết kế trong việc xác thực mã PIN (chia PIN làm 2 nửa để kiểm tra), số lượng tổ hợp cần thử giảm từ 100 triệu xuống chỉ còn 11,000. Đây là lỗ hổng nghiêm trọng, do đó các chuyên gia bảo mật luôn khuyên tắt tính năng WPS PIN trên Router.*

**Câu 224:** Kiến trúc mạng 5G Core (5GC) chuyển đổi hoàn toàn sang mô hình điện toán đám mây (Cloud-Native), được gọi là SBA. SBA viết tắt của từ gì?
A. Sub-Band Architecture
B. Software-Based Access
C. Service-Based Architecture (Kiến trúc dựa trên dịch vụ)
D. System Base Area
*Đáp án: C*
*Giải thích: Trong SBA của 5G, các nút mạng truyền thống (như MME, SGW) được phá vỡ thành các "Hàm mạng" (Network Functions - NFs) siêu nhỏ (microservices) giao tiếp với nhau qua API chuẩn (như HTTP/REST), rất dễ ảo hóa, mở rộng và tự động hóa.*

**Câu 225:** Trong công nghệ truyền thông vệ tinh (Satellite Communications), các vệ tinh LEO (Low Earth Orbit - Quỹ đạo Trái Đất tầm thấp, ví dụ Starlink) có ưu điểm vượt trội gì so với vệ tinh GEO (Geostationary Earth Orbit - Quỹ đạo địa tĩnh)?
A. Đứng yên tại một vị trí so với mặt đất
B. Chỉ cần 3 vệ tinh là phủ sóng toàn cầu
C. Độ trễ (Latency) thấp hơn rất nhiều (chỉ vài chục ms so với >500ms của GEO) do ở khoảng cách gần Trái đất hơn (từ 500-2000 km)
D. Có kích thước lớn bằng một trạm không gian
*Đáp án: C*
*Giải thích: Vệ tinh GEO cách Trái đất ~36.000 km, thời gian truyền sóng đi và về rất lớn (round-trip time cao). LEO gần hơn rất nhiều, giúp cung cấp kết nối Internet vệ tinh có độ trễ tương đương cáp quang, phù hợp cho chơi game online hoặc gọi video.*

**Câu 226:** Để kết nối với mạng vệ tinh LEO (ví dụ Starlink), thiết bị nhận (chảo thu) ở mặt đất sử dụng công nghệ ăng-ten nào để liên tục "theo dõi" và kết nối với các vệ tinh di chuyển cực nhanh trên bầu trời mà không cần mô tơ xoay cơ học?
A. Dipole Antenna (Ăng ten lưỡng cực)
B. Phased Array Antenna (Ăng ten mảng pha)
C. Parabolic Dish Antenna truyền thống
D. Yagi-Uda Antenna
*Đáp án: B*
*Giải thích: Ăng-ten mảng pha (Phased Array) là một tấm phẳng chứa hàng ngàn ăng-ten con. Bằng cách thay đổi pha điện tử vi mô trên từng ăng-ten con, nó tạo ra beamforming có thể quét (steer) theo vị trí vệ tinh trong chớp mắt mà không có bộ phận chuyển động cơ học nào.*

**Câu 227:** Khái niệm "Near Field Communication" (NFC) hoạt động hiệu quả nhất ở khoảng cách nào?
A. Dưới 4 centimet (cm)
B. Lên đến 10 mét
C. Lên đến 100 mét
D. Lên đến 1 kilomet
*Đáp án: A*
*Giải thích: NFC (giao thức dựa trên RFID tần số cao 13.56 MHz) yêu cầu các thiết bị phải được đặt rất sát nhau (thường là chạm vào nhau hoặc cách vài centimet). Điều này bản thân nó cung cấp một lớp bảo mật vật lý chống nghe trộm từ xa (rất thích hợp cho thanh toán Apple Pay, Google Pay).*

**Câu 228:** Trong WPA3, giao thức nào thay thế hoàn toàn tiêu chuẩn bảo mật 802.11 Mở (Open Wi-Fi) ở các quán cà phê, sân bay, cung cấp mã hóa từng cá nhân mà không cần nhập mật khẩu chung?
A. OWE (Opportunistic Wireless Encryption)
B. WPA3-Enterprise
C. EAP-SIM
D. Captive Portal
*Đáp án: A*
*Giải thích: OWE (thường được gọi là WPA3-Enhanced Open) sử dụng trao đổi khóa Diffie-Hellman không xác thực. Nó tạo ra kết nối được mã hóa riêng biệt cho mỗi thiết bị khi kết nối Wi-Fi công cộng (tránh bị phần mềm bắt gói tin nghe lén), mà người dùng vẫn trải nghiệm kết nối "không cần mật khẩu" như mạng Open cũ.*

**Câu 229:** Thành phần nào của khung MAC 802.11 chịu trách nhiệm kiểm tra tính toàn vẹn của dữ liệu (phát hiện lỗi bit) ở phần đuôi gói tin?
A. MAC Header
B. Payload
C. FCS (Frame Check Sequence)
D. BSSID
*Đáp án: C*
*Giải thích: FCS sử dụng thuật toán mã vòng CRC (Cyclic Redundancy Check) dài 32-bit. Máy nhận sẽ tính lại CRC dựa trên dữ liệu thu được, nếu không khớp với FCS kèm theo, nó sẽ vứt bỏ gói tin và không gửi ACK.*

**Câu 230:** Một "Mesh AP" trong hệ thống Wireless Mesh Network khác với "Root AP" (Gateway AP) ở điểm nào?
A. Mesh AP không có ăng-ten
B. Mesh AP không có kết nối cáp (Wired Uplink) trực tiếp với mạng LAN/Internet; nó phải chuyển tiếp vô tuyến gói tin qua các Mesh AP khác để đến được Root AP
C. Mesh AP không hỗ trợ chuẩn 802.11ac
D. Mesh AP tiêu thụ ít điện hơn ZED
*Đáp án: B*
*Giải thích: Root AP (hoặc Portal) là điểm giao cắt giữa mạng không dây Lưới và hệ thống cáp quang/đồng. Mesh AP đóng vai trò như các trạm lặp (repeater) thông minh, giúp mở rộng vùng phủ sóng mà không cần kéo cáp.*

**Câu 231:** Hiện tượng tín hiệu điện từ bị suy giảm công suất (mất năng lượng) khi đi xuyên qua các vật liệu vật lý (tường gạch, kính, gỗ, lá cây) được gọi là gì?
A. Reflection (Phản xạ)
B. Refraction (Khúc xạ)
C. Attenuation (Suy hao/Hấp thụ)
D. Diffraction (Nhiễu xạ)
*Đáp án: C*
*Giải thích: Hấp thụ (Absorption) hay Suy hao (Attenuation) là quá trình năng lượng sóng vô tuyến bị vật liệu chuyển hóa một phần thành nhiệt năng, làm tín hiệu yếu đi khi xuyên qua.*

**Câu 232:** Giao thức định tuyến DSR (Dynamic Source Routing) dùng trong mạng Ad-hoc có điểm khác biệt cốt lõi nào so với AODV?
A. Định tuyến tập trung
B. Gói tin dữ liệu mang theo toàn bộ danh sách đường đi (Source Route - địa chỉ của từng nút trung gian) trong phần Header, do đó các nút trung gian không cần phải duy trì bảng định tuyến chi tiết
C. Sử dụng định tuyến trạng thái liên kết (Link-State)
D. Tương thích chuẩn BGP
*Đáp án: B*
*Giải thích: Trong DSR, máy gửi chỉ định chính xác đường dẫn (danh sách các IP hop-by-hop) và nhúng nó vào mào đầu (header) gói tin IP. Nút trung gian chỉ việc đọc và chuyển tiếp theo danh sách đó.*

**Câu 233:** Trong kiến trúc Wi-Fi Mesh, "Backhaul" đề cập đến khái niệm nào?
A. Đường truyền dữ liệu người dùng qua Bluetooth
B. Liên kết mạng nội bộ giữa các Access Point Mesh với nhau (và với Router chính) để vận chuyển lưu lượng hệ thống, thường được tách riêng ra một băng tần (ví dụ 5GHz thứ hai) để không ảnh hưởng tốc độ của Client
C. Quá trình sao lưu dữ liệu cấu hình
D. Quá trình Client gửi gói tin ngược về AP
*Đáp án: B*
*Giải thích: Các hệ thống Mesh cao cấp (Tri-band) thường dành riêng một băng tần vô tuyến 5GHz chỉ để làm "đường cao tốc" (Backhaul) chuyên chở dữ liệu giữa các node, đảm bảo thiết bị Client luôn có tốc độ kết nối tối đa ở các băng tần còn lại.*

**Câu 234:** Công nghệ nào cho phép một thiết bị di động kết hợp đồng thời kết nối Wi-Fi và mạng di động (LTE/5G) để tải xuống một tệp tin lớn nhanh hơn hoặc tạo sự dự phòng liền mạch?
A. MPTCP (Multipath TCP)
B. ARP
C. ICMP
D. CSMA/CA
*Đáp án: A*
*Giải thích: MPTCP là một phần mở rộng của giao thức TCP, cho phép một kết nối TCP được chia thành nhiều luồng phụ (subflows) truyền song song qua nhiều giao diện mạng khác nhau (như Wi-Fi và Cellular) trên cùng một thiết bị di động.*

**Câu 235:** Tại sao dải tần 2.4 GHz lại được gọi là dải tần ISM?
A. Viết tắt của Internet Service Mobility
B. Là dải tần số vô tuyến được quốc tế phân bổ riêng cho các mục đích Công nghiệp, Khoa học và Y tế (Industrial, Scientific, and Medical) không cần xin giấy phép (unlicensed), do đó được Wi-Fi và Bluetooth sử dụng tự do
C. Do tập đoàn ISM phát minh
D. Là băng tần chỉ dành cho chính phủ
*Đáp án: B*
*Giải thích: Các băng tần ISM không yêu cầu người dùng trả phí bản quyền (phổ tần), nhưng bù lại, họ phải chấp nhận việc các thiết bị (như lò vi sóng, bộ định tuyến Wi-Fi, camera không dây) có thể gây nhiễu lẫn nhau.*

**Câu 236:** Kỹ thuật nào giúp các nhà mạng cung cấp dịch vụ Internet vạn vật (IoT) diện rộng, với ưu điểm pin dùng 10 năm, xuyên tường sâu (đặt dưới tầng hầm), sử dụng ngay trên phổ tần 4G LTE hiện hữu?
A. Wi-Fi 6E
B. NB-IoT (Narrowband IoT)
C. Wimax
D. Li-Fi
*Đáp án: B*
*Giải thích: NB-IoT là một tiêu chuẩn mạng di động diện rộng tiết kiệm điện (LPWAN) của 3GPP. Nó chỉ sử dụng một dải tần số rất hẹp (180 kHz), hy sinh tốc độ (rất chậm) để đạt được khả năng đâm xuyên cực tốt và tối ưu năng lượng tối đa cho các công tơ điện/nước thông minh.*

**Câu 237:** Sự phân biệt về mặt chức năng giữa Control Plane (Mặt phẳng điều khiển) và User/Data Plane (Mặt phẳng dữ liệu) được thực hiện triệt để trong cấu trúc 5G Core. Khái niệm này gọi là gì?
A. CUPS (Control and User Plane Separation)
B. NAT (Network Address Translation)
C. VPN
D. CSMA
*Đáp án: A*
*Giải thích: CUPS cho phép nhà mạng đặt các nút xử lý dữ liệu tải nặng (User Plane) ở gần người dùng (Edge Computing - giảm độ trễ) trong khi vẫn duy trì cụm máy chủ Điều khiển (Control Plane) nằm tập trung trên Cloud để dễ quản lý.*

**Câu 238:** Chuẩn không dây nào (còn được gọi là Wi-Fi Halow) được tối ưu hóa hoạt động ở dải tần số dưới 1 GHz (Sub-1 GHz) nhằm đánh đổi tốc độ lấy tầm phủ sóng rộng lớn (lên tới 1km) và đâm xuyên vật cản tốt cho ứng dụng IoT?
A. 802.11ac
B. 802.11ah
C. 802.11ad
D. 802.15.1
*Đáp án: B*
*Giải thích: IEEE 802.11ah hoạt động ở băng tần ~900 MHz. Do tần số thấp, sóng lan truyền xa hơn rất nhiều so với 2.4/5 GHz của Wi-Fi truyền thống, cạnh tranh trực tiếp với Zigbee và LoRa trong lĩnh vực nhà thông minh và nông nghiệp.*

**Câu 239:** Trong ngữ cảnh bảo mật Wi-Fi, "PMK" (Pairwise Master Key) được tạo ra từ đâu trong mạng gia đình (WPA2-Personal)?
A. Do máy chủ RADIUS sinh ra ngẫu nhiên
B. Được dẫn xuất trực tiếp từ Mật khẩu Wi-Fi (Pre-Shared Key - PSK) mà người dùng nhập vào cùng với tên mạng (SSID) thông qua hàm băm nhiều vòng (PBKDF2)
C. Nhúng cứng trong phần cứng của nhà sản xuất
D. Tải từ máy chủ DNS
*Đáp án: B*
*Giải thích: PMK là chìa khóa bí mật cấp cao nhất trong phiên kết nối. Đối với mạng dùng mật khẩu (WPA-PSK), PMK được băm từ mật khẩu văn bản và SSID (được dùng như một "salt" để chống lập bảng băm Rainbow Tables).*

**Câu 240:** LoRaWAN (Long Range Wide Area Network) thuộc nhóm công nghệ mạng nào?
A. LPWAN (Low Power Wide Area Network)
B. WPAN (Wireless Personal Area Network)
C. WLAN (Wireless Local Area Network)
D. HSPA+
*Đáp án: A*
*Giải thích: LoRaWAN là chuẩn LPWAN nổi tiếng (không dùng tần số của nhà mạng di động). Nó dùng kỹ thuật trải phổ Chirp Spread Spectrum, cho phép gửi gói tin dữ liệu cực nhỏ đi xa hàng chục kilomet với cục pin cúc áo duy trì nhiều năm.*

**Câu 241:** Kỹ thuật điều chế nào sau đây sử dụng ánh sáng nhìn thấy (Visible Light) thay vì sóng vô tuyến (RF) để truyền dữ liệu không dây tốc độ cao?
A. Bluetooth Low Energy
B. Zigbee
C. Li-Fi (Light Fidelity)
D. Wi-Fi 7
*Đáp án: C*
*Giải thích: Li-Fi sử dụng các bóng đèn LED nhấp nháy ở tần số cực cao (mắt người không thấy được) để truyền dữ liệu. Ưu điểm là băng thông cực lớn và hoàn toàn miễn nhiễm với nhiễu sóng RF, cũng như bảo mật vật lý tốt (ánh sáng không xuyên tường).*

**Câu 242:** "Kênh điều khiển quảng bá" (BCH - Broadcast Control Channel) trong mạng di động thực hiện nhiệm vụ gì?
A. Phân bổ IP cho người dùng
B. Liên tục phát (broadcast) các thông tin hệ thống (System Information) của trạm gốc (như nhận dạng mạng PLMN ID, thông số kênh) để các thiết bị trong vùng phủ sóng có thể dò tìm và đồng bộ với mạng
C. Thiết lập cuộc gọi video
D. Nhắn tin SMS
*Đáp án: B*
*Giải thích: Giống như Beacon trong Wi-Fi, BCH là kênh một chiều (từ trạm gốc tới các thiết bị) truyền tải thông tin định danh và đặc tính cấu hình bắt buộc để một chiếc điện thoại mới bật máy có thể nhận diện và tham gia vào mạng.*

**Câu 243:** Tại sao khi tăng công suất phát (Tx Power) của Access Point Wi-Fi lên mức tối đa thường không làm tăng chất lượng kết nối của các thiết bị di động (như smartphone) ở xa?
A. Vì smartphone không hỗ trợ tín hiệu mạnh
B. Vì kết nối Wi-Fi là kết nối hai chiều (bán song công). Smartphone có thể "nghe" thấy AP (do AP phát mạnh), nhưng AP không thể "nghe" thấy Smartphone (do ăng-ten/pin của điện thoại nhỏ và phát tín hiệu yếu), dẫn đến giao tiếp một chiều thất bại (Asymmetric Power)
C. Vì công suất mạnh làm quá tải mạng lưới cáp quang
D. Vì bị can thiệp bởi vệ tinh
*Đáp án: B*
*Giải thích: Đây là lỗi phổ biến khi thiết lập mạng. Phủ sóng Wi-Fi phụ thuộc vào khả năng phát của thiết bị yếu nhất trong chuỗi liên kết. Nếu điện thoại phát sóng không về tới AP, gói ACK sẽ không tới và kết nối sẽ bị đứt.*

**Câu 244:** Băng tần 6 GHz được cấp phép cho chuẩn Wi-Fi nào mới nhất, mở ra một lượng kênh không chồng lấn khổng lồ (lên tới 1200 MHz phổ tần bổ sung)?
A. Wi-Fi 4 (802.11n)
B. Wi-Fi 5 (802.11ac)
C. Wi-Fi 6E (802.11ax extended) và Wi-Fi 7 (802.11be)
D. Wi-Fi 1 (802.11b)
*Đáp án: C*
*Giải thích: Việc mở rộng băng tần (Extended - chữ E trong Wi-Fi 6E) cho phép sử dụng dải tần 6GHz hoàn toàn mới, loại bỏ hoàn toàn nhiễu từ các thiết bị chuẩn cũ (legacy devices), cho phép sử dụng các kênh siêu rộng (160MHz hoặc 320MHz trong Wi-Fi 7).*

**Câu 245:** "Multi-Link Operation" (MLO) là tính năng cách mạng của Wi-Fi 7 (802.11be). Chức năng của nó là gì?
A. Kết nối nhiều máy tính qua cáp đồng
B. Cho phép thiết bị (AP và Client) sử dụng đồng thời (gửi và nhận dữ liệu cùng lúc) trên nhiều băng tần khác nhau (ví dụ vừa dùng 5GHz vừa dùng 6GHz) để gộp băng thông và giảm độ trễ tuyệt đối
C. Phát chung một SSID cho nhiều mạng
D. Mã hóa lưu lượng bằng thuật toán lượng tử
*Đáp án: B*
*Giải thích: Khác với Wi-Fi trước đây chỉ kết nối vào một băng tần tại một thời điểm, MLO cho phép thiết bị "gộp" các liên kết vật lý (link aggregation không dây). Nếu một băng tần bị nghẽn (nhiễu ngắn hạn), dữ liệu lập tức chạy qua băng tần kia (độ trễ siêu thấp).*

**Câu 246:** Kỹ thuật điều chế 4096-QAM (4K-QAM) được giới thiệu trong chuẩn Wi-Fi 7 nhằm mục đích gì?
A. Tăng khả năng xuyên tường
B. Đóng gói tới 12 bit dữ liệu vào mỗi một biểu tượng (symbol) tín hiệu, tăng 20% tốc độ truyền tải lý thuyết so với 1024-QAM của Wi-Fi 6 ở cùng điều kiện lý tưởng (SNR cực tốt)
C. Đơn giản hóa phần cứng phát sóng
D. Chống lại tấn công DoS
*Đáp án: B*
*Giải thích: Điều chế biên độ cầu phương QAM càng cao, càng nhồi nhét được nhiều bit vào một sóng mang. Tuy nhiên, 4096-QAM yêu cầu tín hiệu cực kỳ sạch và khoảng cách rất gần giữa AP và Client để có thể phân biệt chính xác 4096 trạng thái pha/biên độ khác nhau.*

**Câu 247:** Mã hóa luồng RC4 (Rivest Cipher 4) là trung tâm của sự cố bảo mật trong giao thức nào?
A. WPA3
B. IPSec
C. WEP và WPA (TKIP) ban đầu
D. SSLv3
*Đáp án: C*
*Giải thích: Do phát hiện nhiều lỗ hổng trong quá trình sinh khóa của RC4, nó đã bị loại bỏ khỏi các tiêu chuẩn bảo mật hiện đại. WEP sụp đổ vì RC4 kết hợp IV yếu. TKIP (WPA) mặc dù có vá lỗi IV nhưng lõi vẫn là RC4 nên vẫn bị coi là không an toàn.*

**Câu 248:** Hiện tượng một thiết bị vô tuyến liên tục chuyển đổi (flip-flop) qua lại giữa việc kết nối với hai trạm phát sóng (Access Point / NodeB) có cường độ tín hiệu xấp xỉ nhau, gây lãng phí tài nguyên mạng và rớt gói tin được gọi là gì?
A. Ping-pong Effect (Hiệu ứng bóng bàn)
B. Roaming
C. Hand-off
D. Paging
*Đáp án: A*
*Giải thích: Hiệu ứng Ping-pong xảy ra do sự biến động nhanh của sóng vô tuyến (fading) tại vùng biên giữa hai Cell. Để giải quyết, người ta sử dụng một biên độ trễ (Hysteresis margin) hoặc Timer – tức là tín hiệu trạm mới phải mạnh hơn trạm cũ một khoảng decibel nhất định trong một khoảng thời gian nhất định thì mới thực hiện chuyển giao.*

**Câu 249:** Tiêu chuẩn nào quy định cách thức cấp nguồn điện DC cho các Access Point Wi-Fi trực tiếp thông qua sợi cáp mạng Ethernet (cáp xoắn đôi) thay vì phải cắm bộ đổi nguồn (Adapter) riêng lẻ tại trần nhà?
A. 802.1Q (VLAN)
B. 802.3af / 802.3at / 802.3bt (Power over Ethernet - PoE)
C. 802.1X (Xác thực)
D. 802.11i (Bảo mật)
*Đáp án: B*
*Giải thích: Các Switch hỗ trợ PoE (như 802.3at PoE+) có thể cung cấp đủ công suất (lên đến 30W hoặc cao hơn) trên cùng sợi cáp CAT5e/CAT6 đang truyền dữ liệu, giúp việc triển khai lắp đặt hàng trăm AP trên trần nhà văn phòng dễ dàng và thẩm mỹ hơn rất nhiều.*

**Câu 250:** Cuối cùng, mục đích tối thượng của mọi công nghệ kết nối Mạng di động và Không dây (từ 1G đến 6G, từ Wi-Fi 1 đến Wi-Fi 7) là để đạt được điều gì trong kỷ nguyên số?
A. Thay thế hoàn toàn cáp quang biển
B. Hiện thực hóa khái niệm Ubiquitous Computing (Điện toán Điện tại / Mọi lúc mọi nơi), nơi con người, vạn vật (IoT), phương tiện giao thông được kết nối liên tục, liền mạch với băng thông cực cao và độ trễ bằng không
C. Phát minh ra các thuật toán AI
D. Chế tạo thiết bị điện tử rẻ tiền hơn
*Đáp án: B*
*Giải thích: Triết lý "Ubiquitous connectivity" (Luôn luôn kết nối ở bất cứ đâu, bất cứ lúc nào, với bất kỳ thiết bị nào) là kim chỉ nam cho sự phát triển của các thế hệ mạng vô tuyến, nhằm xóa bỏ mọi giới hạn vật lý về dây cáp và vị trí địa lý.*
