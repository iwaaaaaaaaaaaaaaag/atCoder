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
    //距離を出す
    const N = lines[0]
    lines.shift()
    let t_start = 0
    let x_start = 0
    let y_start = 0
    let dist = 0
    let time = 0
    for (const [index, line] of lines.entries()) {
        const tmp = line.split(' ')
        let t_end = +tmp[0]
        let x_end = +tmp[1]
        let y_end = +tmp[2]
        dist = Math.abs(x_end - x_start) + Math.abs(y_end - y_start)
        time = t_end - t_start

        //判定
        if (time % 2 == dist % 2 && dist <= time) {
            if (index == N - 1) {
                console.log('Yes')
            }
        }
        else {
            console.log('No')
            break
        }
        t_start = t_end
        x_start = x_end
        y_start = y_end
    }

});