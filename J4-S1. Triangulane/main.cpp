#include <iostream>

int main() {
    int N;
    std::cin >> N;
    

    // Initialize the rows
    int row1[N];
    int row2[N];

    // Fill the rows
    for (int i = 0; i < N; i++) {
        std::cin >> row1[i];
    }
    for (int i = 0; i < N; i++) {
        std::cin >> row2[i];
    }

    // Store the total amount of meter tape required
    int total = 0;

    // Iterate over row1
    for (int i = 0; i < N; i++) {
        if (row1[i] == 1) {
            total += 3;
        }
    }

    // Iterate over row2
    for (int i = 0; i < N; i++) {
        if (row2[i] == 1) {
            total += 3;
        }
    }

    // Check if there is a triangle infront of the current triangle
    for (int i = 0; i < N - 1; i++) {
        if (row1[i] == 1 && row1[i + 1] == 1) {
            total -= 2;
        }
        if (row2[i] == 1 && row2[i + 1] == 1) {
            total -= 2;
        }
    }

    // Check if there are triangles under / above the rows
    for (int i = 0; i < N; i += 2) {
        if (row1[i] == 1 && row2[i] == 1) {
            total -= 2;
        }
    }

    // Print the total
    std::cout << total << std::endl;
    return 0;
}


/*
Tests:

Input:
7
0 0 1 1 0 1 0
0 0 0 0 0 0 0

Output: 7


Input:
5
1 0 1 0 1
0 0 0 0 0

Output: 9

*/