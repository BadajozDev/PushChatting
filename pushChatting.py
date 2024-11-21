import os
import json
import sys
import time
from termcolor import colored
from pusher import Pusher
import pysher
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv(dotenv_path='.env')


class TerminalChat:
    def __init__(self):
        self.pusher = None
        self.clientPusher = None
        self.user = None
        self.users = {}  # Usuarios conectados
        self.chatrooms = ["sports", "general", "education", "health", "technology"]
        self.selected_chatroom = None
        self.initPusher()

    def initPusher(self):
        self.pusher = Pusher(
            app_id=os.getenv('PUSHER_APP_ID'),
            key=os.getenv('PUSHER_APP_KEY'),
            secret=os.getenv('PUSHER_APP_SECRET'),
            cluster=os.getenv('PUSHER_APP_CLUSTER')
        )
        self.clientPusher = pysher.Pusher(os.getenv('PUSHER_APP_KEY'), os.getenv('PUSHER_APP_CLUSTER'))
        self.clientPusher.connection.bind('pusher:connection_established', self.connectHandler)
        self.clientPusher.connect()

    def connectHandler(self, data):
        print(colored("✅ Conexión exitosa a Pusher.", "green"))
        self.listenForUsers()

    def listenForUsers(self):
        self.channel = self.clientPusher.subscribe('user-channel')
        self.channel.bind('user_connected', self.userConnected)
        self.channel.bind('user_disconnected', self.userDisconnected)

    def userConnected(self, message):
        user = json.loads(message)
        if user['username'] not in self.users:
            self.users[user['username']] = 'online'
            print(colored(f"🎉 ¡{user['username']} se ha conectado!", "green"))

    def userDisconnected(self, message):
        user = json.loads(message)
        if user['username'] in self.users:
            print(colored(f"⚠️ ¡{user['username']} se ha desconectado!", "red"))
            del self.users[user['username']]

    def login(self):
        self.clearScreen()
        username = input(colored("Por favor ingresa tu nombre de usuario: ", "yellow"))
        self.user = username
        self.registerUser()
        self.mainMenu()

    def registerUser(self):
        self.pusher.trigger('user-channel', 'user_connected', {'username': self.user})
        print(colored(f"✅ Usuario {self.user} registrado en Pusher.", "green"))

    def mainMenu(self):
        while True:
            self.clearScreen()
            print("\n📜 Menú:")
            print("[1] Mostrar usuarios conectados")
            print("[2] Mostrar chatrooms")
            print("[3] Salir")
            option = input(colored("Selecciona una opción: ", "yellow"))

            if option == "1":
                self.showUsers()
            elif option == "2":
                self.showChatrooms()
            elif option == "3":
                print(colored("👋 Saliendo del programa...", "red"))
                sys.exit(0)
            else:
                print(colored("⚠️ Opción inválida. Por favor, ingresa una opción válida.", "red"))
                time.sleep(2)

    def showUsers(self):
        self.clearScreen()
        print(colored("\n👥 Usuarios conectados:", "blue"))
        if not self.users:
            print(colored("⚠️ No hay usuarios conectados.", "red"))
        else:
            for user in self.users.keys():
                print(colored(f"• {user}", "white"))
        input(colored("\nPresiona Enter para regresar al menú...", "yellow"))

    def showChatrooms(self):
        self.clearScreen()
        print(colored("\n🗨️ Chatrooms disponibles:", "blue"))
        for idx, chatroom in enumerate(self.chatrooms, 1):
            print(f"{idx}. {chatroom}")

        choice = input(colored("Selecciona un chatroom para unirte (1-5): ", "yellow"))
        try:
            chatroom_idx = int(choice) - 1
            if 0 <= chatroom_idx < len(self.chatrooms):
                self.selected_chatroom = self.chatrooms[chatroom_idx]
                print(colored(f"✅ Te has unido al chatroom {self.selected_chatroom}.", "green"))
                self.joinChatroom()
            else:
                print(colored("⚠️ Selección inválida, por favor ingresa un número entre 1 y 5.", "red"))
                time.sleep(2)
        except ValueError:
            print(colored("⚠️ Opción no válida, por favor ingresa un número.", "red"))
            time.sleep(2)

    def joinChatroom(self):
        chatroom_channel = self.clientPusher.subscribe(self.selected_chatroom)
        chatroom_channel.bind('new_message', self.receiveMessage)
        self.sendMessageLoop()

    def sendMessageLoop(self):
        self.clearScreen()
        print(colored(f"📢 Chatroom: {self.selected_chatroom}", "blue"))
        print(colored("Escribe tus mensajes. Escribe 'salir' para salir del chatroom.\n", "yellow"))

        while True:
            message = input(colored("Tú: ", "yellow"))
            if message.lower() == "salir":
                print(colored("👋 Saliendo del chatroom...", "red"))
                self.clientPusher.unsubscribe(self.selected_chatroom)
                self.selected_chatroom = None
                break
            self.sendMessage(message)

    def sendMessage(self, message):
        self.pusher.trigger(self.selected_chatroom, 'new_message', {'username': self.user, 'message': message})

    def receiveMessage(self, message):
        data = json.loads(message)
        if data['username'] != self.user:
            print(f"{colored(data['username'], 'blue')}:" + f" {data['message']}")

    def clearScreen(self):
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    chat = TerminalChat()
    chat.login()
