from Tavin import *
import subprocess
obj = subprocess.Popen('"assets/main.exe"', stdin = subprocess.PIPE, shell = True)

app = Tavin(title = 'TheMarkDomain-Browser', env = __name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api')
def api():
    webview.create_window(
        title = 'TheMarkDomain-Browser',
        url = request.values.get('link'),
        width = 800,
        height = 600
    )
    return redirect('/')

app.run()
obj.stdin.write(b'^Z\n')