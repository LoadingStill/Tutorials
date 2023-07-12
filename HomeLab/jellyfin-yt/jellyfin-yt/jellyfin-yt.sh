#!/bin/bash

# Directory where you want to save the videos
dir="/path/to/your/YouTube"

# The document where the channels are listed
doc="/path/to/your/doc.txt"

# Check if youtube-dl is installed
if ! command -v youtube-dl &> /dev/null
then
    echo "youtube-dl could not be found"
    exit
fi

# Loop over each channel in the document
while IFS= read -r channel
do
    # Create the channel directory
    channel_dir="$dir/${channel} - [%(uploader_id)s]"
    mkdir -p "$channel_dir"

    # Define the output template
    output_template="$channel_dir/%(title)s - %(uploader)s - %(upload_date)s - [%(id)s]/%(title)s - %(uploader)s - %(upload_date)s - [%(id)s]"

    # Download the videos
    youtube-dl -ciw -o "$output_template.%(ext)s" --write-info-json --write-sub --sub-lang en --format "bestvideo[height<=1080]+bestaudio/best[height<=1080]" "ytuser:$channel"
done < "$doc"





# Remember to replace /path/to/your/YouTube, /path/to/your/doc.txt, and /path/to/your/script.sh with the actual paths in your environment.
# Also, make sure that you have the necessary permissions to read the document and write to the specified directory.

# Please note that this script assumes that the document contains the actual channel names, not the channel IDs.
# If the document contains the channel IDs, you should replace "ytuser:$channel" with "ytchannel:$channel".
