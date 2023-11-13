// max of three numbers
function getMax(x, y, z) {
    return Math.max(x, y, z);
}

// min of three numbers
function getMin(x, y, z) {
    return Math.min(x, y, z);
}

// get the mean of three numbers
function getMean(x, y, z) {
    return (x + y + z) / 3;
}

// compare two words
function compare(word1, word2) {
    if (word1 === word2) {
        return 0;
    } else if (word1 > word2) {
        return 1;
    } else {
        return -1;
    }
}

// get characters per line with optional indentation
function getCharPerLine(str, indent) {
    let result = '';
    for (let i = 0; i < str.length; i++) {
        if (str[i] !== ' ') {
            result += (indent ? ' '.repeat(i) : '') + str[i] + '\n';
        }
    }
    return result;
}

// create a right-pointing arrow
function arrow(size) {
    let result = '';
    for (let i = 1; i <= size; i++) {
        result += '*'.repeat(i) + '\n';
    }
    for (let i = size - 1; i > 0; i--) {
        result += '*'.repeat(i) + '\n';
    }
    return result;
}