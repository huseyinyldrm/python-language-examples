#key ve value kavramlari vardir.
#degiskenAdi={'istanbul':34 ,'diyarbakir':21} seklinde yazilir.

plakalar={'Kocaeli':41,'Istanbul':34,'Diyarbakir':21,'Bingol':12}

print(plakalar['Kocaeli'])
print(plakalar['Diyarbakir'])
print(plakalar['Bingol'])
print(plakalar['Istanbul'])

plakalar['Ankara']=6

print(plakalar)

print('------------------------------------------------')

users={
    'sadikTuran':{
        'age':36,
        'email':'sadikturan@.com',
        'address':'Kocaeli',
        'phone':'05355555555'
    },
    'cinarTuran':{
        'age':21,
        'roles':['admin','user'],
        'email':'cinarturan@.com',
        'address':'Kocaeli',
        'phone':'05355554444'
    }
}

print('------------------------------------------------')

print(users['cinarTuran']['age'])
print(users['cinarTuran']['email'])
print(users['cinarTuran']['address'])
print(users['cinarTuran']['phone'])
print(users['cinarTuran']['roles'][0])
print(users['cinarTuran']['roles'][1])

print('------------------------------------------------')

print(users['sadikTuran']['age'])
print(users['sadikTuran']['email'])
print(users['sadikTuran']['address'])
print(users['sadikTuran']['phone'])


