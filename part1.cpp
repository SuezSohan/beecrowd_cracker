/* //Area-1012
#include<iostream>
#include<iomanip>
using namespace std;
int main(){
    double A, B, C;
    cin>>A>>B>>C;
    cout<<fixed<<setprecision(3);
    cout<<"TRIANGULO: "<<(0.5*A*C)<<endl;
    cout<<"CIRCULO: "<<3.14159*C*C<<endl;
    cout<<"TRAPEZIO: "<<0.5*(A+B)*C<<endl;
    cout<<"QUADRADO: "<<B*B<<endl;
    cout<<"RETANGULO: "<<A*B<<endl;
    return 0;
} */

/* //Sphere-1011
#include<iostream>
#include<iomanip>
using namespace std;
int main(){
    double r, v;
    cin>>r;
    v = (4/3.0)*3.14159*r*r*r;
    cout<<"VOLUME = "<<fixed<<setprecision(3)<<v<<endl;
    return 0;
} */

/* //Simple Calculate-1010
#include<iostream>
#include<iomanip>
using namespace std;
int main(){
    int a1, a2, b1, b2;
    float p1, p2, t;
    cin>>a1>>b1>>p1;
    cin>>a2>>b2>>p2;
    t = (b1*p1)+(b2*p2);
    cout<<"VALOR A PAGAR: R$ "<<fixed<<setprecision(2)<<t<<endl;
    return 0;
} */

/* //Salary with bonus-1009
#include<iostream>
#include<iomanip>
using namespace std;
int main(){
    string N;
    double S, Ps, T;
    cin>>N>>S>>Ps;
    T = S+(Ps*15/100);
    cout<<"TOTAL = R$ "<<fixed<<setprecision(2)<<T<<endl;
    return 0;
}*/

/* //salary-1008
#include<iostream>
#include<iomanip>
using namespace std;
int main(){
    int A, B;
    float Sh, S;
    cin>>A>>B>>Sh;
    S=Sh*B;
    cout<<"NUMBER = "<<A<<"\nSALARY = U$ "<<fixed<<setprecision(2)<<S<<endl;
    return 0;
}

 */

/* //Difference-1007
#include<iostream>
using namespace std;
int main(){
    int A, B, C, D, dif;
    cin>>A>>B>>C>>D;
    dif = (A*B)-(C*D);

    cout<<"DIFERENCA = "<<dif<<endl;
    return 0;
} */

/* //Average 2-1006
#include<iostream>
#include<iomanip>
using namespace std;
int main(){
    double A, B, C, M;
    cin>>A>>B>>C;
    A*=2;
    B*=3;
    C*=5;
    M=(A+B+C)/(2+3+5);
    cout<<"MEDIA = "<<fixed<<setprecision(1)<<M<<endl;
    return 0;

} */

/* //Average 1-1005
#include<iostream>
#include<iomanip>
using namespace std;
int main(){
    double A, B, media;

    cin >> A >> B;
    A = A*3.5;
    B = B*7.5;
    media = (A+B)/(3.5+7.5);
    cout << "MEDIA = " << fixed << setprecision(5)<< media << endl;
    return 0;

} */

/* //Simple Product-1005
#include<iostream>
using namespace std;
int main(){
    int A, B, PROD;
    cin >> A >> B;
    PROD = A*B;
    cout << "PROD = " << PROD << endl;
    return 0;
} */

/* //Simple Sum-1003
#include<iostream>
using namespace std;
int main(){
    int A, B, SOMA;
    cin >> A >> B;
    SOMA = A+B;
    cout<< "SOMA = " << SOMA << endl;
    return 0;
} */

/* //Problem code:1000
#include<iostream>
#include<iomanip>
using namespace std;
int main(){
    double R, A;
    cin >> R;
    A = 3.14159*R*R;
    std::cout << std::setprecision(4) << std::fixed;
    cout << "A="<< A << endl;
    return 0;
} */

/* //Problem code: 1001
#include<iostream>
using namespace std;

int main(){
    int A, B;
    cin >> A >> B;
    int X=A+B;
    cout<<"X = "<< X <<endl;
} */

/* //Problem code: 1000

#include <iostream>
 
using namespace std;
 
int main() {
 
    cout<<"Hellow World!"<<endl;
 
    return 0;
} */