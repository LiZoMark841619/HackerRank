def timeConversion(s):
    hour, minute, second = s.split(':')
    sec, am_pm = second[:2], second[2:]
    
    if am_pm == 'PM':
        if hour in ['0'+str(i) for i in range(10)]:
            hour = int(hour[-1])
            hour += 12
        elif hour in ['10', '11']:
            hour = int(hour)
            hour += 12        
    elif am_pm == 'AM':
        if hour == '12':
            hour = '00'
            
    return f'{hour}:{minute}:{sec}'

if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)