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
  const tmp = lines[0].split(' ')
  const N = tmp[0]
  const A = +tmp[1]
  const B = +tmp[2]

  let sum = 0
  for (let i = 1; i <= N; i++) {
    const N_splits = String(i).split('')
    let sum_N_split = 0
    for (const N_split of N_splits) {
      sum_N_split = sum_N_split + Number(N_split)
    }
    if (A <= sum_N_split && sum_N_split <= B) {
      sum = sum + i
    }
  }
  console.log(sum)
});