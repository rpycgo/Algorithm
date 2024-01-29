#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
	int N, M, temp, sum, minimum = 1000000;
	vector<int> array, array4Sum;
	cin >> N >> M;

	for (int i = 0; i < N; ++i) {
		cin >> temp;
		array.push_back(temp);
	}

	for (int i = 0; i < N; ++i) {
		for (int j = i + 1; j < N; ++j) {
			for (int k = j + 1; k < N; ++k) {
				sum = array[i] + array[j] + array[k];

				if ((sum <= M) && ((M - sum) < minimum)) {
					minimum = M - sum;
					temp = sum;
				}
			}
		}
	}

	cout << temp << endl;

	return 0;
}