class BookStore:
    
    NoOfBooks = 0

    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author

        BookStore.NoOfBooks += 1

    def Display(self):
        print(f"{self.Name} by {self.Author}. No of Books: {BookStore.NoOfBooks}")


def main():
    obj1 = BookStore("Shrimanyogi", "Ranjeet Desai")
    obj2 = BookStore("Wings of Fire", "A. P. J. Abdul Kalam")
    obj3 = BookStore("C Programming", "Dennis Ritchie")

    obj1.Display()
    obj2.Display()
    obj3.Display()


if __name__ == "__main__":
    main()

