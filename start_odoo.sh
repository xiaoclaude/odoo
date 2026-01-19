#!/bin/bash
# No more killing 8069
sleep 1
# Start Odoo on 8070 (from conf)
nohup python3 -u /home/web/odoo/odoo-bin -c /mnt/c/Users/xiao/.gemini/antigravity/scratch/odoo19/odoo.conf -d odoo_fresh --logfile=/tmp/odoo_8070.log > /tmp/odoo_stdout.log 2>&1 &
echo "Odoo started on port 8070. Check /tmp/odoo_8070.log"
