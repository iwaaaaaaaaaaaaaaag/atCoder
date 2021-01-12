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
  const A = +lines[0] //500円
  const B = +lines[1] //100円
  const C = +lines[2] //50円
  const X = +lines[3]
  let count = 0

  for (let i = 0; i <= A; i++) {
    for (let j = 0; j <= B; j++) {
      for (let k = 0; k <= C; k++) {
        if (500 * i + 100 * j + 50 * k == X) {
          count++
        }
      }
    }
  }
  console.log(count)
});