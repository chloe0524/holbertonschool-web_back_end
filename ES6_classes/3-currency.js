/* eslint-disable */
export default class HolbertonCourse {
  constructor(code, name) {
    this.name = 'string';
    this.code = 'string';

    this.code = code;
    this.name = name;
  }

  get code() {
    return this._code;
  }

  set code(value) {
    if (typeof value !== 'string') throw TypeError('Code must be a string');
    this._code = value;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value !== 'string') throw TypeError('Name must be a string');
    this._name = value;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
