import * as readline from 'readline'

const reader = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const lines: string[] = []

reader.on('line', function (line) {
    lines.push(line);
});
reader.on('close', function () {
    const tmp = lines[0].split(' ')
    const N = +tmp[0]
    const C = +tmp[1] //一日払えば全部使える
    lines.shift()
    
    
    
    for(const lists of lines){
        let list = lists.split(' ')
        if(list[0] <= min ){
            min = list[0]
        }        
    }
    
});
