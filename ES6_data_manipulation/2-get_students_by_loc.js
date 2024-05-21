/*eslint-disable*/
export default (students, city) => (Array.isArray(students) ? students.filter((student) => student.location === city) : []);