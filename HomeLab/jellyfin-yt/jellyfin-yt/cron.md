In terms of where these are stored, typically each user has their own crontab, and they are usually stored in /var/spool/cron/crontabs/ or a similar directory, but these are not meant to be edited directly. Always use the crontab command to interact with cron jobs.

For example, to add the cron job to run your script every 4 hours and at boot, you would do the following:

1. Open your crontab file in the default text editor by typing crontab -e in your terminal.

2. Add the following lines to the file (substituting "/path/to/your/script.sh" with the actual path to your script):

3. Save and close the file. The cron daemon will automatically apply the changes.

```
@reboot /path/to/your/script.sh
0 */4 * * * /path/to/your/script.sh
```
