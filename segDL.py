import requests

base_link = "https://a6-rf5-s-jtof.vidstream.to/stream/5606eddde87089caNxM7bq81Jvi4GjtNA.CgHS2FUJ3mOlPW8Jpxf1Lw__.eTI2eTZZNjRFVW5JbElrdCtBS1FMRGthK05SVmtzN2VWcHhjOEdFOVN3eUtSVzVaZ2JKQlFRWDF4akpwTmZCZzZDbXFRTWtNOXBuejJIMHkydXkvcW5nZTFrSmVnaVJVbTF0Si9SMWFaSmw2NGF2Q0JJWDhDWC9QalRBMTQ2V3FOaE5tQkpVekRTYkFrUVA1Z1B1dWVaeUk2bWRPVmV3Ymd1Q2cwNzR5RElnbm9BTWhrdGtNb2xKSFcxTXJmVTk1b1VSZ0FZOFcwVzNaQUZoTGNPcm1ZQlZSV2F0ZmwwYUZXQk9xSUtaQTNRU0E5a3VmcFN1b1hSOEpMdk40V1B4cWpJN1YwQjNIdzhONDliamR1Ui84a0YvYmRNRFhDdHFLcHNUejNVME8yOWpOS2RBd3ZhQi9uTG5LR3V4QW93OUcrV2FTNGhyMkgzV1B2c0htazJJZDdtUTZZKzJNS1dPTTdzVThESklNUnI1ZUtSbzlqelp0THVNcDRHMkxKcXJLWjdweUtzZGM2YlFNVHlseUJsU1VYcnRtZm9wU0Y0RE9pcDI5UUlzZWNrMkIrQkh4VnFGYXEwTzRqWVQ1T1RYS1d4c2NTYWtJQWNDaA__/"

local_filename = "out.ts"

seg_len = 4
mov_len = 2 * 60 * 60
count = mov_len // seg_len
print(count)


for i in range(1, count):
    # increment link
    lnk = base_link + "seg-" + str(i) + "-v1-a1.ts"

    print("Processing Part", i, "Completed", i * 100 // count, "%")

    # dl segment
    with requests.get(lnk, stream=True) as seg:
        # append segment on disk
        with open(local_filename, 'ab') as f:
            f.write(seg.raw.data)
