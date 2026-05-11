// # include<iostream>
// using namespace std;

// int main(){



//     int row=3;

//     for(int i=0;i<row;i=i+1){//i=0 0<3

//         for(int col=0; col<5;col++){//col=0 0<5

//             if(i==0||i==2){  


//                 cout<<"* ";
//             }

//             else if(i==2){

//                 if(col==0||col==4){

//                     cout<<"*";
//                 }

//                 else{

//                     cout<<" ";
//                 }
//             }

//         }
//         cout<<endl;
//     }
// }

#include <iostream>
using namespace std;

int main()
{

    int row = 3;
    int col = 5;

    for (int i = 0; i < row; i++)
    {

        for (int j = 0; j < col; j++)
        {

            // boundary condition
            if (i == 0 || i == row - 1 || j == 0 || j == col - 1)
            {
                cout << "* ";
            }
            else
            {
                cout << "  ";
            }
        }

        cout << endl;
    }

    return 0;
}