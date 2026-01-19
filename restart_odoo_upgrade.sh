#!/bin/bash
# 停止Odoo
echo "Stopping Odoo..."
pkill -f 'odoo-bin' 2>/dev/null || kill $(ps aux | grep 'odoo-bin' | grep -v grep | awk '{print $2}') 2>/dev/null
sleep 2

# 启动Odoo并升级模块
echo "Starting Odoo and upgrading sz_shouzheng_homepage module..."
nohup python3 -u /home/web/odoo/odoo-bin -c /mnt/c/Users/xiao/.gemini/antigravity/scratch/odoo19/odoo.conf -d odoo_fresh -u sz_shouzheng_homepage --logfile=/tmp/odoo_8070.log > /tmp/odoo_stdout.log 2>&1 &

echo "Odoo restarted with module upgrade. Check /tmp/odoo_8070.log for details"
echo "Visit http://localhost:8070 to verify"
