# cicd_assignment
Source code of Assignment on CI/CD

## Setup Nginx

- Installing Nginx
```bash
sudo apt update
sudo apt install nginx
```

- Start Nginx
```bash
sudo systemctl start nginx
sudo systemctl enable nginx
```

- Restart Nginx
```bash
sudo systemctl restart nginx
```

## Cron Job to Run the Python Script

- Cron Job Configuration
```bash
crontab -e
```

- Run the Python Script (5 min interval)
```bash
*/5 * * * * /opt/conda/bin/python                   $HOME/deployments/cicd_deployment/check_html_commit.py >> cronjob.log 2>&1
```

- Check Cron Log
```bash
sudo grep CRON /var/log/syslog
```