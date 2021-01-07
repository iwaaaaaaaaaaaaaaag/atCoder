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
    const tmp = lines[0]
    const s1 = +tmp.substr(0,1)
    const s2 = +tmp.substr(1,1)
    const s3 = +tmp.substr(2,1)
    console.log(s1 + s2 + s3)
});