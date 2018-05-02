'use strict';
//tests for the anagram detector

const anagram = require("./anagram-lazy.js");
const ok = require("assert").ok;

ok(anagram("anagram", "nagaram") === true);
ok(anagram("green", "egern") === true);
ok(anagram("abcd", "abcd") === true);
ok(anagram("egg", "bacon") === false);
