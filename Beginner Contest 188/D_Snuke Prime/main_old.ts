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
    const N = +tmp[0]
    const C = +tmp[1] //一日払えば全部使える
    lines.shift()
    let min = +lines[0].split(' ')[0]
    let max = +lines[0].split(' ')[1]
    
    // 最小値を求める
    // 最大値を求める
    for (const line of lines) {
        const datas = line.split(' ')
        if (+datas[0] <= min) {
            min = +datas[0]
        }
        else if (max <= +datas[1]) {
            max = +datas[1]
        }
    }
    
    // 合計値を出力
    let sum = 0
    for (let i = min; i <= max; i++) {
        let tmp_sum = 0
        for (const line of lines) {
            const datas = line.split(' ')
            if (+datas[0] <= i && i <= +datas[1]) {
                tmp_sum = tmp_sum + +datas[2]
            }
        }
    
        if (tmp_sum <= C) {
            sum = sum + tmp_sum
        }
        else {
            sum = sum + C
        }
    }
    console.log(sum)
});
