screen masturbation:
    add 'pic/events/mastur/start.png'
    fixed xpos 0.01 ypos 0.01:
        hbox:
            vbar value StaticValue(endurance, 200):
                xalign 0.0 yalign 0.0
                ymaximum 750
            vbar value StaticValue(player.getLust(), 100):
                xalign 0.0 yalign 0.0
                ymaximum 750
    fixed:
        text 'Настроение' xalign 0.0051 yalign -0.02  style style.verticalText
        text 'Возбуждение' xalign 0.0248 yalign 0.95 style style.verticalText
    fixed xpos 0.75 ypos 0.01:
        vbox:
            textbutton 'Ласкать грудь' xminimum 200 action Jump('mastur_tits')
            textbutton 'Гладить себя' xminimum 200 action Jump('mastur_teasing')
            textbutton 'Ласкать клитор' xminimum 200 action Jump('mastur_clit')
            textbutton 'Вставить палец в киску' xminimum 200 action Jump('mastur_1finger')
        
label startMastur:
    $ changetime(3)
    $clrscr()
    if endurance < 0 or player.getLust() <= 0:
        jump endMastur
    if player.getLust() >= 100:
        jump mastur_orgasm
    else:
        call screen masturbation
    
label endMastur:
    show expression 'pic/events/mastur/end.png' at top as tempPic
    'В какой то момент вы почувствовали, что вам это всё надоело. Вами овладело раздражение.'
    player.say 'Чёрт подери, я даже мужика себе найти не могу!'
    'В удрученном настроении вы начали приводить себя в порядок.'
    python:
        player.incLust(-100)
        player.incEnergy(-100)
        move(curloc)

label mastur_orgasm:
    show expression 'pic/events/mastur/orgasm.png' at top as tempPic
    'Ваши стоны становятся громче, вы начинаете энергичней трахать свою киску пальчиком, одновременно лаская выпирающий клитор.'
    player.say 'О-о-о... А-а-а...'
    'В миг сладострастия, судороги прокатываются по вашему телу стремительным домкратом.'
    'Вы извиваетесь от сокращений мышц и громко стонете от сказочного удовольствия.'
    'Море эмоций затапливает ваш мозг, вы не можете контролировать своё тело, и оно исторгает из себя потоки влаги.'
    python:
        player.incDirty(1)
        player.incLust(-100)
        player.incCorr(1)
        player.incEnergy(50)
        move(curloc)
        
label mastur_tits:
    show expression 'pic/events/mastur/tits.png' at top as tempPic
    if player.getLust() < 25:
        'Трепеща, вы дотрагиваетесь до своих грудей руками и начинаете поглаживать бархатистую кожу.'
        'Ваше тело с готовностью отвечает на ласки и ноги невольно раздвигаются, предвкушая грядущее наслаждение.'
        player.say 'О, Боже! Как же это приятно!'
        'Вы продолжаете сжимать свои груди, слегка поигрывая сосками, пока волна жара внизу живота не напоминает о себе сладкой истомой.'
        python:
            if player.getLust() < 10:
                endurance += 1
                player.incLust(5)
            else:
                endurance += 10
                player.incLust(10)
    elif player.getLust() < 50:
        'Вы стискиваете свои груди, ощущая как волны жара прокатываются по вашему телу. Всё ваше естество кричит: "Ещё! Ещё!"'
        'Всё тело изгибается и бёдра сами по себе двигаются, ища наслаждения посильнее.'
        player.say 'Я хочу заполнить себя чем то! - бормочите вы, поглаживая напрягшиеся соски.'
        python:
            endurance += 1
            player.incLust(5)
    else:
        'Ваши руки беспорядочно мнут груди и соски. Тело трепещет от наслаждения, но вы сдерживаетесь, не позволяя рукам опускаться ниже.'
        player.say 'Как же это тяжело! Я не могу больше сдерживаться!'
        'Вам стоит больших усилий оставаться вдали от текущей щели между ног, и высокая концентрация слегка сбивает возбуждение.'
        python:
            endurance -= 10
            player.incLust(-5)
    jump startMastur
        
label mastur_teasing:
    show expression 'pic/events/mastur/teasing.png' at top as tempPic
    if player.getLust() < 20:
        'Вы поглаживаете своё тело, поднимая в себе волну возбуждения. Ваши руки нигде особо не задерживаются, разве что на особо приятных местах.'
        'Вы слегка стискиваете свой пирожок, сдерживая рвущийся из груди стон, и тут же поднимаетесь выше, царапая ногтями плоский живот.'
        'Поглаживая наливающиеся соски, вы подумываете о более интенсивных ласках.'
        python:
            endurance += 5
            player.incLust(5)
    else:
        'Вы сдерживаетесь, всего лишь поглаживая свою кожу, вместо того, чтобы засунуть сразу несколько пальцев в трепещущее лоно.'
        'Касания рук причиняют вам почти болезненное наслаждение и тело покрывают мурашки, когда вы проводите пальцами по половым губам, игнорируя жар внутри.'
        player.say 'Ах, ах! - срываются с вашей груди стоны.'
        player.say 'Я так долго не выдержу!'
        python:
            endurance -= 5
            player.incLust(-5)
    jump startMastur
    
label mastur_clit:
    show expression 'pic/events/mastur/clit.png' at top as tempPic
    if player.getLust() < 25:
        'Вы проводите пальцем по своему клитору, и вас пронзает серия почти что болезненных ощущений.'
        player.say 'Вот, бля! - не удерживаетесь вы от крепкого словечка, поспешно убирая руку.'
        python:
            endurance -= 10
            player.incLust(-10)
    elif player.getLust() < 50:
        'Вы дотрагиваетесь до своего набухшего бугорка между ног, медленно поглаживая эрогенную точку под пальцами.'
        'Несмотря на приятные ощущения, вызываемые прикосновениями, вы чувствуете, что до оргазма ещё далеко, и нехотя убираете руку.'
        python:
            endurance -= 5
    elif player.getLust() < 75:
        'Смачивая пальцы в своих склизких выделениях, вы проводите по выпирающему из капюшончика клитору.'
        player.say 'О, даа!!!'
        'Ваша рука, подрагивая от наслаждения, наглаживает набухший бугорок. Тело трепещет от возбуждения и бёдра сами по себе начинают двигаться навстречу шаловливым пальчикам.'
        python:
            endurance += 5
            player.incLust(10)
    else:
        'Блестящие от влаги пальцы порхают над клитором, то едва касаясь его, то сильно сжимая, заставляя тело вздрагивать от удовольствия.'
        'Ваша голова запрокидывается назад, а из груди вылетают стоны.'
        player.say 'Да! Да! Я сейчас! Я скорооо! Даааа!'
        'Пальцы вновь ныряют в хлюпающую киску и, обильно смазанные, вновь принимаются теребить самую эрогенную точку вашего тела.'
        python:
            endurance -= 5
            player.incLust(15)
    jump startMastur
    
label mastur_1finger:
    show expression ('pic/events/mastur/1finger%d.png' % rand(1,2)) at top as tempPic
    if player.getLust() < 20:
        'Несмотря на неприятные ощущения, вы засовываете палец в свою ещё не намокшую киску. Аккуратно трогая тёплые стенки своего влагалища, вы так и не смогли вызвать у себя никаких приятных чувств.'
        player.say 'Мда, сначала надо возбудиться...'
        python:
            endurance -= 5
            player.incLust(-5)
    elif player.getLust() < 50:
        'Вы скользите пальчиком вниз к вашей заветной щёлке. Достигнув дырочки, вы сначала делаете несколько круговых движений, обильно смазывая палец соками.'
        'Наконец, вы погружаете в неё свой средний палец на всю длину. Вас охватывает приятное удовлетворение, словно это именно то, что вам сейчас нужно.'
        'Лёгкий стон срывается с ваших губ, когда вы начинаете неторопливо трахать себя.'
        python:
            endurance += 5
            player.incLust(10)
    else:
        'Ваш палец так и мелькает, то входя, то выходя из трепещущей дырки. Вы пытаетесь достать им как можно глубже, чтобы усилить наслаждение и приблизить оргазм.'
        player.say 'Мне нужно больше, ещё! - стонете вы от удовольствия.'
        'Вы мечетесь по кровати от перевозбуждения и осознания, что не можете достигнуть вершины удовольствия используя только один палец. Даже появившаяся дрожь от массирования вашей точки G не приближает вас к оргазму ни на миллиметр.'
        python:
            endurance -= 5
    jump startMastur
