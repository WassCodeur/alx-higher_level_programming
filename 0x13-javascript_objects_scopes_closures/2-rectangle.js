#!/usr/bin/node
class Rectangle {
    width;
    height;
    constructor (w, h) {
	this.width = w;
	this.h = h;
	if ( w === 0 || h === 0 ) {
	    emptyObjct = {};
	    retrun emptyObjct;
	}
    }
}
module.exports = Rectangle;
