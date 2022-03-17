# -*- coding: utf-8 -*-
### VERSION 2.00 STANDALONE

# Continuous: Solid line
# CENTER: Center ____ _ ____ _ ____ _ ____ _ ____ _ ____
# DASHED: Dashed __ __ __ __ __ __ __ __ __ __ __ __ __ _
# PHANTOM: Phantom ______  __  __  ______  __  __  ______
# HIDDEN: Hidden __ __ __ __ __ __ __ __ __ __ __ __ __ __
# CENTERX2: Center (2x) ________  __  ________  __  ________
# CENTER2: Center (.5x) ____ _ ____ _ ____ _ ____ _ ____
# DASHEDX2: Dashed (2x) ____  ____  ____  ____  ____  ____
# DASHED2: Dashed (.5x) _ _ _ _ _ _ _ _ _ _ _ _ _ _
# PHANTOMX2: Phantom (2x)____________    ____    ____    ____________
# PHANTOM2: Phantom (.5x) ___ _ _ ___ _ _ ___ _ _ ___ _ _ ___
# DASHDOT: Dash dot __ . __ . __ . __ . __ . __ . __ . __
# DASHDOTX2: Dash dot (2x) ____  .  ____  .  ____  .  ____
# DASHDOT2: Dash dot (.5x) _ . _ . _ . _ . _ . _ . _ . _
# DOT: Dot .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .
# DOTX2: Dot (2x) .    .    .    .    .    .    .    .
# DOT2: Dot (.5) . . . . . . . . . . . . . . . . . . .
# DIVIDE: Divide __ . . __ . . __ . . __ . . __ . . __
# DIVIDEX2: Divide (2x) ____  . .  ____  . .  ____  . .  ____
# DIVIDE2: Divide(.5x) _ . _ . _ . _ . _ . _ . _ . _
clt = {
    # ID:["име","linetype","lineweight","colorid"]
    "0": ["0", "Continuous", 13, 7],
    "hatch": ["HATCH", "Continuous", 13, 8],
    "txt": ["TEXT", "Continuous", 13, 140],
    "cid": ["CONTOUR ID", "Continuous", 13, 140],
    "gp": ["GEOPOINTS", "Continuous", 13, 30],
    "so": ["СО НИВО", "Continuous", 13, 220],
    "9": ["Линия за репераж", "Continuous", 13, 7],
    "10": ["Полигонова линия", "Continuous", 13, 7],
    "11": ["Осова линия", "DASHDOTX2", 13, 7],
    "12": ["Операционна линия", "Continuous", 13, 7],
    "13": ["Линия за сгради", "Continuous", 50, 7],
    "14": ["Постройка в строеж", "Continuous", 13, 7],
    "15": ["Разрушена сграда", "Continuous", 13, 7],
    "16": ["Линия за открити външни стълби", "Continuous", 13, 7],
    "17": ["Открит вход за подземна част", "Continuous", 13, 7],
    "18": ["Калкан на сграда", "Continuous", 50, 7],
    "19": ["Балкон (веранда) на стълбове", "Continuous", 13, 7],
    "20": ["Илюминатор", "Continuous", 13, 7],
    "21": ["Шахта  за изба", "Continuous", 13, 7],
    "22": ["Тераса", "Continuous", 13, 7],
    "23": ["Въздушен проход", "Continuous", 13, 7],
    "24": ["Надземна част на подземна постройка", "Continuous", 13, 7],
    "25": ["Бордюр", "Continuous", 13, 7],
    "26": ["Бeседки", "Continuous", 13, 7],
    "27": ["Навес", "Continuous", 13, 7],
    "28": ["Противопожарна стена", "Continuous", 13, 7],
    "29": ["Парници", "Continuous", 13, 7],
    "30": ["Трамвайна тролейбусна автобусна спирка (масивна)", "Continuous", 13, 7],
    "32": ["Трамвайна тролейбусна автобусна спирка (на колони)", "Continuous", 13, 7],
    "33": ["Парник", "Continuous", 13, 7],
    "34": ["Пчелин", "Continuous", 13, 7],
    "36": ["Проектна ос на трамвайна линия", "Continuous", 13, 7],
    "40": ["Срутен вход на шахта шурф", "Continuous", 13, 7],
    "41": ["Табан", "Continuous", 13, 7],
    "42": ["Геоложка канавка", "Continuous", 13, 7],
    "43": ["Открити разработки", "Continuous", 13, 7],
    "44": ["Портален и мостов кран", "Continuous", 13, 7],
    "45": ["Естакада 1", "Continuous", 13, 7],
    "46": ["Естакада 2", "Continuous", 13, 7],
    "47": ["Електрoпровод  на  дървени стълбове", "Continuous", 13, 7],
    "48": ["Електрoпровод  на  железни стълбове", "Continuous", 13, 7],
    "49": ["Електрoпровод  на железни ферми", "Continuous", 13, 7],
    "50": ["Подземен електропровод", "Continuous", 13, 7],
    "51": ["Тръбопровод надземен на опори", "Continuous", 13, 7],
    "52": ["Канализация надземна на опори", "Continuous", 13, 7],
    "53": ["Телефонна и телеграфна линия", "Continuous", 13, 7],
    "54": ["Железопътна линия", "Continuous", 13, 7],
    "55": ["Железопътна линия двойна", "Continuous", 13, 7],
    "56": ["Железопътна линия електрифицирана", "Continuous", 13, 7],
    "57": ["Железопътна линия електрифицирана", "Continuous", 13, 7],
    "58": ["Железопътен електропровод", "Continuous", 13, 7],
    "59": ["Железопътна линия в строеж", "Continuous", 13, 7],
    "60": ["Изоставена железопътна  линия", "Continuous", 13, 7],
    "61": ["Теснолинейна железопътна линия", "Continuous", 13, 7],
    "62": ["Теснолинейна железопътна линия в строеж", "Continuous", 13, 7],
    "63": ["Теснолинейна железопътна линия електрифицирана", "Continuous", 13, 7],
    "64": ["Трамвайна  линия единична", "Continuous", 13, 7],
    "65": ["Трамвайна  линия двойна", "Continuous", 13, 7],
    "66": ["Трамвайна линия в строеж", "Continuous", 13, 7],
    "67": ["Въжена линия", "Continuous", 13, 7],
    "68": ["Тролейбусна линия на стълбове", "Continuous", 13, 7],
    "69": ["Тролейбусна линия на постройки", "Continuous", 13, 7],
    "70": ["Автомагистрала", "Continuous", 13, 7],
    "71": ["Шосе", "Continuous", 13, 7],
    "72": ["Шосе в строеж", "Continuous", 13, 7],
    "73": ["Път (земеустройствен почвен)", "Continuous", 13, 7],
    "74": ["Полски и горски път", "Continuous", 13, 7],
    "75": ["Профилирана туристическа пътека", "Continuous", 13, 7],
    "76": ["Пътека", "Continuous", 13, 7],
    "77": ["Изоставен път", "Continuous", 13, 7],
    "78": ["Шосе в насип", "Continuous", 13, 7],
    "79": ["Шосе в изкоп", "Continuous", 13, 7],
    "80": ["Алея в паркове и градини", "Continuous", 13, 7],
    "81": ["Шосе с дървета", "Continuous", 13, 7],
    "82": ["Прокар с ограда", "Continuous", 13, 7],
    "83": ["Прокар без ограда", "Continuous", 13, 7],
    "84": ["Предпазна ограда каменна", "Continuous", 13, 7],
    "85": ["Предпазна ограда метална", "Continuous", 13, 7],
    "90": ["Канал", "Continuous", 13, 42],
    "91": ["Канал", "Continuous", 13, 42],
    "92": ["Канал", "Continuous", 13, 42],
    "93": ["Канал в строеж", "DASHED2", 13, 42],
    "94": ["Канал в строеж", "DASHED2", 13, 42],
    "95": ["Води", "Continuous", 13, 7],
    "96": ["Водна линия на пресъхващи реки", "Continuous", 13, 7],
    "97": ["Непостоянна водна линия на езера и блата", "Continuous", 13, 7],
    "98": ["Подпорна стена наклонена бетонна", "Continuous", 13, 7],
    "99": ["Подпорна стена наклонена каменна", "Continuous", 13, 7],
    "100": ["Дървена подпорна стена", "Continuous", 13, 7],
    "101": ["Подпорна стена отвесна бетонна каменна", "Continuous", 13, 7],
    "102": ["Подпорна стена дървена наклонена", "Continuous", 13, 7],
    "103": ["Подпорна стена дървена отвесна", "Continuous", 13, 7],
    "104": ["Откос укрепен", "Continuous", 13, 7],
    "105": ["Откос неукрепен", "Continuous", 13, 7],
    "106": ["Буна с откос", "Continuous", 13, 7],
    "107": ["Буна без откос", "Continuous", 13, 7],
    "108": ["Каменна или бетонна язовирна стена", "Continuous", 13, 7],
    "109": ["Земен бент", "Continuous", 13, 7],
    "110": ["Водопровод надземен", "Continuous", 13, 7],
    "111": ["Подземен тръбен канал с хидранти", "Continuous", 13, 7],
    "112": ["Дига изразена немащабно", "Continuous", 13, 7],
    "113": ["Дига изразена мащабно", "Continuous", 13, 7],
    "114": ["Мост железен каменен или стоманобетонен", "Continuous", 13, 7],
    "115": ["Мостдървен", "Continuous", 13, 7],
    "116": ["Висящ мост за пешеходци", "Continuous", 13, 7],
    "117": ["Брод", "Continuous", 13, 7],
    "118": ["Пристанищна стена", "Continuous", 13, 7],
    "119": ["Вълнолом", "Continuous", 13, 7],
    "120": ["Вълнолом", "Continuous", 13, 7],
    "121": ["Водопад", "Continuous", 13, 7],
    "130": ["Държавна граница", "Continuous", 13, 7],
    "131": ["Граница на област", "Continuous", 13, 7],
    "132": ["Граница на окръг", "Continuous", 13, 7],
    "133": ["Граница на община", "Continuous", 13, 7],
    "134": ["Кметство", "Continuous", 13, 7],
    "135": ["Землище", "Continuous", 13, 7],
    "136": ["Граница на административен район", "Continuous", 13, 7],
    "137": ["Стопанска граница", "Continuous", 13, 7],
    "138": ["Резерват", "Continuous", 13, 7],
    "139": ["Граница на растителна покривка", "Continuous", 13, 7],
    "140": ["Масивна ограда", "Continuous", 13, 7],
    "141": ["Масивна ограда обща", "Continuous", 13, 7],
    "142": ["Полумасивна ограда", "Continuous", 13, 7],
    "143": ["Полумасивна ограда обща", "Continuous", 13, 7],
    "144": ["Паянтова ограда", "Continuous", 13, 7],
    "145": ["Паянтова ограда обща", "Continuous", 13, 7],
    "146": ["Граница нематериализирана", "Continuous", 13, 7],
    "147": ["Граница спорна", "Continuous", 13, 7],
    "148": ["Тесни горски пояси", "Continuous", 13, 7],
    "149": ["Тясна ивица гора", "Continuous", 13, 7],
    "150": ["Тясна ивица храсти", "Continuous", 13, 7],
    "151": ["Вал", "Continuous", 13, 7],
    "152": ["Просека в гора", "Continuous", 13, 7],
    "153": ["Основен хоризонтал", "Continuous", 13, 7],
    "154": ["Удебелен хоризонтал", "Continuous", 13, 7],
    "155": ["Допълнителен хоризонтал", "Continuous", 13, 7],
    "156": ["Спомагателен хоризонтал", "Continuous", 13, 7],
    "157": ["Бергщрих", "Continuous", 13, 7],
    "158": ["Обрив почвен", "Continuous", 13, 7],
    "159": ["Слог", "Continuous", 13, 7],
    "160": ["Изкуствена тераса", "Continuous", 13, 7],
    "161": ["Закрепен свличащ се терен", "Continuous", 13, 7],
    "171": ["Граница на сервитут", "Continuous", 13, 7],
    "175": ["Вътрешна рамка на планов лист", "Continuous", 13, 7],
    "176": ["Граница на кадастрален район", "Continuous", 13, 7],
    "177": ["Граница на кадастрален район през улица", "Continuous", 13, 7],
    "178": ["Граница на улична отсечка", "DOT2", 20, 7],
    "188": ["Подземна или надземна сграда", "Continuous", 13, 7],
    "499": ["Граница на защитена територия", "Continuous", 13, 7]
}
