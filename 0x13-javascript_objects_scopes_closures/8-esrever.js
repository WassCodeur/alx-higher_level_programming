#!/usr/bin/node
exports.esrever = function (list) {
  const revArray = [];
  let len = list.length - 1;
  while (len >= 0) {
    revArray.push(list[len]);
    len--;
  }
  return revArray;
};
