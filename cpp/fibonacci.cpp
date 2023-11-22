#include <iostream>


using namespace std;

int getNthFib(int n) {
  int f[] = {0, 1};

  for (int i = 2; i < n; i++) {
  	int nextFib = f[1] + f[0];
  	f[0] = f[1];
  	f[1] = nextFib;
  }
  if (n > 1) {
  	return f[1];
  } else {
  	return f[0];
  }
}

int main(int argc, char const *argv[]) {
	int result = getNthFib(6);

	cout << "Result: " << result << "\n";
}