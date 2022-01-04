// Get the input in an array form
// from the text fil saved


const fs = require('fs');

fs.readFile('input.txt','utf-8',(err, data) => {
    const input = data.split('\n').map((x) => Number(x))
    const valuesToCheck= []
    let count = 0
    for (let i = 0; i < input.length; i++) {
        valuesToCheck.push(input.slice(i, i+3).reduce((acc,v)=> acc + v, 0))

    }
    for (let i =0; i < valuesToCheck.length; i++) {
        const first = valuesToCheck[i]
        const second = valuesToCheck[i+1]
        if (second > first) {
            ++count
        }
    }

    console.log('Count=', count)
})