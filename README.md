# Speed Test
A simple speed test script to check internet speed over a scheduled time.

## Chart 
I created a simple [Line chart](https://public.flourish.studio/visualisation/11273439/ "@embed") with the help of [Flourish](https://app.flourish.studio/)

You can use your own embed link in **chart.html**


## Cron Scheduler
I scheduled this script to run at 20th minute as 
```
*/20 * * * * /home/fasih/code/test/venv/bin/python /home/fasih/code/test/speed_test.py 1> /home/fasih/code/test/speed_test.log 2> /home/fasih/code/test/speed_test.err
```
## Libraries
Make sure you have installed speedtest_cli.

`pip install speedtest_cli`



I am open to suggestions. Kindly fork this repo if you want to use it for yourself.