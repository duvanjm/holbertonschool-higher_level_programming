#!/usr/bin/node

exports.esrever = function (list) {
  let rev = list.length - 1;
  for (let i = 0; i < rev; i++, rev --) {
    const li = list[i];
    list[i] = list[rev];
    list[rev] = li;
  }
  return (list);
}
