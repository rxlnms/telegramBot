import telebot
from telebot import types

bot = telebot.TeleBot('7533322099:AAFewbI-eKS9_TxRDV8sf2UzjBclPBISPVM')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Ссылка на важный вопрос')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Музыка')
    markup.row(btn2)
    btn3 = types.KeyboardButton('Идеи для свиданий')
    markup.row(btn3)
    btn4 = types.KeyboardButton('Моменты')
    markup.row(btn4)
    bot.send_message(message.chat.id, f'Приветик, {message.from_user.first_name}! Этот бот сделан для тебя в честь дня Святого Валентина. Сделано с душой и самыми искренними чувствами. Зацени мой гений.', reply_markup=markup)
    file = open('./photo.jpeg', 'rb')
    bot.send_photo(message.chat.id, file)


@bot.message_handler(func=lambda message: message.text == 'Ссылка на важный вопрос')
def send_q(message):
    question = (
        "<b>На этом сайте ты должна будешь ответить на важный вопрос</b>\n"
        "https://rxlnms.github.io/valentine/"
    )
    bot.send_message(message.chat.id, question, parse_mode="HTML")


@bot.message_handler(func=lambda message: message.text == 'Музыка')
def send_audio(message):
    audio = open('Sabira.m4a', 'rb')
    bot.send_audio(message.chat.id, audio, caption='Эту песню я сочинила для тебя, чтобы показать свои чувства')
    audio.close()


@bot.message_handler(func=lambda message: message.text == 'Идеи для свиданий')
def date_ideas(message):
    ideas = (
        "<b>Идеи для свиданий</b>\n"
        "1. Гончарка\n"
        "2. Теннис\n"
        "3. Лего-дейт\n"
        "4. Аркады\n"
        "5. Обсерватория\n"
        "6. Кукинг-дейт\n"
        "7. Пластилин-дейт\n"
        "8. Каток\n"
        "9. Компьютерные игры\n"
        "10. Совместный просмотр фильмов"
    )
    bot.send_message(message.chat.id, ideas, parse_mode='HTML')


@bot.message_handler(func=lambda message: message.text == 'Моменты')
def moments(message):
    photo1 = open('moment1.jpg', 'rb')
    bot.send_photo(message.chat.id, photo1, caption='11 августа 2024 года ты позвала меня гулять. Наша первая прогулка была на следующий день - 12 августа.')
    photo2 = open('BigApple.JPG', 'rb')
    bot.send_photo(message.chat.id, photo2, caption='Один из ярких первых наших моментов - твой кофе. Мне кофе не нравится, но только твой пить я готова постоянно')
    video1 = open('ittt1.MOV', 'rb')
    bot.send_video(message.chat.id, video1, caption='Тут наш первый опыт в совместных играх. Ты такой нубасик хахаха, но все равно моя гордость')
    photo3 = open('gagarin.jpg', 'rb')
    bot.send_photo(message.chat.id, photo3, caption='Здесь мы гуляли возле моего дома и я попросила тебя сфоткаться с Гагариным')
    video2 = open('baby.MOV', 'rb')
    bot.send_video(message.chat.id, video2, caption='А тут я напросилась снять с тобой тот тред из тиктока')
    photo4 = open('11october.jpg', 'rb')
    bot.send_photo(message.chat.id, photo4, caption='11 октября. В этот день я предложила тебе встречаться и это первая сделанная мною фотка будучи в отношениях')
    photo5 = open('birthday.jpg', 'rb')
    bot.send_photo(message.chat.id, photo5, caption='Хоть я и не смогла тебя поздравить с днем рождения должным образом, я хотела, чтобы ты хотя бы была рада моим цветам. Я заставила тупо всех работать (заслуженно)')
    photo6 = open('little_brazil.HEIC', 'rb')
    bot.send_photo(message.chat.id, photo6, caption='Здесь я позвала тебя в Литл Бразил отметить твой день рождения. На фото ты такая недовольная, потому что не хотела фотографироваться. Очень жаль, ведь я люблю тебя фоткать. Я обожаю каждую твою фотографию и готова пересматривать их вечно')
    photo7 = open('golden_apple.jpg', 'rb')
    bot.send_photo(message.chat.id, photo7, caption='Мое любимое золотое яблоко... Я готова туда только с тобой ходить. Это по-настоящему гиблое место...')
    photo8 = open('brawl.jpg', 'rb')
    bot.send_photo(message.chat.id, photo8, caption='Одно из самых моих любимых времяпроводждений с тобой. Люблю играть в бравл с тобой. Ты ж мой нубасик на Шелли 😘')
    photo9 = open('ball.jpg', 'rb')
    bot.send_photo(message.chat.id, photo9, caption='ЗИМНИЙ БАЛ С МОЕЙ САБИРОЧКОЙ!!! Ужасный бал, но я рада, что была там именно с тобой. Хоть один школьный момент я смогла разделить с тобой')
    photo10 = open('mega.jpg', 'rb')
    bot.send_photo(message.chat.id, photo10, caption='ТУТ Я НАКОНЕЦ-ТО СМОГЛА ТЕБЯ СФОТКАТЬ У ЕЛКИ 😍 Ничего лучше я не видела. Идеальный новый год. Идеальные новогодние выходные')
    photo11 = open('funny.jpg', 'rb')
    bot.send_photo(message.chat.id, photo11, caption='Я плохо помню ту ночь, но я хорошо помню, как добавила именно эту фотку в избранные. Ты тут такая забавная 😘')
    photo12 = open('drunk.jpg', 'rb')
    bot.send_photo(message.chat.id, photo12, caption='Мне эта фотка просто нравится хахаха')


@bot.message_handler(commands=['site'])
def site(message):
    send_s = (
        "<b>Вот тут ссылка на твой сайт, чтобы ты его долго не искала:</b>\n"
        "https://rxlnms.github.io/love/"
    )
    bot.send_message(message.chat.id, send_s, parse_mode='HTML')


@bot.message_handler(commands=['help'])
def desc(message):
    bot.send_message(message.chat.id, f'{message.from_user.first_name}, по этому боту ты можешь все понять из названия. Сюда ты можешь отправлять свои фотографии, а еще пользоваться его функциями. Считай это твой мини-проводник. Я добавила функцию сайта, чтобы ты всегда могла иметь прямой доступ к нему и не искала ссылку на телефоне. Если есть, что добавить, то пиши мне, и я сделаю все в пределах своих возможностей (ну и в пределах возможностей телеграма)')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn2 = types.InlineKeyboardButton('Новое сообщение', callback_data='edit')
    markup.row(btn1, btn2)
    bot.reply_to(message, 'Какое красиво фото!', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Восхитительное фото! Просто чудесно!', callback.message.chat.id, callback.message.message_id)


bot.infinity_polling(none_stop=True)