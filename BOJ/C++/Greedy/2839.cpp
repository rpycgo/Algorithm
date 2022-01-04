#include <iostream>

using namespace std;

int main() {
	int N;
	cin >> N;

	int count = 0;

	while (N > 0) {
		if ((N % 5) == 0) {			
			count += (N / 5);
			N -= N;
			break;
		}
		else {
			N -= 3;
			count++;
		}
	}

	if ((N == 0) && (count != 0)) {
		cout << count << endl;
	}
	else {
		cout << -1 << endl;
	}
 }
