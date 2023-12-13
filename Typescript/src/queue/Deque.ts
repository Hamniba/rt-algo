import { Queue } from "./Queue";

/**
 * The deque data structure, also known as the double-ended queue, 
 * is a special queue that allows us to insert and remove elements from the end or from the front of the queue.
 * 
 * Because the deque implements both principles, FIFO and LIFO, 
 * we can also say that the deque is a merger between the queue and the stack data structures.
 */
export class Deque<T> extends Queue<T> {
    addFront(item: T) {
        this.items.unshift(item)
    }

    addBack(item: T) {
        super.enqueue(item)
    }

    removeFront(): T | undefined {
        return super.dequeue()
    }

    removeBack(): T | undefined {
        return this.items.pop()
    }

    peekFront(): T | undefined {
        return super.peek()
    }

    peekBack(): T | undefined {
        if (this.items.length > 0) {
            return this.items[this.size() - 1]
        }

        return undefined
    }
}