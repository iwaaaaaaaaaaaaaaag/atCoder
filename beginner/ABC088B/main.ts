import * as readline from 'readline'

const reader = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const lines: any = []

reader.on('line', function (line) {
    lines.push(line);
});
reader.on('close', function () {
    const N = lines[0]
    const lists = lines[1].split(" ") as number[]
    lists.sort(compareFunc)

    let alice = 0
    let bob = 0
    let count = 1
    while (lists.length > 0) {
        if (count % 2 == 1) {
            alice = sum_store(alice, lists[lists.length - 1])
        } else {
            bob = sum_store(bob, lists[lists.length - 1])
        }
        lists.pop()
        count++
    }
    console.log(alice - bob)

    function sum_store(store: number, card_number: number) {
        return Number(store) + Number(card_number)
    }

    function compareFunc(a: number, b: number) {
        return a - b;
    }
});