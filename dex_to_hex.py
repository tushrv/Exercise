dec_to_hex_dict = {'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','10':'A','11':'B','12':'C','13':'D','14':'E','15':'F'}
num = int(input('Enter a number: '))
hex = ''

while num>0:
    hex += dec_to_hex_dict[str(num%16)] 
    num = num//16

result = hex[::-1] #from right to left
print(result)