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
    const N = tmp[0]
    const Y = tmp[1]

    let flag = false
    break_loop:
    for (let itiman_yen = 0; itiman_yen <= N; itiman_yen++) {
        next:
        for (let gosen_yen = 0; gosen_yen <= N; gosen_yen++) {
            for (let sen_yen = 0; sen_yen <= N; sen_yen++) {
                if (itiman_yen + gosen_yen + sen_yen > N) {
                    break next
                }
                if (itiman_yen * 10000 + gosen_yen * 5000 + sen_yen * 1000 == Y) {
                    console.log(itiman_yen + " " + gosen_yen + " " + sen_yen)
                    flag = true
                    break break_loop
                }
            }
        }
    }
    if (!flag) {
        console.log("-1 -1 -1")
    }
});