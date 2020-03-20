import os, base64

icon = open('question.png', 'rb')
icon_data = icon.read()
icon_data_base64 = base64.b64encode(icon_data)

LIMIT = 60
limit_icon = []

if __name__ == '__main__':
    # print(icon_data_base64)
    while True:
        sLimit = icon_data_base64[:LIMIT]
        icon_data_base64 = icon_data_base64[LIMIT:]
        limit_icon.append('\'%s\'' %sLimit)
        if len(sLimit) < LIMIT:
            break
    print(os.linesep.join(limit_icon))