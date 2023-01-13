/*
Stacks is a data structure used to hold data. They are differnt in that you can only access the most recently added element, whether it is to view it or to take out for usage. A deck of cards would be a stack if you were to draw cards one by one from the top of the deck. The four main methods are as follows:
 - pop(): Remove the most recently added element, if any
 - peek(): View the most recently added element, if any
 - push(): Add an element to the top of a stack
 - size(): Returns the size of the stack

This example will use a template that is useable for primitive data types that can be added to an array (this is an array implementation of a stack).
*/

#include <cstddef>

// Stack struct
template <typename T>
struct Stack {
    size_t capacity = 1;
    size_t count = 0;
    T* elements = new T[1] {};
};

// Implementation of push
template <typename T> 
void push (Stack<T>& stack, T element) 
{
    // Resize array
    if (stack.count == stack.capacity) {
        T* new_elements = new T[stack.capacity * 2];
        for (size_t index = 0; index < stack.capacity; ++index) {
            new_elements[index] = stack.elements[index];
        };

        delete[] stack.elements;
        stack.elements = new_elements;
        stack.capacity *= 2;
    }

    // Push the element
    stack.elements[stack.count] = element;
    stack.count += 1;
};

// Implementation of pop
template <typename T>
T pop(Stack<T>& stack) 
{
    // Empty stack edge case
    if (stack.count == 0) {
        return 0;
    }

    T element = stack.elements[stack.count - 1];
    stack.elements[stack.count - 1] = 0;
    stack.count -= 1;
    return element;
};

// Implementation of peek
template <typename T>
T peek(Stack<T>& stack)
{
    // Empty stack edge case
    if (stack.count == 0) {
        return 0;
    }

    return stack.elements[stack.count - 1];
};

// Implementation of size
template <typename T>
size_t size(Stack<T>& stack) 
{
    return stack.count;
};