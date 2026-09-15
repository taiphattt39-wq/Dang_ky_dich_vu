from flask import Flask, render_template, request, jsonify
import io, sys, traceback
from vn_translator import dich_ma

app = Flask(__name__)

def chay_an_toan(ma_nguon):
    try:
        ma_python = dich_ma(ma_nguon)
        dau_ra = io.StringIO()
        sys.stdout = dau_ra
        moi_truong = {"__name__": "__main__"}
        exec(ma_python, moi_truong)
        sys.stdout = sys.__stdout__
        return {"thanhcong": True, "ketqua": dau_ra.getvalue(), "loi": ""}
    except Exception as e:
        sys.stdout = sys.__stdout__
        return {
            "thanhcong": False,
            "ketqua": "",
            "loi": f"LỖI: {type(e).__name__}\n{str(e)}"
        }

@app.route("/")
def trang_chinh():
    return render_template("index.html")

@app.route("/api/chay", methods=["POST"])
def xu_ly():
    dl = request.get_json()
    kq = chay_an_toan(dl.get("code", ""))
    return jsonify(kq)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
  
