package com.realtanx.ds;

import java.util.Iterator;

public class Queue<Item> implements Iterable<Item>
{
    private int N = 0;
    private Node<Item> first;
    private Node<Item> last;

    public void enqueue(Item item) {
        Node<Item> old = last;
        last = new Node<Item>();
        last.item = item;
        last.next = null;

        if (isEmpty()) {
            first = last;
        }
        else {
            old.next = last;
        }

        N++;
    }

    public Item dequeue() {
        Node<Item> old = first;
        first = first.next;

        if (isEmpty()) {
            last = null;
        }

        N--;

        return old.item;
    }

    public boolean isEmpty() {
//        return N == 0;
        return first == null;
    }

    public int size() {
        return N;
    }

    @Override
    public Iterator<Item> iterator() {
        return new ListIterator<Item>(first);
    }
}
