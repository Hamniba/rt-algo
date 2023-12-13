import { Deque } from "./Deque"

/**
 * Whether a phrase is a palindrome.
 * 
 * A palindrome is a word, phrase, number, 
 * or other sequence of characters which reads the same backward as forward, such as madam or racecar.
 */

function palindromeChecker(aString: string): boolean {
    if (aString.length == 0) {
        return false
    }

    let isEqual = true
    let first = ''
    let last = ''
    const deque = new Deque<string>()

    for (const char of aString) {
        deque.addBack(char)
    }
    console.log(`Deque => ${deque.toString()}`);

    while (deque.size() > 1 && isEqual) {
        first = deque.removeFront()
        last = deque.removeBack()
        isEqual = first === last
    }

    return isEqual
}

console.log(`palindrome => ${palindromeChecker("kayak")}`)

