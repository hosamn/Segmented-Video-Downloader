import requests
import shutil

def download_file(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    return local_filename


url = "https://a6-rf5-s-jtof.vidstream.to/stream/5606eddde87089caNxM7bq81Jvi4GjtNA.CgHS2FUJ3mOlPW8Jpxf1Lw__.eTI2eTZZNjRFVW5JbElrdCtBS1FMRGthK05SVmtzN2VWcHhjOEdFOVN3eUtSVzVaZ2JKQlFRWDF4akpwTmZCZzZDbXFRTWtNOXBuejJIMHkydXkvcW5nZTFrSmVnaVJVbTF0Si9SMWFaSmw2NGF2Q0JJWDhDWC9QalRBMTQ2V3FOaE5tQkpVekRTYkFrUVA1Z1B1dWVaeUk2bWRPVmV3Ymd1Q2cwNzR5RElnbm9BTWhrdGtNb2xKSFcxTXJmVTk1b1VSZ0FZOFcwVzNaQUZoTGNPcm1ZQlZSV2F0ZmwwYUZXQk9xSUtaQTNRU0E5a3VmcFN1b1hSOEpMdk40V1B4cWpJN1YwQjNIdzhONDliamR1Ui84a0YvYmRNRFhDdHFLcHNUejNVME8yOWpOS2RBd3ZhQi9uTG5LR3V4QW93OUcrV2FTNGhyMkgzV1B2c0htazJJZDdtUTZZKzJNS1dPTTdzVThESklNUnI1ZUtSbzlqelp0THVNcDRHMkxKcXJLWjdweUtzZGM2YlFNVHlseUJsU1VYcnRtZm9wU0Y0RE9pcDI5UUlzZWNrMkIrQkh4VnFGYXEwTzRqWVQ1T1RYS1d4c2NTYWtJQWNDaA__/seg-1-v1-a1.ts"


download_file(url)