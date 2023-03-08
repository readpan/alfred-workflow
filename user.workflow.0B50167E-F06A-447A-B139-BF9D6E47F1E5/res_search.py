#!/usr/bin/env python3
import subprocess
import sys
import json

# Run the command and capture the output
output_bytes = subprocess.check_output(
    ["/opt/homebrew/bin/displayplacer", "list"])

# Decode the output bytes into a string
output_str = output_bytes.decode("utf-8")

class ScreenConfig:
    def __init__(self, config_string):
        config_list = config_string.split("\n")
        self.screen_id = config_list[0].split(":")[1].strip()
        self.items = {
            "items": []
        }
        # self.mode = []
        for line in config_list:
            #  mode 47: res:1280x960 hz:60 color_depth:8 scaling:on
            line = line.strip()
            if line.startswith("mode"):
                info_items = line.split(" ")
                mode_num = int(info_items[1].replace(":",""))
                # if int(mode_num) > 3:
                    # continue
                # mode_dict = {
                #     "mode": int(info_items[1].replace(":","")),
                #     "res": info_items[2].split(":")[1],
                #     "scaling": "on" if len(info_items) > 5 else "off"
                # }
                scaling = "on" if len(info_items) > 5 else "off"
                mode_dict = {
                    "title": line,
                    "arg": f'id:{self.screen_id} mode:{mode_num}'
                }
                self.items['items'].append(mode_dict)


screen_config = ScreenConfig(output_str)

print(json.dumps(screen_config.items))

# 根据id不同, 给出一些预设值.
