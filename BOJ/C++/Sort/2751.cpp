#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
	int numOfRows, temp;
	vector<int> array;

	cin >> numOfRows;
	for (int i = 0; i < numOfRows; i++) {
		cin >> temp;
		array.emplace_back(temp);
	}

	sort(array.begin(), array.end());

	for (int item : array) {
		cout << item << '\n';
	}

	return 0;
}