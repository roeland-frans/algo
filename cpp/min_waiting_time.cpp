#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int minimumWaitingTime(vector<int> queries) {
  int total = 0;
  int queriesLeft = 0;

  sort(queries.begin(), queries.end());
  
  for (int i=0; i < queries.size(); i++) {
    queriesLeft = queries.size() - (i + 1);
    total += queries[i] * queriesLeft;
  }
  return total;
}

int main(int argc, char const *argv[]) {
  int waitingTimes[] = {16, 2, 77, 29};
  vector<int> queries (
  	waitingTimes,
  	waitingTimes + sizeof(waitingTimes) / sizeof(int)
  );
  cout << "Minimum waiting time: " << minimumWaitingTime(queries) << "\n\n";
}
