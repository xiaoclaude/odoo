#!/bin/bash
pkill -f odoo-bin
sleep 2
nohup python3 -u /home/web/odoo/odoo-bin -c /mnt/c/Users/xiao/.gemini/antigravity/scratch/odoo19/odoo.conf -u base > /home/web/odoo_repair.log 2>&1 &
echo "Odoo repairing base module. Check /home/web/odoo_repair.log"
