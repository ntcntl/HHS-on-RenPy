init python:
    def dailyRecount(chars):
    
        global him_zavivka, depilation, skin_care, manicure, pedicure, ptime, last_eat, timeGetPanties, month, weekday, studs, teachers, lastWork, lastWashed, corrTeacherTime, camSold
        
        timeGetPanties = 0 # сброс времени выдачи трусов
        aphroUsedArr[:] = [] # сброс людей под афродизиаком
        
        if weekday == 1:
            school.daysWorked = 0
        
        if development == 0:
            # Голод
            if (ptime - last_eat)/24 > 1:
                temp = (ptime - last_eat)/2
                player.incHealth( -temp )
                
            # Вонь    
            if ptime - lastWashed > 48:
                player.incDirty(1)
            
        # Работа
        lastWork = -30
        
        # Собрания
        corrTeacherTime = - 100
        
        # Проверка камер
        camSold = -30
        
        # Салон красоты
        if him_zavivka > 0:
            him_zavivka -= 1
        if depilation > 0:
            depilation -= 1
        if skin_care > 0:
            skin_care -= 1
        if manicure > 0:
            manicure -= 1
        if pedicure > 0:
            pedicure -= 1
        
        # Олимпиада
        if (rand(1,10) == 1) and olympiad.month != month and olympiad.active == False and weekday <= 5 or weekday == 2:
            olympiad.weekday = weekday + 2
            if olympiad.weekday > 5:
                olympiad.weekday -= 5
            olympiad.active = True
        
        # Если есть клуб, забиваем в него как минимум 4 человек
        if 'cherleader' in school.clubs and len(getClubChars('cherleader')) < 4:
            while len(getClubChars('cherleader')) < 4:
                choice(getClubChars('','female','please')).club = 'cherleader'
                
        if 'cosplay' in school.clubs and len(getClubChars('cosplay')) < 4:
            while len(getClubChars('cosplay')) < 4:
                choice(getClubChars('','please')).club = 'cosplay'

        if 'sport' in school.clubs and len(getClubChars('sport')) < 4:
            while len(getClubChars('sport')) < 4:
                choice(getClubChars('','please')).club = 'sport'
                
        if 'medic' in school.clubs and len(getClubChars('medic')) < 4:
            while len(getClubChars('medic')) < 4:
                choice(getClubChars('','please')).club = 'medic'
                
        if 'pants' in school.clubs and len(getClubChars('pants')) < 4:
            while len(getClubChars('pants')) < 4:
                choice(getClubChars('','female','please')).club = 'pants'

                
        for char in chars:
            # Поломка подарков
            for item in char.inventory:
                if item.type == 'present':
                    item.durability -= rand(1,2)
                    if item.durability <= 0:
                        char.removeItem(item)

            if char in studs:
                # Подтягиваем или уменьшаем разврат до учительского уровня. Чем сильнее разница, тем выше изменениия. В будущем УБРАТЬ и сделать через статусы.
                char.incCorr((getPar(teachers,'corr') - char.getCorr())/10)
                # Добавление трусов, если их нет у чара.
                if char.getSex != 'male' and char.getItem(studpantiesF.name) == False:
                    char.addItem(studpantiesF)
                    
                # Убираем клуб, если его удалили или ученик не в том клубе
                if char.club not in school.clubs or (char.getSex() == 'male' and char.club in ['cherleader','pants']):
                    char.club = ''
                
                # Добавляем клуб (предварительная версия)
                if char.club == '' and rand(1,10) == 1 and len(school.getAllClubs('available')) > 0:
                    if char.getSex() != 'male':
                        char.club = choice(school.getAllClubs('available'))
                    else:
                        available = school.getAllClubs('available')
                        tempArr = []
                        for club in available:
                            if club not in ['pants','cherleader']:
                                tempArr.append(club)
                        if len(tempArr) > 0:
                            char.club = choice(tempArr)
                
                # Мастурбация или секс c любовником
                if char.getLust() > 70 and char.partner != None and rand(1,3) == 1 and char.getCorr() > 30:
                    if char.partner.getLust() > 70:
                        hadSex(char, char.partner)
                elif char.getLust() > 70:
                    hadSex(char)

    def hourlyReset():
        global hour, weekday, inhibLow, detentions
        
        if hour == 18:
            inhibLow = 0
        
        if hour % 4 == 0:
            for char in allChars:
                char.sayCount = int(1 + char.getLoy()/10 + (player.getBeauty()/20))
        
        if hour >= 17:
            detentions[:] = []
        
        if school.budget < 0: 
            school.removeClub('cherleader')
            school.removeClub('sport')
            school.removeClub('cosplay')
            school.removeClub('medic')
            school.removeClub('paint')
            
        if hour == 15 and weekday < 6:
            if 'cherleader' in school.clubs and weekday in [1,3,5]:
                school.budget -= 200
            if 'sport' in school.clubs and weekday in [2,4]:
                school.budget -= 100
            if 'cosplay' in school.clubs:
                school.budget -= 500
            if 'paint' in school.clubs:
                school.budget -= 300
            if 'medic' in school.clubs:
                school.budget -= 250
                
    def monthlyReset():
        global is_teacher_room_1, is_teacher_room_2, is_teacher_room_3
        if is_teacher_room_1 != 0: is_teacher_room_1 = 2
        if is_teacher_room_2 != 0: is_teacher_room_2 = 2
        if is_teacher_room_3 != 0: is_teacher_room_3 = 2