from flask import Flask, request
import subprocess
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def alertmanager_webhook():
    data = request.json
    print("Alert Received:", json.dumps(data, indent=2))  # Optional logging

    # Run the Ansible playbook
    subprocess.run(['ansible-playbook', '/opt/webhook/restart_nginx.yml'])

    return 'Alert Received and Handled\n', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

