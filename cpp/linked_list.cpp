#include <iostream>

using namespace std;

struct Item {
	uint value;
	Item* nextItem = NULL;
};


int main(int argc, char const *argv[])
{
	struct Item item3 = {1, NULL};
	struct Item item2 = {2, &item3};
	struct Item item1 = {3, &item2};
	struct Item* itemPtr = &item1;

	cout << "Hello world!\n";

	while (1) {
		cout << "Item: " << itemPtr->value << "\n";
		itemPtr = itemPtr->nextItem;
		if (itemPtr == NULL) {
			break;
		}
	}

	return 0;
}