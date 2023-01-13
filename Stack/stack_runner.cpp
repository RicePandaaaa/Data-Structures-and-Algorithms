/*
 * This is a test runner file for my implemenation of the stack.
 * Examples will include int, double, and char
 */

#include <string>
#include <iostream>
#include <sstream>
#include <cstddef>
#include "stack.cpp"

using std::cout, std::endl, std::string;

int main() {
    // Making the stacks
    Stack<size_t> ints;
    Stack<double> doubles;
    Stack<char> chars;

    // Testing push()
    for (size_t loop_num = 0; loop_num < 2; loop_num++) {
        push(ints, loop_num + 1);
        push(doubles, (loop_num + 1) * 1.0);
        push(chars, char(65 + loop_num));
    }

    // Testing size()
    cout << "Expecting size of 2 from all stacks." << endl;
    cout << "Size of ints: " << size(ints) << endl;
    cout << "Size of doubles: " << size(doubles) << endl;
    cout << "Size of chars: " << size(chars) << endl;

    // Testing pop() and peek()
    cout << "Expecting 2, 2,and B in next two lines." << endl;
    cout << "Peeking: " << peek(ints) << " " << peek(doubles) << " " << peek(chars) << endl; 
    cout << "Popping: " << pop(ints) << " " << pop(doubles) << " " << pop(chars) << endl; 
    cout << "Expecting 1, 1,and A from next two lines." << endl;
    cout << "Peeking: " << peek(ints) << " " << peek(doubles) << " " << peek(chars) << endl; 
    cout << "Popping: " << pop(ints) << " " << pop(doubles) << " " << pop(chars) << endl; 
    cout << "Expecting 0, 0, and invisible character from next two lines." << endl;
    cout << "Peeking: " << peek(ints) << " " << peek(doubles) << " " << peek(chars) << endl; 
    cout << "Popping: " << pop(ints) << " " << pop(doubles) << " " << pop(chars) << endl; 


    return 0;
}