# https://youtu.be/8ygQtUA_SxM
# https://youtu.be/KSD0Zuyju4E

from pytube import YouTube


def save_captions(link, lang):
    yt = YouTube(link)
    caption = yt.captions.get_by_language_code(lang)
    caption_text = caption.generate_srt_captions()
    video_name = yt.title
    str_video_name = str(video_name)
    str_file_name_clean = "".join(
        c for c in str_video_name if c.isalpha() or c.isspace())  # удаляем все кроме букв и пробелов
    file_name = str_file_name_clean.replace(" ", "_")  # заменяем пробелы подчеркиваниями

    with open(f'{file_name}_{lang}.txt', 'w') as file:
        file.write(yt.author)
        file.write('\n')
        file.write(yt.channel_url)
        file.write('\n')
        file.write(yt.title)
        file.write('\n')
        file.write(yt.watch_url)
        file.write('\n')
        file.write('*' * 79)
        file.write('\n')
        for line in caption_text:
            file.write(line)

    print("Не обращай внимания на ошибку - успех наступил!")


def get_available_captions(link):
    yt = YouTube(link)
    print(f"Для видео '{yt.title}' доступны субтитры: ")
    code_list = []  # временный список
    a = yt.captions.lang_code_index  # сохраняем только коды
    for i in a.keys():
        code_list.append(i)

    # code_dict = {code_list[i]: i+1 for i in range(0, len(code_list),1)}
    code_dict = {code: it for it, code in enumerate(code_list)}  # создаем словарь из списка
    rev_code_dict = {v: k for k, v in code_dict.items()}  # переворачиваем словарь
    for key in rev_code_dict:
        print(f"Для выбора '{rev_code_dict[key]}' - введите {key}")

    choose = int(input("Ваш выбор: "))
    chosen_code = rev_code_dict[choose]
    return chosen_code


def main():
    link = input("Please enter link for video: ")
    lang = get_available_captions(link=link)
    save_captions(link=link, lang=lang)


if __name__ == "__main__":
    main()
