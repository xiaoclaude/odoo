#!/bin/bash
# Rebuild script
pkill -f odoo-bin
sleep 2

echo "Initializing odoo_fresh..."
python3 -u /home/web/odoo/odoo-bin -c /mnt/c/Users/xiao/.gemini/antigravity/scratch/odoo19/odoo.conf -d odoo_fresh -i base --stop-after-init > /tmp/odoo_init.log 2>&1

echo "Starting Odoo on odoo_fresh (Port 8070)..."
nohup python3 -u /home/web/odoo/odoo-bin -c /mnt/c/Users/xiao/.gemini/antigravity/scratch/odoo19/odoo.conf -d odoo_fresh --logfile=/tmp/odoo_fresh.log --log-level=debug > /tmp/odoo_stdout.log 2>&1 &

echo "Done. Logs at /tmp/odoo_fresh.log"
