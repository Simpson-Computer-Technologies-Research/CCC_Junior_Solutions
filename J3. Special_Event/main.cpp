#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

int main() {
    // Get the number of attendees
    int N;
    std::cin >> N;

    // Initialize an array of days
    std::vector<int> days;

    // Get the availabilities
    for (int i = 0; i < N; i++) {
        std::string availability;
        std::cin >> availability;

        // Iterate over the availability string
        for (int j = 0; j < availability.length(); j++) {
            // If the day doesn't exist in the array, add it
            if (days.size() <= j) {
                days.push_back(0);
            }
            
            // Increment the number of attendees for that day
            if (availability[j] == 'Y') {
                days[j]++;
            }
        }
    }

    // Get the max number of attendees throughout the days
    int maxAttendees = *std::max_element(days.begin(), days.end());

    /* Could've also done this

    // Get the max number of attendees throughout the days
    int maxAttendees = -1;
    for (int i = 0; i < days.size(); i++) {
        if (days[i] > maxAttendees) {
            maxAttendees = days[i];
        }
    }

    */

    // Iterate over the days
    std::string result = "";
    for (int i = 0; i < days.size(); i++) {
        // If the day has the most attendees, add it to the result string
        if (days[i] == maxAttendees) {
            result += std::to_string(i + 1) + ",";
        }
    }
    
    // Print the result without the last comma
    std::cout << result.substr(0, result.length() - 1) << std::endl;
    return 0;
}