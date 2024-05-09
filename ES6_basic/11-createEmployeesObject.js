export default (departmentName, employees) => {
  return {
    [departmentName]: Array(employees),
  };
}
