import tkinter as tk
from sqlite import save_metrics, get_normalized_metrics


class TrafficLightPet:
    def __init__(self):
        # 1. СОХРАНЯЕМ СВЕЖИЕ ДАННЫЕ
        print("📝 Сохраняем свежие метрики...")
        save_metrics()
        print("✅ Данные сохранены")

        self.root = tk.Tk()
        self.root.title("Индикатор нагрузки")
        self.root.overrideredirect(True)
        self.root.geometry("120x120+100+100")

        # Прозрачный фон
        self.transparent_color = '#abcdef'
        self.root.config(bg=self.transparent_color)
        self.root.wm_attributes('-transparentcolor', self.transparent_color)
        self.root.wm_attributes('-topmost', True)

        self.canvas = tk.Canvas(
            self.root,
            width=100,
            height=100,
            bg=self.transparent_color,
            highlightthickness=0
        )
        self.canvas.pack(expand=True)

        # Рисуем кружок (изначально серый)
        self.circle = self.canvas.create_oval(
            10, 10, 90, 90,
            fill='gray',
            outline=''
        )

        # Текст состояния
        self.label = self.canvas.create_text(
            50, 50,
            text='?',
            font=('Arial', 20, 'bold'),
            fill='white'
        )

        # Перетаскивание
        self.canvas.bind("<Button-1>", self.start_move)
        self.canvas.bind("<B1-Motion>", self.do_move)

        # Запускаем обновление
        self.update_status()

        self.root.mainloop()

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def do_move(self, event):
        x = self.root.winfo_x() + event.x - self.x
        y = self.root.winfo_y() + event.y - self.y
        self.root.geometry(f"+{x}+{y}")

    def update_status(self):
        """Обновляем цвет в зависимости от нагрузки"""
        try:
            # 2. КАЖДЫЙ РАЗ СОХРАНЯЕМ СВЕЖИЕ ДАННЫЕ
            save_metrics()

            # 3. ЗАГРУЖАЕМ ОБНОВЛЁННЫЕ ДАННЫЕ
            data = get_normalized_metrics()
            load = data['load']

            if not load:
                color = 'gray'
                text = '?'
            else:
                avg = sum(load) / len(load)
                current = load[-1]

                print(f"Средняя: {avg:.3f}, Текущая: {current:.3f}")

                # Определяем состояние
                if current < avg * 0.7:
                    color = '#00FF00'  # зелёный
                    text = '😴'
                elif current < avg * 1.3:
                    color = '#FFFF00'  # жёлтый
                    text = '😺'
                else:
                    color = '#FF0000'  # красный
                    text = '😱'

            self.canvas.itemconfig(self.circle, fill=color)
            self.canvas.itemconfig(self.label, text=text)

        except Exception as e:
            print(f"Ошибка: {e}")
            self.canvas.itemconfig(self.circle, fill='gray')
            self.canvas.itemconfig(self.label, text='?')

        self.root.after(5000, self.update_status)  # обновляем каждые 5 секунд


if __name__ == "__main__":
    TrafficLightPet()