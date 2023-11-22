#include <vector>
#include <iostream>
#include <limits>

using namespace std;

vector<int> findThreeLargestNumbers(vector<int> array) {
	int Lowest = numeric_limits<int>::lowest();
	int init[] = {Lowest, Lowest, Lowest};
	vector<int> output (init, init + sizeof(init) / sizeof(int));

	for (int i = 0; i < array.size(); i++) {
		for (int j = output.size() - 1; j >= 0; j--) {
			int value = array[i];
			int maxValue = output[j];
			if (value >= maxValue) {
				for (int k = 0; k < j; k++) {
					output[k] = output[k + 1];
				}
				output[j] = value;
			}
		}
	}
	return output;
}

int main(int argc, char const *argv[]) {
	int input[] = {141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7};
	vector<int> array (input, input + sizeof(input) / sizeof(int));
	vector<int> result = findThreeLargestNumbers(array);
	cout << "Result: " << "TEst" << "\n\n";
}