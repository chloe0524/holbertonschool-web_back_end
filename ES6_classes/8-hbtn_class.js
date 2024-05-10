/* eslint-disable */
export default class HolbertonClass {
    constructor(size, location) {
      this._size = 'Number';
      this._location = 'String';
      
      this._size = size;
      this._location = location;
    }

    toString(){
      return `${this._location}`;
    }
    valueOf() { 
      return `${this._size}`;
    }
};