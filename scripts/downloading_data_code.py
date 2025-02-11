import requests as re
import os

parameters = [
    "T2M", "ALLSKY_SFC_SW_DWN", "WS2M", "RH2M", "T2M_MAX", "T2M_MIN", "WS50M", "WD50M", "WD2M",
    "CLOUD_AMT", "PRECTOTCORR", "GWETPROF", "TS", "QV2M", "GWETROOT", "GWETTOP", "WS50M_MAX",
    "WS50M_MIN", "ALLSKY_SFC_UVA", "ALLSKY_SFC_UVB", "ALLSKY_SFC_UV_INDEX", "MIDDAY_INSOL",
    "SZA", "TS_MAX", "TS_MIN", "WS2M_MAX", "WS2M_MIN", "PW", "AIRMASS", "CLOUD_AMT_DAY",
    "CLOUD_AMT_NIGHT", "CLRSKY_DAYS", "EVLAND", "ORIGINAL_ALLSKY_SFC_SW_DWN", "PSH", "PRECSNO",
    "RHOA", "TO3", "T10M", "T10M_MAX", "T10M_MIN", "TSOIL1", "TSOIL2", "TSOIL3", "TSOIL4",
    "TSOIL5", "TSOIL6", "Z0M"
]

for y in range(2019, 2024):
    for param in parameters:
        url = f'https://power.larc.nasa.gov/api/temporal/daily/regional?start={y}0101&end={y}1231&latitude-min=22&latitude-max=32&longitude-min=24.5&longitude-max=34.5&community=ag&parameters={param}&format=csv&header=true&time-standard=utc'
        response = re.get(url)
        if response.status_code == 200:
            with open(f"D:/data/{y}/{param}.csv", "w") as file:
                file.write(response.text)
            print('.', sep="")
        else:
            print(f"Error with D:/data/{y}/{param}.csv")
            print(response.status_code)

