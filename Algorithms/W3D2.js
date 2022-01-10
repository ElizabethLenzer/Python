const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 */
function reverseString(str) {
    var newString = "";
for(var i=str.length-1; i>=0; i--){
    newString =newString + str[i];
    console.log(newString);
    }
}

var string = "creature";
var string2 = "dog"
reverseString(string)
module.exports = { reverseString };

// psuedo code
// str.split(): Will split up a string by each character
//      I.E: var str = "hello there"
//           str.split("")
            // Console.log(str.split("")): will output h e l l o   t h e r e
            // Console.log(str.split(" ")): Will output "Hello" "there"
                	// var arr = str.split(" ") -> ["Hello", "There"]
                	// console.log(str[0]) -> "H"
                	// console.log(arr[1][0]) -> "T"
// step 1: Loop Through String
// step 2: identify if the character is a space
// step 3: capitalize


// //////////////// Question 1/////////////////// //
/* 
Acronyms
Create a function that, given a string, returns the string’s acronym 
(first letter of each word capitalized). 
Do it with .split first if you need to, then try to do it without
*/

const str1 = " there's no free lunch - gotta pay yer way. ";
const expected1 = "TNFL-GPYW";

const str2 = "Live from New York, it's Saturday Night!";
const expected2 = "LFNYISN";

// psuedo code
// str.split(): Will split up a string by each character
//      I.E: var str = "hello there"
//           str.split("")
            // Console.log(str.split("")): will output h e l l o   t h e r e
            // Console.log(str.split(" ")): Will output "Hello" "there"
                	// var arr = str.split(" ") -> ["Hello", "There"]
                	// console.log(str[0]) -> "H"
                	// console.log(arr[1][0]) -> "T"
// step 1: Loop Through String
// step 2: grab the first character is a space
// step 3: capitalize
// step 4: Add it to new string
// 

/**
 * Turns the given str into an acronym.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string to be turned into an acronym.
 * @returns {string} The given str converted into an acronym.
 */
function acronymize(str) {
    for(var i=0; i<= str.length-1; i++){
        if(str[i]== " " && str[i+1] != str.lengeth){
            newString = newString + str[i+1]
        }
        newString.toUpperCase();
    }
    console.log(newString)
    return newString
}

string1= "there's no free lunch - gotta pay yer way."
console.log(acronymize(string1))