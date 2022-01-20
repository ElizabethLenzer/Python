function stringDedupe(str) {
    const char_in_string = []
    for(let x =str.length-1;x >=0;x--){
        if(!char_in_string.includes(str[x])){
            char_in_string.splice(0,0,str[x])
        }
    }
    return char_in_string.join('')
}

// -----------------------------------------------------------

function reverseWords(str) {
    temp_str = ''
    final_str = ''
    for(let x = 0;x<=str.length;x++){
        if(str[x]!=' ' && x!=str.length){
        temp_str = str[x]+temp_str
        }
        else{
            final_str += temp_str
            temp_str = ''
            if(x!=str.length){
                final_str += ' '
            }
        }
    }
    return final_str
}