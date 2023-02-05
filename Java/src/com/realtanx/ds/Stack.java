package com.realtanx.ds;

import java.util.Iterator;

public class Stack<Item> implements Iterable<Item>
{
    private Node<Item> first;
    private int N = 0;

    public void push(Item item) {
        Node<Item> old = first;
        first = new Node<Item>();
        first.item = item;
        first.next = old;
        N++;
    }

    public Item pop() {
        Node<Item> old = first;
        first = first.next;
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
