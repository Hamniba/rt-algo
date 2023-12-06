import { Stack } from "./Stack"

/**
 * Convert decimal numbers to binary
 * @param decimal 
 * @returns 
 */
function decimalToBinary(decimal: number): string {
    const remainderStack = new Stack<number>()
    let number = decimal
    let remainder = 0

    while (number > 0) {
        remainder = Math.floor(number % 2)
        remainderStack.push(remainder)
        number = Math.floor(number / 2)
    }

    let binaryStr = ''
    while (remainderStack.size() > 0) {
        binaryStr = binaryStr + remainderStack.pop().toString()
    }

    return binaryStr
}

console.log(`decimalToBinary 1024 => ${decimalToBinary(1024)}`)

