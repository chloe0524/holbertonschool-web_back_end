/* eslint-disable */
export default function createIteratorObject(report) {
  const employees = Object.values(report.allEmployees).flat();

  return employees[Symbol.iterator]();
};