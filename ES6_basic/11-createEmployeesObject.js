export default function createEmployeesObject(departmentName, employees) {
  return {
    [departmentName]: Array(employees),
  };
}
