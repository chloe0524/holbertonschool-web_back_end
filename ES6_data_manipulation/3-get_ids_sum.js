/*eslint-disable*/
export default (students) => (Array.isArray(students) ? students.reduce((sum, student) => sum + student.id, 0) : 0);