from flask import Flask, jsonify, Response
import requests

app = Flask(__name__)

def fetch_market_data():
    url = "https://www.hn-rtj.cn/admin/get_price5.php"
    headers = {
        "Referer": "https://www.hn-rtj.cn/index.php",
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding
    raw = response.text.strip()
    
    print("原始数据：")
    print(raw)

    return raw

@app.route('/api/market-data', methods=['GET'])
def get_market_data():
    try:
        data = fetch_market_data()
        # 直接返回原始数据，并添加 CORS 头
        response = Response(
            response=data,
            status=200,
            mimetype="text/plain"
        )
        response.headers["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        error_response = jsonify({
            "status": "error",
            "message": str(e)
        })
        error_response.headers["Access-Control-Allow-Origin"] = "*"
        return error_response, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=82, debug=True)