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
    const n = +lines[0]
    let a = lines[1].split(' ')

    let count = 0
    while (true) {
        const divisor = a.map((val: number) => { return val % 2 })
        if (divisor.includes(1)) {
            break
        }
        a = a.map((val: number) => { return val / 2 })
        count++
    }
    console.log(count)
})
