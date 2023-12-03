const foo = Bun.file("input3.txt"); // relative to cwd
// const foo = Bun.file("input3_example.txt"); // relative to cwd

foo.size; // number of bytes
foo.type; // MIME type
let rawtext = await foo.text();
// ignore line breaks
var lines = rawtext.split('\n')
const lastchar = lines[0][0]
const digits = '1234567890'
var value=''
var total = 0
console.log(lines.length)

var line_counter = 0
var next_to_char = false

function check_chars(x,y,lines){
    var out = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]].some(d => {
        var whitelist = '1234567890.'
        try {
            // console.log(d,typeof(d[0]),typeof(d[1]),typeof(x),typeof(y))
            if (!whitelist.includes(lines[y+parseInt(d[1])][x+parseInt(d[0])])){
                // console.log('done',lines[y][x],arr,d,x,y,x+d[0],y+d[1])
                // console.log('true',arr)
                return true
            }
        } catch (err) {
            // console.error(err);
        }
         
    });
    return out
}

for (const line of lines){

    if ((value.length>0)){
        if (next_to_char){
            total+=parseInt(value)
        }else{
            console.log('not near',value)
        }
        value=''
        next_to_char=false
    }
    value=''
    next_to_char=false

    console.log(line_counter,line)
    var c=0
    for (const charpos in line){
        if (digits.includes(line[charpos])){
            value+=line[charpos]
            // check around the 8 values for a special char
            // console.log(check_chars(parseInt(charpos),line_counter,lines))
            if (check_chars(c,line_counter,lines)){
                // console.log(value,check_chars(parseInt(charpos),line_counter,lines))
                next_to_char=true
            }
        }else{
            if ((value.length>0)&next_to_char){
                if (next_to_char){
                    total+=parseInt(value)
                }else{
                    console.log('not near',value)
                }
                value=''
                next_to_char=false
            }
        }
        c+=1
    }
    line_counter+=1
}

console.log(total)
// part 1
// 548403 too low
// 549500 too low
// 551451 wrong
// 550064 from python 
// where is the fucking bug