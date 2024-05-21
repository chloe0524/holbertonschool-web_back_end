export default (students) => (Array.isArray(students) ? students.map((student) => student.id) : []);
