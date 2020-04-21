from base64 import b64decode as dc64

class Formatter():
    def cleanSubject(subject):
        if subject[:10].upper() == '=?UTF-8?B?':
            print('[+] Base64 detected')
            msgs = subject.split()
            ret = ''
            for i in msgs:
                data = i[10:]
                try:
                    ret += dc64(data).decode()
                except Exception as e:
                    ret = data
            return ret.replace('\n', ' ')
        elif subject.startswith('=?UTF-8?Q?') or subject.startswith('=3D=3D=3D'):
            print('[+] Hex detected from subject')
            print('\t[+] It will take some time')
            msgs = subject.split()
            from string import digits, ascii_uppercase as up
            valid = digits + up[:6]
            ret = ''
            for i in msgs:
                tmp, data, clean = [], '', ''
                i = i.replace('=?UTF-8?Q?', '').replace('?=', '')
                for j in i.split('='):
                    if len(j) >= 2 and j[0] in valid and j[1] in valid:
                        if len(j) == 2: tmp.append(j)
                        else:  
                            tmp.append(j[0] + j[1])
                            tmp.append(j[2:])
                try: ret += bytes.fromhex(''.join(tmp).replace('_', '').replace('/', '')).decode('utf-8')
                except:
                    for j in tmp:
                        if len(j) == 2: data += j
                        else:
                            clean = bytes.fromhex(data).decode('utf-8') + j
                            data = ''
                    ret += clean
            return ret.replace('_',' ')
        else:
            return subject.replace('\n', ' ')
    def cleanTime(time):
        time = time.split(' ')[:4]
        ret = ' '.join(time)
        return ret

    def cleanFrom(data):
        try:
            if data.index('<') == 0: data = data[1:-1]
            elif '@' in data: data = data[:data.index('<') - 1]
            if data.startswith('=?UTF-8?B?'):
                data = data.replace('=?UTF-8?B?', '').replace('?=', '')
                try: data = dc64(data).decode()
                except Exception as e: pass
            return data.replace("\"", '')
        except:
            return data

    def cleanBody(body):
        if body.startswith('=?UTF-8?Q?') or body.startswith('=3D=3D=3D'):
            print('[+] Hex detected from body')
            print('\t[+] It will take some time')
            print('\t[-] Maybe spaces will not shown up')
            msgs = body.split()
            from string import digits, ascii_uppercase as up
            valid = digits + up[:6]
            ret = ''
            for i in msgs:
                tmp, data, clean = [], '', ''
                i = i.replace('=?UTF-8?Q?', '').replace('?=', '')
                for j in i.split('='):
                    if len(j) >= 2 and j[0] in valid and j[1] in valid:
                        if len(j) == 2: tmp.append(j)
                        else:  
                            tmp.append(j[0] + j[1])
                            tmp.append(j[2:])
                try: ret += bytes.fromhex(''.join(tmp).replace('_', '').replace('/', '')).decode('utf-8')
                except:
                    for j in tmp:
                        if len(j) == 2: data += j
                        else:
                            try: clean = bytes.fromhex(data).decode('utf-8') + j
                            except:
                                return ret.replace('=', '').replace('-', '')
                            data = ''
                    ret += clean
            return ret.replace('_',' ').replace('-', '')
        return body.replace('_', '')
