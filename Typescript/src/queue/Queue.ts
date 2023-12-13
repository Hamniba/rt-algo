export class Queue<T> {
    protected items: Array<T>

    constructor() {
        this.items = [];
    }

    enqueue(item: T) {
        this.items.push(item)
    }

    dequeue(): T | undefined {
        return this.items.shift()
    }

    peek(): T | undefined {
        if (this.items.length > 0) {
            return this.items[0]
        }

        return undefined
    }

    isEmpty(): boolean {
        return this.items.length == 0
    }

    size(): number {
        return this.items.length
    }

    clear() {
        this.items = []
    }

    toString(): string {
        return this.items.toString()
    }
}