const path = require('path')
const CSV = require('fast-csv')
const File = require('fs')

const rows = [
    ['a', 'b'],
    ['a1', 'b1'],
    ['a2', 'b2'],
];

const writeStream = File.createWriteStream(path.resolve(__dirname, 'tmp.csv'), {flags : 'a'})

const csvStream = CSV.format({ headers: ['哈哈','嘿嘿'], })

csvStream.pipe(writeStream)

csvStream.write(['a2', 'b2'])

csvStream.write(['a1', 'b1'])

csvStream.end()

/* csvStream.writeToPath(path.resolve(__dirname, 'tmp.csv'), rows)
.on('error', err => console.error(err))
.on('finish', () => console.log('Done writing.')); */