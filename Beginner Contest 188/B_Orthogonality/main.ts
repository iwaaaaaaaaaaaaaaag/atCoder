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
    const N = +lines[0]
    const A = lines[1].split(' ') as number[]
    const B = lines[2].split(' ') as number[]
    let naiseki = 0
    for (const [i, A_elem] of A.entries()) {
        naiseki = naiseki + A_elem * B[i]
    }
    if (naiseki == 0) {
        console.log('Yes')
    } else {
        console.log('No')
    }
});