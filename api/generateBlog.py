# api/generateBlog.py
import json

def handler(request):
    """
    Vercel Python Serverless Function
    POST /api/generateBlog
    """
    data = request.json() or {}
    kw = data.get("keyword", "")

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "title": f"{kw} を極めるバイオハック入門",
            "outline": "- 導入\n- 問題提起\n- 解決策\n- まとめ"
        })
    }




