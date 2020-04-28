

计划任务就是每周1到周5,晚上14点每隔30分钟执行一次


# 计划任务分两块：1. 搜集数据的计划任务，  2. 定时发邮件的计划任务

crontab -e

分钟  小时 天  周  月

0,30  0-6 * * 1-5   /usr/local/bin/python3.6 /root/jsP_Mons.py



sudo service cron start

