*Self-Healing Infrastructure using Prometheus, Alertmanager, Flask & Ansible

Objective
Automatically detect service failures (like NGINX down or CPU > 90%) and **recover** them using **alerts + automation**.

Tools Used
- Prometheus (Monitoring)
- Alertmanager (Alert routing)
- Ansible (Auto-healing)
- Flask (Webhook Receiver)
- Shell Scripting
- Ubuntu Server (EC2)

Workflow Overview
1. Prometheus monitors node metrics (via `node_exporter`)
2. When NGINX is down or CPU > 90%, it fires an alert
3. Alertmanager receives the alert and sends it to a Flask webhook
4. Flask triggers an Ansible playbook that **restarts NGINX**
5. System auto-recovers from failure without manual intervention

-> Setup Guide

1. Install Components
- Install and run: `nginx`, `node_exporter`, `prometheus`, `alertmanager`, `ansible`, `flask`

2. Configure Prometheus
- `prometheus.yml`: Includes scrape configs and alert rule file
- `alerts.yml`: Contains alert for `CPU > 90%` and `nginx down`

3. Configure Alertmanager
- `alertmanager.yml`: Sends webhook POST to Flask on port `5001`

4. Flask Webhook
- `webhook.py`: Listens for alerts and triggers `restart_nginx.yml`
- `restart_nginx.yml`: Ansible playbook to restart NGINX service

5. Run Flask
```bash
python3 webhook.py
