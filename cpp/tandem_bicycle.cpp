#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

bool desc (int i, int j) { return (i>j); }

int tandemBicycle(
  vector<int> redShirtSpeeds, vector<int> blueShirtSpeeds, bool fastest
) {
  if (fastest) {
  	sort(redShirtSpeeds.begin(), redShirtSpeeds.end());
  	sort(blueShirtSpeeds.begin(), blueShirtSpeeds.end(), desc);
  } else {
  	sort(redShirtSpeeds.begin(), redShirtSpeeds.end());
  	sort(blueShirtSpeeds.begin(), blueShirtSpeeds.end());
  }

  int sum = 0;

  for (int i=0; i < redShirtSpeeds.size(); i++) {
  	sum += max(redShirtSpeeds[i], blueShirtSpeeds[i]);
  }

  return sum;
}

int main(int argc, char const *argv[]) {
  int red[] = {5, 5, 3, 9, 2};
  int blue[] = {3, 6, 7, 2, 1};
  vector<int> redShirtSpeeds (red, red + sizeof(red) / sizeof(int) );
  vector<int> blueShirtSpeeds (blue, blue + sizeof(blue) / sizeof(int) );
  cout << "Speed: " << tandemBicycle(redShirtSpeeds, blueShirtSpeeds, false) << "\n\n";
}