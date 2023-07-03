from moviepy.editor import *
from django.conf import settings


def generate_ticker(text: str):
    """
    Function receives input string, creates ticker and renders it into video clip in format .mp4"
    """
    duration = 3  # длительность видео в секундах
    size = 100, 100  # размер видео
    fps = 36  # количество кадров в секунду

    # Создаем текстовый клип, чтобы добавить текстовую надпись на видео
    txt_clip = TextClip(text, fontsize=30, color='black')

    # Создаем клип с установленными параметрами
    txt_clip = txt_clip.set_position('center').set_duration(duration).set_fps(fps)

    # Создаем пустой клип заднего плана
    background_video_clip = ColorClip(size, color=(0, 255, 0)).set_duration(duration).set_fps(fps)

    # Анимируем текст
    text_length = len(text)*20
    txt_speed = text_length / duration
    txt_mov = txt_clip.set_position(lambda t: (100-(int(txt_speed * t)), 'center'))

    # Объединяем клипы
    final_video_clip = CompositeVideoClip([background_video_clip, txt_mov])

    # Рендерим видео
    file_path = os.path.join(settings.MEDIA_ROOT, 'ticker.mp4')
    final_video_clip.write_videofile(file_path, fps=fps)

    return file_path


if __name__ == '__main__':
    generate_ticker(input())

