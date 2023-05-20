# подключение библиотек
# В google colab добавить: !pip install pyTelegramBotAPI
# для установки необходимо в файл requirements.text добавить строку
# 'PyTelegramBotApi'

from telebot import TeleBot, types
import random


bot = TeleBot(token='6078951158:AAGFkTEqSwDjgoqxKmtsu_WWjTvIEk6s0Vs', parse_mode='html') # создание бота

#библиотека с книгами по жанрам:
classics_list = ["М.А. Булгаков \nМастер и Маргарита\nhttps://www.labirint.ru/books/361610/\nили\nСобачье сердце\nhttps://www.labirint.ru/books/408558/", "Д. Остен \nЭмма\nhttps://www.labirint.ru/books/805101/\nили\nДоводы рассудка\nhttps://www.labirint.ru/books/704040/", "Т. Капоте\nГолоса травы\nhttps://www.livelib.ru/book/1000328136-golosa-travy-sbornik-trumen-kapote\nили\nЗавтрак у Тиффани\nhttps://fantlab.ru/edition53003", "И.А. Бунин\nГражданин из Сан-Франциско\nhttps://www.labirint.ru/books/647660/", "Г.Г. Маркес\nОсень патриарха\nhttps://www.labirint.ru/books/920735/\nили\nСто лет одиночества\nhttps://www.labirint.ru/books/463785/", "А.С. Пушкин\nПовести покойного Ивана Петровича Белкина\nhttps://www.labirint.ru/books/911516/\nили\nПиковая дама\nhttps://www.labirint.ru/books/721397/"]
modern_list = ["Л.Е. Улицкая\nМедея и ее дети\nhttps://www.labirint.ru/books/835450/\nили\nДаниэль Штайн, переводчик\nhttps://www.labirint.ru/books/814376/","Ф. Флэгг\nЖареные зеленые помидоры в кафе Полустанок\nhttps://www.labirint.ru/books/615013/","Ф. Бакман\nВторая жизнь Уве\nhttps://www.labirint.ru/books/835733/", "Д. Тартт\nЩегол\nhttps://www.labirint.ru/books/462781/", "Д.И. Рубина\nМаньяк Гуревич\nhttps://www.labirint.ru/books/850838/\nили\nВот идёт Мессия!\nhttps://www.labirint.ru/books/893760/", "Т.Н. Толстая\nКысь\nhttps://www.labirint.ru/books/489247/\nили\nРека Оккервиль\nhttps://www.labirint.ru/books/7947/"]
detective_list = ["Ж. Диккер\nПравда о деле Гарри Квеберта\nhttps://www.labirint.ru/books/599458/\nили\nЗагадка номера 622\nhttps://www.labirint.ru/books/790852/", "А. Кристи\nПосле похорон\nhttps://www.labirint.ru/books/699904/\nили\nУбийства по алфавиту\nhttps://www.labirint.ru/books/678492/", "А.К. Дойл\nЭтюд в багровых тонах\nhttps://www.labirint.ru/books/807827/\nили\nСобака Баскервилей\nhttps://www.labirint.ru/books/840284/", "Д. Браун\nКод да Винчи\nhttps://www.labirint.ru/books/549738/\nили\nПроисхождение\nhttps://www.labirint.ru/books/912413/", "Эдгар По\nУбийство на улице Морг\nhttps://www.labirint.ru/books/155036/", "Умберто Эко\nИмя розы\nhttps://www.labirint.ru/books/463786/"]
popular_sci_list = ["Р. Сапольски\nКто мы такие?\nhttps://alpinabook.ru/catalog/book-kto-my-takie/\nили\nБиология добра и зла\nhttps://alpinabook.ru/catalog/book-biologiya-dobra-i-zla/", "М. Элиаде\nАспекты мифа\nhttps://www.labirint.ru/books/938706/", "В.Я. Пропп\nИсторические корни волшебной сказки\nhttps://www.labirint.ru/books/863345/\nили\nМорфология волшебной сказки\nhttps://www.labirint.ru/books/860650/", "А.Ю. Панчин\nЗащита от темных искусств\nhttps://www.labirint.ru/books/635238/", "С. Хокинг\nКраткая история Времени\nhttps://www.labirint.ru/books/903610/", "Ю.Н. Харари\nSapiens\nhttps://www.labirint.ru/books/781273/"]
fantasy_list = ["Р.Р. Толкин\nХоббит, или Туда и обратно\nhttps://www.labirint.ru/books/417700/\nили\nтрилогия Властелин колец\nhttps://www.labirint.ru/books/524024/\nhttps://www.labirint.ru/books/524023/\nhttps://www.labirint.ru/books/524022/", "Т. Пратчетт\nСтража! Стража!\nhttps://www.labirint.ru/books/789570/\nили\nДержи марку!\nhttps://www.labirint.ru/books/527211/", "А. Сапковский\nВедьмак (Последнее желание)\nhttps://www.labirint.ru/books/571931/", "Н. Гейман\nБлагие знамения\nhttps://www.labirint.ru/books/943777/\nили\nНикогде\nhttps://www.labirint.ru/books/607637/", "Ф. Пулман\nСеверное сияние\nhttps://www.labirint.ru/books/525095/"]
sci_fi_list = ["Ф. Герберт\nДюна\nhttps://www.labirint.ru/books/875702/", "Б.Н. и А.Н. Стругацкие\nПикник на обочине\nhttps://www.labirint.ru/books/484897/\nили\nПонедельник начинается в субботу\nhttps://www.labirint.ru/books/486543/", "Р. Брэдбери\n451 градус по Фаренгейту\nhttps://www.labirint.ru/books/774021/", "С. Лем\nСолярис\nhttps://www.labirint.ru/books/592560/", "Дж. Оруэлл\n1984\nhttps://www.labirint.ru/books/419735/\nили\nСкотный двор\nhttps://www.labirint.ru/books/584142/"]
childhood_list = ["Т. Янссон\nОпасное лето\nhttps://www.labirint.ru/books/911861/\nили\nШляпа волшебника\nhttps://www.labirint.ru/books/911865/", "Дж.К. Роулинг\nГарри Поттер и Узник Азкабана\nhttps://www.labirint.ru/books/445211/\nили\nГарри Поттер и Дары смерти\nhttps://www.labirint.ru/books/481841/", "А.А. Милн\nВинни-Пух и все-все-все\nhttps://www.labirint.ru/books/535381/", "Л. Кэррол\nПриключения Алисы в Стране чудес\nhttps://www.labirint.ru/books/610751/", "Ю. Олеша\nТри толстяка\nhttps://www.labirint.ru/books/911301/", "А. Линдгрен\nПеппи Длинныйчулок\nhttps://www.labirint.ru/books/911590/\nили\nМалыш и Карлсон, который живет на крыше\nhttps://www.labirint.ru/books/517514/"]
horror_list = ["Б. Стокер\nДракула\nhttps://www.labirint.ru/books/935400/", "С. Кинг\nСияние\nhttps://www.labirint.ru/books/679419/\nили\nОно\nhttps://www.labirint.ru/books/860995/", "Н.В. Гоголь\nПортрет\nhttps://www.labirint.ru/books/112904/", "О. Уальд\nПортрет Дориана Грея\nhttps://www.labirint.ru/books/589212/", "Дж. Бром\nКрампус, Повелитель Йоля\nhttps://www.labirint.ru/books/649771/\nили\nПотерянные боги\nhttps://www.labirint.ru/books/609946/", "А. Райс\nИнтервью с вампиром\nhttps://www.labirint.ru/books/226696/"]
poetry_list = ["А.С. Пушкин\nМаленькие трагедии\nhttps://www.labirint.ru/books/729157/\nили\nРуслан и Людмила\nhttps://www.labirint.ru/books/882532/", "Л. А. Филатов\nПро Федота-стрельца, удалого молодца\nhttps://www.labirint.ru/books/583887/", "И. А. Бродский\nКонец прекрасной эпохи\nhttps://www.labirint.ru/books/841962/", "Гомер\nОдиссея\nили\nИлиада\nhttps://www.labirint.ru/books/918337/"]
choise_list = ["Что-то из современного? Может быть, классика? Выбери внизу👇🏻"]

# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("В метро, краем глаза👀")
    btn2 = types.KeyboardButton("Дома, сосредоточенно☕️")
    btn3 = types.KeyboardButton("На пляже, расслабленно☀️")
    btn4 = types.KeyboardButton("Ночами напролет, увлечённо🔥")
    btn5 = types.KeyboardButton("В перерыве на работе, деловито🤓")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, text="Добро пожаловать, {0.first_name}!❤️ Давай я помогу тебе выбрать книгу🤗\nДля начала определимся: где и как ты будешь читать?📚".format(message.from_user), reply_markup=markup)
    bot.send_video(message.chat.id, 'https://media1.giphy.com/media/toSMxU7Mguxnq/giphy.gif?cid=ecf05e47jgw7n0l7sanatki3sjwtjvtufwufwzw0o0xwow1m&ep=v1_gifs_search&rid=giphy.gif&ct=g', None, 'Text')

# обработчик всех остальных сообщений    
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "В метро, краем глаза👀"):
     bot.send_message(message.chat.id,"А какой жанр тебе нравится?\n\n{0}".format(random.choice(choise_list)))
     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
     btn1 = types.KeyboardButton("Классика🎩")
     btn2 = types.KeyboardButton("Современная проза🕶")
     btn3 = types.KeyboardButton("Детектив🔍")
     btn4 = types.KeyboardButton("Научпоп🔭")
     btn5 = types.KeyboardButton("Фентези🧙🏻‍♂️")
     btn5 = types.KeyboardButton("Фантастика🚀")
     markup.add(btn1, btn2, btn3, btn4, btn5)
     bot.send_photo(message.chat.id, open('ed101afe9055b244768d69d9e47a31ca.jpg', 'rb'), reply_markup=markup)


    elif(message.text == "Классика🎩"):
      bot.send_message(message.chat.id,"Предлагаю почитать:\n\n{0}".format(random.choice(classics_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Супер! Приступаю❤️")
      btn2 = types.KeyboardButton("Что еще есть в этом жанре?🎩")
      btn3 = types.KeyboardButton("Хочу вернуться в главное меню👆🏻")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="То, что нужно?", reply_markup=markup)

    elif message.text == "Что еще есть в этом жанре?🎩":
      bot.send_message(message.chat.id,"🙌🏻Тогда предлагаю почитать:\n\n{0}".format(random.choice(classics_list)))
      
    elif(message.text == "Современная проза🕶"):
      bot.send_message(message.chat.id,"Предлагаю почитать:\n\n{0}".format(random.choice(modern_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Супер! Приступаю❤️")
      btn2 = types.KeyboardButton("Что еще есть в этом жанре?🕶")
      btn3 = types.KeyboardButton("Хочу вернуться в главное меню👆🏻")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="То, что нужно?", reply_markup=markup)

    elif message.text == "Что еще есть в этом жанре?🕶":
      bot.send_message(message.chat.id,"🙌🏻Тогда предлагаю почитать:\n\n{0}".format(random.choice(modern_list)))
      
    elif(message.text == "Детектив🔍"):
      bot.send_message(message.chat.id,"Предлагаю почитать:\n\n{0}".format(random.choice(detective_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Супер! Приступаю❤️")
      btn2 = types.KeyboardButton("Что еще есть в этом жанре?🔍")
      btn3 = types.KeyboardButton("Хочу вернуться в главное меню👆🏻")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="То, что нужно?", reply_markup=markup)

    elif message.text == "Что еще есть в этом жанре?🔍":
      bot.send_message(message.chat.id,"🙌🏻Тогда предлагаю почитать:\n\n{0}".format(random.choice(detective_list)))
      
    elif(message.text == "Научпоп🔭"):
      bot.send_message(message.chat.id,"Предлагаю почитать:\n\n{0}".format(random.choice(popular_sci_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Супер! Приступаю❤️")
      btn2 = types.KeyboardButton("Что еще есть в этом жанре?🔭")
      btn3 = types.KeyboardButton("Хочу вернуться в главное меню👆🏻")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="То, что нужно?", reply_markup=markup)

    elif message.text == "Что еще есть в этом жанре?🔭":
      bot.send_message(message.chat.id,"🙌🏻Тогда предлагаю почитать:\n\n{0}".format(random.choice(popular_sci_list)))
      
    elif(message.text == "Фентези🧙🏻‍♂️"):
      bot.send_message(message.chat.id,"Предлагаю почитать:\n\n{0}".format(random.choice(fantasy_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Супер! Приступаю❤️")
      btn2 = types.KeyboardButton("Что еще есть в этом жанре?🧙🏻‍♂️")
      btn3 = types.KeyboardButton("Хочу вернуться в главное меню👆🏻")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="То, что нужно?", reply_markup=markup)

    elif message.text == "Что еще есть в этом жанре?🧙🏻‍♂️":
      bot.send_message(message.chat.id,"🙌🏻Тогда предлагаю почитать:\n\n{0}".format(random.choice(fantasy_list)))
      
    elif(message.text == "Фантастика🚀"):
      bot.send_message(message.chat.id,"Предлагаю почитать:\n\n{0}".format(random.choice(sci_fi_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Супер! Приступаю❤️")
      btn2 = types.KeyboardButton("Что еще есть в этом жанре?🚀")
      btn3 = types.KeyboardButton("Хочу вернуться в главное меню👆🏻")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="То, что нужно?", reply_markup=markup)

    elif message.text == "Что еще есть в этом жанре?🚀":
      bot.send_message(message.chat.id,"🙌🏻Тогда предлагаю почитать:\n\n{0}".format(random.choice(sci_fi_list)))
      
    elif(message.text == "Дома, сосредоточенно☕️"):
      bot.send_message(message.chat.id,"А какой жанр тебе нравится?\n\n{0}".format(random.choice(choise_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Назад в детство🧸")
      btn2 = types.KeyboardButton("Современная проза🕶")
      btn3 = types.KeyboardButton("Детектив🔍")
      btn4 = types.KeyboardButton("Классика🎩")
      btn5 = types.KeyboardButton("Триллер🪓")
      btn6 = types.KeyboardButton("Фентези🧙🏻‍♂️")
      btn7 = types.KeyboardButton("Фантастика🚀")
      btn8 = types.KeyboardButton("Поэзия✨")
      markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
      bot.send_photo(message.chat.id, open('shutterstock_225967033.jpg', 'rb'), reply_markup=markup)

    elif(message.text == "Назад в детство🧸"):
      bot.send_message(message.chat.id,"Предлагаю почитать:\n\n{0}".format(random.choice(childhood_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Супер! Приступаю❤️")
      btn2 = types.KeyboardButton("Что еще есть в этом жанре?🧸")
      btn3 = types.KeyboardButton("Хочу вернуться в главное меню👆🏻")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="То, что нужно?", reply_markup=markup)

    elif message.text == "Что еще есть в этом жанре?🧸":
      bot.send_message(message.chat.id,"🙌🏻Тогда предлагаю почитать:\n\n{0}".format(random.choice(childhood_list)))
          
    elif(message.text == "Современная проза🕶"):
      bot.send_message(message.chat.id,"Предлагаю почитать:\n\n{0}".format(random.choice(modern_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Супер! Приступаю❤️")
      btn2 = types.KeyboardButton("Что еще есть в этом жанре?🕶")
      btn3 = types.KeyboardButton("Хочу вернуться в главное меню👆🏻")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="То, что нужно?", reply_markup=markup)

    elif message.text == "Что еще есть в этом жанре?🕶":
      bot.send_message(message.chat.id,"🙌🏻Тогда предлагаю почитать:\n\n{0}".format(random.choice(modern_list)))
      
    elif(message.text == "Детектив🔍"):
      bot.send_message(message.chat.id,"Предлагаю почитать:\n\n{0}".format(random.choice(detective_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Супер! Приступаю❤️")
      btn2 = types.KeyboardButton("Что еще есть в этом жанре?🔍")
      btn3 = types.KeyboardButton("Хочу вернуться в главное меню👆🏻")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="То, что нужно?", reply_markup=markup)

    elif message.text == "Что еще есть в этом жанре?🔍":
      bot.send_message(message.chat.id,"🙌🏻Тогда предлагаю почитать:\n\n{0}".format(random.choice(detective_list)))
      
    elif(message.text == "Классика🎩"):
      bot.send_message(message.chat.id,"Предлагаю почитать:\n\n{0}".format(random.choice(classics_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Супер! Приступаю❤️")
      btn2 = types.KeyboardButton("Что еще есть в этом жанре?🎩")
      btn3 = types.KeyboardButton("Хочу вернуться в главное меню👆🏻")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="То, что нужно?", reply_markup=markup)

    elif message.text == "Что еще есть в этом жанре?🎩":
      bot.send_message(message.chat.id,"🙌🏻Тогда предлагаю почитать:\n\n{0}".format(random.choice(classics_list)))
      
    elif(message.text == "Триллер🪓"):
      bot.send_message(message.chat.id,"Предлагаю почитать:\n\n{0}".format(random.choice(horror_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Супер! Приступаю❤️")
      btn2 = types.KeyboardButton("Что еще есть в этом жанре?🪓")
      btn3 = types.KeyboardButton("Хочу вернуться в главное меню👆🏻")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="То, что нужно?", reply_markup=markup)

    elif message.text == "Что еще есть в этом жанре?🪓":
      bot.send_message(message.chat.id,"🙌🏻Тогда предлагаю почитать:\n\n{0}".format(random.choice(horror_list)))
          
    elif(message.text == "Фентези🧙🏻‍♂️"):
      bot.send_message(message.chat.id,"Предлагаю почитать:\n\n{0}".format(random.choice(fantasy_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Супер! Приступаю❤️")
      btn2 = types.KeyboardButton("Что еще есть в этом жанре?🧙🏻‍♂️")
      btn3 = types.KeyboardButton("Хочу вернуться в главное меню👆🏻")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="То, что нужно?", reply_markup=markup)

    elif message.text == "Что еще есть в этом жанре?🧙🏻‍♂️":
      bot.send_message(message.chat.id,"🙌🏻Тогда предлагаю почитать:\n\n{0}".format(random.choice(fantasy_list)))
      
    elif(message.text == "Фантастика🚀"):
      bot.send_message(message.chat.id,"Предлагаю почитать:\n\n{0}".format(random.choice(sci_fi_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Супер! Приступаю❤️")
      btn2 = types.KeyboardButton("Что еще есть в этом жанре?🚀")
      btn3 = types.KeyboardButton("Хочу вернуться в главное меню👆🏻")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="То, что нужно?", reply_markup=markup)

    elif message.text == "Что еще есть в этом жанре?🚀":
      bot.send_message(message.chat.id,"🙌🏻Тогда предлагаю почитать:\n\n{0}".format(random.choice(sci_fi_list)))
          
    elif(message.text == "Поэзия✨"):
      bot.send_message(message.chat.id,"Предлагаю почитать:\n\n{0}".format(random.choice(poetry_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Супер! Приступаю❤️")
      btn2 = types.KeyboardButton("Что еще есть в этом жанре?✨")
      btn3 = types.KeyboardButton("Хочу вернуться в главное меню👆🏻")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="То, что нужно?", reply_markup=markup)

    elif message.text == "Что еще есть в этом жанре?✨":
      bot.send_message(message.chat.id,"🙌🏻Тогда предлагаю почитать:\n\n{0}".format(random.choice(poetry_list)))
      
    elif(message.text == "На пляже, расслабленно☀️"):
      bot.send_message(message.chat.id,"А какой жанр тебе нравится?\n\n{0}".format(random.choice(choise_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Современная проза🕶")
      btn2 = types.KeyboardButton("Классика🎩")
      btn3 = types.KeyboardButton("Детектив🔍")
      btn4 = types.KeyboardButton("Фентези🧙🏻‍♂️")
      btn5 = types.KeyboardButton("Фантастика🚀")
      btn6 = types.KeyboardButton("Поэзия✨")
      markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
      bot.send_photo(message.chat.id, open('reading_a_letter_on_the_beach_rtp_0.jpg', 'rb'), reply_markup=markup)
      
    
    elif(message.text == "Современная проза🕶"):
      bot.send_message(message.chat.id,"Предлагаю почитать:\n\n{0}".format(random.choice(modern_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Супер! Приступаю❤️")
      btn2 = types.KeyboardButton("Что еще есть в этом жанре?🕶")
      btn3 = types.KeyboardButton("Хочу вернуться в главное меню👆🏻")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="То, что нужно?", reply_markup=markup)

    elif message.text == "Что еще есть в этом жанре?🕶":
      bot.send_message(message.chat.id,"🙌🏻Тогда предлагаю почитать:\n\n{0}".format(random.choice(modern_list)))
          
    elif(message.text == "Классика🎩"):
      bot.send_message(message.chat.id,"Предлагаю почитать:\n\n{0}".format(random.choice(classics_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Супер! Приступаю❤️")
      btn2 = types.KeyboardButton("Что еще есть в этом жанре?🎩")
      btn3 = types.KeyboardButton("Хочу вернуться в главное меню👆🏻")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="То, что нужно?", reply_markup=markup)

    elif message.text == "Что еще есть в этом жанре?🎩":
      bot.send_message(message.chat.id,"🙌🏻Тогда предлагаю почитать:\n\n{0}".format(random.choice(classics_list)))
      
    elif(message.text == "Детектив🔍"):
      bot.send_message(message.chat.id,"Предлагаю почитать:\n\n{0}".format(random.choice(detective_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Супер! Приступаю❤️")
      btn2 = types.KeyboardButton("Что еще есть в этом жанре?🔍")
      btn3 = types.KeyboardButton("Хочу вернуться в главное меню👆🏻")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="То, что нужно?", reply_markup=markup)

    elif message.text == "Что еще есть в этом жанре?🔍":
      bot.send_message(message.chat.id,"🙌🏻Тогда предлагаю почитать:\n\n{0}".format(random.choice(detective_list)))
      
    elif(message.text == "Фентези🧙🏻‍♂️"):
      bot.send_message(message.chat.id,"Предлагаю почитать:\n\n{0}".format(random.choice(fantasy_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Супер! Приступаю❤️")
      btn2 = types.KeyboardButton("Что еще есть в этом жанре?🧙🏻‍♂️")
      btn3 = types.KeyboardButton("Хочу вернуться в главное меню👆🏻")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="То, что нужно?", reply_markup=markup)

    elif message.text == "Что еще есть в этом жанре?🧙🏻‍♂️":
      bot.send_message(message.chat.id,"🙌🏻Тогда предлагаю почитать:\n\n{0}".format(random.choice(fantasy_list)))
      
    elif(message.text == "Фантастика🚀"):
      bot.send_message(message.chat.id,"Предлагаю почитать:\n\n{0}".format(random.choice(sci_fi_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Супер! Приступаю❤️")
      btn2 = types.KeyboardButton("Что еще есть в этом жанре?🚀")
      btn3 = types.KeyboardButton("Хочу вернуться в главное меню👆🏻")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="То, что нужно?", reply_markup=markup)

    elif message.text == "Что еще есть в этом жанре?🚀":
      bot.send_message(message.chat.id,"🙌🏻Тогда предлагаю почитать:\n\n{0}".format(random.choice(sci_fi_list)))
          
    elif(message.text == "Поэзия✨"):
      bot.send_message(message.chat.id,"Предлагаю почитать:\n\n{0}".format(random.choice(poetry_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Супер! Приступаю❤️")
      btn2 = types.KeyboardButton("Что еще есть в этом жанре?✨")
      btn3 = types.KeyboardButton("Хочу вернуться в главное меню👆🏻")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="То, что нужно?", reply_markup=markup)

    elif message.text == "Что еще есть в этом жанре?✨":
      bot.send_message(message.chat.id,"🙌🏻Тогда предлагаю почитать:\n\n{0}".format(random.choice(poetry_list)))
      
    elif(message.text == "Ночами напролет, увлечённо🔥"):
      bot.send_message(message.chat.id,"А какой жанр тебе нравится?\n\n{0}".format(random.choice(choise_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Назад в детство🧸")
      btn2 = types.KeyboardButton("Современная проза🕶")
      btn3 = types.KeyboardButton("Детектив🔍")
      btn4 = types.KeyboardButton("Триллер🪓")
      btn5 = types.KeyboardButton("Фентези🧙🏻‍♂️")
      btn6 = types.KeyboardButton("Фантастика🚀")
      markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
      bot.send_photo(message.chat.id, open('full-size-render-3.jpg', 'rb'), reply_markup=markup)
      
    elif(message.text == "Назад в детство🧸"):
      bot.send_message(message.chat.id,"Предлагаю почитать:\n\n{0}".format(random.choice(childhood_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Супер! Приступаю❤️")
      btn2 = types.KeyboardButton("Что еще есть в этом жанре?🧸")
      btn3 = types.KeyboardButton("Хочу вернуться в главное меню👆🏻")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="То, что нужно?", reply_markup=markup)

    elif message.text == "Что еще есть в этом жанре?🧸":
      bot.send_message(message.chat.id,"🙌🏻Тогда предлагаю почитать:\n\n{0}".format(random.choice(childhood_list)))
          
    elif(message.text == "Современная проза🕶"):
      bot.send_message(message.chat.id,"Предлагаю почитать:\n\n{0}".format(random.choice(modern_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Супер! Приступаю❤️")
      btn2 = types.KeyboardButton("Что еще есть в этом жанре?🕶")
      btn3 = types.KeyboardButton("Хочу вернуться в главное меню👆🏻")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="То, что нужно?", reply_markup=markup)

    elif message.text == "Что еще есть в этом жанре?🕶":
      bot.send_message(message.chat.id,"🙌🏻Тогда предлагаю почитать:\n\n{0}".format(random.choice(modern_list)))

    elif(message.text == "Детектив🔍"):
      bot.send_message(message.chat.id,"Предлагаю почитать:\n\n{0}".format(random.choice(detective_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Супер! Приступаю❤️")
      btn2 = types.KeyboardButton("Что еще есть в этом жанре?🔍")
      btn3 = types.KeyboardButton("Хочу вернуться в главное меню👆🏻")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="То, что нужно?", reply_markup=markup)

    elif message.text == "Что еще есть в этом жанре?🔍":
      bot.send_message(message.chat.id,"🙌🏻Тогда предлагаю почитать:\n\n{0}".format(random.choice(detective_list)))

    elif(message.text == "Триллер🪓"):
      bot.send_message(message.chat.id,"Предлагаю почитать:\n\n{0}".format(random.choice(horror_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Супер! Приступаю❤️")
      btn2 = types.KeyboardButton("Что еще есть в этом жанре?🪓")
      btn3 = types.KeyboardButton("Хочу вернуться в главное меню👆🏻")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="То, что нужно?", reply_markup=markup)

    elif message.text == "Что еще есть в этом жанре?🪓":
      bot.send_message(message.chat.id,"🙌🏻Тогда предлагаю почитать:\n\n{0}".format(random.choice(horror_list)))

    elif(message.text == "Фентези🧙🏻‍♂️"):
      bot.send_message(message.chat.id,"Предлагаю почитать:\n\n{0}".format(random.choice(fantasy_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Супер! Приступаю❤️")
      btn2 = types.KeyboardButton("Что еще есть в этом жанре?🧙🏻‍♂️")
      btn3 = types.KeyboardButton("Хочу вернуться в главное меню👆🏻")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="То, что нужно?", reply_markup=markup)

    elif message.text == "Что еще есть в этом жанре?🧙🏻‍♂️":
      bot.send_message(message.chat.id,"🙌🏻Тогда предлагаю почитать:\n\n{0}".format(random.choice(fantasy_list)))

    elif(message.text == "Фантастика🚀"):
      bot.send_message(message.chat.id,"Предлагаю почитать:\n\n{0}".format(random.choice(sci_fi_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Супер! Приступаю❤️")
      btn2 = types.KeyboardButton("Что еще есть в этом жанре?🚀")
      btn3 = types.KeyboardButton("Хочу вернуться в главное меню👆🏻")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="То, что нужно?", reply_markup=markup)

    elif message.text == "Что еще есть в этом жанре?🚀":
      bot.send_message(message.chat.id,"🙌🏻Тогда предлагаю почитать:\n\n{0}".format(random.choice(sci_fi_list)))
    
    elif(message.text == "В перерыве на работе, деловито🤓"):
      bot.send_message(message.chat.id,"А какой жанр тебе нравится?\n\n{0}".format(random.choice(choise_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Научпоп🔭")
      btn2 = types.KeyboardButton("Современная проза🕶")
      btn3 = types.KeyboardButton("Детектив🔍")
      btn4 = types.KeyboardButton("Классика🎩")
      markup.add(btn1, btn2, btn3, btn4)
      bot.send_photo(message.chat.id, open('15336491311194485940_a24713f14c42d62f198ead58ce43d3ce.jpg', 'rb'), reply_markup=markup)

    elif(message.text == "Научпоп🔭"):
      bot.send_message(message.chat.id,"Предлагаю почитать:\n\n{0}".format(random.choice(popular_sci_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Супер! Приступаю❤️")
      btn2 = types.KeyboardButton("Что еще есть в этом жанре?🔭")
      btn3 = types.KeyboardButton("Хочу вернуться в главное меню👆🏻")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="То, что нужно?", reply_markup=markup)

    elif message.text == "Что еще есть в этом жанре?🔭":
      bot.send_message(message.chat.id,"🙌🏻Тогда предлагаю почитать:\n\n{0}".format(random.choice(popular_sci_list)))

    elif(message.text == "Современная проза🕶"):
      bot.send_message(message.chat.id,"Предлагаю почитать:\n\n{0}".format(random.choice(modern_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Супер! Приступаю❤️")
      btn2 = types.KeyboardButton("Что еще есть в этом жанре?🕶")
      btn3 = types.KeyboardButton("Хочу вернуться в главное меню👆🏻")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="То, что нужно?", reply_markup=markup)

    elif message.text == "Что еще есть в этом жанре?🕶":
      bot.send_message(message.chat.id,"🙌🏻Тогда предлагаю почитать:\n\n{0}".format(random.choice(modern_list)))

    elif(message.text == "Детектив🔍"):
      bot.send_message(message.chat.id,"Предлагаю почитать:\n\n{0}".format(random.choice(detective_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Супер! Приступаю❤️")
      btn2 = types.KeyboardButton("Что еще есть в этом жанре?🔍")
      btn3 = types.KeyboardButton("Хочу вернуться в главное меню👆🏻")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="То, что нужно?", reply_markup=markup)

    elif message.text == "Что еще есть в этом жанре?🔍":
      bot.send_message(message.chat.id,"🙌🏻Тогда предлагаю почитать:\n\n{0}".format(random.choice(detective_list)))
    
    elif(message.text == "Классика🎩"):
      bot.send_message(message.chat.id,"Предлагаю почитать:\n\n{0}".format(random.choice(classics_list)))
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn1 = types.KeyboardButton("Супер! Приступаю❤️")
      btn2 = types.KeyboardButton("Что еще есть в этом жанре?🎩")
      btn3 = types.KeyboardButton("Хочу вернуться в главное меню👆🏻")
      markup.add(btn1, btn2, btn3)
      bot.send_message(message.chat.id,text="То, что нужно?", reply_markup=markup)

    elif message.text == "Что еще есть в этом жанре?🎩":
      bot.send_message(message.chat.id,"🙌🏻Тогда предлагаю почитать:\n\n{0}".format(random.choice(classics_list)))
  
    elif(message.text == "Супер! Приступаю❤️"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("/start")
        markup.add(btn1)
        bot.send_message(message.chat.id,text="Рад помочь!🥰", reply_markup=markup)
        bot.send_video(message.chat.id, 'https://media4.giphy.com/media/diUKszNTUghVe/giphy.gif?cid=ecf05e47290m1afu7tf3v9zl8g3pzasy2541ghe07ejsignj&ep=v1_gifs_search&rid=giphy.gif&ct=g', None, 'Text')
    
    elif (message.text == "Хочу вернуться в главное меню👆🏻"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("В метро, краем глаза👀")
        btn2 = types.KeyboardButton("Дома, сосредоточенно☕️")
        btn3 = types.KeyboardButton("На пляже, расслабленно☀️")
        btn4 = types.KeyboardButton("Ночами напролет, увлечённо🔥")
        btn5 = types.KeyboardButton("В перерыве на работе, деловито🤓")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, text="Попробуем еще раз с начала🧐\nИтак, где и как ты будешь читать?", reply_markup=markup)
        bot.send_video(message.chat.id, 'https://media3.giphy.com/media/VcizxCUIgaKpa/giphy.gif?cid=ecf05e47k6d33ravczpklkz0h7aw77jns18ssc49ld4dmd7o&ep=v1_gifs_search&rid=giphy.gif&ct=g', None, 'Text')
    else:
        bot.send_message(message.chat.id, text="Не понимаю, что это значит😟")


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()