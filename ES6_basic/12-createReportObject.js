export default (employeesList) => ({
  allEmployees: employeesList,
  getNumberOfDepartments: () => Object.keys(employeesList).length,
});
