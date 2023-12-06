export class Stack<T> {
    private items: Array<T>

    constructor() {
        this.items = [];
    }

    // Pushes an item to the top of the stack
    push(element: T) {
        this.items.push(element);
    }

    // Removes an item from the top of the stack
    pop(): T {
        return this.items.pop();
    }

    // Shows the last item pushed into the stack
    peek(): T {
        return this.items[this.size() - 1];
    }

    // Empty the stack
    clear() {
        this.items = [];
        // or 
        // this.items.length = 0;
    }

    // Gets the current size of the stack
    size(): number {
        return this.items.length;
    }

    isEmpty(): boolean {
        return this.size() == 0
    }

    toString() {
        return this.items.toString();
    }
}