from os import urandom
import sys

def serializeUAVData(uav_data:dict) -> str:
    res = ''
    for k in uav_data:
        res += f'{uav_data[k]} '
    return res.strip()


if __name__ == "__main__":
    FLAG = sys.argv[1]
    
    GS_DATA = {
        "port": 50013,
        "GID": urandom(20).hex()
    }
    UAVs = [
        {
        "tuid": urandom(20).hex(),
        "psk": urandom(40).hex(),
        "initiator": 1,
        "flag_part": FLAG[:len(FLAG)//2 + 1]
        },
        {
        "tuid": urandom(20).hex(),
        "psk": urandom(40).hex(),
        "initiator": 0,
        "flag_part": FLAG[len(FLAG)//2 + 1:]
        }
    ]

    with open("./config/gs.config", "w") as f:
        f.write(f'{GS_DATA["GID"]} {GS_DATA["port"]}\n')

        for uav in UAVs:
            f.write(f'{uav["tuid"]} {uav["psk"]}\n')

    i = 1
    for uav in UAVs:
        with open(f"./config/uav_{i}.config", "w") as f:
            f.write(f'{GS_DATA["GID"]} {GS_DATA["port"]}\n')
            f.write(serializeUAVData(uav) + '\n')
            i += 1
        