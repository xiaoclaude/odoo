#!/bin/bash
lsof -t -i:8069 | xargs -r kill -9
sleep 2
echo "Initializing new database odoo_fix..."
python3 /home/web/odoo/odoo-bin -c /mnt/c/Users/xiao/.gemini/antigravity/scratch/odoo19/odoo.conf -d odoo_fix -i base --stop-after-init
echo "Starting Odoo on odoo_fix..."
nohup python3 /home/web/odoo/odoo-bin -c /mnt/c/Users/xiao/.gemini/antigravity/scratch/odoo19/odoo.conf -d odoo_fix > /home/web/odoo.log 2>&1 &
echo "Odoo started on new DB."
