# ubuntu-wilyXML-config-script

# About
This Python Script will generate a wily.xml file for ubuntu in order
to create a background wallpaper slide show with new added images.
I couldn't find an easy way to add new images to the background slide show That comes with ubuntu apart from manually modifying the wily.xml file that the transitions for the slide show.

# Usage
Clone this repository to your computer

Backup the wily.xml file you currently have now

Add new  images with the '.jpg' extension to '/usr/share/backgrounds/' that you wish to add to the slide show

You must run the script with elevated permissions using
sudo python wily.py
