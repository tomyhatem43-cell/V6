from http.server import HTTPServer, SimpleHTTPRequestHandler
import json

html_v6 = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><meta charset="UTF-8"><title>V6 Master</title></head>
<body style="background:#000; color:#0f0; font-family:monospace; padding:20px;">
    <h1>نظام V6: مصنع السينما</h1>
    <textarea id="input" style="width:100%; height:100px; background:#111; color:#0f0; border:1px solid #0f0;"></textarea>
    <button onclick="process()" style="background:#0f0; color:#000; padding:10px; width:100%;">توليد الإتقان</button>
    <div id="log" style="margin-top:20px;"></div>
    <script>
        async function process() {
            const val = document.getElementById('input').value;
            const res = await fetch('/api', {method:'POST', body:JSON.stringify({data:val})});
            const data = await res.json();
            document.getElementById('log').innerText = data.response;
        }
    </script>
</body>
</html>
"""

class V6_Engine(SimpleHTTPRequestHandler):
    def do_POST(self):
        content = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(content).decode())
        response = {"response": f"V6: تم إتقان السيناريو: {data['data'][:20]}.. بجودة 8K"}
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode())

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(html_v6.encode('utf-8'))

HTTPServer(('localhost', 3000), V6_Engine).serve_forever()
