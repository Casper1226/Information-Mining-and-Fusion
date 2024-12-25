#检查用户名和密码
database = [
    ['albert','1234'],
    ['shen','0601'],
    ['mun','njas'],
    ['muyan','1254']
    ]

username = input("User name: ")
pin = input('PIN code: ')

if [username,pin] in database: print('登陆成功，允许访问')
