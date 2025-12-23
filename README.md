<div align="center">
  <img src="logo.jpg" alt="Telerisk Logo" width="200" height="200">
</div>

# Telerisk - Telegram Bot

<div align="center">

Telerisk là một Telegram bot open-source được phát triển bằng Python. Bot cung cấp các tính năng tiện ích như kiểm tra thông tin hệ thống và tìm kiếm dữ liệu.

</div>

## Tính Năng

- `/start` - Bắt đầu bot
- `/help` - Hiển thị danh sách lệnh khả dụng
- `/whoami` - Hiển thị username của người dùng
- `/whoareyou` - Lấy thông tin người dùng hệ thống
- `/hostname` - Hiển thị hostname của server
- `/timenow` - Hiển thị thời gian hiện tại
- `/ifconfig` - Thông tin cấu hình mạng
- `/checkleak` - Kiểm tra thông tin trong cơ sở dữ liệu

## Cài Đặt

### Yêu cầu
- Python 3.7+
- pip

### Bước cài đặt

1. Clone repository:
```bash
git clone https://github.com/yourusername/Telerisk.git
cd Telerisk
```

2. Tạo virtual environment (tùy chọn nhưng khuyến nghị):
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# hoặc
venv\Scripts\activate  # Windows
```

3. Cài đặt dependencies:
```bash
pip install -r requirements.txt
```

4. Cấu hình bot token:
```bash
cp .env.example .env
# Sửa file .env và thêm Telegram Bot Token của bạn
```

5. Chạy bot:
```bash
python3 bot.py
```

## Cấu Trúc Dự Án

```
Telerisk/
├── bot.py              # File chính của bot
├── requirements.txt    # Dependencies
├── .env.example        # Template cho environment variables
├── .gitignore          # Git ignore rules
└── README.md          # File này
```

## Lưu Ý Bảo Mật

Đây là dự án mã nguồn mở và được phát hành cho mục đích học tập. Khi triển khai trong môi trường production, vui lòng kiểm tra kỹ mã nguồn và thực hiện các biện pháp bảo mật cần thiết.

## Cộng Tác

Nếu bạn tìm thấy các lỗi thực sự (không phải intentional), vui lòng báo cáo qua Issues.

## Giấy Phép

MIT License - Xem file LICENSE để biết chi tiết

## Tác Giả

Telerisk Contributors

---

**Disclaimer**: Bot này được cung cấp như hiện trạng (as-is) cho mục đích học tập và nghiên cứu. Người dùng chịu trách nhiệm đảm bảo sử dụng phù hợp với các luật lệ hiện hành.
