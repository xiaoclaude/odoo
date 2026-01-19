#!/bin/bash
pkill -f odoo-bin
sleep 2

echo "Installing module..."
python3 -u /home/web/odoo/odoo-bin -c /mnt/c/Users/xiao/.gemini/antigravity/scratch/odoo19/odoo.conf -d odoo_fresh -i sz_shouzheng_homepage --stop-after-init > /tmp/odoo_install.log 2>&1

echo "Restarting Odoo..."
nohup python3 -u /home/web/odoo/odoo-bin -c /mnt/c/Users/xiao/.gemini/antigravity/scratch/odoo19/odoo.conf -d odoo_fresh --logfile=/tmp/odoo_fresh.log --log-level=info > /tmp/odoo_stdout.log 2>&1 &
echo "Done."
