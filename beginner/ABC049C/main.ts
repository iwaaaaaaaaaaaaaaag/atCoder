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
    let str = lines[0]
    
    interface Targets {
        id: number,
        str: string,
        match: boolean
    }
    
    const targets = [
        { id: 1, str: 'dreamer', match: false },
        { id: 2, str: 'eraser', match: false },
        { id: 3, str: 'dream', match: false },
        { id: 4, str: 'erase', match: false },
    ] as Targets[]
    
    while (true) {
        for (const target of targets) {
            target.match = false
            let last_word = str.substr(-target.str.length, target.str.length)//最後の単語から比較する
            if (last_word === target.str) {
                target.match = true
            }
        }
        const index = targets.findIndex(({ match }) => match === true);
        if (index == -1) {
            console.log('NO')
            break
        }
        str = str.substring(0, str.length - targets[index].str.length)//最後の単語を除外する
        if (str === "") {
            console.log('YES')
            break
        }
    }
});