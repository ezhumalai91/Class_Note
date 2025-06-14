'''
Class:
        A class is a user-defined blueprint or prototype from which objects are created.
        It consists of objects and methods.

Syntax:

            class class_name:
                Statement

                
Note:  __init__ is a constructor function.
    Constructor in is a special method that is invoked automatically
    at the time an object of a class is created.
'''

'''
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city


p = Person('Asabeneh', 'Yetayeh', 50, 'Finland', 'Helsinki')
a=Person('Aravind', 'mark', 100, 'India', 'Mumbai')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)
print(a.firstname)
print(a.lastname)
'''

'''
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
      def person_info(self,mark):
        return f'My mark is {mark}. {self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'


p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.person_info(488))
'''


'''
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
      def display(self):
        print("First Name:", self.firstname)
        print("Last Name:",self.lastname)

firstname=input("Please enter your first name:\t")
lastname=input("Please enter your last name:\t")

p = Person(firstname, lastname, 250, 'Finland', 'Helsinki')
print(p.display())
'''

'''
class Student:  
    def __init__(self, name, id, age):  
        self.name = name  
        self.id = id  
        self.age = age  
  
s = Student("John", 101, 22)  
  
# prints the attribute name of the object s  
print(getattr(s, 'name'))  
  
# reset the value of attribute age to 23  
setattr(s, "age", 23)
  
# prints the modified value of age  
print(getattr(s, 'age'))  
  
# prints true if the student contains the attribute with name id  
  
print(hasattr(s, 'id'))  
# deletes the attribute age  
delattr(s, 'age')  
  
# this will give an error since the attribute age has been deleted  
print(s.age)
'''


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author):
        self.books[book_id] = {'title': title, 'author': author}

    def update_book(self, book_id, title=None, author=None):
        if book_id in self.books:
            if title:
                self.books[book_id]['title'] = title
            if author:
                self.books[book_id]['author'] = author
            print("Book updated successfully.")
        else:
            print("Book not found.")

    def delete_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            print("Book deleted successfully.")
        else:
            print("Book not found.")

    def search_book(self, book_id):
        if book_id in self.books:
            return self.books[book_id]
        else:
            return None

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. Search Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(book_id, title, author)

        elif choice == '2':
            book_id = input("Enter book ID to update: ")
            title = input("Enter new title (leave blank to keep unchanged): ")
            author = input("Enter new author (leave blank to keep unchanged): ")
            library.update_book(book_id, title, author)

        elif choice == '3':
            book_id = input("Enter book ID to delete: ")
            library.delete_book(book_id)

        elif choice == '4':
            book_id = input("Enter book ID to search: ")
            book = library.search_book(book_id)
            if book:
                print("Book found:")
                print("ID:", book_id)
                print("Title:", book['title'])
                print("Author:", book['author'])
            else:
                print("Book not found.")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()


'''
class library:
    def __init__(self):
        self.books={}
    def add(self):
        book_id=int(input("Please book id"))
        book_title=input("Please book Title")
        book_author=input("Please book Author")
        book_count=int(input("Please book count"))
        if book_id not in self.books:
            self.books[book_id] = {'book_title': book_title, 'book_author': book_author,'book_count':book_count}      #{101:{},102:{}}
            print(self.books)
        else:
            print("Book id already present. Please change book id. Try again!!")
            self.add()
    def view(self):
        book_id=int(input("Please enter book id"))
        if book_id in self.books:
            print("Book Name:\t",self.books['book_title'])
            print("Book Author:\t",self.books['book_author'])
            print("Book Count:\t",self.books['book_count'])
        else:
            print("Book not found. Please enter correct book id")
            self.view()


if __name__=="__main__":
    l=library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. Search Book")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            l.add()
        elif choice==4:
            l.view()
        elif choice == 5:
            exit()

'''



        

































