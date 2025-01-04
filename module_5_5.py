import hashlib
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age

    def hash_password(self, password):
        """Возвращает хэш от пароля."""
        return hashlib.sha256(password.encode()).hexdigest()

    def __str__(self):
        return f"User(nickname={self.nickname}, age={self.age})"

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return f"Video(title={self.title}, duration={self.duration}, adult_mode={self.adult_mode})"

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        """Вход пользователя."""
        for user in self.users:
            if user.nickname == nickname and user.password == user.hash_password(password):
                self.current_user = user
                return f"Добро пожаловать, {nickname}!"
        return "Неверные данные для входа."

    def register(self, nickname, password, age):
        """Регистрация пользователя."""
        if any(user.nickname == nickname for user in self.users):
            return f"Пользователь {nickname} уже существует"
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.log_in(nickname, password)  # Вход после регистрации
        return f"Пользователь {nickname} успешно зарегистрирован"

    def log_out(self):
        """Выход пользователя."""
        self.current_user = None

    def add(self, *videos):
        """Добавление видео."""
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search_word):
        """Поиск видео по ключевому слову."""
        search_word = search_word.lower()
        return [video.title for video in self.videos if search_word in video.title.lower()]

    def watch_video(self, title):
        """Просмотр видео."""
        if not self.current_user:
            return "Войдите в аккаунт, чтобы смотреть видео"

        video = next((v for v in self.videos if v.title == title), None)
        if not video:
            return "Видео не найдено"

        if video.adult_mode and self.current_user.age < 18:
            return "Вам нет 18 лет, пожалуйста покиньте страницу"

        while video.time_now < video.duration:
            print(video.time_now + 1)
            video.time_now += 1
            time.sleep(1)

        video.time_now = 0
        return "Конец видео"

# Тестирование:

ur = UrTube()

# Добавление видео
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
print(ur.watch_video('Для чего девушкам парень программист?'))
print(ur.register('vasya_pupkin', 'lolkekcheburek', 13))
print(ur.watch_video('Для чего девушкам парень программист?'))
print(ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25))
print(ur.watch_video('Для чего девушкам парень программист?'))

# Проверка входа в другой аккаунт
print(ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55))
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
print(ur.watch_video('Лучший язык программирования 2024 года!'))
