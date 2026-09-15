def dich_ma(ma):
    tu_doi = {
        # === CẤU TRÚC CỐT LÕI ===
        "biến": "",
        "hàm": "def",
        "lớp": "class",
        "thuộc": ".",
        
        # === ĐIỀU KIỆN ===
        "nếu": "if",
        "thì": ":",
        "còn_nếu": "elif",
        "còn_lại": "else",
        
        # === VÒNG LẶP & ĐIỀU KHIỂN ===
        "lặp_khi": "while",
        "lặp_mỗi": "for",
        "trong": "in",
        "phạm_vi": "range",
        "ngắt": "break",
        "tiếp_tục": "continue",
        "truy_cập_toàn_cục": "global",
        "không_cục_bộ": "nonlocal",
        
        # === GIÁ TRỊ & KIỂU DỮ LIỆU ===
        "Đúng": "True",
        "Sai": "False",
        "Rỗng": "None",
        "số_nguyên": "int",
        "số_thực": "float",
        "chuỗi": "str",
        "danh_sách": "list",
        "bộ_ba": "tuple",
        "từ_điển": "dict",
        "tập_hợp": "set",
        "danh_sách_tạo": "list",
        "từ_điển_tạo": "dict",
        
        # === HÀM CƠ BẢN & VÀO/RA ===
        "in": "print",
        "nhập": "input",
        "trả_về": "return",
        "độ_dài": "len",
        "loại": "type",
        "phạm_vi": "range",
        "sắp_xếp": "sorted",
        "tổng": "sum",
        "lớn_nhất": "max",
        "nhỏ_nhất": "min",
        "làm_tròn": "round",
        "mã_hoá": "repr",
        "biểu_diễn": "str",
        
        # === TOÁN TỬ LOGIC & SO SÁNH ===
        "và": "and",
        "hoặc": "or",
        "không": "not",
        "là": "is",
        "có_trong": "in",
        "bằng": "==",
        "khác": "!=",
        "lớn_hơn": ">",
        "nhỏ_hơn": "<",
        "lớn_hơn_bằng": ">=",
        "nhỏ_hơn_bằng": "<=",
        
        # === LÀM VIỆC VỚI TỆP & HỆ THỐNG ===
        "mở": "open",
        "đọc": "read",
        "viết": "write",
        "đóng": "close",
        "đường_dẫn": "path",
        "tồn_tại": "exists",
        "xóa": "remove",
        "đổi_tên": "rename",
        "danh_sách_thư_mục": "listdir",
        
        # === XỬ LÝ LỖI ===
        "thử": "try",
        "bắt_lỗi": "except",
        "cuối_cùng": "finally",
        "nâng_lỗi": "raise",
        "làm_thí_dụ": "assert",
        
        # === MÔ ĐUN & NHẬP ===
        "nhập": "import",
        "từ": "from",
        "dưới_tên": "as",
        "thông_tin": "dir",
        "trợ_giúp": "help"
    }
    
    ma_python = ma
    for vn, en in tu_doi.items():
        # Chỉ thay từ nguyên hoàn chỉnh, không ảnh hưởng phần trong chuỗi/tên biến
        ma_python = ma_python.replace(vn, en)
    
    return ma_python
  
