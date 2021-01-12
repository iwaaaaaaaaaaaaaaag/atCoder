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
    const number = lines[0]
    lines.shift()

    lines.sort(compareFunc)

    let set = new Set(lines)
    let setToArr = Array.from(set)

    console.log(setToArr.length)
    function compareFunc(a: number, b: number) {
        return a - b;
    }

});