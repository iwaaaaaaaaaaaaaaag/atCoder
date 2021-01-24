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
    const tmp = lines[0].split(' ')
    const X = tmp[0]
    const Y = tmp[1]
    if (Math.abs(X - Y) < 3) {
        console.log('Yes')
    } else {
        console.log('No')
    }
});