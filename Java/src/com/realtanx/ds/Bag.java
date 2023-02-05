package com.realtanx.ds;

import java.util.Iterator;

public class Bag<Item> implements Iterable<Item>
{
    private Node<Item> first;
    private int N = 0;

    public void add(Item item) {
        Node<Item> old = first;
        first = new Node<Item>();
        first.item = item;
        first.next = old;
        N++;
    }

    public boolean isEmpty() {
        return N == 0;
    }

    public int size() {
        return N;
    }

    @Override
    public Iterator<Item> iterator() {
        return new ListIterator<Item>(first);
    }
}
