import * as readline from 'readline'

const reader = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const lines : any = []

reader.on('line', function (line) {
  lines.push(line);
});
reader.on('close', function () {
  // input
  const a = +lines[0] 
  const tmp = lines[1].split(' ')
  const b = +tmp[0] 
  const c = +tmp[1] 
  const s = lines[2] as string

  // output
  console.log(a + b + c + " " + s)
});