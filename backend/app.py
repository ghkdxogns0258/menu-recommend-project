from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/recommend", methods=["GET"])
def recommend():
    # 예제 메뉴 추천 데이터
    data = {"menu": "샐러드", "attributes": ["건강한", "채소"]}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)