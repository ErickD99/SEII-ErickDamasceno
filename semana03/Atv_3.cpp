#include <iostream>
using namespace std;

void mover(int, char, char, char);

int main()
{	char a, b, c;
	int x;
	a = 'A';
	b = 'B';
	c = 'C';
	cout << "Quantidade de discos: ";
	cin >> x;
	mover(x, a, c, b);

	system("Pause");
	return 0;
}
void mover(int x, char a , char c, char b)
{
	if(x == 1)
	{     
		cout << "Movendo o disco 1 de "<< a <<" para "<< c << endl;
		x = x - 1;
	}
	else
	{
		mover(x - 1, a, b, c);
        cout << "Movendo o disco " << x << " de " << a << " para " << c << endl;
		mover(x -1, b, c, a);
	}
}