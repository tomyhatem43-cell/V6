from http.server import HTTPServer, SimpleHTTPRequestHandler
import json

ui_global = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>V6 Neural Interface</title>
    <style>
        body { background: #050505; color: #00ff41; font-family: 'Courier New', monospace; margin: 0; padding: 20px; }
        .grid { display: grid; grid-template-columns: 1fr 2fr; gap: 20px; }
        .panel { border: 1px solid #00ff41; padding: 15px; border-radius: 8px; background: #0a0a0a; box-shadow: 0 0 10px rgba(0,255,65,0.2); }
        textarea { width: 100%; height: 120px; background: #000; color: #fff; border: 1px solid #00ff41; }
        button { background: #00ff41; color: #000; border: none; padding: 12px; width: 100%; font-weight: bold; cursor: pointer; margin-top: 10px; }
        #console { height: 200px; overflow-y: auto; border: 1px solid #333; padding: 10px; margin-top: 10px; background: #000; }
    </style>
</head>
<body>
    <h1>نظام V6: النواة العصبية العالمية</h1>
    <div class="grid">
        <div class="panel">
            <h3>التحكم في الوكلاء</h3>
            <button onclick="task('Render')">بدء الرندر العالمي</button>
            <button onclick="task('Optimize')">تحسين الخوارزمية (8K)</button>
            <button onclick="task('Deploy')">نشر الوكيل المساعد</button>
        </div>
        <div class="panel">
            <h3>وحدة المعالجة المركزية</h3>
            <textarea id="prompt" placeholder="أدخل بيانات التوليد العالمي..."></textarea>
            <button onclick="process()">توليد الإبداع</button>
        </div>
    </div>
    <div class="panel" style="margin-top:20px;">
        <h3>سجل العمليات (Neural Console)</h3>
        <div id="console"></div>
    </div>
    <script>
        const log = (m) => document.getElementById('console').innerHTML += `> ${m}<br>`;
        async function task(t) {
            log("تفعيل المهمة: " + t);
            const res = await fetch('/api', {method:'POST', body:JSON.stringify({type:'task', t})});
            const d = await res.json();
            log("الوكيل: " + d.msg);
        }
        async function process() {
            const p = document.getElementById('prompt').value;
            log("بدء معالجة: " + p.substring(0,20));
            const res = await fetch('/api', {method:'POST', body:JSON.stringify({type:'gen', p})});
            const d = await res.json();
            log("النتيجة: " + d.msg);
        }
    </script>
</body>
</html>
"""
class V6_Neural(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200); self.end_headers()
        self.wfile.write(ui_global.encode())
    def do_POST(self):
        content = int(self.headers['Content-Length'])
        data = json.loads(self.rfile.read(content))
        response = {"msg": f"تم تنفيذ {data.get('t', 'التوليد')} بنجاح عبر الوكيل المساعد."}
        self.send_response(200); self.send_header('Content-Type', 'application/json'); self.end_headers()
        self.wfile.write(json.dumps(response).encode())
HTTPServer(('localhost', 3000), V6_Neural).serve_forever()
