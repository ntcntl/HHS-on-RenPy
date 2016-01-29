init -5 python:
    import random
    from random import choice
    import time
    from operator import attrgetter

    dublicationChar = []
    classrooms = []
    
    def rand(a, b):
        if a - b >= 0 or b == 0:
            return 0
        else :
            return random.randint(a,b)

    def randf(a, b):
        return random.uniform(a,b)


    def getPar(list, *args):
        temp = 0
        if args[0] == 'loy':
            for x in list:
                temp = temp + x.getLoy()
            return round(temp/len(list),2)

        if args[0] == 'fun':
            for x in list:
                temp = temp + x.getFun()
            return round(temp/len(list),2)

        if args[0] == 'corr':
            for x in list:
                temp = temp + x.getCorr()
            return round(temp/len(list),2)

        if args[0] == 'lust':
            for x in list:
                temp = temp + x.getLust()
            return round(temp/len(list),2)

        if args[0] == 'edu':
            for x in list:
                temp = temp + x.getEdu()
            return round(temp/len(list),2)

        if args[0] == 'rep':
            for x in list:
                temp = temp + x.getRep()
            return round(temp/len(list),2)
        return 'error'

    def waiting(t):
        player.stats.energy -= randf(t/2,t)
        changetime(t)
        move(curloc)
        
#Динамическая картинка
    def dynImage(st,at): 
        return dynpicto, None

#Работа с людьми
    def getChar(*args): 
        global dublicationChar, studs, teachers
        temp = []

        if len(args) == 0:
            return choice(studs)

        if len(args) == 1:
            if len(getLoc(curloc).getPeople()) > 0:
                for char in getLoc(curloc).getPeople():
                    if char.body.sex() == args[0] and teachers.count(char) == 0 and dublicationChar.count(char) == 0:
                        temp.append(char)
                if len(temp) > 0:
                    choosen = choice(temp)
                    dublicationChar.append(choosen)
                    if len(dublicationChar) > 10:
                        dublicationChar = []
                    return choosen

            for char in studs:
                if char.body.sex() == args[0] and dublicationChar.count(char) == 0:
                    temp.append(char)

            choosen = choice(temp)
            dublicationChar.append(choosen)
            if len(dublicationChar) > 10:
                dublicationChar = []
            return choosen

        elif len(args) == 2:
            if args[1] == 'classroom':
                for x in getLoc(curloc).getPeople():
                    if (x.body.sex() == args[0] or args[0] == '') and x in studs:
                        temp.append(x)
                if len(temp) == 0:
                    return getChar(args[0])
                else:
                    return choice(temp)
                    
            elif args[1] == 'teacher':
                for x in teachers:
                    if x.body.sex() == args[0] or args[0] == '':
                        temp.append(x)
                return choice(temp)
                
            else:
                for x in studs:
                    if x.body.sex() == args[0] or args[0] == '':
                        temp.append(x)
                tempChar = temp[0]
                if args[1] == 'beautymax':
                    return max(temp, key = lambda x: x.stats.beauty)
                if args[1] == 'beautymin':
                    return min(temp, key = lambda x: x.stats.beauty)
                if args[1] == 'edumax':
                    return max(temp, key = lambda x: x.stats.education)
                if args[1] == 'edumin':
                    return min(temp, key = lambda x: x.stats.education)
                if args[1] == 'corrmax':
                    return max(temp, key = lambda x: x.stats.corr)
                if args[1] == 'corrmin':
                    return min(temp, key = lambda x: x.stats.corr)
                if args[1] == 'lustmax':
                    return max(temp, key = lambda x: x.stats.lust)
                if args[1] == 'lustmin':
                    return min(temp, key = lambda x: x.stats.lust)
                if args[1] == 'brustmax':
                    return max(temp, key = lambda x: x.body.parts['грудь'].size)
                if args[1] == 'brustmin':
                    return min(temp, key = lambda x: x.body.parts['грудь'].size)
                if args[1] == 'loymax':
                    return max(temp, key = lambda x: x.stats.loyalty)
                if args[1] == 'loymin':
                    return min(temp, key = lambda x: x.stats.loyalty)
                

    def clrscr():
        renpy.scene(layer='screens')

    def skipEvent():
        tryEvent(curloc)

    def setRep(count,amount):
        for x in range(0, count):
            getChar().incRep(amount)

    def setLoy(count,amount):
        for x in range(0, count):
            getChar().incLoy(amount)
            
    def setCorr(count,amount):
        for x in range(0, count):
            getChar().incCorr(amount) 
            
    def setLust(count,amount):
        for x in range(0, count):
            getChar().incLust(amount)
            
    def setFun(count,amount):
        for x in range(0, count):
            getChar().incFun(amount)   
            
    def setEdu(count,amount):
        for x in range(0, count):
            getChar().incEdu(amount)   

    def hadSex(*args):
        maleArr = []
        femaleArr = []
        for x in args:
            x.incCorr(randf(0.0,1.0))
        
        # мастурбация
        if len(args) == 1:
            if args[0].getSex() != 'male':
                if args[0].body.parts['вагина'].size < 4:
                    args[0].body.parts['вагина'].size += randf(0.0,0.1)
                if args[0].body.parts['анус'].size < 4:
                    args[0].body.parts['анус'].size += randf(0.0,0.1)
            args[0].incFun(5)
            args[0].setLust(0)
            args[0].incCorr(0.5)
            
        else:
            for x in args:
                if x.getSex() != 'female':
                    x.setLust(0)
                    maleArr.append(x)
                else:
                    x.setLust(0)
                    femaleArr.append(x)
                    
            # Лесбийская
            if len(maleArr) == 0:
                for x in femaleArr:
                    x.body.parts['вагина'].size += randf(0.0,0.1)
                    x.body.parts['анус'].size += randf(0.0,0.05)
                    x.incFun(5)
                    x.incCorr(1)
                    
            # Футы и не только?
            elif len(femaleArr) == 0:
                for x in maleArr:
                    if x.getSex() == 'futa':
                        x.body.parts['вагина'].size += randf(0.0,0.1)
                    x.body.parts['анус'].size += randf(0.0,0.05)
                    x.incFun(5)
                    x.incCorr(1)
                    
            else:
                # норма
                fucked = []
                for male in maleArr: # перебираем всех male/futa
                    male.incFun(5)
                    male.incCorr(1)
                    diameter = male.body.parts['пенис'].size/3.14
                    for female in femaleArr: # перебираем всех female
                        if female not in fucked: # если ещё не была в соитии
                            female.incCorr(1)
                            
                            if female.body.parts['вагина'].size < diameter/2: # Если диаметр слишком большой
                                female.body.parts['вагина'].size += diameter/5
                                female.incFun(-5)
                                fucked.append(female)
                                
                            elif female.body.parts['вагина'].size < diameter: # Если немного меньше
                                female.incFun(5)
                                female.body.parts['вагина'].size += diameter/15
                                if rand(1,3) == 1:
                                    female.body.parts['анус'].size += diameter/10
                                fucked.append(female)
                                
                            if len(fucked) == len(femaleArr): # Если бабы кончились, продолжаем начиная с первой
                                fucked = []
                            break
            
    def addDetention(*args):
        global detentions
        for char in args:
            if char in detentions == False:
                detentions.append(char)
            
    def getDays(number):
        if number == 0 or number >= 5:
            return str(number) + ' дней'
        elif number == 1:
            return str(number) + ' день'
        else:
            return str(number) + ' дня'

            
    def fillClasses():
        global classrooms
        for x in allChars:
            x.moveToLocation(None)
            
        classrooms = []
        classrooms.append(getLoc('loc_class1'))
        classrooms.append(getLoc('loc_class2'))
        classrooms.append(getLoc('loc_class3'))
        classrooms.append(getLoc('loc_class4'))
        classrooms.append(getLoc('loc_class5'))
        
        if weekday == 2 or weekday == 4:
            classrooms.append(getLoc('loc_pool'))
        else:
            classrooms.append(getLoc('loc_gym'))

        for x in studs:
            if x != callup:
                if x.inClass == 1: # первый класс
                    tempIndex = lt() - 1 + 0
                    if tempIndex > 5: tempIndex -= 6
                    x.moveToLocation(classrooms[tempIndex])
                    
                elif x.inClass == 2: # Второй класс
                    tempIndex = lt() - 1 + 1
                    if tempIndex > 5: tempIndex -= 6
                    x.moveToLocation(classrooms[tempIndex])
                    
                elif x.inClass == 3: # Третий класс
                    tempIndex = lt() - 1 + 2
                    if tempIndex > 5: tempIndex -= 6
                    x.moveToLocation(classrooms[tempIndex])
                    
                elif x.inClass == 4: # Четвёртый класс
                    tempIndex = lt() - 1 + 3
                    if tempIndex > 5: tempIndex -= 6
                    x.moveToLocation(classrooms[tempIndex])
                    
                else: # Пятый класс
                    tempIndex = lt() - 1 + 4
                    if tempIndex > 5: tempIndex -= 6
                    x.moveToLocation(classrooms[tempIndex])

        # Если в классе кто-то есть, то учитель идет туда, иначе - в учительскую.
        if len(classrooms[0].getPeople()) > 0 : 
            kupruvna.moveToLocation(classrooms[0].id)
        else:
            kupruvna.moveToLocation('loc_teacherRoom')
            
        if len(classrooms[1].getPeople()) > 0 : 
            danokova.moveToLocation(classrooms[1].id)
        else:
            danokova.moveToLocation('loc_teacherRoom')   
            
        if len(classrooms[2].getPeople()) > 0 :  
            frigidovna.moveToLocation(classrooms[2].id)
        else:
            frigidovna.moveToLocation('loc_teacherRoom')   
            
        if len(classrooms[3].getPeople()) > 0 : 
            bissektrisovna.moveToLocation(classrooms[3].id)
        else:
            bissektrisovna.moveToLocation('loc_teacherRoom')   
            
        if len(classrooms[4].getPeople()) > 0 : 
            dikovna.moveToLocation(classrooms[4].id)
        else:
            dikovna.moveToLocation('loc_teacherRoom')    
            
        if len(classrooms[5].getPeople()) > 0 :  
            mustangovich.moveToLocation(classrooms[5].id)
        else:
            mustangovich.moveToLocation('loc_teacherRoom')        
                    
    def clearLocations():
        for x in locations:
            x.removePeoples([])
            
    def checkJail():
        for x in studs:
            if x.getRep() < 5 and x.name in complains:
                move('jail')
  
    def addHighlight(char):
        if char in highlightP:
            highlightP.remove(char)
        else:
            highlightP.append(char)

    def getClubChars(club,*args):
        tempArr = []
        if len(args) == 0:
            for x in allChars:
                if x.club == club:
                    tempArr.append(x)
        else:
            if args[0] in ['male','female','futa']:
                for x in allChars:
                    if x.club == club and x.getSex() == args[0]:
                        tempArr.append(x)
                        
            if len(args) == 2 and args[1] in ['please'] and len(tempArr) == 0:
                tempChar = getChar(args[0])
                tempChar.club = club
                tempArr.append(tempChar)
                
            if args[0] in ['please']:
                for x in allChars:
                    if x.club == club:
                        tempArr.append(x)
                if len(tempArr) == 0:
                    tempChar = getChar()
                    tempChar.club = club
                    tempArr.append(tempChar)
        return tempArr
            
    def getCamArr():
        photoArr = []
        returnArr = []
        for path in config.searchpath:
            # Ищем каталоги с картинками во всех возможных RenPy каталогах ресурсов
            try:
                for x in os.listdir(os.path.join(path, 'pic/events/camera/wcf/')):
                    photoArr.append('pic/events/camera/wcf/' + x)
            except OSError:
                pass
                
        for x in range(1,4):
            returnArr.append(choice(photoArr))
        return returnArr
        
    def hasLocationsItem(item):
        for x in locations:
            if item in x.items:
                return True
        return False
