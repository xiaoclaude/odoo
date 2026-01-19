#!/bin/bash
# Update module script
echo "Updating sz_shouzheng_homepage on 8070..."
python3 -u /home/web/odoo/odoo-bin -c /mnt/c/Users/xiao/.gemini/antigravity/scratch/odoo19/odoo.conf -d odoo_fresh -u sz_shouzheng_homepage --stop-after-init
echo "Module updated. You can now refresh your browser."
