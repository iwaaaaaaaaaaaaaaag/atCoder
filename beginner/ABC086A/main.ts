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
    // input
    const tmp = lines[0].split(' ')
    const a = +tmp[0]
    const b = +tmp[1]

    // output
    const mul = a * b
    if (mul % 2 == 1) {
        console.log('Odd')
    }
    else {
        console.log('Even')
    }
});