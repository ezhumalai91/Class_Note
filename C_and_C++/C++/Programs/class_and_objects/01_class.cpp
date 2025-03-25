#include <iostream>
using namespace std;

class Student_details
{
    private:
        char name[30];
        int roll_no;
        int age;
        float marks;
    public:
        void get_details()
        {
            cout<<"Enter name: ";
            cin>>name;
            cout<<"Enter roll no: ";
            cin>>roll_no;
            cout<<"Enter age: ";
            cin>>age;
            cout<<"Enter marks: ";
            cin>>marks;
        }
        void display()
        {
            cout<<"\n\n****STUDENT DETAILS***\n";
            cout<<"Name: "<<name<<endl;
            cout<<"Roll no: "<<roll_no<<endl;
            cout<<"Age: "<<age<<endl;
            cout<<"Marks: "<<marks<<endl;
        }
};
int main()
{
    Student_details s;
        s.get_details();
        s.display();
    return 0;
    }   

    
