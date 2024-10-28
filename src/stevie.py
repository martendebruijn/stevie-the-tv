import os
import requests
import argparse
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
device_id = os.getenv("DEVICE_ID")

base_url = f"https://api.smartthings.com/v1/devices/{device_id}/commands"
headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

parser = argparse.ArgumentParser(description="Control Stevie the TV")

parser.add_argument(
    "--turn", type=str, help="Turn Stevie on or off", choices=["on", "off"]
)

parser.add_argument("--volume", type=int, help="Set Stevie's volume (0-100)")
args = parser.parse_args()


# Capability: Switch
# See: https://developer.smartthings.com/docs/devices/capabilities/capabilities-reference#switch
def turn_stevie(command):
    data = {
        "commands": [{"component": "main", "capability": "switch", "command": command}]
    }
    response = requests.post(base_url, headers=headers, json=data)
    if response.status_code == 200:
        print(f"Stevie is turned {command}!")
    else:
        print(f"Error sending command: {response.status_code}")


if args.turn:
    turn_stevie(args.turn)


# Capability: Audio Volume
# See: https://developer.smartthings.com/docs/devices/capabilities/capabilities-reference#audioVolume
# Volume: integer 0-100
def set_volume(volume):
    data = {
        "commands": [
            {
                "component": "main",
                "capability": "audioVolume",
                "command": "setVolume",
                "arguments": [volume],
            }
        ]
    }
    response = requests.post(base_url, headers=headers, json=data)
    if response.status_code == 200:
        print(f"Stevie's volume set to {volume}!")
    else:
        print(f"Error sending command: {response.status_code}")


if args.volume:
    set_volume(args.volume)
