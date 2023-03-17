#include <iostream>
#include <map>

int main() {
    // Create a string, int map
    std::map<std::string, int> scovilleHeatUnits = {
        {"Poblano", 1500},
        {"Mirasol", 6000},
        {"Serrano", 15500},
        {"Cayenne", 40000},
        {"Thai", 75000},
        {"Habanero", 125000},
    };

    // Get the amount of peppers that will be inputted
    int numPeppers;
    std::cin >> numPeppers;

    // Get the total pepper heat
    int totalPepperHeat = 0;
    for (int i = 0; i < numPeppers; i++) {
        // Get the pepper type
        std::string pepper;
        std::cin >> pepper;

        // Add the heat to the total
        totalPepperHeat += scovilleHeatUnits[pepper];
    }

    // Print the total heat
    std::cout << totalPepperHeat << std::endl;
    return 0;
}