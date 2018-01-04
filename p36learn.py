#coding:utf-8
what_he_does = ' plays '
his_instrument = 'guitar'
his_name = 'Robert Johnson'
artist_intro = his_name + what_he_does + his_instrument
print(artist_intro)

word = 'a loooooong word'
num = 12
string = 'bang!'
total = string * (len(word) - num)
print(total)

word = 'friends'
find_the_evil_in_your_friends = word[0]+word[2:4]+word[-3:-1]
print(find_the_evil_in_your_friends)

phone_number = '1386-666-0006'
hiding_number = phone_number.replace(phone_number[:9],'*'*9)
print(hiding_number)

search = '168'
num_a = '1386-168-0006'
num_b = '1681-222-0006'
print(search + ' is at ' + str(num_a.find(search)) + ' to '+ str(num_a.find(search) + len(search)) + ' of num_a')
print(search + ' is at ' + str(num_b.find(search)) + ' to '+ str(num_b.find(search) + len(search)) + ' of num_b')

print('{} a word she can get what she {} for.'.format('With','came'))
print('{preposition} a word she can get what she {verb} for'.format(preposition = 'With',verb = 'came'))
print('{0} a word she can get what she {1} for.'.format('With','came'))

# city = input("write down the name of city:")
# url = "http://apistore.baidu.com/microservice/weather?citypinyin={}".format(city)

a = [1,2,3,4]
b = 'abcde'
print a[::-1]
print b[::-1]
print list(reversed(a))
print list(reversed(b))

value = {'greet':'Hello world','language':'Python'}
print '%(greet)s from %(language)s.' %value
print '{greet} from {language}.'.format(greet = 'hello world',language = 'python')

