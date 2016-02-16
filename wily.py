# Script for generating the wily.xml files for ubuntu
# This script will look in the /usr/share/backgrounds/ folder for any new .jpg images
# It will then generate a wily.xml file for the background slideshow

import glob
from lxml import etree
fileNames = glob.glob("/usr/share/backgrounds/*.jpg")

# create XML
root = etree.Element('background')
starttime = etree.Element('starttime')

year = etree.Element('year')
year.text = '2009'

month = etree.Element('month')
month.text = '08'

day = etree.Element('day')
day.text = '04'

hour = etree.Element('hour')
hour.text = '00'

minute = etree.Element('minute')
minute.text = '00'

second = etree.Element('second')
second.text = '00'

starttime.append(year)
starttime.append(month)
starttime.append(day)
starttime.append(hour)
starttime.append(minute)
starttime.append(second)

root.append(starttime)

i = 0
for i in range(0,len(fileNames)-1):
    static = etree.Element('static')
    duration1 = etree.Element('duration')
    duration2 = etree.Element('duration')
    filename = etree.Element('file')
    fromname = etree.Element('from')
    to = etree.Element('to')
    transition = etree.Element('transition')
    # print "Filename is " + fileNames[i]
    filename.text = fileNames[i]
    duration1.text = '1795.0'
    static.append(duration1)
    static.append(filename)
    duration2.text = '5.0'
    transition.append(duration2)
    fromname.text = fileNames[i]
    transition.append(fromname)
    to.text = fileNames[i+1]
    transition.append(to)
    # print etree.tostring(static, pretty_print=True)
    root.append(static)
    root.append(transition)

f = open('/usr/share/backgrounds/contest/wily.xml','w')
# pretty string
s = etree.tostring(root, pretty_print=True)
f.write(s)
f.close()
print "Success"
