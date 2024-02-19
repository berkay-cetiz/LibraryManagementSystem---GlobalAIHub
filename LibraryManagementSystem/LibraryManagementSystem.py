import pandas as pd

class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        file_contents = self.file.read()
        books_list = file_contents.splitlines()

        data = [book.split(",") for book in books_list]
        df = pd.DataFrame(data, columns=["Kitap Adı", "Yazar","Çıkış Yılı", "Sayfa Sayısı"])
        print(df.to_string(index=False, justify='right', float_format='{:0.0f}'.format,col_space=12))

    def add_book(self):
        book_title = input("Kitabın adını giriniz: ")
        book_author = input("Kitabın yazarını giriniz: ")
        first_release_year = input("Kitabın yayınlanma tarihini giriniz: ")
        num_of_pages = input("Kitabın sayfa sayısını giriniz: ")

        infofbooks = f"{book_title},{book_author},{first_release_year},{num_of_pages}\n"

        self.file.write(infofbooks)
        print(f"{book_author} tarafından yazılan {book_title} kütüphaneye eklendi..")

    def remove_book(self):
        book_title_remove = input("Silmek istediğiniz kitabın adını giriniz: ")

        self.file.seek(0)
        books_list = self.file.readlines()

        index_to_remove = None
        for i, book in enumerate(books_list):
            if book_title_remove.lower() in book.lower():
                index_to_remove = i
                break

        if index_to_remove != None:
            del books_list[index_to_remove]
            print(f"{book_title_remove} adlı kitap kütüphaneden silindi.")

            self.file.seek(0)
            self.file.truncate()
            self.file.writelines(books_list)
        else:
            print(f"Silmek istediğiniz {book_title_remove} adlı kitap kütüphanede bulunamadı.")

lib = Library()

while True:
    print()
    print("\n*** MENU ***")
    print("1) Kitapları listele")
    print("2) Kitap ekle")
    print("3) Kitap sil")
    print("Q) Çıkış yap")

    menu_choice = input("\nYapmak istediğiniz işlemi giriniz(1-3), çıkış yapmak 'q' giriniz: ")

    if menu_choice == "1":
        lib.list_books()
    elif menu_choice == "2":
        lib.add_book()
    elif menu_choice == "3":
        lib.remove_book()
    elif menu_choice.lower() == "q":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçenek. Lütfen 1 ile 3 arasında bir sayı veya çıkış yapmak için 'q' girin.")

input("Press Enter to exit...")