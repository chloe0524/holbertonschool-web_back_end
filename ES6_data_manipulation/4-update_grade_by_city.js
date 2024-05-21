/*eslint-disable*/
export default (students, city, newGrades) => (Array.isArray(students) ? students.filter((student) => student.location === city)
  .map((student) => {
    const gradeObj = newGrades.find((grade) => grade.studentId === student.id);
    return { ...student, grade: gradeObj ? gradeObj.grade : 'N/A' };
  }) : []);