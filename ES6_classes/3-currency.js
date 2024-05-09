/* eslint-disable */
export default class HolbertonCourse {
  constructor(name, code) {
    this.name = 'string';
    this.code = 'string';

    this.name = name;
    this.code = code;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value !== 'string') throw TypeError('Name must be a string');
    this._name = value;
  }

  get code() {
    return this._code;
  }

  set code(value) {
    if (typeof value !== 'string') throw TypeError('Code must be a string');
    this._code = value;
  }

  displayFullCurrency() {
    return `${this.code} (${this.name})`;
  }
}
