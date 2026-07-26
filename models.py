class Task:
    def __init__(self, title):
        self.title = title
        self.done = False

    def mark_done(self):
        self.done = True

    def show_task(self):
        if self.done:
            print(f"[Done] {self.title}")
        else:
            print(f"[Todo] {self.title}")

    def to_dic(self):
        return {
            "title": self.title,
            "done": self.done
        }
    

