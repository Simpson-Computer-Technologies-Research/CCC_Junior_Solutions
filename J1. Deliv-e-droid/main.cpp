#include <iostream>

using namespace std;
int main() {
    // Get the number of deliveries
    int deliveries;
    std::cin >> deliveries;

    // Get the number of collisions
    int collisions;
    std::cin >> collisions;

    // Calculate the final score
    int finalScore = (deliveries * 50) - (collisions * 10);

    // Check whether to add the bonus, if yes, then add 500 points
    if (deliveries > collisions) finalScore += 500;

    // Print the final score
    std::cout << finalScore << std::endl;
    return 0;
}