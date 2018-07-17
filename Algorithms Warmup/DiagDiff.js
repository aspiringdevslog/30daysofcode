'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the diagonalDifference function below.
function diagonalDifference(arr) {
    
    var abs, sum1 = 0, sum2 = 0; 
    
    for(var i=0; i<arr.length; i++){
        for(var j=0; j<arr.length; j++){
            if(i == j){ // 00,11,22 diag 1
                sum1 += arr[i][j];
                // console.log(i+","+j+":"+arr[i][j]);
            }
            if(i+j == arr.length-1){ // 03,12,21,30 diag 2
                sum2 += arr[i][j];
                // console.log(i+","+j+":"+arr[i][j]);
            }
        }
    }
    
    // console.log(sum1 + " sum2: " + sum2);
    
    abs = Math.abs(sum1 - sum2);
    
    return abs;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const n = parseInt(readLine(), 10);

    let arr = Array(n);

    for (let i = 0; i < n; i++) {
        arr[i] = readLine().split(' ').map(arrTemp => parseInt(arrTemp, 10));
    }

    const result = diagonalDifference(arr);

    ws.write(result + '\n');

    ws.end();
}
