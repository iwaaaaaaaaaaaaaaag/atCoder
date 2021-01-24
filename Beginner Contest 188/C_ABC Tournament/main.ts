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
    const lists = lines[1].split(' ') as number[]
    loop:
    while (true) {

        if (lists.length == 2) {
            break loop
        }
        if (+lists[0] < +lists[1]) {
            lists.push(lists[1])
        }
        else {
            lists.push(lists[0])
        }
        lists.shift()
        lists.shift()
    }
    let second_winner = 0
    if (lists[0] < lists[1]) {
        second_winner = lists[0]
    } else {
        second_winner = lists[1]
    }

    console.log(lines[1].split(' ').indexOf(second_winner) + 1)
});
