"""
Модуль инструкции для автоподписки
Содержит функции для отображения подробной инструкции по использованию раздела "Автоподписка".
"""

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_autosubscribe_instruction_text(language: str = "ru"):
    """
    Возвращает текст инструкции для автоподписки в зависимости от языка пользователя.
    RU — по умолчанию, EN — английский перевод.
    """
    lang = (language or "ru").strip().lower()

    if lang.startswith("en"):
        return (
            "<b>Subscription ➕</b>\n\n\n\n"
            "🔘 First, choose the account on which you want to run Auto-subscription to groups/chats/channels.\n\n"
            "🔘 After selecting a Telegram account in the section \"Select account for auto-subscription:\", you will move to the next section where you should send a list of @username or links like \"https://t.me/...\" to which the bot will automatically subscribe.\n\n"
            "🔘 Do not forward @username or links from \"Saved Messages\" or other chats. The @username or \"https://t.me/...\" links must be sent directly to the bot in this section by typing or pasting them. It's best to prepare the list in \"Saved Messages\" in advance, then copy and paste it here.\n"
            "Please note: the bot cannot solve CAPTCHAs for you due to Telegram API limitations.\n\n\n"
            "🔘 List format:\n\n"
            "❌ \n@username1, @username2, @username3 ...\n\n"
            "✅\n@username1\n@username2\n@username3\n\n\n"
            "🔘 After you send @username or \"https://t.me/...\" links, the auto-subscription service will start:\n"
            "- By pressing \"Back\" you will collapse this section and it will continue running in the background.\n"
            "- By pressing \"Finish\" you completely stop the \"Subscription ➕\" service."
        )

    return (
        "<b>Подписка ➕</b>\n\n\n\n"
        "🔘 В первую очередь вам нужно выбрать аккаунт, на котором вы хотите запустить сервис Автоподписки по группам/чатам/каналам.\n\n"
        "🔘 После выбора телеграмм аккаунта в разделе \"Выберите аккаунт для автоподписки:\" вы перемещаетесь в следующий раздел, где вам следует отправить список @username или ссылок в виде \"https://t.me/...\" на которые будет происходиться автоматическая подписка.\n\n"
        "🔘Не отправляйте в этом разделе @username или ссылки на чаты путём пересылания их из \"Избранное\" или других диалогов ― @username или ссылки \"https://t.me/...\" должны быть отправлены боту в этом разделе непосредственно вводом и отправкой сообщения. Поэтому, лучше всего заранее приготовить список в \"Избранное\", затем скопировать его и вставить в этот раздел.\n"
        "Учтите, что бот не в силах проходить капчи вместо вас. Это попросту невозможно в связи с Telegramp API ограничениями.\n\n\n"
        "🔘 Формат того, как должен выглядеть список:\n\n"
        "❌ \n@username1, @username2, @username3 ...\n\n"
        "✅\n@username1\n@username2\n@username3\n\n\n"
        "🔘 После ввода @username или ссылок \"https://t.me/...\", сервис автоподписки на чаты/каналы будет запущен:\n"
        "-Нажав кнопку \"Назад\" вы свернёте этот раздел и он будет работать в фоновом режиме.\n"
        "-Нажав кнопку \"Завершить\" и полностью прекращаете работу сервиса \"Подписка ➕\"."
    )


def get_autosubscribe_instruction_keyboard(language: str = "ru"):
    """
    Возвращает клавиатуру с кнопкой "Вернуться"/"Back" в зависимости от языка.
    """
    lang = (language or "ru").strip().lower()
    back_text = "Back 🔙" if lang.startswith("en") else "Вернуться 🔙"
    markup = InlineKeyboardMarkup(inline_keyboard=[])
    markup.inline_keyboard.append([
        InlineKeyboardButton(text=back_text, callback_data="instructions")
    ])
    return markup


async def send_autosubscribe_instruction(bot, chat_id, user_id=None, language="ru"):
    """
    Отправляет инструкцию по автоподписке пользователю согласно языку.
    """
    try:
        text = get_autosubscribe_instruction_text(language=language)
        keyboard = get_autosubscribe_instruction_keyboard(language=language)
        await bot.send_message(chat_id=chat_id, text=text, reply_markup=keyboard, parse_mode="HTML")
    except Exception:
        await bot.send_message(chat_id=chat_id, text="Инструкция по автоподписке временно недоступна.")


