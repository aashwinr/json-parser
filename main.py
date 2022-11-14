object = {
    "hello":"world",
    "key2":"value2",
    "key3":"value3"
}

kvpairs = list(object.items())
for i in kvpairs:
    print(f'Key: {i[0]}, Value: {i[1]}')