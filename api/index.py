import json

def handler(request):
    """
    POST /api/index
    Body: {"keyword": "マインドフルネス バイオハック"}
    """
    try:
        data = json.loads(request.body or b"{}")
    except Exception:
        data = {}

    kw = data.get("keyword", "")

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({
            "title": f"{kw} を極めるバイオハック入門",
            "outline": "- 導入\n- 問題提起\n- 解決策\n- まとめ"
        })
    }

