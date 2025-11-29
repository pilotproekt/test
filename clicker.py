from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import threading
import time

# Инициализация контроллера мыши
mouse = Controller()

# Флаги для управления автокликером
is_running = False
stop_key = KeyCode(char='w') # клавиша для остановки
start_key = KeyCode(char='e') # клавиша запуска

# Параметры кликов
click_delay = 0.1 # Задержка между кликами
click_count = 100 # Количество кликов

class AutoClicker(threading.Thread):
    def __init__(self):
        super().__init__()
        self.running = False
        
    def run(self):
        global is_running
        self.running = True
        click_counter = 0
        
        while self.running and click_counter < click_count:
            mouse.click(Button.left) # левы клик
            click_counter +=1
            time.sleep(click_delay)
            
        is_running = False
        print(f"Автокликер завершен. Выполнено {click_counter} кликов")
        
    def stop(self):
        self.running = False
        
# Обработчик нажатия клавиш
def on_press(key):
    global is_running
    
    if key == start_key and not is_running:
        print("Автокликер запущен!")
        clicker = AutoClicker()
        clicker.start()
        is_running = True
    elif key == stop_key and is_running:
        print("Автокликер остановлен!")
        clicker.stop()
        is_running = False
# Запуск прослушки клавиатуры
def main():
    with Listener(on_press=on_press) as listener:
        print(f"Автокликер готов. Нажмите '{start_key.char}' для запуска, '{stop_key.char}' для остновки.")
        listener.join()
    
if __name__ == "__main__":
    main()             
