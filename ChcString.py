
"""//字符串的合并
what_he_does = 'plays'
his_instrument = 'guitar'
his_name = 'Robert Johnson'
artist_intro = his_name+what_he_does+his_instrument


//字符串的转换
print(artist_intro)
num = 1
string = '1'
num2 = int(string) //转换变量类型
print(num + num2)


words = 'word'*3 //字符串可以相加，相乘
print(words)

word = 'a loooooong word'
num = 12
string = 'bang!'
total = string * (len(word)-num)
print(total)

//字符串的分片与索引
name = 'My name is ljyy'

print(name[0])
print(name[4])
print(name[0:4]) #from name[0]'M' to name[4]'a' , name[4] is encluded
print(name[-15]) #M
print(name[-1])#y



url = 'http://ww3.site.cn/185cc87jw1ex23yyvq29j20jg0t6gp4.gif'
file_name=url[-10:]

print(file_name)


phone_number = '159-1699-6904'
hiding_number = phone_number.replace(phone_number[:9],'*'*9)
print(hiding_number)

//xxx.find
search = '168'
num_a = '1386-168-0006'
num_b = '1681-131-0006'
print(search+'is at'+str(num_a.find(search))+'to'+str(num_a.find(search)+len(search))+'of num_a')
print(search+'is at'+str(num_b.find(search))+'to'+str(num_b.find(search)+len(search))+'of num_b')
print(str(num_a.find(search)))

//xxx.format 使用方法
print('{} a word she can get what she {} for.'.format('With', 'came'))
print('{preposition} a word she can get what she {verb} for'.format(preposition = 'With', verb = 'came'))
print('{} a word she can get what she {} for.'.format('With', 'came')) """


city = input('write down the name of city:')
print("http://apistore.baidu.com/microservice/weather?citypinyin={}".format(city))


