import os
from datetime import datetime
from time import sleep
from speedtest import Speedtest, SpeedtestException


SERVERS = []
THREADS = None
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "speed_data.csv")
print(datetime.now(), FILE_PATH)
while True:
    try:
        s = Speedtest()
        s.get_servers(SERVERS)
        s.get_best_server()
        s.download(threads=THREADS)
        s.upload(threads=THREADS)
        break
    except SpeedtestException as e:
        print(f"Got Exception as: {str(e)}" )
        sleep(5)
        continue


# s.results.share()
results_dict = s.results.dict()

results_dict["timestamp"] = str(datetime.now())
results_dict["timestamp"] = (
    results_dict["timestamp"][0:10] + " " + results_dict["timestamp"][11:19]
)
result = f"""\n{results_dict['timestamp']},{results_dict['client']['isp']},{results_dict['ping']},{results_dict['download']/1000000:.3f},{results_dict['upload']/1000000:.3f},Mbps"""

with open(FILE_PATH, "a", encoding="ascii") as file:
    file.write(result)
