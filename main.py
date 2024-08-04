class CinemaTicketSystem:
    def __init__(self):
        self.movies = {}
        self.users = {}
        self.tickets = {}
        self.movieIdCounter = 1
        self.userIdCounter = 1
        self.ticketIdCounter = 1

    def addMovie(self, movieName):
        movieId = self.movieIdCounter
        self.movies[movieId] = movieName
        self.movieIdCounter += 1
        print(f"Добавили фильм {movieName} с айди {movieId}")

    def showAllMovies(self):
        if self.movies:
            for id, name in self.movies.items():
                print(f"Фильм {name} под айди {id}")
        else:
            print("Фильмов пока нет, добавьте что-нибудь!")

    def addUser(self, userName):
        userId = self.userIdCounter
        self.users[userId] = userName
        self.userIdCounter += 1
        print(f"Пользователь {userName} теперь с нами, его айди {userId}")

    def buyTicket(self, userId, movieId):
        if userId in self.users and movieId in self.movies:
            ticketId = self.ticketIdCounter
            self.tickets[ticketId] = (userId, movieId)
            self.ticketIdCounter += 1
            print(f"Купил билет на {self.movies[movieId]}! Номер билета {ticketId}")
        else:
            print("Проверь айдишники")

    def cancelTicket(self, ticketId):
        if ticketId in self.tickets:
            print(f"Билет номер {ticketId} на {self.movies[self.tickets[ticketId][1]]} отменен, свободен!")
            del self.tickets[ticketId]
        else:
            print("Такого билета нет, проверь номер")


system = CinemaTicketSystem()
while True:
    print("\nЧего желаешь?")
    print("1. Добавить фильм")
    print("2. Показать все фильмы")
    print("3. Регистрация пользователя")
    print("4. Купить билет")
    print("5. Отменить билет")
    print("6. Я устал, я ухожу ...")
    choice = input("Ну, выбирай: ")
    if choice == '1':
        movieName = input("Как назовем фильм? ")
        system.addMovie(movieName)
    elif choice == '2':
        system.showAllMovies()
    elif choice == '3':
        userName = input("Как зовут пользователя? ")
        system.addUser(userName)
    elif choice == '4':
        userId = int(input("ID пользователя: "))
        movieId = int(input("ID фильма: "))
        system.buyTicket(userId, movieId)
    elif choice == '5':
        ticketId = int(input("ID билета: "))
        system.cancelTicket(ticketId)
    elif choice == '6':
        print("Адиос!")
        break
