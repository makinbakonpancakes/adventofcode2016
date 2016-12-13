import hashlib

num = 0
code = ''
code2 = [None, None, None, None, None, None, None, None]
while True:
    door = 'abbhdwsy'
    door += str(num)
    hashbrown = hashlib.md5(door.encode('utf-8')).hexdigest()
    if hashbrown[:5] == '00000':
        hashslinginslasher = hashbrown[5]
        code += hashslinginslasher
        if hashslinginslasher.isdigit() and int(hashslinginslasher) < 8:
            if code2[int(hashslinginslasher)] is None:
                code2[int(hashslinginslasher)] = hashbrown[6]
            if len(code) >= 8 and not None in code2:
                code = code[:8]
                code2 = ''.join(code2)
                break
    num += 1
print('Part 1: ' + code)
print('Part 2: ' + code2)
