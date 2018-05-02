
module.exports = (a, b) => `${a}`.split('').sort().join('') === `${b}`.split('').sort().join('');
//basically sorts each string, then compares them
//uses string templating as a cheap hack to force string conversion
