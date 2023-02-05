package com.realtanx.ds;

import java.util.Iterator;

public class ListIterator<Item> implements Iterator<Item> {

    private Node<Item> current;

    public ListIterator(Node<Item> first) {
        current = first;
    }

    @Override
    public boolean hasNext() {
        return current != null;
    }

    @Override
    public Item next() {
        Item item = current.item;
        current = current.next;

        return item;
    }

    @Override
    public void remove() {
    }
}
