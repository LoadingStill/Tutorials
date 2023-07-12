# Jellyfin-YT naming and set up.


After creating the script, you need to make it executable. You can do this with the chmod command:  

```
chmod +x /path/to/your/jellyfin-yt.sh
```  
Just replace /path/to/your/youtube_downloader.sh with the actual path to your script.  


Then you can run the script directly from the terminal:

```
/path/to/your/jellyfin-yt.sh
```

And set it up in your crontab like so:  
```
@reboot /path/to/your/jellyfin-yt.sh
0 */4 * * * /path/to/your/jellyfin-yt.sh  
```
Again, replace /path/to/your/youtube_downloader.sh with the actual path to your script.
