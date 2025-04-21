from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/generateBlog', methods=['POST'])
def generate_blog():
    kw = request.json.get('keyword', '')
    return jsonify({
        "title": f"{kw} を極めるバイオハック入門",
        "outline": "- 導入\n- 問題提起\n- 解決策\n- まとめ"
    })

if __name__ == '__main__':
    app.run()

