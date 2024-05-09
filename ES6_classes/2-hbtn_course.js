/* eslint-disable */
export default class HolbertonCourse {
  constructor(name, length, students) {
    this.name = 'string';
    this.length = 0;
    this.students = [];

    this.name = name;
    this.length = length;
    this.students = students;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value !== 'string') throw TypeError('Name must be a string');
    this._name = value;
  }

  get length() {
    return this._length;
  }

  set length(value) {
    if (typeof value !== 'number') throw TypeError('Length must be a number');
    this._length = value;
  }

  get students() {
    return this._students;
  }

  set students(newStudents) {
    if (!Array.isArray(newStudents) || newStudents.some((student) => typeof student !== 'string')) {
      throw TypeError('Students must be an array of strings');
    }
    this._students = newStudents;
  }
}
