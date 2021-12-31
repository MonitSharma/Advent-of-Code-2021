const fs = require('fs')
// const input = [1, 2, 3, 4, 5, 7, 1, 9, 10]
// const input = [ [1, 2, 3], [2, 3, 4] , [3, 4, 5]]

fs.readFile('input-data.txt', 'utf-8', (err, data) => {
  const input = data.split('\n').map((x) => Number(x))
  const valuesToCheck = []
  let counter = 0
  for (let i = 0; i < input.length; i++) {
    valuesToCheck.push(input.slice(i, i + 3).reduce((acc, v) => acc + v, 0))
  }
  for (let i = 0; i < valuesToCheck.length; i++) {
    const firstVal = valuesToCheck[i]
    const secondVal = valuesToCheck[i + 1]
    if (secondVal > firstVal) {
      ++counter
    }
  }
  console.log('Counter=', counter)
})